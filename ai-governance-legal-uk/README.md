# AI Governance Plugin (UK)

In-house AI governance counsel workflows for UK law: use case triage, AI impact assessments,
vendor AI review, and regulation-to-policy gap analysis. Built around a team practice profile
learned from your AI policy, a reference impact assessment, and your key vendor AI agreements.

Covers the UK's pro-innovation regulatory framework: ICO AI guidance, UK GDPR / DPA 2018 automated
decision-making rights, CMA AI Foundation Models review, FCA AI model risk requirements, Online Safety Act 2023
(Ofcom), DSIT's sector-regulator-led approach, MHRA AI as a Medical Device, and Cabinet Office public
sector AI governance. Also covers EU AI Act obligations for UK companies that offer AI systems to EU
users or deploy in EU/EEA — not domestic UK law, but a key compliance obligation for many UK companies.

**Every output is a draft for solicitor or barrister review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A lawyer reviews, verifies, and decides. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Privacy counsel / AI governance counsel** | Impact assessments, vendor AI review, reg gap analysis |
| **Product counsel** | Use case triage, launch review with AI component |
| **GC / Legal ops** | AI policy governance, escalation, board-level issues |
| **Procurement / legal** | Vendor AI contract review |
| **DPO / compliance** | UK GDPR Article 22 automated decision-making, ICO AI audit readiness |

## UK regulatory landscape

This plugin applies these frameworks:

| Regulator / Framework | What it covers |
|---|---|
| **ICO** | UK GDPR / DPA 2018 — Article 22 automated decision-making rights, data protection impact assessments (DPIAs), AI and data protection guidance, ICO AI auditing framework |
| **CMA** | Competition and Markets Authority — AI Foundation Models review, algorithmic accountability, market studies on AI |
| **FCA / PRA** | Financial services AI — model risk management (PS7/24), algorithmic trading, credit decisions, insurance pricing AI |
| **Ofcom** | Online Safety Act 2023 — systemic risk assessments, age verification, illegal content; AI-generated content obligations |
| **MHRA** | AI as a Medical Device (AIaMD) — guidance on software as a medical device, adaptive algorithms |
| **DSIT** | Department for Science, Innovation and Technology — pro-innovation regulatory framework, AI Safety Institute, Algorithmic Transparency Recording Standard (ATRS) |
| **Cabinet Office** | Public sector AI — procurement guidance, algorithmic transparency obligations for public bodies |
| **EU AI Act** | Applies to UK companies offering AI systems to EU users or deploying in EU/EEA — not UK domestic law, but critical for many UK companies with EU exposure |

## First run: the cold-start interview

The plugin interviews you to learn: are you a builder, deployer, or both — which
UK regulations actually apply — what your use case red lines are — and what good
impact assessment looks like here. Then it reads your seed documents and learns your
real positions and house style.

```
/ai-governance-legal-uk:cold-start-interview
```

## Commands

| Command | Does |
|---|---|
| `/ai-governance-legal-uk:cold-start-interview` | Cold-start interview — writes your practice profile |
| `/ai-governance-legal-uk:use-case-triage [use case]` | Classify a use case against your registry (approved / conditional / never) |
| `/ai-governance-legal-uk:aia-generation [use case]` | Run an AI impact assessment (AIA) in your house style |
| `/ai-governance-legal-uk:vendor-ai-review [vendor/file]` | Review a vendor AI agreement against your positions |
| `/ai-governance-legal-uk:reg-gap-analysis [regulation]` | Diff a new regulation or guidance against current policy/practice |
| `/ai-governance-legal-uk:policy-monitor` | Weekly sweep for AI policy drift, or direct query for a proposed new practice |
| `/ai-governance-legal-uk:policy-starter` | Draft a firm AI usage policy from published model policies, adapted to your practice profile (draft for solicitor review) |
| `/ai-governance-legal-uk:ai-inventory` | Manage the per-system AI inventory — EU AI Act role / tier classification, UK regulatory flags |
| `/ai-governance-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Writes `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` from interview + seed docs |
| **use-case-triage** | Classifies use cases against the registry; flags missing assessments |
| **aia-generation** | AI impact assessment (AIA) in house format — covers UK GDPR/DPA 2018, ICO guidance, sector regulation, EU AI Act (where applicable) |
| **vendor-ai-review** | AI-specific vendor contract review against governance positions |
| **reg-gap-analysis** | New reg/guidance vs. current state, remediation plan — covers ICO guidance updates, CMA reports, FCA publications, DSIT framework, EU AI Act implementing acts |
| **policy-monitor** | Crawls outputs for practice drift; drafts AI policy language updates |
| **policy-starter** | Produces a first-draft AI usage policy sourced from UK published model policies (Law Society AI guidance, ICO AI guidance, SRA risk outlook, sector regulator guidance, peer policies, EU AI Act Art. 4 AI literacy requirements), adapted to your practice profile — draft for solicitor review, not a finished policy |
| **ai-inventory** | EU AI Act per-system inventory with UK regulatory flags (ICO DPIA trigger, CMA, FCA); role and tier assessed per system |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

## Quick start

### 1. Setup

```
/ai-governance-legal-uk:cold-start-interview
```

Have ready (if they exist): your AI or acceptable use policy, one prior impact assessment,
key vendor AI agreements, model inventory or approved tool list.

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` and survives plugin updates.

