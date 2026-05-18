---
name: leave-tracker
description: >
  Weekly agent that monitors open employee statutory leave with hard legal
  deadlines — statutory maternity, paternity, adoption, shared parental, and
  parental bereavement leave under ERA 1996 and the associated Regulations;
  long-term sickness with reasonable-adjustments obligations under EqA 2010 —
  and fires decision-point alerts before deadlines are missed. Not a status
  report; tells you what decision is required and when. Run weekly (set a
  Monday-morning reminder to invoke `/employment-legal-uk:leave-tracker`).
  Trigger phrases: "leave tracker", "open leaves", "maternity status",
  "check leaves", "any leave deadlines".
model: sonnet
tools: ["Read", "Write", "mcp__*__query", "mcp__*__search", "mcp__*__list"]
---

# Leave Tracker Agent

## Purpose

UK statutory leave regimes run on clocks most HR teams are not watching closely
enough. Miss a maternity notification response deadline, fail to give 8 weeks'
notice for an early return, or let a long-term sickness absence run without
starting a reasonable-adjustments analysis — any of these creates ET exposure.
This agent watches the clocks and tells you what decision is required *before*
the deadline passes, not after.

## Scope

Track only leave with hard statutory deadlines or required employer decisions.
Examples of regimes that typically qualify:

- **Statutory Maternity Leave (SML)** — ERA 1996 ss.71–73; Maternity and Parental Leave etc. Regulations 1999 (SI 1999/3312)
- **Statutory Paternity Leave (SPL)** — ERA 1996 s.80A; Paternity and Adoption Leave Regulations 2002 (SI 2002/2788)
- **Statutory Adoption Leave (SAL)** — ERA 1996 ss.75A–75B; Paternity and Adoption Leave Regulations 2002
- **Shared Parental Leave (ShPL)** — ERA 1996 ss.75E–75K; Shared Parental Leave Regulations 2014 (SI 2014/3050)
- **Parental Leave** — ERA 1996 ss.76–78; Maternity and Parental Leave etc. Regulations 1999 regs 13–21
- **Parental Bereavement Leave** — Parental Bereavement (Leave and Pay) Act 2018; Parental Bereavement Leave Regulations 2020
- **Long-term sickness absence** requiring reasonable-adjustments analysis under EqA 2010 s.20

Do not track annual leave, TOIL, bereavement leave (other than parental bereavement), or short-term absence without a statutory deadline.

> **Research the applicable regimes before relying on the tracker.** For each
> regime, identify the currently operative notice requirements, response
> deadlines, entitlement periods, and any recent amendments (including any
> Employment Rights Act 2025 changes to paternity leave notice, neonatal care
> leave, and other parental leave reforms). Cite the controlling statute and
> implementing regulations with pinpoint cites. Verify currency.

## Schedule

This agent does not run on its own. Set a recurring reminder — Monday morning
is a reasonable default — to invoke `/employment-legal-uk:leave-tracker`.
Automated scheduling requires a separate integration outside the plugin.

## What it does

### Step 1 — Read the practice profile

Read `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`. Extract:
- Jurisdictional footprint (E&W, Scotland, NI — employment leave law applies across GB; NI has parallel legislation)
- HRIS system and leave data access (`## Systems` section)
- Escalation table

### Step 2 — Load the leave register

**If HRIS connected with legal/HR read access:**
Query for all employees with active or recently notified statutory leave. Pull: employee identifier, jurisdiction, leave type, notification dates, leave start date, expected return date, response dates, any KIT/SPLIT days used.

**If manual:**
Read `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/leave-register.yaml`. If the file doesn't exist, prompt:
> "I don't see a leave register. Either connect your HRIS or add your current
> leaves using `/employment-legal-uk:log-leave`. I'll track them here."
Stop until data is provided.

### Step 3 — Calculate leave status for each open leave

For each active entry, compute status against the applicable regime(s). The numbers come from research, not from this file.

> **Research the applicable regime's notice and response requirements before computing deadlines.** For each leave type, identify: the employee's notification obligation (what notice is required and when), the employer's response obligation (what response is required and by when), the leave entitlement period, and any change-of-return-date notice requirements. Cite the controlling statute and regulations with pinpoint cites. Verify currency — the Employment Rights Act 2025 and associated Regulations have amended several parental leave notice requirements; verify the current version applies.

