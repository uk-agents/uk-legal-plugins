---
name: log-leave
description: >
  Add a new statutory leave to the leave register with the minimum information
  needed to start tracking deadlines. Use when an employee goes on statutory
  leave and you want the tracker to watch notification response, return-date
  change, and reasonable-adjustments deadlines from day one.
argument-hint: "[describe the leave — employee/role, type, jurisdiction, start date]"
---

# /log-leave

Adds a new leave entry to `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/leave-register.yaml` with the minimum
information needed to start tracking deadlines. Use when an employee goes on
leave and you want the tracker to watch the clocks from day one.

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdiction table and Systems section.

2. Ask all of the following in a single prompt — do not drip them one at a time:

   > A few quick questions to set up leave tracking:
   >
   > - Employee name or role (anonymised is fine)
   > - Where do they work? (E&W / Scotland / NI — this determines which rules apply)
   > - Leave type: SML (maternity) / SPL (paternity) / SAL (adoption) / ShPL (shared parental) / Parental / Parental Bereavement / long-term sickness
   > - Leave start date
   > - Notification date (when did the employer receive the statutory notification?)
   > - Expected return date (if known — leave blank if not)
   > - For ShPL: weeks taken from the shared pool; which parent is on leave
   > - For long-term sickness: has an OH referral been made? Has an adjustments assessment been initiated?

3. Using the jurisdiction table in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`, look up the applicable leave entitlement period for this leave type.

4. Compute the first upcoming deadline based on the information provided:
   - SML/SAL notification received but employer response not sent → deadline is 28 days from notification
   - ShPL booking notice received but no employer response → 2-week response window from notice date
   - Long-term sickness, no OH referral → flag immediately if absence exceeds 4 weeks
   - Both notification and response sent → next deadline is the return date or any change-of-date notice window

5. Write a new entry to `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/leave-register.yaml` using the leave register
   format from the leave-tracker agent. If the file doesn't exist, create it.

6. Confirm with a single line:
   > "Logged. [Employee/Role] — [Leave type] — [Jurisdiction] — started [date].
   > First deadline: [what it is and when]. Leave tracker will alert automatically."

## Examples

```
/employment-legal-uk:log-leave
```

```
/employment-legal-uk:log-leave
Sarah (Sr. Engineer, works in London) just started statutory maternity leave
today. Employer received her 15-week notification last month. No response sent yet.
```
