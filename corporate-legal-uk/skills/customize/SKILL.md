---
name: customize
description: >
  Guided customisation of your corporate practice profile — change one thing
  without re-running the whole cold-start interview. Adjust risk posture,
  escalation contacts, active modules (M&A / Board & Secretary / Public Company /
  Entity Management), materiality thresholds, disclosure schedule format, written
  resolution precedents, or matter workspace paths. Use when the user says
  "change my [thing]", "update my profile", "edit my config", or "customise".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/corporate-legal-uk:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a module
toggle, an output format — without re-running the whole cold-start interview
and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`
   (and `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/corporate-legal-uk:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions (E&W / Scotland / NI), stage
     (Ltd / plc / AIM-listed / subsidiary), practice setting *(shared across plugins —
     changes flow through `company-profile.md`)*
   - **Active modules** — which of M&A, Board & Secretary, Public Company,
     Entity Management are on. Turning a module on/off changes which skills
     prompt for setup.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for diligence materiality and disclosure schedule scope
   - **People** — deal team, board secretary / company secretary, entity
     management owner, escalation chain (solicitors / GC / board)
   - **M&A module** — materiality thresholds (contract value in £, headcount,
     revenue), VDR platforms trusted, AI bulk-review trust level
     (Luminance / Kira), deal team briefing cadence, completion mechanism
     preference (locked-box / completion accounts)
   - **Board & Secretary module** — house written resolution format, resolution
     language ("IT IS RESOLVED THAT" vs "RESOLVED THAT"), signatory
     preferences, committee structure
   - **Public Company module** — FCA/AIM disclosure calendar, PDMR/PCA
     notification process, UK MAR Art. 17 delay-to-disclosure procedure
   - **Entity Management module** — entity table, Companies House filing
     calendar, PSC register update cadence, charge registration reminders
   - **Workflow** — matter workspaces (deal rooms), closing checklist
     location, VDR watcher cadence
   - **Integrations** — Box / Datasite / iManage / Slack status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Materiality threshold £250k → £500k:* "`/diligence-issue-extraction`
     and `/material-contract-schedule` will now treat £500k as the cutoff.
     Existing findings stay as logged; re-run if you want the new threshold
     applied retroactively."
   - *Turning on the Public Company module:* "I'll prompt you for FCA/AIM
     disclosure calendar and PDMR notification controls next time you run
     anything in that area."
   - *AI bulk-review trust "check every row" → "spot-check 10%":* "`/ai-tool-
     handoff` will QA a 10% sample rather than every extraction."
   - *Completion mechanism locked-box → completion accounts:* "The closing-
     checklist skill will use completion accounts mechanics when building
     the checklist. Locked-box leak protections will no longer be the default."
   - *Adding Scotland to jurisdiction footprint:* "Skills will now flag
     Scottish-specific differences (dual charge registration, Scots law
     property rules, Scottish court proceedings) for entities and deals
     with Scottish connections."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` and note:

   > This change affects all plugins in this suite — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/corporate-legal-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behaviour.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., Public Company module off + "FCA counsel" in
  escalation; or aggressive risk posture + £25k materiality threshold; or
  plc entity type but CA2006 s.281(2) written resolution limits not noted), flag
  the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags on retrieved documents, and `[verify]` tags on cited authorities are
  load-bearing — explain the trade-off before removing.
- **One change at a time.** Don't re-ask the whole interview.
