---
name: worker-classification
description: >
  Classify a proposed worker engagement — employee, worker (limb (b)), or
  self-employed contractor — by running the applicable UK status tests and
  flagging gaps between the intended arrangement and what the facts actually
  support. Includes IR35/off-payroll working assessment for PSC engagements.
  Prospective use only. Use when someone says "we want to bring on a
  contractor", "should this person be employed or self-employed", "how should
  we classify this person", or describes a proposed working arrangement.
argument-hint: "[describe the proposed arrangement, or just start and I'll ask]"
---

# /worker-classification

Runs the applicable UK classification tests for the proposed arrangement and
flags where the facts don't match the intended structure. Prospective only —
for existing relationships, consult a solicitor.

## Instructions

1. Load `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Run the full workflow below.
3. If the user provides details upfront, extract what's available and ask only about the gaps.

## Examples

```
/employment-legal-uk:worker-classification
We want to bring on a data engineer for 6 months, working out of our
London office, using our tools, embedded in our analytics team.
```

```
/employment-legal-uk:worker-classification
Is our recruiter contractor arrangement okay? She works exclusively for
us, sets her own hours, uses her own laptop, fee per placement.
```

```
/employment-legal-uk:worker-classification
(skill will ask for details)
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The most expensive classification decision is the one nobody made consciously.
Someone describes what they want ("a contractor"), the engagement starts, and
two years later the facts look like employment or deemed employment for tax.
This skill walks the applicable UK tests on the proposed arrangement before it
starts — and tells you when what you're describing doesn't match the structure
you're trying to use.

This skill teaches the reasoning pattern. It does not state the law. Every
test formulation, statutory citation, and case-law development must come from
current research.

## Prospective-only hard gate — run BEFORE intake

**This skill analyses a PROPOSED engagement before the work starts.** Before any substantive intake (Step 1), ask:

> Has this work already started? Is the worker currently engaged, or have they been performing work under this arrangement for any period of time?

If the answer is yes — **STOP**. Do not proceed to Step 1 intake. Classifying an existing arrangement is not a planning exercise; it's a liability assessment with remediation implications: back-pay (NMW, holiday, unlawful deduction from wages), employer and employee NICs arrears, HMRC PAYE exposure, Employment Tribunal claims, and HMRC penalties. That analysis is privileged, led by a solicitor, and coupled with a remediation plan.

Output exactly this block and wait for a response:

> **Out of scope — existing arrangement.**
>
> This skill is designed to analyse a worker engagement *before it starts*, so the classification choice informs how to structure the contract and operations. You've described an arrangement that already exists. Analysing an existing engagement retroactively is a different exercise: reclassification risk assessment coupled with remediation planning — back-pay exposure (NMW, holiday, unlawful deductions), NICs and PAYE arrears, HMRC penalties, Employment Tribunal claim exposure, and prospective restructuring. That work should be privileged, led by a solicitor, and likely coupled with outside counsel review given the financial and enforcement exposure.
>
> Recommended next step: escalate per your config's escalation table (for retroactive classification, this typically routes to GC + outside employment/tax counsel).
>
> **If you want to proceed with the prospective-style analysis anyway for planning purposes, say "proceed anyway" — but understand:**
>
> - The output is NOT a remediation plan and should not be treated as one.
> - The output does NOT scope back-pay, NICs arrears, or HMRC penalty exposure for the period already worked.
> - The output does NOT substitute for the reclassification risk assessment this fact pattern actually calls for.
> - The output will carry a prominent banner and the consequential-action gate will require a solicitor yes before the analysis is treated as reliable.

**Only proceed past this gate with an explicit "proceed anyway".** If the user proceeds anyway, prepend this banner to every output for this session:

```
⚠️ SCOPE MISMATCH — OUT-OF-SCOPE USE
This skill analyses prospective worker engagements. The arrangement here
already exists. This output is the prospective-style analysis the user
requested for planning purposes only — it is NOT a remediation plan, does
NOT scope existing back-pay / NICs / PAYE / HMRC penalty exposure, and does
NOT substitute for the reclassification risk assessment this fact pattern
requires. Escalate to counsel.
```

If the answer to "has this work already started?" is no (genuinely prospective), proceed.

---

## Load context

Read `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, any prior HMRC disputes or ET claims noted, escalation table, and any house classification policy recorded.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → `## Outputs`.

