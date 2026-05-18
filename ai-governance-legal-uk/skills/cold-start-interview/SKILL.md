---
name: cold-start-interview
description: >
  Run the cold-start interview — learns your UK AI governance practice and writes
  `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` from
  your AI policy, a reference impact assessment, and key vendor AI agreements.
  Use when the practice profile is missing or contains `[PLACEHOLDER]` markers,
  or when user says "set up ai governance plugin", "onboard me", "configure ai
  governance".
argument-hint: "[--redo | --check-integrations]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` — if populated and no `--redo`, confirm before overwriting.
2. Run the interview using the workflow below (includes Part 0 role + integration check).
3. Seed docs: AI/acceptable use policy (URL or file), a prior impact assessment, key vendor AI agreements, model inventory or allowlist/blocklist if they exist. Read all provided.
4. Extract: policy commitments and prohibitions, vendor positions (note gaps vs. stated), impact assessment structure, approved/prohibited tool lists.
5. Migration: if a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/ai-governance-legal-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and tell the user what was migrated.
6. Write `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` (create parent directories as needed). Show summary. Offer first task.

## Flags

- `--redo` — re-run the full interview and overwrite `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
- `--check-integrations` — re-scan available MCP connectors and refresh the `## Available integrations` table in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` without re-running the full interview.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.

```
/ai-governance-legal-uk:cold-start-interview
/ai-governance-legal-uk:cold-start-interview --check-integrations
```

---

## Purpose

Learn how *this* UK AI governance team works — what role the company plays in the AI
supply chain, which regulations actually apply to them (ICO, CMA, FCA, DSIT framework,
EU AI Act if EU nexus), what their use case red lines are, and what good impact
assessment looks like here. Write it into the plugin config so every other skill reads
from the same understanding.

AI governance postures vary enormously in the UK context. A company that builds AI products for enterprise customers has almost nothing in common with a company that deploys off-the-shelf AI tools internally. The interview figures out which one this is before anything else — because builder obligations and deployer obligations are nearly opposite exercises, whether you're looking at EU AI Act obligations (where EU nexus exists) or UK GDPR/DPA 2018 obligations.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/uk-legal-plugins/ai-governance-legal-uk/*/CLAUDE.md` but not at the config path, copy it forward to the config path before proceeding.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation and fork, ask the company questions and write them to the shared profile (per the template at `references/company-profile-template.md` in the plugin root), then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other legal plugins will read it and skip these questions."

The company questions that belong in the shared profile (and should NOT be re-asked if it exists): practice setting, company name, industry, what-you-sell, size, jurisdictions, regulators, risk appetite, escalation names. The plugin-specific questions (playbook positions, review framework, house style, supervision model, etc.) stay per-plugin.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead — see QUICKSTART.md. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding: continue with project scope, or pause to reinstall user-scoped.

## Before the interview starts

Open with the fork-first preamble. Keep it to 3-4 short lines. Ask quick-or-full before anything else.

> **`ai-governance-legal-uk` is for people who run AI governance in a UK context: use-case triage, impact assessments, vendor AI review, policy monitoring.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, practice setting, and which AI regulatory regimes apply (ICO / UK GDPR / CMA / FCA / Online Safety Act / EU AI Act if EU nexus), plus working defaults for use-case triage thresholds, AIA format, and vendor AI positions. **15 minutes** adds your use-case registry and red lines, governance tiers, vendor AI playbook positions, escalation matrix, AIA house-style template extracted from a seed assessment, and the AI policy commitments extracted from your actual policy.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and regulatory scope. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for use-case triage thresholds, AIA format, and vendor AI positions. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/ai-governance-legal-uk:cold-start-interview --full` anytime to do the whole interview, or `/ai-governance-legal-uk:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

## After the user picks quick or full

Give the fuller orientation. One paragraph, in your own voice:

> "This plugin maintains: your practice profile (governance tiers, red lines, policy commitments), a use-case registry, impact assessments, and vendor AI reviews — all in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/`. It learns how you actually work — your practice, your risk calibration, your house conventions — and writes that into a plain-text file the plugin reads from every time. Everything you answer can be changed later."

Then: "Ready? A few quick questions first, then we'll go deeper."

