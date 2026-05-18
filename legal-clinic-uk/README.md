# Claude for UK Law School Clinics

*Supercharging access to justice through AI-enabled clinical legal education — built for the SRA and BSB supervision framework.*

A plugin for UK law school clinics — the institutions where law students, supervised by solicitors or barristers, provide free legal services to people who cannot afford representation. Housing, immigration, employment, family law, consumer protection, criminal defence, civil rights, benefits, debt.

**Every output is a draft for student analysis and supervising solicitor/barrister review — marked, gated, and logged. The plugin scaffolds the work; a student reasons through it; a supervising solicitor or barrister reviews. Nothing leaves the clinic without going through the supervision model the supervisor set at setup.**

## The problem this solves

UK law school clinics are structurally capacity-constrained. A supervising solicitor or barrister manages five to ten students. Each student carries a handful of cases while juggling lectures and seminars. Students turn over every term. Administrative tasks — intake write-up, first drafts, research starting points, status updates — consume hours that could go to advising clients. The result: long waitlists, limited caseloads, people who give up waiting.

This plugin cuts the time cost of everything *around* the lawyering, so the same students and supervisor serve meaningfully more clients — and students spend more time on the analysis and strategy that make clinical legal education worthwhile.

**It accelerates the non-educational parts. It preserves the analytical work.** That is the design principle.

## Who uses it

| Role | Runs | Gets |
|---|---|---|
| **Supervising solicitor / barrister** | `/legal-clinic-uk:cold-start-interview` (once), `/legal-clinic-uk:supervisor-review-queue` (if formal review enabled) | Clinic context configured, student work reviewed |
| **Students** | `/legal-clinic-uk:ramp` (start of term), then `/legal-clinic-uk:client-intake`, `/legal-clinic-uk:draft`, `/legal-clinic-uk:memo`, `/legal-clinic-uk:research-start`, `/legal-clinic-uk:status`, `/legal-clinic-uk:client-letter` | Starting points — never final work product |

## Commands

| Command | What it does | What it doesn't do |
|---|---|---|
| `/legal-clinic-uk:cold-start-interview` | **Supervisor.** One-time clinic config: practice areas, jurisdiction (E&W / Scotland / NI), supervision style, handbook/rules upload | — |
| `/legal-clinic-uk:build-guide` | **Supervisor.** Author a per-practice-area guide: intake questions, pedagogy posture (assist / guide / teach), review gates, cross-plugin checks | Doesn't replace `/legal-clinic-uk:cold-start-interview` — this tunes skills for one practice area |
| `/legal-clinic-uk:ramp` | **Students.** Term onboarding: clinic procedures, tool walkthrough, practice exercises | Doesn't replace the supervisor's orientation |
| `/legal-clinic-uk:client-intake` | Structured intake: practice-area templates, cross-area issue spotting, conflict flags, triage | Doesn't decide whether to take the case |
| `/legal-clinic-uk:draft [doc]` | First draft: ET1 claim narratives, eviction defences, protective injunction applications, demand letters — jurisdiction-aware for E&W / Scotland / NI | Doesn't produce final work product |
| `/legal-clinic-uk:memo` | IRAC-scaffolded case analysis with research gaps flagged — OSCOLA format for citations | Doesn't write the analysis — scaffolds it |
| `/legal-clinic-uk:research-start [issue]` | Research roadmap: statutes, case law areas, BAILII / Westlaw UK / LexisNexis UK search terms — OSCOLA-formatted starting citations | **Leads, not verified authority** — students confirm everything |
| `/legal-clinic-uk:status [audience]` | Case status summary: client-facing, internal, or tribunal/court-ready | Doesn't file anything |
| `/legal-clinic-uk:client-letter [type]` | Routine correspondence: appointment confirms, doc requests, brief updates | Doesn't do substantive advice — that's `/legal-clinic-uk:status client` or a conversation |
| `/legal-clinic-uk:deadlines` | Track case deadlines — add, cross-case rollup with warnings at 14/7/3/1 days, overdue flags | Doesn't calculate deadlines from triggering events; student does the math per the applicable rule |
| `/legal-clinic-uk:client-comms-log [case]` | Append-only per-case communication log — calls, emails, letters, in-person | Doesn't store substantive legal analysis; comm record only |
| `/legal-clinic-uk:semester-handoff` | End-of-term offboarding — per-case handoff memos for the next cohort | Doesn't close cases; cases closing at term end get a final `/legal-clinic-uk:status internal` memo |
| `/legal-clinic-uk:supervisor-review-queue` | **Supervisor, if formal review enabled.** What's waiting, approve/edit/return | Optional — one of three supervision models |

