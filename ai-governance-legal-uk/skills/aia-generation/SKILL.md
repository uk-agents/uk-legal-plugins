---
name: aia-generation
description: >
  Run an AI impact assessment — structured intake, risk analysis, UK regulatory
  classification (UK GDPR / DPA 2018, ICO AI guidance, sector-specific UK
  regulation), EU AI Act analysis where EU nexus exists, policy consistency
  diff, and recommendation with conditions. Uses the house-style structure
  learned from the seed impact assessment in
  `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
  Use when user says "impact assessment for", "assess this AI use case", "run an
  AIA", "generate an AIA", "we need to document this AI system", "AI risk
  assessment for X", or follows a conditional triage result.
argument-hint: "[describe the use case or system, or pass a triage result]"
---

# /aia-generation

1. Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. Confirm impact assessment house style is populated.
2. Determine risk track (fast or full) from governance tier and use case characteristics, using the framework below.
3. Run intake — conversational, not a form.
4. Regulatory classification for each regime in the footprint — UK GDPR / DPA 2018 / ICO guidance as primary; sector-specific UK obligations; EU AI Act where EU nexus exists. Research tier, prohibited-practice exposure, and applicable obligations; cite primary sources.
5. Write assessment in house style (from seed doc, or default if none captured).
6. Policy diff against `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` AI policy commitments.
7. Output: assessment doc + conditions list + handoff flags (privacy DPIA, vendor review if needed).

```
/ai-governance-legal-uk:aia-generation "AI résumé screening for HR"
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ai-governance-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

An AI impact assessment is a documented decision, not a form. It answers: what does this AI system do, how does it reach its outputs, who's affected if it's wrong, what's the oversight, and is it okay to deploy. This skill structures that conversation and writes the output in this team's format — the one learned from the seed impact assessment during cold-start.

An AI impact assessment is not the same as a UK GDPR Article 35 DPIA. A DPIA asks whether personal data is handled lawfully. An AIA asks whether the AI system is designed and deployed responsibly. They often need to happen in parallel; they're not substitutes. For AI systems processing personal data at scale, both are likely required — the DPIA under UK GDPR Art. 35, and the AIA under the company's AI governance framework. The ICO expects organisations to maintain evidence of their assessments; the AIA provides that evidence for AI-specific risks.

## Load house style

Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` → `## Impact assessment house style`. That has:
- What triggers an impact assessment at this company
- The structure template extracted from the seed assessment
- Typical depth
- Who signs off

If the seed structure is in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`, **use it**. The point is that this assessment looks like the other assessments this team produces.

**Jurisdictional scope.** This assessment applies the regulatory regimes listed in `## Regulatory footprint` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. UK AI legal rules and obligations are evolving and apply differently across England & Wales, Scotland, and Northern Ireland in some respects, and EU AI Act obligations apply only where EU nexus exists. If this system is (or will be) deployed outside that footprint, re-run or expand the footprint.

---

## Step 0: Is an impact assessment needed?

Check the trigger criteria in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

**Also check these UK-specific triggers regardless:**
- Does this AI make or materially influence a decision affecting an individual (employment, credit, access to services, pricing, content moderation)? → UK GDPR Art. 22 / Art. 35 trigger.
- Does this AI process personal data about individuals at large scale or using new technology? → UK GDPR Art. 35 DPIA mandatory.
- Does this AI process special category data (health, biometric, race/ethnic origin, trade union membership, etc.)? → Art. 35 DPIA mandatory; ICO high-risk flag.
- Is this a customer-facing AI system in a regulated sector (financial services, health, online safety)? → Sector regulatory assessment required.
- Does the company have EU nexus and does this AI system affect EU data subjects? → EU AI Act risk classification required in addition.
- Is this a public sector AI system? → ATRS publication obligation may apply.

If none of the above and the house trigger isn't met:
> "Doesn't look like this needs a full impact assessment. Here's a one-paragraph record for the file explaining why — in case the ICO or another regulator asks later."

---

## Step 1: Risk track