**Fresh professional profile.** Setup builds a fresh professional profile from the user's answers and the documents they explicitly share. It does not read the user's personal Claude history, unrelated conversations, or their home-directory CLAUDE.md. If something relevant surfaces in the current conversation context (e.g., they mentioned their company earlier), ask before using it.

## Interview pacing

- **Assume the answer exists somewhere.** Prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts.

**Pause for real answers.** Some questions are quick (pick A/B/C). Others need the user to type, describe, or share a document.

- **Ask and wait.** Say explicitly: "This one needs a typed answer — I'll wait."
- **For uploads or shared documents:** "Paste the contents, share a file path, or say 'skip for now.'"
- **Before writing the practice profile:** review the interview and list any questions that were skipped or answered with placeholders.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' and I'll save your progress." When the user pauses, write a partial configuration with a `<!-- SETUP PAUSED AT: [section name] — run /ai-governance-legal-uk:cold-start-interview to resume -->` comment at the top and `[PENDING]` markers on unanswered fields.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration.

## The interview

### Opening

> I'm going to help with AI impact assessments, vendor AI reviews, use case triage,
> and keeping an eye on when the UK regulations move under you. Before I do any of
> that, I need to know what kind of AI governance shop this is. Ten to fifteen minutes.
>
> Then I'm going to ask you to show me a few things: your AI or acceptable use policy,
> a prior impact assessment if you have one, and your key vendor AI agreements. I'll
> learn more from those than from anything you tell me.

---

### Part 0: Who's using this, and what's connected

Two quick questions before we get into AI governance specifics.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every output — solicitor/barrister/lawyer gets "PRIVILEGED & CONFIDENTIAL — LEGAL PROFESSIONAL WORK PRODUCT"; non-lawyer gets "RESEARCH NOTES — NOT LEGAL ADVICE" and outputs framed as research for solicitor review.)
>
> 1. **Solicitor, barrister, or authorised legal professional** — qualified lawyer, legal ops working under solicitor oversight.
> 2. **Non-lawyer with legal access** — founder, business lead, contracts manager, HR, procurement; you have an in-house or outside solicitor/barrister you can consult.
> 3. **Non-lawyer without regular legal access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for solicitor or barrister review, not as verdicts.** Instead of "GREEN — sign it," you'll get "here's what I found and here are the questions to ask before you sign."
> 2. **I'll pause before steps that have legal consequences** — approving an AI use case for deployment, signing a vendor AI agreement, certifying an impact assessment.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organisation, structure — and licensed legal judgment about your specific situation.

If the answer is 3, add:

> If you need to find a solicitor, barrister, or other authorised legal professional: the Solicitors Regulation Authority (SRA) and the Bar Council maintain referral services for England & Wales. The Law Society of Scotland and the Law Society of Northern Ireland for those jurisdictions. Citizens Advice and legal aid organisations can help for personal matters. Many offer free initial consultations.

#### Practice setting

Ask once, early, so later questions about escalation and sign-off branch correctly:

> Practice setting? (This feeds the governance team and escalation matrix.)
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, billing thresholds, and who signs off above you.
> - **In-house** — I'll ask about your escalation matrix, who the GC/CLO is, and when something goes to the business.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

#### What's connected?

> This plugin can work with: document storage (Google Drive, SharePoint, Box), scheduled-tasks, Slack. Let me check which connectors you have configured.

For each connector this plugin uses, only report ✓ on a successful response. Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect. Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

Write a `## Who's using this` section and an `## Available integrations` section into the plugin config immediately after the first section.

---

### Part 1: Builder, deployer, or both? (3-4 min)

**What does [your company] do?** You don't have to type it out: paste a link to your company website, your "about" page, or give me the one-sentence version: what you sell, to whom, and how. The builder/deployer question below only makes sense on top of this.

**This is the question that determines everything else.**

**EU AI Act context (only if EU nexus).** If the company has users, customers, or employees in the EU/EEA, or offers AI systems to EU users:

> **EU AI Act roles are per-system, not per-company.** If your company has EU nexus, your role (provider, deployer, importer, distributor, authorized representative, product manufacturer) and risk tier are assessed for each AI system separately. Instead of assigning one company-level role, I'll set up a system inventory. We can do 1-3 systems now and add the rest later with `/ai-governance-legal-uk:ai-inventory add`. Or skip the inventory for now if you're not ready.
>
> **Note: the EU AI Act is NOT UK domestic law.** The UK did not retain it after Brexit. UK domestic obligations come from UK GDPR, DPA 2018, ICO guidance, and sector-specific regulation. If your company operates in both the UK and EU, you may have both sets of obligations — and they are different.