## Ethical and confidentiality preconditions

Before using this plugin with real client matters, confirm with your clinic's supervising solicitor or barrister and your school's IT / legal professional responsibility team:

1. **Your Claude account tier and its data retention and training policies.** Team, Enterprise, Work, Education, and individual accounts have different guarantees about retention, training use, and subprocessor handling. Confirm what applies to the clinic's account.
2. **Your client consent and disclosure practices for AI-assisted work** per the SRA Code of Conduct 2019 (Principle 7 — acting in clients' best interests; Principle 6 — behaving in a way that maintains trust), BSB Handbook (gC18, gC19 on supervision), and your school's ethics guidance. Decide whether and how the clinic discloses AI use to clients; document it.
3. **How privileged and confidential material will be handled** — what gets pasted into sessions, where outputs are stored, who has access, how long material is retained, how student turnover affects access.
4. **Whether any of your clinic's practice areas involve heightened confidentiality** (immigration / asylum, criminal defence, domestic violence, some family and civil rights matters) that require additional safeguards — and decide whether the plugin is appropriate for those case types at all.

Do not skip this step. The cold-start interview (`/legal-clinic-uk:cold-start-interview`) captures these decisions as Part 0 before any other configuration.

## Confidence markers

Skills across this plugin flag confidence inline so students and supervising solicitors/barristers can see where the scaffold is uncertain vs. where it is asserting. Every marker is a prompt to verify — nothing marked is trusted.

- `[AI-ASSISTED DRAFT — requires student analysis and supervising solicitor/barrister review]` — baseline label applied to every output. Review label, not part of client-facing content; strip before anything goes out.
- `[UNCERTAIN: specific reason]` — the skill is genuinely unsure on this call (minority position, debatable issue, jurisdiction the skill doesn't know well). Used in memo, intake, status, draft.
- `[VERIFY: claim — check source]` — a claim stated as likely but unverified. Student must confirm before relying — citations, local rule formats, rule statements. Used heavily in research-start, draft, status, memo.
- `[RESEARCH NEEDED: ...]` — memo scaffold marker where a rule statement is a research gap, not a conclusion.
- `[STUDENT ANALYSIS: ...]` — memo scaffold marker where the application is blank by design.
- `[STUDENT CONCLUSION: ...]` — memo scaffold marker where the conclusion is blank by design.
- `[FACT NEEDED: ...]` — draft scaffold marker where a required fact is missing from case notes.
- `CHECK WITH [SUPERVISOR] BEFORE SENDING` / `BEFORE FILING` — supervision-flag label applied in "configurable flags" supervision mode to outputs on flagged topics.
- `[SRA-CODE]` — reference to the SRA Code of Conduct 2019 or SRA Standards and Regulations.
- `[BSB-HANDBOOK]` — reference to the BSB Handbook.
- `[CPR-RULE]` — reference to the Civil Procedure Rules 1998 or a specific Practice Direction.
- `[LIMITATION-ACT-1980]` — reference to the Limitation Act 1980 limitation period provisions.

## Built-in safeguards

Every output from every skill includes:

- **AI-assisted label** — requires student analysis and supervising solicitor/barrister review
- **Confidence indicators** — `[UNCERTAIN: ...]` where genuinely unsure, rather than guessing
- **Verification prompts** — specific things to fact-check before relying on output
- **Ethical reminders** calibrated to the task and to the SRA/BSB supervision requirements

These are designed to reinforce the clinical education model: the student does the thinking, the plugin does the heavy lifting around it. Students are not solicitors or barristers — all advice is supervised.

**Research outputs specifically:** `/legal-clinic-uk:research-start` gives leads and frameworks for the student to verify and develop using Westlaw UK, LexisNexis UK, BAILII, or legislation.gov.uk. It explicitly does **not** provide legal citations as authoritative. Citations are formatted in OSCOLA style as a starting structure — the student confirms accuracy and authority before relying on them. This is both an ethical safeguard and a pedagogical feature.

## Supervision workflow (configurable)

Whether the plugin includes a formal review workflow — student draft → supervisor review → approved — is a genuine open question. Some clinics want a hard gate; others find it overly prescriptive for their supervision structure.

The cold-start interview asks the supervisor to choose:

1. **Formal review queue** — client/tribunal-bound output queues, supervisor approves, all logged
2. **Configurable flags, informal review** — certain triggers label output "CHECK WITH SUPERVISOR," no queue mechanism
3. **Lighter-touch** — standard safeguard labels on everything, supervisor supervises through existing clinic structure (case rounds, one-on-ones)

Changeable later by editing `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. Your configuration is stored at that version-independent path and survives plugin updates.

## Term turnover: the `/legal-clinic-uk:ramp` solution

Every term, clinics rebuild from scratch. New students need weeks to learn procedures, tools, practice-area basics. `/legal-clinic-uk:ramp` is the interactive onboarding — it reads the clinic handbook the supervisor uploaded at setup and teaches it, with low-stakes practice exercises (fake intake, practice draft, research roadmap) before the student touches a real case.

`/legal-clinic-uk:ramp --card` generates the one-page student reference card: commands, what Claude can and can't help with, verification habits. Hand it out on day one.

## Ethical framework: SRA Code of Conduct 2019 and BSB Handbook

The ethical framework this plugin operates within. The SRA Code of Conduct 2019 (for solicitors and SRA-authorised firms) and BSB Handbook (for barristers) require competence, confidentiality, appropriate supervision, and client care. The SRA Standards and Regulations set minimum terms for professional indemnity insurance and regulate third-party managed accounts. For clinics with access to legal aid, LASPO 2012 (Legal Aid, Sentencing and Punishment of Offenders Act) rules on scope and eligibility apply. The Access to Justice Foundation and pro bono protocols are relevant for unmet-need referrals.

Clinical supervisors are among the most thoughtful people in legal education about professional responsibility. The plugin is designed to operate the way they would want it to.

## Citation style

Citations in all skills follow **OSCOLA** (Oxford University Standard for the Citation of Legal Authorities), the standard for UK legal writing. Research-start outputs, memos, and drafts use OSCOLA style as a starting point — the student verifies and refines citations before any document is finalised. Not Bluebook.

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Supervisor's one-time setup — practice areas, jurisdiction (E&W / Scotland / NI), supervision style, seed docs |
| **build-guide** | Supervisor's per-practice-area guide — intake, pedagogy posture (assist/guide/teach), review gates, cross-plugin checks |
| **ramp** | Student term onboarding — procedures, tools, practice exercises |
| **client-intake** | Practice-area-specific intake with cross-area issue spotting, conflict flags, triage |
| **draft** | First-draft generation — practice-area templates, jurisdiction-aware (CPR, tribunal rules, Scottish procedure), explicitly starting point |
| **memo** | IRAC scaffolding with research gaps flagged in OSCOLA format — the analysis is the student's |
| **research-start** | Research roadmap — leads not authorities, students verify and develop via Westlaw UK / LexisNexis UK / BAILII / legislation.gov.uk |
| **status** | Audience-aware case summaries — client / internal / tribunal or court |
| **client-letter** | Routine correspondence from templates — client care obligations per SRA Code |
| **supervisor-review-queue** | Optional formal review workflow — only active if supervisor chose it |
| **deadlines** | Per-case deadline tracking, cross-case rollup, warning cadence, overdue flags — ET 3-month limit plausibility band included |
| **client-comms-log** | Append-only per-case communication record — calls, emails, letters, in-person |
| **semester-handoff** | End-of-term offboarding memos; mirror of `/legal-clinic-uk:ramp` |

*(Two deprecated skills — `form-generation`, `plain-language-letters` — redirect to `/legal-clinic-uk:draft` and `/legal-clinic-uk:client-letter` + `/legal-clinic-uk:status client` respectively.)*

## Research connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The UK legal research connectors in this plugin are:

- **uk-legal MCP** — UK case law (TNA Find Case Law), legislation (legislation.gov.uk), Hansard, Bills, HMRC guidance, and OSCOLA citation parsing. Citations retrieved through uk-legal are tagged `[uk-legal]` and can be traced back to primary sources.
- **BAILII** — British and Irish Legal Information Institute. Full-text case law. Citations retrieved here are tagged `[BAILII]`.
- **govuk MCP** — official GOV.UK guidance, statutory instruments, and regulatory content.
- **Model knowledge** tagged `[model knowledge — verify]` — to be checked against Westlaw UK, LexisNexis UK, BAILII, or legislation.gov.uk before anyone relies on it.

## Integrations (open questions)

Ships with the UK MCP connectors in `.mcp.json`:

- **uk-legal** — statutes, case law, Hansard, bills, OSCOLA citation parsing
- **govuk** — GOV.UK guidance and postcode/local authority lookup
- **uk-due-diligence** — Companies House, Charity Commission, HMLR, Gazette, HMRC VAT

Clio, LEAP, and Osprey are noted as optional future case-management integrations — widely used in UK law schools. Starting with file upload; a connector would let `/legal-clinic-uk:client-intake` and `/legal-clinic-uk:status` pull case data directly.

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## File structure

```
legal-clinic-uk/
├── .claude-plugin/plugin.json
├── .mcp.json                          # uk-legal, govuk, uk-due-diligence
├── CLAUDE.md                          # Supervisor's clinic config — written by cold-start
├── README.md
├── deadlines.yaml                     # operational deadline ledger
├── skills/                            # each skill is also the slash command /legal-clinic-uk:<skill>
│   ├── cold-start-interview/          # Supervisor — one-time setup
│   ├── build-guide/                   # Supervisor — per-practice-area guide
│   ├── ramp/                          # Students — term onboarding
│   ├── client-intake/
│   │   └── references/intake-templates/
│   ├── draft/
│   ├── memo/
│   ├── research-start/
│   ├── status/
│   ├── client-letter/
│   ├── supervisor-review-queue/       # Supervisor, if formal review enabled
│   │   └── references/review-queue.yaml
│   ├── deadlines/
│   ├── client-comms-log/
│   ├── semester-handoff/
│   ├── form-generation/               # deprecated → /legal-clinic-uk:draft
│   └── plain-language-letters/        # deprecated → /legal-clinic-uk:client-letter, /legal-clinic-uk:status client
├── references/
│   └── plausibility-bands/
│       └── EW.md                      # England & Wales deadline plausibility bands
├── handoffs/                          # per-term handoff memos
│   └── [YYYY-term]/
│       ├── _summary.md
│       └── [case-id].md
├── client-comms/                      # per-case communication logs
│   └── [case-id]/
│       └── log.md
└── hooks/hooks.json
```

## Prerequisites

Some features reference external integrations (document management, case management, legal research). These are not bundled — if you have an MCP server for one of these in your environment, the relevant features will use it. Without one, the plugin falls back to file upload and manual workflows. Run `/legal-clinic-uk:cold-start-interview --check-integrations` to see what's available in your environment.