### 2. Triage a new use case

```
/ai-governance-legal-uk:use-case-triage "Sales team wants to use AI to score leads automatically"
```

Output: risk tier, registry match or gap, required conditions, impact assessment needed or not.

### 3. Run an impact assessment

```
/ai-governance-legal-uk:aia-generation "AI-powered CV screening for HR"
```

Intake questions → impact assessment in your house format → policy consistency check →
mitigation conditions → UK GDPR Article 22 analysis → ICO guidance check.

### 4. Review a vendor AI agreement

```
/ai-governance-legal-uk:vendor-ai-review openai-terms.pdf
```

Output: term-by-term vs. your positions, proposed redlines, gaps to escalate.

### 5. Gap analysis against new UK or EU AI regulation

```
/ai-governance-legal-uk:reg-gap-analysis "ICO AI auditing framework"
/ai-governance-legal-uk:reg-gap-analysis "EU AI Act high-risk provisions — EU nexus"
/ai-governance-legal-uk:reg-gap-analysis "Online Safety Act 2023 Ofcom duties"
```

## Plugin triangle: AI governance ↔ product counsel ↔ privacy

These three plugins are designed to work together. AI governance is the third leg.

- **Product counsel** detects when a launch has an AI component → hands off to
  `/ai-governance-legal-uk:use-case-triage` and `/ai-governance-legal-uk:aia-generation`
- **Privacy** detects when an AI use case involves personal data → hands off to
  `/privacy-legal-uk:pia-generation`, if the plugin is installed. Note: UK GDPR Article 35 DPIA and AIA often overlap — an AI system processing personal data at scale likely needs both; the AIA does not substitute for the DPIA.
- **AI governance** detects when an impact assessment raises data protection issues →
  hands off to `/privacy-legal-uk:pia-generation`, if the plugin is installed

The handoff is explicit: each plugin flags when the other is needed and states what
question to answer there.

## UK-specific notes

- **ICO AI guidance is the primary UK reference for data-driven AI governance.** The ICO has published guidance on explaining AI decisions, AI auditing, and high-risk processing. This is not a statutory code but the ICO treats it as indicative of good practice.
- **UK GDPR Article 22 is live UK law.** Automated individual decision-making rights apply to any system making solely automated decisions with significant effects on individuals. Unlike the EU AI Act, this is already in force. Every AIA should assess Article 22 exposure.
- **The EU AI Act is NOT UK domestic law.** The UK did not retain the EU AI Act after Brexit. However, if your company offers AI systems to EU users or deploys in the EU, the EU AI Act applies to that activity. Many UK companies need both frameworks.
- **DSIT's pro-innovation approach means no single AI Act (yet).** The UK's current approach is for existing regulators to apply existing laws to AI, with cross-cutting principles from DSIT. Watch for an AI Bill or specific powers legislation — this may change.
- **Sector regulators vary significantly.** FCA/PRA (financial services), Ofcom (online safety/comms), MHRA (medical devices), CQC (health), ORR (rail), CAA (aviation) each have their own AI risk posture and guidance. Sector-specific obligations can be more demanding than the general framework.
- **Public sector.** Public bodies have additional obligations under the Algorithmic Transparency Recording Standard (ATRS) and Cabinet Office procurement guidance.

## File structure

```
ai-governance-legal-uk/
├── CLAUDE.md
├── README.md
├── references/
│   └── currency-watch.md
└── skills/
    ├── cold-start-interview/
    ├── use-case-triage/
    ├── aia-generation/
    ├── vendor-ai-review/
    ├── reg-gap-analysis/
    ├── policy-monitor/
    ├── policy-starter/
    ├── ai-inventory/
    └── matter-workspace/
```

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `policy-monitor` agent watches for drift between your AI governance policy and your practice and proposes updates. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Notes

- Gap check (`reg-gap-analysis`) handles incoming regulations. Policy monitor handles internal practice drift. Different tools for different directions of change.
- Policy monitor requires an outputs folder to be configured (set during setup) for the sweep to work. Direct-query mode works without it.
- Use case triage is only as good as the registry. Spend the setup interview getting the red lines right — they drive everything.
- Impact assessment format comes from your seed assessment. If you didn't provide one during setup, it uses a baseline structure — re-run setup with a reference to improve it.
- Builder and deployer obligations are treated separately. If you're both, the skills ask which hat you're wearing for each task.
- Gap analysis is manual (you point it at a regulation or guidance doc). For automated monitoring, pair with the `regulatory-legal-uk` plugin, if the plugin is installed.
- The EU AI Act section of the practice profile applies only where the company has EU nexus. The cold-start interview asks about this explicitly.
