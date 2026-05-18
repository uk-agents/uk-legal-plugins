---
name: cold-start-interview
description: >
  Run the cold-start interview — learns your UK data-protection practice and writes
  CLAUDE.md from your privacy notice, DPA template, and a reference DPIA. Use on
  first run, when CLAUDE.md is missing or has placeholders, or when the user says
  "set up the privacy plugin", "onboard me", "configure privacy", or wants to re-run
  the interview or re-check integrations.
argument-hint: "[--redo to re-run] [--check-integrations to re-probe integrations only]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` — if populated and no `--redo`, confirm before overwriting.
2. Run the interview workflow below.
3. Seed docs: privacy notice (URL or file), DPA template, one reference DPIA. Read all three.
4. Extract: notice commitments, DPA positions (note deltas vs. stated), DPIA structure.
5. Migration: if a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/privacy-legal-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.
6. Write `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` (create parent directories as needed). Show summary. Offer first task.

## `--check-integrations`

Re-runs the integration availability check (document storage, Slack, scheduled-tasks) and updates `## Available integrations` in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. Does not re-interview. Use when you connect or disconnect an MCP and want the plugin to notice without rerunning the full setup.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.

```
/privacy-legal-uk:cold-start-interview
```

```
/privacy-legal-uk:cold-start-interview --check-integrations
```

---

# Cold-Start Interview: UK Privacy & Data Protection

## Purpose