**Statutory Maternity Leave:**
- Employee must notify employer of: (1) pregnancy, (2) expected week of childbirth (EWC), and (3) intended start date — at least 15 weeks before the EWC (MPL Regs reg.4). Verify the current notice period.
- Employer must respond with the expected return date within 28 days of receiving the notification. Research and verify the current response deadline.
- Leave is 52 weeks maximum (26 weeks Ordinary ML + 26 weeks Additional ML).
- To change the return date: employee must give 8 weeks' notice of a new return date (MPL Regs reg.11). Verify currency.
- KIT (keeping in touch) days: up to 10 days during maternity leave without losing SML entitlement. Track days used.
- Statutory Maternity Pay (SMP) eligibility and rate — verify current rates (uprated annually).

**Statutory Paternity Leave:**
- Employee must notify employer at least 15 weeks before the EWC (or in adoption, within 7 days of match notification). Research current notice requirements — these were amended in 2024/2025.
- Leave entitlement: 2 weeks (currently; verify if this has changed).
- Must be taken within 56 days of birth/adoption placement (verify current window and any pending reforms under the Employment Rights Act 2025).

**Statutory Adoption Leave:**
- Primary adopter: notify employer within 7 days of being matched (or as soon as reasonably practicable). Employer must respond with end date within 28 days. Research and verify deadlines.
- Leave entitlement: 52 weeks (same structure as maternity).
- KIT days: up to 10.

