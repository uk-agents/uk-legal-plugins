---
name: escalation-flagger
description: >
  Route a contract issue to the right approver per the escalation matrix in
  `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`, and draft the ask. Includes
  UK regulatory referral triggers (CMA, FCA, ICO, Companies House). Use when the
  user says "who needs to approve this", "escalate this", "does this need Head of
  Legal sign-off", "route this for approval", or when another skill finds an issue
  that exceeds the reviewer's authority.
argument-hint: "[describe the issue, or reference a review memo]"
---

# /escalation-flagger

Names the approver for a contract issue per the `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` escalation matrix and drafts the message so you're not writing "hey got a sec" at 5pm.

## Instructions

1. **Load `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`** → Escalation section. If missing, say so — the practice profile needs editing.

2. **Characterize the issue:** pound threshold / term deviation / automatic trigger / regulatory trigger / business decision.

3. **Match to matrix, name the approver.** Be specific — a person or role, not "legal leadership."

4. **Draft the ask** per the template below: what the contract says, what playbook says, options with recommendation, decision-by date.

5. **Do not send.** Draft it, show it, let the solicitor send.

## Examples

```
/commercial-legal-uk:escalation-flagger
The Acme MSA has uncapped liability — who approves and what do I say?
```

```
/commercial-legal-uk:escalation-flagger
Reference: acme-review-memo.md
Issue: §8.2 indemnity carveouts
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Every contracts team has an escalation matrix, written or not. This skill reads the written one, matches a contract issue against it, names the approver, and drafts the ask so the solicitor isn't writing "hey do you have a sec" messages at 5pm.

## Load the matrix

**Which side?** Before matching to the matrix, determine which side the company is on for the contract being escalated. Read the matching playbook section to evaluate whether the term is inside fallbacks or triggers an automatic escalation. Note which side in the drafted ask.

Read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` → `## Escalation`. If it's missing or vague, say so.

Expected structure:

| Can approve | Threshold | Escalates to | Via |
|---|---|---|---|
| Paralegal | Standard terms, <£50K | Solicitor/Counsel | Slack |
| Solicitor/Counsel | Non-standard but within fallbacks, <£500K | Head of Legal/GC | Slack or email |
| Head of Legal/GC | Everything else | CFO/Board | Meeting |

Plus **automatic escalation triggers** — things that escalate regardless of pound value. Typically: unlimited liability, IP assignment, anything on the "never accept" lists, and UK regulatory triggers.

**UK regulatory triggers (check for each):**

