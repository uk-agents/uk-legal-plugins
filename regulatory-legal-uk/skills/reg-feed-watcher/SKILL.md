---
name: reg-feed-watcher
description: Check UK regulatory feeds now and report what's new since the last check, filtered by your materiality threshold. Use when the user says "check the feeds", "what's new from UK regulators", "regulatory update", when running from the scheduled agent, or when manually pasting a UK regulatory development for classification and diff.
argument-hint: "[optional: --since DATE]"
---

# /reg-feed-watcher

1. Load `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → watchlist, materiality threshold, feed config.
2. Use the workflow below.
3. Pull each feed. Filter by materiality.
4. Output: what's new, categorised by materiality tier.

---

## Purpose

Pull the UK regulatory feeds. Filter by materiality. Output what's left. The filter is the value — unfiltered regulatory feeds are noise.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → watchlist, materiality threshold, feed configuration, digest output path (if set).

`references/source-catalog.md` (in this skill's directory) → curated catalogue of RSS/JSON/HTML sources across UK primary, UK secondary, EU/international, and aggregator categories. Use when configuring new sources or when the user's watchlist has coverage gaps (see Step 0).

## Workflow

### Step 0: Coverage check (before pulling)

Before running the pull, compare the watchlist + feed configuration in CLAUDE.md against `references/source-catalog.md`:

- Which UK regulators does the user care about per their watchlist?
- Which of those have zero or very few sources configured?

If there's an obvious gap — e.g., user is FCA-regulated but has no FCA feed configured; user is a data controller but has no ICO feed — surface it once at the top of the digest:

> **Coverage gap noticed:** Your watchlist includes [regulator], but no feed is configured. The source catalogue lists options for this regulator (see `references/source-catalog.md`). Want me to suggest additions? Run `/regulatory-legal-uk:cold-start-interview --redo` to update, or edit the config directly.

Don't nag the same gap repeatedly — if the user has explicitly said "skip Ofcom for now," respect that. Note state in CLAUDE.md so it sticks.

### Step 1: Pull

Pull from all configured feed tiers. Every installation has Tier 1. Tiers 2 and 3 are additive — use them if configured, skip if not.

**Tier 1 — Free UK feeds (always active)**

For each regulator in the watchlist, pull from the configured feed. Primary UK sources:

| Regulator | Primary feed | Notes |
|---|---|---|
| legislation.gov.uk | uk-legal MCP or `https://www.legislation.gov.uk/new.rss` | Returns new Acts and SIs; filter by `type=uksi` for statutory instruments |
| GOV.UK consultations | govuk MCP or `https://www.gov.uk/government/consultations.atom` | Returns all open and newly-closed consultations |
| FCA | `https://www.fca.org.uk/news/rss.xml` + email alerts | Policy statements, CPs, Dear CEO letters, enforcement notices |
| PRA | `https://www.bankofengland.co.uk/rss/publications` | PRA supervisory statements, CPs, PS |
| Bank of England | `https://www.bankofengland.co.uk/rss/publications` | FPC statements, MPC decisions, macroprudential rules |
| ICO | `https://ico.org.uk/global/rss-feeds/` | Enforcement decisions, guidance, code consultations |
| CMA | `https://www.gov.uk/cma.atom` + `https://www.gov.uk/government/organisations/competition-and-markets-authority.atom` | Market investigations, merger decisions, enforcement |
| Ofcom | `https://www.ofcom.org.uk/rss/news` | Enforcement, consultations, OSA guidance |
| HSE | `https://www.hse.gov.uk/news/index.htm` (no RSS — manual or web fetch) | ACOPs, enforcement bulletins |
| MHRA | `https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency.atom` | Guidance, device approvals, public health letters |
| HMRC | uk-legal MCP (`hmrc_search_guidance`) + HMRC technical guidance site | VAT notices, MTD updates, technical guidance |
| HM Treasury | `https://www.gov.uk/government/organisations/hm-treasury.atom` | Financial regulation consultations, FSMA updates |
| DSIT | `https://www.gov.uk/government/organisations/department-for-science-innovation-and-technology.atom` | AI/tech policy consultations |
| CAT | uk-legal MCP (case law search) | Judgments |
| UK Parliament (Bills) | uk-legal MCP (bills search) or `https://bills.parliament.uk/rss/publicbills.rss` | Bills, Committee reports |
| FRC | `https://www.frc.org.uk/news/rss` | Accounting standards, audit reforms |
| Gambling Commission | `https://www.gamblingcommission.gov.uk/news-action-and-statistics/news/rss` | LCCP updates |

**uk-legal MCP primary functions:**
- `legislation_search` — search legislation.gov.uk for new Acts and SIs by keyword, type, year
- `legislation_get_toc` — table of contents for a specific Act or SI
- `legislation_get_section` — read a specific section
- `bills_search_bills` / `bills_get_bill` — UK parliamentary bills and stages
- `hmrc_search_guidance` — HMRC guidance search
- `case_law_search` — Find Case Law (TNA) judgments
- `committees_search_evidence` — Select Committee evidence submissions