## Workflow

### Step 1 — Information gathering

Ask all of the following in a single block. Briefly explain why — users answer better when they understand what the question is testing.

> To run the right classification tests I need to understand the proposed arrangement in detail. Please answer as many of these as you can:
>
> **The work**
> - What will this person actually do day-to-day?
> - Is this work part of your company's core business, or peripheral to it? (A software engineer at a tech company = core; an IT contractor at a law firm = more peripheral. This is relevant to the integration test.)
> - Is this a defined project with a clear end, or ongoing indefinite work?
> - How specialised is the skill? Does this person have expertise your team doesn't?
>
> **Control**
> - Who sets their hours and schedule — them or you?
> - Where will they work — your office, their location, or either?
> - Will you direct how they do the work (methods, process, sequence), or just what the end result should be?
> - Will they supervise any of your employees?
>
> **Personal service and substitution**
> - Must this specific person do the work personally, or can they send a substitute?
> - If a substitute is permitted: is the substitute subject to your approval? Who pays the substitute?
> - An unfettered right to substitute weighs strongly against worker and employee status — this factor is important.
>
> **Economics and mutuality**
> - How will they be paid — hourly, daily, or fixed project fee?
> - Will you provide equipment, tools, or software, or do they use their own?
> - Do they work for other clients, or will this be exclusive?
> - Will they bear financial risk — can they profit beyond the fee, or lose money on the engagement?
> - When there is no work available, are you obliged to offer work? Are they obliged to accept it?
> - (Mutuality of obligation — the obligation to offer work and the obligation to accept it — is one of the three core elements of employee status in UK law.)
>
> **Structure**
> - Are they engaging as an individual, or via a limited company or personal service company (PSC)?
> - If via a PSC: are you a public-sector body, or a medium/large private-sector business (more than 50 employees or more than £10.2m turnover)? (This triggers the off-payroll working rules.)
> - Will there be a written contract?
> - How long is the engagement expected to run?
> - Will they work alongside your employees doing similar work?
>
> **Purpose of the classification**
> - Which protections or obligations are you thinking about? Employment rights (unfair dismissal, holiday, NMW, WTR), tax/NICs (PAYE vs self-assessment), IR35/off-payroll working, or all three? Different tests apply to each purpose and the answers can diverge.
>
> **Jurisdiction**
> - Where will this person physically perform the work? (E&W / Scotland / NI / mixed)

Wait for responses. Note any gaps — they affect the analysis.

### Step 2 — Identify the applicable tests

> **Research the applicable tests before proceeding.** For the purpose(s) identified in intake, research the currently operative UK classification tests. The three purposes use different (though overlapping) tests:
>
> **Purpose 1 — Employment rights** (ERA 1996, EqA 2010, WTR 1998, NMW Act 1998):
> The *Ready Mixed Concrete (SE & E) Ltd v Ministry of Pensions and National Insurance* [1968] 2 QB 497 three-element test for employee status: (1) personal service by the worker, (2) a wage or other remuneration, (3) a sufficient degree of control. Additional factors from the multi-factor approach developed in subsequent case law. The *Autoclenz Ltd v Belcher* [2011] UKSC 41 principle that written terms are not determinative if they do not reflect the reality of the working arrangement.
>
> For **worker (limb (b))** status: ERA 1996 s.230(3)(b) — an individual who contracts personally to perform work or services for another party who is not their client or customer. The personal service requirement applies but mutuality and control requirements are lower than for employee status. *Uber BV v Aslam* [2021] UKSC 5 and *Pimlico Plumbers Ltd v Smith* [2018] UKSC 29 are the leading Supreme Court cases. Cite and verify currency.
>
> **Purpose 2 — Income tax and NICs** (PAYE/self-assessment):
> HMRC applies common-law employment status factors drawn from ITEPA 2003 and the general law: control, substitution, mutuality, financial risk, equipment, integration, and the overall picture. Research the current HMRC Employment Status Manual (ESM) guidance, particularly ESM0500 onwards on the tests. Note that HMRC's approach and the general law tests are closely aligned but the employment rights tests and the tax tests are applied by different bodies (Employment Tribunal vs HMRC/First-tier Tribunal) and can diverge in borderline cases.
>
> **Purpose 3 — IR35 / off-payroll working** (where engagement is via PSC):
> If the worker is engaging via a PSC and the client is a public-sector body or a medium/large private-sector business, ITEPA 2003 Chapter 10 (off-payroll working rules, as reformed April 2021) applies. The test is whether, if the worker had contracted directly with the client, that contract would constitute employment. The client (not the PSC) is responsible for making the status determination and issuing a Status Determination Notice (SDN). Research the current Chapter 10 test and SDN requirements. For small private-sector clients, Chapter 8 applies and the PSC is responsible for self-assessment. Verify currency — the April 2021 reform shifted responsibility to the client for medium/large private-sector businesses.
>
> Cite the controlling primary sources. Note the effective date and whether any test is subject to recent case law or legislative change. Verify currency. If you cannot verify, flag it.

