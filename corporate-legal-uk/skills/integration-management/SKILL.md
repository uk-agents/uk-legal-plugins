---
name: integration-management
description: >
  Post-completion M&A integration tracker — phased workplan, consent tracking,
  contract assignment at scale, weekly status reports. Initialises from whatever
  deal artefacts are available (purchase agreement, deal summary, closing
  checklist) and connects to deal-context.md and closing-checklist.yaml from the
  M&A cold-start. Use when user says "integration", "post-completion", "post-closing",
  "consents outstanding", "contract assignment", "integration status", or
  "what's left on the deal".
argument-hint: "[--init | --contracts | --report | --update | --export [--format csv|table] [--section all|consents|contracts|workplan]] [--deal [code]]"
---

# /integration-management

1. Load `deal-context.md` for deal code, target, completion date, deal lead.
2. Load `integration-tracker.yaml` if it exists (or create on --init).
3. Use the workflow below.
4. Route by flag:
   - `--init`: Mode 1 — read SPA/APA, build phased workplan, consent tracker
   - `--contracts`: Mode 2 — import contract list (repository or upload), tier and classify
   - `--report`: Mode 3 — generate status report
   - `--update`: Mode 4 — manual update or parse uploaded status document
   - `--export`: Mode 5 — CSV or table export
5. Read/write `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/integration-tracker.yaml`.
6. After any write: show summary of changes and surface any new flags.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Outside solicitors complete the deal. Legal inherits the workstream. This skill is the
programme management layer for post-completion integration — not the business
integration, not IT systems, not HR org design. The legal workstream: consents,
contract assignments, entity rationalisation, IP recordals, SPA/APA obligations.
It tracks what's done, what's due, what's blocked, and what needs a decision.

UK terminology note: "completion" is the standard UK term for what US practice calls "closing". Both terms are used in this skill where context makes the meaning clear.

---

## Tracker file

Lives at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/integration-tracker.yaml`. Read `deal-context.md` for
the deal code, target name, completion date, and deal lead. Inherit any post-completion
items from `closing-checklist.yaml` if it exists.

```yaml
# integration-tracker.yaml

metadata:
  deal_code: "[code]"
  target: "[company name]"
  completion_date: "[YYYY-MM-DD]"
  deal_lead: "[name]"
  outside_solicitors: "[firm and lead solicitor]"
  last_updated: "[date]"
  last_status_report: "[date or null]"

spa_dates:
  required_consents_deadline: "[YYYY-MM-DD — extract from SPA/APA]"
  warranty_survival_expires: "[YYYY-MM-DD]"
  escrow_release: "[YYYY-MM-DD or null]"
  earnout_milestones:
    - description: "[milestone]"
      measurement_date: "[YYYY-MM-DD]"
      payment_date: "[YYYY-MM-DD]"
      owner: "finance"   # always finance — legal tracks date only

workplan:
  day_1:
    target_date: "[completion_date + 7 days]"
    items: []
  day_30:
    target_date: "[completion_date + 30 days]"
    items: []
  day_90:
    target_date: "[completion_date + 90 days]"
    items: []
  day_180:
    target_date: "[completion_date + 180 days]"
    items: []

required_consents: []
desired_consents: []

contracts:
  source: "[repository / manual-upload / disclosure-schedule]"
  repository_path: "[path or null]"
  last_imported: "[date]"
  total: 0
  tier_1: []
  tier_2: []
  tier_3: []
  tier_4: []
```

**Workplan item structure:**
```yaml
- id: "W-001"
  description: "[action item]"
  phase: "[day_1 / day_30 / day_90 / day_180]"
  owner: "[legal-owns / legal-supports]"
  workstream: "[legal / hr / it / finance / real-estate / other]"
  priority: "[critical / high / medium / low]"
  deadline: "[YYYY-MM-DD or null]"
  deadline_basis: "[spa-obligation / regulatory / best-practice]"
  status: "[not_started / in_progress / complete / blocked / deferred]"
  blocker: "[description or null]"
  depends_on: "[item id or null]"
  notes: ""
```

**Consent entry structure:**
```yaml
- id: "CON-001"
  counterparty: "[name]"
  contract_type: "[customer / vendor / lease / IP-licence / financial / other]"
  required_consent: true        # true = named in SPA Required Consents schedule
  spa_deadline: "[YYYY-MM-DD]"  # only for required_consent: true
  status: "[not_started / outreach_sent / in_negotiation / obtained / waived / refused]"
  assigned_to: "[name or null]"
  outreach_date: "[date or null]"
  obtained_date: "[date or null]"
  notes: ""
