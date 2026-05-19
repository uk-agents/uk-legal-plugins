# CLAUDE.md

Guidance for working on this repo. `uk-legal-plugins` is a Claude Code plugin
marketplace — 11 UK-jurisdiction legal plugins. Most work here is editing
prompt content (skills, agents, hooks) or plugin metadata — not application code.

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
- Several plugin `CLAUDE.md` templates reference `references/` at repo root as if it were bundled inside the plugin directory. That's a known gap — don't silently move the files.
