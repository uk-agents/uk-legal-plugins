---
name: policy-redraft
description: Produce a proposed marked-up policy redraft that closes a gap found by /regulatory-legal-uk:gaps or /regulatory-legal-uk:policy-diff. A first draft for internal review — not for direct application to approved policy documents. Use when the user says "redraft the policy", "draft the policy fix", "mark up the policy", or when gap-surfacer hands off a gap for drafting.
argument-hint: "[GAP-ID or gap description]"
---

# /policy-redraft

1. Load `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → policy library index + practice profile.
2. Use the workflow below.
3. Gather inputs: the gap (from `/regulatory-legal-uk:gaps` output or described directly), the current approved policy text, the UK rule text.
4. Verify the rule is current (per the policy-diff rule-status check). If you can't verify, emit the `⚠️ RULE STATUS UNVERIFIED` banner.
5. Produce a marked-up redraft of the affected policy section(s) — smallest-possible edit, `[verify]` tags carried through, inline comments explaining WHY each change was made.
6. Output a Policy Redraft Memo. Write it to a new file named `[policy-name]-proposed-redraft-[YYYY-MM-DD].md` — never write to the source policy document.
7. Do NOT close the gap in the tracker. The gap closes when the redraft is applied AND approved, which is the policy owner's action.

---

> This skill produces a **proposal**, not an edit. It writes to a new file with a clearly-marked draft filename. It never writes over a source policy document, and it never closes a gap in the tracker — the gap closes when the redraft is applied AND approved by the policy owner.

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/regulatory-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Gap-surfacer finds the gap. Policy-diff names what needs to change. This skill takes the next step and produces a marked-up redraft of the affected UK policy section — small, specific, flagged — as a first draft for the policy owner's review.

## Hard guardrails — read these first

These are the load-bearing rules. If any of them would be violated, stop and ask.

1. **This is a PROPOSAL, not an edit.** Never write directly to a source policy document. The output goes to a new file at `[policy-name]-proposed-redraft-[YYYY-MM-DD].md`, or into the matter workspace. Not `[policy-name].md`.
2. **Never close the gap in the tracker.** Gaps close when the redraft is APPLIED AND APPROVED — that is the policy owner's action.
3. **"Apply this for me" is not in scope.** If the user asks you to apply the redraft to the source policy: "I don't apply policy changes — that's the policy owner's action after review and approval. I produce the proposal. When it's been reviewed and approved, tell me and I'll update the gap tracker."
4. **Confirm the policy version before redrafting.** If the user gives you a file, ask: "Is this the approved version of the policy, and is it the latest?" If they paste text, trust but flag in the reviewer note.
5. **Smallest-possible edit.** Strike a word before a sentence, a sentence before a paragraph, a paragraph before a section. Only touch sections affected by the gap. Don't restyle the policy.
6. **UK plain English.** UK policy drafting follows Cabinet Office plain-English conventions. "Must" not "shall" in modern UK policy and regulatory drafting. Do not import US-style drafting conventions.
7. **Carry `[verify]` tags through.** Any effective date, threshold, OSCOLA citation, or requirement that came from model knowledge or an unverified source gets tagged in the redraft itself, not just in the memo.

## Step 1: Gather inputs

Three inputs are required. If any is missing, ask — don't infer.

### 1a. The gap

One of:
- A `GAP-ID` from the gap tracker — load the entry from `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/gap-tracker.yaml` (or the matter-level equivalent).
- A gap described in the user's message — capture the requirement, the UK regulation (OSCOLA citation), and the affected policy.
- A diff summary pasted from `/regulatory-legal-uk:policy-diff` output.

### 1b. The current policy text

One of:
- A file path — read it, then ask: "Is this the approved version of the policy, and is it the latest?" Note the answer in the reviewer note.
- Pasted text — trust but flag in the reviewer note: "Policy text was pasted directly; I assumed it was the current approved version. Confirm before applying."
- Neither — ask for one. Do not guess at the policy text.

### 1c. The UK rule text

One of:
- The diff output (already has the rule extracted and tagged).
- A fetched UK regulation via uk-legal MCP — note the source with a provenance tag.
- Pasted rule text from the user — tag `[user provided]`.

If the rule text is partial or ambiguous, apply the **no silent supplement** rule from CLAUDE.md: offer the user the options (paste full text, point at legislation.gov.uk or FCA Handbook, web-search-with-verify-tag, or stop), and wait.

## Step 2: Verify the rule is current

UK-specific rule-status check:

Red flags that the UK rule may not be in force:
- The SI's commencement date has passed by more than 30 days with no confirmation it wasn't delayed by a further SI.
- The rule is more than 12 months old.
- Post-Brexit: the provision derives from retained EU law and may have been modified or revoked by REULA 2023 or a subsequent UK instrument.
- The FCA Handbook provision may have been superseded by a more recent Policy Statement.

When you see a red flag, check (via uk-legal MCP, legislation.gov.uk, FCA Handbook) for: amendments, revocations, transitional provisions, commencement delays. If you can verify the rule is in force, proceed. If you cannot verify:

> `⚠️ RULE STATUS UNVERIFIED — I could not confirm this UK rule is currently in force. SIs and FCA Handbook provisions are frequently amended or subject to transitional arrangements. Do not apply this redraft until you confirm the rule's status at legislation.gov.uk, handbook.fca.org.uk, or the issuing authority's website.`

Emit that banner above the work-product header. Tag every commencement/compliance date in the redraft as `[commencement date per published instrument — status unverified]`.

## Step 3: Produce the redraft

A marked-up version of the affected policy section.

### Redline granularity — smallest possible edit

- Strike a word before a sentence.
- Strike a sentence before a paragraph.
- Strike a paragraph before a section.
- Only touch sections affected by the gap. Don't restyle the whole policy.

### UK drafting conventions

- Use "must" not "shall" (Cabinet Office plain-English style).
- Use plain language: "the company" not "the Regulated Entity".
- Defined terms: capitalise the first use if introducing a new defined term, add `("X")` after the definition.
- If the gap requires reference to an FCA Handbook rule, use the standard Handbook abbreviation format: COBS 4.2.1R, SYSC 9.1.1R, etc.

### Conventions

- Struck text: `~~struck text~~`
- Inserted text: **inserted text**
- Each change carries an inline comment explaining WHY — the UK rule, the OSCOLA citation, the gap being closed:

  > `[Change: added 'biometric data' to the definition of 'personal data' per UK GDPR Art. 9(1) as amended by the Data Protection (Amendment) Act 2024 [SI-YEAR/NO verify] (in force [date — verify])]`

- Any commencement date, threshold, OSCOLA citation, or requirement that came from model knowledge or an unverified source gets a `[verify]` tag inline.
- Carry source tags through from the diff: `[uk-legal MCP]`, `[FCA-HANDBOOK]`, `[web search — verify]`, `[model knowledge — verify]`, `[user provided]`.

### Scope discipline

If a section of the policy isn't affected by the gap, leave it alone.

If you see a second gap while redrafting — a provision that's clearly out of step with the UK rule but wasn't in the original gap — don't silently fix it. Flag it in the reviewer note: "While redrafting for [GAP-ID], I noticed [other provision] appears to have a related issue with [requirement]. Not included in this redraft. Consider a follow-on gap."

## Step 4: Output — Policy Redraft Memo

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **⚠️ Reviewer note**
> - **Sources:** [Research connector: uk-legal MCP ✓ verified | govuk MCP ✓ verified | not connected — cites from training knowledge, verify before relying]
> - **Read:** [sections of the policy reviewed; what wasn't read]
> - **Flagged for your judgment:** [N items marked `[review]` inline | none]
> - **Currency:** [rule status verified against legislation.gov.uk / FCA Handbook, [date] | unverified — see banner above]
> - **Before relying:** confirm this is the current approved version of the policy; verify rule status and commencement date; get the policy owner's review; follow your policy-change approval process; update the gap tracker only when applied and approved.

## Policy Redraft: [Policy name]

**Gap:** [GAP-ID or short description]
**UK regulation:** [name, OSCOLA citation, commencement date]
**Policy:** [name, last-updated date]
**Status:** PROPOSAL — not yet reviewed or approved

### Bottom line

[One sentence: what the gap is. One sentence: what the redraft does. One sentence: what needs review.]

### Marked-up policy section(s)

[The redlined text, with inline `[Change: ...]` comments. Only the affected sections.]

### Change summary

| # | Provision | Current | Proposed | Why | Citation | Verify |
|---|---|---|---|---|---|---|
| 1 | §2.1 Definition | "…personal data…" | "…personal data, including biometric data…" | UK GDPR Art. 9(1) special category expansion | [uk-legal MCP] | |
| 2 | §4.3 Retention period | "30 days" | "14 days" | FCA COBS [rule] imposes 14-day cap | `[model knowledge — verify]` | ✓ verify |

### Before applying — checklist

- [ ] Confirm this is the current approved version of the policy being redrafted.
- [ ] Verify the UK rule status and commencement date (legislation.gov.uk, FCA Handbook, or the issuing authority).
- [ ] Get the policy owner's review.
- [ ] Follow your policy-change approval process.
- [ ] Update the gap tracker when applied and approved — not before.
- [ ] If the gap is an FCA Handbook obligation: confirm with the compliance function whether notification to the FCA is required.

---

**What next? Pick one and I'll help you build it out:**

1. **Apply and get sign-off** — you review, circulate to the policy owner, walk it through your approval process. When approved, tell me and I'll mark the gap closed.
2. **Get more info on [X]** — if a specific change needs more grounding (an OSCOLA citation verified, a commencement date checked, a Handbook interpretation question), tell me which one and I'll dig in.
3. **Escalate to [owner / GC / compliance function]** — if the redraft raises something above the policy-owner's authority, I'll draft a short escalation with the facts, the proposed change, and what decision is needed.
4. **Watch and wait** — if the rule's status is uncertain or the policy owner is unavailable, I'll add a revisit note to the gap tracker.
5. **Something else** — tell me what you'd do with it.
```

## Filename

`[policy-name]-proposed-redraft-[YYYY-MM-DD].md`

Not `[policy-name].md`. Not `[policy-name]-v2.md`. The word "proposed-redraft" and the date are load-bearing — they prevent the draft from being mistaken for the current version.

## Config-dependent fallbacks

- **Policy owner missing:** still produce the redraft. Note in the reviewer note: "No policy owner is set for [policy] in `## Policy library`. Assign one with `/regulatory-legal-uk:cold-start-interview --redo` so the approval path is routable."
- **Policy library empty and the gap doesn't name a specific policy:** stop and ask: "I need the current policy text to redraft. Paste the text of the affected policy, or point me at the file."

## What this skill does not do

- Apply the redraft to the source policy. That's the policy owner's action.
- Close the gap in the tracker. Gaps close when the redraft is applied and approved.
- Rewrite the whole policy. Smallest-possible edit to close the gap.
- Advise on whether a policy change needs notification to the FCA, ICO, CMA, or another UK regulator — flag it `[review]` if relevant and route to the lawyer.