> **No silent supplement.** If a research query returns few or no results, report what was found and stop. Say: "The search returned [N] results from [tool]. Options: (1) broaden the search, (2) try a different tool, (3) search the web — results tagged `[web search — verify]`, (4) flag as unverified and stop. Which would you like?"
>
> **Source attribution.** Tag every citation: `[uk-legal MCP]` for legislation or case law from the uk-legal MCP; `[BAILII]` for BAILII case law; `[legislation.gov.uk]` for statutory provisions; `[govuk MCP]` for HMRC/GOV.UK guidance; `[web search — verify]` for web searches; `[model knowledge — verify]` for training-data citations. Never strip the tags.

### Step 3 — Apply the researched tests to the facts

For each test, apply it to the intake facts and score each factor explicitly. Use a structure like:

```
Test: [name of test, per research]
Purpose: [employment rights / income tax & NICs / IR35]
Source: [pinpoint cite]
Currency: [verified as of date]

| Factor | Intake facts | Signal |
|---|---|---|
| [Factor from researched test] | [from intake] | [direction] |
...

How this test weighs factors:
[From research — e.g., conjunctive (all three Ready Mixed elements must be met),
multi-factor balancing, or dominant-purpose test]

Result:
[Employee / Worker (limb (b)) / Self-employed — or: Unclear — contested factor X]
```

Repeat for each applicable test and purpose. Where tests give different answers for different purposes, present each on its own track.

**Notes on contested factors.** Mutuality of obligation and the degree of control required for employee (as distinct from worker) status are the most commonly contested elements in UK case law. The distinction between a contractual right to substitute and a genuine, exercised right to substitute is also frequently litigated. Identify contested factors explicitly.

### Step 4 — Classify and flag gaps

**The classification call**

Based on the test results, state the most defensible classification:

- **Employee**: facts support employee status under *Ready Mixed Concrete* / *Autoclenz*; entitled to full employment rights; PAYE applies.
- **Worker (limb (b))**: facts support worker but not employee status; entitled to NMW, WTR, and holiday rights; PAYE likely applies for income tax/NICs.
- **Genuinely self-employed**: facts support self-employed status under all applicable tests; no employment rights; self-assessment for income tax/NICs (absent IR35).
- **IR35 deemed employment (PSC engagement)**: the hypothetical direct contract test suggests deemed employment; client must issue SDN and operate PAYE on fees paid to the PSC.
- **Unclear / close call**: facts cut both ways — state which test is the problem and why.

If the tests give different answers for different purposes, say so explicitly and name the controlling purpose and jurisdiction.

**The gap analysis**

This is the most important output:

```
Intended structure: [what they want]
What the facts suggest: [what the tests say]

Gaps — where the arrangement doesn't match:
🔴 [Factor]: [what they described] conflicts with [intended classification]
   because [researched test language + cite]. Significant misclassification
   risk if the engagement proceeds as described.
🟡 [Factor]: weaker point under [test]. Not disqualifying alone but increases
   risk in combination.
✅ [Factor]: supports [intended classification]. No issue.
```

**Escalation trigger**

Escalate per `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` if any of the following:
- Work is core to the company's business and control/integration factors point toward employment or worker status.
- Prior HMRC dispute or ET claim noted in config — heightened scrutiny applies.
- Worker will supervise employees or make business decisions on behalf of the client.
- Engagement expected to exceed 12 months with no clear project endpoint.
- PSC engagement and the client is a public-sector body or medium/large private-sector business — IR35 SDN required before the engagement starts.
- Any contested factor where the outcome changes the classification.

