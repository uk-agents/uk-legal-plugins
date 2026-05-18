---
name: matter-workspace
description: Manage matter workspaces — create, list, switch, close, or detach the active matter (practice-level). Use when working across multiple UK clients or matters and you need to keep one engagement's context separate from another, or when a substantive skill needs to know which matter it's working in.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple UK clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This skill manages those workspaces.

## Subcommands

- `/regulatory-legal-uk:matter-workspace new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `/regulatory-legal-uk:matter-workspace list` — list matters with status and active flag
- `/regulatory-legal-uk:matter-workspace switch <slug>` — set the active matter
- `/regulatory-legal-uk:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/_archived/`, never delete)
- `/regulatory-legal-uk:matter-workspace none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one company, so the plugin works from practice-level context automatically. If you actually work across multiple clients, re-run `/regulatory-legal-uk:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Use the file-management logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/<slug>/matter.md`, seed `history.md` and `notes.md`.
   - `list` → enumerate `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/<slug>/` to `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes. UK SRA retention requirements may apply.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

Multi-client practitioners (private practice — solicitors' firm, barrister's chambers, in-house regulatory counsel advising related companies) work across many UK client matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; it explains the disabled state.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/
├── CLAUDE.md                       # practice-level practice profile
└── matters/
    ├── <slug>/
    │   ├── matter.md               # client, counterparty, matter type, key facts, overrides
    │   ├── history.md              # dated log of events, decisions, drafts, reviews
    │   ├── notes.md                # free-form working notes
    │   └── outputs/                # skill outputs for this matter (optional subfolder)
    └── _archived/
        └── <slug>/                 # closed matters — readable but not active
```

Slugs are lowercase with hyphens. Examples: `acme-fca-enquiry-2026`, `zenith-osa-compliance`, `vendor-xyz-dpa-gap`.

## Active matter is in the practice CLAUDE.md

The `Active matter:` line under `## Matter workspaces` in the practice-level CLAUDE.md is the single source of truth. Switching a matter edits that line. No separate state file.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/` or `matters/_archived/<slug>/`. If reused, ask the user to pick a different slug.
2. Run the intake interview:
   - **Client** (the party we represent, or the internal business unit if in-house)
   - **Matter type** (for regulatory-legal-uk: FCA enquiry | FCA CP response | ICO investigation | CMA investigation | Ofcom enforcement | gap remediation | SI commencement | standing topic | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings)
   - **UK jurisdiction(s)** (England & Wales | Scotland | Northern Ireland | UK-wide — matters may have different extents)
   - **Key facts** (2–5 sentences: what this matter is about, who the stakeholders are, what's at stake)
   - **Matter-specific overrides to the practice playbook** (e.g., "FCA has issued a Section 166 notice — outputs must not be shared outside the investigation team", "client is jointly regulated by FCA and PRA")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/regulatory-legal-uk:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | UK jurisdiction | Status | Opened | Active |
|---|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/regulatory-legal-uk:matter-workspace new <slug>`.
2. Edit the `Active matter:` line in the practice-level CLAUDE.md to `Active matter: <slug>`.
3. Show the user the matter.md summary so they can confirm they're on the right matter.

### `close <slug>`

1. Confirm `matters/<slug>/` exists.
2. Append a "Closed" entry to `matters/<slug>/history.md` with today's date.
3. Move `matters/<slug>/` → `matters/_archived/<slug>/`.
4. If the closed matter was the active matter, set `Active matter:` to `none — practice-level context only`.

### `none`

Set `Active matter:` in the practice-level CLAUDE.md to `none — practice-level context only`. Confirm with the user.

## `matter.md` template

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this` in the practice-level CLAUDE.md]

# Matter: [Client] — [short description]

**Slug:** [slug]
**Opened:** [YYYY-MM-DD]
**Status:** active
**UK jurisdiction:** [England & Wales | Scotland | Northern Ireland | UK-wide]
**Confidentiality:** [standard / heightened / clean-team]

---

## Parties

**Client:** [name]
**Regulator / counterparty:** [name(s)]

## Matter type

[FCA enquiry | FCA CP response | ICO investigation | CMA investigation | Ofcom enforcement | gap remediation | SI commencement | standing topic | other — with one-line rationale]

## Key facts

[2–5 sentences. What this matter is about. Who the stakeholders are. What's at stake. What makes it different from the default playbook.]

## Matter-specific overrides

*Any deviation from the practice-level playbook that applies to this matter and only this matter.*

- [e.g., "FCA s.166 notice in force — do not share outputs outside investigation team."]
- [e.g., "Jointly regulated by FCA and PRA — check both Handbooks for every gap."]
- [e.g., "Client requires OSCOLA citations throughout, not house-style abbreviations."]

## Related matters

- [slug — one line why related]

## Notes on confidentiality

[If heightened or clean-team, describe why. Who may see matter files. Whether cross-matter context is permissible even if globally on.]
```

## `history.md` seed

```markdown
# History: [Client] — [short description]

Append-only event log. Most recent at top.

---

## [YYYY-MM-DD] — Matter opened

Intake completed. Slug: `[slug]`. Status: active. UK jurisdiction: [jurisdiction].
[Any initial context worth preserving beyond matter.md.]
```

## Cross-matter context

The practice-level CLAUDE.md has a `Cross-matter context:` flag. When it's `off` (the default), a skill working in matter A **never reads** files in `matters/B/` for any other `B`. Period. This is the confidentiality guarantee the setting exists to provide.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's / firm's job (SRA Code of Conduct r. 6.1); the intake captures what the user declares.
- **Enforce retention.** Closing archives a matter; it does not delete. UK SRA retention requirements and GDPR retention periods are out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active.
