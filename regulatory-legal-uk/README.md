# Regulatory Counsel Plugin — UK

Watches UK regulatory feeds, diffs new rules and statutory instruments against your policy library, surfaces compliance gaps. Learns your materiality threshold so it doesn't alert on every regulator's blog post. Wired for legislation.gov.uk, GOV.UK consultations, the FCA Handbook, ICO enforcement, CMA decisions, Ofcom statements, and the full range of UK sector regulators.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A lawyer reviews, verifies, and decides. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

**FCA rules have force of law.** Gaps in FCA Handbook compliance are enforcement risks, not just policy gaps. This plugin treats FCA/PRA findings as regulatory obligations, not advisory guidance.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Compliance / regulatory counsel** | Watchlist maintenance, gap triage, policy update coordination |
| **Privacy / DPO counsel** | Filtered alerts for UK GDPR, ICO enforcement, Data Protection Act |
| **Financial services counsel** | FCA Handbook diffs, PRA supervisory statement tracking, Dear CEO letter monitoring |
| **GC / CLO** | Escalation recipient for material gaps with deadlines |

## First run: cold-start

Asks which UK regulators you watch, connects your policy document folder, learns what "material" means to you. Builds a watchlist and indexes your policy library.

```
/regulatory-legal-uk:cold-start-interview
```

## Skills

| Skill | Does |
|---|---|
| `/regulatory-legal-uk:cold-start-interview` | Cold-start: watchlist + policy index + materiality threshold |
| `/regulatory-legal-uk:reg-feed-watcher` | Check UK regulatory feeds now, report what's new |
| `/regulatory-legal-uk:policy-diff [reg]` | Diff a specific regulatory change against policy library |
| `/regulatory-legal-uk:gaps` | Open gaps tracker — what's been flagged and not yet closed |
| `/regulatory-legal-uk:comments` | Review open consultation response periods, log decisions, track deadlines |
| `/regulatory-legal-uk:policy-redraft` | Proposed marked-up policy redraft that closes a gap — a first draft for internal review, not a direct edit to source documents |
| `/regulatory-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |
| **gap-surfacer** *(reference)* | Shared gap- and consultation-tracker framework loaded by `/gaps` and `/comments` |
| `/regulatory-legal-uk:customize` | Adjust watched regulators, policy library, materiality threshold without re-running the full interview |

## Interactive skills vs. scheduled agents

The skills above run when you invoke them — for when you're working a matter. The agents below run on a schedule — for what moves while you're not looking:

| Agent | What it watches | Default cadence |
|---|---|---|
| **reg-change-monitor** | UK regulatory feeds — filters by the materiality threshold learned at cold-start and posts a digest that's signal, not noise | Weekly (daily if the regulatory environment is active) |

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors in this plugin (uk-legal, govuk, uk-due-diligence) are the difference between a verified citation and a citation you have to check. A citation retrieved through a connected research tool is tagged with its source and can be traced back. A citation from the model's knowledge or from web search is tagged `[verify]` or `[model knowledge — verify]` and should be checked against a primary source before anyone relies on it. The plugin tiers its citations so your verification time goes where it matters.

Citation format follows OSCOLA (Oxford University Standard for the Citation of Legal Authorities).

## UK regulatory coverage

**Primary feed sources configured by this plugin:**

| Regulator | Covers | Feed type |
|---|---|---|
| legislation.gov.uk | Acts of Parliament, Statutory Instruments, retained EU law | JSON API |
| GOV.UK publications | Consultations, policy papers, guidance, ministerial statements | JSON API / RSS |
| FCA | Handbook updates, CPs, PSs, FGs, supervisory statements, Dear CEO/CFO letters | RSS + email |
| PRA | Supervisory statements, consultation papers, policy statements | RSS + email |
| Bank of England | FPC statements, MPC decisions, macroprudential rules | RSS |
| CMA | Market investigations, merger decisions, enforcement, guidance | RSS |
| ICO | Enforcement decisions, codes of practice, guidance updates | RSS |
| Ofcom | Consultation papers, enforcement decisions, Online Safety Act guidance | RSS |
| HSE | Consultations, ACOPs, enforcement bulletins | RSS |
| MHRA | Guidance updates, device approvals, public health letters | RSS + email |
| HMRC | Technical guidance, VAT notices, consultation papers | RSS |
| DSIT | AI/tech policy consultations | GOV.UK feed |
| HM Treasury | Financial regulation consultations, FSMA/FMI updates | GOV.UK feed |
| CAT | Judgments | uk-legal MCP |
| UK Parliament | Bills, committee reports, written ministerial statements | uk-legal MCP |
| FRC | Accounting standards, audit reforms | RSS + email |
| Gambling Commission | LCCP updates | RSS |
| OPSS | Product safety updates | GOV.UK feed |

## UK parliamentary consultation process

UK consultations follow the Cabinet Office Code of Practice on Consultation (typically 12 weeks). This plugin tracks:

- GOV.UK consultation closing dates (not US-style "notice-and-comment" — the UK term is "consultation response" or "response to consultation")
- Parliamentary Select Committee inquiry evidence submission deadlines
- Written ministerial statements that change policy without formal consultation
- Statutory instruments: affirmative vs. negative procedure timelines
- Primary legislation: Second Reading, Committee stage, Report stage, Third Reading

## Integrations

Ships with UK legal research connectors in `.mcp.json`:

- **uk-legal** — legislation.gov.uk, TNA Find Case Law, Hansard, Bills, HMRC guidance, OSCOLA citation parsing
- **govuk** — GOV.UK content, consultations, guidance, organisations
- **uk-due-diligence** — Companies House, Charity Commission, HMLR, The Gazette, HMRC VAT

Add Slack and Google Drive by extending `.mcp.json` when partner URLs are available. Direct regulator RSS/email as fallback for all feeds.

## Prerequisites

Owner notifications (gap assignments, due-date reminders, consultation alerts) require a Slack MCP server in your environment. Without one, the gap tracker and consultation tracker still work — notifications just won't post, and the skills will flag ungated items in the status report instead.

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `reg-change-monitor` agent watches the UK regulatory feeds and flags changes against your policy library. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Notes

- Materiality filtering is the value. Everything is "technically a regulatory development" — the plugin learns what actually matters here.
- Policy diff compares against indexed policies. If the policy library isn't connected, diffs run against what you paste.
- Post-Brexit divergence tracking: this plugin flags where UK rules diverge from the evolving EU position on retained EU law. Pair with the privacy-legal-uk plugin for deep GDPR/UK GDPR dives.
- This is the UK equivalent of the US regulatory-legal plugin. It is not a translation — it uses UK parliamentary process, UK regulator names, OSCOLA citations, and UK Handbook-first analysis throughout.

## Configuration

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` and survives plugin updates — you only run setup once.
