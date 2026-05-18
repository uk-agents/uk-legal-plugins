---
name: matter-workspace
description: >
  Manage matter workspaces — create, list, switch, close, or detach (practice-level).
  Keeps one client or engagement's context separate from every other for multi-client
  practitioners. Use when the user wants to open a new matter, switch matters, list
  matters, close/archive a matter, or work at practice-level only.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This skill manages those workspaces.

## Subcommands

- `/privacy-legal-uk:matter-workspace new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `/privacy-legal-uk:matter-workspace list` — list matters with status and active flag
- `/privacy-legal-uk:matter-workspace switch <slug>` — set the active matter
- `/privacy-legal-uk:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/_archived/`, never delete)
- `/privacy-legal-uk:matter-workspace none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one organisation, so the plugin works from practice-level context automatically. If you actually work across multiple clients (e.g., a law firm, DPO-as-a-service, privacy consultancy), re-run `/privacy-legal-uk:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Use the subcommand logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/<slug>/matter.md`, seed `history.md` and `notes.md`.
   - `list` → enumerate `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/<slug>/` to `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention and conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

# Matter Workspace

Multi-client practitioners (private practice — solo, small firm, large firm; DPO-as-a-service; privacy consultancy) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; the workflow above explains the disabled state and suggests `/privacy-legal-uk:cold-start-interview --redo` for users who actually need matter isolation.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/
├── CLAUDE.md                       # practice-level practice profile
└── matters/
    ├── <slug>/
    │   ├── matter.md               # client, engagement, matter type, key facts, overrides
    │   ├── history.md              # dated log of events, decisions, drafts, reviews
    │   ├── notes.md                # free-form working notes
    │   └── outputs/                # skill outputs for this matter (optional subfolder)
    └── _archived/
        └── <slug>/                 # closed matters — readable but not active
```

Slugs are lowercase with hyphens. Examples: `acme-dpia-2026`, `zenith-dsa-response`, `vendor-xyz-dpa`, `ico-enquiry-q4`.

## Active matter is in the practice CLAUDE.md

The `Active matter:` line under `## Matter workspaces` in the practice-level CLAUDE.md is the single source of truth. Switching a matter edits that line. No separate state file.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/` or `matters/_archived/<slug>/`. If reused, ask the user to pick a different slug.
2. Run the intake interview:
   - **Client** (the organisation we represent, or the internal business unit if in-house)
   - **Counterparty** (the other side — for a DPA review, the controller or processor; for a DSAR, the data subject; for an ICO enquiry, the ICO)
   - **Matter type** (for privacy-legal-uk: DPIA | DPA review | DSAR | ICO enquiry | privacy notice review | transfer mechanism review | personal data breach | Children's Code assessment | PECR compliance review | reg-gap-analysis | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings)
   - **Key facts** (2-5 sentences: what this matter is about, who the stakeholders are, what's at stake, whether there is any ICO involvement)
   - **Matter-specific overrides to the practice playbook** (e.g., "client requires 48-hour breach notification to controller not 72-hour"; "counterparty is a strategic partner — relationship-preserving tone"; "PECR is not in scope — B2B only")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/privacy-legal-uk:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/privacy-legal-uk:matter-workspace new <slug>`.
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
**Confidentiality:** [standard / heightened / clean-team]

---

## Parties

**Client:** [name]
**Counterparty:** [name(s) — controller / processor / data subject / ICO]

## Matter type

[DPIA | DPA review | DSAR | ICO enquiry | privacy notice review | transfer mechanism review | personal data breach | Children's Code assessment | PECR compliance | reg-gap-analysis | other — with one-line rationale]

## UK regulatory context

[Which UK regimes are directly in scope for this matter: UK GDPR / DPA 2018 / PECR / NIS / OSA / Children's Code / sector-specific. Note if EU GDPR also applies.]

## Key facts

[2-5 sentences. What this matter is about. Who the stakeholders are. What's at stake. Any ICO involvement. What makes it different from the default playbook.]

## Matter-specific overrides

*Any deviation from the practice-level playbook that applies to this matter only.*

- [e.g., "Breach notification: client requires 48-hour notification to controller (stricter than playbook standard)."]
- [e.g., "Tone: relationship-preserving — counterparty is a strategic partner."]
- [e.g., "Governing law: English law."]
- [e.g., "PECR not in scope — B2B processing only."]

## Related matters

- [slug — one line why related]

## Notes on confidentiality

[If heightened or clean-team, describe why. Who may see matter files. Whether cross-matter context is permissible even if globally on. Note: ICO enquiry matters should generally be heightened.]
```

## `history.md` seed

```markdown
# History: [Client] — [short description]

Append-only event log. Most recent at top.

---

## [YYYY-MM-DD] — Matter opened

Intake completed. Slug: `[slug]`. Status: active.
[Any initial context worth preserving beyond matter.md — e.g., "Opened in response to ICO information notice dated [date]." or "Opened for client DPIA re [processing activity]."]
```

## Cross-matter context

The practice-level CLAUDE.md has a `Cross-matter context:` flag. When it's `off` (the default), a skill working in matter A **never reads** files in `matters/B/` for any other `B`. This is the confidentiality guarantee the setting exists to provide.

When it's `on`, a skill may read files across matter folders only when the user explicitly asks (e.g., "compare our standard DPA position across the last five processor matters"). Even when `on`, the default is to load only the active matter unless the user asks for a cross-matter view.

**Note for ICO enquiry matters:** Cross-matter context should be off for any matter involving an ICO investigation or enforcement action. Information generated in response to one ICO enquiry should not accidentally surface in a different client's matter.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's / firm's job; the intake captures what the user declares.
- **Enforce retention.** Closing archives a matter; it does not delete. UK GDPR / DPA 2018 retention policy for client files is out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active, not what to put in it.
- **Decide whether cross-matter is appropriate.** It reads the flag and obeys.