- **CMA (Competition and Markets Authority):** Agreements that may restrict competition — horizontal price-fixing, market-sharing, or vertical restraints above market-share thresholds; potential Chapter I or Chapter II violations (Competition Act 1998). If flagged: "A solicitor with competition law expertise should review before signature. Consider voluntary disclosure to CMA if there is any doubt about compliance." `[model knowledge — verify]`
- **FCA (Financial Conduct Authority):** Contracts involving regulated activities (payment processing, financial promotions, insurance intermediation, credit agreements). If flagged: "FCA authorisation or permission may be required. A solicitor with financial services regulatory expertise should advise before signature." `[model knowledge — verify]`
- **ICO (Information Commissioner's Office):** High-risk data processing requiring a DPIA (UK GDPR Article 35); data breaches requiring notification within 72 hours (Article 33); processing arrangements that may constitute a breach of Article 28 (processor obligations). `[model knowledge — verify]`
- **Companies House:** Charges over company assets require registration within 21 days of creation (Companies Act 2006 s.859A). Failure to register means the charge is void against a liquidator, administrator, or creditor. `[model knowledge — verify]`

## Workflow

### Step 1: Characterize the issue

What's being escalated?

- **Pound threshold:** Contract value exceeds someone's approval authority
- **Term deviation:** A term is outside the playbook fallbacks — someone more senior needs to decide whether to accept
- **Automatic trigger:** One of the always-escalate items is present
- **Regulatory trigger:** CMA / FCA / ICO / Companies House notification or authorisation may be required
- **Business decision:** Not a legal call — needs the business owner, not legal leadership

Don't escalate things that are actually fine. If the term is within the fallbacks in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`, it doesn't need to go up.

### Step 2: Match to the matrix

```
Is the issue a regulatory trigger?
  → YES: escalate to [solicitor with relevant regulatory expertise] AND flag for possible regulatory notification
  → NO: continue

Is the issue an automatic (internal) trigger?
  → YES: escalate to [person named for that trigger]
  → NO: continue

Is the contract value above the reviewer's threshold?
  → YES: escalate to whoever has authority at that pound level
  → NO: continue

Is the term deviation outside all documented fallbacks?
  → YES: escalate to whoever can approve non-standard terms
  → NO: reviewer can approve — no escalation needed
```

### Step 3: Name the approver

Be specific. Not "escalate to legal leadership" — name the person or role from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the matrix doesn't name anyone for this situation, say so.

For regulatory triggers, name both the internal approver AND the relevant UK regulator/solicitor route:
- CMA: competition solicitor / Head of Legal with competition experience
- FCA: financial services regulatory solicitor
- ICO: privacy counsel / DPO (if appointed)
- Companies House: Head of Legal (charge registration is administrative but time-critical — 21 days)

### Step 4: Draft the ask

The approver should be able to decide from the message alone — no "let me pull up the contract."

```markdown
**Escalating to:** [name]
**Via:** [Slack #channel / email / meeting — per `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`]
**Urgency:** [deadline if there is one]
**Regulatory flag:** [if applicable — e.g., "Possible CMA Chapter I issue — competition solicitor review recommended before signature"]

---

Hey [name] —

Need your call on the [Counterparty] [agreement type]. [One sentence on deal context.]

**The issue:** [Plain English, one paragraph. What they want, why it's outside
our standard under English contract law / UCTA 1977 / UK GDPR, what the risk actually is.]

**What the contract says:**
> "[exact quote]"

**What our playbook says:** [quote from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`]

**Applicable UK law / regulatory context:**
[e.g., "Under UCTA 1977 s.3, this exclusion must satisfy the reasonableness test in a B2B standard-terms context. `[model knowledge — verify]`"
Or: "This arrangement may constitute a Chapter I infringement under the Competition Act 1998. `[model knowledge — verify]`"
Or: "UK GDPR Article 28 requires these sub-processor obligations to be included. `[model knowledge — verify]`"]

**Options:**
1. **Accept** — [one line on why this might be okay]
2. **Push back with:** "[proposed counter-language]" — [one line on likely counterparty reaction]
3. **Walk** — [one line on whether that's realistic given the business context]

**My recommendation:** [which option and why, briefly]

**Need a decision by:** [date, if there is a deadline]

[Link to full review memo]
```

### Step 5: Record the escalation

If this team uses a ticket system or CLM approval workflows, log it. If not, note in the review memo that the escalation was sent, to whom, and when.

## Calibration: when in doubt, escalate with a note

The cost of an unnecessary escalation is ~30 seconds of the approver's time. The cost of a missed escalation is signing an unapproved term or missing a regulatory notification window. The costs are not symmetric. **When in doubt, escalate.**

The calibration for what warrants escalation lives in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`, not in this skill. Check the playbook's stated position, its fallbacks, and its "automatic escalation regardless of contract value" list.

**For regulatory triggers:** err strongly on the side of escalation. A missed ICO notification has a 4-week window (72 hours for data breach notification — UK GDPR Article 33). A missed Companies House charge registration renders the charge void. These deadlines do not have fallbacks.

Do not suppress an escalation because over-escalation might train approvers to skim. That's an approver-experience problem the solicitor solves by adjusting thresholds in the playbook.

If a term comes up that the playbook doesn't address, don't guess the threshold — ask the reviewing solicitor whether this class of issue should escalate, and offer to record the answer in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.

## What this skill does not do

- It does not approve anything. It routes.
- It does not decide between the options. The draft includes a recommendation but the approver decides.
- It does not send the escalation message — it drafts it. The solicitor sends it after reading.
- It does not advise on regulatory compliance — it flags that regulatory expertise may be needed and names the right internal or external route.
