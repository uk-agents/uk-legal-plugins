# UK Regulatory Source Catalogue

A starting catalogue for the reg-feed-watcher. The cold-start interview configures
which sources to watch; this catalogue provides the options. URLs verified as of
**May 2026** — feed URLs change; verify if a source stops returning results.

**How to read this catalogue:**
- **Format** — what the feed returns: JSON API (structured, best), RSS/Atom (semi-structured, good), HTML page (needs scraping or change detection), Email only (requires Gmail/Outlook MCP).
- **Tier** — *Primary* means the UK regulator or official publisher itself; *Secondary* means a commentator, aggregator, or law firm summarising primary sources. Always trace a secondary source back to the primary before treating it as authoritative.
- **Auth** — None means open; Key means a free-but-registered API key; Paid means a subscription.
- **Notes** — any gotchas (rate limits, feed retirement, discovery steps).

Sources flagged ⚠️ have been reported as unreliable, subject to change, or without a confirmed RSS URL — verify before configuring.

---

## UK Primary — Legislation and Parliamentary

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| legislation.gov.uk — New Legislation | `https://www.legislation.gov.uk/new.rss` | RSS | All new UK Acts, SIs, SSIs (Scotland), WSIs (Wales), NISRs (NI) | None | Filter by `type=uksi` for SIs only. The uk-legal MCP `legislation_search` gives more structured results. |
| legislation.gov.uk — SI search API | `https://www.legislation.gov.uk/search?type=uksi&sort=new` | HTML/JSON | Statutory Instruments by type and date | None | Use via uk-legal MCP `legislation_search` for structured search; direct URL for browsing. |
| UK Parliament Bills | `https://bills.parliament.uk/rss/publicbills.rss` | RSS | Public Bills before Parliament | None | Also available via uk-legal MCP `bills_search_bills`. Covers both Commons and Lords bills. |
| UK Parliament Hansard | uk-legal MCP | API | Debates, Written Statements, Oral Questions | None | Use `parliament_search_hansard` via uk-legal MCP. Full text available. |
| UK Parliament Select Committees | uk-legal MCP | API | Committee inquiries, evidence, reports | None | Use `committees_search_committees` and `committees_search_evidence` via uk-legal MCP. |
| Written Ministerial Statements | `https://www.parliament.uk/business/publications/written-questions-answers-statements/written-statements/?page=1` | HTML | Ministerial statements (can change policy without a formal consultation) | None | ⚠️ No direct RSS. Monitor via uk-legal MCP Hansard search or govuk MCP. |
| House of Lords Secondary Legislation Scrutiny Committee | `https://www.parliament.uk/business/committees/committees-a-z/lords-select/secondary-legislation-scrutiny-committee/` | HTML | Scrutiny of SIs; flags "interesting" SIs | None | ⚠️ No public RSS. Important for catching problematic SIs before they come into force. |

---

## UK Primary — Financial Regulation

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| FCA News | `https://www.fca.org.uk/news/rss.xml` | RSS | Policy statements, CPs, DPs, Dear CEO letters, enforcement notices, press releases | None | Email alerts at `fca.org.uk/newsletters-emails-sign-up` are the supported channel; RSS available. |
| FCA Regulatory Sandbox / Innovation | `https://www.fca.org.uk/innovation/rss.xml` | RSS | Regulatory sandbox, InnovateFinance | None | Narrower — only relevant for fintech/innovation teams. |
| PRA Publications | `https://www.bankofengland.co.uk/rss/publications` | RSS | PRA supervisory statements, CPs, PS, policy statements | None | Shared with Bank of England publications; filter by "Prudential Regulation Authority" in the feed or web UI. |
| Bank of England Publications | `https://www.bankofengland.co.uk/rss/publications` | RSS | FPC statements, MPC minutes/reports, working papers, financial stability reports | None | Broad feed — filter by publication type. |
| FCA Handbook | `https://www.handbook.fca.org.uk/` | HTML (no RSS) | FCA Handbook: COBS, SYSC, MAR, EMIR, MiFIR, UK-GDPR provisions | None | ⚠️ No RSS for Handbook changes. Track via FCA news RSS (Policy Statements announce Handbook changes) or monitor instrument-level pages. Handbook update instruments (HUIs) are the primary mechanism. |
| PRA Rulebook | `https://www.prarulebook.co.uk/` | HTML (no RSS) | PRA rules for banks, insurers, designated investment firms | None | ⚠️ No RSS. Changes announced via PRA publications RSS. |

