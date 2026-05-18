---
name: launch-review
description: >
  Full UK launch review against your framework and risk calibration. Use when the
  user says "review this launch", "legal review for [feature]", "can we ship
  this", "what are the legal issues with [product]", or references a launch
  tracker ticket or PRD that needs a category-by-category review memo. UK
  regulatory framing: CMA, ICO, FCA, ASA/CAP Code, MHRA, Ofcom.
argument-hint: "[PRD file | Drive link | tracker ticket ID]"
---

# /launch-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → framework + calibration. Stop if placeholders.
2. Get PRD + related docs. If tracker connected, pull ticket and comments.
3. Walk every framework category using the workflow below.
4. Calibrate each finding against the table. Novel = flag explicitly.
5. Output review memo in house format. Post summary to ticket if connected.
6. Hand off: marketing-claims-review if substantial marketing; feature-risk-assessment if a finding needs depth.

```
/product-legal-uk:launch-review PROJ-1234
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/product-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the legal professional privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for legal advice) can break privilege. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitised version for the broader channel, or (c) both.

## Purpose

Read the PRD, check every category in this team's framework, calibrate against what actually blocks here (per `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`), and output a review in house format. Goal: a PM reads it and knows exactly what has to happen before they ship — under UK law.

## Load calibration

Read `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`:
- `## Review framework` — the categories to check
- `## Risk calibration` — what blocks vs. what's FYI *at this company*
- `## Launch review process` — output format
- `## Escalation` — when to route up

The calibration table is the difference between this skill and a generic checklist. If the table says "new data collection → DPIA triage, ships in 1-3 days," don't write "this might require a full DPIA and ICO consultation." Match the team's actual practice.

## Workflow

### Step 1: Get the inputs

- **PRD** — from file, Drive, or the launch tracker ticket
- **Spec/design doc** — if separate
- **Marketing plan** — if there is one (hands off to marketing-claims-review if substantial)
- **Launch date** — for urgency calibration
- **Launch tracker ticket** — if connected, pull it for context and comments

If Jira/Linear MCP is connected, pull the ticket history — often there's context in earlier comments that the PRD doesn't capture.

### Step 2: Understand what's launching

Before the checklist, answer in plain English:

- What does this thing do?
- Who uses it — existing users, new users, a new segment?
- What's new vs. what's an extension of something already reviewed?
- Any new data, new vendors, new claims, new jurisdictions?

**AI detection — run before the framework walk.** Check whether this launch uses
AI in any form: a third-party model, an internally built model, an AI-powered
vendor feature, automated scoring or classification, generative content,
recommendations, predictions. Look for this even if the PRD doesn't label it
"AI" — words like "intelligent", "automated", "personalised", "generated",
"suggested" are tells.

If AI component detected → flag it, then run `/ai-governance-legal:use-case-triage [feature]`
alongside the framework walk. Category 8 below handles the detail; this flag
ensures it's never skipped even if the PRD is vague.

### Step 3: Walk the UK framework

