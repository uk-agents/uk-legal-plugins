---
name: customize
description: >
  Guided customization of your UK IP practice profile — change one thing without
  re-running the whole cold-start interview. Adjust risk posture, escalation
  contacts, portfolio scope, brand protection strategy, enforcement posture,
  clearance thresholds, OSS review rules, or matter workspace paths. Use when
  the user says "change my [thing]", "update my profile", "edit my config",
  or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/ip-legal-uk:customize`. They want to change something in their
UK IP practice profile — a risk posture, an escalation contact, a portfolio
position, an enforcement tactic — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`
   (and `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/ip-legal-uk:cold-start-interview` first —
   > customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all plugins — changes flow through
     `company-profile.md`)*
   - **IP practice profile** — which IP types are in scope (patents, trade marks,
     copyright, trade secrets, designs), practice orientation (prosecution /
     transactions / enforcement / in-house portfolio)
   - **Post-Brexit portfolio position** — UK/EU split, EUIPO comparable UK marks,
     UPC opt-out status, design coverage gaps
   - **Risk posture** — conservative / middle / aggressive, what each means
     for clearance thresholds, FTO opinions, and cease-and-desist escalation
   - **People** — IP counsel, outside firms by IP type (UK solicitors, Chartered
     Patent Attorneys, Trade Mark Attorneys), enforcement escalation chain,
     invention committee
   - **Portfolio** — patent families, trade mark classes, key marks, countries
     of registration (UK IPO / EUIPO / Madrid), watch services
   - **Brand protection** — enforcement posture on marketplace takedowns,
     domain squatters, parody / fair use calls; note UK and EU watch services
     are separate since Brexit
   - **Enforcement posture** — when to send C&D vs. soft letter vs. file proceedings
     (IPEC / High Court); escalation triggers by infringement type
   - **Clearance and FTO** — search vendors, clearance confidence thresholds,
     FTO opinion format
   - **OSS review** — licence tier policies (note UK vs. EU enforcement differences
     on some licences), ship-blocker licences, review cadence for new dependencies
   - **Workflow** — matter workspaces (matter IDs, family IDs), docket feed,
     invention intake form
   - **Integrations** — UK IPO / EUIPO / EPO connectors / uk-legal MCP / Slack /
     document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new trade mark watch class:* "`/ip-legal-uk:portfolio` will include class
     XX in watch reports and `/ip-legal-uk:infringement-triage` will route class-XX
     findings accordingly."
   - *Enforcement posture aggressive → middle:* "`/ip-legal-uk:cease-desist` will offer
     soft-letter drafts as a first option for ambiguous cases instead of
     going straight to C&D."
   - *New ship-blocker OSS licence:* "`/ip-legal-uk:oss-review` will fail reviews that
     include this licence rather than warning."
   - *Post-Brexit EU coverage added:* "I'll update your jurisdiction footprint to
     include EUIPO filings and note which marks have comparable UK equivalents."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` and note:

   > This change affects all plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/ip-legal-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" an IP type from
  scope, set it to `[Not currently in scope]` and explain what drops out.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., trade mark out of scope + trade mark watch service
  configured; or aggressive enforcement posture + "all C&Ds go to outside
  counsel"), flag the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags, and `[verify]` tags on cited authorities are load-bearing — do not
  remove. Clearance confidence is load-bearing on `/ip-legal-uk:clearance` output — do
  not suppress.
- **One change at a time.** Don't re-ask the whole interview.
- **Flag post-Brexit implications.** If the user changes their jurisdiction
  footprint (adding or removing UK or EU), flag the post-Brexit implications
  for trade marks, designs, and the UPC opt-out on patents.