**govuk MCP primary functions:**
- `govuk_search` — search GOV.UK content
- `govuk_get_content` — fetch a specific GOV.UK page
- `govuk_get_organisation` — fetch all publications for an organisation (use for CMA, DSIT, HMT, HSE, MHRA, Ofcom)
- `govuk_get_section` — read a specific section of GOV.UK guidance

**No silent supplement.** If the feed pull returns few or no results for a regulator in the watchlist, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The feed check returned [N] items from [regulators hit]. Coverage appears thin for [regulator]. Options: (1) broaden the date window, (2) try a different feed or MCP, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the regulator's website before relying, or (4) stop here. Which would you like?"

**Source attribution.** Tag every citation and regulatory item:
- `[uk-legal MCP]` — from uk-legal MCP tool result
- `[govuk MCP]` — from govuk MCP tool result
- `[FCA RSS]` / `[ICO RSS]` / `[legislation.gov.uk RSS]` / `[GOV.UK feed]` — from that RSS/Atom feed
- `[web search — verify]` — from web search
- `[model knowledge — verify]` — from training data
- `[user provided]` — pasted in manually

**Secondary sources.** Tag items from law firm alerts, Legal Futures, Lexology, IAPP, or similar commentators as `[secondary source]` in addition to the feed-name tag. In the digest: "→ Trace to primary: [link to regulator site]." Do not classify a secondary-source item as "Always material" until the primary source is located.

**Tier 2 — Paid feeds (if configured)**

- **Westlaw UK / LexisNexis:** Query for UK regulatory updates since last check date, filtered to watchlist regulators.
- **Regulatory intelligence services (Compliant, Corlytics, TCC):** Same.

De-duplicate across tiers — the same document may appear in multiple sources. Prefer the richest source.

**Tier 3 — Manual entry**

If the user has pasted regulatory text or a summary: treat the pasted content as a single item, skip to Step 2 for classification, and record source as "manual entry." No feed pull required.

Record the check timestamp after pulling. Next scheduled run pulls from here forward.

### Step 2: Classify

Each item gets a materiality tier per `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`:

| UK item type | Match against threshold |
|---|---|
| FCA Policy Statement (final rules/Handbook changes) | Usually "always material" |
| PRA Supervisory Statement | Usually "always material" for PRA-regulated firms |
| FCA Consultation Paper (CP) / PRA CP | Usually "review-worthy" — and always log consultation closing date |
| FCA Dear CEO / Dear CFO letter | Always material if addressed to relevant firm type |
| Statutory Instrument (final, in force) | Usually "always material" if it amends regulations we operate under |
| GOV.UK public consultation | Review-worthy if in our sector; log closing date |
| FCA Discussion Paper (DP) / PRA DP | Review-worthy for strategy — log closing date |
| ICO enforcement action | Sector match → material; related-practice match → review-worthy; neither → FYI or skip |
| ICO code of practice consultation | Review-worthy if we process the relevant data type |
| CMA market investigation or Phase 2 inquiry | Sector match → material |
| Ofcom enforcement notice | Sector match → material |
| HSE enforcement bulletin | Sector match → material |
| Bill receiving Royal Assent | Review whether any provisions affect our sector |
| Select Committee report | Review-worthy if relevant sector; check for government response due |
| Regulator speech or blog post | FYI or skip per threshold |
| Court of Appeal / UKSC judgment (regulatory) | Review-worthy if relevant doctrine |
| CAT judgment | Sector match → material if competition/consumer |
| Post-Brexit divergence notice | Flag separately in all tiers — EU rule changed, UK rule may now differ |

**Consultation / Discussion Paper handling — specific:**

Pre-rule items (CPs, DPs, GOV.UK consultations, draft SIs) are distinct from final rules in one important way: they don't change the law, but they do carry closing dates and they signal the regulator's direction. Treat them as a separate branch:

- **Do not** classify a CP/DP as "always material" — the compliance impact is zero until final rules issue.
- **Do** classify as review-worthy if any of the consultation's issue areas touch the watchlist's always-material categories.
- **Do** log the consultation closing date to `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/consultation-tracker.yaml` with `decision: undecided` and the default consultation decision owner.
- **Do** include in the digest entry: "UK consultation. Closing date [date]. Route to `/regulatory-legal-uk:policy-diff` only as a pre-positioning analysis (no compliance obligation yet)."
- **Route to the consultation-tracker, not the gap-tracker.** Consultation-decision items are not compliance gaps.

**FCA Dear CEO / Dear CFO letter handling:**

Dear CEO/CFO letters are regulatory communications that, while not technically binding rules, represent strong regulatory expectations and are closely followed by the FCA in supervision. Classify as "always material" if the letter is addressed to the firm's sector. Log as a gap-surfacer `watch` item with `gap_type: watch` and note: "FCA Dear CEO letter — not a Handbook rule but treated as a regulatory expectation. Monitor for follow-on CP or supervisory action."