For each category in `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Review framework. If the team doesn't have one, use the UK 8-category default below. The categories are stable framing concepts; within each category, research the UK regulatory regimes applicable to the product's sector, audience, and jurisdictions before calibrating severity.

| # | Category | Key question | Auto-skip if |
|---|---|---|---|
| 1 | **Contractual commitments** | Does this conflict with any customer-facing promise (ToS, SLA, marketing materials)? | No customer-facing changes |
| 2 | **Privacy / UK GDPR** | New data collection, new purpose, new sharing? DPIA trigger? | No data changes |
| 3 | **Security** | New attack surface, new data at rest, new access patterns? | UI-only, no backend change |
| 4 | **IP** | Third-party code/content? Open-source licence check? Outputs that could infringe? | No new dependencies, no user-generated content |
| 5 | **Third-party** | New vendor, partner, or integration? DPA in place? | No new external parties |
| 6 | **Regulatory (UK)** | Does this touch a UK-regulated sector, audience, or jurisdiction? Research the applicable UK regimes. | Same users, same sectors, same jurisdictions as existing product |
| 7 | **Marketing claims (ASA / CAP Code)** | Any claims that need CAP Code substantiation? Any financial promotions needing FCA s 21 approval? | No marketing component |
| 8 | **AI governance** | Does this use AI in any form? Is the use case in the registry? DPIA done for automated decisions? Vendor AI terms reviewed? | No AI component detected in Step 2 |

> **No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, govuk MCP, legislation.gov.uk, or equivalent) returns few or no results for a regime, enforcement precedent, or regulator guidance, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution tiering.** Tag every citation in the review with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
>
> - `[settled]` — stable, well-known UK statutory and regulatory references unlikely to have changed (e.g., *Consumer Rights Act 2015*, s 9; *UK GDPR*, Art 5). Still verify before relying on it to clear a launch, but lower priority. Note: for UK law, always check commencement provisions — a provision may be enacted but not yet in force.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific commencement orders, regulatory guidance, CMA decisions, ICO enforcement notices, FCA enforcement actions, ASA adjudications, thresholds, effective dates, post-training amendments.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, paragraph numbers, article numbers) carry the highest fabrication risk and should ALWAYS be verified against a primary source (legislation.gov.uk for statutes; the relevant regulator's website for guidance).
>
> Tool-retrieved citations keep their source tag (`[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`, `[ICO]`, `[CMA]`, `[ASA]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations (from the PRD or seed materials) remain `[user provided]`. Never strip or collapse the tags.
>
> `[platform policy — verify against live docs]` — platform rules (Apple App Store Review Guidelines, Google Play policies, PEGI descriptors, card-network rules, app-store in-app-purchase policies) cited without fetching the live page. Never use `[settled]` for a platform policy — these change without notice.

**For each category, output:**

```markdown
### [N]. [Category]

**Checked:** [what you looked at]
**Finding:** [Clear | Needs work | Blocker | Skipped]
**Detail:** [what the issue is, if any — specific to the PRD, not generic]
**Calibration:** [per the config CLAUDE.md — this is usually an FYI / usually needs X / usually blocks]
**Action:** [what has to happen, who owns it, by when]
```

**Auto-skip honestly.** If a category doesn't apply, say so with a one-line reason. Don't pad.

**UK sector hints.** The 8-category framework above is enterprise-SaaS-shaped. If the launch involves any of the sectors below, add the overlay: ask the overlay question alongside the base-framework question for each affected category, and surface the sector-specific UK regime before calibrating severity.

| Sector | UK overlay regimes to surface |
|---|---|
| **Children / minors** | UK GDPR `[UK-GDPR-ART]` + ICO Age Appropriate Design Code (Children's Code) for services likely to be accessed by under-18s; PEGI age ratings for games; OSA 2023 `[OSA-2023-S]` content harmful to children provisions; ASA / CAP Code rules on advertising to children |
| **Gaming / loot boxes / in-game currency** | Gambling Act 2005 (prize draws vs. skill competitions; loot boxes as prize gaming); PEGI descriptors (In-Game Purchases; Real Gambling); ASA / CAP Code gambling rules; platform store policies (Apple, Google, console); verify current DCMS / DCSE position on loot box regulation |
| **Financial / fintech** | FSMA 2000 s 21 `[FSMA-2000-S]` financial promotions approval (criminal offence without FCA-authorised approval); FCA Consumer Duty (if retail financial product or service); Payment Services Regulations 2017; Electronic Money Regulations 2011; FCA CASS rules; FCA regulated activity authorisation requirements |
| **Health / medical** | MHRA medical devices registration pathway; UKCA marking; Medical Devices Regulations 2002; Medicines Act 1968; NHS Digital / DTAC (Digital Technology Assessment Criteria) for NHS-facing products; General Medical Council code for AI-assisted clinical decision support |
| **Education** | UK GDPR `[UK-GDPR-ART]` + ICO Children's Code for student data; DfE safeguarding guidance; Ofsted inspection criteria if assessed |
| **Employment / HR tech** | Equality Act 2010 (AI-assisted hiring / performance tools — indirect discrimination); ICO employment practices guidance; UK GDPR Art 22 (automated decisions affecting employees); Immigration, Asylum and Nationality Act 2006 (right-to-work checks if integrated); IR35 / off-payroll rules if classification feature |
| **Consumer / retail / marketing** | CPR 2008 `[CPR-2008-REG]`; DMCC Act 2024 `[DMCC-ACT-2024]` (subscription traps, drip pricing, fake reviews); CMA Green Claims Code (environmental claims); CAP/BCAP Code `[CAP-CODE]`; Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 (distance selling); ASA substantiation standards |
| **Online platforms / user-generated content** | Online Safety Act 2023 `[OSA-2023-S]` (regulated services: user-to-user, search; illegal content duties; children's safety duties); Ofcom codes of practice; NetzDG / DSA where EEA users served |

If a sector hint fires and no dedicated category in the base framework covers it, insert it as a category (e.g., "6a. Sector overlay — children / ICO Children's Code + OSA 2023"). Don't let it disappear into category 6 Regulatory as an afterthought; the sector regime often supplies the controlling floor, not a footnote.

### Step 4: Calibrate severity

For each finding, check against the calibration table in `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`:

- If it matches a "usually FYI" pattern → note it, don't block
- If it matches "usually requires work" → specify the work, estimate timeline from the table
- If it matches "usually blocks" → flag prominently, route per escalation table
- If it's **novel** (not in the table) → say so explicitly: "This doesn't match any pattern in the calibration — needs a human call"
- **Financial promotion without FCA s 21 approval** → always Blocking, regardless of calibration table. Do not downgrade.

### Step 5: Assemble the review

Format per `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Launch review process → output format. Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`). If no house format is specified:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Launch Review (UK): [Feature name]

**Reviewed:** [date] | **Launch date:** [date] | **Reviewer:** [name]
**PRD:** [link] | **Ticket:** [link if connected]

---

## Bottom line

[One paragraph: can this ship? What has to happen first?]

**Call:** [Clear to ship | Ship with conditions | Blocked pending X | Needs escalation]

> **Before emitting a "Clear to ship" or "Ship with conditions" call:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:
>
> > Clearing a launch is a legal act — once the product ships, the company is committed to the legal posture documented here. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
> >
> > [Generate a 1-page summary: the launch, the findings by category, any open questions, the residual risk after conditions, and the three things to ask the solicitor before the launch goes out.]
> >
> > If you need to find a solicitor: the SRA Find a Solicitor tool (sra.org.uk) is the fastest starting point. The Law Society of England and Wales also operates a referral service.
>
> Do not proceed past this gate to a "Clear to ship" or "Ship with conditions" call without an explicit yes.

---

## Findings by category

[All the category blocks from Step 3 — skip-noted categories at the bottom]

---

## Action items

| # | Item | Owner | Due | Blocking? |
|---|---|---|---|---|
| 1 | [specific] | [PM/eng/legal] | [date] | Yes/No |

---

## Escalations

[If any — who, why, drafted per escalation skill]

---

## Notes for next time

[If this launch surfaced a pattern that should update the calibration table]

---

## Citation check

Any statutes, regulations, regulatory guidance, case law, or enforcement actions referenced in this review were generated by an AI model and have not been verified against a primary source. Before relying on a citation in a launch decision, verify it:
- UK statutes: legislation.gov.uk (check for current version and commencement)
- Case law: TNA Find Case Law, BAILII, or the uk-legal MCP
- Regulatory guidance: CMA, ICO, FCA, ASA, MHRA, Ofcom — check the issuing regulator's website
Source tags on each citation (e.g., `[uk-legal MCP]`, `[web search — verify]`) show where it came from; `[verify]` tags carry higher fabrication risk and should be checked first.
```

### Step 6: Produce BOTH outputs — the privileged memo AND the redacted ticket comment

⚠️ **Privilege warning:** Posting the full privileged memo to a Jira/Linear ticket that is widely shared with engineering, PM, and other non-legal roles may waive legal professional privilege. Don't paste the full memo into a broadly-shared ticket.

**Both of the following are REQUIRED outputs of this skill.** Neither is optional. Print them in the order below, with a clear divider between them.

**Output 1 — Privileged launch review memo.** The full analysis assembled in Step 5: work-product header, bottom line, findings by category with risk rationale, action items, escalations, notes for next time, citation check. This is internal legal work product. Keep it in your matter file. Distribute only to people inside the privilege circle.

**Output 2 — Redacted ticket-comment block — SAFE TO POST TO TRACKER.** After the memo, with a clear `---` divider and the header `## SAFE TO POST TO TRACKER (non-privileged)`, produce a short comment block containing ONLY:

- **Launch status:** green / yellow / red (i.e., Clear to ship / Ship with conditions / Blocked pending X / Needs escalation)
- **Conditions as action items:** each condition is a bullet, written as an instruction to the PM/eng ("add DPIA link to ticket before ship", "remove 'best on the market' language from homepage copy"). No legal reasoning.
- **Deadline per condition.**
- **Owner per condition.**

The redacted block contains NO work-product / privilege header, NO risk rationale, NO internal legal discussion, NO regulatory citations, NO escalation notes.

Example:

```markdown
---

## SAFE TO POST TO TRACKER (non-privileged)

**Launch status:** Blocked pending conditions below.

**Conditions:**
- [ ] Attach completed DPIA triage to ticket — Owner: [PM] — Due: [date]
- [ ] Remove "most accurate on the market" copy from homepage draft — Owner: [Marketing] — Due: [date]
- [ ] Confirm FCA s 21 approval in writing before publish — Owner: [Legal] — Due: [date]
```

Paste Output 2 (and only Output 2) to the tracker.

## Handoffs

- **To marketing-claims-review:** If there's a substantial marketing component, hand off the claims section — particularly any ASA / CAP Code substantiation questions or potential financial promotions.
- **To feature-risk-assessment:** If a finding is complex enough to need its own doc (e.g., novel AI feature, children's product, financial promotion pathway), spawn a deeper assessment.
- **To privacy:** If the launch touches personal data, run `/privacy-legal:use-case-triage [feature]`. If triage returns DPIA REQUIRED (UK GDPR Art 35), run `/privacy-legal:pia-generation [feature]`. Don't just note "DPIA needed" — trigger it.
- **To AI governance:** If an AI component was detected in Step 2, run `/ai-governance-legal:use-case-triage [feature]`. If a new AI vendor is involved, run `/ai-governance-legal:vendor-ai-review [vendor agreement]`.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't replace a conversation with the PM. Often the PRD is wrong or out of date — the review surfaces questions, a human asks them.
- It doesn't approve the launch. It informs the approval.
- It doesn't retroactively calibrate. If this launch turns out fine (or badly) in a way that should update the calibration table, a human updates `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`.
