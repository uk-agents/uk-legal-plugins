---
name: diligence-issue-extraction
description: >
  Read VDR documents and extract issues per house categories and materiality
  thresholds, producing findings in house memo format under English / UK law.
  Use when user says "review the data room", "extract issues from [folder]",
  "diligence review", "what's in the VDR", or points at VDR documents.
argument-hint: "[VDR folder path or category name]"
---

# /diligence-issue-extraction

1. Load `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` + `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/deal-context.md`.
2. Use the workflow below.
3. Check `ai-tool-handoff` — if category is bulk and tool is configured, hand off first.
4. Read docs, apply materiality filter, extract per category.
5. Findings in house memo format. Hand off consents to closing checklist.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The VDR has 2,000 documents. Somewhere in there are the 30 that matter for the deal. This skill reads documents against the diligence categories and materiality thresholds from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`, extracts issues under UK law, and writes them in house memo format.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → Diligence structure (categories, materiality thresholds)
- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → Issues memo format (how findings are stated)
- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/deal-context.md` → deal-specific thresholds, VDR location, whether deal involves public company / Panel / CMA

If deal-context.md doesn't exist, ask which deal this is for.

## Workflow

### Step 1: Inventory the VDR

If VDR MCP (Box/Datasite/iManage) is connected, pull the index. Map VDR folders to diligence request list categories. Note gaps — request list categories with no corresponding VDR content.

```markdown
## VDR Inventory: [Deal code]

| Request category | VDR folder | Docs | Status |
|---|---|---|---|
| Corporate & Organisational | /01-Corporate | 45 | Reviewed |
| Material Contracts | /02-Contracts | 312 | In progress |
| IP | /03-IP | 89 | Not started |
| [etc.] | | | |

**Gaps:** [Request categories with no VDR content — follow-up request needed]
```

### Step 2: Apply materiality filter

Per `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` / deal-context thresholds. Don't review everything if the threshold says contracts >£X.

For contracts specifically: sort by stated value (if in filename/metadata) or by counterparty significance. Review top-down until you hit the threshold or the category is exhausted.

### Step 3: Extract issues

For each document read, check against the standard diligence concerns for its category under UK law:

**Material contracts — standard extraction set:**
- Change of control provision (triggered by this deal? consent required under the contract?)
- Anti-assignment restriction (can the contract move to buyer / surviving entity?)
- Exclusivity / non-compete (restricts buyer's business post-closing?)
- MFN / most-favoured nation (pricing constraints)
- Termination rights (can counterparty terminate because of the deal?)
- Unusual indemnities or liability exposure
- English law / Scots law governing law considerations

**Corporate & organisational — standard extraction set:**
- CA2006 compliance: share register, register of members accurate? Cap table in order?
- Board consent requirements for the transaction (CA2006 s.190 — substantial property transactions; s.197–214 — loans to directors; s.177/s.182 — conflicts of interest disclosures)
- Shareholders' agreement restrictions (drag-along, tag-along, pre-emption rights under CA2006 s.561 or bespoke articles)
- Subsidiary structure and intercompany arrangements
- PSC register — accurate and filed at Companies House?
- Companies House filing compliance — any late filings, struck-off risk?
- Articles of Association — any unusual provisions restricting the transaction?

**IP — standard extraction set:**
- Ownership chain (CA2006-compliant assignments from founders/employees in place?)
- Open source in the product (copyleft risk under FOSS licences)
- Key IP licensed vs. owned; IP licence consent to assignment
- Pending or threatened IP litigation (UKIPO / EPO / High Court IP)

**Employment — standard extraction set:**
- TUPE implications (Transfer of Undertakings (Protection of Employment) Regulations 2006) — does the deal trigger TUPE? If asset purchase: almost certainly yes. If share purchase: no automatic TUPE (business transfers with the shares), but sub-acquisitions may trigger TUPE.
- Change-of-control severance triggers (golden parachutes / enhanced severance)
- Key employee retention risk; restrictive covenant enforceability under English law
- Pending employment tribunal claims
- Worker classification risk (employees / workers / self-employed — IR35)
- Collective agreements / trade union recognition

**Litigation — standard extraction set:**
- Pending matters and reserves
- Threatened claims
- Regulatory inquiries (FCA, CMA, ICO, sector regulators)
- Pattern litigation

**Regulatory — UK-specific extraction set:**
- FCA / PRA authorisation: does the target hold any regulated permissions (FSMA 2000)? Does the deal require FCA Part XII change of control approval?
- CMA merger control: does the deal meet the Enterprise Act 2002 merger thresholds (share of supply test or turnover test)? Note: mandatory pre-notification NOT required in UK but CMA can investigate post-completion
- Sector-specific licences (Ofgem, Ofwat, Ofcom, CQC, etc.)
- Data protection: UK GDPR / Data Protection Act 2018 — data processor agreements, international transfer mechanisms, ICO registration
- Environmental permits and licences

### Step 4: State each finding

> **Source attribution.** Where a finding references a statute, regulation, case, or regulator action, tag the citation with where it came from: `[uk-legal MCP]` for citations retrieved from the uk-legal MCP; `[uk-due-diligence]` for Companies House / Gazette data; `[govuk MCP]` for GOV.UK guidance; `[legislation.gov.uk]` for statute text retrieved from the official source; `[BAILII]` for case law retrieved from BAILII; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the VDR, deal-team memos, or outside-solicitors feedback. Document-source citations (VDR path, Bates, filename) retain their native reference. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.
>
> **When disagreeing with a user's cited statute, quote the text or decline to characterise it.** If the user (or a deal-team note, or a sell-side disclosure) cites a statute for a proposition you don't think is correct, and you don't have the statute text available from a connected research tool or the VDR, do not invent a description of what the statute says. Say instead: "That section doesn't match what I'd expect a [TUPE / CA2006 s.175 / CMA threshold] requirement to say — I'd need to pull the actual text to tell you what it actually covers. `[statute unretrieved — verify]`" Then either (a) retrieve the text via the uk-legal MCP or legislation.gov.uk and quote it, (b) ask the user to paste the text, or (c) flag for outside solicitors.
>
> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a legal basis the finding needs, report what was found and stop.

Per the finding template in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If the seed memo used this:

```
Issue #N: [Title]
Category: [request list category]
Severity: [level per house scheme]
Documents: [VDR path + doc name]
Finding: [what the document says and why it matters under UK law]
Recommendation: [price adjustment / indemnity / consent required / warranty / walk]
```

...then use exactly that. If the seed memo was bullets, write bullets.

**Severity calibration** (if house scheme is R/Y/G):
- 🔴 **Red:** Affects deal value or structure. Change of control requiring major customer consent. Undisclosed material litigation. IP ownership gap. TUPE exposure not accounted for. FCA authorisation issue. CMA risk.
- 🟡 **Yellow:** Needs attention, solvable. Consent required but likely obtainable. Open source requiring remediation. Employment classification risk. Companies House compliance gap.
- 🟢 **Green:** Noted for file. Consistent with warranties. No action needed beyond the warranty.

**TUPE note.** In an asset purchase, TUPE is almost certain to apply if employees are engaged in the acquired business. Flag clearly: "This is an asset purchase — TUPE (Transfer of Undertakings (Protection of Employment) Regulations 2006) will almost certainly apply to employees assigned to the acquired business. The seller must inform and, if measures are proposed, consult affected employees. Failure to do so gives rise to a protective award (up to 13 weeks' pay). The buyer inherits existing employment contracts, liabilities, and collective agreements. `[model knowledge — verify current TUPE position]`."

In a share purchase: "This is a share purchase — TUPE does not apply to the acquisition of shares in a company (the employer entity does not change). However, TUPE may apply to any sub-acquisitions, hive-out structures, or post-completion restructurings planned as part of the deal. `[verify with employment counsel if restructuring planned]`."

### Step 5: Assemble per category

Group findings by request list category. Within category, sort by severity.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This output is derived from VDR materials that are confidential and subject to legal professional privilege. It inherits the source's privilege and confidentiality status — distribution beyond the privilege circle can waive LPP. In England & Wales, litigation privilege requires litigation to be in reasonable contemplation. Store with the matter's privileged files and make distribution decisions deliberately.

# Diligence Issues: [Deal code] — [Category]

**Documents reviewed:** [N] of [M] in category
**Coverage:** [All | >£X threshold | Top N]
**Findings:** [N]🔴 [N]🟡 [N]🟢

---

### Bottom line

[🔴 N blocking · 🟠 N high · 🟡 N medium] — [the one thing the deal team needs to know]

---

[Each finding in house format]

---

## Gaps

- [Request list item with no responsive document]
- [Document referenced but not in VDR]
```

## Handoffs

- **To ai-tool-handoff:** If Luminance/Kira is in use per `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`, hand bulk contract review there. This skill handles the nuanced documents (side letters, amendments, anything the AI tool struggles with).
- **To deal-team-summary:** Aggregated findings feed the deal team brief.
- **To material-contract-schedule:** Contract-level extractions feed the disclosure schedule.
- **To closing-checklist:** Any finding that implies a discrete pre-closing action becomes a checklist item. The handoff covers:
  - **Conditions precedent / regulatory approvals** — CMA Phase 1/2 clearance (Enterprise Act 2002), FCA Part XII change of control (FSMA 2000), sector-specific regulatory approvals.
  - **Shareholder vote / other closing corporate action** — CA2006 s.190 shareholder approval for substantial property transactions; any special resolution required.
  - **Third-party consents** — change-of-control, anti-assignment consents; Panel consent conditions.
  - **Releases, terminations, or pay-offs** — employment releases tied to change-of-control, payoff letters, charge releases.
  - **TUPE obligations** — information and consultation obligations to be discharged before or after completion.
  Every finding with a pre-closing action tag should reach closing-checklist, not just the ones labelled "consent."

**Successor liability note.** Under English law, asset purchases do not carry automatic successor liability as broadly as in some US states, BUT: (a) TUPE transfers employment liabilities; (b) product liability and tort claims can follow the business if the buyer continues the business under the same trade name; (c) environmental liabilities may follow the site; (d) certain statutory liabilities (e.g., under the Environmental Protection Act 1990) attach to the occupier/owner of a site, not the predecessor company. Flag these specifically — don't assume "asset deal = clean."

## Batch processing

For large categories (300 contracts), process in batches. After each batch, update the running issues list and flag anything 🔴 immediately — don't wait for the full category to surface a deal-affecting issue.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

If the extraction surfaced more than ~10 issues, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by severity (🔴 / 🟠 / 🟡 / 🟢), counts by house category, and a sortable grid of issues with materiality, category, and VDR source.

## What this skill does not do

- It doesn't make the materiality call on close cases. It applies the threshold; a human decides the borderline.
- It doesn't negotiate warranties and indemnities. It produces the findings that inform them.
- It doesn't replace bulk AI review. For high-volume clause extraction, hand off to Luminance/Kira per `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. This skill is for the judgment layer.
- It doesn't determine whether CMA merger control notification is required — that analysis (Enterprise Act 2002 thresholds + share of supply test) requires outside solicitors' input and is flagged, not decided.