Before intake, determine which track to run. The tier definitions and the fast-track criteria come from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`, not from any hardcoded regime-specific framework.

Research the applicable risk classification framework for each regime in the user's regulatory footprint:
- **UK domestic:** ICO's list of processing types that require a DPIA (Art. 35(3) categories — systematic automated processing, large-scale special category data, systematic monitoring of public areas); sector regulator risk frameworks (FCA, MHRA, Ofcom as applicable).
- **EU AI Act (if EU nexus):** Prohibited practices (Art. 5), high-risk categories (Annex III), limited-risk transparency obligations, GPAI. Note that EU AI Act article numbers shifted during consolidation — every pinpoint cite should be verified against the Official Journal text.

Note that most UK regulatory frameworks treat employee data as personal data and employee monitoring as consequential; don't assume internal-only systems are out of scope.

> **No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, govuk MCP, legislation.gov.uk, or firm platform) returns few or no results for a regime's risk tiers or triggers, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority before relying, or (4) flag as unverified and stop. Which would you like?"
>
> **Source attribution tiering.** Tag every citation in the AIA — regulatory text, delegated acts, guidance, standards — with its source. For model-knowledge citations, use one of three tiers:
>
> - `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., UK GDPR Art. 22 as a concept, DPA 2018 structure, ICO as the UK supervisory authority).
> - `[verify]` — model-knowledge citations that are real but should be verified: specific ICO guidance versions, FCA publications, sector regulator guidance, Data (Use and Access) Act 2025 provisions, effective dates, thresholds.
> - `[verify-pinpoint]` — pinpoint citations (specific article numbers, section references, subsection letters) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`); web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`.
>
> **For non-lawyer users, uncertain dates go in a confirm-list, not inline.** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If Role is **Non-lawyer** and a date, deadline, phase-in, threshold, or effective-date assertion is uncertain, replace the inline assertion with "effective date: confirm with your solicitor/barrister" and collect all uncertain assertions in a final AIA section titled:
>
> > **Things I'm not certain about — ask your solicitor or barrister to confirm before relying on this:**

**Fast track vs. full assessment:** `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` defines what qualifies for abbreviated treatment.

If in doubt, run the full assessment.

---

## Step 2: Intake

Before writing anything, get answers to these. Conversational is fine.

### The system

