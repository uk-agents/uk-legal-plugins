---
name: gap-surfacer
description: >
  Reference: shared gap- and consultation-tracker framework backing /regulatory-legal-uk:gaps
  and /regulatory-legal-uk:comments. Tracks open policy gaps with remediation status,
  ingests gaps from policy-diff, surfaces what's open and aging, routes to owners,
  and notifies gap owners via Slack with per-send confirmation. Loaded by the gaps
  and comments skills before doing substantive work.
user-invocable: false
---

# Gap Surfacer

> Owner notifications: on by default. To opt an owner out, leave `owner_slack` empty.

## Per-send confirmation — no exceptions

Before sending ANY Slack message (assignment notice, overdue reminder, bulk notification, status report):

1. Show the user exactly what you're about to send and to whom: "I'm about to send this to [N] people: [preview]."
2. Wait for an explicit yes.
3. If the message contains any citations, deadlines, or compliance conclusions, add: "⚠️ The citations in this message are unverified — I'm not confirming they're current before sending. Do you want me to add a 'verify before acting' line?"
4. Never send without the confirm. Not on a cadence. Not in a batch. Not because it was sent yesterday.

Auto-send without confirmation is the most irreversible action in this plugin. Regulatory compliance deadlines sent unchecked to owners who have no way to verify them is the exact scenario this rule exists to prevent.

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/regulatory-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

UK regulatory gaps get found and then forgotten. This skill tracks them until they're closed and notifies the people responsible for closing them.

## The tracker

Lives at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/gap-tracker.yaml`:

> **Note on consultation-tracker.yaml:** `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/consultation-tracker.yaml` is a sibling file owned by the comments skill. It is written to by reg-feed-watcher (which logs UK consultations automatically) and the comments skill (which tracks user-initiated consultation response decisions). This skill does not read or cross-reference it.

```yaml
gaps:
  - id: GAP-001
    requirement: "[what the UK rule requires]"
    regulation: "[name + cite — OSCOLA format, e.g., Financial Services and Markets Act 2000, s 165]"
    policy_affected: "[name or 'new policy needed']"
    gap_type: "partial"  # none | partial | full | new-policy | watch | consultation-decision
    owner: "[name from policy index]"
    owner_slack: "[Slack user ID or handle, if known]"
    opened: 2026-03-01
    due: 2026-06-01  # SI/FCA rule effective date, internal deadline, or consultation closing date
    status_verified: true  # false if upstream policy-diff could not confirm the rule is in force; unverified items never hit 🔴 Overdue
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false
    resolution: ""  # filled on close
```

**Never classify a gap as Overdue on an unverified rule.** The 🔴 Overdue classification means "we missed a binding deadline." If the rule's status is unverified (policy-diff set `status_verified: false`, or the rule is >12 months old / past its applicability date with no currency confirmation), the deadline may not be binding. Use 🟡 "Review needed" and note: "If this rule is in force as published, this would be overdue by [N] days. Verify rule status before escalating." Route unverified-rule items to `watch`, not to the active overdue/due-soon buckets.

**`gap_type` semantics for UK regulatory context:**

| Value | Meaning | Typical reminder cadence |
|---|---|---|
| `none` | Policy already covers the requirement. Logged for audit trail only. | No auto-reminder. |
| `partial` | Policy addresses the topic but doesn't fully cover the new UK rule requirement. Needs an amendment. | 30 days before due. |
| `full` | Policy contradicts or silently omits the new UK requirement. Needs a rewrite or new section. | 30 days before due. |
| `new-policy` | No existing policy covers this. Policy needs to be drafted. | 30 days before due. |
| `watch` | Forward-looking item — UK consultation or proposed SI not yet final. No compliance obligation today; policy work waits for the final rule or SI. `due:` is a revisit date (typically the consultation closing date or a one-year horizon). | No auto-reminder; re-evaluate when a final policy statement or SI is published. |
| `consultation-decision` | Pre-rule consultation response decision pending — GOV.UK/FCA/ICO/Ofcom consultation where the team is deciding whether to file a response. `due:` is the consultation closing date. | 21 days before due (tighter because consultation-drafting windows are short). |

A `watch` or `consultation-decision` entry is not a compliance gap — it's a tracking artifact for pre-rule items. Surface them in the status report in their own bucket so counsel reading at 7am can tell at a glance which items are "fix this before the FCA notices" vs. "keep an eye on this consultation."

## Modes

### Mode 1: Ingest from policy-diff

When policy-diff finds gaps, append them to gap-tracker.yaml. De-dupe — same requirement + same policy = same gap, don't double-count.

**After ingesting, notify the owner:**

If Slack MCP is available and `owner_slack` is set:

Send a Slack DM to the gap owner — but only after the per-send confirmation at the top of this file. Preview the message to the user, wait for an explicit yes, then send:

```
📋 New compliance gap assigned to you

