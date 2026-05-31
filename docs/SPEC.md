# uk-legal-plugins — Harness Spec

This repo is a **harness** for UK legal professionals using foundation-model agents (Claude Code, Cursor, Copilot, Codex). Agency lives in the model. We provide tools (MCP connectors), knowledge (skills, practice profiles, OSCOLA conventions), observation (cold-start interviews, matter-workspaces), action interfaces (commands, hooks), and permissions (jurisdiction gates, "verify with qualified lawyer" warnings, irreversibility gates on filings/sends).

Every component here is filtered by the durability test: *would this still matter if the model got 10× smarter tomorrow?* Connectors to live UK registers — yes. Schema for a UK practice profile — yes. Retry wrappers, output validators, prompt-engineering scaffolds the model now absorbs — no.

## Current State (local audit)

- **11 plugins live** under `<plugin>/` with `.claude-plugin/plugin.json`, `.mcp.json`, `skills/<name>/SKILL.md`, `agents/`, `hooks/`, per-plugin `CLAUDE.md` template (copied by `cold-start-interview` to `~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md`).
- **Marketplace manifest** at `.claude-plugin/marketplace.json` — alpha order warning is known/curated.
- **Skill counts (audited):** employment 18, commercial 11, corporate 13, IP 12, privacy 9, product 7, regulatory 9, ai-governance 10, litigation 19, legal-clinic 16, law-student 13. Every plugin ships `cold-start-interview`, `customize`, `matter-workspace`.
- **MCP wiring is inconsistent.** `employment-legal-uk` already points at production HTTPS Fly endpoints (`uk-legal-mcp.fly.dev`, `govuk-mcp.fly.dev`, `uk-due-diligence-mcp.fly.dev`, `whatdotheyknow-mcp.fly.dev`, `property-shared.fly.dev`) — this is the canonical shape. `commercial-legal-uk` and `litigation-legal-uk` still use placeholder `npx -y @modelcontextprotocol/server-uk-legal` stdio commands that don't exist on npm. **Normalising `.mcp.json` across all 11 plugins is the single highest-leverage Build item.**

## Coverage Matrix

