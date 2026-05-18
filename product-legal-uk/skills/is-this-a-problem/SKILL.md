---
name: is-this-a-problem
description: >
  Fast "is this a problem?" answer for the quick Slack question — pattern-matches
  against your UK risk calibration. Use when the user says "is this a problem",
  "quick question", "can we do X", "do I need legal review for", "sanity check", or
  pastes a PM's question that needs a same-minute fine / needs a look / hold call.
  UK regulatory framing: CMA, ICO, FCA, ASA/CAP Code, MHRA, Ofcom.
argument-hint: "[the question]"
---

# /is-this-a-problem

1. Load `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → Risk calibration.
2. Apply the triage workflow below.
3. Pattern-match. Check for common UK-specific traps.
4. Answer in one minute: ✅ Fine / ⚠️ Needs a look / 🛑 Hold. One sentence why.
5. If ⚠️ or 🛑: name the next step.

```
/product-legal-uk:is-this-a-problem "Can we use customer logos on the pricing page?"
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/product-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the legal professional privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for legal advice) can break privilege. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitised version for the broader channel, or (c) both.

## Purpose

Most "quick legal question" Slacks are one of three things: (a) not a problem, say so fast, (b) a real thing that needs a real look, route it, (c) a thing that looks fine but has a UK-specific trap, catch the trap. This skill sorts in under a minute using the calibration table.

The goal is speed. The PM asked at 4:47pm. They want an answer, not a memo.

## Load calibration

Read `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` → `## Risk calibration`. The whole point of this skill is pattern-matching against that table.

## The triage

### Match against calibration

Does the question match a pattern in the calibration table?

**Matches "usually FYI":**
→ Say so. One line. "You're fine — [pattern]. Ship it."

**Matches "usually requires work":**
→ Name the work. "Needs a [DPIA triage / vendor DPA / ASA substantiation check]. Takes [timeline from table]. Want me to start it?"

**Matches "usually blocks":**
→ Stop them. "Hold on — [pattern]. This needs a real look before anyone commits to a date. Let's talk."

**Doesn't match anything:**
→ Say that too. "This doesn't pattern-match to anything I've seen here. Needs a human look — [your name] or me tomorrow?"

### The UK trap check

Some questions are fine on the surface but have a UK-specific twist. Recognise the fact pattern, ask the catch question, then research the applicable doctrine for the specific fact pattern before concluding whether it's a problem or not.

