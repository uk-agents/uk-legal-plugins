# Commercial Counsel Plugin (UK)

In-house commercial contracts workflows for UK-based teams: vendor agreement review, NDA triage, SaaS subscription review, renewal tracking, escalation routing, and business-stakeholder summaries. Built around English contract law (with jurisdiction notes for Scotland and Northern Ireland) and a team practice profile that gets written by a cold-start interview — the plugin learns *your* playbook, not a generic one.

**Every output is a draft for solicitor or barrister review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A legal professional reviews, verifies, and decides. Citations are tagged by source (uk-legal MCP, BAILII, legislation.gov.uk, govuk MCP, or model knowledge) so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Commercial solicitor / in-house counsel** | Vendor agreement review, escalation routing, stakeholder summaries |
| **Contracts manager / paralegal** | NDA triage, renewal tracking, first-pass review |
| **Procurement** | Renewal awareness, stakeholder summaries as recipients |
| **Sales / BD** | NDA triage self-serve before pinging legal |

## UK legal framework

This plugin applies English contract law as the default, with jurisdiction notes where Scots law or Northern Ireland law materially diverge:

- **Contract formation:** Offer, acceptance, consideration, certainty of terms, intention to create legal relations — English common law. Scotland: no consideration requirement; a gratuitous promise can bind.
- **Sale of goods / services:** Sale of Goods Act 1979; Supply of Goods and Services Act 1982; Consumer Rights Act 2015 (B2C); implied terms of satisfactory quality and fitness for purpose.
- **Unfair terms:** Unfair Contract Terms Act 1977 (UCTA) — B2B limitation/exclusion clauses must satisfy the reasonableness test. Consumer Rights Act 2015 — B2C unfair terms are unenforceable. Residual controls in Schedule 2 of the CRA and common law unconscionability.
- **SaaS / tech contracts:** Governed by English contract law; UK GDPR / DPA 2018 data processing terms; standard SaaS clauses.
- **NDAs / confidentiality:** Common law of confidence (Coco v AN Clark Engineers Ltd [1969]); springboard doctrine; no specific statute.
- **Governing law:** Choice of English law (or Scots law); Rome I Regulation retained as UK law; post-Brexit jurisdiction — exclusive English court clauses valid but check enforcement in EU.
- **Competition:** Competition Act 1998; Chapter I prohibition (anti-competitive agreements); Chapter II prohibition (abuse of dominant position); CMA enforcement; Enterprise Act 2002.
- **Payment:** Late Payment of Commercial Debts (Interest) Act 1998; Prompt Payment Code.
- **IP in contracts:** Copyright Designs and Patents Act 1988; assignment vs. licence distinction; background/foreground IP split.
- **Force majeure:** No statutory provision in English law — common law frustration under Law Reform (Frustrated Contracts) Act 1943; COVID caselaw.
- **Dispute resolution:** Arbitration Act 1996; LCIA/ICC/UNCITRAL; English courts (costs-shifting — loser pays); without-prejudice privilege; Part 36 offers.

## First run: the cold-start interview

On first use, the plugin interviews you — ten minutes, conversational — to learn how your team actually works under UK commercial law. It asks about your playbook positions, your escalation rules, and the thing that makes you groan when it hits your desk.

It writes what it learns to `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` — a plain-English document about your team that every other skill reads before doing anything. You edit the document, not a config file.

```
/commercial-legal-uk:cold-start-interview
```

