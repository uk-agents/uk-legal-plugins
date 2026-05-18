---
name: feature-risk-assessment
description: >
  Deeper risk assessment for a single feature or product area when the launch
  review found something that needs more than a line item. Structured analysis:
  what could go wrong, how likely, how bad, what mitigates it. Use when user
  says "deep dive on this risk", "risk assessment for [feature]", "what could
  go wrong with", or when launch-review flags a novel issue. UK regulatory
  framing: CMA, ICO, FCA, MHRA, Ofcom, ASA.
---

# Feature Risk Assessment (UK)

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/product-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The launch review is broad. This is deep. When a single issue needs more than a table row — a novel AI feature, a children's product, a financial promotion, something under active CMA or ICO scrutiny — this skill produces a standalone assessment.

Not every launch needs one. Most don't. This is for the 10% where "DPIA triage done, shipped" isn't the right level of scrutiny.

## When to run this

- Launch review found a pattern that's **not in the calibration table** (novel)
- Launch review found something in the **"usually blocks"** category
- GC or leadership asked "what's the risk here" and wants more than a one-liner
- The feature is in an area with **active regulatory attention** (AI, children, financial products, online platforms, medical devices, biometric data)
- CMA, ICO, FCA, MHRA, or Ofcom are actively looking at this space
- Someone outside legal is worried and a structured answer would help

If none of the above, the launch review is enough. Don't generate paperwork for its own sake.

## Structure

### 1. What we're assessing

One paragraph. What the feature does, what's new about it, why it got escalated to a full assessment.

### 2. The risks

For each distinct risk (aim for 2-5, not 15):

```markdown
### Risk [N]: [Short name]

**Scenario:** [What would have to happen for this to go wrong. Be specific —
not "CMA investigation" but "the subscription default-on enrolment triggers
CMA scrutiny under DMCC Act 2024 s 224-227 because users are enrolled without
a single click opt-in at point of first payment."]

**Who gets hurt:** [Users? The company? A third party? Specific.]

**How likely:** [Low / Medium / High — with a reason. "Low — would require
both X and Y to fail simultaneously." Not just a vibes rating.]

**How bad if it happens:** [Low / Medium / High — with a reason. "High —
CMA enforcement notice + potential civil/criminal penalty under DMCC Act 2024"
vs. "Low — ASA challenge requiring copy change, no financial penalty."]

**Existing mitigations:** [What already reduces the likelihood or impact]

**Gap:** [What's missing, if anything]

**Residual risk:** [After existing mitigations — is this acceptable or does
it need more?]
```

### 3. UK Regulatory landscape (if relevant)

Only include if a UK or EEA regulator is actively interested in this space. If so:

- Which regulator (CMA, ICO, FCA, MHRA, ASA, Ofcom, HSE, OPSS), what they've said/done recently
- How this feature would look to them under the relevant statute
- Whether we'd rather they hear about it from us or from a headline
- Any relevant enforcement precedent (CMA decisions, ICO fines, FCA enforcement notices, MHRA actions, ASA adjudications)

**Regulatory footprint by area:**

| Feature area | Regulator | Statute / Code |
|---|---|---|
| Consumer-facing commercial practices | CMA | CPR 2008 `[CPR-2008-REG]`; DMCC Act 2024 `[DMCC-ACT-2024]` |
| Advertising / marketing claims | ASA | CAP Code; BCAP Code `[CAP-CODE]` |
| Personal data processing | ICO | UK GDPR `[UK-GDPR-ART]`; DPA 2018 |
| Financial products / promotions | FCA | FSMA 2000 `[FSMA-2000-S]`; FPO 2005 |
| Medical devices / diagnostics | MHRA | Medical Devices Regulations 2002 |
| Online platforms / user content | Ofcom | Online Safety Act 2023 `[OSA-2023-S]` |
| General product safety | OPSS | GPSR 2005; Product Safety and Metrology etc Act 2024 |
| Children online | ICO | UK GDPR; Children's Code (Age Appropriate Design Code) |

### 4. Precedent (if any)

Has another company faced regulatory action in this space? What happened?

- If nothing bad happened → useful, not dispositive
- If something bad happened → what was different about their situation, does it apply here

Reference UK enforcement actions, CMA decisions, ICO enforcement notices, ASA adjudications, FCA final notices, or relevant Tribunal / High Court judgments. Check the currency of any precedent — CMA enforcement posture under the DMCC Act 2024 is newer than earlier practice under the Consumer Rights Act 2015 and Enterprise Act 2002.

Don't overweight precedent. Regulators change priorities; one company getting away with something doesn't mean the next one will.

### 5. Options

Present 2-3 realistic paths:

```markdown
| Option | Description | Risk reduction | Cost |
|---|---|---|---|
| A: Ship as designed | [current plan] | None | None |
| B: Ship with [mitigation] | [change] | [how much] | [eng effort, timeline, UX] |
| C: Don't ship [component] | [scope cut] | [how much] | [product impact] |
```

