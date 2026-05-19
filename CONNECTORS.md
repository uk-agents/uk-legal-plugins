# Adding a Connector

The plugins are at their best when connected to authoritative sources. If you build or operate a legal data source, research tool, CLM, DMS, eDiscovery platform, or practice management system, we want your MCP connector in the suite.

## What makes a good legal MCP connector

- **Remote MCP server over HTTPS** with OAuth or API-key auth (streamable HTTP or SSE transport)
- **Read-heavy tools** — search, fetch, list. Write tools (create, send, file) need an explicit confirmation prompt on the client side; say so in your tool descriptions.
- **Provenance in results** — return the source, date retrieved, and a citation-ready identifier. The plugins tag every cite by source; your connector should make that possible.
- **No instruction-like content in results** — the plugins treat retrieved content as data, not commands. If your tool results include metadata or system notes, mark them clearly so they don't look like embedded directives.
- **Rate limits and errors that degrade gracefully** — the plugins have a fallback for when a connector isn't responding; a clean error is better than a timeout.

## How to submit

1. Publish your MCP server and document its tools, auth flow, and data coverage.
2. Open a PR adding your server to the relevant plugin's `.mcp.json` with the URL, auth method, and a one-line description of what it gives Claude.
3. Include a note on which practice areas / plugins it's most useful for.
4. We'll test against the plugin workflows and merge. Connectors that pass the retrieval-quality and injection-resistance checks go in the default `.mcp.json`; others get documented in the plugin README for users to add themselves.

## Current connectors

Connectors shipped in the default `.mcp.json` of each plugin:

| Connector | Plugins |
|---|---|
| **UK Legal MCP** | all 11 |
| **Slack** | all 11 |
| **Google Drive** (`gdrive`) | all 11 |
| **Descrybe** | legal-clinic-uk, ip-legal-uk, law-student-uk |
| **Definely** | commercial-legal-uk, corporate-legal-uk |
| **iManage** | commercial-legal-uk, corporate-legal-uk |
| **Solve Intelligence** | corporate-legal-uk, ip-legal-uk |
| **TopCounsel** | commercial-legal-uk, corporate-legal-uk, litigation-legal-uk |
| **Box** | corporate-legal-uk |
| **Ironclad** | commercial-legal-uk |
| **DocuSign / DocuSign CLM** | commercial-legal-uk |
| **Everlaw** | litigation-legal-uk |
| **Aurora** | litigation-legal-uk |
| **Linear** | product-legal-uk |
| **Atlassian (Jira)** | product-legal-uk |
| **Asana** | product-legal-uk |

See the `.mcp.json` in each plugin directory for the authoritative list.

**UK Legal MCP** includes Find Case Law (TNA), BAILII, and legislation.gov.uk — covering E&W judgments from 2001, Scottish and NI case law, and the full UK statute book. It is the primary research connector for all 11 plugins.

## Wanted connectors

These would make specific plugins significantly more useful. If you build or operate one, see "How to submit" above.

- **IP management systems** (Anaqua, Clarivate IPfolio, AppColl, Patrix, Alt Legal, FoundationIP) — full docket sync for `ip-legal-uk` portfolio tracking
- **EPO Open Patent Services (OPS)** — free API (4 GB/month, registration required) covering UK IPO, EP, and 100+ national offices via INPADOC. Portfolio lookups by applicant name. Best current free option for `ip-legal-uk` until the UKIPO One IPO API ships.
- **UKIPO One IPO API** (in development, targeting 2026) — View rights portfolio, Renewals, and IP Register APIs for UK patents and trade marks. Will be the authoritative programmatic source for `ip-legal-uk` portfolio and deadline tracking.
- **UK IPO Trade Mark Register** — trade mark status and renewal deadlines for `ip-legal-uk`. Web access free; programmatic access via UKIPO One IPO API when available.
- **Jira / Linear / Asana for OSS requests** — `ip-legal-uk` OSS clearance can monitor and respond to incoming tickets
- **Thomson Reuters** (Practical Law, Westlaw UK) — research and drafting for every plugin. Requires subscription.
- **SS&C Intralinks / Datasite** — VDR access for `corporate-legal-uk` diligence
- **Relativity / Everlaw beyond read** — eDiscovery workflow for `litigation-legal-uk`
- **SRA / BSB CPD tracker** — `law-student-uk` and qualification tracking. No official SRA/BSB API exists (the SRA moved to an outcomes-based model in 2016 with no central submission portal). A connector here would implement the SRA five-step reflection framework as a structured self-assessment tool and track BSB hours (12/year established practitioners).
- **HMCTS e-filing** — with a hard irreversibility gate. HMCTS operates an online civil money claims and probate service; broader e-filing API access is part of the HMCTS data programme.
- **HMCTS court listings (licensed)** — HMCTS is making hearing lists and outcome registers available to licensed recipients. Would give `litigation-legal-uk` court calendar and docket data comparable to Trellis. Requires application to HMCTS data licensing programme.
- **Global AI Regulation Tracker** (techieray.com/GlobalAIRegulationTracker) — jurisdiction-tagged AI regulation tracking with structured API. Curated, verified, multi-jurisdiction. Primary-source-adjacent feed for `ai-governance-legal-uk` and `regulatory-legal-uk`.
- **Regulatory primary sources** — a connector to official UK registers (legislation.gov.uk, FCA register, ICO register, Companies House, GOV.UK consultation tracker) that normalises and caches responses. legislation.gov.uk and GOV.UK already have free APIs; a unified connector wrapping them would be high value.

## Questions

Open an issue on this repo. For partnership or integration questions, see the contact on each plugin's README.