**Post-Brexit divergence tracking:**

When a UK feed item concerns retained EU law, check whether the equivalent EU rule has changed since the UK domesticated the provision. Flag:

> **Post-Brexit divergence check:** [UK rule] derives from [EU source]. The EU has [amended / not amended] this rule since UK domestication `[model knowledge — verify]`. If your firm operates in both jurisdictions, verify whether the EU version now differs.

**Consultation closing date handling:**

For every CP/DP/consultation classified at any tier above "skip":
- Extract closing date from the consultation document
- If consultation tracking is enabled in CLAUDE.md: append to `consultation-tracker.yaml` with `decision: undecided` and the default consultation decision owner
- Include closing date in the output entry

### Step 3: Enrich

For each item above FYI tier:

- One-line summary (what changed)
- Why it might matter here (the relevance hook — "this is about [practice you do]")
- Link to source
- Commencement date or consultation closing date if applicable
- FCA Handbook module or SI reference if applicable

Don't summarise FYI items individually — just count them.

## Output

The digest goes into the chat by default. **Also write it to a shareable file** whenever the output contains one or more items above FYI, unless the user's CLAUDE.md explicitly sets `Digest output → chat only`.

**File output behaviour:**

1. Look for `Digest output path` in CLAUDE.md. Default if unset: `~/regulatory-legal-uk-digests/reg-digest-YYYY-MM-DD.md`.
2. Create parent directories if needed.
3. Write the full digest as Markdown.
4. If a file already exists at the path for today, append a new section with a timestamped subheader.
5. After writing, tell the user: "Digest written to `<path>`. Share as-is, or convert to .docx with Pandoc: `pandoc <path> -o <path>.docx`."

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## UK Regulatory Feed Check — [date]

**Period:** [last check] to [now]
**Feeds checked:** [list active tiers — e.g., "uk-legal MCP, govuk MCP, FCA RSS, ICO RSS, legislation.gov.uk RSS"]
**Items found:** [N] total

### Bottom line

[N gaps need action by [date] — top 3: X, Y, Z]

### 🔴 Always material

**[Regulator] — [Title]** `[source tag]`
[One-line summary]. [Relevance hook]. In force from [date] / Closing [date].
[Link]
→ Recommend: run `/regulatory-legal-uk:policy-diff` against [likely affected policy]

[repeat for each]

### 🟡 Review-worthy

**[Regulator] — [Title]** `[source tag]`
[One-line]. [Relevance]. [Closing date if a consultation].
[Link]

[Consultations: include "📝 Consultation closing: [date] — response decision pending" if consultation tracking enabled]

[Post-Brexit divergence items flagged separately here]

[repeat]

### 📝 FYI

[N] items — [expandable list of titles + links, no summaries]

---

**Last check updated to:** [timestamp]
**Consultation tracker:** [N] open consultations with undecided response decisions — run `/regulatory-legal-uk:comments` to review

---

**Verify citations before relying on them.** UK regulatory citations here were AI-generated and have not been checked against a primary source. Before acting on any rule, guidance, or enforcement action above, confirm it against legislation.gov.uk, the FCA Handbook (handbook.fca.org.uk), or the issuing authority's website — check accuracy, commencement date, and current status. Citations are in OSCOLA format where applicable; verify SI numbers and Act section numbers. Source tags on each item (e.g., `[uk-legal MCP]`, `[model knowledge — verify]`) show where the citation came from.
```

## Config-dependent fallbacks

- **Watchlist empty:** stop and say "The watchlist in your configuration is empty. Run `/regulatory-legal-uk:cold-start-interview --redo` or edit `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` and add at least one UK regulator."
- **Materiality threshold empty:** fall back to the default tiers and append: "This output used the default materiality tiers because your configuration doesn't have custom thresholds set. Tune them with `/regulatory-legal-uk:cold-start-interview --redo`."
- **Feed configuration empty:** run uk-legal MCP + govuk MCP only and append: "This output used only the free uk-legal and govuk MCP feeds because your configuration doesn't list direct RSS or paid feeds. Add feeds with `/regulatory-legal-uk:cold-start-interview --redo`."

If nothing above FYI: "All quiet. [N] FYI items, nothing needing attention."

## Handoff

- **To policy-diff:** Any "always material" item with a likely policy impact → offer to run the diff.
- **To gap-surfacer:** If a diff finds a gap → tracked.
- **To consultation-tracker:** Any consultation/CP/DP classified above "skip" → consultation closing date logged automatically if tracking is enabled.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- Read every item in full. It classifies and enriches; deep reading is for the items that survive the filter.
- Change the materiality threshold. If the filter is wrong, edit the config.
- Require paid feeds. Free uk-legal MCP + govuk MCP + regulator RSS are the baseline.
