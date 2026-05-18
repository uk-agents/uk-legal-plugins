---
name: memo
description: >
  IRAC-scaffolded UK case analysis memo with research gaps flagged in OSCOLA
  citation style — the scaffold, not the analysis. Rule blocks are RESEARCH
  NEEDED, Application is STUDENT ANALYSIS prompts, Conclusion is blank.
  Use when a student needs to scaffold a case analysis memo, write up their
  analysis, or build an IRAC memo for a UK clinic case.
argument-hint: "[optional: specific issue to focus]"
---

# /legal-clinic-uk:memo

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice areas, jurisdiction.
2. Use the workflow below. Read intake summary / case notes.
3. Frame issues as questions. Scaffold IRAC for each — Rule blocks are RESEARCH NEEDED, Application is STUDENT ANALYSIS prompts, Conclusion is blank.
4. Strengths/weaknesses/open questions. Research gaps summary.
5. Output with prominent "the analysis is yours" label. OSCOLA citation format throughout.

```
/legal-clinic-uk:memo
```

---

# Memo: Internal Case Analysis

## Purpose

The case analysis memo is where the student's thinking lives. This skill provides the IRAC scaffolding and flags the research gaps — the student fills in the analysis.

**The analysis is the student's.** This skill structures; it doesn't conclude.

Citations in this skill follow **OSCOLA** (Oxford University Standard for the Citation of Legal Authorities). Citation starts are provided in OSCOLA format as a research orientation; they are explicitly unverified and must be checked before use.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice areas, jurisdiction (E&W / Scotland / NI), supervision style.
Intake summary and case notes for facts.

## Pedagogy check

Read the supervisor guide for this practice area at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Check the `pedagogy_posture` setting:

- **`guide` (default):** Produce the IRAC structure and the research-gap list. Ask the student to draft each rule statement themselves from research. Give feedback on what they wrote. Offer to fill the framework rule for a section only when the student has tried once.
- **`assist`:** Produce the memo scaffold and fill what can be filled. The `[STUDENT ANALYSIS]` and `[STUDENT CONCLUSION]` blocks remain blank by design — `assist` fills the IRAC scaffold and framework rule statement; it does not produce the application or the conclusion.
- **`teach`:** Don't produce the framework or the scaffold content. Ask the student to frame the issues, state the rules from their research, and do the application. Give feedback. Ask leading questions when they're stuck.

If no guide exists, use `guide`. Whatever the posture, the output always includes: "**Pedagogy mode: [assist/guide/teach]** — set by your supervisor's guide."

## Workflow

### Step 1: Frame the issues

From the intake summary and case notes: what are the legal questions this case presents?

State each as a question. Not "Section 21 validity" — "Is the Section 21 notice valid under the Deregulation Act 2015 and Housing Act 1988, and are the preconditions in ss.21A–21B satisfied (deposit protected, gas safety certificate served, EPC provided, 'How to Rent' guide)?"

If there are multiple issues, each gets its own IRAC block.

### Step 2: Scaffold the IRAC

For each issue:

**Issue:** Stated as a question (from Step 1).

**Rule:** This is a research gap, not a conclusion. State what the student needs to find:

> `[RESEARCH NEEDED: Section 21 validity requirements — Housing Act 1988 ss.21, 21A–21B as amended by the Deregulation Act 2015; associated regulations on prescribed information. Check legislation.gov.uk for current text. Also check: whether any saving provisions apply for tenancies starting before the 2015 commencement date (1 October 2015). OSCOLA starting form: Housing Act 1988, s 21 as amended by Deregulation Act 2015, s 35. See /legal-clinic-uk:research-start for a full roadmap.]`

If the skill has high confidence in the general rule framework, state that as a starting point — **but explicitly mark it as unverified**:

> *Framework (unverified — confirm via legislation.gov.uk and case law):* The Housing Act 1988 s 21(1)(b) requires two months' written notice. The Deregulation Act 2015 introduced additional preconditions: the deposit must be protected in an authorised scheme and prescribed information given (ss 21A–21B, Housing Act 1988); a gas safety certificate, EPC, and 'How to Rent' guide must have been given to the tenant.
> `[VERIFY: all preconditions, current statute text on legislation.gov.uk, s 21A–21B as in force — Housing Act 1988, ss 21A, 21B (inserted by Deregulation Act 2015, s 35)]` `[model knowledge — verify]`

**Application:** This is where the student's analysis goes. Scaffold the structure, don't fill it:

> `[STUDENT ANALYSIS: Apply the rule to the facts. Key facts to address:
> - Was the deposit protected and prescribed information given within 30 days? (Housing Act 2004 ss 213–215; deposit scheme provider evidence needed)
> - Was a gas safety record served before occupation and annually since? (Gas Safety (Installation and Use) Regulations 1998, reg 36(6))
> - Was an EPC provided? (Energy Performance of Buildings (England and Wales) Regulations 2012)
> - Was the 'How to Rent' guide provided (in correct version)? (Assured Shorthold Tenancy Notices and Prescribed Requirements (England) Regulations 2015)
> - Was Form 6A used for the notice? When was it given, and what period?]`

List the facts that matter. Let the student do the applying.

**Conclusion:** Explicitly blank:

> `[STUDENT CONCLUSION: Based on your research and analysis above, is the Section 21 notice valid? If not valid, which precondition(s) fail? What is the practical consequence for the client?]`

### Step 3: Identify strengths, weaknesses, open questions

Separate section:

**Strengths (apparent from facts — student should test these):**
- [Fact that seems helpful and why]

**Weaknesses (apparent from facts — student should assess how serious):**
- [Fact that seems harmful and why]
- `[UNCERTAIN: whether [X] is actually a weakness — depends on [jurisdiction] rule on [Y]]`

**Open questions (things the memo can't answer without more info):**
- Factual: [what we don't know from the client]
- Legal: [what needs research]
- Strategic: [judgment calls for the student/supervisor]

## Output

```markdown
═══════════════════════════════════════════════════════════════════════
  AI-ASSISTED SCAFFOLD — THE ANALYSIS IS YOURS TO WRITE
  Every [RESEARCH NEEDED] and [STUDENT ANALYSIS] block is a prompt, not
  a placeholder to delete. The thinking happens when you fill them in.
  OSCOLA citation starts are unverified leads — check every one.
═══════════════════════════════════════════════════════════════════════

# Case Analysis Memo: [Client] — [Matter]

**Date:** [date] | **By:** [student] | **For:** [Supervisor]

---

## Bottom line

[Take the case / Decline because X / Need more info on Y — next step is Z]

---

## Issues Presented

1. [Issue as question]
2. [Issue as question]

---

## Issue 1: [Issue]

### Rule

[Framework starting point with VERIFY flags, and RESEARCH NEEDED blocks.
OSCOLA citation starts where applicable.]

### Application

[STUDENT ANALYSIS scaffold with the facts that matter]

### Conclusion

[STUDENT CONCLUSION — blank]

---

[repeat for each issue]

---

## Strengths

[list with caveats]

## Weaknesses

[list with UNCERTAIN flags where applicable]

## Open Questions

**Factual:** [list]
**Legal:** [list — these feed /legal-clinic-uk:research-start]
**Strategic:** [list — these are for discussion with Supervisor]

---

## Research gaps summary

[Every RESEARCH NEEDED block pulled out into one list, so the student can
work through them systematically — and can run /legal-clinic-uk:research-start on each]

═══════════════════════════════════════════════════════════════════════

## What this memo is NOT

This is a scaffold, not an analysis. The [STUDENT ANALYSIS] blocks are where
the educational value lives — filling them in is the work. A memo where those
blocks are still empty is a memo that hasn't been written yet.

---

**Cite verification — required before use.** Any framework rules, cases, or statutes suggested above were generated by an AI model and have not been verified. Before relying on any citation — or including it in client work — run it through Westlaw UK, LexisNexis UK, BAILII, or legislation.gov.uk for accuracy and current-law status. Citations are formatted in OSCOLA style as a starting structure; confirm format and accuracy before finalising. Flag unverified citations to your supervisor.

**Source attribution.** Tag every suggested citation with where it came from: `[uk-legal]`, `[BAILII]` or `[legislation.gov.uk]` for citations retrieved from a legal research connector or official source this session; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations supplied by the supervisor or case file. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

**No silent supplement.** If a query to a configured research tool returns few or no results for a rule the memo needs, say so and stop. Do NOT fill the gap from web search or model knowledge without asking.
```

## What this skill does NOT do

- **Write the analysis.** It scaffolds the IRAC and flags the gaps. The student reasons through the application.
- **Provide verified rules.** Every rule statement is explicitly unverified until the student researches it.
- **Reach conclusions.** The C in IRAC is blank on purpose.
- **Replace the conversation with the supervisor.** The Open Questions / Strategic section is the agenda for that conversation, not a substitute.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced.