### Step 5 — Output

> **Research-connector pre-flight.** Before emitting the analysis, check whether a legal research connector is reachable — the uk-legal MCP or BAILII. If no connector returns results in Step 2, record it in the **Sources:** line: e.g., `not connected — cites from training knowledge; the highest-fabrication topics in UK status analyses are the current IR35 off-payroll rules (reformed April 2021), the *Autoclenz*/*Uber* case holdings, and HMRC ESM section references — spot-check those first`.

> **Jurisdiction assumption.** Employment status law under ERA 1996 and NMW Act 1998 applies across Great Britain. The IR35 off-payroll working rules under ITEPA 2003 apply UK-wide including Northern Ireland. Northern Ireland has its own Employment Rights (Northern Ireland) Order 1996 for employment rights purposes — flag NI engagements explicitly.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Worker Classification Analysis
**Proposed arrangement:** [what they described]
**Jurisdiction:** [E&W / Scotland / NI]
**Purpose(s):** [employment rights / income tax & NICs / IR35]
**Tests applied:** [list, each with pinpoint cite and currency date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one sentence]

---

### Classification

**Closest classification:** [Employee / Worker (limb (b)) / Self-employed / IR35 deemed employment / Unclear]

[One paragraph — test results in plain language, tied to cited sources.]

---

### Test results

#### [Test name — per research]
Purpose: [...] | Source: [...] | Currency: [...]
[Scored table from Step 3]
**Result:** [Employee / Worker / Self-employed / Unclear]

#### [Additional tests — repeat]

---

### Gap analysis

[🔴 / 🟡 / ✅ flags from Step 4]

---

### Escalation

[None needed | Escalate to [name] before proceeding — [reason]]

---

### Next steps

[If self-employed viable: "Proceed — ensure the written agreement reflects the terms supporting self-employed status, including a genuine substitution right and no mutuality of obligation."]
[If worker status is right: "Structure as a worker engagement — ensure NMW, WTR, and holiday rights are built into the contract."]
[If employee: "Classification is employee — run `/employment-legal-uk:hiring-review` for the offer letter and ERA s.1 particulars."]
[If IR35: "IR35 applies — issue a Status Determination Notice (SDN) and operate PAYE on fees before the engagement starts. Take specialist tax advice."]
[If gaps: "Address the following before using [intended structure]: [list]"]
[If escalation: "Do not proceed until a solicitor reviews [specific issue]."]
```

## Consequential-action gate (classify a worker)

**Before producing a final classification recommendation:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Classifying a worker has legal consequences — misclassification as self-employed when the facts support worker or employee status exposes the business to NMW/holiday back-pay, NICs arrears, HMRC penalties, and Employment Tribunal claims. IR35 misclassification triggers PAYE liability on the client. Have you reviewed this classification call with a solicitor or employment/tax adviser? If yes, proceed. If no, here's a brief to bring to them:
>
> - The arrangement (work, control, substitution, economics, structure) as described
> - Jurisdiction and which tests were applied
> - Test-by-test results with cites and currency
> - Gap analysis (🔴 / 🟡 / ✅) with contested factors called out
> - Open questions and what's unresolved
> - What could go wrong (NMW/holiday back-pay; NICs/PAYE arrears; IR35 liability; ET claims)
> - What to ask the solicitor (is self-employed status defensible; would restructuring remove the risk; is IR35 in scope; what contract terms are needed)
>
> If you need to find a solicitor specialising in employment or tax law: the SRA's Find a Solicitor tool (sra.org.uk/consumers/find-a-solicitor) is the official public register. For IR35 specifically, consider a specialist employment tax adviser.

Do not produce a final classification recommendation past this gate without an explicit yes. A marked-DRAFT analysis for solicitor review is fine.

---

## What this skill does NOT do

- Analyse an existing relationship retroactively — prospective only.
- Draft the contractor agreement or consultancy terms.
- Advise on remediation if misclassification has already occurred.
- Issue a Status Determination Notice (SDN) — that is the client's legal obligation under ITEPA 2003 Chapter 10; this skill provides the analysis to support that determination.
- State the law on its own — every test, factor, and case must come from verified current research.
- Substitute for a solicitor or tax adviser on close calls.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced. The tree is the output; the lawyer or HR professional picks.
