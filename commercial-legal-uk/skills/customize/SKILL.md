---
name: customize
description: >
  Guided customisation of your UK commercial contracts practice profile — change
  one thing without re-running the whole cold-start interview. Adjust risk
  posture, escalation contacts, playbook positions, NDA triage preferences,
  house style, review preferences, or matter workspace paths. Use when the
  user says "change my [thing]", "update my profile", "edit my playbook",
  "tune my config", or "customise".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/commercial-legal-uk:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a playbook
position, a UK jurisdiction, an output format — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`
   (and `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/commercial-legal-uk:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions (E&W / Scotland / NI), stage, practice setting, sales-side vs. purchasing-side orientation *(shared across all 12 plugins — changes flow through `company-profile.md`)*
   - **Risk posture** — conservative / middle / aggressive, what each means for fallback positions and escalation triggers
   - **People** — escalation chain, approvers by pound threshold and by clause type; regulatory referral contacts (CMA / FCA / ICO / Companies House)
   - **Playbook positions** — the substantive contract positions: liability caps, indemnity scope, IP ownership, data protection (UK GDPR / DPA 2018), termination, auto-renewal, price escalation (CPI/RPI), and the fallbacks for each
   - **NDA triage preferences** — what green / yellow / red looks like for inbound NDAs under English law of confidence
   - **Review preferences** — redline style, explanation depth, whether to produce a stakeholder summary by default
   - **House style** — document format, signature block, renewal-alert channel, deviation-log format; UK English preferences
   - **Workflow** — matter workspace paths, intake path, renewal watcher cadence
   - **Integrations** — Ironclad / DocuSign / uk-legal MCP / govuk MCP / Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Liability cap fallback 12 months → 6 months:* "`/review` will now flag anything above 6 months as a deviation; the UCTA 1977 reasonableness analysis adjusts accordingly."
   - *New escalation approver:* "Any redline exceeding your own authority will now route to this approver — `/escalation-flagger` will include them by default for the matching risk band."
   - *Risk posture middle → aggressive:* "I'll accept more vendor-friendly positions without flagging them and shift the `[review]` bar higher."
   - *Jurisdiction footprint change (add Scotland):* "I'll add Scots law jurisdiction notes throughout reviews — key differences: no consideration requirement, distinct offer/acceptance rules, different frustration doctrine."

5. **For shared-profile changes** (company name, industry, jurisdictions, practice setting, stage): write to `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can run `/commercial-legal-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it to `[Not configured]` and explain what that means for the plugin's behaviour.
- **Flag internal inconsistency.** If the change would make the profile inconsistent (e.g., risk posture aggressive + "every redline needs Head of Legal approval"; or "sales-side" + a purchasing-side playbook position), flag the tension and ask which one they want.
- **Flag guardrail degradation.** If the user asks to turn off a guardrail (drop the `[review]` flag, skip the privilege header, remove `[verify]` tags), explain what the guardrail protects against and confirm they understand the trade-off. The `[review]` flag, source attribution tags, and `[verify]` tags on cited statutes are load-bearing and should not be removed.
- **One change at a time.** Don't re-ask the whole interview.
- **UK English.** Write all profile updates in UK English (recognise, organise, licence as noun, favour, etc.).