Gap: [GAP-ID] — [requirement, one sentence]
Regulation: [name + link — OSCOLA citation]
Policy affected: [policy name or "new policy needed"]
Due: [rule effective date / SI commencement date]

View full gap tracker: /regulatory-legal-uk:gaps
```

Set `notified: true` in the tracker entry after sending.

If Slack MCP is not available: note in the status report that owner notification was not sent and flag for manual follow-up.

### Mode 2: Status report

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Open Gaps — [date]

### Bottom line

[N gaps need action by [date] — top 3: X, Y, Z]

### 🔴 Overdue

| ID | Requirement | Policy | Owner | Due | Days over |
|---|---|---|---|---|---|

### 🟠 Due in <30 days

[same]

### 🟡 Open

[same]

### 👀 Watch items (forward-looking — pre-rule UK consultations)

[Pre-rule tracking — `watch` and `consultation-decision` entries. These are not
compliance gaps. Surface separately so the overdue / due-soon bands contain
only real compliance deadlines.]

| ID | Item | Type (CP/SI/GOV.UK consultation) | Closing date | Owner |
|---|---|---|---|---|

### In progress

[same]

### Recently closed

[last 5, with resolution]

---

**Oldest open gap:** [ID], [N] days
**Gaps by owner:** [breakdown]
**Owner notifications sent:** [N] / [N total gaps]

---

**Next step for each open gap:** `/regulatory-legal-uk:policy-redraft` produces a marked-up policy redraft with `[verify]` tags and a change summary. It's a proposal for the policy owner's review — not a direct edit to source documents.

---

**Verify citations before relying on them.** Regulation citations in this tracker were AI-generated upstream (by reg-feed-watcher and policy-diff) and have not been checked against a primary source. Before closing or risk-accepting a gap — or citing one in an attestation, board report, or regulator response — confirm the underlying rule against the FCA Handbook, legislation.gov.uk, or the issuing authority's website. Citations follow OSCOLA format: verify SI numbers, Act section numbers, and FCA Handbook cross-references before relying on them. Source tags carried forward from upstream (e.g., `[uk-legal MCP]`, `[model knowledge — verify]`) show where each citation originated; `[model knowledge — verify]` tags carry higher fabrication risk and should be checked first. Never strip the tags when surfacing gaps.
```

## Config-dependent fallbacks

This skill reads gap-response owners and the escalation path from `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`. When a value it needs is empty or still `[PLACEHOLDER]`:

- **Gap-response triager missing:** leave assignment open and append: "No triager is set in `## Gap response process`. Assign one with `/regulatory-legal-uk:cold-start-interview --redo` or by editing the config so new gaps get routed."
- **Owner unknown for a newly-ingested gap:** log the gap with `owner: [unassigned]` and append: "[N] gaps were ingested without an owner because the policy library doesn't name one for the affected policy."
- **Escalation path missing for an overdue material gap:** still report it as overdue, and append: "No escalation path is set for material overdue gaps."

Say nothing about config when the values are populated.

