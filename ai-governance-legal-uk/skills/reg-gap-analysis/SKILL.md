---
name: reg-gap-analysis
description: >
  Diff a new UK AI regulation, ICO guidance, CMA report, FCA publication, or EU
  AI Act implementing act against your current governance posture — surfaces gaps,
  priorities, and a remediation plan with owners and deadlines. Use when a UK AI
  regulation or guidance moves (or you learn about one you missed), or when user
  says "new guidance just dropped", "does [regulation] affect us", "gap analysis
  for ICO AI guidance", "compliance check against [UK AI law or guidance]",
  "EU AI Act gap analysis", or pastes regulatory text.
argument-hint: "[regulation name, or paste regulatory text, or attach a document]"
---

# /reg-gap-analysis

1. Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. Confirm regulatory footprint and use case registry are populated.
2. Use the framework below.
3. Scope: does this regulation apply? (Jurisdiction — UK domestic vs. EU AI Act with UK nexus; sector; builder/deployer; threshold.) If not, one line and done.
4. Extract requirements. Diff against current state in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
5. Prioritize gaps. Output: remediation plan with must-do / should-do / already compliant / accepted gaps.
6. Save as dated markdown doc for the file.

```
/ai-governance-legal-uk:reg-gap-analysis "ICO AI auditing framework"
/ai-governance-legal-uk:reg-gap-analysis "EU AI Act high-risk provisions — EU nexus confirmed"
/ai-governance-legal-uk:reg-gap-analysis "Online Safety Act 2023 Ofcom algorithmic safety duties"
```

---

## Purpose

ICO publishes updated AI guidance. The CMA publishes a new report on foundation models. The FCA releases a feedback statement on AI in financial services. DSIT announces cross-cutting AI principles. The EU AI Act's implementing acts take effect. Something moves — and now you need to know what, if anything, you have to change.

This skill diffs the new requirement against your current UK AI governance posture (per `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` — use case registry, vendor positions, impact assessment practices, and AI policy commitments) and produces a gap list with a remediation plan.

The UK AI regulatory landscape is moving fast — ICO guidance updates, CMA reports, FCA Dear CEO letters, Ofcom codes of practice under the Online Safety Act, DSIT framework publications, and EU AI Act phased implementation all interact. When a regulation is genuinely ambiguous, say so. Don't paper over uncertainty — legal teams need to know when they're on solid ground versus when they're making a judgment call.

## Load current state

Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`:
- `## Regulatory footprint` — what already applies
- `## Use case registry` — what AI you're actually running, and under what conditions
- `## AI policy commitments` — what you've publicly or contractually committed to
- `## Vendor AI governance` — what vendor positions are in place
- `## Impact assessment house style` — what assessment practices exist

If the regulation clearly doesn't apply (wrong jurisdiction, below threshold, wrong sector, builder/deployer distinction eliminates you from scope), say so directly: "Doesn't apply. Here's why: [reason]. No action needed."

---

## Research first, then workflow

Before running the gap analysis, research the currently operative AI regulatory and guidance landscape for the jurisdictions in the user's footprint. For each regime identify:

- **Scope** — who's covered (provider/builder vs. deployer; sectoral carve-outs; UK domestic vs. EU AI Act extraterritorial reach).
- **Applicability thresholds** — sector, processing type, scale, system category, affected-population size.
- **Risk-tier definitions** — how the regime distinguishes tiers (e.g., ICO "high-risk processing" vs. EU AI Act "high-risk").
- **Substantive obligations** — transparency, documentation, human oversight, bias testing, accountability, vendor flow-down.
- **Enforcement mechanism** — which regulator (ICO, CMA, FCA, Ofcom, MHRA, etc.), what penalties, any private right of action.
- **Effective dates / implementation status** — many UK and EU AI obligations are phased; note which are live vs. upcoming.

Cite the regulatory text / guidance with pinpoint references where possible. Flag provisions subject to ongoing interpretation, consultation, or pending implementing guidance. The UK AI regulatory landscape changes quickly — verify currency against `references/currency-watch.md` before advising.

Build the gap analysis from the researched requirements, not from hardcoded reference tables.

