# CLAUDE.md

Guidance for working on this repo. `uk-legal-plugins` is a UK-jurisdiction
legal plugin marketplace — 11 plugins, 140+ skills. Most work here is editing
prompt content (skills, agents, hooks) or plugin metadata — not application code.

## Target ecosystems

These plugins reach **three** MCP-speaking client ecosystems via dual-manifest packaging (`.claude-plugin/plugin.json` + `.codex-plugin/plugin.json` per plugin, sharing the same `skills/` + `.mcp.json`):

| Ecosystem | Audience | Reaches via |
|---|---|---|
| Claude Code | Developer + lawyer-developers | `.claude-plugin/plugin.json` |
| Cowork (Anthropic) | Anthropic collaborative env | Same as Claude Code |
| OpenAI Codex CLI | OpenAI developer audience | `.codex-plugin/plugin.json` |

ChatGPT consumer (~80M/week) is NOT reachable through these plugins — ChatGPT supports MCP tools only, no skills, no resources, no prompts. ChatGPT users connect directly to `uk-legal-mcp.fly.dev/mcp`; for them, the MCP server's tool descriptions are the only workflow-teaching layer. See `uk-legal-mcp/docs/chatgpt-workflow-encoding.md` (in the sibling repo).

## Documentation index

In `docs/`:

- [`SPEC.md`](docs/SPEC.md) — pre-existing specification
- [`skill-gaps-and-design.md`](docs/skill-gaps-and-design.md) — 5 new skills closing the dogfeed-failure workflows (find-member-contribution, find-case-by-party-verify, oscola-build-citation, statute-amendments-trace, bill-debate-trace)
- [`distribution-strategy.md`](docs/distribution-strategy.md) — distribution decision (Option C1: single free public repo), dual-manifest plugin pattern, future revenue paths (recorded; not implemented)

## Layout

```
.claude-plugin/marketplace.json   # the marketplace manifest — one entry per plugin
<plugin>/                         # 11 plugins (employment-legal-uk, privacy-legal-uk, ...)
  .claude-plugin/plugin.json      # plugin manifest (name, version, description, author)
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (see "Plugin CLAUDE.md" below)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  agents/<name>.md                # subagent definitions
  hooks/hooks.json                # hook config (most plugins ship an empty stub)
  .gitignore
references/                       # shared templates read by cold-start and dashboard skills
  company-profile-template.md     # shape of ~/.claude/plugins/config/uk-legal-plugins/company-profile.md
  dashboard-template.md           # rendering standard for HTML/terminal/Excel dashboard outputs
```

## Validation — run before opening a PR

This repo follows the same conventions `anthropics/claude-plugins-official`
enforces in CI. Run the equivalent checks locally:

```bash
# 1. Marketplace + per-plugin schema validation (source of truth)
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done

# 2. JSON sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
```

### Marketplace invariants (I1–I11)

`claude-plugins-official` layers these on top of the schema check. They apply
here too — the ones most likely to trip a contributor:

- **I1** — `plugins[]` should be alpha-sorted by name (case-insensitive).
  *Currently a known warning: the array is in a curated display order. If you
  add a plugin, ask before re-sorting the whole array.*
- **I2** — no duplicate plugin names.
- **I3** — `description` 10–2000 chars, no leading/trailing whitespace.
- **I8** — every vendored `source` (`"./<dir>"`) must point at a directory that
  contains `.claude-plugin/plugin.json`.
- **I9** — `source` paths/URLs must contain no shell metacharacters or `..`.
- **I10** — no hidden Unicode (zero-width chars, bidi controls) in
  `name`/`description`.
- **I11** — `name` must match `^[a-z0-9][a-z0-9-]{1,63}$`.

### Frontmatter requirements

Every `agents/*.md` needs `name` and `description`. Every
`skills/<name>/SKILL.md` needs `description`. Every `commands/*.md` needs
`description`. Multi-line descriptions use `>` block scalars and that's fine —
`claude plugin validate` parses them correctly.

## Skill authoring conventions

### MCP-native skill pattern (reference: `regulatory-legal-uk:reg-feed-watcher`)

