---
name: portfolio
description: >
  Track the UK IP portfolio — registrations, renewals, maintenance fees (UK
  IPO annual fees, EUIPO renewals, EPO annuities, Madrid Monitor). Use when
  checking what's renewing, adding or updating an asset, recording a filing,
  or auditing the register for gaps, lapses, and post-Brexit coverage issues.
  Receives handoffs from prosecution and clearance work.
argument-hint: "[--report [--days N] | --add | --update | --audit]"
---

# /portfolio

Surfaces what's renewing, adds assets, records filings, and audits the register.

## Instructions

1. **Follow the workflow below** and read
   `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/portfolio.yaml`.

2. **Default (no args):** equivalent to `--report` — show deadlines in the
   next 90 days grouped by urgency (🔴 lapsed/grace, ⏰ due within window,
   🟡 upcoming, 🌐 agent-managed, ❓ unknown).

3. **`--report [--days N]`:** Mode 2. Change the window with `--days`
   (30 / 60 / 90 / 180 typical). Always prepend the work-product header
   per CLAUDE.md → Outputs. Always close with the verification caveat.

4. **`--add`:** Mode 3. Walk through a new asset interactively — type,
   jurisdiction, number, dates, owner, business owner. Capture a custom
   rule if the jurisdiction isn't built in.

5. **`--update`:** Mode 4. Record that a maintenance filing or fee payment
   was made, sync with the IP management system, or change an asset's
   status. Enforce the consequential-action gate before setting any
   deadline to `filed`.

6. **`--audit`:** Mode 5. Broader health check — deadline hygiene,
   registration gaps, post-Brexit coverage gaps (UK/EU marks and designs),
   owner inconsistencies, expiration horizon, unwatched marks.

7. **If the register is empty and an IP management system is connected:**
   Offer Mode 1 — pull the portfolio from the system of record and
   initialise the register.

8. **Guardrail reminder:** Computed deadlines are reference only. Every
   output closes with a line directing verification against the UK IPO
   online records, EUIPO eSearch, WIPO Madrid Monitor, EPO Register,
   or the relevant national registry before filing or paying.

## Examples

```
/ip-legal-uk:portfolio
```

```
/ip-legal-uk:portfolio --report --days 180
```

```
/ip-legal-uk:portfolio --add
```

```
/ip-legal-uk:portfolio --update
```

```
/ip-legal-uk:portfolio --audit
```

---

## Works better connected

This skill tracks deadlines from what you tell it. It works much better
connected to:

- **An IP management system (IPMS) via MCP** — Anaqua, Clarivate IPfolio,
  CPA Global, AppColl, Patrix, Alt Legal. A connected IPMS gives you the
  full docket, maintenance fee schedules, and incoming correspondence.
- **UK IPO online records** — UK trade mark and patent status.
- **EUIPO eSearch Plus** — EU trade mark status.
- **EPO Online Register** — EP patent status and annuity records.
- **WIPO Madrid Monitor** — international trade mark status.

Without any of these, paste your docket or upload a spreadsheet.

## Purpose

A trade mark registration that isn't renewed on time can be cancelled. A
patent without its annual renewal fee paid lapses. A domain that expires can
be sniped within hours. This skill maintains the calendar.

## Important: deadline reference caveat

> The deadline rules this skill applies reflect publicly available requirements
> as of the skill's build date. UK IPO, EUIPO, EPO, WIPO Madrid Monitor
> requirements, grace periods, fee structures, and maintenance schedules change.
> **Always confirm computed deadlines against the UK IPO online records,
> EUIPO eSearch, EPO Register, WIPO Madrid Monitor, or the relevant national
> registry before acting.** If you use Anaqua, CPA Global, Clarivate, Alt Legal,
> or another IP management system, their docket is authoritative for your
> assets — use this tracker to organise and surface their data, not to replace it.
>
> A docketed-but-wrong deadline is worse than an undocketed one: it creates
> false confidence.

## Jurisdiction and type assumptions

Maintenance mechanics vary by jurisdiction and asset type:

**UK trade marks (UK IPO)**
- 10-year registration term from filing date, renewable for further 10-year periods.
- Renewal due before the expiry date; 6-month late renewal allowed with a surcharge (Form TM11).
- Action: file Form TM11 (or via a trade mark attorney) and pay the fee.

**EUIPO trade marks**
- 10-year registration term from filing date, renewable for further 10-year periods.
- Renewal due 3 months before expiry; 6-month grace period with surcharge.
- **Post-Brexit note:** EUIPO registrations do NOT cover UK territory since 31 Dec 2020. UK trade marks and EUTMs are entirely separate. Comparable UK marks were automatically created from existing EUTMs at the transition date, but those UK marks now have their own separate renewal dates at the UK IPO.

**Madrid international trade marks (WIPO)**
- 10-year term from registration date; renewable for further 10-year periods.
- Separate UK designation and EU designation must each be maintained.
- If the basic application/registration on which the international registration is based is cancelled or expires within the first 5 years ("central attack"), the UK / EU designations also fall.

**UK patents (UK IPO national)**
- Annual renewal fees payable on each anniversary of the filing date from the 4th anniversary onwards (Form RF1 / RP7, online).
- 6-month late payment period available with surcharge; after that, the patent lapses.
- 20-year maximum term from filing date (subject to supplementary protection certificates (SPCs) for qualifying pharma/biotech — UK SPCs are separate from EU SPCs post-Brexit).

**European patents (EP designating UK)**
- Granted by the EPO; UK validation required within 3 months of grant (Form EP(UK)1); UK renewal fees then apply from the 3rd or 4th year post-filing.
- Annual UK renewal fees payable at the UK IPO on each anniversary of the EP filing date.
- **UPC note:** The UK is NOT party to the Unified Patent Court. EP(UK) patents are managed entirely at the UK IPO; UPC opt-out decisions do not affect UK designations.

**EPO annuities (pre-grant)**
- Annual fees payable at the EPO from the 3rd year after EP filing.
- 6-month late payment with surcharge; failure to pay triggers application being deemed withdrawn.

**PCT applications**
- 30-month national/regional phase entry in most jurisdictions (some 31 months). UK IPO national phase entry at 30/31 months.
- Country-specific fees and requirements apply at national phase entry.

**UK registered designs (UK IPO)**
- 5-year initial protection period from registration date; renewable for up to 25 years total (5 renewals).
- 6-month grace period for late renewal with surcharge.
- **Post-Brexit note:** EU registered designs registered before 31 Dec 2020 generated comparable UK registered designs. New EU registered designs after 31 Dec 2020 do NOT cover UK.

**UK unregistered design right (CDPA 1988)**
- No registration; automatic on creation. No maintenance.

**UK supplementary unregistered design right (UK SUDR)**
- 3 years from first making available to the public in the UK. No maintenance.

**Domains**
- Annual or multi-year renewal per registrar; typical 30-day grace then redemption period (~30 days at high fee) then drop.

**EU trade marks (EUIPO) — post-Brexit note for existing comparable UK marks**
- Any existing EUTM that generated a comparable UK mark at transition (31 Dec 2020) now has a separate UK renewal date at the UK IPO. Check that both the EUIPO renewal and the comparable UK mark renewal are tracked separately.

If the portfolio includes assets in jurisdictions not listed above, capture
the maintenance mechanic in the register's `custom_rules` block and the
report will surface them as `agent_managed`.

---

## The register

Lives at `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/portfolio.yaml`.
Structure:

```yaml
# IP Portfolio Register
# Generated: [date]
# Last updated: [date]
# Disclaimer: computed deadlines are reference only — confirm with UK IPO /
# EUIPO / EPO / WIPO Madrid Monitor / relevant registry before acting.

metadata:
  company: "[Company Name]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"
  source_system: "[Anaqua / CPA Global / manual / none]"

custom_rules:   # non-built-in jurisdictions captured manually
  []

assets:
  - id: "TM-UK-001"
    type: "trademark"
    jurisdiction: "UK"               # UK / EUIPO / Madrid-UK / Madrid-EU / other
    mark_or_title: "[Mark]"
    owner: "[Record owner — registered entity name]"
    status: "registered"             # pending / registered / lapsed / abandoned / cancelled
    application_number: "[number or null]"
    registration_number: "[number or null]"
    classes: ["9", "42"]             # Nice classes
    filing_date: "[YYYY-MM-DD or null]"
    registration_date: "[YYYY-MM-DD or null]"
    comparable_uk_mark: false        # true if created from EUTM at Brexit transition 31 Dec 2020
    source_eutm: "[EUTM reg number or null]"   # if comparable_uk_mark is true
    next_deadlines:
      - type: "UK trade mark renewal"
        due_date: "[YYYY-MM-DD]"
        grace_end: "[YYYY-MM-DD or null]"
        basis: "10th anniversary of filing date"
        action: "File Form TM11 and pay renewal fee at UK IPO"
        status: "upcoming"           # upcoming / due_soon / overdue / grace / filed
    agent_managed: false
    local_agent: null
    docket_id: null
    outside_counsel: "[firm or null]"
    business_owner: "[email or team]"
    notes: ""

  - id: "PAT-UK-001"
    type: "patent"
    jurisdiction: "UK"               # UK national / EP(UK) / EP-GB / PCT-UK
    mark_or_title: "[Invention title]"
    owner: "[Owner]"
    status: "granted"
    application_number: "[number]"
    registration_number: "[patent number]"
    filing_date: "[YYYY-MM-DD]"
    grant_date: "[YYYY-MM-DD]"
    priority_date: "[YYYY-MM-DD or null]"
    expiration_date: "[YYYY-MM-DD]"  # 20 years from earliest priority; SPC may extend
    spc: false                       # true if Supplementary Protection Certificate granted
    spc_expiry: "[YYYY-MM-DD or null]"
    next_deadlines:
      - type: "UK annual renewal fee"
        due_date: "[YYYY-MM-DD]"
        grace_end: "[YYYY-MM-DD]"
        basis: "4th anniversary of filing date"
        action: "Pay UK IPO annual renewal fee (Form RF1)"
        status: "upcoming"
    claims_count: 20
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""
```

Status values for `next_deadlines`:
- `upcoming` — more than 90 days out
- `due_soon` — due within 90 days, not yet filed
- `overdue` — past the primary due date, within grace window (if any)
- `grace` — in the grace period (explicit flag — carries surcharge)
- `lapsed` — past grace with no action; asset effectively lost unless revivable
- `filed` — action completed this cycle

---

## Mode 1: Initialise

Run when no register exists, or with `--rebuild`.

### Step 1: Determine the source

Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`:
- **IP management system connected:** pull the portfolio via its integration. The system of record wins on conflicts.
- **No IP management system, but spreadsheet / export available:** import what's present; flag assets missing key dates.
- **Nothing at hand:** walk through assets interactively.

### Step 2: For each asset, compute deadlines

Apply the rules above. For comparable UK marks created from EUTMs at Brexit
transition: check that the UK mark's renewal date is independently captured
and not confused with the EUIPO renewal for the parent EUTM.

**For assets this skill cannot confidently schedule:**
- Unknown jurisdiction rules → add a stub under `custom_rules`, flag `agent_managed: true`.
- Missing dates → set `next_deadlines` empty with a note, list as `unknown`.

### Step 3: Write the register

```
Portfolio register initialised.

Assets: [N]
  Trade marks (UK IPO): [N]
  Trade marks (EUIPO): [N]
  International marks (Madrid): [N]
  Patents (UK national / EP(UK)): [N]
  Registered designs (UK): [N]
  Domains: [N]

Post-Brexit flags: [N] — assets where UK/EU split may need review
Agent-managed / jurisdiction TBC: [N]
Unknown (missing key dates): [N]