Learn how *this* UK data-protection team works — what regulations actually apply (UK GDPR / DPA 2018 / PECR / NIS / OSA / Children's Code), what they will and won't agree to in a DPA, what a good DPIA looks like here. Write it into `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` so every other skill reads from the same understanding.

UK data-protection practices vary widely by sector and organisational type. A B2B SaaS processor has almost nothing in common with a consumer app controller subject to the Children's Code. The interview figures out which one this is before anything else.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/uk-legal-plugins/privacy-legal-uk/*/CLAUDE.md` but not at the config path, copy it forward.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** After the orientation and fork, ask the company questions and write them to the shared profile, then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other legal plugins will read it and skip these questions."

The company questions that belong in the shared profile (and should NOT be re-asked if it exists): practice setting, company name, industry, what-you-sell, size, jurisdictions, regulators, risk appetite, escalation names.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it once and ask the user to confirm before proceeding.

## Before the interview starts

Show the fork-first preamble — 3-4 short lines:

> **`privacy-legal-uk` is for people who run the UK data-protection programme: DPIAs, DPA reviews, DSAR responses, regulatory gap analysis under UK GDPR and DPA 2018.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, which side of a DPA you sit on (controller/processor/both), and primary UK regulatory footprint, with sensible defaults everywhere else. **15 minutes** adds your DPA playbook positions, your DPIA template structure from a reference DPIA, your full footprint (PECR / NIS / Children's Code / OSA), and your processing-activity seeds.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

Wait for the user's pick before showing anything else.

## After the user picks quick or full

Orient them before the first interview question:

> "This plugin maintains your UK privacy practice profile (DPA playbook, DPIA house style, UK regulatory footprint including PECR and Children's Code), a processing-activity register, and per-activity DPIAs and DPA reviews. This setup interview learns how you actually work — your practice, your DPA positions, your DPIA house style — and writes it into a plain-text file the plugin reads every time. Everything you answer can be changed later. Once done, the plugin's commands will work the way you work, not the way a generic template does."
>
> Then: "Setup builds a fresh professional profile from your answers. It does not read your personal Claude history, other conversations, or your home-directory CLAUDE.md. If I notice relevant information in our conversation context, I'll ask before using it."
>
> Then: "Ready? A few quick questions first, then we'll go deeper."

**Why this matters.** A generic configuration gives you generic output — a default DPA position, a default DPIA format, a default DSAR workflow, and a review that treats your B2B processor agreement the same as a consumer-controller one. Telling the plugin your actual UK regulatory footprint, your actual DPA positions, and your actual DPIA house style is what makes the difference between "a privacy AI tool" and "a tool that works the way your programme works."

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and UK regulatory footprint. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for DPA positions, DSAR timing, and DPIA thresholds. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/privacy-legal-uk:cold-start-interview --full` anytime to do the whole interview."

**Full setup path:** the existing interview flow below.

## Interview pacing

- **Assume the answer exists somewhere.** Prompt for a link or a paste before asking the user to type it from memory.
- **Batch size — count subparts.** Never ask more than 2-3 answerable prompts in one turn, counting subparts.
- **Pause for real answers.** Some questions need more than a quick tap. Say explicitly: "This one needs a typed answer — I'll wait."
- **Pause and resume.** Tell the user upfront: "If you need to stop, say 'pause' and I'll save your progress." When paused, write a partial configuration with `<!-- SETUP PAUSED AT: [section name] -->` at the top.

**Verify user-stated UK legal facts as they come up in setup.** When the user states a UK GDPR article number, DPA 2018 section, PECR regulation number, ICO guidance reference, deadline, or threshold — and it's something you can sanity-check — do the check before writing it into the configuration.

## The interview

### Opening

> I'm going to help with DPAs, DSARs, DPIAs, and keeping an eye on when UK data-protection rules move under you. Before I do any of that, I need to know what kind of privacy programme this is. Ten minutes.
>
> Then I'm going to ask you to show me three things: your privacy notice, your standard DPA, and one DPIA you think is good. I'll learn more from those than from anything you tell me.

### Part 0: Who's using this, and what's connected

Three quick questions before we get into UK privacy specifics.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds every skill's work-product header and output framing — qualified lawyer / solicitor gets "LEGAL PROFESSIONAL PRIVILEGE," non-lawyer gets research framing and professional-review checkpoints before legally consequential steps.)
>
> 1. **Lawyer, solicitor, barrister, or legal professional** — qualified, or paralegal / privacy ops working under their oversight.
> 2. **Non-lawyer with access to a solicitor** — DPO-office non-lawyer, privacy programme manager, founder handling privacy with an in-house or outside solicitor you can consult.
> 3. **Non-lawyer without regular solicitor access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — triage, DPA review, DPIAs, DSAR responses, reg-gap analysis, policy monitoring. Two things change in how I work:
>
> 1. **I'll frame outputs as research for professional review, not as conclusions.** Instead of "cleared to sign," you'll get "here's what I found and here are the questions to ask your solicitor before you sign."
> 2. **I'll pause before steps that have legal consequences** — sending a DSAR response, signing a DPA, submitting a DPIA to the ICO, notifying a personal data breach. I'll ask whether you've reviewed with a qualified professional, and I'll put together a short brief so that conversation is fast.
>
> This isn't a disclaimer. It's the plugin knowing the difference between research, organisation, and structure — which it can do — and qualified legal or DPO judgment about your specific situation, which a tool cannot give you.

If the answer is 3, add:

> If you need to find a qualified solicitor, barrister, or other authorised legal professional: the Solicitors Regulation Authority's [Find a Solicitor](https://solicitors.lawsociety.org.uk/) service or the Bar Council's [Find a Barrister](https://www.barcouncil.org.uk/) service are the fastest starting points. For small businesses, local law school clinics and Citizens Advice can also point you in the right direction. For data-protection-specific queries, a qualified DPO or privacy consultant registered with the IAPP or BCS may also help.

#### Practice setting

> Which of these best describes where you're practising?
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, billing thresholds, and who signs off above you.
> - **In-house** — I'll ask about your escalation matrix, who the GC / CLO / DPO is, and when something goes to the business.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

#### What's connected?

> This plugin can work with: document storage (Google Drive, SharePoint), Slack, and scheduled-tasks. Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back gracefully.

**Check what's actually connected, not what's configured.** Only report ✓ on a successful MCP tool call. Report ⚪ if configured but untested. Never report ✓ based on `.mcp.json` alone.

#### Record to CLAUDE.md

Write `## Who's using this` and `## Available integrations` sections immediately.

### Part 1: What kind of UK privacy programme is this? (2-3 min)

**The business model question:**

> **What does [your company] do?** Paste a link to your company website or "about" page, or give me the one-sentence version: what you sell, to whom, and how.

- Whose data flows through the company?
- Are you mostly a **controller** (your own users' data, your own purposes) or mostly a **processor** (customers' data, customers' purposes)? Both?
- B2B, B2C, or both? Consumers or enterprise?

**UK regulatory footprint:**

Which UK data-protection regimes actually apply?

- **UK GDPR + DPA 2018** — almost certainly yes if you process personal data in or about people in the UK
- **PECR** — if you use cookies, send marketing emails/SMS to individuals, or operate electronic communications services
- **ICO Children's Code (Age Appropriate Design Code)** — if your online service is likely to be accessed by children under 18
- **NIS Regulations 2018** — if you operate essential services or are a digital service provider (cloud, online marketplace, search engine)
- **Online Safety Act 2023** — if you operate a user-to-user service or search service in scope of Ofcom regulation
- Any EU-facing processing? (UK GDPR governs UK side; EU GDPR governs EU side — dual regime)
- Any ICO correspondence, investigation, undertaking, or enforcement notice?
- Where does the data physically live? UK only? UK + EU? US? Other?

**The team:**

- How many privacy people? Is there a designated DPO? In-house or external?
- When a review finds something that needs someone more senior to sign off — a DPA position above your approval threshold, a DSAR with exemptions in play, a mandatory DPIA with residual high risk, ICO contact, a suspected breach — who does that go to?

### Part 2: DPA negotiating positions (3-4 min)

*These positions feed `/privacy-legal-uk:dpa-review` — every inbound DPA is reviewed against your standards, fallbacks, and never-accepts. Wrong positions here = wrong reviews every time.*

Before the structured questions: "Do you have an existing DPA template, a negotiation playbook, or a fallback-positions memo I can read? Paste the contents or share a file path."

If the user uploads: read it, extract the positions, confirm what you found, and skip the corresponding detailed questions.

**UK GDPR Art.28 context:** processor DPAs must address the Art.28(3) mandatory provisions. Any processor DPA that doesn't — however labelled — is non-compliant. The review checks this first.

**When you're the processor (controllers / customers send you a DPA):**

- Do you have a standard DPA you push (Art.28 compliant), or do you take customer paper?
- Audit rights: what's your offer — third-party audit report (e.g., ISO 27001 / Cyber Essentials Plus), ICO-format questionnaire, or on-site?
- Breach notification to the controller: what's the shortest window you've agreed to? (Note: the controller has a 72-hour window to the ICO — processors must notify promptly enough to allow this.)
- Sub-processor approval: advance notice with objection right, or notification only?
- Data location commitments: can you commit to UK / UK+EU, or is it "wherever cloud puts it"?
- Deletion on termination: how many days, and do you certify?
- International transfers: if you process outside the UK, what transfer mechanism do you use — IDTA, UK Addendum to EU SCCs, or a UK adequacy decision? Can you commit to that in a DPA?

**When you're the controller (you send a DPA to vendors):**

Same questions, opposite polarity. What do you *require* from processors?

**The one thing in a DPA that makes you say no:**

What's the term that's an automatic reject?

### Part 3: House style (1-2 min)

**DPIAs:** *(This feeds `/privacy-legal-uk:dpia-generation` — the skill uses your trigger, format, depth, and sign-off as the default template for every DPIA it drafts.)*

- What triggers a DPIA at your organisation — only the mandatory Art.35(3) triggers, or a broader house threshold (e.g., every new data category, every new vendor)?
- How long is a good DPIA — one page or ten?
- Who signs off — just you, the DPO, a privacy review committee?
- Does the DPO need to be consulted (Art.35(2))? Is there a formal DPO consultation process?
- Have you ever done a prior ICO consultation (Art.36)?

**DSARs:** *(This feeds `/privacy-legal-uk:dsar-response` — the systems list drives the locate step, the handler drives who gets the runbook, the SLA drives deadline calculations.)*

- Volume — one a month or a hundred?
- Who handles them — you, or a support team with a runbook?
- What systems does a DSAR touch — how many places does personal data live?
- Do you apply any DPA 2018 Schedule 2 exemptions regularly (e.g., legal professional privilege, management forecasts)?
- Have you ever refused or charged for a manifestly unfounded / excessive request?

### Part 4: Seed documents (3-4 min)

> I want to see three things. They'll tell me how you actually work.
>
> 1. **Your current privacy notice.** The public one (Art.13/14 fair processing information). I'll read it to understand what you've committed to — every DPIA and DPA has to be consistent with it.
>
> 2. **Your standard DPA template.** The one you push on controllers or to vendors. This is your stated Art.28 playbook — I'll compare it to what you told me.
>
> 3. **One DPIA you're happy with.** Not a perfect one — a *representative* one. I'll learn your structure, your tone, how deep you go, how you document lawful basis and risk mitigations.

**How to read the seed docs:**

**Privacy notice:** Extract every commitment. Data categories, purposes and lawful bases, retention, third parties / processors, data subject rights offered, international transfers including transfer mechanism. These are the commitments the DPIA skill needs to check against, and the policy-monitor skill watches.

**DPA template:** Map every term to the interview answers. Deltas are interesting — "you said 48-hour breach notification to the controller but your template says 'without undue delay' — which is the real position?"

**DPIA:** Extract the structure as a template. Section headings, depth of analysis, how risk statements are written, how mitigations are documented, how sign-off is recorded. This becomes the default output format for the dpia-generation skill.

### Part 5: Outputs and notice location (1 min)

- **Where do you save completed DPIAs, DPA reviews, and triage results?** A folder path or shared drive location. This is where the policy-monitor skill will crawl to detect practice drift.
- **Where is the actual privacy notice?** The one that gets published or shared with data subjects. I'll need to read it to suggest edits when drift is found.
- **Is there a naming convention for output files?** (e.g., `DPIA_FeatureName_YYYY-MM-DD`) or is it ad hoc?

## Writing the practice profile

```markdown
# UK Privacy & Data Protection Practice Profile

*Written by the cold-start interview on [DATE]. Edit this file directly.*

---

## Who we are

[Company] is a [B2B SaaS / consumer app / platform / etc.]. We are primarily a
[controller / processor / both] with respect to [whose data]. Data lives in
[regions]. Privacy team is [N] people. [DPO name or "no designated DPO"]. Escalation
goes to [GC / CLO / DPO / name].

**Regulatory footprint:** [UK GDPR / DPA 2018 / PECR / Children's Code / NIS Regulations / OSA / other — only list what applies]

**Open regulatory matters:** [none / list]

---

## Who's using this

**Role:** [Lawyer / legal professional | Non-lawyer with solicitor access | Non-lawyer without regular solicitor access]
**Attorney contact:** [Name / team / outside firm / N/A — fill in if non-lawyer]

---

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Document storage (Drive / SharePoint) | [✓ / ✗] | Outputs saved locally; policy-monitor sweep runs in direct-query mode only |
| Slack | [✓ / ✗] | Breach / triage notifications delivered inline instead of posted |
| Scheduled tasks | [✓ / ✗] | Policy-monitor sweep runs on demand only |

*Re-check: `/privacy-legal-uk:cold-start-interview --check-integrations`*

---

## DPA playbook

### When we are the processor (controller DPAs)

| Term | Our standard | Fallback | Never |
|---|---|---|---|
| Audit rights | [e.g., annual ISO 27001 certificate] | [e.g., third-party questionnaire on 30 days' notice] | [on-site without notice] |
| Breach notification to controller | [e.g., team's standard window from discovery — must allow controller to meet 72-hr ICO window] | [e.g., acceptable fallback] | [windows that prevent controller meeting ICO deadline] |
| Sub-processor changes | [e.g., 30 days' advance notice, controller may object] | [notice only, no veto] | [blanket approval right that blocks adding infrastructure] |
| Data location | [e.g., UK + EU only] | [follows controller region] | [hard commitment to single DC] |
| Deletion on termination | [e.g., 30 days post-termination, certification on request] | [longer window] | [immediate] |
| Liability for data | [e.g., within MSA cap] | [separate capped carveout] | [uncapped] |
| International transfers | [e.g., IDTA for non-UK/EU transfers] | [UK Addendum to EU SCCs] | [no mechanism] |

> *From the DPA template:* [any deltas between template and stated positions]

### When we are the controller (vendor DPAs)

| Term | We require | Acceptable | Never accept |
|---|---|---|---|
| [Term] | [what we require] | [what we'll accept] | [what we won't accept] |

### The one thing

[DPA term that's an automatic no]

---

## Privacy notice commitments

*Extracted from [URL / filename] on [date]. If the notice changes, re-run setup or edit this section.*

**Data categories we say we collect:** [list]
**Purposes and lawful bases we state:** [list each purpose + lawful basis under UK GDPR Art.6; note any Art.9 special category bases]
**Retention commitments:** [what the notice says]
**Third-party disclosures / processors named:** [list]
**Data subject rights offered:** [access / erasure / rectification / restriction / portability / objection / Art.22 rights]
**International transfers:** [countries, transfer mechanism used]

---

## DPIA house style

**Trigger:** [what requires a DPIA — Art.35(3) mandatory triggers, plus house triggers]
**DPO consultation required?** [Yes / No / Depends on risk level]
**Format:** [structure extracted from the seed DPIA, or "ICO template"]
**Depth:** [typical length / detail level]
**Sign-off:** [who approves — and note: Art.35(2) requires DPO consultation for mandatory DPIAs]

**Template structure (from seed DPIA):**
[section headings and rough content of each]

---

## DSAR process

**Volume:** [rough monthly count]
**Handler:** [privacy team / support team / automated]
**Systems to check:** [list of every place personal data lives — production DB, analytics, CRM, support, email marketing, backups, third-party processors]
**Identity verification method:** [how you confirm the requester is the data subject]
**Response deadline (statutory):** 1 calendar month from receipt (UK GDPR Art.12(3)). Extension: up to 2 further months for complex/numerous with notice within month 1.
**Internal SLA:** [internal target — must be within the 1-month statutory deadline]
**Exemptions applied:** [DPA 2018 Schedule 2 exemptions regularly relied on, if any]
**Manifestly unfounded / excessive policy:** [whether and when you refuse or charge]

---

## Escalation

| Issue type | Handle at | Escalate to | When |
|---|---|---|---|
| Routine DSAR | [handler] | [you] | Unusual scope, litigation hold, dispute, manifestly unfounded query |
| Customer DPA negotiation | [you] | [GC / DPO] | Outside fallbacks above |
| Mandatory DPIA | [you + DPO consultation] | [GC] | High-risk processing, residual high risk after mitigations |
| Prior ICO consultation (Art.36) | — | [DPO + GC immediately] | When DPIA concludes residual high risk |
| ICO contact or enquiry | — | [GC + DPO immediately] | Always |
| Suspected personal data breach | — | [Security + DPO + GC immediately] | Always — 72-hour Art.33 clock starts on awareness |
| Children's Code compliance | [you] | [DPO + product] | New service / feature likely accessed by under-18s |

---

## Seed documents

| Doc | Location | Date reviewed | Notes |
|---|---|---|---|
| Privacy notice | [URL] | [date] | [version] |
| DPA template | [path/link] | [date] | |
| Reference DPIA | [path/link] | [date] | "[name of processing activity it was for]" |

---

## Outputs

**Outputs folder:** [path where completed DPIAs, DPA reviews, and triage results are saved]
**Naming convention:** [file naming pattern, or "ad hoc"]
**Privacy notice document:** [path or URL to the published privacy notice]
**Notice last updated:** [date]
**Last policy sweep:** [date of last policy-monitor crawl — updated automatically]

**Work-product header** (prepended to DPA reviews, DPIAs, reg-gap analyses, policy-monitor sweeps, and triage outputs):

- If Role is Lawyer / legal professional: `PRIVILEGED & CONFIDENTIAL — LEGAL PROFESSIONAL PRIVILEGE — PREPARED AT THE DIRECTION OF COUNSEL`
- If Role is Non-lawyer: `RESEARCH NOTES — NOT LEGAL ADVICE — REVIEW WITH A QUALIFIED SOLICITOR OR BARRISTER BEFORE ACTING`

For externally-facing deliverables (DSAR response letters, ICO correspondence, data subject communications) the header is omitted.

---

*Re-run: `/privacy-legal-uk:cold-start-interview --redo`*
```

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in UK data-protection practice:**
>
> - **Review a DPA against your Art.28 playbook** — flags deviations from your positions; checks IDTA / UK Addendum for international transfers. Try: `/privacy-legal-uk:dpa-review`
> - **Triage a processing activity** — UK GDPR lawful basis + DPIA mandatory trigger check + Children's Code check. Try: `/privacy-legal-uk:use-case-triage`
> - **Generate a DPIA in house format** — ICO template structure, Art.35(3) trigger check, policy consistency diff, DPO consultation prompts. Try: `/privacy-legal-uk:dpia-generation`
> - **Walk through a DSAR** — verify, locate, DPA 2018 Sch.2 exemptions, draft the 1-month response. Try: `/privacy-legal-uk:dsar-response`
> - **Diff a new UK reg or ICO guidance against your notice** — gap list and remediation plan with owners and deadlines. Try: `/privacy-legal-uk:reg-gap-analysis`
> - **Sweep for policy drift** — look across saved DPIAs, DPA reviews, and triage results to find where the privacy notice no longer matches practice. Try: `/privacy-legal-uk:policy-monitor`
>
> **My suggestion for your first one:** Run `/use-case-triage` on one real processing activity — it's the fastest way to see whether your playbook is capturing the right cuts. Or tell me what's on your plate and I'll pick.

Close with:

1. **Show the summary.** "Here's what I heard. The DPA playbook is the part to check hardest — did I get your positions right?"

2. **Research connector prompt.** Say:
   > "Before your first DPA review or DPIA: connect a research tool. Without one, I'll flag every UK GDPR citation as unverified — with one (the uk-legal MCP), I verify them against current UK legislation. In Claude Code: the uk-legal MCP is already configured in `.mcp.json`. Authorise when a skill prompts you."

3. **Propose first tasks:**
   - "Want me to diff your privacy notice against your actual data collection? Notices drift."
   - "Got a customer DPA in the queue I can take a crack at?"
   - If DSAR volume is high: "Want a DSAR response template built from your systems list?"

4. **Flag gaps:** If they couldn't produce a DPA template or a reference DPIA, note it: "You're running without a standard DPA — first time a customer or vendor asks, you'll be negotiating from scratch. Want to draft one?"

5. **Close with the "you can change anything later" note:**
   > "Your practice profile is at `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` — a plain text file you can read and edit directly.
   >
   > - Edit the file directly for a quick change
   > - Run `/privacy-legal-uk:cold-start-interview --redo` for a full re-interview
   > - Run `/privacy-legal-uk:cold-start-interview --check-integrations` to re-check what's connected
   >
   > The three sections people adjust most: the **DPA playbook** (as you negotiate more and harden positions), the **UK regulatory footprint** (especially PECR and Children's Code as products launch), and the **DSAR systems list** (as the data landscape changes)."

6. **Your practice profile learns.** End with this note:
   > **Your practice profile learns.** It gets better as you use the plugins:
   >
   > - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
   > - The `policy-monitor` skill watches for drift between your privacy notice and how you actually practice. When it finds drift, it'll propose edits.
   > - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
   >
   > Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

## Failure modes

- **Don't assume UK GDPR is the only applicable regime.** If the company uses cookies, PECR applies. If the service is accessed by children, the Children's Code applies. If it runs essential services, NIS applies. Ask and confirm.
- **Don't let them skip the controller/processor question.** If they're not sure, walk through it: "When your customer's users' data comes into your system, whose privacy notice governs it — yours or the customer's?"
- **Don't write a DPA playbook from generic positions.** If they haven't negotiated many DPAs, say so in the config CLAUDE.md: `[POSITIONS UNTESTED — this team hasn't negotiated many UK GDPR DPAs yet. Treat as starting points, not settled positions.]`
- **Don't assume EU GDPR and UK GDPR are identical.** Post-Brexit they are diverging. If the team has EU data subjects, note that both regimes may run in parallel and the ICO is not the sole regulator.
