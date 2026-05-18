---
name: use-case-triage
description: >
  Classify a proposed AI use case against your registry — approved, conditional,
  or not approved — and produce required conditions and next steps. Applies UK
  GDPR Article 22 automated decision-making analysis, ICO AI guidance, and
  sector-specific UK regulatory flags. Flags cross-plugin handoffs to privacy
  or product counsel. Use when user says "triage this use case", "can we use AI
  for X", "is this approved", "what do we need to do to use AI for X".
argument-hint: "[describe the use case, or 'batch' to triage a list]"
---

# /use-case-triage

1. Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. Confirm registry is populated — if not, stop and direct to setup.
2. Use the framework below. Clarify the use case if vague.
3. Registry lookup → red line check → classify.
4. Apply UK GDPR Art. 22 check, ICO AI guidance flags, and sector-specific regulatory overlay.
5. Output: classification, reasoning, conditions table (if conditional), governance tier, cross-plugin handoffs.
6. Propose registry update if use case wasn't already in the registry.

```
/ai-governance-legal-uk:use-case-triage "Sales team wants to score leads with AI automatically"
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ai-governance-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Stop the conversation that happens in a hallway and starts as "can we just use AI for this?" Give a fast, calibrated answer from the registry — and if the answer is conditional, make the conditions concrete and the next step obvious.

The triage skill is a gateway, not a destination. Its job is to classify, flag what's required, and route. The aia-generation skill does the deep work.

## Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` first

Before triaging, always read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. The use case registry and red lines there are authoritative. Generic AI ethics reasoning is not a substitute for what this company has actually decided.

If `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` contains `[PLACEHOLDER]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor the use case registry, red lines, and governance tiers to your practice.
>
> **Two choices:**
> - Run `/ai-governance-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll triage tailored to YOUR practice.
> - Say **"provisional"** and I'll triage against generic defaults — UK jurisdiction, middle risk appetite, solicitor role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run triage normally using these generic defaults: middle risk appetite, solicitor role, UK (E&W) jurisdiction, no registry (classify by UK AI governance principles — UK GDPR, ICO guidance, CMA, sector regulation — rather than matching to a registered entry). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against UK default assumptions. Run `/ai-governance-legal-uk:cold-start-interview` to get output calibrated to YOUR practice — your registry, your jurisdiction, your risk appetite. 2 minutes."

**Jurisdictional scope.** Triage applies the registry, red lines, and governance tiers configured for the regulatory footprint in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. AI rules vary materially by jurisdiction — an APPROVED classification in one footprint may be CONDITIONAL or prohibited in another. If deployment touches a jurisdiction not in the footprint, surface that and re-triage rather than extending by analogy.

---

## Triage process

### Step 1: Understand the use case

Before classifying, make sure you understand what's actually being proposed. If the description is vague, ask:

- "What is the AI doing, exactly — generating content, making a decision, surfacing recommendations, automating a task?"
- "Who or what is the AI acting on — employees, customers, third parties?"
- "Is a human reviewing the AI output before anything happens, or is it automated?"
- "Which vendor or tool is being proposed?"
- "Is this internal-only, or does it touch customers or other external parties?"

---

### Step 2: Registry lookup

