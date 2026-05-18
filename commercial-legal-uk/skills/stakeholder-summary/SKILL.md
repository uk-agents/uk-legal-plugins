---
name: stakeholder-summary
description: >
  Translates a contract review into a summary the business stakeholder will
  actually read. Not a legal memo — a two-minute answer to "can I sign this
  and what do I need to know." Use when user says "summarize for the business",
  "write this up for [stakeholder]", "explain this to procurement", "non-legal
  summary", or when a review is done and needs to go to someone outside legal.
---

# Stakeholder Summary

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination outside the legal professional privilege circle, flag it and offer alternatives. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

The business owner who asked for this contract doesn't want a legal memo. They want to know: can I sign it, what's the catch, and what do I need to do. This skill takes a completed review and turns it into that.

## Which side?

The underlying review memo was run against either the sales-side or the purchasing-side playbook. Carry that framing through. Check which side the review was run on (noted at the top of the review memo) and match the voice. If it's not obvious, ask the solicitor before summarising.

## Audience calibration

Read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` → `## House style` → who reads stakeholder summaries, how long should they be. If not specified, default to: procurement or a department head, two paragraphs max, no legal terms of art.

Different audiences need different summaries:

| Audience | Cares about | Doesn't care about |
|---|---|---|
| **Procurement** | Price, renewal mechanics, approval routing | Liability cap structure |
| **Department head (budget owner)** | Can their team use it, what happens if it breaks, cost | Indemnity scope |
| **Finance** | Total cost of ownership, renewal price risk, CPI/RPI escalators, off-balance-sheet commitments | Governing law |
| **Security / IT** | Data handling, sub-processors, UK GDPR compliance, ISO 27001 / Cyber Essentials, where data lives | Everything else |
| **Executive sponsor** | Is this going to embarrass us, is legal a blocker | Details |

Ask who this is for if it's not obvious from context.

## The summary

### Length cap — enforced

The summary is:
- **One paragraph** for the verdict and what this is (business terms, plain English)
- **One paragraph** for the catch — the thing the stakeholder would be surprised by later if nobody told them now
- **A 2-3 item checklist** for what the stakeholder actually needs to do (at most three items)
- **A one-line close** with approval timing

**Under 200 words total.**

### Scope of quote — discipline

When quoting a contract clause, quote the **full conditional sentence**, not a truncated version. If a full conditional quote doesn't fit the summary's length cap, paraphrase rather than truncate.

### Format

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]
<!-- Remove the header above if forwarding outside the legal professional privilege circle (e.g., to a business stakeholder, counterparty, or vendor). Confirm the correct marking for your jurisdiction and matter before forwarding. -->

**[Counterparty] [Agreement type]** — [READY TO SIGN | NEEDS CHANGES | BLOCKED]