---

## UK Primary — Data Protection and Privacy

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| ICO News | `https://ico.org.uk/global/rss-feeds/` | RSS (multiple) | Enforcement decisions, news, guidance, blog | None | Separate feeds for news, enforcement, blog. Enforcement list also at `ico.org.uk/action-weve-taken/enforcement/`. |
| ICO Consultations | `https://ico.org.uk/about-the-ico/consultations/` | HTML | Codes of practice consultations, guidance consultations | None | ⚠️ No dedicated RSS. Covered by main ICO RSS. |
| NCSC | `https://www.ncsc.gov.uk/section/information-for/general-public/news` | HTML + RSS option | Cyber guidance, alerts | None | Check page for current RSS link. |

---

## UK Primary — Competition and Consumer

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| CMA (GOV.UK feed) | `https://www.gov.uk/government/organisations/competition-and-markets-authority.atom` | Atom | Market investigations, merger decisions, enforcement, guidance | None | Also accessible via govuk MCP `govuk_get_organisation`. |
| CAT Judgments | uk-legal MCP `case_law_search` | API | Competition Appeal Tribunal judgments | None | CAT publishes via TNA Find Case Law; use uk-legal MCP for structured search. |
| ASA Rulings | `https://www.asa.org.uk/news/rss.asp` | RSS | Advertising standards rulings | None | Relevant for consumer-facing businesses with advertising compliance obligations. |

---

## UK Primary — Communications and Online Safety

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| Ofcom News | `https://www.ofcom.org.uk/rss/news` | RSS | Consultations, enforcement, OSA guidance, spectrum | None | Broad feed. Online Safety Act guidance is high priority for relevant firms. |
| Ofcom Online Safety | `https://www.ofcom.org.uk/online-safety` | HTML | OSA codes, guidance, categorisation decisions | None | ⚠️ No separate OSA RSS. Monitor via main Ofcom feed. |

---

## UK Primary — Health and Safety, Medicines, and Product Safety

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| HSE News | `https://www.hse.gov.uk/news/index.htm` | HTML | ACOPs, enforcement bulletins, consultations | None | ⚠️ No reliable RSS located. Monitor via govuk MCP or manual entry. |
| MHRA Publications | `https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency.atom` | Atom | Guidance updates, device approvals, public health letters | None | Accessible via govuk MCP `govuk_get_organisation`. |
| OPSS (Product Safety) | `https://www.gov.uk/government/organisations/office-for-product-safety-and-standards.atom` | Atom | Product safety updates, recall notices | None | Accessible via govuk MCP. |

---

## UK Primary — Tax and Customs

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| HMRC Technical Guidance | uk-legal MCP `hmrc_search_guidance` | API | VAT notices, Making Tax Digital, technical guidance | None | Best accessed via uk-legal MCP `hmrc_search_guidance` for structured search. |
| HMRC VAT Rate lookup | uk-legal MCP `hmrc_get_vat_rate` | API | Current UK VAT rates by category | None | Real-time via uk-legal MCP. |
| HMRC MTD Status | uk-legal MCP `hmrc_check_mtd_status` | API | Making Tax Digital status by tax type | None | Real-time via uk-legal MCP. |
| HMRC Policy Papers | `https://www.gov.uk/government/organisations/hm-revenue-customs.atom` | Atom | Policy consultations, guidance | None | Accessible via govuk MCP. |

---

## UK Primary — Financial Reporting and Audit

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| FRC News | `https://www.frc.org.uk/news/rss` | RSS | Accounting standards, audit reforms, enforcement | None | Verify current RSS URL at `frc.org.uk/news`. |
| FRC Consultations | `https://www.frc.org.uk/about-the-frc/consultation` | HTML | FRS consultations, audit reform consultations | None | ⚠️ No dedicated RSS. Covered by main FRC feed. |