```

**Contract entry structure:**
```yaml
- id: "C-001"
  name: "[contract name or filename]"
  counterparty: "[party name]"
  contract_type: "[MSA / SaaS / lease / IP-licence / employment / NDA / other]"
  annual_value: "[amount or unknown]"
  assignment_mechanism: "[auto-assign / consent-required / coc-provision / silent]"
  tier: 1   # 1=Required Consent, 2=material+consent-required, 3=CoC, 4=auto-assign
  required_consent: false
  spa_deadline: "[YYYY-MM-DD or null]"
  status: "[not_reviewed / no_action / consent_pending / outreach_sent / in_negotiation / consent_obtained / assignment_complete / waived / refused / coc_triggered]"
  assigned_to: "[name or null]"
  notes: ""
  last_updated: "[date]"
```

---

## Mode 1: Initialise

```
/corporate-legal-uk:integration-management --init [--deal [code]]
```

### Step 1: Load deal context

Read `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/deal-context.md`. If not found: ask for deal code name,
target company, completion date, deal lead, and outside solicitors. Write to
deal-context.md if it doesn't exist.

Read `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/closing-checklist.yaml` if it exists. Any items marked as
post-completion become Day 1 or Day 30 workplan items (inherit status from
closing-checklist).

### Step 2: Read deal inputs

**A full SPA/APA produces the most complete tracker.** The agreement's Required
Consents schedule and post-completion covenants section are the authoritative source
for hard deadlines and legal obligations. But the skill can initialise usefully
from whatever is available — partial inputs produce a starter tracker the solicitor
fills in rather than an empty page.

> What deal artefacts do you have available? Share whatever exists:
>
> **Ideal:** The SPA or APA (upload or connected document path). I'll read
> the post-completion covenants, Required Consents schedule, warranty survival
> periods, escrow terms, and earn-out provisions.
>
> **Also useful — share any combination of:**
> - Deal summary or heads of terms (gives me the key economics and timeline)
> - Integration to-do list or post-completion checklist from outside solicitors
> - Existing workplan or integration tracker (I'll import and continue from it)
> - Closing checklist — if generated by the M&A cold-start skill, I'll inherit it
>   automatically from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/closing-checklist.yaml`
> - Required Consents list alone (if the SPA is held by outside solicitors)
>
> **If you have nothing written down:** Tell me the deal in plain terms — who was
> acquired, when it completed, what the main open items are — and I'll build a
> starter tracker from the standard Day 1/30/90/180 workplan that you edit.

**What changes based on what's provided:**

| Input | What you get |
|---|---|
| Full SPA/APA | Complete workplan + Required Consents with deadlines + SPA dates |
| SPA/APA + contract list | Full tracker + contract assignment tier list |
| Deal summary / to-do list | Standard workplan skeleton, Required Consents as placeholders |
| Nothing | Standard workplan scaffold; solicitor fills in consents and contract lists |

The tracker is designed to be built out progressively — a skeleton today, filled
in as more information becomes available.

**From the SPA/APA extract:**

*Required Consents schedule:*
- For each consent: counterparty name, contract type, and the contractual
  deadline. Set as required_consent: true with spa_deadline populated.

*Post-completion obligations:*
- Map each obligation to a workplan item. Assign to the correct phase based
  on the deadline. Tag as spa-obligation in deadline_basis.

*Key dates:*
- Required Consents deadline — extract from the SPA/APA
- Warranty survival expiry — pull the specific survival periods from the SPA/APA.
  General, fundamental, and tax warranty periods typically differ; pull
  each one the SPA/APA defines and record them separately. Do not assume a default.
- W&I (warranty and indemnity) insurance expiry — extract from the SPA/APA or W&I policy if available.
- Escrow release date(s) — extract from the SPA/APA
- Any earn-out measurement and payment dates — add to spa_dates.earnout_milestones,
  owner always set to "finance"

**TUPE note (asset purchases / business transfers):**
If the deal was structured as an asset purchase or business transfer (not a share purchase), TUPE Regulations 2006 obligations may survive completion. Flag TUPE obligations as Day 1/Day 30 items (employee liability information, consultation obligations, any outstanding TUPE claims). Share purchases do not trigger TUPE.