- What does the AI do? Describe it in plain language, not marketing copy.
- Which model or vendor is powering it? Fine-tuned or off-the-shelf?
- Where does it sit in the workflow — is it assistive (human reviews output), augmentative (human can override but usually doesn't), or automated (no human in the loop)?
- What's the output — generated text, a score, a classification, a recommendation, an action?

### Who's affected

- Who does the AI's output act on — employees, customers, third parties?
- Are they in the UK? Which nations (E&W, Scotland, NI)? Any EU users?
- If the AI produces an error (false positive, false negative, hallucination), who bears the harm and what's the worst realistic case?
- Are any vulnerable groups disproportionately in scope — minors, job applicants, people in financial distress, patients?

### Inputs and data

- What data does the AI take in?
- Does it take in personal data? Whose?
- Special category data (health, biometric, race/ethnic origin, etc.)?
- Was the model trained on data from this company, or is it a foundation model with no company-specific training?
- Where does input data go — does it leave the perimeter to a third-party model API?

### Decisions and oversight

- Does the AI output trigger an action automatically, or does a human decide what to do with the output?
- UK GDPR Art. 22 check: Is this a **solely automated** decision with **legal or similarly significant effects** on individuals? If so, what is the lawful basis?
- If there's human review: how often does the human actually change the AI's output? (If the answer is "rarely" — the human isn't really reviewing; they're rubber-stamping.)
- Is there an appeals or correction process for people affected by the AI's outputs?
- Who is accountable for the AI system's outputs — is there a named owner?

### Accuracy and failure

- What's the known or estimated error rate? What testing has been done?
- What happens when the AI is wrong — is the error surfaced, logged, corrected?
- Has bias testing been done? Against what demographic groups? (ICO expects bias testing for high-risk automated processing.)

### Deployment stage and scale

Ask:
- **Stage:** "Is this system (a) proposed and not yet built, (b) in pilot, (c) live in production, or (d) live and scaled?"
- **Scale:** "Roughly how many individuals are affected per [month/year]? How long has it been running?"
- **History:** "Has it been assessed before? Has it produced decisions that were challenged, appealed, or reversed?"

Stage changes the assessment: a proposed system gets a design review. A pilot gets a design review plus a "before you scale" gate. A live system gets a retrospective impact check AND a go-forward review.

---

## Step 3: Regulatory classification

**Step 3 pre-check — footprint freshness.** Before iterating over the captured `## Regulatory footprint`, compare the use case's affected population and decision type (from Step 2) against the footprint as written. If the use case introduces an affected population or a decision type that the footprint does not contemplate, **re-derive the applicable regimes**.

For each regime in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` → `## Regulatory footprint` that applies to this system — **plus any regime surfaced by the re-derivation above** — research the currently operative risk classification framework and determine where the system lands.

Research tasks:

**UK domestic (primary for all UK-based organisations):**
- **UK GDPR / DPA 2018:** Does this involve personal data? Is a DPIA required (Art. 35)? Does Art. 22 apply (solely automated significant decisions)? What is the lawful basis? Any special category data?
- **ICO AI guidance:** Does ICO's current guidance on explaining AI decisions, auditing, or high-risk processing apply? ICO has published specific guidance on AI fairness, transparency, and explainability — check current versions. `[model knowledge — verify against current ICO guidance]`
- **Sector-specific (apply only if in scope):**
  - **FCA/PRA:** Model risk management (PS7/24 / SS1/23) — consequential AI in regulated financial services. Model validation, documentation, human oversight requirements.
  - **Ofcom/Online Safety Act 2023:** Systemic risk assessment, age verification, illegal content for in-scope services.
  - **MHRA:** AI as a Medical Device (AIaMD) — software as a medical device lifecycle requirements, post-market surveillance.
  - **Cabinet Office/DSIT:** Algorithmic Transparency Recording Standard for public bodies.
  - **NICE:** Evidence standards for AI diagnostic and clinical decision support tools.

**EU AI Act (only if EU nexus exists):**
- What is the regime's own tier taxonomy (prohibited / high-risk / limited / minimal / GPAI)?
- What are the criteria for each tier? Cite primary sources with pinpoint references, tagged `[verify-pinpoint]`.
- Which tier does this system fall into?
- Are there prohibited practices the system might touch?
- Are there transparency obligations that apply regardless of tier?
- If the company is a builder providing a general-purpose or foundation model, what provider-level obligations apply?
- **Does any regime require a separate fundamental-rights impact assessment (FRIA)?** EU AI Act Art. 27 requires a FRIA for certain deployers of high-risk AI systems. If a FRIA is required, flag it as a separate deliverable — do not treat this AIA as a substitute.

**Provider-vs-deployer split (when `AI role: Both` for EU AI Act purposes).** If the company is both a provider/builder and a deployer, produce per regime:

| Obligation | As provider | As deployer |
|---|---|---|
| [specific obligation, pinpoint cite] | [what applies] | [what applies] |

---

## Step 4: Write the assessment

**Use the seed structure from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.** If none was captured, use this default:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# AI Impact Assessment: [System/Feature Name]

**Prepared by:** [name] | **Date:** [date] | **Status:** DRAFT / APPROVED
**System owner:** [name] | **AI governance reviewer:** [name]
**Governance tier:** [Standard / Elevated / High]
**Track:** [Fast track / Full assessment]

---

## Executive summary

[Two sentences: what this AI does and whether it's okay to deploy. E.g., "This
system uses a third-party LLM to draft initial responses to customer support
tickets before human agent review. Processing is consistent with the company's AI
policy; three conditions required before production deployment."]

**Overall risk:** 🟢 Low / 🟡 Medium / 🟠 High / 🔴 Very high

---

## 1. System description

**What it does:** [plain English — not marketing]
**Model / vendor:** [who's providing the AI]
**Deployment mode:** [Assistive / Augmentative / Automated]
**Output type:** [text / score / classification / recommendation / action]
**Status:** [Not started / Pilot / Production]

---

## 2. Affected parties

**Who it acts on:** [employees / customers / third parties]
**UK nations:** [E&W / Scotland / NI / all UK — and EU if applicable]
**Scale:** [how many people, how often]
**Harm if wrong:** [most realistic worst case — specific, not generic]
**Vulnerable groups in scope:** [yes — [who] / no]

---

## 3. Data inputs

**Data categories used:** [specific fields, not "user data"]
**Personal data:** [yes — [whose] / no]
**Special category data:** [yes — [what] / no]
**Data leaves perimeter?** [yes — to [vendor] / no]
**Model training:** [company data used / foundation model / fine-tuned on [dataset]]

---

## 4. Decision-making and oversight

**Human in the loop:** [Always / Nominally (rubber-stamp risk) / No]
**Art. 22 UK GDPR position:** [Not triggered / Triggered — [lawful basis] / Unclear [review]]
**Override mechanism:** [how a human can intervene or correct]
**Appeals / correction for affected parties:** [yes — [how] / no]
**Named owner:** [name or role]

---

## 5. Accuracy and bias

**Error rate:** [known / estimated / untested]
**Failure mode:** [what happens when it's wrong — surfaced? logged? corrected?]
**Bias testing:** [done — [results] / not done / not applicable — ICO expects bias testing for consequential AI on personal data]

---

## 6. Regulatory classification

*[One subsection per regime in the regulatory footprint that applies to this system.]*

### 6.1 UK domestic

**UK GDPR / DPA 2018:**
- **Art. 22 automated decision-making:** [Not triggered / Triggered — lawful basis: [contract / statutory / explicit consent] / Unclear [review]]
- **Art. 35 DPIA required?** [Yes — DPIA should be run in parallel / No / Unclear [review]]
- **Special category data:** [Not present / Present — [what] — additional safeguards required under Art. 9]
- **Lawful basis for processing:** [cite basis and provision] `[verify]`

**ICO AI guidance:**
- **Explainability obligations:** [applicable / not applicable — reason]
- **High-risk processing under ICO guidance:** [yes / no / unclear [review]]
- **ICO AI auditing framework relevance:** [applicable / not applicable]
`[model knowledge — verify against current ICO AI guidance versions]`

**Sector-specific (complete only if applicable to this company's regulatory footprint):**
- **FCA/PRA model risk (PS7/24 / SS1/23):** [applicable / not applicable — reason] `[verify]`
- **Online Safety Act / Ofcom:** [applicable / not applicable — reason] `[verify]`
- **MHRA AIaMD:** [applicable / not applicable — reason] `[verify]`
- **ATRS (public sector):** [applicable / not applicable — reason] `[verify]`

### 6.2 EU AI Act (complete only if EU nexus exists)

**EU nexus confirmed:** [Yes / No — skip this section]

**Classification under EU AI Act:**
- **Prohibited practices triggered (Art. 5):** [none identified / [specific provision and why]] `[verify-pinpoint]`
- **Risk tier:** [prohibited / high_risk — Annex III [area] / limited / minimal / GPAI] `[verify-pinpoint]`
- **Applicable obligations:** [researched list with citations] `[verify]`
- **FRIA required (EU AI Act Art. 27)?** [Yes — separate deliverable required / No / Not applicable] `[verify-pinpoint]`
- **Effective / enforcement date:** [date(s)] `[verify]`

**Provider-vs-deployer obligation split (required if `AI role: Both` for EU purposes):**

| Obligation | As provider | As deployer |
|---|---|---|
| [specific obligation + pinpoint cite] | [what applies] | [what applies] |

---

## 7. AI policy consistency

| Policy commitment | Consistent? | Notes |
|---|---|---|
| [commitment from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` AI policy section] | 🟢 / 🟡 / 🟠 / 🔴 | |

[If any item is 🟡 or worse: policy update needed before deployment, or design needs to change. One of them has to change — not both flagged and left open.]

---

## 8. Risks and mitigations

| # | Risk | Likelihood | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|---|---|
| 1 | [specific risk tied to this design — not "AI hallucination" generically] | L/M/H | L/M/H | [specific control] | Done / Planned / Gap | [name] |

**Residual risk after mitigations:** [assessment]

---

## 9. Recommendation

**[APPROVED / APPROVED WITH CONDITIONS / CHANGES REQUIRED / NOT APPROVED]**

**Conditions (if any):**
- [ ] [specific action before deployment — owner, deadline]

**UK GDPR Art. 35 DPIA required?** [Yes — run `/privacy-legal-uk:pia-generation`, if the plugin is installed / No]

**EU AI Act FRIA required?** [Yes — separate deliverable / No / Not applicable — no EU nexus]

**Sign-off:** [name, date]

---

## Cite check

Regulatory citations in Section 6 (and anywhere else) were generated by an AI model and have not been verified against primary sources. Before the assessment is certified or relied on, run a verification pass against a legal research tool (uk-legal MCP, legislation.gov.uk, govuk MCP, or your firm's platform) for each cited provision — confirm the pinpoint, currency, and any implementing guidance. The UK AI regulatory landscape is moving quickly; verify before advising. Source tags on each citation show where it came from; `verify` and `verify-pinpoint` tags carry higher fabrication risk and should be checked first.
```

**Before certifying the AIA (the Sign-off step, marking Status: APPROVED):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Certifying this AIA has legal consequences — it becomes the record the company relies on if the ICO, FCA, CMA, or another regulator asks how this use case was assessed. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the system, the UK GDPR Art. 22 and Art. 35 position, the sector regulatory flags, the risks identified, the mitigations in place, residual risk, open questions, what to ask the solicitor before certifying.]
>
> If you need to find a solicitor or barrister: sra.org.uk (SRA), barcouncil.org.uk (Bar Council) for England & Wales; lawscot.org.uk (Law Society of Scotland); lawsoc-ni.org (Law Society of Northern Ireland).

Do not proceed past this gate without an explicit yes.

---

## Risk quality standards

Risks must be **specific and tied to the design**.

| Bad risk | Why bad | Better |
|---|---|---|
| "AI hallucination" | Applies to every LLM; says nothing | "Model may generate plausible but incorrect legal citations — support agents have no current verification step before sending to customers" |
| "Bias" | Too vague | "CV scoring model trained on historical hires; if historical cohort was demographically homogeneous, underrepresented candidates may be systematically scored lower — Art. 22 automated significant decision risk" |
| "Vendor risk" | Circular | "Vendor's terms permit training on API inputs by default; unless the opt-out is confirmed in the agreement, customer support messages may be used to train the model" |

Aim for 2-5 real risks, not 12 padded ones.

---

## AI policy diff

Every assessment should cross-check against the AI policy commitments in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
Common drift:

- Policy prohibits AI use in [category] — this use case is that category. Stop.
- Policy requires human review — this deployment has no human step. Design needs to change.
- Policy requires disclosure to affected parties — disclosure mechanism hasn't been built.
- Approved vendor list exists — this vendor isn't on it. Procurement step required.

Flag every mismatch. One of them has to change before deployment.

---

## Handoffs

- **To product / engineering:** Conditions list with owners and deadlines.
- **To privacy:** If personal data is involved and Art. 35 DPIA is required, flag: "Run `/privacy-legal-uk:pia-generation [system name]` in parallel, if the plugin is installed — the AIA doesn't substitute for a DPIA."
- **To vendor-ai-review:** If a new vendor is involved, flag: "If there's no AI addendum reviewed for [vendor], run `/ai-governance-legal-uk:vendor-ai-review` before production."
- **To reg-gap-analysis:** If new regulatory obligations emerged (EU AI Act high-risk, new ICO guidance, FCA policy statement), that skill tracks the gap.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.

## What this skill does not do

- It doesn't approve the deployment. A human signs the assessment.
- It doesn't constitute any regulatory conformity assessment — where a regime (e.g., EU AI Act) requires a formal conformity assessment, that is a separate exercise requiring external legal review and technical documentation beyond what's here.
- It doesn't substitute for a UK GDPR Art. 35 DPIA when personal data is involved. Run both.
- It doesn't design the mitigations. It describes what needs mitigating; engineering designs the fix.