---

## UK Primary — Gambling

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| Gambling Commission News | `https://www.gamblingcommission.gov.uk/news-action-and-statistics/news/rss` | RSS | LCCP updates, licence conditions, enforcement | None | Verify RSS URL on site. |

---

## UK Primary — GOV.UK Cross-Cutting

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| GOV.UK All Consultations | `https://www.gov.uk/government/consultations.atom` | Atom | All open and recently-closed UK government consultations | None | Broad. Filter client-side by department or keyword. Best processed via govuk MCP `govuk_search` for structured results. |
| GOV.UK Policy Papers | `https://www.gov.uk/government/publications?publication_filter_option=policy-papers.atom` | Atom | Government policy papers | None | Includes command papers (Cm), White Papers, Green Papers. |
| GOV.UK Press Releases | `https://www.gov.uk/search/all.atom?keywords=&content_store_document_type=press_release` | Atom | Government press releases across all departments | None | Broad — filter by department. |
| HM Treasury | `https://www.gov.uk/government/organisations/hm-treasury.atom` | Atom | Financial regulation consultations, FSMA amendments, FSCS, FMI updates | None | Accessible via govuk MCP. |
| DSIT | `https://www.gov.uk/government/organisations/department-for-science-innovation-and-technology.atom` | Atom | AI/tech policy consultations, data regulation | None | Accessible via govuk MCP. |

---

## EU / International (for Post-Brexit Divergence Tracking)

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| EDPB News | `https://www.edpb.europa.eu/news/news_en` | RSS | GDPR guidelines, opinions, enforcement summaries — for tracking EU divergence from UK GDPR | None | Compare against ICO positions for UK–EU GDPR divergence. |
| ESMA News | `https://www.esma.europa.eu/press-news/esma-news` | RSS | EU securities regulation — for tracking MiFIR/EMIR divergence from UK versions | None | Compare against FCA Handbook UK MiFIR/EMIR rules. |
| European Commission Press Corner | `https://ec.europa.eu/commission/presscorner/` | RSS + email | DSA, DMA, AI Act, DORA implementing acts | None | Relevant for UK firms with EU presence tracking post-Brexit regulatory divergence. |
| EUR-Lex (OJ) | `https://eur-lex.europa.eu/` | Webservice + RSS by search | Official Journal publications | Key (free) | Use to track EU secondary legislation that UK may need to diverge from or align with. |
| OECD AI Policy Observatory | `https://oecd.ai/en/` | HTML + newsletter | National AI policies, OECD guidance | None | Relevant for tracking international AI regulation alongside UK DSIT consultations. |

---

## Secondary / Aggregators

**Treat content from these sources as leads, not authority.** A secondary source saying "the FCA issued X" means: find X on fca.org.uk, then rely on it. Tag items from these feeds as `[secondary source]` in the digest.

| Source | Feed URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| UK Regulatory Radar (Hogan Lovells) | `https://www.hoganlovells.com/en/rss` | RSS (per practice) | UK and global regulatory client alerts | None | Per-practice sub-feeds available. |
| Linklaters Regulate — Blog | `https://www.linklaters.com/en/insights/blogs/regulateuk/rss` | RSS | UK financial services regulation | None | High quality UK finreg commentary. |
| Allen & Overy Regulatory Insights | ⚠️ Check firm website | RSS/HTML | UK regulatory alerts | None | Verify current RSS at allenovery.com. |
| Freshfields Regulatory Insights | ⚠️ Check firm website | RSS/HTML | UK and EU regulatory | None | Verify current RSS at freshfields.com. |
| Lexology | `https://www.lexology.com/account/rss` | RSS (customisable) | Aggregated UK and global firm alerts by topic/jurisdiction | Account (free) | Build topic+jurisdiction feeds for UK financial services, UK data protection, etc. |
| Legal Futures | `https://www.legalfutures.co.uk/feed` | RSS | Legal tech, SRA regulation, legal services regulation | None | Relevant for law firms tracking SRA regulatory changes. |
| IAPP Daily Dashboard | `https://iapp.org/rss/daily-dashboard/` | RSS | Global privacy + AI governance news, includes UK ICO | None (some items paywalled) | High signal-to-noise for data protection and privacy teams. |
| FinRegEU | `https://www.finregeu.com/feed/` | RSS | EU and UK financial regulation | None | Good for post-Brexit EU/UK financial services divergence tracking. |
| TLT Compliance Made Simple | ⚠️ Check TLT website | RSS/email | UK financial and regulatory updates | None | Verify at TLT.com. |
| UK Technology Law Alliance | ⚠️ Check website | RSS/email | UK tech law, data protection, AI regulation | None | Aggregated UK tech law perspectives. |