**Due-date reminder logic (runs during status report and scheduled agent):**

Reminder cadence is a function of `gap_type` — compliance gaps get a 30-day heads-up, consultation-decision items get 21 days (tighter because the drafting window is shorter), watch items get no auto-reminder.

For each gap with status "open" or "in-progress":
- `partial`, `full`, `new-policy`, `none`: if due date is within 30 days and a reminder has not been sent in the last 7 days, PREVIEW a Slack DM and wait for per-send confirm before sending.
- `consultation-decision`: if consultation closing date is within 21 days and a reminder has not been sent in the last 7 days, PREVIEW a Slack DM (subject "💬 UK consultation closing in [N] days — response decision needed") and wait for per-send confirm before sending.
- `watch`: no auto-reminder. Revisit when the tracker is reviewed or a final policy statement or SI is published for the same subject matter.
- If due date has passed on a compliance gap: flag as overdue in the report and PREVIEW a Slack DM — wait for per-send confirm before sending.
- If consultation closing date has passed on a `consultation-decision` item and no response was filed: flag as overdue, PREVIEW a Slack DM, and ask the owner to update to `risk-accepted` (deliberate no-response) or `closed` (response filed) with a note.
- Record reminder timestamps in the tracker to avoid repeat nags.
- Batch reminders still require per-send confirm.

### Consequential-action gate (certify compliance)

**Before closing a gap as resolved, or producing any output that certifies compliance with a UK regulatory requirement (internal attestation, board report, FCA attestation, audit response, regulator response):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Certifying compliance — or closing a gap as resolved — has legal consequences in the UK regulatory context. An FCA attestation that is subsequently shown to be incorrect may constitute a breach of the FCA's Principle 11 (relations with regulators) or SM&CR obligations, and can be the basis for enforcement action. Have you reviewed this with a solicitor or your compliance function? If yes, proceed. If no, here's a brief to bring to them:
>
> - The gap (requirement, source, what the policy diff found)
> - What the proposed resolution does and does not cover
> - Any residual gap or ambiguity
> - Open questions and what's unresolved
> - What could go wrong (overbroad certification, unresolved residual obligation, inconsistent prior submission to the regulator)
> - What to ask the solicitor or compliance officer (is this truly closed; should we risk-accept with rationale instead; do we need to notify the FCA/ICO/CMA?)
>
> If you need to find a UK solicitor: the Law Society's "Find a Solicitor" service (`solicitors.lawsociety.org.uk/`). For Scotland: the Law Society of Scotland (`lawscot.org.uk/find-a-solicitor/`).

Do not mark a gap closed or produce a compliance certification past this gate without an explicit yes. Status reports and tracking views do not require the gate.

### Mode 3: Close a gap

```
/regulatory-legal-uk:gaps --close GAP-001
Resolution: "Policy updated v2.3, approved [date], reviewed by [solicitor/compliance officer]"
```

Updates status to closed, records resolution and close date.

### Mode 4: Risk-accept a gap

```
/regulatory-legal-uk:gaps --accept GAP-002
Rationale: "Requirement applies only to [condition we don't meet]. Revisit if [trigger — e.g., 'FCA finalises CP25/X' or 'we obtain Part 4A permission for Y']."
Accepted by: [name with authority]
```

Status → risk-accepted. Stays in the tracker (not deleted) but falls out of the open-gaps report.

## Integration: reg-change-monitor agent

The agent's digest includes the gap count and oldest-open-gap age. If anything goes overdue, that goes at the top of the digest. The agent also runs the due-date reminder check and sends any outstanding Slack notifications.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced.

If the tracker surfaced more than ~10 open gaps, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by severity, a timeline of gaps by due date, and a sortable grid with owner, status, and last-touched date.

## What this skill does not do

- Close gaps on its own. Closing requires the resolution note and the human action that the note describes.
- Send Slack notifications if the Slack MCP is not configured.
- Send more than one reminder per 7-day period per gap.