### 6. Recommendation

Pick one. Explain why. Acknowledge what you're trading off.

```markdown
**Recommended: Option [X]**

[Why. What risk remains. Why that's acceptable. Who accepts it.]

**If the answer is "not my call":** [Who decides, what they need to know]
```

## Calibration check

Before finalising, check against `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Risk calibration:

- Is this risk assessment calibrated to *this company*, or is it generic?
- A risk that's "High" at a company under an ICO enforcement notice might be "Medium" at one that isn't
- The assessment should reflect the actual UK regulatory posture, enforcement history, and risk appetite captured in the practice profile
- **Financial promotions:** if the feature includes anything that constitutes an invitation or inducement to engage in investment activity (FSMA 2000 s 21), this is a blocker until FCA-authorised approval is confirmed. Do not rate this below "Blocking" without a specific record of confirmed s 21 approval.

## UK-specific risk triggers — check before finalising

Before finalising the assessment, run through this list. If any trigger fires, ensure it is addressed explicitly in the relevant risk block or the Regulatory landscape section:

- **DPIA trigger:** does the feature involve systematic processing of personal data that is likely to result in high risk to individuals? (UK GDPR Art 35 `[UK-GDPR-ART]`) — If yes, DPIA required before launch.
- **Children's Code / Age Appropriate Design Code:** does the feature extend to children (under 18)? (ICO statutory code under DPA 2018) — If yes, gap analysis against the 15 standards required.
- **Online Safety Act risk assessment:** is this a regulated user-to-user service or search service? (OSA 2023, Pts 2-3 `[OSA-2023-S]`) — If yes, Ofcom expects illegal content risk assessments.
- **FCA / FPO financial promotion:** does the feature involve communicating a financial promotion? (FSMA 2000 s 21 `[FSMA-2000-S]`) — If yes, blocker until FCA-authorised person approves.
- **MHRA approval pathway:** does the feature constitute a medical device, in vitro diagnostic, or clinical decision support tool? (Medical Devices Regulations 2002) — If yes, UKCA marking / MHRA approval pathway must be confirmed.
- **Equality Act 2010 accessibility / discrimination:** does the feature use automated decision-making that could directly or indirectly discriminate based on a protected characteristic? — If yes, flag for review under EA 2010 and UK GDPR Art 22.
- **DMCC Act 2024 subscription / drip pricing:** does the feature involve a subscription, free trial with auto-renewal, or multi-stage price reveal? (DMCC Act 2024 `[DMCC-ACT-2024]`) — If yes, confirm compliance with CMA's enhanced subscription contract requirements.

## Handoffs

- **To AI governance:** If the deep-dive was triggered by an AI feature — which it often is — run `/ai-governance-legal:aia-generation [feature]` in parallel or immediately after. The feature risk assessment frames the decision; the AIA documents the AI system specifically in the format AI governance needs.
- **To privacy:** If the feature involves new data collection or processing, run `/privacy-legal:pia-generation [feature]`. For UK products, the DPIA obligation under UK GDPR Art 35 may be mandatory — "PIA needed" should trigger the full assessment, not just a note.
- **To AI governance vendor review:** If the feature uses a new AI vendor, run `/ai-governance-legal:vendor-ai-review [vendor agreement]` if not already done during the launch review.

## Output format

Standalone doc, 2-4 pages. Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

Not a slide deck, not a memo to file — a decision document someone reads and then decides.

Save where `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Launch review process says review docs go. If the doc is going to be shared with anyone outside the privileged loop, drop the work-product header only for that externally-facing copy and keep the privileged original in the matter file.

## Citation check

If the assessment cites cases, statutes, regulations, or enforcement actions — in the Regulatory landscape or Precedent sections especially — those citations were generated by an AI model and have not been verified against a primary source. Before the decision document goes to a decisionmaker, verify each citation:

- UK statutes: check legislation.gov.uk for the current version and any amendments or commencement provisions
- Case law: verify via the uk-legal MCP, TNA Find Case Law (caselaw.nationalarchives.gov.uk), or BAILII
- Regulatory guidance: check the issuing regulator's website for current version
- ASA adjudications: check asa.org.uk
- CMA decisions: check gov.uk/cma
- ICO enforcement: check ico.org.uk/action-weve-taken/enforcement

A risk assessment built on a superseded statute or a misquoted enforcement action is worse than no assessment.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the regime or precedent the assessment needs, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / precedent]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation in the Regulatory landscape and Precedent sections with where it came from: `[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`, `[ICO]`, `[CMA]`, `[ASA]`, `[FCA]`, `[MHRA]` for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the feature team. Citations tagged `verify` carry higher fabrication risk and should be checked first.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't assess every feature. Most features get a launch review and that's it.
- It doesn't make the decision. It frames the decision. Someone with authority picks an option.
- It doesn't do quantitative risk modelling. If the company has a formal risk framework with numbers, use that — this is qualitative.