Check the use case registry in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` for a direct or close match.

**Direct match:** If the registry has a directly matching entry, apply it.

**Near match:** If the use case is similar to a registry entry but not identical, flag this: "This looks like [registered use case] — I'm applying that classification, but if the scope is meaningfully different, it may need its own assessment."

**No match:** If the use case isn't in the registry, default to CONDITIONAL pending an AI impact assessment. Surface the preliminary read on risk and route to the AIA.

---

### Step 2A: UK GDPR Article 22 check (always run)

Before proceeding with general triage, run a UK GDPR Art. 22 check. This is a UK legal requirement that applies regardless of the registry classification.

> **UK GDPR Article 22 — automated individual decision-making and profiling**
>
> Art. 22 gives individuals rights where a decision is made **solely on the basis of automated processing** (including profiling) which produces **legal or similarly significant effects** on them.
>
> Three questions:
> 1. Is the AI making or significantly influencing a decision about an individual (not just about aggregated data)?
> 2. Is the processing **solely automated** — no meaningful human review before the decision takes effect?
> 3. Does the output produce **legal effects** (e.g., contract terms, access to services, credit, employment) or **similarly significant effects** (effects of the same magnitude — significant financial, reputational, or physical impact)?
>
> If all three: Art. 22(1) applies. Three permitted bases: (a) necessity for contract, (b) authorised by law, (c) explicit consent. Must also provide: meaningful information about the logic involved, the significance and envisaged consequences, and the right to obtain human intervention, express a point of view, and contest the decision.
>
> Source tags for the above: `[settled — UK GDPR Art. 22 as retained EU law; verify any ICO guidance updates — model knowledge — verify]`

Flag the Art. 22 position in the output:

| Art. 22 question | Answer | Flag |
|---|---|---|
| Decision about an individual? | [Yes/No/Unclear] | |
| Solely automated? | [Yes/No/Unclear] | |
| Legal or similarly significant effects? | [Yes/No/Unclear] | |
| **Art. 22 triggered?** | **[Yes/No/Possibly]** | **[review]** if unclear |

If Art. 22 is triggered, add to CONDITIONS: "Human review step required before decision takes effect — or explicit consent and meaningful information obligations must be satisfied."

---

### Step 3: Red line check

Before going further, check the red lines in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

If the use case triggers a red line — even partially, even in a charitable reading — say so immediately.

> "This use case touches [red line]. Your red lines treat this as an automatic no. If there's something different about this situation, that's a conversation for legal sign-off — not a triage call."

Do not soften red line outcomes. If it's a no, it's a no.

---

**UK nations / jurisdiction check.** Ask: "Who's affected, and where are they? Which UK nations? Any EU users?" Then check the use case against EVERY regime in the practice profile's `## Regulatory footprint`, not just the primary one. Flag conflicts:
- "CONDITIONAL under UK law, but if EU residents are affected, EU AI Act obligations may also apply — confirm whether any affected individuals are in the EU/EEA."
- "Standard tier under your governance framework, but if this is in financial services, FCA model risk management expectations apply."
- "Low risk domestically, but if this involves children, the ICO Children's Code (AADC) and age-appropriate design requirements apply."

A use case that crosses jurisdictions gets the strictest applicable treatment.

---

### Step 4: ICO AI guidance and sector-specific overlay

After the Art. 22 check and red line check, apply applicable sector-specific UK regulatory flags:

**ICO AI guidance flags** (applies to any personal data processing):
- High-risk processing requiring a DPIA (UK GDPR Art. 35): large-scale systematic monitoring of individuals, processing of special category data using new technology, automated decision-making with significant effects.
- ICO's list of processing types requiring a DPIA: check current ICO guidance. `[model knowledge — verify against current ICO DPIA guidance]`

