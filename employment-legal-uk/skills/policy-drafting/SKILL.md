---
name: policy-drafting
description: >
  Draft an employment policy with jurisdiction variants where law differs across
  the footprint (England & Wales, Scotland, Northern Ireland, and any other
  countries with employees). Use when the user says "draft a [topic] policy",
  "we need a policy on", "update our [topic] policy", or names a policy gap.
argument-hint: "[policy topic — e.g., 'remote working', 'parental leave', 'sickness absence', 'disciplinary']"
---

# /policy-drafting

1. Load `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, handbook location.
2. Use the workflow below.
3. Draft core policy. Check each jurisdiction in footprint for required variants.
4. Output: core policy + jurisdiction supplements. Flag where law is currently shifting.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A policy that satisfies ERA 1996 minimum standards may need a supplement for
employees covered by a collective agreement, and a Northern Ireland variant
where the parallel legislation differs. This skill drafts a core GB policy and
generates jurisdiction supplements where the footprint requires different rules
or additional statutory content.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, handbook location and format.

## Workflow

### Step 1: Scope the policy

- What's the policy for? (Sickness absence, disciplinary and grievance, parental leave, remote working, data protection, modern slavery, etc.)
- Why now? (Legal requirement, incident, handbook gap, headcount threshold reached, regulatory obligation)
- Who does it apply to? (All employees, workers, certain roles, certain locations)
- Is there a collective agreement or recognised trade union? (Relevant to disciplinary, grievance, and consultation policies.)

### Step 2: Statutory baseline and jurisdictional scan

> **Research the current statutory minimum requirements for this policy topic** before drafting. For every policy topic, identify whether there is a statutory obligation to have a written policy, what it must contain, and whether there is a statutory framework the policy must reflect. Do not draft from memory on statutory requirements — verify currency.

**Common topics with statutory content or mandatory policies:**

| Topic | Statutory basis | Notes |
|---|---|---|
| Disciplinary and grievance | ACAS Code of Practice (TULRCA 1992 s.207A); ERA 1999 s.10 right to be accompanied | Failure to follow ACAS Code → 25% ET uplift. Policy must meet the Code. |
| Parental leave | ERA 1996 Part VIII; Maternity and Parental Leave etc. Regulations 1999; PaternityPay and Shared Parental Leave Regulations | Statutory entitlements are the floor; policy can be more generous. Verify current entitlement periods and pay rates (uprated). |
| Sickness absence and sick pay | SSP (Social Security Contributions and Benefits Act 1992); SSP Regulations 1982 | SSP rate and waiting days — verify current rate (uprated annually). |
| Working time | WTR 1998 | 48-hour opt-out must be documented; rest break entitlements; annual leave accrual. |
| Data protection / privacy | UK GDPR / DPA 2018 | Employee privacy notice is a separate obligation (not just a policy). |
| Whistleblowing | ERA 1996 ss.43A–43L (PIDA); ERA 1996 s.103A | Policy recommended (and often required by regulators/investors); must not discourage qualifying disclosures. |
| Equal opportunities / anti-harassment | EqA 2010 | No mandatory written policy but strongly recommended for s.109(4) "all reasonable steps" defence to vicarious liability. |
| Modern Slavery | Modern Slavery Act 2015 s.54 | MANDATORY statement for organisations with annual turnover ≥ £36m; must be signed by a director and published on website. |
| Gender pay gap reporting | Equality Act 2010 (Gender Pay Gap Information) Regulations 2017 | MANDATORY for employers with ≥250 relevant employees; annual report required. |
| Redundancy | ERA 1996 Part XI; TULRCA 1992 s.188 | Policy (selection criteria, consultation process) recommended; collective consultation obligations are statutory. |
| TUPE | Transfer of Undertakings (Protection of Employment) Regulations 2006 | Information and consultation obligations are statutory. |
| Flexible working | Employment Relations (Flexible Working) Act 2023; ERA 1996 s.80F | Right to request is statutory (now day-1 right); policy must reflect current rules — verify post-2023 changes. |

For each jurisdiction in the footprint, check: does this jurisdiction have a specific rule or variant on this topic?

**GB-wide vs NI:** Most employment law statutes apply across Great Britain (ERA 1996, EqA 2010, WTR 1998). Northern Ireland has parallel legislation. If the footprint includes NI employees, flag where the NI equivalent differs. The differences are generally minor but should be verified.

**International employees:** If the footprint includes employees outside the UK, flag each country — employment law varies materially and a single UK policy cannot safely cover, e.g., Irish, French, or German employees.

If the topic has no jurisdictional variance within GB (dress code, for example), skip the supplements step.

### Step 3: Draft the core policy

One policy. Applies to all GB employees unless supplemented. Clear and readable — employees should understand it without a lawyer.

Structure:
- **Purpose** (one sentence — why this policy exists)
- **Scope** (who it applies to — employees, workers, contractors if relevant)
- **The rule** (what's required/permitted/prohibited)
- **Process** (how to raise an issue, who approves, what happens next, timescales)
- **Questions** (who to contact)

Avoid: legal jargon, nested exceptions, promises the company doesn't intend to keep. This is a handbook policy, not a contract. But it is read by Employment Tribunals — say what you mean and mean what you say.

**Statutory minimum language.** Where a policy topic is governed by a statutory code or regulation, the policy must at minimum reflect the statutory entitlements and procedure. Do not draft a policy that is less than the statutory minimum. Where the employer intends to be more generous, state that clearly.

### Step 4: Jurisdiction supplements

For each jurisdiction in the footprint where the rule differs (primarily Northern Ireland, and any countries outside GB):

```markdown
### Northern Ireland Supplement