**Playbook side.** Early in setup, you'll be asked whether to build a **sales-side** playbook (you sell your product/service; you're the vendor; usually your paper), a **purchasing-side** playbook (you buy from vendors; you're the customer; usually their paper), or both.

## Commands

| Command | Does |
|---|---|
| `/commercial-legal-uk:cold-start-interview` | Run (or re-run) the cold-start interview |
| `/commercial-legal-uk:review [file]` | Review a vendor agreement, NDA, or SaaS subscription against your playbook |
| `/commercial-legal-uk:renewal-tracker` | What's renewing in the next 90 days and when the cancel-by deadlines are |
| `/commercial-legal-uk:escalation-flagger` | Route an issue to the right approver and draft the ask |
| `/commercial-legal-uk:amendment-history [file(s)]` | Trace how a contract has changed across its base agreement and all amendments |
| `/commercial-legal-uk:review-proposals` | Step through pending playbook update proposals from the monitor agent |
| `/commercial-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | First-run interview that writes `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` |
| **vendor-agreement-review** | Full playbook-vs-contract deviation analysis with redlines under English contract law |
| **nda-review** | Fast GREEN/YELLOW/RED triage applying English law of confidence and UCTA |
| **saas-msa-review** | Subscription-specific overlay: auto-renewal, price escalation, data exit, UK GDPR DPA, SLAs |
| **renewal-tracker** | Register of cancel-by deadlines, surfaces what's coming |
| **escalation-flagger** | Matches issues to the escalation matrix (including CMA/FCA/ICO referrals), drafts the approver ask |
| **stakeholder-summary** | Two-paragraph business translation of a legal review |
| **amendment-history** | Summarizes changes across a base agreement and its amendments, or traces a specific provision to its current controlling language |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

## Interactive commands vs. scheduled agents

The commands above run when you invoke them — for when you're working a matter. The agents below run on a schedule — for what moves while you're not looking:

| Agent | What it watches | Default cadence |
|---|---|---|
| **renewal-watcher** | Renewal register — posts what's coming up in the next 90 days, with red-flag escalation for cancel-by windows in 0–13 days | Weekly (Monday) |
| **deal-debrief** | Recently signed agreements for playbook deviations; prompts the solicitor to log context while memory is fresh | Weekly (Monday) |
| **playbook-monitor** | Deviation log — proposes playbook updates when a clause has been overridden 5+ times in a rolling 12-month window | Data-triggered (after each deal-debrief) |

## Integrations

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[model knowledge — verify]` and the reviewer note above each deliverable records that sources weren't verified. Skills work either way; a research tool (uk-legal MCP, BAILII, legislation.gov.uk) just shifts verification work off your plate.

Ships with connectors configured in `.mcp.json`:

- **uk-legal** — UK case law (TNA Find Case Law), legislation, Hansard, HMRC guidance, OSCOLA citations
- **govuk** — GOV.UK content, CMA/FCA/ICO guidance, government organisations
- **uk-due-diligence** — Companies House, HMLR, The Gazette (insolvency notices), HMRC VAT
- **Ironclad** — contract lifecycle management
- **DocuSign** — signature status and envelope tracking
- **Definely** — contract structure: definitions, cross-references, structural diffs
- **Slack** — search messages, read channels (general bucket)
- **Google Drive** — search, read, and fetch documents (general bucket)

## Quick start

### 1. Get interviewed

```
/commercial-legal-uk:cold-start-interview
```

Ten minutes. Have 5-10 recent signed agreements ready to share.

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` and survives plugin updates.

### 2. Review a contract

```
/commercial-legal-uk:review vendor-msa.pdf
```

Output: deviation-by-deviation memo against your playbook under English contract law, with specific redline language and named approver.

### 3. See what's renewing

```
/commercial-legal-uk:renewal-tracker
```

Output: everything with a cancel-by deadline in the next 90 days, grouped by urgency. Business-day roll-back applied for England & Wales bank holidays.

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `playbook-monitor` agent proposes updates when your practice diverges from your playbook. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Jurisdiction notes

- **England & Wales:** Full support. Default jurisdiction.
- **Scotland:** Scots law notes surfaced where relevant (no consideration requirement, offer/acceptance differences, Scots-specific statutes). For matters governed by Scots law, recommend a Scotland-qualified solicitor for final sign-off.
- **Northern Ireland:** NI law notes surfaced where legislation extent differs from E&W. For matters governed by NI law, recommend an NI-qualified solicitor.
- **Cross-border / EU:** Post-Brexit Rome I (retained) governs choice of law. English court judgments not automatically recognised in EU — note enforcement risks.

## File structure

```
commercial-legal-uk/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Your team practice profile — written by cold-start, edited by you
├── README.md
├── agents/
│   ├── renewal-watcher.md
│   ├── deal-debrief.md
│   └── playbook-monitor.md
├── skills/
│   ├── cold-start-interview/
│   ├── review/
│   ├── review-proposals/
│   ├── vendor-agreement-review/
│   ├── nda-review/
│   ├── saas-msa-review/
│   ├── renewal-tracker/
│   │   └── references/renewal-register.yaml
│   ├── escalation-flagger/
│   ├── amendment-history/
│   ├── matter-workspace/
│   ├── stakeholder-summary/
│   └── customize/
└── hooks/hooks.json
```

## Notes

- The plugin defaults to **English law** (England & Wales). Where governing law is Scots law or NI law, it notes the differences; for finalisation, recommend a jurisdiction-qualified solicitor.
- NDA triage is built for self-serve by non-lawyers. GREEN means "route to signature." It does not negotiate.
- Renewal tracking only knows about contracts that were reviewed through this plugin or bulk-loaded from the CLM. Contracts signed before you installed this need a one-time scan.
- UK GDPR / DPA 2018 data processing terms are checked in every vendor agreement and SaaS review — not just flagged when a DPA is attached.
