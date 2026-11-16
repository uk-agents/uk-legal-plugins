# Journey evals

The manifest in [`../manifest.json`](../manifest.json) tests **skills in isolation** —
one prompt, one assertion: "does prompt X trigger skill Y and call tool Z." That
misses the thing a real user actually experiences: a **stateful, multi-turn journey**
whose correctness lives in files on disk and in cross-turn memory, not in a single
tool call.

A journey eval drives that path headlessly through `claude -p` against a **sandboxed
HOME** (so "fresh install" is real and repeatable) and asserts on two surfaces:

1. **Filesystem side-effects** (deterministic) — did cold-start actually *write* the
   practice profile and the shared `company-profile.md`, with the right content?
2. **Transcript text** (heuristic) — did the second plugin *read* the shared profile
   instead of re-asking the company questions?

## The new-user journey, staged

| Stage | What happens | Assertable via |
|---|---|---|
| 1. Install | user installs a plugin | (out of scope for this slice) |
| 2. Cold start | `/cold-start-interview` writes a populated practice profile | filesystem |
| 3. Shared profile | first plugin writes `company-profile.md`; **second plugin reads it and does NOT re-ask** | filesystem + transcript |
| 4. First real task | a real skill reads the profile, applies guardrails, calls MCP, doesn't fabricate | transcript + judge *(not yet built)* |
| 5. Cross-cutting discipline | anti-fabrication under empty MCP, jurisdiction recognition, irreversibility gates | transcript + judge *(not yet built)* |
| 6. Matter workspace | new/switch/close; matter A never reads matter B | filesystem *(not yet built)* |

This slice implements **stages 2–3** ([`cold-start-shared-profile.json`](cold-start-shared-profile.json)).

## Running

```bash
python3 evals/journey/run_journey.py evals/journey/cold-start-shared-profile.json
# options:
#   --model claude-haiku-4-5-20251001   (default; the model under test)
#   --keep                              (keep the sandbox dir for inspection)
#   --timeout 300                       (per-turn seconds)
```

Exit code is `0` only when every assertion passes. Output is a per-turn scorecard.

**Auth & isolation.** The runner symlinks your real `~/.claude/.credentials.json`
into a throwaway `HOME` sandbox, so no API key env is needed and **nothing is written
to your real `~/.claude` config.** Each run starts from a genuinely empty config.

## Assertion types

| Type | Surface | Meaning |
|---|---|---|
| `file_exists` | fs | path exists under the sandbox config root |
| `file_contains` / `file_contains_any` | fs | substring present |
| `placeholder_count_below` | fs | fewer than N `[PLACEHOLDER` markers (a run that did nothing leaves the full template's worth) |
| `default_markers_present` | fs | at least N `[DEFAULT` markers — proves quick-start actively filled defaults |
| `file_unchanged_since` | fs | file identical to its snapshot at the end of an earlier turn (shared profile not clobbered) |
| `must_contain_any` | txt | transcript mentions at least one expected string |
| `must_not_contain_any` | txt | transcript contains none of the forbidden strings (e.g. re-asked questions) |

`[PLACEHOLDER` vs `[DEFAULT` matters: quick-start is *supposed* to leave `[DEFAULT — …]`
markers on sections it sensibly defaulted (tagged for later tuning). Only `[PLACEHOLDER`
means genuinely unfilled. The unwritten template has 29 `[PLACEHOLDER` / 0 `[DEFAULT`;
a correct quick-start leaves ~12 `[PLACEHOLDER` / ~20 `[DEFAULT`.

## Findings so far (model under test: haiku)

- **cold-start persistence is flaky.** Across runs of the identical turn-1 prompt,
  the model sometimes writes both config files correctly and sometimes narrates a
  completed setup ("The configuration will get better as you use it…") while writing
  **nothing** to disk — the config directory is never created and the company name
  appears only in the session transcript. This is the exact "said it did, didn't do
  it" failure a single-turn triggering eval cannot see.
- **Implication:** a journey eval should be run **N times for a pass-rate**, not once.
  A single green run does not mean the journey is reliable. (A `--repeat N` mode and
  an LLM-judge for stages 4–5 are the natural next extensions.)