Employees working in Northern Ireland are subject to the following
in addition to / instead of the core policy:

- [Specific difference under NI parallel legislation]
- [Cite the NI equivalent legislation]
```

Keep supplements tight. Only what's different — don't repeat the core.

For countries outside the UK: draft a stub noting that local law applies and that a local employment law adviser should review before the policy is rolled out in that jurisdiction.

### Step 5: Cross-check

- Does this policy conflict with anything already in the handbook?
- Does it promise more than the company intends to deliver? (An employment policy is read as a contractual term or at minimum a legitimate expectation — drafting error here is future ET ammunition.)
- Does it need to be consulted on with a recognised trade union or works council before rollout? (For disciplinary and grievance policies, consultation is good practice and may be required under a recognition agreement.)
- Are there any mandatory reporting or publication requirements? (Gender pay gap report, Modern Slavery statement — check whether the headcount/turnover thresholds are met.)

## Output

```markdown
# [Policy Name]

**Version:** DRAFT [date] — not in effect until reviewed and approved
**Applies to:** [all employees / workers in GB / specify]

## Core Policy (England, Wales, and Scotland)

[Full text]

## Northern Ireland Supplement
[If applicable — only what differs]

## [Country] Note
[Stub for non-UK jurisdictions — local law applies; seek local advice before rollout]

---

## Drafting Notes (internal — remove before handbook insertion)

- **Statutory basis:** [what law requires; current rate/entitlement verified as at date]
- **Jurisdictional scan:** [which jurisdictions checked; which have variance]
- **Conflicts with existing handbook:** [none | list]
- **Law currently shifting:** [any area in flux — flexible working post-2023, holiday pay post-Brazel amendments, etc.]
- **Mandatory obligations triggered?** [Modern Slavery / Gender Pay Gap thresholds met? Y/N]
- **Union / collective consultation needed?** [Y/N]
- **Review cadence:** [when to revisit — annual for statutory pay rates; upon legislation change]
```

> **Draft, not a policy in effect.** This is a drafting aid for solicitor or HR adviser review, not a policy you can publish. Employment handbook policies are read by Employment Tribunals and can create enforceable legitimate expectations. A solicitor, qualified HR adviser, or other authorised professional in your jurisdiction reviews, edits as needed, and takes responsibility before the policy is rolled out. Do not publish or distribute this draft unreviewed.

## Handoff

To handbook-updates skill: when this policy is approved, it diffs against the current handbook and flags what changes.

## What this skill does not do

- Approve the policy. It drafts; a human approves.
- Roll out the policy. Communication to employees is an HR workflow.
- Cover every country on earth — only the ones in the footprint. If the footprint expands, re-run.
- State current statutory pay rates (SSP, SMP, NLW) from memory — every rate is researched and cited at the time of drafting.
