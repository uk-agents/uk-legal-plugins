#!/usr/bin/env python3
"""
Journey eval runner for uk-legal-plugins.

Drives a multi-turn new-user journey headlessly through `claude -p` against a
SANDBOXED HOME, so a "fresh install" is real and repeatable, then asserts on
two surfaces:

  1. filesystem side-effects  (deterministic) -- did cold-start actually write
     the practice profile + shared company-profile.md, with the right content?
  2. transcript text          (heuristic)     -- did the second plugin read the
     shared profile instead of re-asking the company questions?

This is the layer the per-skill manifest.json cannot reach: the journey's
correctness lives in files on disk and in cross-turn state, not in a single
tool call.

Usage:
    python3 evals/journey/run_journey.py evals/journey/cold-start-shared-profile.json
    python3 evals/journey/run_journey.py <spec.json> --model claude-haiku-4-5-20251001 --keep

Auth: symlinks your real ~/.claude/.credentials.json into the sandbox, so no
API key env is required. Nothing is written to your real ~/.claude config.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REAL_HOME = Path.home()
REPO_ROOT = Path(__file__).resolve().parents[2]

GREEN, RED, YELLOW, DIM, BOLD, RESET = (
    "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[1m", "\033[0m"
)


def make_sandbox() -> Path:
    sbx = Path(tempfile.mkdtemp(prefix="uklegal-journey-"))
    (sbx / ".claude").mkdir(parents=True)
    creds = REAL_HOME / ".claude" / ".credentials.json"
    if creds.exists():
        os.symlink(creds, sbx / ".claude" / ".credentials.json")
    else:
        print(f"{YELLOW}warn:{RESET} no ~/.claude/.credentials.json; relying on "
              f"ANTHROPIC_API_KEY in the environment.")
    settings = REAL_HOME / ".claude" / "settings.json"
    if settings.exists():
        shutil.copy(settings, sbx / ".claude" / "settings.json")
    return sbx


def run_turn(sbx: Path, plugin_dir: str, prompt: str, model: str, timeout: int) -> dict:
    """Run one headless turn. Returns the parsed --output-format json result."""
    env = dict(os.environ, HOME=str(sbx))
    env.pop("ANTHROPIC_API_KEY", None) if (sbx / ".claude" / ".credentials.json").exists() else None
    cmd = [
        "claude", "-p", prompt,
        "--model", model,
        "--plugin-dir", str(REPO_ROOT / plugin_dir),
        "--permission-mode", "bypassPermissions",
        "--output-format", "json",
    ]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=timeout)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"is_error": True, "result": proc.stdout[-2000:] + "\n[STDERR]\n" + proc.stderr[-1000:]}


# ---- assertion primitives --------------------------------------------------

def _resolve(sbx: Path, config_root: str, rel: str) -> Path:
    return sbx / config_root / rel


def check_fs(sbx: Path, config_root: str, a: dict, snapshots: dict) -> tuple[bool, str]:
    t = a["type"]
    p = _resolve(sbx, config_root, a["path"]) if "path" in a else None
    if t == "file_exists":
        return p.exists(), f"exists {a['path']}" if p.exists() else f"MISSING {a['path']}"
    if not p or not p.exists():
        return False, f"cannot check {t}: {a['path']} does not exist"
    body = p.read_text(errors="replace")
    if t == "file_contains":
        ok = a["text"] in body
        return ok, f"{'contains' if ok else 'MISSING text'} {a['text']!r} in {a['path']}"
    if t == "file_contains_any":
        hit = next((x for x in a["text"] if x in body), None)
        return hit is not None, (f"found {hit!r}" if hit else f"none of {a['text']} in {a['path']}")
    if t == "placeholder_count_below":
        # Count only genuinely-unfilled [PLACEHOLDER markers. [DEFAULT markers are
        # EXPECTED in quick-start (the skill fills sensible defaults and tags them
        # for later tuning) -- counting them would flag correct behavior as failure.
        n = len(re.findall(r"\[PLACEHOLDER", body))
        return n < a["max"], f"{n} [PLACEHOLDER markers (max {a['max']}) in {a['path']}"
    if t == "default_markers_present":
        # Proves quick-start actually defaulted the sections it could, rather than
        # leaving the raw template untouched (unwritten template has 0 [DEFAULT).
        n = len(re.findall(r"\[DEFAULT", body))
        return n >= a["min"], f"{n} [DEFAULT markers (need >= {a['min']}) in {a['path']}"
    if t == "file_unchanged_since":
        prev = snapshots.get(a["since_turn"], {}).get(a["path"])
        if prev is None:
            return False, f"no snapshot of {a['path']} from {a['since_turn']} (it was never written)"
        return prev == body, f"{'unchanged' if prev == body else 'CHANGED'} since {a['since_turn']}"
    return False, f"unknown fs assertion {t}"


def check_transcript(result_text: str, a: dict) -> tuple[bool, str]:
    t = a["type"]
    low = result_text.lower()
    if t == "must_contain_any":
        hit = next((x for x in a["text"] if x.lower() in low), None)
        return hit is not None, (f"found {hit!r}" if hit else f"none of {a['text']}")
    if t == "must_not_contain_any":
        hit = next((x for x in a["text"] if x.lower() in low), None)
        return hit is None, (f"clean" if hit is None else f"CONTAINS forbidden {hit!r}")
    return False, f"unknown transcript assertion {t}"


# ---- driver ----------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--model", default=None, help="override spec model")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--keep", action="store_true", help="keep the sandbox for inspection")
    args = ap.parse_args()

    spec = json.loads(Path(args.spec).read_text())
    model = args.model or spec.get("model", "claude-haiku-4-5-20251001")
    config_root = spec["config_root"]

    sbx = make_sandbox()
    print(f"{BOLD}journey:{RESET} {spec['journey']}   {DIM}model={model}  sandbox={sbx}{RESET}\n")

    snapshots: dict[str, dict] = {}   # turn_id -> {rel_path: body_at_end_of_turn}
    total_passed = total = 0
    turn_lines = []

    for turn in spec["turns"]:
        tid = turn["id"]
        print(f"{BOLD}-> turn {tid}{RESET} {DIM}(plugin_dir={turn['plugin_dir']}){RESET}")
        res = run_turn(sbx, turn["plugin_dir"], turn["prompt"], model, args.timeout)
        result_text = res.get("result", "") or ""
        if res.get("is_error"):
            print(f"   {RED}run errored{RESET}: {result_text[:300]}")

        # snapshot every path this journey cares about, for later unchanged-since checks
        snap = {}
        for other in spec["turns"]:
            for a in other.get("fs_assertions", []):
                rp = a.get("path")
                if rp:
                    fp = _resolve(sbx, config_root, rp)
                    if fp.exists():
                        snap[rp] = fp.read_text(errors="replace")
        snapshots[tid] = snap

        results = []
        for a in turn.get("fs_assertions", []):
            ok, detail = check_fs(sbx, config_root, a, snapshots)
            results.append((ok, "fs ", detail, a.get("why", "")))
        for a in turn.get("transcript_assertions", []):
            ok, detail = check_transcript(result_text, a)
            results.append((ok, "txt", detail, a.get("why", "")))

        for ok, kind, detail, why in results:
            mark = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
            print(f"   [{mark}] {kind} {detail}")
            if not ok and why:
                print(f"          {DIM}{why}{RESET}")
        p = sum(1 for ok, *_ in results if ok)
        total_passed += p
        total += len(results)
        turn_lines.append(f"  {tid}: {p}/{len(results)}")
        print()

    print(f"{BOLD}scorecard{RESET}")
    for line in turn_lines:
        print(line)
    color = GREEN if total_passed == total else (YELLOW if total_passed else RED)
    print(f"{BOLD}total: {color}{total_passed}/{total}{RESET}\n")

    if args.keep:
        print(f"{DIM}sandbox kept: {sbx}{RESET}")
    else:
        shutil.rmtree(sbx, ignore_errors=True)

    sys.exit(0 if total_passed == total else 1)


if __name__ == "__main__":
    main()