Run /ip-legal-uk:portfolio --report to see what's due.
```

---

## Mode 2: Report

```
/ip-legal-uk:portfolio --report [--days 30|60|90|180]
```

Default window: 90 days. Refresh computed deadlines for every asset before
producing the report.

Output (prepend work-product header):

```
IP PORTFOLIO DEADLINE REPORT — [date]
[Company Name] — window: next [N] days

🔴 LAPSED / IN GRACE ([N])
  [Asset ID] / [Jurisdiction] / [Type] / [Mark or title]
    [Action] — original due [date], grace ends [date]
    Status: [grace / lapsed]

⏰ DUE WITHIN [N] DAYS ([N])
  [Asset ID] / [Jurisdiction] / [Type] / [Mark or title]
    [Action] — due [date]
    Basis: [e.g., "10-year anniversary of UK registration date"]
    [Agent: firm / docket: id — if present]

🟡 UPCOMING (next window beyond 30 days, within [N] days)
  [list]

🌐 AGENT-MANAGED ([N])
  [Asset ID] / [Jurisdiction] — managed by [local agent]; confirm directly

❓ UNKNOWN ([N])
  [Asset ID] — missing [field]; cannot compute deadline

POST-BREXIT FLAGS
  [Any assets where UK/EU coverage gap may need review]

SUMMARY
  Total assets tracked: [N]
  Deadlines in window: [N]
  Last audit: [date]
```

Close with: *"Computed from portfolio register. Verify each deadline against
the UK IPO online records / EUIPO eSearch / WIPO Madrid Monitor / EPO Register
/ relevant national registry before filing or paying."*

If the report lists more than ~10 assets, offer the dashboard.

---

## Mode 3: Add

```
/ip-legal-uk:portfolio --add
```

Interactive add of a single asset. Ask for:
1. Type (trade mark / patent / copyright / design / domain)
2. Jurisdiction (UK IPO / EUIPO / EP / Madrid / other — note post-Brexit separation)
3. Mark or title / invention name
4. Owner (record owner — matters for renewal filings and assignments)
5. Key dates (filing, registration, grant, priority, expiration)
6. Number(s)
7. Classes / claims count
8. If trade mark: is this a comparable UK mark created from an EUTM at Brexit transition? Record `comparable_uk_mark: true` and `source_eutm`.
9. Source — is this tracked in the IP management system?
10. Outside counsel / foreign associate
11. Business owner

After capture:
- Compute next deadlines per the rules above.
- If jurisdiction rules aren't built in, walk through the `custom_rules` capture flow.
- Append to `assets:` in `portfolio.yaml`.

---

## Mode 4: Update

```
/ip-legal-uk:portfolio --update
```

### Consequential-action gate

**Before recording that a maintenance filing or fee payment was made:** Read
`## Who's using this` in CLAUDE.md. If the Role is **Non-lawyer**:

> Recording a UK trade mark renewal, a UK patent annual fee, an EUIPO renewal,
> or an EPO annuity payment as "filed" has consequences. If the record is wrong
> — missed deadline, wrong form, wrong entity — the deadline doesn't move and
> the asset can still lapse. Have you confirmed this with the solicitor, trade
> mark attorney, or Chartered Patent Attorney who actually made the filing, or
> with the UK IPO / EUIPO / EPO / Madrid Monitor directly? If yes, proceed.
> If no:
>
> - Do not record as filed yet.
> - Bring to the relevant professional: asset ID, jurisdiction, deadline type,
>   what you believe was filed and when.
>
> To find a Chartered Patent Attorney: CIPA (cipa.org.uk). To find a Registered
> Trade Mark Attorney: CITMA (citma.org.uk). For general legal advice: SRA
> register for solicitors (sra.org.uk).

Do not set a deadline's `status` to `filed` past this gate without an
explicit yes.

### Sub-modes

**Manual update:** "We filed the UK renewal for TM-UK-001 on [date]." Update the matching deadline: `status: filed`, `filed_date`, and compute the next deadline (next 10-year renewal).

**From IP management system sync:** Pull latest docket and reconcile. Flag mismatches; system of record wins; surface anything the register had that the system doesn't.

**Status change:** "Mark TM-UK-004 as abandoned." Update `status`, clear `next_deadlines`, note the date.