Walk through the EU AI Act role options if the user has EU nexus; otherwise explain UK-specific framing (builder vs. deployer under ICO guidance, which affects how data protection obligations apply to AI systems).

**Offer to populate the EU inventory now** (if EU nexus). If they decline or their footprint is UK-only, note that in the config and move on.

**High-level context questions** (ask lightly regardless of inventory choice, to size the practice):
- What kind of AI touches your company today — generative, classification, recommendation, automation, something else?
- Who experiences the AI — customers, employees, candidates, no humans?
- Do you train or fine-tune models, or only consume third-party AI?
- Who manages vendor AI relationships — procurement, legal, a dedicated AI team?
- Are you using AI in any decisions that affect employees or customers? (UK GDPR Art. 22 trigger.)

**Shadow AI discovery.** After the formal tool inventory, ask: "Beyond your approved tools, what AI is actually in use?
- **Embedded AI in tools you've already approved:** Microsoft Copilot, Slack AI, Google Workspace AI, Salesforce Einstein, CRM lead scoring. Many organisations adopted these as 'productivity tools' and never triaged them as AI.
- **Informally adopted tools:** Employees using ChatGPT, Gemini, Claude, Perplexity, or other consumer AI without central approval.
- **Vendor AI you may not know about:** A 'CRM tool' with an AI scoring feature, a 'document system' with AI classification, a 'HR platform' with AI screening.

Add anything surfaced to the use case registry as `[UNDOCUMENTED — NEEDS TRIAGE]`. A registry calibrated only to formal deployments while unapproved tools run in the shadows is a registry that lies."

---

### Part 2: Regulatory footprint (2-3 min)

> Which regulations are actually on your radar? I don't want to assume — tell me
> what's real for you.

**Do not assume any regulation applies. Ask the user which regimes they think apply, then research the AI-specific regulations currently in effect or pending for UK companies in their situation.**

Prompts to walk through:

- **UK domestic footprint** — where are customers, employees, data subjects, and business operations in the UK? Which nation(s): E&W, Scotland, NI?
- **UK GDPR / DPA 2018** — does the company process personal data using AI? Any automated decision-making affecting individuals? (Art. 22 trigger — ask specifically.) DPIA required for high-risk processing?
- **ICO AI guidance** — ICO's guidance on explaining AI decisions, auditing, and high-risk processing is not statutory but regulatorily significant.
- **Sector regulation** — financial services (FCA/PRA), health (MHRA/CQC), online platforms (Ofcom/OSA 2023), insurance, employment screening?
- **CMA** — any AI systems touching competition-sensitive areas, algorithmic pricing, or foundation models the company builds or depends on?
- **EU AI Act** — does the company have EU nexus (users/customers/employees in EU/EEA, or offering AI to EU users)? If yes, EU AI Act obligations layer on top of UK obligations.
- **Contractual requirements** — do enterprise customers require AI disclosures, impact assessments, or AI-specific DPA terms?

**Open regulatory matters:**
- Any regulator (ICO, FCA, CMA, Ofcom) who knows you by name? Investigations, voluntary commitments, enforcement notices relating to AI?

**Practical calibration:**
> "Some teams are in full compliance mode for one or more regimes; others are focused primarily on contract commitments from enterprise customers. Where are you on that spectrum?"

---

### Part 3: Use case registry and red lines (4-5 min)

> Before the scenarios: do you have an existing AI use case registry, an AI policy, or a list of approved/prohibited AI tools I can read? Paste the contents, share a file path, or say 'no' and I'll walk through the scenarios.

If not, extract the registry conversationally from examples.

> "I want to build a picture of your use case landscape and where your lines are.
> I'll give you some scenarios — tell me if they'd be a yes, a conditional yes,
> or a hard no at your company."

**Scenario prompts (tailor to builder/deployer profile):**

*For deployers / internal use:*
- "An HR team wants to use AI to screen CVs before a recruiter looks at them. Under UK GDPR Art. 22, this may be a solely automated significant decision — what happens — is that approved, conditional, or a no?"
- "A manager wants to use AI to summarise performance review notes before writing their own."
- "Customer support wants to use AI to draft responses before a human reviews and sends. Yes, conditional, no?"
- "Finance wants to use an AI tool to flag anomalies in expense reports."
- "Legal wants to use an AI assistant to first-draft NDAs."

