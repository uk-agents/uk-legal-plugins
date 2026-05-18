---
name: closing-checklist
description: >
  What's blocking completion — maintain the closing checklist with status,
  critical path, and days to completion. Self-updating: ingests new items
  from diligence findings and schedule builds, tracks status, surfaces what's
  blocking. UK-specific: covers CMA merger control, FCA Part XII change of
  control, Panel conditions, and CA2006 corporate approvals. Use when user
  says "closing checklist", "what's left to close", "checklist status",
  "add to the checklist", or on a scheduled status pull.
argument-hint: "[optional: item ID + status update]"
---

# /closing-checklist

1. Read `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/closing-checklist.yaml` and use the modes below.
2. If status update provided: Mode 3 (update item).
3. Otherwise Mode 4: blocking items, critical path, days to completion.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Deals complete when the checklist is done. Everything on it, done. Nothing missing. This skill maintains the list, ingests new items as they surface from diligence, and tells the team what's blocking completion ("closing" in UK practice terminology is often called "completion").

## The checklist

Lives at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/closing-checklist.yaml`. Structure:

```yaml
deal_code: "Project Falcon"
target_completion: [DATE]
exchange_date: [DATE]
last_updated: [DATE]

conditions_precedent:
  - id: CP-001
    item: "CMA Phase 1 clearance (or expiry of waiting period)"
    category: "Regulatory"
    responsible: "Buyer's solicitors"
    due: 2026-07-15
    status: "Notified to CMA 2026-06-01; initial period runs 40 working days"
    blocking: true
    source: "SPA §7.1(a); Enterprise Act 2002 s.34ZA"

  - id: CP-002
    item: "FCA Part XII change of control approval — [Target FCA firm]"
    category: "Regulatory"
    responsible: "Target — [name]"
    due: 2026-07-20
    status: "Change of control notification submitted 2026-06-10; assessment period 60 working days"
    blocking: true
    source: "SPA §7.1(b); FSMA 2000 ss.178–191C"

  - id: CP-003
    item: "Acme Ltd consent to assignment — MSA §14.2"
    category: "Third-party consents"
    responsible: "Target — [name]"
    due: 2026-07-25
    status: "Request sent 2026-06-15, no response"
    blocking: true
    source: "Schedule [X](a)(3); Acme MSA §14.2"

completion_deliverables:
  - id: CD-001
    item: "Target's certificate of good standing — Companies House"
    category: "Corporate"
    responsible: "Target's solicitors"
    due: 2026-07-28
    status: "Not started"
    blocking: true
    source: "SPA §2.3(b)(iv)"

  - id: CD-002
    item: "Executed share transfer forms (stock transfer form — J30)"
    category: "Corporate"
    responsible: "Sellers' solicitors"
    due: 2026-07-29
    status: "Not started"
    blocking: true
    source: "SPA §2.3(b)(i)"

  # ... etc
```

## Modes

### Mode 1: Initialise from the SPA/APA

Read the signed (or near-final) SPA/APA. Extract:

- Every condition precedent (read the actual conditions section — not a generic assumption)
- Every completion deliverable (completion mechanics schedule or corresponding section)
- Every covenant with a pre-completion deadline

Each becomes a checklist item with a source cite to the agreement section.

**Research obligations before populating regulatory/approval items.** UK regulatory approvals have jurisdiction-specific mechanics, thresholds, and timing windows that change. Extract the name of each regulatory condition from the agreement, then research the currently operative mechanics. Cite primary sources and verify currency. Do not populate a timing assumption from memory.

**Key UK regulatory items to research and populate:**

- **CMA merger control (Enterprise Act 2002):** UK has a voluntary notification regime (no mandatory pre-notification). CMA can investigate post-completion. If voluntarily notified: Phase 1 = 40 working days initial period; Phase 2 = up to 24 weeks. Jurisdictional thresholds: (a) combined UK turnover >£70m OR (b) share of supply test (>25% in any UK market). Note: CMA has power to issue interim orders preventing further integration. Research current thresholds and merger notification guidance. `[model knowledge — verify current CMA guidance]`
- **FCA change of control (FSMA 2000 Part XII):** Required where target is an FCA-authorised firm (or controlled by one). Controller must submit a notification (Form K) to the FCA. Assessment period: 60 working days (extendable). Research current FCA notification requirements. `[model knowledge — verify current FCA guidance]`
- **PRA change of control:** Required for PRA-regulated firms (banks, building societies, insurers). Similar mechanics to FCA. Usually submitted simultaneously. `[model knowledge — verify]`
- **Panel on Takeovers and Mergers (public company deals):** If target is a listed company, the Takeover Code applies. Rule 9 mandatory offer; consent conditions under the Code. Offer timetable strictly controlled by the Panel. `[model knowledge — verify current Code provisions]`
- **Sector-specific approvals:** Ofgem (energy), Ofwat (water), Ofcom (telecoms/broadcasting), CQC (health), CMA Phase 2 (complex mergers). Research applicable sector regulator requirements for the specific deal.

**Material adverse change / material adverse effect closing conditions.** Pull the defined MAC/MAE term from the SPA/APA — framing is negotiated. Under English law, MAC clauses are interpreted narrowly (courts are reluctant to find a MAC); research English case law on MAC interpretation before flagging an event as a potential MAC trigger. `[model knowledge — verify current English MAC case law position]`

**Consent-requirement extraction from material contracts** depends on the specific contractual language and English law default rules. Research the applicable rule per contract rather than assuming a default.

### Mode 2: Ingest from diligence (the "self-updating" part)

Mode 2 is triggered when an upstream skill produces a finding with a pre-completion action. The upstream skills and output types this mode ingests:

- **`diligence-issue-extraction` findings** — any finding flagged for a completion action (consent, shareholder vote, board resolution, regulatory filing, release, escrow mechanic, pay-off letter, TUPE obligation).
- **`material-contract-schedule` CoC / assignment items** — change-of-control provisions, anti-assignment clauses, MFN triggers.
- **`deal-team-summary` output** — reads the latest deal-team-summary in the deal folder and reconciles its completion-action items against the checklist.

The handoff schema covers the full range of pre-completion actions:

```yaml
handoff:
  # Required fields
  item: "[Counterparty or action, one line]"
  category: "[Third-party consents | Shareholder / board action | Regulatory approval | Release / termination | Escrow / holdback | Completion deliverable | TUPE obligation]"
  source: "[Contract name / statutory section / VDR path + Bates]"
  blocking: true  # unless the agreement has a materiality qualifier
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — carried from upstream, see severity-floor rule in CLAUDE.md]"

  # Consent / third-party action fields
  counterparty: "[e.g., Acme Ltd]"
  guarantor: "[e.g., Buyer parent guarantee required, or N/A]"
  conditions: "[any substantive condition the counterparty attached]"
  notice_deadline: "[e.g., 30 days prior to completion, or specific date]"

  # Corporate action fields
  approval_body: "[Shareholders | Board | Committee | Regulator | Panel]"
  approval_threshold: "[e.g., 75% by value CA2006 s.190 / special resolution / unanimous board]"
  statutory_or_charter_source: "[e.g., CA2006 s.190; Articles Art. 12]"

  # Timing
  estimated_time_to_complete: "[e.g., 30 days]"
  must_occur_before: "[e.g., completion | exchange | end of offer period]"
