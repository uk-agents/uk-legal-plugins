# UK Legal Plugins for Claude Code

11 legal plugins built for UK jurisdiction — English & Welsh, Scottish, and Northern Irish law.

Works in any agent that supports the [Open Plugins spec](https://github.com/anthropics/claude-plugins-official): Claude Code, Cursor, GitHub Copilot, and Codex.

---

## Plugins

| Plugin | Practice area |
|--------|--------------|
| `employment-legal-uk` | Hires, terminations, worker classification (IR35/PSC), statutory leave, internal investigations |
| `commercial-legal-uk` | Contracts, NDAs, SaaS subscriptions under English contract law; Scots law divergences noted |
| `corporate-legal-uk` | M&A diligence, CA2006 compliance, board minutes, Companies House, PSC register, Takeover Code |
| `ip-legal-uk` | Trade marks (TMA 1994), copyright (CDPA 1988), patents (PA77/EPC), designs, trade secrets, UK IPO filings |
| `privacy-legal-uk` | UK GDPR / DPA 2018, DPIA, DSAR (1-month deadline), PECR, ICO gap analysis |
| `product-legal-uk` | Product launches, ASA/CAP Code, CMA, MHRA, Online Safety Act, DMCC Act 2024 |
| `regulatory-legal-uk` | FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HM Treasury, GOV.UK consultation tracking |
| `ai-governance-legal-uk` | AI use-case registry, impact assessments, ICO AI guidance, UK AI Act exposure, OSA 2023 |
| `litigation-legal-uk` | CPR deadlines, skeleton arguments, claim charts, LPP logs, Letters Before Action |
| `legal-clinic-uk` | SRA/BSB-supervised clinics, OSCOLA research, semester handoffs |
| `law-student-uk` | SQE1/SQE2 and LLB prep, OSCOLA citations, BAILII case briefs, Socratic drilling |

---

## Install

```bash
claude plugin install https://github.com/uk-agents/uk-legal-plugins
```

To install a single plugin:

```bash
claude plugin install https://github.com/uk-agents/uk-legal-plugins --plugin employment-legal-uk
```

---

## Agent compatibility

| Agent | Supported |
|-------|-----------|
| Claude Code | Yes |
| Cursor | Yes |
| GitHub Copilot | Yes |
| OpenAI Codex | Yes |

---

## Upstream

These plugins were contributed upstream to `anthropics/claude-for-legal` as PR #46. This repo exists as a standalone published product for UK legal professionals — it is kept in sync with the upstream contribution.

---

> Not affiliated with Anthropic. Built by the community as a UK-jurisdiction contribution to the Open Plugins ecosystem.