### Step 3: Build the phased workplan

Generate standard workplan items for each phase. Add SPA/APA obligations extracted
in Step 2. Items inherited from the closing checklist are pre-populated.

**Day 1 — legal-owns:**
- Company name change filing at Companies House (if target entity is being renamed) — Form NM01 or written resolution + notification to Companies House [priority: critical]
- Bank account signatory updates — notify bank with completion documentation [priority: critical]
- Registered office notification if changing — notify Companies House within 14 days [priority: high]
- Key IP assignment execution — if any IP assignments were deferred from completion [priority: critical]
- Domain name and social media account transfer [priority: high]
- D&O insurance — confirm tail policy is bound for acquired entity's outgoing directors [priority: critical]
- Companies House officer appointment/resignation filings — AP01/TM01 as required, within 14 days [priority: high]
- PSC register update notification — if PSC has changed, file at Companies House within 14 days [priority: critical]

**Day 1 — legal-supports:**
- Employee announcement and communications (HR owns, legal reviews) [priority: critical]
- Benefits day-1 coverage confirmation (HR owns, legal advises on TUPE obligations where applicable)
- Customer communication letters (business owns, legal reviews for accuracy)

**Day 30 — legal-owns:**
- Required Consents initial push — contact all counterparties, document outreach [priority: critical]
- IP assignment recordal at UKIPO (patents, trademarks, designs) [priority: high]
- Trade mark assignment recording — UKIPO Form TM16 [priority: high]
- Material contract review — complete tier 1 and tier 2 contract assignment analysis [priority: high]
- Insurance tail policy final confirmation [priority: high]
- Charge satisfaction or assignment filings at Companies House — MR04 if charges being released [priority: high]

**Day 30 — legal-supports:**
- Data migration privacy review — ICO notification if applicable (IT owns, legal advises on UK GDPR obligations)
- Real estate lease review for assignment provisions (facilities owns, legal advises)

**Day 90 — legal-owns:**
- Required Consents deadline — all Required Consents must be obtained or escalated [priority: critical, deadline: spa_dates.required_consents_deadline]
- Entity rationalisation decision — recommend keep separate / merge / dissolve [priority: high]
- Secondary consent push — remaining outstanding consents [priority: high]
- Tier 3 change-of-control contract resolution [priority: critical]
- TUPE outstanding matters — any remaining employee liability claims (asset purchase only) [priority: high]

**Day 90 — legal-supports:**
- Full HR harmonisation documentation (HR owns, legal advises on employment law)

**Day 180 — legal-owns:**
- Entity merger filing — if rationalisation decision is to amalgamate [priority: high]
- Entity voluntary striking off — if rationalisation decision is to wind down (CA2006 s.1003, or MVL if assets) [priority: high]
- Full contract novation — contracts requiring buyer entity's name [priority: high]
- Warranty survival tracking — note upcoming expiry date [priority: medium]
- Confirmation Statement (CS01) — due at first anniversary of completion if incorporated entity [priority: medium]

Show summary after generating:

```
Integration tracker initialised — [Deal code] / [Target]

Completion date: [date]
Required Consents deadline: [date] ([N] days from today)
Warranty survival expires: [date]

Workplan items: [N] ([N] legal-owns, [N] legal-supports)
Required Consents: [N] (from SPA/APA schedule)
Desired Consents: [N] (from diligence — no SPA deadline)

Contract assignment: not yet imported — run --contracts to populate

Next step: run /corporate-legal-uk:integration-management --contracts to import the
contract list, then --report to see your first status summary.
```

---

## Mode 2: Contract Assignment

```
/corporate-legal-uk:integration-management --contracts [--deal [code]]
```

This is the dedicated contract assignment initialisation. Separate from the
main init so it can be run independently and re-run when the contract list
changes.

### Step 1: Get the contract list

Two paths — use whichever applies:

**Path A: Connected repository**