**Sector-specific flags** (apply only if the company's regulatory footprint includes the sector):
- **FCA/PRA:** Is this a use case in a regulated financial services firm? Model risk management (PS7/24 / SS1/23) applies to consequential AI in credit, insurance, trading.
- **Ofcom/Online Safety Act:** Is this a use case for an online platform with significant UK user numbers? Systemic risk assessment obligations may apply.
- **MHRA:** Is this a use case for software that meets the definition of a medical device or in vitro diagnostic medical device? MHRA AI as a Medical Device guidance applies.
- **DSIT/ATRS:** Is this a use case in the public sector? Algorithmic Transparency Recording Standard may require a published record.

---

### Source attribution (applies whenever the triage cites regulation)

Triage typically stays high-level, but if the classification depends on citing a regulation, statute, rule, directive, standard, or guidance — tag the citation.

**Source attribution tiering.** For model-knowledge citations, use one of three tiers:

- `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., UK GDPR Art. 22 as a concept, DPA 2018 structure, ICO as the UK supervisory authority). Still verify before certifying, but lower priority.
- `[verify]` — model-knowledge citations that are real but should be verified: ICO guidance versions, FCA publications, sector regulator guidance, effective dates, thresholds, post-2023 amendments, Data (Use and Access) Act 2025 provisions.
- `[verify-pinpoint]` — pinpoint citations (specific article numbers, section references, subsection letters, paragraph numbers) carry the highest fabrication risk and should ALWAYS be verified against a primary source.

Other sources keep their own tags: `[registry]` when drawn from the practice profile's use case registry; `[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`, `[BAILII]` when retrieved from a connected legal research tool; `[web search — verify]` for web-search citations; `[user provided]` for user-supplied citations.

**For non-lawyer users, uncertain dates and thresholds go in a confirm-list, not inline.** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If Role is **Non-lawyer** and an effective date, phase-in, threshold, or deadline is uncertain (would carry `[verify]` or `[verify-pinpoint]` if inline), replace the inline assertion with "effective date: confirm with your solicitor/barrister" and collect all uncertain assertions in a final triage section titled: "**Things I'm not certain about — ask your solicitor or barrister to confirm before relying on this:**"

---

### Step 5: Classification and output

The APPROVED / CONDITIONAL / NOT APPROVED buckets, the red-line definitions, and the CONDITIONAL required-controls list all come from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If the playbook doesn't define a criterion the use case turns on, ask the user: "Your playbook doesn't cover [specific question]. What's your default position? I'll add it to `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` so the next triage is consistent."

**Before issuing an APPROVED classification:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Approving this use case for deployment has legal consequences. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the use case and its scope, how it maps to the registry, the UK GDPR Art. 22 position, what sector-specific flags apply, what could go wrong in deployment, what to ask the solicitor before green-lighting.]
>
> If you need to find a solicitor or barrister: the Solicitors Regulation Authority (SRA) at sra.org.uk, the Bar Council at barcouncil.org.uk for England & Wales; the Law Society of Scotland at lawscot.org.uk; the Law Society of Northern Ireland at lawsoc-ni.org.

Do not proceed past this gate without an explicit yes.

**Format for each triage output:**

---

[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

**USE CASE:** [State the use case as you understand it]

**CLASSIFICATION:** [APPROVED / CONDITIONAL / NOT APPROVED]

**Registry match:** [Direct match / Near match — [name] / No match]

**UK GDPR Art. 22 position:** [Not triggered / Triggered — conditions required / Unclear — [review]]

**Sector-specific flags:** [None / [flag and regulatory basis]]

**Reasoning:**
[1-3 sentences on why this classification.]

**Red lines triggered:** [None / List any that apply]

---

*If CONDITIONAL — required before proceeding:*

| Requirement | Owner | Done? |
|---|---|---|
| [e.g., AI impact assessment] | [AI governance counsel] | ☐ |
| [e.g., UK GDPR Art. 35 DPIA] | [DPO / privacy counsel] | ☐ |
| [e.g., Human-in-the-loop — Art. 22 compliance] | [Product] | ☐ |
| [e.g., Disclosure to affected parties] | [Product / Legal] | ☐ |
| [e.g., Specific vendor only — [approved vendor name]] | [Procurement] | ☐ |
| [e.g., Solicitor sign-off] | [GC / Legal] | ☐ |

**Governance tier:** [Standard / Elevated / High — per `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`]

**Approval path:** [Who needs to sign off, per tier]

**Next step — offer to continue:**

After presenting a CONDITIONAL result, always end with:

> "Want me to start the impact assessment now? I can run the intake questions and produce the assessment document without you needing to run a separate command."

If they say yes, load the `aia-generation` skill and continue in the same conversation — no need to restart. Pass the use case description and governance tier already determined.

---

*If NOT APPROVED:*

**Reason:** [Specific red line, policy prohibition, or registry entry]

**If there's a version of this that could work:** [Optional] Only include if genuinely true.

---

### Step 6: Cross-plugin handoffs

**Privacy handoff:** If the use case involves personal data:

> "This use case involves personal data. A UK GDPR Art. 35 DPIA is likely required in addition to an AI impact assessment (if this is 'high-risk processing'). Use `/privacy-legal-uk:pia-generation [use case]`, if the plugin is installed, to run that in parallel."

**Product counsel handoff:** If this is a new product feature involving AI:

> "If this use case is part of a product launch, loop in product counsel. Use `/product-legal-uk:launch-review`, if the plugin is installed — it will detect the AI component and route to this plugin."

Only flag handoffs that are actually relevant.

---

### Step 7: Registry update suggestion

If this triage resulted in a classification that isn't in the registry yet:

> "I'd suggest adding this to your use case registry. Proposed entry:"

```
| [Use case description] | [Approved/Conditional/Never] | [Conditions if any] | [Reason if Never] |
```

> "Add to `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` → Use case registry."

---

## Batch triage

If the user presents multiple use cases at once — a list, a backlog, a product roadmap — run through each one and output a summary table first, then expand each conditional or not-approved entry:

| # | Use case | Classification | Art. 22? | Key condition / blocker |
|---|---|---|---|---|
| 1 | [use case] | 🟢 Approved | No | — |
| 2 | [use case] | 🟡 Conditional | Possibly | DPIA + human review required |
| 3 | [use case] | 🔴 Not approved | Yes | Automated adverse decision — red line |

---

## Edge cases and failure modes

**"We're already doing this" triage:**
> "This looks like retroactive triage. If this is already running without an assessment, that's a gap to document, not to wave through. I'm searching the registry for any existing entry covering this deployment before running the triage fresh."

**"It's just internal" doesn't change the analysis:**
Internal AI use affecting employees (screening, monitoring, evaluation) is often higher-risk than customer-facing AI — UK GDPR Art. 22 applies to employment decisions. Flag this if the user implies internal scope reduces risk.

**"The vendor says it's safe":**
Vendor representations don't substitute for your own impact assessment.

**"We're just piloting":**
A pilot that touches real employee or customer data is not exempt from triage or impact assessment.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.