```

Preserve every field the upstream skill populated. Append to the checklist. De-dupe on (counterparty + action type), not on the freeform item name. When de-duping, merge fields rather than overwrite.

### Mode 3: Status update

User (or dataroom-watcher agent) provides a status update. Find the item, update status and last-updated.

```
/corporate-legal-uk:closing-checklist
CP-003: Acme responded, consent form attached, needs countersignature
```

### Mode 4: What's blocking

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This status report is derived from the SPA/APA, diligence findings, and internal deal records. It inherits their LPP status — distribution beyond the privilege circle (counterparty, broader business teams) can waive privilege. Confirm the distribution list before sending.

## Completion Checklist Status — [Deal code] — [date]

**Target completion:** [date] ([N] days out)
**Items:** [N] total — [N] done, [N] in progress, [N] not started

### 🔴 Blocking and at risk

| ID | Item | Due | Status | Days to due |
|---|---|---|---|---|
| [CP-XXX] | [item] | [date] | [status] | **[N]** |

### 🟡 Blocking, on track

[same table]

### ✅ Complete

[N] items — [collapsed list]

### Not blocking (post-completion, informational)

[N] items

---

**Critical path:** [The item(s) that, if they slip, push the completion date]
```

## Critical path analysis

Not all blocking items are equal. CMA clearance (40+ working days) is critical path. A good-standing search that takes 2 days is not, even though both are blocking.

For each blocking item, estimate time-to-complete. The ones where `(due date - today) < estimated time` are at risk. Those go at the top of every status report.

If the checklist has more than ~10 items, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`).

## Integration: dataroom-watcher agent

The agent checks the checklist on schedule, pulls any status updates from email/Slack if connected, and posts the "what's blocking" report to the deal team channel. Mode 4 is the agent's output.

## Consequential-action gate (certify completion)

**Before producing a "ready to complete / all CPs satisfied" certification or completion memo:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Certifying that completion conditions have been satisfied (or producing a completion memo asserting this) has legal consequences — it's the signal that drives funds transfer, title transfer, and post-completion obligations. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
>
> - The full CP list with status (what's done, what's in progress, what's not started)
> - Anything where evidence of completion is weak or missing
> - Any waivers needed for items that won't be satisfied in time
> - Open questions (counterparty consents still pending, any MAC/bring-down risk, CMA / FCA approval status)
> - What to ask the solicitor (is this ready to complete; are any conditions being walked past that shouldn't be; what needs to go on a schedule of exceptions)
>
> If you need to find a solicitor: contact the SRA at sra.org.uk, the Law Society of Scotland at lawscot.org.uk, or the Law Society of Northern Ireland at lawsoc-ni.org for a referral service.

Do not produce a final "ready to complete" certification past this gate without an explicit yes. Status tracking and "what's blocking" reports do not require the gate.

---

## What this skill does not do

- It doesn't obtain consents, file forms, or draft documents. It tracks that they need to happen.
- It doesn't decide what's blocking — the SPA/APA decides that. This skill reads the agreement.
- It doesn't complete the deal. It tells you when you can.
- It doesn't assess whether CMA merger control notification is mandatory — that analysis requires outside solicitors' input; this skill tracks the status once the decision has been made.
