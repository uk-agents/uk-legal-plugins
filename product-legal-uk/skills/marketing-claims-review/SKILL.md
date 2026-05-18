---
name: marketing-claims-review
description: >
  Review marketing copy for claims that need ASA/CAP Code substantiation,
  reframing, or cutting. Use when the user says "review this marketing copy",
  "check these claims", "can we say this", "is this puffery or a problem",
  or pastes marketing content (landing pages, emails, ads, taglines). UK
  regulatory framing: ASA/CAP Code/BCAP Code, CPR 2008, DMCC Act 2024,
  CMA Green Claims Code, FSMA 2000 s 21.
argument-hint: "[paste copy, or file path]"
---

# /marketing-claims-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Marketing claims standards.
2. Apply the claim taxonomy and review workflow below.
3. Extract every claim. Classify: puffery / factual / comparative / implied / absolute / green / financial.
4. For each non-puffery claim: substantiation check under CAP Code, suggested fix.
5. Check for financial promotions requiring FCA s 21 approval.
6. Output: claim-by-claim with calls, suggested revision if short enough.

```
/product-legal-uk:marketing-claims-review
[paste landing page copy]
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/product-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Marketing wants to say the product is the best. Legal needs it to be true, or at least not provably false and not a regulatory problem. In the UK, the ASA / CAP Code is the primary mechanism for substantiation challenges — an ASA adjudication is cheaper for competitors to trigger and faster to resolve than litigation, which makes it a real enforcement risk even for small campaigns. This skill finds the claims that will get an ASA complaint or a CMA letter, and suggests how to keep the energy while fixing the exposure.

**Financial promotions — mandatory first check.** Before any other analysis, scan the copy for any element that could constitute a financial promotion under FSMA 2000 s 21 `[FSMA-2000-S]` — any invitation or inducement to engage in investment activity. If present, this is a **Blocking finding** regardless of other analysis. The copy cannot go out until an FCA-authorised person has approved it. Flag this before proceeding with the rest of the review.

## Load standards

Read `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → `## Marketing claims`:
- Comparative claims policy (allowed with substantiation / discouraged / never)
- Substantiation standard (what's required before a claim ships)
- Common rejected claims (learn from history)
- Financial promotions approver (FCA-authorised person identified?)

## Research the applicable UK standards before clearing copy

Research the currently operative UK advertising and substantiation standards for the applicable jurisdictions and media. The primary UK frameworks are:

- **CAP Code** (Committee of Advertising Practice, non-broadcast) `[CAP-CODE]` — applies to online ads, emails, brochures, printed materials, social media
- **BCAP Code** (Broadcast Committee of Advertising Practice) `[CAP-CODE]` — applies to radio and TV advertising
- **CPR 2008** `[CPR-2008-REG]` (Consumer Protection from Unfair Trading Regulations 2008) — applies to commercial practices more broadly, including online presentations and checkout flows
- **DMCC Act 2024** `[DMCC-ACT-2024]` — CMA's enhanced powers on fake reviews, drip pricing, subscription traps, and misleading commercial practices
- **CMA Green Claims Code** (2021) — for environmental / sustainability claims
- **FSMA 2000, s 21** `[FSMA-2000-S]` — financial promotions must be approved by FCA-authorised person before communication

Identify what substantiation the *specific claim* requires — who measured it, when, sample size, apples-to-apples basis — not just whether *some* substantiation exists on file. The CAP Code requires that marketing communications be "substantiated, if challenged" (CAP Code rule 3.7). Flag implied claims and comparative claims for heightened scrutiny. Verify currency: ASA guidelines and adjudications update constantly.

> **Only cite the standards that apply to the specific claims under review.** A blanket list of every CAP rule, CPR provision, or CMA guidance note makes the load-bearing ones invisible. A standard earns its place in the output by mapping to a specific quoted claim; otherwise drop it.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the applicable standard, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority before relying, or (4) flag as unverified and stop.
>
> **Source attribution tiering.** Tag every citation with its source. For model-knowledge citations:
>
> - `[settled]` — stable, well-known UK advertising law references unlikely to have changed (e.g., CAP Code rule 3.1 on truthfulness; CPR 2008 as a concept). Still verify before approving copy, but lower priority.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific ASA adjudications, CAP guidance notes, CMA decisions, platform policies, effective dates, recent updates.
> - `[verify-pinpoint]` — pinpoint citations (specific rule numbers, paragraph numbers, case references) carry the highest fabrication risk and should ALWAYS be verified against a primary source (asa.org.uk for adjudications and CAP guidance; gov.uk/cma for CMA decisions).
>
> Tool-retrieved citations keep their source tag; web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`.

## Claim taxonomy

The categories below are structural patterns the reviewer should be able to recognise. Whether a given phrase is actionable under UK law depends on the currently operative CAP Code rule or statutory provision in the applicable jurisdiction, the specific substantiation available, and the audience — research that before concluding.

### Vague / subjective claims (puffery equivalent)

Subjective assertions with no measurable content. The ASA distinguishes between puffery (non-actionable) and specific objective claims that require substantiation. The line depends on whether a reasonable person would take the claim as a factual assertion.

| Example |
|---|
| "The best way to manage your projects" |
| "You'll love it" |
| "Revolutionary" |

### Specific factual claims

Measurable, specific, a reasonable person might rely on it. Under CAP Code rule 3.7, advertisers must hold substantiation before a claim is made.

| Example | Substantiation to look for |
|---|---|
| "50% faster than [competitor]" | Benchmark data, disclosed methodology, date — comparative advertising rules (Business Protection from Misleading Marketing Regulations 2008) apply; comparison must be objective, verifiable, not misleading |
| "Trusted by 10,000 companies" | Actual count (not cumulative signups — *currently* trusted) |
| "Saves 5 hours per week" | Study or customer data, disclosed sample — CAP Code rule 3.7 |
| "Enterprise-grade security" | What does that mean? ISO 27001? SOC 2? Spell it out or it's a promise without content |
| "GDPR compliant" | Specific: what processing? What lawful basis? "Compliant" is a high bar — "designed with UK GDPR in mind" or "supports your GDPR obligations" are safer unless you can back the blanket claim |

### Comparative claims (heightened scrutiny)

Naming a competitor or implying one. The *Business Protection from Misleading Marketing Regulations 2008* (BPR 2008) govern comparative advertising in the UK: comparisons must be objective, verifiable, relevant, and not misleading.

| Example | Fix pattern |
|---|---|
| "Faster than [Competitor]" | Either name the competitor with head-to-head data you can defend (meeting BPR 2008 criteria), or abstract to "faster than legacy tools" with substantiation |
| "The only platform that does X" | False if anyone else does X — "The first platform to..." (if true) or drop "only" |
| "[Competitor] can't do this" | Show your feature. Let the viewer compare. |

Per `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` — if comparative claims are "never," flag all of them. If "allowed with substantiation," check that the comparison is objective, verifiable, and not misleading under BPR 2008.

### Implied claims

Not stated outright but a reasonable reader infers it. Under CAP Code rule 3.1 and CPR 2008, implied claims carry the same substantiation burden as express claims if a significant proportion of consumers would take the implied meaning.

| Example | Implication | Fix |
|---|---|---|
| "Finally, a secure alternative" | Competitors are insecure | "Finally, security you can verify" |
| Customer logos without context | These companies endorse us | "Customers include..." is fine; "Trusted by..." implies more |
| "Built for healthcare" | Clinically validated / MHRA approved | Clarify or qualify |
| "The sustainable choice" | Lower environmental impact than alternatives | CMA Green Claims Code: substantiate specifically or don't claim |

### Absolute claims

No room for error. One counter-example makes them false.

| Example | Fix pattern |
|---|---|
| "Never goes down" | "99.9% uptime" (with SLA that defines it) |
| "100% accurate" | A specific, substantiated percentage tied to a benchmark |
| "Guaranteed" | Only if you actually offer a guarantee with terms — creates contractual obligations under *Consumer Rights Act 2015* `[CRA-2015-S]` |
| "Always" / "Every" | "Typically" / "Most" |

### Green / environmental claims — heightened scrutiny

The CMA Green Claims Code (2021) requires that environmental claims must be:
1. Truthful and accurate
2. Clear and unambiguous
3. Not omit or hide important information
4. Only make fair and meaningful comparisons
5. Consider the full life cycle of the product
6. Substantiated

| Example | Problem | Fix |
|---|---|---|
| "Eco-friendly" | Vague — what aspect? | "Made from X% recycled materials" (substantiated) |
| "Carbon neutral" | Requires independent verification and does not mask high absolute emissions | Disclose methodology, verification, and limitations |
| "Sustainable" | Unsubstantiated | Specify what is sustainable and the evidence |
| "Green" / "clean" | Vague | Replace with specific, substantiated claim |

Green claims are actively enforced by the CMA and ASA. The DMCC Act 2024 `[DMCC-ACT-2024]` expands CMA's enforcement powers in this area.

### Financial promotions — mandatory blocking check

**This check runs first, before the rest of the taxonomy.** If any element of the copy could constitute a financial promotion under FSMA 2000 s 21 `[FSMA-2000-S]` — any invitation or inducement to engage in investment activity, including buying shares, investment products, bonds, crypto assets, or insurance investment products — this is a **🔴 BLOCKER** until:

1. An FCA-authorised person (identified in the practice profile under `## Marketing claims → Financial promotions`) has reviewed and approved the copy in writing; or
2. The copy is confirmed not to constitute a financial promotion.

Do not proceed with the rest of the review for any copy containing a potential financial promotion until this is resolved. Communicating an unapproved financial promotion is a criminal offence under FSMA 2000 s 25.

## The review

### Step 1: Financial promotions scan (mandatory)

Before extracting claims, scan the entire copy for any element that could constitute a financial promotion (see above). If present:

```markdown
🔴 **FINANCIAL PROMOTION DETECTED — BLOCKER**

This copy contains content that may constitute a financial promotion under FSMA 2000 s 21 [FSMA-2000-S]. The highlighted passage(s) must be reviewed and approved by an FCA-authorised person before this copy can be published.

**Passage(s):** "[exact quote]"
**Reason:** [why this may constitute a financial promotion]
**Next step:** Confirm whether the FCA-authorised approver identified in the practice profile ([name, or "not yet identified"]) has been engaged.

The remainder of this review covers non-financial claims. None of the non-financial findings below override this blocker.
```

### Step 2: Extract every claim

Read the copy. List every sentence or phrase that asserts a fact, makes a comparison, or promises something. Ignore pure subjective puffery in the list.

### Step 3: Classify and check

For each claim:

```markdown
**Claim:** "[exact quote]"
**Type:** [Specific factual | Comparative | Implied | Absolute | Green/environmental]
**Substantiation on file:** [Yes — link | No | Unknown]
**Applicable UK standard:** [CAP Code rule X.X | BPR 2008 | CMA Green Claims Code | CPR 2008 Sch 1 | Other]
**Call:** [✅ Fine | ⚠️ Needs substantiation | ⚠️ Needs rewording | 🔴 Cut]
**Suggested fix:** "[alternative phrasing that keeps the energy]"
**Why:** [one line]
```

### Step 4: Check against the product

Does the product actually do what the copy says? Not a philosophical question — check the PRD or ask the PM.

Common drift: marketing copy written from an early spec, product changed, nobody updated the copy. Under CAP Code rule 3.1, the copy must not materially mislead — copy that described an unimplemented feature creates consumer expectation the product cannot meet.

### Step 5: Output

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Marketing Review (UK): [Campaign/Asset name]

**Reviewed:** [date]
**Asset:** [landing page / email / ad / etc.]
**Applicable standards:** [CAP Code | BCAP Code | CPR 2008 | DMCC Act 2024 | CMA Green Claims Code | FSMA 2000 s 21 — as applicable]

---

## Summary

[N] claims reviewed. [N]✅ [N]⚠️ [N]🔴

**Ready to ship:** [Yes | With changes below | No — rewrite needed]

> **Before emitting "Ready to ship: Yes" (i.e., approving a claim for external use / publication):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:
>
> > Approving a marketing claim for publication is a legal act — once published, substantiation gaps and comparative-claim exposure become ASA challenge or CMA enforcement risk. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
> >
> > [Generate a 1-page summary: asset, claims approved, claim types (specific factual / comparative / implied / absolute / green / financial), substantiation on file for each, any implied claims flagged, and the three things to ask the solicitor before the copy goes live.]
> >
> > If you need to find a solicitor: the SRA Find a Solicitor tool (sra.org.uk) is the fastest starting point.
>
> Do not proceed past this gate to "Ready to ship: Yes" without an explicit yes.

---

## Claim-by-claim

[All the claim blocks from Step 3, grouped: 🔴 first, then ⚠️, then ✅]

---

## Suggested revision

[For short assets — under 50 words, or a tweet, headline, one-liner, tagline, short ad — the output in this block is the actual revised copy with the fixes applied inline, not a description of what changed. The reader should be able to copy-paste this block into the asset.
For longer assets (>50 words but <300 words), show the revised copy with fixes applied inline.
For longer assets (300+ words), summarise the changes as a bulleted diff ("Strip Claim 1. Rewrite Claim 3 to drop 'only.' Soften Claim 4 for green-claims risk.") rather than pasting the whole asset.]

---

## Substantiation needed before ship

| Claim | Need | From whom |
|---|---|---|
| [claim] | [data type — e.g., benchmark, customer study, independent verification] | [PM / data team / eng / external auditor] |

---

## Citation check

Any CAP Code rules, ASA adjudications, CMA decisions, BPR 2008 provisions, CPR 2008 provisions, or FSMA 2000 references cited in this review were generated by an AI model and have not been verified against a primary source. Before relying on a specific rule to clear or reject copy, verify it:
- CAP Code / ASA adjudications: asa.org.uk
- CMA decisions: gov.uk/cma-cases
- Legislation: legislation.gov.uk
Source tags on each citation (e.g., `[ASA]`, `[web search — verify]`) show where it came from; `[verify]` tags carry higher fabrication risk and should be checked first.
```

## Disclosure overlays

Copy that involves any of the fact patterns below sits inside an additional UK disclosure regime. Research the currently operative requirements and verify currency — these regimes update frequently.

- **Testimonials / reviews / endorsements** — CAP Code rules 3.45-3.52 on testimonials; CAP Code on fake reviews (reinforced by DMCC Act 2024 `[DMCC-ACT-2024]`); material connections between the speaker and the advertiser must be disclosed. If an influencer is involved, check the ASA's influencer guidance and the CAP Code rules on recognising ads.
- **"Results may vary" / atypical results** — CAP Code rule 3.22: if a testimonial or case study shows results that are not typical, that must be made clear. Research the current form and placement requirements.
- **Free trial / auto-renewal / subscription** — DMCC Act 2024 `[DMCC-ACT-2024]` subscription contract requirements: the advertising of free trials that auto-convert must be clear, prominent, and not misleading. CMA actively enforces this.
- **Drip pricing** — DMCC Act 2024 `[DMCC-ACT-2024]` — mandatory fees must be included in the initial price or clearly and prominently disclosed. The CMA has designated drip pricing a priority enforcement area.
- **Financial promotions** — FSMA 2000 s 21 `[FSMA-2000-S]` — see mandatory first check above.
- **Children's advertising** — CAP Code Section 5 (children); OSA 2023 `[OSA-2023-S]` duties on advertising harmful to children on regulated platforms. Stricter rules on product placement, health claims, and targeting.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't write the marketing. It fixes what's wrong with it. The suggested rewrites keep the energy, but the marketer owns the voice.
- It doesn't substantiate claims. It identifies which ones need it and who has the data.
- It doesn't review design or imagery — words only. If an image implies a claim (competitor logo with a red X through it), flag it, but visual review is a human judgment.
- It doesn't give FCA s 21 approval. Only an FCA-authorised person can do that.