| Plugin | Citing UK sources | Use as-is | Extend | Build (critical) |
|---|---|---|---|---|
| **employment** | ERA 1996, Equality Act 2010, IR35/ITEPA, ACAS code, ET rules | 18 skills, MCP wired | Add Scots/NI ET divergence supplements | Auto-pulled ACAS Code links via govuk MCP |
| **commercial** | English contract law (Misrep Act 1967, SGA, CRA 2015), Scots law notes | Definely/Ironclad/iManage MCP | Fix `.mcp.json` to HTTPS endpoints | Scots law divergence rules (delict, prescription) as a reference doc the model loads |
| **corporate** | CA 2006, Takeover Code, FSMA 2000, PSC | Companies House via uk-due-diligence MCP | Add Takeover Panel feed connector | PSC/director sanction-list cross-check tool |
| **ip** | TMA 1994, PA 1977, CDPA 1988, RDA 1949, Trade Secrets Regs 2018 | Skills full | UKIPO One IPO API connector (target 2026) | Portfolio-deadline calendar tool reading UKIPO once API ships [UKIPO One IPO programme — retrieved 2026-05-21](https://www.gov.uk/government/publications/one-ipo-transformation-programme) |
| **privacy** | UK GDPR, DPA 2018, PECR, NIS Regs | Skills full | ICO reg-action feed (RSS) | DSAR 1-month deadline tracker with calendar hooks |
| **product** | CRA 2015, DMCC Act 2024, OSA 2023, CAP Code, MHRA | Skills full | ASA ruling feed | DMCC 2024 unfair-practice checklist as skill |
| **regulatory** | FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HMT, GOV.UK consultations | `reg-feed-watcher` skill | Per-regulator RSS adapters | Diff-engine: changed-statute → policy-library impact |
| **ai-governance** | ICO AI guidance, DSIT framework, EU AI Act (UK→EU), OSA | Skills full | Global AI Reg Tracker connector | UK-specific AI use-case registry schema (no equivalent exists) |
| **litigation** | CPR, PD 57AC, Civil Evidence Act, Scots OCR/RCS, NI rules | 19 skills | Fix `.mcp.json` placeholders | HMCTS court listings connector (licensed programme — pending application) [HMCTS court data — retrieved 2026-05-21](https://www.gov.uk/government/publications/hmcts-data-strategy) |
| **legal-clinic** | SRA student practice rule, BSB pupillage rule, OSCOLA | Descrybe MCP | OSCOLA validator skill | Supervisor-signoff hook (irreversibility gate on client-facing outputs) |
| **law-student** | LLB, GDL, SQE1/SQE2, BPTC, CILEx, Scots DPLP | Full | BAILII MCP wired by default | SQE syllabus mapper (free + viral) |

## Data Sources

| Source | Used by | Wired (live MCP) | Notes |
|---|---|---|---|
| `legislation.gov.uk` | all 11 | yes — `uk-legal` MCP | check `extent` field for E&W/Scot/NI |
| TNA Find Case Law | all 11 | yes — `uk-legal` MCP | E&W judgments from 2001 |
| BAILII | all 11 | partial — local stdio only (BAILII blocks cloud IPs) | document the constraint |
| Hansard / Bills / Votes / Committees | regulatory, ai-gov, product | yes — `uk-legal` MCP | |
| GOV.UK content + organisations | all 11 | yes — `govuk` MCP | |
| Companies House | corporate, commercial, litigation | yes — `uk-due-diligence` MCP | |
| Charity Commission | corporate, regulatory | yes — `uk-due-diligence` MCP | |
| HMLR Land Registry | corporate, litigation | yes — `uk-due-diligence` MCP | |
| The Gazette (insolvency) | corporate, litigation | yes — `uk-due-diligence` MCP | |
| HMRC VAT register + guidance | commercial, employment, regulatory | yes — `uk-legal` + `uk-due-diligence` | |
| WhatDoTheyKnow (FOI) | regulatory, ai-gov, litigation | yes — `whatdotheyknow` MCP | |
| ICO register / enforcement | privacy, ai-gov | **missing** — model knowledge only | Build: ICO RSS adapter |
| FCA register / Handbook | regulatory, corporate, product | **missing** | Build: FCA register adapter (public) |
| UKIPO (TM/patent/design register) | ip | **missing** — EPO OPS partial workaround | Wait for UKIPO One IPO API |
| ASA rulings | product | **missing** | Build: ASA scraper or RSS |
| HMCTS court listings | litigation | **missing — licensing required** | Pending HMCTS data programme |
| Definely / Ironclad / DocuSign / iManage / Box | commercial, corporate | wired via `.mcp.json` | third-party paid |

## Jurisdictional Fidelity

`marketplace.json` claims E&W + Scotland + NI coverage for every plugin. Audit reality:

- **Solid:** legislation MCP returns `extent` per statute; `uk-legal` and `uk-due-diligence` are jurisdiction-aware.
- **Conflation risk:** `commercial-legal-uk` defaults to English contract law with "Scots law notes" but skills like `nda-review`, `saas-msa-review` don't take a `jurisdiction` parameter. Same in `litigation-legal-uk` (CPR-defaulted; OCR/RCS for Scotland and NI rules glossed over).
- **Build:** add an explicit `jurisdiction: "EW" | "Scot" | "NI"` arg to every drafting/review skill, default from practice profile. The model handles the divergence — the harness must surface the choice.

## Compliance & Professional Duty

SRA and the courts have been explicit. *Ayinde v Hackney* and *Al-Haroun v QNB* (High Court, May 2025) confirmed solicitors must verify AI-cited authorities against authoritative sources; the duty to the court is not delegable to a model [Law Society — Generative AI: the essentials, updated post-Ayinde — retrieved 2026-05-21](https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials), [SRA compliance tips on AI — retrieved 2026-05-21](https://www.sra.org.uk/solicitors/resources/innovate/compliance-tips-for-solicitors/).

Harness implications (all Build, all durable):

1. **Provenance tagging.** Every citation rendered by a skill must carry `[source — retrieved YYYY-MM-DD]` or `[model knowledge — verify]`. Already partially implemented in `CONNECTORS.md` philosophy; enforce as a skill-template invariant.
2. **Verify-with-lawyer banner.** Every drafting output ends with the standard disclaimer block; encoded in `references/dashboard-template.md` style.
3. **Audit trail.** `matter-workspace` skill writes a `transcript.md` per matter. Make this mandatory and machine-parseable (frontmatter: matter-id, jurisdiction, skills-invoked, sources-cited).
4. **Irreversibility gates.** Letters Before Action, cease-and-desist, court filings, DSAR responses, board minutes circulated — require explicit user confirmation before any "send/file" tool runs. Hooks layer.
5. **CILEx/BSB equivalents.** Same duties apply; add a paralegal/barrister flag in the practice profile so the disclaimer language matches the regulator.

## Monetisation Surface

- **Free + OSS (distribution moat):** plugins, skills, marketplace manifest, OSCOLA validator, jurisdiction divergence reference docs, cold-start interviews. Distribution is the play.
- **Paid (separate `uk-legal-mcp` repo, out of scope here):** hosted MCP servers — `uk-legal`, `govuk`, `uk-due-diligence`, `whatdotheyknow`. Per-seat or per-call hosting + SLA + audit log.
- **Plugin paid tier (don't build yet).** No native paid-plugin mechanism exists in Claude Code / Cursor / Copilot / Codex marketplaces as of May 2026 [Claude Code plugin docs — retrieved 2026-05-21](https://code.claude.com/docs/en/discover-plugins), [Anthropic claude-plugins-official — retrieved 2026-05-21](https://github.com/anthropics/claude-plugins-official). Anthropic's marketplace is curated, free, and validation-gated; community marketplaces (claudemarketplaces.com, tonsofskills.com, agensi.io) are aggregators not payment rails. **Revenue stays at the MCP layer until a marketplace ships billing primitives.**

## Cross-Jurisdiction Portability

Architecture *is* portable; UK-specific content isn't (by design). Reusable harness pieces:

- Plugin/marketplace shape, `cold-start-interview`/`customize`/`matter-workspace` skill triad, practice-profile pattern, provenance tagging, irreversibility hooks — all jurisdiction-agnostic.
- MCP connectors are per-jurisdiction. An `ie-legal-mcp` (Irish Statute Book, BAILII-IE, CRO), `au-legal-mcp` (AustLII, ASIC, Federal Register), `nz-legal-mcp` (NZLII, Companies Office, PCO), `sg-legal-mcp` (Statutes Online, SAL), `ca-legal-mcp` (CanLII, OSC/SEDAR+, Corporations Canada) each plug in cleanly.
- Shared OSCOLA-style citation handling: needed in IE; AU uses AGLC, CA uses McGill, SG uses SAcLJ — not free, but the citation-parser scaffolding generalises.

## Plugin Marketplace Economics

State of play, May 2026:

- **Anthropic official marketplace** is auto-installed in Claude Code, free, automated validation [Claude Code marketplace docs — retrieved 2026-05-21](https://code.claude.com/docs/en/discover-plugins).
- **Community aggregators** (claudemarketplaces.com, agensi.io, tonsofskills.com, buildwithclaude.com, aitmpl.com) are catalogue/discovery only, no payment rails.
- **Cursor / GitHub Copilot / OpenAI Codex** consume Open Plugins via the spec — same constraint, no paid tier.
- **Implication:** ship plugins free, OSS, MIT-licensed for distribution; monetise via the hosted MCP server (auth, SLA, audit log, write-back integrations) which sits behind OAuth/API keys and can charge per seat or call. This is consistent with `uk-legal-mcp` being a separate repo.

## Recommended Backlog (Build column, ordered)

1. **Normalise `.mcp.json` across all 11 plugins** to the `employment-legal-uk` HTTPS shape. Kill placeholder `npx -y @modelcontextprotocol/server-uk-legal` references.
2. **Provenance + verify-with-lawyer skill-template invariant.** Lint check in `claude plugin validate` extension or CI.
3. **`jurisdiction` parameter** mandatory on every drafting/review skill across commercial, corporate, litigation, employment, privacy.
4. **`matter-workspace` audit-trail schema.** Frontmatter spec; CI lint.
5. **Irreversibility hook layer.** Standard `hooks/hooks.json` template gating send/file/circulate tool calls.
6. **ICO RSS adapter** (privacy, ai-gov) and **FCA register adapter** (regulatory, corporate, product). Public APIs, no licensing barrier.
7. **OSCOLA validator skill** (legal-clinic, law-student, all citation-emitting skills).
8. **UKIPO One IPO API connector** — pre-stub against the 2026 spec; activate when published.
9. **HMCTS court listings application** (litigation) — submit to data licensing programme.
10. **Scots / NI divergence reference docs** in `references/` — loaded by jurisdiction-tagged skills.
11. **SQE syllabus mapper skill** (law-student) — free top-of-funnel content.
12. **Portability scaffolding extraction** — pull jurisdiction-agnostic skill templates into a `references/_portable/` directory so IE/AU/NZ/SG/CA forks reuse them.

## Citations

- [Law Society — Generative AI: the essentials — retrieved 2026-05-21](https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials)
- [SRA — Compliance tips on AI — retrieved 2026-05-21](https://www.sra.org.uk/solicitors/resources/innovate/compliance-tips-for-solicitors/)
- [SRA — Risk Outlook: AI in the legal market — retrieved 2026-05-21](https://www.sra.org.uk/sra/research-publications/artificial-intelligence-legal-market/)
- [Claude Code plugin marketplace docs — retrieved 2026-05-21](https://code.claude.com/docs/en/discover-plugins)
- [anthropics/claude-plugins-official — retrieved 2026-05-21](https://github.com/anthropics/claude-plugins-official)
- [Claude Code Plugin Marketplace Guide (agensi.io) — retrieved 2026-05-21](https://www.agensi.io/learn/claude-code-plugin-marketplace-guide)
- [UKIPO One IPO transformation programme — retrieved 2026-05-21](https://www.gov.uk/government/publications/one-ipo-transformation-programme)
- [HMCTS data strategy — retrieved 2026-05-21](https://www.gov.uk/government/publications/hmcts-data-strategy)
- legislation.gov.uk — primary statute source, used directly via `uk-legal` MCP