## Workflow

### Step 1: Scope the regulation

Before diffing, answer:

- **Does it apply?** Is this UK domestic law / guidance (e.g., UK GDPR, ICO guidance, Online Safety Act, FCA rules) or EU law that applies to UK companies with EU nexus (EU AI Act)? Jurisdiction, sector carve-outs, builder vs. deployer distinction, threshold.

  **UK domestic vs. EU AI Act.** The EU AI Act is NOT UK domestic law. It applies to UK companies only if they offer AI systems to EU users or deploy AI systems in the EU/EEA. If the company has no EU nexus, EU AI Act obligations do not apply. Always scope this first.

  **Builder/deployer matters a lot.** Many UK sector regimes impose different obligations on the entity that develops/provides the AI system versus the entity that deploys/uses it. Research which role the company occupies under each regime's definitions.

- **When?** Effective date. Enforcement date (often different — e.g., ICO guidance is advisory but treated as indicative of expected practice immediately; Online Safety Act obligations phased in by Ofcom code deadlines). Phase-in periods. Verify currency.

- **What's actually new?** Some "new" AI guidance largely restates existing legal principles (data minimisation, fairness, explainability) applied to AI. Others are genuinely new obligations. Identify the delta from what you already do, not the full text of the guidance.

### Step 2: Extract requirements

Read the regulation, guidance, or summary. List every substantive requirement:

| # | Requirement | Citation | Category |
|---|---|---|---|
| 1 | [requirement] | [section] | [see categories below] |

**Categories:**
- **Transparency** — disclosures to users, employees, or affected parties about AI use; ICO explainability requirements; Art. 22 information obligations
- **Impact assessment** — required documentation before deployment (UK GDPR Art. 35 DPIA; AIA; FRIA under EU AI Act)
- **Human oversight** — mandatory human review, override, or appeals mechanisms; Art. 22 human intervention rights
- **Accuracy / testing** — bias testing, accuracy documentation, validation; FCA model validation expectations
- **Governance** — record-keeping, designated responsible persons, accountability frameworks; ATRS for public sector
- **Vendor flow-down** — obligations to pass down to AI vendors or pass up from AI vendors; UK GDPR processor obligations
- **Prohibited practices** — outright bans on specific AI capabilities or uses (EU AI Act Art. 5 where applicable; ICO red lines)
- **Rights** — what affected parties can request or invoke (Art. 22 rights; Subject Access Requests; rights to explanation)
- **Sector-specific** — FCA model risk management; MHRA AIaMD lifecycle; Ofcom safety duties; CQC care AI; NICE evidence standards

### Step 3: Diff against current state

For each requirement:

```markdown
### [Requirement #N]: [short name]

**Regulation / guidance says:** [requirement, quoted or paraphrased]

**We currently:** [what `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` / AI policy / use case registry / assessment
practice shows]

**Gap:** [None | Partial | Full]

**If partial/full — what's missing:** [specific — not "more documentation" but
"no human review step is documented for [use case category]"]

**Effort to close:** [Policy update only | Process change | Product/system change |
New assessment required | Vendor renegotiation | Registration / filing]

**Risk of non-compliance:** [penalty range, enforcement likelihood, reputational]
```

### Step 4: Prioritize

Not every gap is equal. Sort by:

1. **Hard deadline with teeth** — statutory deadline + active enforcement + real penalties (ICO fines up to £17.5m / 4% global turnover; FCA sanctions; Ofcom fines up to 10% global turnover for OSA)
2. **Prohibited practice** — if the gap is a prohibition, not a process requirement, that's the first priority regardless of enforcement date
3. **Effort-to-impact ratio** — updating policy language is cheap; adding human oversight to a deployed system is not
4. **Use case overlap** — gaps that affect multiple use cases in the registry are higher priority than single-use-case gaps

### Step 5: Remediation plan

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Remediation Plan: [Regulation / guidance name]

