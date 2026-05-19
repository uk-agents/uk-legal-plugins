# UK Legal Plugins

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

### Claude Code and coding agents

The repo is the marketplace. Add it first, then install plugins from it.

```bash
# Add the marketplace
claude plugin marketplace add uk-agents/uk-legal-plugins

# Install a single plugin
claude plugin install employment-legal-uk@uk-legal-plugins
```

Or browse the plugins via /plugins command in chat session. 

To remove:

```bash
claude plugin marketplace remove uk-legal-plugins  # removes marketplace and all its plugins
claude plugin uninstall employment-legal-uk         # removes a single plugin
```

### Claude Cowork

**Add the marketplace** (access all 11 plugins):
1. Personal plugins → Create plugin → Add marketplace → enter `uk-agents/uk-legal-plugins`
2. Go to Plugins → Personal and click `+` next to each plugin you want to install

**Upload a single plugin** (ZIP file):
1. Download the ZIP for the plugin you want from the [Releases page](https://github.com/uk-agents/uk-legal-plugins/releases)
2. In Cowork: Personal plugins → Create plugin → Upload plugin → select the ZIP file
3. The plugin appears in your personal plugins list once uploaded

---

## Getting started

After installing a plugin, run the cold-start interview in a Claude Code session:

```
/employment-legal-uk:cold-start-interview
```

Replace `employment-legal-uk` with whichever plugin you installed.

**Quick start (2 minutes):** records your role, practice setting, and jurisdictional footprint. Skills run immediately with sensible defaults.

**Full setup (10–15 minutes):** adds your real termination triggers, seed documents, escalation matrix, and integration checks. More thorough outputs.

The interview asks which at the start — you can upgrade any time with `--full` or re-run any section with `--redo`.

### What it builds

The interview writes a plain-text practice profile to:

```
~/.claude/plugins/config/uk-legal-plugins/[plugin-name]/CLAUDE.md
```

Every skill reads this file before doing anything. It survives plugin updates and can be edited directly.

### Shared company profile

The first plugin you configure saves your company name, industry, jurisdiction list, and escalation chain to a shared profile:

```
~/.claude/plugins/config/uk-legal-plugins/company-profile.md
```

Every other plugin reads this and skips those questions — so setup gets faster as you add more plugins.

### Connect a research tool (optional)

Pair with the [UK Legal MCP server](https://github.com/uk-agents/uk-legal-mcp) for live case law and legislation. Without it, every citation is tagged `[model knowledge — verify]`.

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