---

## Sources without feeds (need web monitoring or email subscription)

Some important UK sources don't publish feeds or their RSS is unreliable.
Monitoring them requires either:
- govuk MCP periodic search
- Email newsletter forwarding (requires Gmail/Outlook MCP integration)
- Manual checking via the reg-feed-watcher "manual entry" path

| Source | URL | Notes |
|---|---|---|
| FCA Handbook changes | `https://www.handbook.fca.org.uk/` | No RSS for Handbook changes; track via FCA news RSS (Policy Statements announce Handbook updates) |
| PRA Rulebook changes | `https://www.prarulebook.co.uk/` | No RSS; changes announced via PRA publications RSS |
| HSE news | `https://www.hse.gov.uk/news/` | No confirmed RSS; use govuk MCP or manual entry |
| ICO detailed enforcement | `https://ico.org.uk/action-weve-taken/enforcement/` | Covered by main ICO RSS; detailed enforcement action pages are HTML |
| CAT judgments (non-MCP) | `https://www.catribunal.org.uk/judgments` | Use uk-legal MCP case_law_search as primary |
| Written Ministerial Statements | `https://www.parliament.uk/wms` | No RSS; use uk-legal MCP Hansard search |
| House of Lords SLSC reports | `https://committees.parliament.uk/committee/255/secondary-legislation-scrutiny-committee/` | No RSS; check weekly via committees MCP or manual |

---

## Suggested UK starter packs

**FCA-regulated financial services firm (UK only):**
FCA RSS, PRA RSS/email, Bank of England RSS, legislation.gov.uk new.rss (filter: financial services SIs), GOV.UK HM Treasury feed, uk-legal MCP (legislation, bills, committees), ICO RSS, Linklaters Regulate blog, IAPP.

**Data-heavy business (UK GDPR focus):**
ICO RSS, legislation.gov.uk new.rss, GOV.UK DSIT feed, GOV.UK consultations (filter: data protection), EDPB RSS (for UK–EU divergence), uk-legal MCP, IAPP Daily Dashboard, govuk MCP.

**Online/digital platform (Online Safety Act focus):**
Ofcom RSS, CMA feed, ICO RSS, DSIT GOV.UK feed, GOV.UK consultations, uk-legal MCP (bills — Digital Markets/OSA-related), legislation.gov.uk new.rss, Lexology (UK tech law), govuk MCP.

**Broad UK in-house regulatory team:**
legislation.gov.uk new.rss, GOV.UK all consultations feed, uk-legal MCP, govuk MCP, FCA RSS, ICO RSS, CMA feed, Ofcom RSS, HM Treasury feed, HMRC guidance (uk-legal MCP), Lexology (UK, customised), IAPP.

**Post-Brexit divergence tracker (UK + EU presence):**
All UK primary feeds above + EDPB RSS, ESMA news, European Commission Press Corner, EUR-Lex OJ feed. Flag every UK feed item against the equivalent EU rule.

---

## Adding a source

To add a UK source that isn't in this catalogue:
1. Find a feed URL (try `/rss`, `/feed`, `/news.rss`, or view page source for `<link rel="alternate" type="application/rss+xml">`).
2. Validate it returns XML/JSON in a browser or with `curl`.
3. Add to the user's regulatory-legal-uk CLAUDE.md under **Feed configuration → Direct regulator feeds**, with: source name, URL, format, what it covers.
4. If no feed exists, add it under **Sources without feeds** and decide: govuk MCP periodic search, email, or change detection.
5. Update this catalogue with the new source so future cold-starts can find it.