**Regulation type:** [UK domestic statute / ICO guidance / UK sector regulation / EU AI Act (EU nexus)]
**Effective / enforcement date:** [date]
**Applies to us as:** [Builder / Deployer / Both]
**Relevant regulator:** [ICO / CMA / FCA / PRA / Ofcom / MHRA / Cabinet Office / EU AI Office — as applicable]

### Must-do before enforcement

| Gap | Fix | Owner | Due | Status |
|---|---|---|---|---|
| [gap] | [specific fix] | [name] | [date] | [ ] |

### Should-do (important but not blocking enforcement)

[same table]

### Already compliant

[list of requirements where gap = None — useful context for the legal/executive
summary of where you actually stand]

### Accepted gaps (risk accepted, not fixing)

[if any — with documented rationale and who accepted the risk. Documenting accepted
risk is better governance than leaving it unaddressed silently.]
```

---

## Research the regulation before building the gap analysis

Do not rely on hardcoded reference tables for specific regimes. For each regulation in scope, research the currently operative text:

- Which obligations apply to the company's role (builder/provider, deployer)?
- What are the live vs. phase-in dates for each obligation?
- Are there implementing guidance documents, statutory codes of practice, or regulator enforcement statements that affect interpretation?
- For sector regulation: what is the sector regulator's stated position on AI governance?

Cite primary sources. Tag model-knowledge citations with the appropriate tier:

- `[settled]` — stable, well-known statutory and regulatory references.
- `[verify]` — real but should be verified: specific ICO guidance versions, FCA publications, Data (Use and Access) Act 2025 provisions, Ofcom codes, effective dates.
- `[verify-pinpoint]` — pinpoint citations carry the highest fabrication risk.

Tool-retrieved citations keep their source tag (`[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`); web-search citations remain `[web search — verify]`.

**For non-lawyer users, uncertain dates, thresholds, and phase-in provisions go in a confirm-list, not inline.** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If Role is **Non-lawyer** and a date, deadline, phase-in, threshold, or effective-date assertion is uncertain, replace the inline assertion with "effective date: confirm with your solicitor/barrister" and collect all uncertain items in a final gap-analysis section: "**Things I'm not certain about — ask your solicitor or barrister to confirm before relying on this:**"

> **No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, govuk MCP, legislation.gov.uk, or firm platform) returns few or no results for a regime's text, delegated act, or guidance, report what was found and stop. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]`, or (4) flag as unverified and stop. A solicitor decides whether to accept lower-confidence sources.

---

## Integration with other skills

**From aia-generation:** AIAs flag regulatory obligations for specific systems → those feed here when a regulation is new or coverage is uncertain.

**From use case triage:** Newly triaged use cases that hit regulatory triggers → gap analysis runs on the specific requirement for that use case type.

**To regulatory-legal-uk plugin, if the plugin is installed:** This skill is the manual version. The monitor plugin watches feeds and triggers this analysis automatically when something relevant changes.

---

## Output

Save as a dated markdown doc. The remediation plan table becomes a tracker — update status as items close.

If the gap analysis concludes "no gaps, we're compliant," still write the doc. It's useful evidence that you looked, and useful baseline when the regulation is amended or the guidance is updated.

**Cite check before relying on this.** Citations here were generated by an AI model and have not been verified against primary sources. Before relying on any citation — statute, regulation, guidance, or case — run a verification pass against a legal research tool (uk-legal MCP, legislation.gov.uk, govuk MCP) for accuracy, currency, and subsequent history. Source tags on each citation show where it came from; `verify` and `verify-pinpoint` tags carry higher fabrication risk and should be checked first.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.

## What this skill does not do

- It doesn't interpret ambiguous regulatory language authoritatively. When the guidance is genuinely ambiguous: say so, state the conservative read, and flag for external counsel if the issue is material.
- It doesn't track regulatory changes proactively. For proactive monitoring, see the `regulatory-legal-uk` plugin, if the plugin is installed.
- It doesn't implement fixes. It plans them.
- It doesn't substitute for sector-specific legal counsel where specialised knowledge is required (financial services AI model risk, MHRA medical device AI, Ofcom online safety AI).
- It does NOT apply EU AI Act as UK domestic law. Always scope EU AI Act analysis to companies with confirmed EU nexus.
