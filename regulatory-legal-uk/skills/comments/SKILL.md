---
name: comments
description: Review open UK consultation response periods, log decisions, track deadlines. Use when a UK consultation (FCA CP, ICO code consultation, GOV.UK consultation, CMA discussion paper) has a response window open and you need to surface closing dates, decide whether to file a response, or record a response / not-responding / waived decision (--decide CMT-ID).
argument-hint: "[optional: --decide CMT-ID]"
---

# /comments

## Purpose

UK consultations have deadlines. The decision to submit a response or not is an attorney call — but the closing date disappearing without a logged decision is the risk. This skill surfaces open consultation periods and records decisions.

**UK terminology note:** This plugin uses "consultation response" and "response to consultation" — not "comment letter" (US terminology). The underlying process is the UK government's public consultation process, governed by the Cabinet Office Code of Practice on Consultation (typically 12 weeks). FCA Consultation Papers (CPs), ICO codes of practice consultations, and Ofcom consultation papers all follow similar processes.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/consultation-tracker.yaml` → all tracked UK consultations and their status.
`~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → default consultation decision owner.

## Default view — open consultation response periods

```markdown
## Consultation Response Tracker — [date]

### ⏰ Closing in <14 days

| ID | Consultation | Issuing authority | Closing date | Days left | Decision | Owner |
|---|---|---|---|---|---|---|
| CMT-001 | [title] | [FCA / ICO / Ofcom / HM Treasury / GOV.UK] | [date] | [N] | Undecided | [owner] |

### 🟡 Open (>14 days)

[same table]

### Recently decided

| ID | Consultation | Decision | Rationale |
|---|---|---|---|
| CMT-002 | [title] | Not responding | [reason] |

---

**Total open:** [N]  **Undecided with closing date <30 days:** [N]

**12-week consultations:** The Cabinet Office Code of Practice on Consultation sets a 12-week standard for most UK public consultations. FCA CPs typically run 3 months. Shorter windows apply to emergency consultations. Check the consultation document for the specific closing date and any extended windows.
```

## Log a decision

```
/regulatory-legal-uk:comments --decide CMT-001
Decision: [responding / not-responding / waived]
Rationale: "[brief — e.g., 'FCA CP covers product type we don't offer' or 'Responding to questions 3-7 on SYSC outsourcing']"
```

Updates tracker. If decision is "responding": prompt for a response-drafting deadline reminder (closing date minus 5 business days for internal review).

**UK consultation response best practice:**
- Responses are typically submitted via the regulator's consultation portal (FCA CP responses via fca.org.uk, GOV.UK consultations via IRAS or Citizen Space, etc.)
- Responses are usually published — unless marked confidential. Flag to the user if the consultation response will be published publicly.
- Coordination with trade associations: many UK regulatory responses are filed jointly through trade bodies (UK Finance, PIMFA, techUK, etc.). Ask the user whether a joint response is planned before drafting a standalone response.

## Notifications

On first detection of a UK consultation (populated by reg-feed-watcher): Slack DM to consultation decision owner if Slack MCP is configured and `owner_slack` is set.

Reminder at 14 days before closing date if decision is still "undecided."
Reminder at 3 days before closing date if still undecided — elevated urgency.

## Consequential-action gate (submit a consultation response / respond to a regulator)

**Before logging a decision as "responding" — and always before producing a consultation response draft for submission:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Submitting a response to a UK public consultation has legal and reputational consequences. It is a public statement of the company's position on proposed regulatory changes, it is usually published on the regulator's website, and positions taken here can be used in subsequent regulatory proceedings and can affect how the regulator views the company. Have you reviewed this with a solicitor or your compliance function? If yes, proceed. If no, here's a brief to bring to them:
>
> - The consultation (regulator, document reference, closing date)
> - What the proposed response says and on which questions
> - Open questions and what's unresolved
> - What could go wrong (adverse admissions, inconsistent prior positions in previous FCA/ICO/CMA submissions, commitment to positions that create compliance obligations)
> - Whether a joint response through a trade association is preferable to a standalone response
> - What to ask the solicitor (should we respond at all; should we file jointly through [trade body]; are there positions we should not take; will our response be published)
>
> If you need to find a UK solicitor: the Law Society's "Find a Solicitor" (`solicitors.lawsociety.org.uk/`). For Scotland: Law Society of Scotland (`lawscot.org.uk/find-a-solicitor/`).

Do not log a "responding" decision or produce a submission-ready draft past this gate without an explicit yes. Tracking views, deadline reminders, and "not-responding / waived" decisions do not require the gate.

---

## UK consultation types reference

| Type | Examples | Typical window | Published? |
|---|---|---|---|
| FCA Consultation Paper (CP) | CP23/1, CP24/5 | ~3 months | Yes, on fca.org.uk/publications |
| FCA Discussion Paper (DP) | DP22/2 | ~3 months | Yes |
| PRA Consultation Paper (CP) | CP15/24 | ~3 months | Yes, on bankofengland.co.uk |
| ICO consultation | DPA 2018 code of practice consultations | 12 weeks (Cabinet Office standard) | Yes, on ico.org.uk |
| Ofcom consultation | OSA guidance, spectrum decisions | Varies (typically 4-6 weeks for statutory); 12 weeks for general | Yes, on ofcom.org.uk |
| GOV.UK public consultation | HMRC, DSIT, HMT consultations | 12 weeks (Cabinet Office standard) | Yes, on gov.uk |
| CMA call for information | Market studies, merger notices | Varies | Yes, on gov.uk/cma |
| Parliamentary Select Committee inquiry | Evidence submissions | Varies; typically 4-8 weeks | Yes, on parliament.uk |
| Draft SI / statutory guidance consultation | Sector-specific | Varies; some very short | Usually yes |

---

## What this skill does not do

- Draft the consultation response. That is a separate attorney task.
- Make the response decision. It tracks the decision; the attorney makes it.
- Monitor post-consultation activity. Once a decision is filed, this tracker's job is done — follow the outcome through `/regulatory-legal-uk:reg-feed-watcher` (the regulator will typically publish a "Response to consultation" or final policy statement several months after the closing date).

> The `consultation-decision` `gap_type` semantics, the per-send Slack confirmation rule, and the consultation-tracker.yaml schema live in the **gap-surfacer** reference skill — load it before doing substantive work.