*For builders / product AI:*
- "A PM wants to add an AI feature that surfaces personalised content recommendations based on user behaviour."
- "A product team wants to use AI to score leads and prioritise sales outreach."
- "A feature uses AI to make automated decisions without human review in the loop. What triggers a review requirement?"

**For each use case, capture:**
- Approved / conditional / never
- If conditional: what does it take? (Privacy review / DPIA, impact assessment, legal sign-off, specific vendor only, human-in-the-loop requirement, disclosure to affected parties?)
- If never: why is it a hard no? (UK GDPR Art. 22? Company policy? ICO guidance risk?)

**The red lines question:**
> "What's the use case that's an automatic no — the thing someone could propose and you'd stop them immediately without needing to think about it?"

Common categories to probe: biometric data, emotion detection, political/religious inference, fully automated adverse decisions affecting employment or credit (Art. 22 trigger), uses involving children (AADC / Children's Code risk), employee monitoring without consent.

**Governance tier question:**
> "Do you have a tiered approval process — some things the team can approve, some things go to legal, some things need the board? Or is it case by case?"

**If the user didn't upload a use-case registry:** at the end of this section, offer: "Want me to write this up as a standalone use-case registry and red-lines doc you can share and maintain?"

---

### Part 4: Governance and escalation (2 min)

**The team:**
- How many people work on AI governance? Is there a dedicated AI ethics or responsible AI function, or does it sit in legal/privacy/security?
- Who owns the relationship with AI vendors — legal, procurement, IT?
- Is there a CISO, CPO, DPO, or equivalent who owns AI risk?

**Escalation:**

> "When a review finds something that needs someone more senior to sign off — a vendor AI agreement with training-on-data or liability issues, an AI use case that doesn't fit your registry, a regulatory gap that needs a decision, or a call above your authority — who does that go to?"

Also ask:
- Has anything been escalated to the board or C-suite over AI in the last year?
- Any engagement with the ICO, CMA, or FCA on AI?

**External commitments:**
- Have you signed any voluntary AI commitments (e.g., the DSIT AI principles), adopted industry standards, or published a customer-facing AI principles page?

---

### Part 5: Seed documents (3-4 min)

> "I want to see what you actually have. Tell me which of these exist, and share what you can."
>
> 1. **AI or acceptable use policy.** Your internal or public-facing policy on how AI can and can't be used.
>
> 2. **A prior AI impact assessment or AI risk assessment.** Even a rough one.
>
> 3. **Key vendor AI agreements or AI addenda.** The contracts with your main AI vendors.
>
> 4. **Model inventory or AI system register.** If you have one.
>
> 5. **Allowlist or blocklist.** Approved tools, prohibited tools, or a tiered approved vendor list.
>
> If you don't have any of these — that's fine and not unusual. Tell me that and I'll work with what you have.

**Graceful degradation — "I have nothing" path:**

If they have no seed documents:
> "That's okay. Here's what we'll do: I'll set up a baseline practice profile using what you told me in the interview, and I'll flag every section that's based on what you said rather than a reviewed document. The two things that matter most to nail down first are your use case red lines (so the triage skill works correctly — especially Art. 22 red lines) and your vendor positions (so we can review the next agreement that comes in)."

---

### Part 6: Outputs and policy document location (1 min)

> "Two last things — I need to know where to look to keep your AI policy current."

- **Where do you save completed AIAs, triage results, and vendor AI reviews?**
- **Where is the actual AI or acceptable use policy document?**
- **Is there a naming convention for output files?**

---

## Writing the practice profile

Use the CLAUDE.md template from the plugin root as the scaffold. Write to `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

Key differences from the US template:
- In `## Company profile`, `**Regulatory footprint:**` should reflect UK-specific regimes: UK GDPR / DPA 2018, ICO AI guidance, CMA, FCA/PRA (if applicable), Ofcom/OSA 2023 (if applicable), MHRA (if applicable), EU AI Act (if EU nexus only).
- In `## AI system inventory`, note that EU AI Act classification only applies where EU nexus exists; UK GDPR Art. 35 DPIA trigger applies to all personal data processing by AI systems.
- In `## Governance team and escalation`, UK regulator escalation is ICO, CMA, FCA, Ofcom — not FTC, DOJ, SEC.
- `## Who's using this` should use "Solicitor / barrister / authorised legal professional" rather than "Attorney."

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in UK AI governance:**
>
> - **Review vendor AI terms** — e.g., "A vendor sent AI provisions in their SaaS agreement — check them against your training-on-data, liability, and model-change positions." Try: `/ai-governance-legal-uk:vendor-ai-review`
> - **Triage a proposed AI use case** — e.g., "A PM wants to add an AI feature — run it against your registry, check the UK GDPR Art. 22 angle, flag ICO guidance." Try: `/ai-governance-legal-uk:use-case-triage`
> - **Run an AI impact assessment** — e.g., "A high-risk use case needs a structured AIA with UK GDPR/ICO analysis and recommended conditions." Try: `/ai-governance-legal-uk:aia-generation`
> - **Diff a new UK AI regulation against your posture** — e.g., "The ICO published new AI guidance — see what gaps it opens and what remediation it forces." Try: `/ai-governance-legal-uk:reg-gap-analysis`
> - **Sweep for policy drift** — e.g., "Look across saved AIAs, triage results, and vendor reviews to find where your AI policy no longer matches practice." Try: `/ai-governance-legal-uk:policy-monitor`
>
> **My suggestion for your first one:** Triage one real use case from your backlog — it's the fastest way to feel what the registry gives you. Or tell me what's on your plate and I'll pick.

1. **Show the summary.** "Here's what I heard. The use case registry is the part to check hardest — did I capture your red lines correctly? The Art. 22 / automated decision-making red lines drive the UK GDPR analysis in every triage."

2. **Propose first tasks:**
   - "Want me to run a triage on the use cases you mentioned and give you a risk tier and impact assessment checklist for each?"
   - "Got a vendor AI agreement in the queue I can review against your positions?"
   - If no impact assessment template: "Want to build your impact assessment template from scratch now?"
   - If no policy: "You're running without a written AI policy — if something goes wrong, you'll be explaining your governance verbally. Want to draft one?"

3. **Flag gaps.** Call out explicitly what's missing and what risk that creates.
   - No model inventory: "You don't have a register of what AI you're running. That means you can't do a systematic Art. 22 assessment or respond quickly to an ICO inquiry."
   - No vendor AI terms: "Your vendor agreements may have no AI-specific provisions — which means your vendors can train on your data, change their models without notice, and disclaim all liability for AI errors."

4. **Connect to privacy:** "Some of this overlaps with your privacy practice — UK GDPR Art. 35 DPIAs and AI impact assessments often cover the same ground. Once both plugins are calibrated, I can flag when a use case needs both."

5. **Close with a note on changeability.** End with something like:

   > "Done. Your configuration is at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` — it's a plain text file you can read and edit directly. Anything you answered can be changed:
   >
   > - Edit the file directly for a quick change
   > - Run `/ai-governance-legal-uk:cold-start-interview --redo` for a full re-interview
   > - Run `/ai-governance-legal-uk:cold-start-interview --check-integrations` to re-check what's connected"

6. **Before your first triage**: connect a research tool. Without one, I'll flag every citation as unverified — with one, I verify them against current legislation and ICO guidance. In Cowork: Settings → Connectors. In Claude Code: authorize when a skill prompts you.

## Your practice profile learns

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune.
> - The `policy-monitor` agent watches for drift between your AI governance policy and your practice, and proposes updates.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.

## Failure modes

- **Don't let them skip the builder/deployer question.** If they say "both," get specific about which side creates the larger governance obligation right now.
- **Don't assume any regulation applies.** Research whether the regime actually reaches them (UK GDPR, ICO guidance, sector regulation, EU AI Act if EU nexus) before treating it as in scope.
- **Don't write a use case registry from generic positions.** If they've never formally approved or rejected a use case, say so in the plugin config: `[POSITIONS FROM INTERVIEW — these reflect stated preferences, not formally reviewed policy]`
- **Don't merge this with the privacy interview.** The overlap is real — DPIAs, vendor assessments, policy frameworks — but the orientation is different enough that running them together loses sharpness.
- **Don't assume EU AI Act applies.** Always ask about EU nexus first. Many UK-only companies have no EU AI Act obligations at all.