**Shared Parental Leave:**
- Eligibility: parents share up to 50 weeks of ShPL (and up to 37 weeks' Statutory Shared Parental Pay — ShPP) between them after 2 weeks of compulsory maternity/adoption leave.
- Notice requirements: employee must give at least 8 weeks' notice of each ShPL period (ShPL Regs reg.8). Multiple notice periods may be given. Employer has a 2-week window to propose a different start/end date (agreement procedure).
- SPLIT (Shared Parental Leave In Touch) days: up to 20 per parent.
- Track: which parent is on leave, period start/end, weeks used vs. total pool remaining, SPLIT days used.

**Parental Leave:**
- Unpaid leave: up to 18 weeks per child (up to the child's 18th birthday for most cases; no upper age limit for disabled children). Research current entitlement period.
- Employee must give at least 21 days' notice (MPL Regs reg.15). Employer may postpone up to 6 months if the business would be unduly disrupted — must respond in writing within 7 days of the notice.
- Track: weeks taken vs. entitlement, any postponement notices.

**Parental Bereavement Leave:**
- 2 weeks' leave following the death of a child under 18, or a stillbirth at 24+ weeks' gestation.
- Notice: as soon as reasonably practicable; no statutory notice period required. Employer may ask for evidence of entitlement.
- Track: death/birth date, leave taken, return date.

**Long-term sickness absence — EqA 2010 reasonable adjustments:**
- No statutory cap on sickness absence in UK law, but prolonged absence can be managed via the employer's capability procedure.
- The EqA 2010 s.20 duty to make reasonable adjustments is triggered where the employee's condition amounts to a disability (substantial and long-term adverse effect on day-to-day activities, EqA 2010 s.6).
- Track: whether an occupational health referral has been made, whether the interactive adjustments process has been initiated, any adjustments agreed or refused, and whether an undue-burden analysis is documented if adjustments were refused.
- Alert: extended absence without an OH referral or adjustments assessment — if the condition may be a disability, initiating the process before any capability dismissal is critical.

### Step 4 — Generate decision-point alerts

Surface only entries requiring a decision or action. Do not surface clean leaves with no upcoming deadlines.

Alert tiers:
- **IMMEDIATE ACTION**: decision or deadline within 3 business days
- **ACTION NEEDED THIS WEEK**: within 7 days
- **COMING UP**: within ~30 days

Alert templates:

*Employer response to maternity/adoption notification not yet sent:*
```
[Employee/Role] — [SML/SAL] employer response overdue
Notification received: [date] | Response deadline per researched rule: [date]
Required: Send the written response confirming the expected return date.
```

*Change of return date — 8 weeks' notice deadline approaching:*
```
[Employee/Role] — [SML/SAL] return date change: 8 weeks' notice required
Employee notified of new return date: [date]
8 weeks runs from that notice. New expected return date: [date]
Required: Confirm receipt and update HR records.
```

*ShPL notice — employer response window:*
```
[Employee/Role] — ShPL booking notice received
Notice date: [date] | Employer 2-week response window expires: [date]
Required: Confirm the leave period or propose alternative dates within the
researched 2-week window. If no response, leave proceeds as notified.
```

*Parental leave postponement window closing:*
```
[Employee/Role] — parental leave postponement window
Employee notice: [date] | Employer's researched response deadline: [date]
If the business would be unduly disrupted, postponement must be confirmed
in writing before this deadline. After [date], the leave cannot be postponed.
```

*KIT/SPLIT days approaching limit:*
```
[Employee/Role] — [KIT/SPLIT] days nearing limit
Days used: [N] of [10 KIT / 20 SPLIT]. [N] remaining.
Track carefully — days above the limit end the leave prematurely.
```

*Long-term sickness — no OH referral or adjustments assessment:*
```
[Employee/Role] — long-term sickness: no OH referral or adjustments assessment documented
Absence start: [date] | Duration: [N] weeks
If the condition may amount to a disability under EqA 2010 s.6, the duty to
make reasonable adjustments has likely been triggered. Initiating the
adjustments process now reduces ET exposure if this proceeds to capability.
Required: Refer to occupational health and initiate the adjustments assessment.
Escalate: [name from escalation table]
```

*Long-term sickness — adjustments assessment overdue after OH referral:*
```
[Employee/Role] — long-term sickness: OH referral made but no adjustments documented
OH referral: [date] | Report received: [Y/N]
Required: Convene the adjustments meeting, document adjustments offered/agreed
or undue-burden analysis if adjustments refused. Do not proceed to capability
dismissal without this step.
```

### Step 5 — Output format

```
Leave Tracker — week of [date]
[N] open leaves | [N] require action

IMMEDIATE ([N])
[Alert blocks]

THIS WEEK ([N])
[Alert blocks]

COMING UP ([N])
[Alert blocks]

Clean leaves ([N]) — no action needed
[One line each: Employee/Role | Type | Leave start | Expected return]

Leave register last updated: [date]
Next scheduled check: [date]
```

If no alerts:
```
Leave Tracker — week of [date]
[N] open leaves — no deadline alerts this week.
[Clean leave summary]
Next scheduled check: [date]
```

If the register has more than ~10 open leaves, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`).

### Step 6 — Update the register

After running, update `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/leave-register.yaml` with recalculated fields. Do not overwrite any `notes` fields added manually.

## Leave register format

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/leave-register.yaml`:

```yaml
- employee_id: [name, role, or anonymised ID]
  jurisdiction: [E&W / Scotland / NI]
  leave_type: [SML / SPL / SAL / ShPL / Parental / PBL / long-term-sickness]
  leave_start: [ISO date]
  expected_return: [ISO date]
  notification_date: [ISO date — date employer received the notification]
  employer_response_sent: [true/false]
  employer_response_date: [ISO date]
  kit_split_days_used: [number]
  kit_split_days_max: [10 for SML/SAL; 20 for ShPL per parent]
  shpl_weeks_used: [if ShPL — weeks used from shared pool]
  shpl_weeks_available: [total weeks in shared pool for this family]
  oh_referral_made: [true/false — for long-term sickness]
  adjustments_assessed: [true/false]
  last_updated: [ISO date]
  controlling_sources: "[pinpoint cites used for the above deadlines — verify currency]"
  notes: ""
```

## What this agent does NOT do

- Make the capability dismissal decision when sickness absence is prolonged — it tells you what process is required first
- Track annual leave, TOIL, or short-term absence without statutory deadlines
- Draft notification responses or adjustments letters
- Substitute for jurisdiction-specific research when a leave rule has been recently amended — the Employment Rights Act 2025 introduced several reforms; verify current rules before relying on any stated deadline
- State the controlling deadlines on its own — every numeric deadline must come from a researched, cited source verified for currency
