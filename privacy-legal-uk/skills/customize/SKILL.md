---
name: customize
description: >
  Guided customisation of your UK privacy practice profile — change one thing
  without re-running the whole cold-start interview. Adjust risk posture,
  escalation contacts, DPA playbook, privacy notice commitments, DPIA house
  style, DSAR process, or matter workspace paths. Use when the user says
  "change my [thing]", "update my profile", "edit my playbook", or
  "customise".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/privacy-legal-uk:customize`. They want to change something in
their UK privacy profile — a risk posture, an escalation contact, a DPA
position, a DPIA section, a DSAR timeline, a regulatory footprint item — without
re-running the whole cold-start interview and without hand-editing a file.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`
   (and `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/privacy-legal-uk:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting, controller vs. processor orientation *(shared across all plugins — changes flow through `company-profile.md`)*
   - **Risk posture** — conservative / middle / measured, what each means
     for processor obligations, Children's Code compliance, cross-border transfers, and retention
   - **People** — DPO, privacy team, DPO reporting line, engineering liaison, outside counsel,
     escalation chain including ICO contact protocol
   - **DPA playbook** — positions on sub-processor notice, deletion, audit,
     liability, international transfers (IDTA / UK Addendum / adequacy), breach notification to controller — as processor and as controller
   - **Privacy notice commitments** — the commitments your notice has made that `/policy-monitor` watches practice against; includes purposes and lawful bases, third parties, retention, and transfer mechanisms
   - **DPIA house style** — section order, risk scoring, DPO consultation trigger, Art.35(3) mandatory triggers plus house triggers
   - **DSAR process** — verification method, 1-month statutory deadline and internal SLA, DPA 2018 Sch.2 exemptions in use, manifestly-unfounded / excessive policy
   - **UK regulatory footprint** — UK GDPR / DPA 2018 / PECR / Children's Code / NIS Regulations / OSA 2023 / any sector-specific obligations; note UK/EU dual-regime if applicable
   - **Workflow** — intake path, matter workspaces, policy-monitor sweep cadence
   - **Integrations** — document storage / Slack status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Sub-processor notice 30 days → 14 days:* "`/privacy-legal-uk:dpa-review` will now flag
     anything shorter than 14 days as a deviation. Existing DPAs stay as
     logged."
   - *New DPA 2018 Sch.2 exemption in the playbook:* "`/privacy-legal-uk:dsar-response` will surface this
     exemption in the assessment step where the facts match."
   - *Risk posture middle → conservative:* "I'll flag more activities for
     DPIA escalation, recommend stricter IDTA clauses, and be more
     conservative on retention periods."
   - *Adding PECR to footprint:* "`/privacy-legal-uk:use-case-triage` will now run cookie and
     direct-marketing checks on every processing activity. `/privacy-legal-uk:reg-gap-analysis` will include PECR in every gap analysis."
   - *Adding Children's Code to footprint:* "`/privacy-legal-uk:use-case-triage` will now
     run a Children's Code check on every consumer-facing activity, and
     `/privacy-legal-uk:dpia-generation` will include a Children's Code section."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` and note:

   > This change affects all plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/privacy-legal-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a regime from
  scope, offer to mark it `[Not currently in scope]` and explain what
  flagging drops.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., "processor only" + controller playbook positions
  active; or "no UK transfers" + IDTA commitments in the DPA template;
  or "Children's Code not applicable" but product description mentions
  an app for students), flag the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags, `[verify]` tags on cited UK GDPR / DPA 2018 provisions, and
  the mandatory-DPIA-trigger check on `/use-case-triage` are load-bearing — do not remove. If DSAR timelines are adjusted below the 1-month UK GDPR Art.12(3) statutory deadline, refuse and explain why. If breach notification windows are set longer than would allow the controller to meet the 72-hour Art.33 ICO window, refuse and explain.
- **One change at a time.** Don't re-ask the whole interview.
- **UK law verification.** When the user wants to change a setting that
  depends on a UK GDPR article, DPA 2018 section, or PECR regulation —
  and you can look it up via the uk-legal MCP — do so before confirming
  the change is permissible. Flag any constraint: "UK GDPR Art.12(3) sets
  the 1-month DSAR deadline as a maximum — we can set your internal SLA
  shorter but not longer `[UK-GDPR-ART.12(3)]`."