> Is your contract repository connected? (Google Drive, Box, SharePoint,
> or a VDR that's still accessible post-completion?)
>
> If yes: give me the folder path or folder name for the acquired company's
> contracts. I'll pull a list of what's there and read each contract for the
> assignment clause and counterparty.

Search the connected repository. For each document found:
- Extract filename and file path
- Read the document — identify: contract party (counterparty name), contract
  type (from header or subject matter), assignment clause text, change of
  control clause text if present, and annual value if stated.

**Path B: Manual list upload**

> Upload a contract list. This can be:
> - The Material Contracts schedule from the SPA/APA disclosure schedules
> - A CSV or Excel export from their contract management system
> - A manually prepared list
>
> Minimum required columns: Contract Name, Counterparty. Helpful but optional:
> Contract Type, Annual Value, Assignment Clause text.

Read the uploaded list. For contracts where no assignment clause text is
provided, set assignment_mechanism to "not_reviewed" and flag for follow-up.

**Path C: Disclosure schedule**

If neither repository nor list is available, read the Material Contracts
schedule from the SPA/APA disclosure schedules (from the SPA/APA uploaded in --init).
This gives the minimum required list — parties and contract types. Assignment
clauses will need manual review.

### Step 2: Determine assignment mechanism

For each contract, classify the assignment mechanism:

| Mechanism | Definition | Tier |
|---|---|---|
| `consent-required` | Explicit clause prohibiting assignment without counterparty consent | 1 or 2 |
| `coc-provision` | Change-of-control clause giving counterparty termination or consent right triggered by the deal | 3 |
| `auto-assign` | No restriction, or explicit permission to assign to affiliates or successors | 4 |
| `silent` | No assignment clause — default to governing law. Under English law, the benefit of a contract may generally be assigned without consent; the burden requires consent. Research the applicable rule for this contract and flag for solicitor review. | 2 |
| `not_reviewed` | Could not read or locate assignment clause | Flag for manual review |

**Scottish law note:** Scots law on assignation differs from English law. For contracts governed by Scots law, flag separately and confirm analysis with Scottish counsel. `[model knowledge — verify with Scottish solicitors]`

For contracts flagged in the Required Consents SPA schedule: override tier to 1
regardless of assignment mechanism classification.

### Step 3: Tier assignment

```
Tier 1 — Required Consents: [N] contracts
  Named in SPA/APA schedule, hard deadline [date], must obtain consent

Tier 2 — Material, consent required: [N] contracts
  Assignment restriction present, not in SPA schedule
  Recommended timeline: obtain within Day 90

Tier 3 — Change-of-control provisions: [N] contracts ⚠️
  Counterparty has termination or consent right triggered by completion
  ACTION REQUIRED: contact counterparty immediately — CoC may already be triggered

Tier 4 — Auto-assign / no action: [N] contracts
  Assigns automatically or by affiliate/successor provision
  Tracking only — no outreach needed

Not reviewed: [N] contracts
  Could not determine assignment mechanism — manual review required
```

Show tier 3 separately and prominently. A change-of-control clause may have
already triggered on the completion date — counterparty may have a right to terminate
that is running right now.

### Step 4: Generate status entries

For each contract, create a tracker entry with:
- All extracted fields (counterparty, type, value, mechanism, tier)
- Initial status: tier 4 → `no_action`; tier 3 → `coc_triggered`; tiers 1/2 → `consent_pending`; not_reviewed → `not_reviewed`
- spa_deadline populated for tier 1 from Required Consents schedule

---

## Mode 3: Status Report

```
/corporate-legal-uk:integration-management --report [--deal [code]]
```

Reads current tracker state. Produces:

```
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This status report is derived from the SPA/APA, diligence findings, and post-completion integration records. It inherits their privilege and confidentiality status — distribution beyond the privilege circle can waive legal professional privilege. Confirm the recipient list before sending.

INTEGRATION STATUS — [Deal code] / [Target]
[Date] — Day [N] post-completion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
[2-3 sentence paragraph: overall status, biggest risk, key win since last report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REQUIRED CONSENTS  [deadline: DATE — N days remaining]
  Obtained:        [N] of [total]  ████████░░  [%]
  In negotiation:  [N]
  Outreach sent:   [N]
  Not started:     [N]
  Refused:         [N] ⚠️

⚠️ AT RISK: [counterparty] — deadline in [N] days, no response to outreach
⚠️ REFUSED: [counterparty] — SPA/APA obligation not met; escalate to outside solicitors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONTRACT ASSIGNMENT
  Tier 1 (Required Consents):   [N] complete / [N] in progress / [N] pending
  Tier 2 (Material contracts):  [N] complete / [N] in progress / [N] pending
  Tier 3 (CoC provisions):      [N] resolved / [N] outstanding ⚠️
  Tier 4 (Auto-assign):         [N] — no action required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WORKPLAN — LEGAL OWNS
  🔴 OVERDUE ([N]):
    [item] — was due [date]

  ⏰ DUE THIS WEEK ([N]):
    [item] — due [date]

  ✅ COMPLETED SINCE LAST REPORT ([N]):
    [item] — completed [date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BLOCKERS & DECISIONS NEEDED
  [item] — blocked on: [description] — owner: [name]
  [item] — decision needed: [description] — recommend: [option]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY DATES COMING UP
  [date] — [milestone / deadline]
  [date] — Warranty survival expires — confirm no pending indemnification claims
  [date] — Confirmation Statement (CS01) due at Companies House
```

---

## Mode 4: Update

```
/corporate-legal-uk:integration-management --update [--deal [code]]
```

**Manual update:** Solicitor tells Claude what changed.

> "We got the Salesforce consent. Mark it obtained, assigned to [name], date today."
> "The entity rationalisation decision is to merge. Update status and add the
> merger filing to Day 180."
> "[Counterparty] refused consent. Flag it and note we need outside solicitors on
> whether this triggers a SPA indemnification claim."

Claude updates the relevant tracker entry, recalculates any downstream status
(e.g., if all tier 1 consents are now obtained, flag the SPA obligation as met),
and shows what changed.

**Upload update:** Workstream owner or outside solicitors send a status document.

> Upload the status update from [outside solicitors / HR lead / corp dev team].
> I'll parse it and update the tracker.

Read the uploaded document. Match described items to tracker entries by
counterparty name or workplan item description. Update status fields.
Flag any items in the update that don't match an existing tracker entry —
may be new items to add.

After any update, show:
```
Updated [N] items.

Changes:
  CON-003 Salesforce: not_started → obtained
  W-014 Entity rationalisation: in_progress → complete

New flags:
  CON-007 [Counterparty]: refused — SPA obligation may be unmet. Consider:
  outside solicitors' review of indemnification claim. ⚠️
```

---

## Mode 5: Export

```
/corporate-legal-uk:integration-management --export [--format csv|table] [--section all|consents|contracts|workplan]
```

Produces a flat CSV or markdown table. Default: all sections, CSV.

CSV format — one row per item, section indicated by a `section` column.
Columns vary by section:

*Workplan:* id, phase, description, owner, workstream, priority, deadline, status, blocker

*Consents:* id, counterparty, contract_type, required_consent, spa_deadline, status, assigned_to, obtained_date, notes

*Contracts:* id, name, counterparty, contract_type, annual_value, assignment_mechanism, tier, required_consent, spa_deadline, status, assigned_to, notes

Export is the shareable format — suitable for outside solicitors, corp dev, or a
board integration update.

---

## What this skill does not do

- It does not manage business integration workstreams (IT, HR, finance, real
  estate). It tracks legal's touchpoints in those workstreams and flags when
  legal input is needed. Ownership stays with the business function.
- It does not draft the consent request letters or novation agreements — those
  are produced by the written-consent skill or by outside solicitors.
- It does not advise on indemnification claims or SPA/APA breach. When a consent is
  refused or a deadline is missed, it flags the situation — the legal analysis
  of consequences is the solicitor's call.
- It does not track earn-out performance. Earn-out milestones and payment dates
  appear in the tracker as reference dates with owner set to finance. The
  business drives the numbers.
- It does not read contracts in real time during status reporting. Contract
  status is what the solicitor has updated in the tracker. The skill reads the
  tracker, not the contracts, at report time.
- It does not advise on TUPE compliance — it flags TUPE obligations for the
  employment solicitor to advise on.

## Formula injection defence

Before writing any cell in Excel, Sheets, or CSV output, neutralise formula injection. Counterparty-sourced text (contract quotes, party names, registered agent data, CLM exports) is attacker-controlled. A cell starting with `=`, `+`, `-`, `@`, `	`, or a newline will be interpreted as a formula or break the row structure.

- **Prefix with a single quote:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (displayed as text, not executed)
- **Applies to every cell that contains text sourced from a document, a tool result, or a user paste.** Column headers you control and computed values you produce are safe.
- **CSV: also escape embedded commas, double quotes, newlines** (RFC 4180 quoting).
- This is not optional. A spreadsheet your user opens in Excel that triggers a macro or exfiltrates data via DDE is a supply-chain attack on your user.