Skills that interact with `uk-legal-mcp` (or any other MCP server in `.mcp.json`) follow five characteristics, taken from `regulatory-legal-uk:reg-feed-watcher` which is the reference template:

1. **"Pushy" trigger description.** YAML frontmatter `description:` opens with "USE WHEN the user says X / asks Y" — concrete user phrases. Agents systematically under-trigger when the description is passive ("a skill for searching"). Use `skill-creator`'s description-optimization loop on every new skill.

2. **MCP tools named verbatim in prose.** Skill instructions write actual tool names: "Call `parliament_find_member(name)` to get the member_id." Not "look up the member." The agent matches actual tool names — named-verbatim wins.

3. **Source-tagged outputs.** Skill output instructs the agent to tag claims with their source: `[uk-legal MCP — Hansard]`, `[uk-legal MCP — legislation.gov.uk]`, `[govuk MCP]`, `[model knowledge — verify]`. Tags propagate to the user's final response so provenance is visible.

4. **"No silent supplement" anti-fabrication clause.** Every MCP-interacting skill includes language to the effect of: *"If a uk-legal MCP tool returns empty or errored, do NOT supplement from training data or web search. Report the empty result with `next_steps` / `detail` surfaced; ask the user for clarification rather than fabricating a plausible answer."* This tightens against confabulation under empty results (see `~/.claude/skill-observations/log.md` Obs 183).

5. **Tier structure where applicable.** Tier 1 (authoritative MCP), Tier 2 (gov MCP), Tier 3 (broader feeds). Teach the agent WHEN to escalate sources, not just WHICH sources exist.

### Content discipline — neutral procedural templates only

All skills (and all tool descriptions in `uk-legal-mcp`) must be **NEUTRAL PROCEDURAL TEMPLATES**, NOT OPINIONATED ADVOCACY.

| Acceptable | Not acceptable |
|---|---|
| "Workflow for retrieving what a peer said in a Hansard debate" | "Workflow for constructing a landlord's strongest defence argument" |
| "USE WHEN the user asks for tenancy-related case law" | "USE WHEN defending a tenant in housing court" |
| Skill flags `[UNCERTAIN]` for non-primary-source content | Skill recommends specific litigation positions or arguments |

The free public connector is reachable by ~80M casual ChatGPT users who may misread legal-position framing as actual legal advice. Existing 140 skills already follow this discipline (e.g. `law-student-uk:case-brief` and `legal-clinic-uk:research-start` flag `[UNCERTAIN]` / `[VERIFY]`); new skills must maintain it.

### Skill authoring procedure

Use **Anthropic's `skill-creator`** skill (canonical, at `~/.claude/skills/skill-creator/`) — NOT one of the user's custom skill-creation packs. The Anthropic skill walks through: capture intent → draft SKILL.md → 2-3 test prompts → run claude-with-skill + baseline → evaluate via the eval-viewer → iterate → optimise description for triggering.

## Conventions

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and
`author` should match the plugin's own `.claude-plugin/plugin.json` field for
field. If you change a plugin's description in one place, change it in the
other.

### Skill names in prose must be canonical

When a `SKILL.md` (especially `customize` or `cold-start-interview`) tells the
user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.
Short forms like `/triage` for `/use-case-triage` look right in prose but are
dead commands — the user types them and nothing happens. Refs to Claude Code
built-ins (`/mcp`, `/plugin`) and to other plugins (`/<other-plugin>:<skill>`)
are fine.

### Plugin CLAUDE.md is a template, not project context

Each `<plugin>/CLAUDE.md` is a practice-profile template that the
`cold-start-interview` skill copies to `~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md`
on the user's machine. It is *not* loaded as project context when the plugin is
installed — `claude plugin validate` warns about this and the warning is
expected. Don't "fix" it by moving the content into a skill.

### Formatting

- 2-space indent in all JSON and `.mcp.json` files.
- Final newline at end of every text file.
- No trailing whitespace.
- Markdown tables: pipe-aligned columns are nice but not required; just keep
  the column count consistent.

## Things to leave alone

- Per-plugin `.gitignore` files differ slightly across plugins. Probably
  intentional; ask before unifying.
- `hooks/hooks.json` is missing in two plugins. Hooks are optional; the missing
  files are not a bug.