[One paragraph: what this agreement does, in business terms. Not "Master Services
Agreement for the provision of cloud-based analytics" — "this is the contract
for the dashboard tool the marketing team wants."]

[One paragraph: what the stakeholder needs to know. The catch, if there is one.
The thing that will surprise them later if nobody tells them now. E.g., "Heads
up: this auto-renews every year and we have to cancel 60 days out — I've added
it to the tracker but you should know." Or: "Clean agreement, no surprises,
cleared to sign."]

<!-- Do not claim "I've added it to the tracker" unless `renewal-tracker` has
actually been run for this contract — see Verify tracker entries before
asserting them below. -->

**What you need to do:**
- [ ] [Action item, if any — "confirm the team is okay with data living outside the UK"
  or "nothing — I'll route for signature"]

**Approval:** [who's approving and expected timing]
```

**Verify tracker entries before asserting them.** Before the summary says "I've added it to the tracker" (or any equivalent), verify that `renewal-tracker` has been run for this contract. If there isn't one, either run `renewal-tracker` first, or write the summary without asserting the tracker entry and include an action item: "Add to renewal tracker — not yet done."

### What to translate

| Legal finding | Business translation |
|---|---|
| "Liability capped at 12 months fees" | "If they break something, the most we can recover is a year's worth of what we paid them." |
| "No termination for convenience" | "Once we sign, we're locked in for the full term — we can't just cancel if we stop using it." |
| "Auto-renewal with 60-day notice" | "This renews automatically every year. To cancel, we have to tell them two months before the renewal date." |
| "No IP indemnity" | "If someone sues us claiming this tool infringes their patent, the vendor isn't on the hook to defend us." |
| "Sub-processor list not disclosed" | "We don't know what other companies will have access to our data through them — which is a UK GDPR concern." |
| "Data deletion within 30 days of termination" | "When we cancel, they delete our data within a month under the contract and UK GDPR obligations. Export anything you need before then." |
| "SLA credits capped at 10% of monthly fee" | "If the service goes down, we get a small credit back. It won't cover the cost of the downtime to the business." |
| "CPI escalator on renewal" | "The price goes up every year in line with inflation (CPI). Finance should model this into the budget." |
| "RPI escalator on renewal" | "The price goes up every year in line with the Retail Prices Index — which typically runs higher than CPI. Finance should check the impact." |
| "UCTA reasonableness concern" | "The exclusion clause may not fully protect them under UK law — that's actually good for us, but the solicitor has flagged it to watch." |

### What NOT to include

- Section numbers
- Defined terms in quotes
- The word "indemnification" (say "they cover us if" / "we cover them if")
- The word "notwithstanding"
- Risk matrices with coloured dots (unless this stakeholder has specifically asked for them before)
- Caveats about how this isn't legal advice — the stakeholder knows who sent it
- UCTA reasonableness analysis — not relevant to the business reader

## When the review found problems

If the review has 🔴 or 🟠 issues, the summary still needs to be two paragraphs — but the second paragraph is "here's what we're pushing back on and why."

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]
<!-- Remove the header above if forwarding outside the legal professional privilege circle. -->

**[Counterparty] [Agreement type]** — NEEDS CHANGES

[What it is, one paragraph.]

We're going back to them on [N] things before this is ready. The main one:
[the critical issue in plain English — "they want the right to use our data
to improve their product, which means our competitors' instance gets smarter
from our data"]. We've asked them to strike it. [Realistic assessment: "They'll
probably agree" / "This might be a sticking point — will keep you posted."]

**What you need to do:**
- [ ] Nothing yet — I'll let you know when it's back from them.
  OR
- [ ] [Business decision they need to make: "If they won't budge on X, are you
  okay with Y, or do we walk?"]
```

## Handoffs

**From vendor-agreement-review / saas-msa-review:** Those skills produce the full memo. This skill reads the memo and compresses it. Don't re-review the contract — read the review.

**To the stakeholder:** Via whatever channel `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` says. If Slack, keep it under 150 words. If email, the format above is fine as-is.

## Escalation-fan-out reconciliation

Before producing the summary, read the upstream review memo and tally escalations:

1. **Count the escalation targets the review named.** De-dupe by approver name.
2. **Count the escalations actually routed.** Read the review folder for `escalation-*.md` drafts produced by `escalation-flagger`.
3. **Reconcile.** If N approvers were named and M drafts exist, (N − M) escalations have not been routed.

Include a short reconciliation block in the summary — above the checklist, below the catch paragraph:

```markdown
**Escalation status:** [M] of [N] escalation targets routed. The following have not been routed and require action:
- [Approver name] — [one line on the finding that named them]
```

If all N have been routed: `**Escalation status:** [N] of [N] escalation targets routed.`

The reconciliation block is exempt from the 200-word cap.

## A note on tone

Stakeholders remember two things about legal: did it block me, and did it make sense. This skill is how legal makes sense. Write like you're explaining it to a smart colleague over coffee, not like you're writing a memo to file. Use UK English (recognise, organise, favour, licence as noun, etc.).

If the honest summary is "this is fine, sign it," say that. Don't pad a clean review into three paragraphs to look thorough.
