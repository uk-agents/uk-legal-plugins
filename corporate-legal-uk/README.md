# Corporate Counsel Plugin (UK)

In-house corporate counsel workflows across four practice areas: M&A deals under English law, board and company secretary, public company governance (FCA/AIM), and entity management under the Companies Act 2006. Activate only the modules that apply to your role. The cold-start interview is modular — it asks targeted questions per active area and writes only the relevant sections to your practice profile.

**Every output is a draft for solicitor/barrister review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A qualified lawyer reviews, verifies, and decides. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Legal professional privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Active modules |
|---|---|
| **In-house M&A counsel** | M&A |
| **Company secretary / assistant secretary** | Board & Secretary |
| **GC at a listed company** | M&A + Public Company + Board & Secretary |
| **GC at a private company** | M&A + Board & Secretary + Entity Management |
| **Legal ops / solo GC** | Whichever apply — mix and match |

## First run

```
/corporate-legal-uk:cold-start-interview
```

Walks through module selection, then a short targeted interview for each active area. Writes a modular `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` with only the relevant sections. Your configuration is stored at that path and survives plugin updates.

Per-deal setup (M&A module only):

```
/corporate-legal-uk:cold-start-interview --new-deal
```

## Commands

| Command | Does |
|---|---|
| `/corporate-legal-uk:cold-start-interview` | Modular cold-start, or `--new-deal` / `--module [m&a \| board \| public \| entities]` |
| `/corporate-legal-uk:diligence-issue-extraction [folder]` | Read VDR docs, extract issues in house format under English law |
| `/corporate-legal-uk:tabular-review` | Tabular review — one row per document, one column per data point, every cell cited to source, Excel output |
| `/corporate-legal-uk:material-contract-schedule` | Material contracts disclosure schedule from diligence findings (per SPA/APA definition) |
| `/corporate-legal-uk:closing-checklist` | Closing checklist — what's blocking, critical path; covers CMA clearance, FCA change of control, Panel consents |
| `/corporate-legal-uk:written-consent` | Written resolutions under CA2006 — precedent-matched draft + signatory tracker |
| `/corporate-legal-uk:entity-compliance` | Entity compliance tracker — init, report, update, audit, export; Companies House filings, PSC register, Confirmation Statements |
| `/corporate-legal-uk:integration-management` | Post-closing integration workplan, consents tracker, contract assignment, status reports |
| `/corporate-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Prerequisites

Several features reference Slack, Google Drive, SharePoint, Box, Datasite, or iManage integrations. These require MCP servers configured in your environment — they are **not bundled with the plugin**. Without them, the plugin falls back to file output (drafts written locally rather than posted to a channel, tracker files written to disk rather than read from a connected repository).

Configure MCP servers in `.mcp.json` at the repo or user level. Skills and agents will detect what's available at runtime and adjust behaviour.

## Skills

| Skill | Module | Purpose |
|---|---|---|
| **cold-start-interview** | All | Modular interview — activates only relevant sections |
| **diligence-issue-extraction** | M&A | VDR docs → issues in house format, by category; UK law (CA2006, FSMA, CMA) |
| **tabular-review** | M&A | Review a document set against a typed column schema; cited cells; `.xlsx` / `.csv` / markdown output; feeds material-contract-schedule |
| **deal-team-summary** | M&A | Tiered briefs: exec / deal lead / working team |
| **material-contract-schedule** | M&A | Disclosure schedule per SPA/APA Material Contract definition |
| **closing-checklist** | M&A | Self-updating: ingests from diligence and schedule builds; CMA / FCA / Panel conditions precedent |
| **ai-tool-handoff** | M&A | Luminance/Kira integration — bulk extraction + QA layer |
| **board-minutes** | Board & Secretary | Calendar-detected meetings → draft minutes in house format; CA2006 quorum and resolution rules |
| **written-consent** | Board & Secretary | Written resolutions under CA2006 with precedent search from resolutions repository; scope warning for major one-off actions |
| **entity-compliance** | Entity Management | Compliance calendar tracker (YAML); Companies House filing deadlines by entity and nation; health audit; Confirmation Statement and accounts tracking; CSV export |
| **integration-management** | M&A | Post-closing integration tracker; phased workplan (Day 1/30/90/180); Required Consents tracker with SPA deadlines; contract assignment at scale (repository or manual list); weekly status reports |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

*Public Company skills (FCA disclosure, MAR notifications, PDMR/PCA tracking) coming in next release.*

## Interactive commands vs. scheduled agents

The commands above run when you invoke them — for when you're working a matter. The agents below run on a schedule — for what moves while you're not looking:

| Agent | Module | What it watches | Default cadence |
|---|---|---|---|
| **dataroom-watcher** | M&A | VDR for new document uploads; flags uploads that match high-priority categories; runs closing checklist status | Weekly |

## Integrations

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[model knowledge — verify]` and the reviewer note above each deliverable records that sources weren't verified. Skills work either way; a research tool just shifts verification work off your plate.

Ships with:

- **uk-legal MCP** — UK case law (TNA Find Case Law / BAILII), legislation.gov.uk, Hansard, HMRC guidance
- **uk-due-diligence MCP** — Companies House, Gazette (insolvency), HMLR Land Registry, HMRC VAT register
- **govuk MCP** — GOV.UK content and guidance
- **Slack** — search messages, read channels, find discussions (general bucket)
- **Google Drive** — search, read, and fetch documents (general bucket)
- **Box** — data room and document management

Datasite and other VDR connectors can be added to `.mcp.json` when partner URLs are available.

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## M&A notes

- Issue extraction applies materiality thresholds — does not read every document if threshold says top N by value.
- Buy-side and sell-side are both supported. Practice profile captures which side applies to this deal; skills adjust posture accordingly.
- Locked-box and completion accounts mechanics are both supported — the skill reads which the SPA uses.
- AI tool handoff (Luminance/Kira) is optional. If `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` says no tool, all extraction runs through the direct skill.
- Closing checklist initialises from the SPA/APA, then self-updates as diligence surfaces consents required. Includes CMA Phase 1/2 clearance items, FCA Part XII change of control approvals, and Panel consent conditions where applicable.
- Scotland: where a target or acquired entity is a Scottish company or holds Scottish property, flag the relevant CA2006 and Scottish law divergences (charge registration at Registers of Scotland, Scots property law) and recommend Scottish law firm involvement.

## Entity management notes

- Confirmation Statement (CS01) is the annual filing at Companies House — distinct from the annual accounts.
- PSC register: mandatory for all UK companies; review and update whenever a registrable change occurs. Threshold: 25%+ shares / voting rights / right to appoint majority of directors / significant influence or control.
- Charge registration: 21-day window from creation (CA2006 s.870); unregistered charges void against insolvency officeholders and creditors. Scottish charges: also register at Scottish Registers if over Scottish property.
- Dormant company accounts: small dormant subsidiaries may file dormant accounts (CA2006 s.480); check eligibility before triggering full statutory audit.