| Question sounds like | Why it might not be simple | Catch it by asking |
|---|---|---|
| "Can we add [vendor] to the integration?" | Vendor touches a new data category — flag as potentially implicating UK GDPR Art 28 data processing agreement requirement and DPIA trigger under Art 35 | "What data flows to them? Is there a DPA in place?" |
| "Can we A/B test the pricing page?" | Differential pricing by segment can implicate CPR 2008 misleading commercial practices and CMA drip-pricing guidance under DMCC Act 2024 `[DMCC-ACT-2024]` | "Are both arms seeing the same final price before payment? How are users assigned to arms?" |
| "Can we auto-enrol users in the new feature?" | Default-on behaviour without a clear opt-in may trigger CMA scrutiny under DMCC Act 2024 subscription rules and CPR 2008 `[CPR-2008-REG]` | "Does this respect existing user preferences? Is there a single-click opt-in at point of first payment?" |
| "Can we use customer logos on the site?" | Logo use is a separate permission from the contract relationship — flag as potentially implicating trademark and passing-off rules and the customer's own contract terms | "What does the contract say about publicity? Do we have written permission?" |
| "Can we train on this data?" | Usage rights for the original collection purpose may not extend to training — flag and research the notice/consent given at collection. UK GDPR Art 5(1)(b) purpose limitation applies. | "What did we tell users when we collected it? What is the lawful basis for the new purpose?" |
| "It's just an internal tool" | Internal tools still process personal data — UK GDPR applies to employee and customer data; flag and route | "Whose data does it touch? Employees, customers, third parties?" |
| "We already do something similar" | "Similar" is doing a lot of work — the delta is where the issue usually is | "Similar how? What's actually different?" |
| "Can we use [AI vendor / LLM] for this?" | Vendor AI terms may permit training on inputs; use case may need a UK GDPR Art 22 check if automated decisions affecting individuals — flag and route | "Is there a data processing agreement? What data goes into the model? Does it make decisions about individuals?" |
| "Can we add AI to this feature?" | May trigger UK GDPR Art 22 DSAR rights (automated decisions); may trigger Equality Act 2010 indirect discrimination risk; may be a new use case not in the AI registry | "What does the AI do — assistive or automated decision-making? Who does it act on and what decisions does it affect?" |
| "The model just decides automatically" | Automated individual decision-making without human review is regulated under UK GDPR Art 22 `[UK-GDPR-ART]`; flag and research the applicable rules for the affected users | "Does this decision significantly affect individuals? Is there a human in the loop? Are users given a right to explanation / challenge?" |
| "It's AI-generated content" | Output IP and disclosure duties vary by sector and audience; OSA 2023 may apply if content is user-facing on a regulated platform | "What's the content type? Does the vendor's terms address output ownership? Who is the audience? Is the platform regulated under OSA?" |
| "We're fine-tuning on our data" | UK GDPR purpose limitation; data subjects' rights over training data; check vendor AI terms carefully | "What's in the training data? Is any of it personal data? What lawful basis applies to the training purpose?" |
| "We want to run a promotion / competition" | UK-specific promotions law (CAP Code, Gambling Act 2005 for prize draws vs. skill competitions, ASA rules on social proofing) — flag | "Is it a prize draw (chance) or a skill competition? What are the entry conditions? Is there a monetary purchase required?" |
| "Can we use this for a healthcare / medical feature?" | MHRA approval pathway for medical devices and SaMD; NHS procurement implications; check whether it is within or outside the clinical decision support exemption | "What does the feature claim to do? Does it make diagnoses, recommend treatment, or is it general wellness?" |
| "We're launching a financial product / feature" | FSMA 2000 s 21 financial promotion approval required before communication; FCA CONSUMER DUTY applies for retail financial products | "Does any element of the feature involve inviting or inducing investment activity? Has FCA-authorised approval been confirmed?" |
| "We're adding a subscription / free trial" | DMCC Act 2024 `[DMCC-ACT-2024]` subscription contract requirements (single-click opt-in, reminder notices, easy cancellation) now apply — flag | "Is there a clear opt-in at point of first payment? Are reminder notices sent before auto-renewal? Is cancellation easy?" |
| "Green / sustainability claim" | CMA Green Claims Code (2021) substantiation requirement applies — flag as requiring evidence | "What specific claim is being made? Is there independent verification of the claim?" |

If a trap might be present, ask the one question before answering. One question, not a checklist. When the answer suggests a real issue, flag for research and route — don't pattern-match to a legal conclusion from the question alone.

## Output format

**For Slack (the common case):**

Slack triage replies are internal legal advice. If the reply is being pasted into a ticket, document, or channel that's broadly shared with non-legal, prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`):

```
[WORK-PRODUCT HEADER — per plugin config ## Outputs]
```

For an in-the-flow Slack DM reply to the PM, the short form is:

```
[✅ Fine | ⚠️ Needs a look | 🛑 Hold]

[One sentence: the call and why.]

[If ⚠️: what the look involves, how long]
[If 🛑: who to talk to, when]
```

**Examples:**

```
✅ Fine — adding an analytics event is an FYI here as long as it's covered by
the existing privacy policy categories and no new purpose under UK GDPR Art 5
is created. This one is.
```

```
⚠️ Needs a DPIA triage — new data collection for [category] under UK GDPR
Art 35. Usually takes a day. Want me to kick it off?
```

```
🛑 Hold — "train on customer data" triggers purpose limitation under UK GDPR
Art 5(1)(b) and possibly a new lawful basis question. What did the privacy
notice say? Let's pull it before anyone promises this to the customer.
```

```
⚠️ Needs an AI governance triage — adding an LLM to this workflow means we need
to check UK GDPR Art 22 (automated decisions) and confirm any use case against
the registry before it ships. Takes a day. Want me to run the triage now?
```

```
🛑 Hold — any communication that constitutes a financial promotion under FSMA
2000 s 21 needs FCA-authorised approval before it goes out. This is a criminal
offence if published without it. Who is our s 21 approver?
```

## When to NOT use this skill

- The question is actually complex (multiple issues, novel area) → route to launch-review or feature-risk-assessment
- The question is "can you review this PRD" → that's launch-review, not triage
- You're not sure → say "I'm not sure, let me look properly" — a wrong fast answer is worse than a slow right one

## Tone

Fast, direct, helpful. The PM is not asking for a lecture. If it's fine, say "fine" — don't list the seven things you checked. If it's not fine, say what's not fine and what to do about it.

You are the lawyer people want to ask, not the one they route around.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.
