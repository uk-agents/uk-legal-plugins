# Product Counsel Plugin (UK)

Product legal workflows for UK-based companies: launch review, marketing claims review under ASA / CAP Code standards, feature risk assessment, and fast "is this a problem?" triage. Built around a risk calibration learned from your actual launch review history — what blocks at *your* company, not generically — and calibrated to UK consumer protection law, CMA enforcement, ICO data regulation, FCA financial promotions, and the Online Safety Act.

**Every output is a draft for legal professional review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A solicitor or barrister reviews, verifies, and decides. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Product counsel / in-house solicitor** | Launch review, feature risk assessment, calibration maintenance |
| **Product managers** | "Is this a problem?" triage self-serve |
| **Marketing** | Claims review before ship (ASA / CAP Code substantiation check) |
| **GC / Legal leadership** | Feature risk assessments for escalated items |

## First run: the cold-start interview

Connects to your launch tracker (Jira/Linear), reads ten of your past launch reviews, learns what you actually block vs. what you wave through. Builds a risk calibration table that every other skill reads from.

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` and survives plugin updates.

```
/product-legal-uk:cold-start-interview
```

## Commands

| Command | Does |
|---|---|
| `/product-legal-uk:cold-start-interview` | Cold-start interview |
| `/product-legal-uk:launch-review [PRD or ticket]` | Full launch review against your framework |
| `/product-legal-uk:marketing-claims-review [copy]` | Marketing claims review (ASA / CAP Code) |
| `/product-legal-uk:is-this-a-problem [question]` | Fast "is this a problem?" answer |
| `/product-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Writes ~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md from interview + past launch reviews |
| **launch-review** | Category-by-category review, calibrated to your company and UK law |
| **marketing-claims-review** | Claims taxonomy: puffery/factual/comparative/implied/absolute — against ASA CAP/BCAP Code standards |
| **feature-risk-assessment** | Deep dive on one issue when launch review isn't enough |
| **is-this-a-problem** | Same-minute triage for the quick Slack question |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

## Interactive commands vs. scheduled agents

The commands above run when you invoke them — for when you're working a matter. The agents below run on a schedule — for what moves while you're not looking:

| Agent | What it watches | Default cadence |
|---|---|---|
| **launch-watcher** | Launch tracker (Jira/Linear) for upcoming launches that likely need legal review; filters tickets with launch dates in the next 30 days per the calibration table | Daily |

## Integrations

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. Skills work either way; a research tool just shifts verification work off your plate.

Ships with connectors configured in `.mcp.json`:

- **uk-legal** — legislation, case law, Hansard, HMRC guidance, Bills and committee evidence
- **govuk** — GOV.UK content, regulatory guidance, postcode resolution
- **uk-due-diligence** — Companies House, Charity Commission, Land Registry, The Gazette, HMRC VAT

With a tracker connected: cold-start pulls launch history, launch-review pulls ticket context, launch-watcher agent monitors the calendar.

## Key UK regulatory context

**Consumer and product regulators:**
- **CMA** (Competition and Markets Authority) — competition and consumer protection; primary enforcement body for unfair commercial practices, subscription traps (DMCC Act 2024), fake reviews, drip pricing
- **ASA** (Advertising Standards Authority) + **CAP/BCAP Codes** — advertising and marketing claims; primary UK route for substantiation challenges; ASA challenge is cheaper and faster than litigation
- **ICO** (Information Commissioner's Office) — data protection; UK GDPR + DPA 2018; products handling personal data
- **FCA** (Financial Conduct Authority) — financial products and promotions; FSMA 2000 s 21 approval required before communicating a financial promotion
- **MHRA** (Medicines and Healthcare products Regulatory Agency) — medical devices, medicines, diagnostics
- **OPSS** (Office for Product Safety and Standards) — general product safety
- **Ofcom** — Online Safety Act 2023; platforms with user-generated content

**Key legislation:**
- Consumer Rights Act 2015 (CRA 2015) `[CRA-2015-S]` — quality, fitness for purpose, digital content
- Consumer Protection Act 1987 (CPA 1987) `[CPA-1987-S]` — product liability (strict)
- Consumer Protection from Unfair Trading Regulations 2008 (CPR 2008) `[CPR-2008-REG]` — misleading/aggressive commercial practices
- Digital Markets, Competition and Consumers Act 2024 (DMCC Act) `[DMCC-ACT-2024]` — new CMA enforcement powers; subscription traps, fake reviews, drip pricing
- UK GDPR + DPA 2018 `[UK-GDPR-ART]` — personal data in products; DPIA obligations
- Online Safety Act 2023 `[OSA-2023-S]` — platforms; illegal content; content harmful to children
- FSMA 2000 s 21 `[FSMA-2000-S]` — financial promotions must be approved by FCA-authorised person

## Quick start

```
/product-legal-uk:cold-start-interview
```

Then:

```
/product-legal-uk:is-this-a-problem "Can we A/B test the pricing page?"
```

→ Same-minute answer calibrated to your risk table.

```
/product-legal-uk:launch-review PROJ-1234
```

→ Full review, category-by-category, with action items.

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Notes

- The calibration table is the whole thing. If it's wrong, every review is wrong. Re-run setup when your risk posture changes (new regulator attention, new consent commitment, new GC).
- `is-this-a-problem` is designed for PMs to self-serve. It answers fast and routes to a real review when it should.
- Feature risk assessment is for the 10% of launches that need depth. Most don't — don't generate paperwork.
- Financial promotions under FSMA s 21 are always a blocker until FCA-authorised approval is confirmed. The plugin flags this early.

## Prerequisites

Some features reference external integrations (document management, launch trackers). These are not bundled — if you have an MCP server for one of these in your environment, the relevant features will use it. Without one, the plugin falls back to file upload and manual workflows. Run `/product-legal-uk:cold-start-interview --check-integrations` to see what's available in your environment.

## Configuration

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md` and survives plugin updates — you only run setup once.
