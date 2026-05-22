# UK Legal Plugins

11 legal plugins built for UK jurisdiction — English & Welsh, Scottish, and Northern Irish law. Reviews, drafting, deadline tracking, investigations, diligence, and learning — wired to UK sources (BAILII, TNA Find Case Law, legislation.gov.uk, Companies House, GOV.UK, ICO, FCA, Hansard).

Works in any agent that supports the [Open Plugins spec](https://github.com/anthropics/claude-plugins-official): Claude Code, Claude Cowork, Cursor, GitHub Copilot, and Codex.

> **New here?** Start with [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds. This README is the full reference.

> [!IMPORTANT]
> **Every output from these plugins is a draft for solicitor or barrister review — not legal advice, not a legal conclusion, not a substitute for a regulated lawyer.** The skills are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced (E&W default, Scots/NI divergences flagged), and explicit gates before anything is filed, sent, or relied on. A regulated lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.
>
> **Not affiliated with Anthropic. Not legal advice. SRA / BSB / CILEX regulated users remain responsible for compliance with their regulator's code of conduct.** Where a skill includes a checklist, framework, risk flag, or characterisation of case law or regulatory guidance, that is an aid to the reviewing lawyer's own analysis — not a settled view of UK law.

---

## Plugins

| Plugin | Practice area |
|--------|--------------|
| `employment-legal-uk` | Hires, terminations, IR35 / employment status, statutory leave (SMP/SPL/SAP/PBL), internal investigations, ACAS Code |
| `commercial-legal-uk` | Vendor agreements, NDAs, SaaS subscriptions under English contract law; Scots law divergences noted |
| `corporate-legal-uk` | M&A diligence, CA 2006 compliance, board minutes, Companies House, PSC register, City Code on Takeovers |
| `ip-legal-uk` | Trade marks (TMA 1994), copyright (CDPA 1988), patents (PA 1977 / EPC), designs, trade secrets, UK IPO filings |
| `privacy-legal-uk` | UK GDPR / DPA 2018, DPIA, DSAR (1-month deadline), PECR, ICO gap analysis |
| `product-legal-uk` | Product launches, ASA / CAP Code, CMA, MHRA, Online Safety Act 2023, DMCC Act 2024 |
| `regulatory-legal-uk` | FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HM Treasury, GOV.UK consultation tracking |
| `ai-governance-legal-uk` | AI use-case registry, impact assessments, ICO AI guidance, UK AI policy, EU AI Act exposure, OSA 2023 |
| `litigation-legal-uk` | CPR deadlines, skeleton arguments, claim charts, LPP logs, Letters Before Action, witness summons |
| `legal-clinic-uk` | SRA / BSB-supervised clinics, OSCOLA research, semester handoffs |
| `law-student-uk` | SQE1 / SQE2 and LLB prep, OSCOLA citations, BAILII case briefs, Socratic drilling |

---

## Agents

Each agent is named for the workflow it runs. Start with the ones that match your practice, then tune the underlying skill, the practice profile, and the connectors to how your team works.

| Agent | What it does | Plugin | Command |
|---|---|---|---|
| **Vendor Agreement Reviewer** | Reviews a vendor agreement against your playbook and produces a redline memo | `commercial-legal-uk` | `/commercial-legal-uk:review` |
| **NDA Triager** | GREEN / YELLOW / RED triage of inbound NDAs so only the hard ones reach a lawyer | `commercial-legal-uk` | `/commercial-legal-uk:review` |
| **SaaS / MSA Reviewer** | Reviews a SaaS subscription or MSA against your playbook, with order-form interaction flags | `commercial-legal-uk` | `/commercial-legal-uk:review` |
| **Amendment Tracer** | Traces how a contract has changed across its base and every amendment | `commercial-legal-uk` | `/commercial-legal-uk:amendment-history` |
| **Renewal Tracker** | Scans the contract register for cancel-by and renewal deadlines | `commercial-legal-uk` | `/commercial-legal-uk:renewal-tracker` |
| **Renewal Watcher** | Weekly sweep of upcoming renewals, posted to your channel | `commercial-legal-uk` | scheduled agent |
| **Deal Debrief** | Weekly surface of signed agreements with playbook deviations | `commercial-legal-uk` | scheduled agent |
| **Playbook Monitor** | Proposes playbook updates when a clause has drifted in practice | `commercial-legal-uk` | scheduled agent |
| **Escalation Router** | Routes contract issues to the right approver and drafts the ask | `commercial-legal-uk` | `/commercial-legal-uk:escalation-flagger` |
| **Stakeholder Summary** | Translates a contract review into a business-stakeholder briefing | `commercial-legal-uk` | (used by `/commercial-legal-uk:review`) |
| **Tabular Diligence Review** | Tabular review across a data room with one row per document and every cell cited | `corporate-legal-uk` | `/corporate-legal-uk:tabular-review` |
| **Diligence Issue Extractor** | Extracts issues per house categories and materiality thresholds | `corporate-legal-uk` | `/corporate-legal-uk:diligence-issue-extraction` |
| **Written Resolution Drafter** | Drafts board or shareholder written resolutions in house format (CA 2006 s.288) | `corporate-legal-uk` | `/corporate-legal-uk:written-consent` |
| **Material Contracts Schedule Builder** | Builds the disclosure schedule from diligence findings against the SPA threshold | `corporate-legal-uk` | `/corporate-legal-uk:material-contract-schedule` |
| **Entity Compliance Tracker** | Confirmation statements (CS01), annual accounts (AA), PSC, dormant filings across the group | `corporate-legal-uk` | `/corporate-legal-uk:entity-compliance` |
| **Closing Checklist Driver** | Tracks every condition, consent, document, and filing blocking completion | `corporate-legal-uk` | `/corporate-legal-uk:closing-checklist` |
| **Integration Runbook** | Phased post-completion integration plan with consent tracking and weekly status | `corporate-legal-uk` | `/corporate-legal-uk:integration-management` |
| **Data Room Watcher** | Monitors the VDR for new uploads and posts closing checklist status | `corporate-legal-uk` | scheduled agent |
| **Termination Reviewer** | Runs a proposed dismissal against ERA 1996, EqA 2010, ACAS Code, and protected disclosures (PIDA) | `employment-legal-uk` | `/employment-legal-uk:termination-review` |
| **Hire Reviewer** | Reviews offer letters and restrictive covenants (post-termination restrictions) with right-to-work flags | `employment-legal-uk` | `/employment-legal-uk:hiring-review` |
| **Employment Status Screener** | IR35 / off-payroll / employee vs worker vs self-employed against status case law (Ready Mixed, Autoclenz, Uber/Aslam) | `employment-legal-uk` | `/employment-legal-uk:worker-classification` |
| **Leave Tracker** | Monitors open SMP / SPL / SAP / PBL and long-term sickness with reasonable-adjustments deadlines (EqA 2010) | `employment-legal-uk` | scheduled agent |
| **Leave Logger** | Adds a new statutory leave to the register | `employment-legal-uk` | `/employment-legal-uk:log-leave` |
| **Investigation Lead** | Opens, tracks, adds to, and summarises internal investigation matters (ACAS Code-aligned) | `employment-legal-uk` | `/employment-legal-uk:investigation-open` |
| **Policy Drafter** | Drafts employment policies with Scots and NI variations where law differs | `employment-legal-uk` | `/employment-legal-uk:policy-drafting` |
| **International Expansion Planner** | EOR-vs-entity planning and outside-counsel briefing for a new jurisdiction | `employment-legal-uk` | `/employment-legal-uk:expansion-kickoff` |
| **Pay & Working Time Q&A** | NMW, Working Time Regulations 1998, holiday pay (Harpur Trust), Bear Scotland — quick channel answers | `employment-legal-uk` | `/employment-legal-uk:wage-hour-qa` |
| **Handbook Diff** | Diffs handbook changes and flags nation-supplement impacts | `employment-legal-uk` | (used by other skills) |
| **DSAR Responder** | Walks a DSAR end-to-end and drafts the response within the one-month statutory deadline (UK GDPR Art. 12) | `privacy-legal-uk` | `/privacy-legal-uk:dsar-response` |
| **DPA Reviewer** | Reviews a Data Processing Agreement against your playbook, auto-detects controller vs processor | `privacy-legal-uk` | `/privacy-legal-uk:dpa-review` |
| **DPIA Generator** | Generates a Data Protection Impact Assessment in house format (UK GDPR Art. 35 / DPA 2018) | `privacy-legal-uk` | `/privacy-legal-uk:dpia-generation` |
| **Privacy Triager** | Decides whether a processing activity needs a DPIA or can proceed under ICO guidance | `privacy-legal-uk` | `/privacy-legal-uk:use-case-triage` |
| **Privacy Reg Gap Checker** | Diffs a new or changed regulation against current privacy policy and practice | `privacy-legal-uk` | `/privacy-legal-uk:reg-gap-analysis` |
| **Privacy Policy Monitor** | Sweeps saved DPIAs, DPA reviews, and triage results for drift between policy and practice | `privacy-legal-uk` | `/privacy-legal-uk:policy-monitor` |
| **Launch Reviewer** | Reviews a product launch against your risk calibration, ASA / CAP Code, MHRA, OSA, DMCC | `product-legal-uk` | `/product-legal-uk:launch-review` |
| **Marketing Claims Checker** | Flags copy that needs substantiation, reframing, or cutting (CAP Code + DMCC Act 2024) | `product-legal-uk` | `/product-legal-uk:marketing-claims-review` |
| **"Is this a problem?" Triage** | Fast answer for the quick Slack question — pattern-matches your calibration | `product-legal-uk` | `/product-legal-uk:is-this-a-problem` |
| **Feature Risk Assessment** | Deep-dive risk on a single feature when launch review flags it | `product-legal-uk` | (used by launch review) |
| **Launch Watcher** | Monitors the launch tracker for upcoming launches that need legal eyes | `product-legal-uk` | scheduled agent |
| **Reg Feed Watcher** | Polls FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HM Treasury, GOV.UK and writes the Monday-morning digest | `regulatory-legal-uk` | `/regulatory-legal-uk:reg-feed-watcher` |
| **Policy Diff** | Diffs a specific regulatory change against the indexed policy library | `regulatory-legal-uk` | `/regulatory-legal-uk:policy-diff` |
| **Gap Tracker** | Open gaps tracker — what's flagged and not yet closed | `regulatory-legal-uk` | `/regulatory-legal-uk:gaps` |
| **Policy Redrafter** | Marked-up policy redraft closing a gap — a proposal for the policy owner's review | `regulatory-legal-uk` | `/regulatory-legal-uk:policy-redraft` |
| **Consultation Tracker** | Tracks open HM Treasury / FCA / Ofcom / CMA consultation papers, logs decisions, monitors deadlines | `regulatory-legal-uk` | `/regulatory-legal-uk:comments` |
| **Reg Change Monitor** | Scheduled feed sweep with materiality filter | `regulatory-legal-uk` | scheduled agent |
| **AI Use Case Triager** | Classifies proposed AI use cases against your registry and ICO AI guidance | `ai-governance-legal-uk` | `/ai-governance-legal-uk:use-case-triage` |
| **AI Impact Assessor** | Runs an AIA across the regimes in scope (ICO, OSA 2023, EU AI Act extraterritorial) | `ai-governance-legal-uk` | `/ai-governance-legal-uk:aia-generation` |
| **AI Inventory** | EU AI Act per-system inventory — provider / deployer roles, risk tier | `ai-governance-legal-uk` | `/ai-governance-legal-uk:ai-inventory` |
| **Vendor AI Reviewer** | Reviews vendor AI terms — training-on-data, liability, model change, policy gaps | `ai-governance-legal-uk` | `/ai-governance-legal-uk:vendor-ai-review` |
| **AI Reg Gap Checker** | Diffs a new AI regulation against your governance posture | `ai-governance-legal-uk` | `/ai-governance-legal-uk:reg-gap-analysis` |
| **AI Policy Monitor** | Sweeps saved AIAs, triage results, and vendor reviews for AI-policy drift | `ai-governance-legal-uk` | `/ai-governance-legal-uk:policy-monitor` |
| **AI Policy Starter** | Drafts a firm AI usage policy from published models, adapted to your profile | `ai-governance-legal-uk` | `/ai-governance-legal-uk:policy-starter` |
| **Trade Mark Clearance Screener** | First-pass clearance — UK IPO knockout check and confusion heuristics | `ip-legal-uk` | `/ip-legal-uk:clearance` |
| **Cease & Desist Drafter** | Drafts or triages a C&D calibrated to your enforcement posture | `ip-legal-uk` | `/ip-legal-uk:cease-desist` |
| **Takedown** | Drafts a notice under the E-Commerce Regulations / CDPA 1988 hosting safe harbour, triages one received | `ip-legal-uk` | `/ip-legal-uk:takedown` |
| **OSS Compliance Checker** | Classifies open source licences against your deployment model | `ip-legal-uk` | `/ip-legal-uk:oss-review` |
| **Invention Intake** | First-pass screen — novelty, inventive step, patentability (PA 1977 s.1), bar dates | `ip-legal-uk` | `/ip-legal-uk:invention-intake` |
| **FTO Triager** | Structured first look at potentially blocking patents — triage, not an opinion | `ip-legal-uk` | `/ip-legal-uk:fto-triage` |
| **Infringement Triager** | Triage across TM, copyright, patent, design, trade secret — factors, not a finding | `ip-legal-uk` | `/ip-legal-uk:infringement-triage` |
| **IP Clause Reviewer** | Reviews assignment, ownership, licence grants, warranties, and indemnities | `ip-legal-uk` | `/ip-legal-uk:ip-clause-review` |
| **IP Portfolio Tracker** | Registrations, renewals, maintenance fees, use declarations | `ip-legal-uk` | `/ip-legal-uk:portfolio` |
| **IP Renewal Watcher** | Scheduled deadline report from the IP portfolio register | `ip-legal-uk` | scheduled agent |
| **Claim Chart Builder** | Element-by-element claim chart, patent or civil cause of action | `litigation-legal-uk` | `/litigation-legal-uk:claim-chart` |
| **Letter Before Action Drafter** | Drafts a LBA under the Pre-Action Protocol with a "without prejudice" gate | `litigation-legal-uk` | `/litigation-legal-uk:demand-draft` |
| **Pre-Action Intake** | Pre-drafting context gathering — parties, facts, basis, leverage, privilege | `litigation-legal-uk` | `/litigation-legal-uk:demand-intake` |
| **LBA Received Triage** | Triages an inbound LBA — options, portfolio cross-check, handoff | `litigation-legal-uk` | `/litigation-legal-uk:demand-received` |
| **Witness Summons Triage** | Classifies, scopes, and plans compliance with a new witness summons | `litigation-legal-uk` | `/litigation-legal-uk:witness-summons-triage` |
| **Chronology Builder** | Builds or updates a chronology from declared sources and uploads | `litigation-legal-uk` | `/litigation-legal-uk:chronology` |
| **Witness Examination Prep** | Builds an examination outline tied to case theory with docs and impeachment | `litigation-legal-uk` | `/litigation-legal-uk:witness-examination-prep` |
| **Skeleton / Brief Drafter** | Drafts a brief section in house style, consistent with case theory | `litigation-legal-uk` | `/litigation-legal-uk:brief-section-drafter` |
| **Privilege / Disclosure Log Reviewer** | First-pass privilege log review (CPR 31) — obvious calls plus flags | `litigation-legal-uk` | `/litigation-legal-uk:privilege-log-review` |
| **Legal Hold** | Issue, refresh, release, or report on legal holds | `litigation-legal-uk` | `/litigation-legal-uk:legal-hold` |
| **Matter Intake / Briefing / Update / Close** | Uniform matter management — writes matter.md, history.md | `litigation-legal-uk` | `/litigation-legal-uk:matter-intake` |
| **Portfolio Status** | Risk distribution, upcoming hearings, stale matters | `litigation-legal-uk` | `/litigation-legal-uk:portfolio-status` |
| **Outside Counsel Status** | Weekly status-request drafts across the active portfolio | `litigation-legal-uk` | `/litigation-legal-uk:oc-status` |
| **Hearing Watcher** | Monitors court diary for upcoming hearings and listed dates | `litigation-legal-uk` | scheduled agent |
| **Clinic Intake** | Structured client intake with cross-area issue spotting and conflict flags | `legal-clinic-uk` | `/legal-clinic-uk:client-intake` |
| **Case Memo Scaffold** | IRAC-scaffolded analysis memo with research gaps flagged | `legal-clinic-uk` | `/legal-clinic-uk:memo` |
| **Research Roadmap** | Statutes, case law areas, BAILII / Westlaw / Lexis search terms — leads, not cites | `legal-clinic-uk` | `/legal-clinic-uk:research-start` |
| **Clinic Deadline Tracker** | Add, report, update, close case deadlines with malpractice-aware warnings | `legal-clinic-uk` | `/legal-clinic-uk:deadlines` |
| **Case Status Summariser** | Case status by audience — client, supervisor, court-ready | `legal-clinic-uk` | `/legal-clinic-uk:status` |
| **Client Letter Drafter** | Routine client correspondence — appointment confirms, document requests, updates | `legal-clinic-uk` | `/legal-clinic-uk:client-letter` |
| **Student Ramp** | Semester onboarding — clinic procedures, tool walkthrough, practice exercises | `legal-clinic-uk` | `/legal-clinic-uk:ramp` |
| **Semester Handoff** | End-of-semester case handoff memos — the mirror of ramp | `legal-clinic-uk` | `/legal-clinic-uk:semester-handoff` |
| **Supervisor Review Queue** | Supervising solicitor's review queue (when formal supervision is configured) | `legal-clinic-uk` | `/legal-clinic-uk:supervisor-review-queue` |
| **SQE / Bar Coach** | SQE1, SQE2, BPC, or LLB question practice targeted at weak subjects | `law-student-uk` | `/law-student-uk:bar-prep-questions` |
| **Socratic Drill Sergeant** | It asks, you answer, it pushes back — does not give you the answer | `law-student-uk` | `/law-student-uk:socratic-drill` |
| **IRAC Grader** | Grades your IRAC essay on structure, issue-spotting, rules, analysis | `law-student-uk` | `/law-student-uk:irac-practice` |
| **Case Briefer** | Brief a case in your preferred format with OSCOLA citation | `law-student-uk` | `/law-student-uk:case-brief` |
| **Outline Builder** | Build or extend an outline in your format from class notes and casebook | `law-student-uk` | `/law-student-uk:outline-builder` |
| **Cold Call Prep** | Predicts your tutor's questions and drills them before class | `law-student-uk` | `/law-student-uk:cold-call-prep` |
| **Exam Forecaster** | Analyse past papers from the same tutor; forecast likely emphases | `law-student-uk` | `/law-student-uk:exam-forecast` |
| **Legal Writing Critic** | Structural feedback on a draft — never rewrites | `law-student-uk` | `/law-student-uk:legal-writing` |
| **Flashcard Drillmaster** | Generate or drill flashcards — Leitner-style buckets | `law-student-uk` | `/law-student-uk:flashcards` |
| **Study Planner** | Long-term study plan, adaptive to session history | `law-student-uk` | `/law-student-uk:study-plan` |

---

## Install

### Claude Code

```bash
# 1. Add the marketplace
claude plugin marketplace add uk-agents/uk-legal-plugins

# 2. Install the plugin(s) you want
claude plugin install employment-legal-uk@uk-legal-plugins
claude plugin install commercial-legal-uk@uk-legal-plugins
claude plugin install privacy-legal-uk@uk-legal-plugins

# 3. Restart Claude Code. The plugin isn't live until you restart.

# 4. Run the cold-start interview
/employment-legal-uk:cold-start-interview
```

Or browse and install interactively with `/plugins` in a chat session.

To remove:

```bash
claude plugin uninstall employment-legal-uk          # remove a single plugin
claude plugin marketplace remove uk-legal-plugins    # remove the marketplace and all its plugins
```

> **Use user scope, not project scope.** When asked, pick *user* scope. Project scope blocks the plugin from reading files outside the project folder — your contracts in Documents, your case bundle in Dropbox. User scope gives the plugin no extra file access; it just works from any folder. See [QUICKSTART.md](QUICKSTART.md) for details.

### Claude Cowork

**Add the marketplace** (access all 11 plugins):

1. Personal plugins → Create plugin → Add marketplace → enter `uk-agents/uk-legal-plugins`
2. Plugins → Personal → click `+` next to each plugin you want

**Or upload a single plugin** (ZIP file):

1. Download the ZIP from the [Releases page](https://github.com/uk-agents/uk-legal-plugins/releases)
2. Personal plugins → Create plugin → Upload plugin → select the ZIP

### Agent compatibility

| Agent | Supported |
|-------|-----------|
| Claude Code | Yes |
| Claude Cowork | Yes |
| Cursor | Yes |
| GitHub Copilot | Yes |
| OpenAI Codex | Yes |

---

## Getting started

**Run the cold-start interview first.** Every other skill in a plugin reads from the practice profile it writes. Skipping setup is the single most common reason a skill produces generic output.

```
/employment-legal-uk:cold-start-interview
```

Replace `employment-legal-uk` with whichever plugin you installed.

- **Quick start (2 minutes)** — role, practice setting, jurisdictional footprint. Skills run immediately with sensible defaults.
- **Full setup (10–15 minutes)** — your real termination triggers, seed documents, escalation matrix, integration checks. Sharper outputs.

The interview asks which at the start. You can upgrade any time with `--full` or re-run any section with `--redo`.

### What it builds

A plain-text practice profile written to:

```
~/.claude/plugins/config/uk-legal-plugins/<plugin-name>/CLAUDE.md
```

Every skill reads this file before doing anything. It survives plugin updates and can be edited directly.

### Shared company profile

The first plugin you configure saves your firm or company name, sector, jurisdiction list, and escalation chain to a shared profile:

```
~/.claude/plugins/config/uk-legal-plugins/company-profile.md
```

Every other plugin reads this and skips those questions — so setup gets faster as you add more plugins.

### Connect a research tool

Pair with the [UK Legal MCP server](https://github.com/paulieb89/uk-legal-mcp) for live case law and legislation. Without it, every citation is tagged `[model knowledge — verify]`. See [MCP Connectors](#mcp-connectors) below for the full list.

---

## How it fits together

| | What it is | Where it lives |
|---|---|---|
| **Plugins** | Self-contained practice-area bundles — skills, agents, hooks, and a template practice profile. Install the ones you need. | `<plugin>/` |
| **Skills** | Domain expertise and step-by-step methods Claude draws on automatically when relevant — and slash actions you trigger explicitly: `/commercial-legal-uk:review`, `/privacy-legal-uk:dsar-response`. | `<plugin>/skills/<skill>/SKILL.md` |
| **Agents** | Scheduled or event-driven workflows (renewal watcher, hearing watcher, reg-change monitor). Runs in the background, posts to a channel or writes a file. | `<plugin>/agents/` |
| **Practice profile** | Plain-English `CLAUDE.md` describing your playbook, escalation rules, and house style. Every skill reads from it. | `~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md` |
| **Connectors** | [MCP servers](https://modelcontextprotocol.io/) wiring Claude to your data — research, CLM, DMS, IP register, productivity. | `.mcp.json` (per plugin) |

Everything is markdown and JSON. No build step.

---

## MCP connectors

> [!IMPORTANT]
> **Connect the UK Legal MCP first.** Without it, every citation comes from training data alone and is flagged `[verify]`. With it, the plugins pull from BAILII, TNA Find Case Law, legislation.gov.uk, and Hansard, and every citation is tagged with its source.

Each plugin's `.mcp.json` already lists the connectors it uses. You authorise them once, then Claude pulls from authoritative sources and verifies its citations against current databases.

| Connector | Source | Plugins |
|---|---|---|
| **[UK Legal MCP](https://github.com/paulieb89/uk-legal-mcp)** | TNA Find Case Law, BAILII, legislation.gov.uk, Hansard, HMRC, OSCOLA | all 11 (primary research) |
| **[BAILII MCP](https://github.com/paulieb89/bailii-mcp)** | BAILII — runs locally (BAILII blocks cloud IPs) | optional supplement for `litigation-legal-uk`, `law-student-uk`, `legal-clinic-uk` |
| **[UK Due Diligence MCP](https://github.com/paulieb89/uk-due-diligence-mcp)** | Companies House, corporate research, compliance | `corporate-legal-uk`, `commercial-legal-uk` |
| **[GOV.UK MCP](https://github.com/paulieb89/govuk-mcp)** | GOV.UK search, content, organisations, postcodes | `regulatory-legal-uk`, `product-legal-uk`, `ai-governance-legal-uk` |
| **[WhatDoTheyKnow MCP](https://github.com/paulieb89/whatdotheyknow-mcp)** | FOI request data | `regulatory-legal-uk`, `litigation-legal-uk` (public-body matters) |
| **Slack** | Your workspace | all 11 |
| **Google Drive** | Your account — docs, sheets, slides | all 11 |
| **Descrybe** | Case law research and summarisation | `legal-clinic-uk`, `ip-legal-uk`, `law-student-uk` |
| **Definely** | In-document drafting, defined terms | `commercial-legal-uk`, `corporate-legal-uk` |
| **iManage** | DMS — matter workspaces, document versions | `commercial-legal-uk`, `corporate-legal-uk` |
| **Ironclad** | Contract register, renewal dates, clauses | `commercial-legal-uk` |
| **DocuSign / CLM** | Envelope status, executed contracts | `commercial-legal-uk` |
| **Solve Intelligence** | Patent drafting and prosecution | `corporate-legal-uk`, `ip-legal-uk` |
| **TopCounsel** | Matter routing and outside counsel panel | `commercial-legal-uk`, `corporate-legal-uk`, `litigation-legal-uk` |
| **Box** | Files and folders in VDRs and matter rooms | `corporate-legal-uk` |
| **Everlaw** | eDiscovery productions, tagged sets, chronologies | `litigation-legal-uk` |
| **Aurora** | Matter management and calendaring | `litigation-legal-uk` |
| **Linear** / **Jira** / **Asana** | Launch tracker, issue tracking | `product-legal-uk` |

See [`CONNECTORS.md`](CONNECTORS.md) for what makes a good legal MCP connector and how to submit one.

---

## Making it yours

These are reference templates. They get better when you tune them to how your team works — and the customisation mechanism is the plugin itself, not a config file buried in a repo.

- **Run the cold-start interview.** It *is* the customisation mechanism. It asks how your practice works, reads your seed documents, and writes your practice profile. Every other skill reads from that profile.
- **Edit the practice profile.** Your profile at `~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md` survives plugin updates. Edit it directly for small fixes — a wrong escalation threshold, a new integration, a policy update.
- **Re-run setup.** `/<plugin>:cold-start-interview` again for a full re-interview when your practice shifts materially (new jurisdiction, new CLM, new policy).
- **Swap connectors.** Point `.mcp.json` at your CLM, DMS, eDiscovery platform, launch tracker, HRIS. Skills fall back gracefully when a connector isn't configured — no silent no-ops.
- **Bring your playbook and templates.** Drop your terminology, house style, and branded templates into the plugin's `CLAUDE.md` and `references/`.
- **Fork skills for house style.** Every skill is a markdown file under `skills/`. Edit the steps, the gates, the output format.

No build step. Everything is markdown and JSON.

---

## Skill & command reference

The full map across all 11 plugins. The cold-start interview is the first thing to run in any plugin.

### `ai-governance-legal-uk`

| Command | What it does |
|---|---|
| `/ai-governance-legal-uk:cold-start-interview` | Learn your AI governance practice |
| `/ai-governance-legal-uk:customize` | Re-run a focused section of the cold start |
| `/ai-governance-legal-uk:ai-inventory` | EU AI Act per-system inventory — provider/deployer role, risk tier |
| `/ai-governance-legal-uk:use-case-triage` | Classify an AI use case — approved, conditional, no |
| `/ai-governance-legal-uk:aia-generation` | Run an AI impact assessment in house format |
| `/ai-governance-legal-uk:vendor-ai-review` | Review vendor AI terms against governance positions |
| `/ai-governance-legal-uk:reg-gap-analysis` | Diff a new AI regulation against your governance posture |
| `/ai-governance-legal-uk:policy-monitor` | Keep the AI policy current with practice |
| `/ai-governance-legal-uk:policy-starter` | Draft a firm AI usage policy, adapted to your profile |
| `/ai-governance-legal-uk:matter-workspace` | Manage matter workspaces |

### `commercial-legal-uk`

| Command | What it does |
|---|---|
| `/commercial-legal-uk:cold-start-interview` | Learn your commercial contracts practice |
| `/commercial-legal-uk:customize` | Re-run a focused section of the cold start |
| `/commercial-legal-uk:review` | Review vendor agreement, NDA, or SaaS subscription |
| `/commercial-legal-uk:amendment-history` | Trace contract changes across base and amendments |
| `/commercial-legal-uk:renewal-tracker` | Contracts with cancel-by deadlines within 90 days |
| `/commercial-legal-uk:escalation-flagger` | Route a contract issue and draft the ask |
| `/commercial-legal-uk:review-proposals` | Review and approve pending playbook update proposals |
| `/commercial-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `renewal-watcher`, `deal-debrief`, `playbook-monitor` |

### `corporate-legal-uk`

| Command | What it does |
|---|---|
| `/corporate-legal-uk:cold-start-interview` | House cold-start, optional `--new-deal` kickoff |
| `/corporate-legal-uk:customize` | Re-run a focused section of the cold start |
| `/corporate-legal-uk:tabular-review` | Tabular review — one row per document, every cell cited |
| `/corporate-legal-uk:diligence-issue-extraction` | Extract issues per house thresholds |
| `/corporate-legal-uk:material-contract-schedule` | Build material contracts disclosure schedule |
| `/corporate-legal-uk:closing-checklist` | What's blocking completion with critical path |
| `/corporate-legal-uk:written-consent` | Draft board or shareholder written resolution (CA 2006 s.288) |
| `/corporate-legal-uk:entity-compliance` | Confirmation statements, accounts, PSC tracker |
| `/corporate-legal-uk:integration-management` | Post-completion integration tracker |
| `/corporate-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `dataroom-watcher` |

### `employment-legal-uk`

| Command | What it does |
|---|---|
| `/employment-legal-uk:cold-start-interview` | Learn jurisdictions and escalation rules |
| `/employment-legal-uk:customize` | Re-run a focused section of the cold start |
| `/employment-legal-uk:wage-hour-qa` | NMW / WTR / holiday pay Q&A |
| `/employment-legal-uk:hiring-review` | Review offer letter and restrictive covenants |
| `/employment-legal-uk:termination-review` | Dismissal review (ERA 1996, EqA 2010, ACAS Code) |
| `/employment-legal-uk:worker-classification` | IR35 / employment status against case law tests |
| `/employment-legal-uk:policy-drafting` | Draft policy with Scots / NI variations |
| `/employment-legal-uk:leave-tracker` | Check open leaves for deadline alerts |
| `/employment-legal-uk:log-leave` | Add a new statutory leave to the register |
| `/employment-legal-uk:investigation-open` | Open a new internal investigation matter |
| `/employment-legal-uk:investigation-add` | Add data to an open investigation |
| `/employment-legal-uk:investigation-memo` | Draft or update the privileged investigation memo |
| `/employment-legal-uk:investigation-query` | Ask questions against an open investigation log |
| `/employment-legal-uk:investigation-summary` | Audience-specific summary from investigation memo |
| `/employment-legal-uk:expansion-kickoff` | Kick off expansion planning for a new country |
| `/employment-legal-uk:expansion-update` | Update an in-progress expansion project |
| `/employment-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `leave-tracker` |

### `ip-legal-uk`

| Command | What it does |
|---|---|
| `/ip-legal-uk:cold-start-interview` | Learn your IP practice and posture |
| `/ip-legal-uk:customize` | Re-run a focused section of the cold start |
| `/ip-legal-uk:clearance` | Trade mark clearance first pass |
| `/ip-legal-uk:fto-triage` | Freedom-to-operate triage, not an FTO opinion |
| `/ip-legal-uk:invention-intake` | Invention disclosure first-pass screen |
| `/ip-legal-uk:cease-desist` | Draft a C&D or triage one you received |
| `/ip-legal-uk:takedown` | Hosting takedown notice or counter-notice |
| `/ip-legal-uk:infringement-triage` | Triage across all IP rights |
| `/ip-legal-uk:ip-clause-review` | Review IP clauses — assignment, licence, warranties |
| `/ip-legal-uk:oss-review` | Open source licence compliance check |
| `/ip-legal-uk:portfolio` | Track IP portfolio deadlines and renewals |
| `/ip-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `ip-renewal-watcher` |

### `law-student-uk`

| Command | What it does |
|---|---|
| `/law-student-uk:cold-start-interview` | Modules, qualification track (SQE / Bar / LLB), learning style |
| `/law-student-uk:customize` | Re-run a focused section of the cold start |
| `/law-student-uk:socratic-drill` | It asks, you answer, it pushes back |
| `/law-student-uk:case-brief` | Brief a case with OSCOLA citation |
| `/law-student-uk:outline-builder` | Build or extend an outline |
| `/law-student-uk:irac-practice` | Grade IRAC essay |
| `/law-student-uk:legal-writing` | Structural feedback on your writing — never rewrites |
| `/law-student-uk:cold-call-prep` | Predict tutor's questions and drill them |
| `/law-student-uk:bar-prep-questions` | SQE1 / SQE2 / BPC / LLB question practice |
| `/law-student-uk:flashcards` | Generate or drill flashcards |
| `/law-student-uk:exam-forecast` | Analyse past papers to forecast emphases |
| `/law-student-uk:study-plan` | Build or update a long-term study plan |
| `/law-student-uk:session` | Run a focused N-question session |

### `legal-clinic-uk`

| Command | What it does |
|---|---|
| `/legal-clinic-uk:cold-start-interview` | Supervisor setup — areas, jurisdiction, supervision style |
| `/legal-clinic-uk:customize` | Re-run a focused section of the cold start |
| `/legal-clinic-uk:build-guide` | Practice-area guide — intake, pedagogy posture, review gates |
| `/legal-clinic-uk:ramp` | Student semester onboarding |
| `/legal-clinic-uk:client-intake` | Structured intake with cross-area issue spotting |
| `/legal-clinic-uk:client-comms-log` | Append-only per-case client communication log |
| `/legal-clinic-uk:research-start` | Research roadmap — statutes, case law, search terms |
| `/legal-clinic-uk:memo` | IRAC-scaffolded analysis memo |
| `/legal-clinic-uk:draft` | First draft of a common clinic document |
| `/legal-clinic-uk:form-generation` | Generate a court / regulatory form from intake data |
| `/legal-clinic-uk:client-letter` | Routine client correspondence |
| `/legal-clinic-uk:status` | Case status by audience |
| `/legal-clinic-uk:deadlines` | Track case deadlines with malpractice-aware warnings |
| `/legal-clinic-uk:supervisor-review-queue` | Supervising solicitor's review queue |
| `/legal-clinic-uk:semester-handoff` | End-of-semester case handoff memos |

### `litigation-legal-uk`

| Command | What it does |
|---|---|
| `/litigation-legal-uk:cold-start-interview` | Risk, landscape, house brief style |
| `/litigation-legal-uk:customize` | Re-run a focused section of the cold start |
| `/litigation-legal-uk:matter-intake` | New matter — writes matter.md and history |
| `/litigation-legal-uk:matter-briefing` | Deep briefing on one matter for a call |
| `/litigation-legal-uk:matter-update` | Append a dated event to a matter's history |
| `/litigation-legal-uk:portfolio-status` | Risk, deadlines, stale matters |
| `/litigation-legal-uk:matter-close` | Close a matter — archive, retain record |
| `/litigation-legal-uk:matter-workspace` | Manage matter workspaces |
| `/litigation-legal-uk:demand-intake` | Pre-LBA context — parties, facts, leverage |
| `/litigation-legal-uk:demand-draft` | Draft LBA with "without prejudice" gate and .docx output |
| `/litigation-legal-uk:demand-received` | Triage inbound LBA — options, cross-check |
| `/litigation-legal-uk:witness-summons-triage` | Triage witness summons — scope, burden, privilege |
| `/litigation-legal-uk:legal-hold` | Issue, refresh, release, or report on legal holds |
| `/litigation-legal-uk:oc-status` | Weekly status-request emails to outside counsel |
| `/litigation-legal-uk:claim-chart` | Element chart — patent or civil cause |
| `/litigation-legal-uk:chronology` | Build a chronology from sources and uploads |
| `/litigation-legal-uk:witness-examination-prep` | Examination outline tied to case theory |
| `/litigation-legal-uk:privilege-log-review` | First-pass disclosure log review (CPR 31) |
| `/litigation-legal-uk:brief-section-drafter` | Draft a brief section in house style |
| *(scheduled)* | `hearing-watcher` |

### `privacy-legal-uk`

| Command | What it does |
|---|---|
| `/privacy-legal-uk:cold-start-interview` | Learn your privacy practice |
| `/privacy-legal-uk:customize` | Re-run a focused section of the cold start |
| `/privacy-legal-uk:use-case-triage` | Determine DPIA vs proceed |
| `/privacy-legal-uk:dpia-generation` | Generate a DPIA in house format |
| `/privacy-legal-uk:dpa-review` | Review a DPA — auto-detects controller vs processor |
| `/privacy-legal-uk:dsar-response` | Walk a DSAR and draft response |
| `/privacy-legal-uk:reg-gap-analysis` | Diff a regulation against current policy and practice |
| `/privacy-legal-uk:policy-monitor` | Keep the privacy policy current with practice |
| `/privacy-legal-uk:matter-workspace` | Manage matter workspaces |

### `product-legal-uk`

| Command | What it does |
|---|---|
| `/product-legal-uk:cold-start-interview` | Connect launch tracker, learn calibration |
| `/product-legal-uk:customize` | Re-run a focused section of the cold start |
| `/product-legal-uk:is-this-a-problem` | Fast answer for the quick question |
| `/product-legal-uk:launch-review` | Full launch review against framework and calibration |
| `/product-legal-uk:marketing-claims-review` | Review marketing copy (CAP Code / DMCC 2024) |
| `/product-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `launch-watcher` |

### `regulatory-legal-uk`

| Command | What it does |
|---|---|
| `/regulatory-legal-uk:cold-start-interview` | Watchlist, policy index, materiality |
| `/regulatory-legal-uk:customize` | Re-run a focused section of the cold start |
| `/regulatory-legal-uk:reg-feed-watcher` | Check regulatory feeds now |
| `/regulatory-legal-uk:policy-diff` | Diff a regulatory change against the policy library |
| `/regulatory-legal-uk:gaps` | Open gaps tracker |
| `/regulatory-legal-uk:policy-redraft` | Marked-up policy redraft closing a gap |
| `/regulatory-legal-uk:comments` | Open consultation papers and deadlines |
| `/regulatory-legal-uk:matter-workspace` | Manage matter workspaces |
| *(scheduled)* | `reg-change-monitor` |

---

## Repository layout

```
.claude-plugin/marketplace.json   # the marketplace manifest
<plugin>/                         # 11 plugins
  .claude-plugin/plugin.json      # plugin manifest
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (copied on cold-start)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  agents/<name>.md                # scheduled / event-driven agents
  hooks/hooks.json                # hook config (optional)
references/                       # shared templates (company profile, dashboard)
```

Each plugin's `CLAUDE.md` is a template — the `cold-start-interview` skill copies it to `~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md` on your machine.

---

## Contributing

Everything here is markdown and JSON. Fork, edit, PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

- **New skill** → add `<plugin>/skills/<skill-name>/SKILL.md` with `name`, `description`, `argument-hint` frontmatter (description under 1024 chars). Invokable as `/<plugin>:<skill-name>`.
- **New agent** → add `<plugin>/agents/<name>.md` with scheduling frontmatter and a system prompt.
- **New connector** → see [CONNECTORS.md](CONNECTORS.md) for what makes a good legal MCP server and how to submit yours.
- **Run validation before pushing** → `claude plugin validate .claude-plugin/marketplace.json` and `claude plugin validate <plugin>/`.

---

## License

Licensed under the [Apache License, Version 2.0](LICENSE).

---

## Credit

These plugins started as a UK-jurisdiction contribution to Anthropic's [`claude-for-legal`](https://github.com/anthropics/claude-for-legal) (PR #46). This repo is the standalone home, maintained as a published product for UK legal professionals.

> Not affiliated with Anthropic. Built by the community as a UK-jurisdiction contribution to the Open Plugins ecosystem.