---

## Mode 5: Audit

```
/ip-legal-uk:portfolio --audit
```

Broader health check:

**Deadline hygiene**
- Any deadlines in `grace` status right now?
- Any `lapsed` assets not marked `abandoned` or `cancelled`?
- Any assets with no `next_deadlines` computed?

**Registration gaps**
- Trade mark applications filed more than 18 months ago still `pending`? Flag for status check at the UK IPO / EUIPO.
- Patents filed more than 4 years ago still `pending`? Flag for prosecution check.

**Post-Brexit coverage gaps**
- Any assets where the register shows EUIPO coverage but no UK IPO equivalent (or vice versa)? Post-Brexit, these are entirely separate registrations.
- Any comparable UK marks (created from EUTMs at transition) whose UK renewal dates are not separately tracked?
- Any Madrid international registrations where UK and EU designations are not both tracked?
- Any registered design portfolio entries that appear to be EU-only (not covering UK since 31 Dec 2020)?
- Any patent portfolio entries that reference UPC opt-out status (irrelevant for UK — UK is not party to the UPC)?

**Ownership hygiene**
- Any assets where the `owner` is not a currently active entity?
- Owner name inconsistencies across assets?

**Expiration horizon**
- Any patents expiring in the next 24 months? Any SPC expiry approaching?

**Unwatched assets**
- Any registered marks not on the watch list in CLAUDE.md → Brand protection?

Output format:

```
IP PORTFOLIO AUDIT — [date]

DEADLINE HYGIENE
  In grace: [N]
  Lapsed (not marked abandoned): [N]
  Missing next-deadline computation: [N]

REGISTRATION GAPS
  TM applications pending >18 months: [list]
  Patent applications pending >4 years: [list]

POST-BREXIT COVERAGE GAPS
  Assets with EUIPO but no UK IPO equivalent (or vice versa): [list]
  Comparable UK marks without separate UK renewal tracking: [list]
  Madrid designations where UK and/or EU not separately tracked: [list]
  Design portfolio EU-only gaps: [list]

OWNERSHIP
  Assets with unrecognised owner strings: [N]
  Owner name inconsistencies: [list]

EXPIRATION HORIZON (24 months)
  Patents expiring: [list]
  SPCs expiring: [list]

BRAND WATCH
  Registered marks not on watch list: [list]

RECOMMENDED ACTIONS
  1. [highest priority — usually any lapsed or grace items]
  2. [etc.]
```

---

## Integration: ip-renewal-watcher agent

The `ip-renewal-watcher` agent in this plugin runs this skill on a schedule
(weekly by default) and posts the Mode 2 report to the channel named in
CLAUDE.md → Renewal alerts. If 🔴 items appear (grace / lapsed), the agent
posts them immediately regardless of schedule.

## Handoffs

- Receives: new asset records from prosecution skills (when an application is filed or a mark clears), from clearance skills (when a mark is adopted and filing is queued).
- Sends: "file renewal now" triggers to the trade mark attorney or Chartered Patent Attorney — this skill doesn't file anything; it tells the attorney the deadline and what to bring.

## What this skill does not do

- **File anything.** Every action it surfaces is for the solicitor, trade mark attorney, or Chartered Patent Attorney to execute (or their instructed foreign associates for non-UK filings).
- **Pay renewal fees or annuities.** CPA Global and similar annuity services do that; this skill points at the deadline, not the payment.
- **Verify deadlines against the UK IPO / EUIPO / EPO / WIPO registers.** It computes from the dates you give it. The register is a working copy; the registry is the source of truth.
- **Decide whether to renew.** Renewal is a business and legal call. This skill surfaces the deadline and the cost; the business and the attorney decide.
- **Make post-Brexit coverage decisions.** It surfaces gaps; the IP team decides whether to file in the missing jurisdiction.
- **Replace an IP management system for multi-hundred-asset portfolios.** For large portfolios, Anaqua, CPA Global, and similar systems have direct registry feeds, deadline automation, and annuity payment services.
