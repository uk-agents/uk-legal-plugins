# Skill gaps and design (Phase B)

## Why this exists

ChatGPT dogfeed of the v2 `uk-legal-mcp` build (now defunct) surfaced workflow failures the routing-probe data couldn't see. Per the audit recorded in `/home/bch/.claude/plans/scalable-tickling-meadow.md`:

- 140 skills exist across 11 plugins
- All 5 dogfeed-failure workflows have **ZERO or PARTIAL coverage**
- Best reference skill: `regulatory-legal-uk:reg-feed-watcher` (MCP-native, explicit tool names, "no silent supplement" anti-fabrication discipline, source-tagged outputs)

This doc specifies 5 new skills to write that close the gaps. Each follows the reg-feed-watcher template. Authored via Anthropic's `skill-creator` skill (the canonical one at `~/.claude/skills/skill-creator/`).

Branch: `feat/skill-gaps` off `main` of `uk-legal-plugins` (at `/home/bch/company/skills-uk/uk-legal-plugins`).

Distribution: free, public, single repo. Per `distribution-strategy.md` (Phase C1 — locked).

## The reference template — what makes reg-feed-watcher work

Read `regulatory-legal-uk/skills/reg-feed-watcher/SKILL.md` before authoring new skills. Five characteristics:

1. **Trigger description is "pushy"** — "USE WHEN the user says 'check the feeds', 'what's new from UK regulators'..." Concrete user phrases, not abstract intent.

2. **MCP tools named verbatim in prose** — "`legislation_search`, `legislation_get_toc`, `legislation_get_section`" — not "search legislation" or "the legislation tool." The agent matches the actual tool names; named-verbatim wins.

3. **Source-tagged outputs** — every claim in the skill's output is tagged `[uk-legal MCP]`, `[govuk MCP]`, `[model knowledge — verify]`, or `[FEED — Y/M/D]`. The tags propagate to the agent's response so the human reader can see provenance.

4. **"No silent supplement" clause** — explicit anti-fabrication: *"If a query to a configured research tool returns few or no results... do NOT manufacture citations from web search or training data."* Tightens against Obs 183 (confabulation) and Obs 190 (bypass).

5. **Tier structure** — Tier 1 (must-have authoritative sources via MCP), Tier 2 (govuk MCP), Tier 3 (broader feeds). The skill teaches WHEN to escalate sources.

Each new skill below adopts all five characteristics.

## Anti-fabrication clause (re-use across all 5 skills)

Every skill in this batch includes this paragraph verbatim near the top of its instructions:

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

## Skill B1 — `find-member-contribution`

### Workflow chain
`parliament_find_member(name)` → get `member_id` → `parliament_search_hansard(query=topic_or_bill_name)` → identify the right debate → `parliament_get_debate_contributions(debate_ext_id, member_id=...)` → extract verbatim contribution text.

### Plugin location
Shared — install in both `legal-clinic-uk/skills/find-member-contribution/` and `regulatory-legal-uk/skills/find-member-contribution/`. Symlink-or-duplicate, decide at author time.

### SKILL.md frontmatter draft

```yaml
---
name: find-member-contribution
description: >
  Retrieve what a named member of either House said in a specific Hansard debate.
  Use this skill whenever the user asks "what did <peer/MP> say about <topic>",
  "find <member>'s contribution to the <bill> debate", "did <name> speak on
  <date>", or "quote <name>'s speech on <subject>". This skill must be used
  for any peer-or-MP-specific Hansard query — text-searching Hansard by member
  name returns unrelated debates and is the most common failure mode.
---
```

### Instructions outline

1. **Get the member_id first.** Call `parliament_find_member(name)`. If multiple members match (e.g. "Lord Smith" matches several peers), ask the user to disambiguate. If `parliament_find_member` returns empty, the name may be wrong — ask the user for the full title.

2. **Find the debate.** Call `parliament_search_hansard(query=...)` with the BILL NAME or TOPIC the user mentioned — NOT the member's name. The search returns up to 4 debates with `debate_ext_id`. If the user gave a specific date, filter by that date (`filters.date`).

3. **Retrieve contributions.** Call `parliament_get_debate_contributions(debate_ext_id, member_id=<from step 1>)`. This filters the debate's contributions list by the member's ID. Returns the verbatim text with `column_ref`, `sitting_date`, `house`.

4. **Surface the contribution to the user with provenance tags:**
   - `[uk-legal MCP — Hansard]` for the text
   - `[Hansard column: HL Deb vol N col M (date)]` for the citation
   - If multiple contributions in the same debate, list them in column order.

5. **Anti-fabrication clause** (reuse the shared paragraph).

### Test prompts (3)
- "What did Lord Pannick say about the Renters' Rights Bill in the Lords on 14 October 2025?"
- "Find Baroness Hale's contribution to the Online Safety Bill Lords debates."
- "Did Hilary Benn speak on the Northern Ireland Troubles legacy bill?"

## Skill B2 — `find-case-by-party-verify`

### Workflow chain
`case_law_search(query="party names")` → extract `neutral_citation` + `tna_uri` from the first ranked result → `citations_resolve(neutral_citation)` to verify before reporting.

### Plugin location
`law-student-uk/skills/find-case-by-party-verify/` and `litigation-legal-uk/skills/find-case-by-party-verify/`.

### SKILL.md frontmatter draft

```yaml
---
name: find-case-by-party-verify
description: >
  Find a UK court judgment by party names and verify its neutral citation
  before citing it to the user. Use whenever the user asks "find <X v Y>",
  "get me the citation for <case>", "what's the neutral citation for the
  <case name>", "is there a case called <name>", or pastes a partial case
  reference. This skill verifies the case exists in TNA Find Case Law BEFORE
  reporting the citation — prevents the "plausible-looking but wrong"
  citation failure that happens when an agent formats from training data.
---
```

### Instructions outline

1. **Search TNA Find Case Law.** Call `case_law_search(query="<party names>")`. Returns up to 50 judgments with `neutral_citation`, `title`, `court`, `sitting_date`, `tna_uri`.

2. **Pick the right judgment.** If the user named both parties, look for an exact title match. If multiple courts have heard the case (e.g. CA + UKSC), list them in court-of-last-resort order. If no result, ask the user for a year or court hint.

3. **Verify the citation.** Call `citations_resolve(neutral_citation=...)` for the top candidate. If it resolves, report to the user with `[uk-legal MCP — TNA Find Case Law]` tag. If it does NOT resolve, surface the verification failure — the case may be from a court not yet in TNA's corpus, or the neutral citation may be unstable.

4. **Surface to the user:**
   - Title (italicised in citation form: *X v Y*)
   - Neutral citation
   - Court + sitting date
   - `tna_uri` for the agent to drill into via `judgment_get_header` / `judgment_get_paragraph` if needed

5. **Anti-fabrication clause** (shared paragraph).

### Test prompts (3)
- "Find Smith v HMRC dealing with VAT recovery and give me the neutral citation."
- "What's the neutral citation for Donoghue v Stevenson?" (note: pre-2001, may not be in TNA)
- "I need the case on the IR35 status of Sky News presenters in the Upper Tribunal."

## Skill B3 — `oscola-build-citation`

### Workflow chain
`citations_resolve(input)` FIRST → only if the source resolves → construct the OSCOLA citation. Refuse to format unresolved sources.

### Plugin location
`law-student-uk/skills/oscola-build-citation/` and `legal-clinic-uk/skills/oscola-build-citation/`.

### SKILL.md frontmatter draft

```yaml
---
name: oscola-build-citation
description: >
  Construct an OSCOLA citation for a UK case, statute, or Hansard reference
  AFTER verifying the source exists via uk-legal MCP. Use whenever the user
  asks to "cite <source> in OSCOLA", "give me the OSCOLA citation for", "format
  this as OSCOLA", or pastes a partial citation. This skill verifies first and
  formats second — preventing the most common citation fabrication route where
  an agent formats plausible-looking fields without confirming the source
  actually exists.
---
```

### Instructions outline

1. **Identify the source type** (case / statute / SI / Hansard / journal).

2. **Verify FIRST.** Call `citations_resolve(input=...)` with whatever identifier the user gave (neutral citation, statute short title, Hansard column). Get back a structured source record or "not_found" / "ambiguous".

3. **Refuse if not resolved.** If `citations_resolve` returns `not_found`, do NOT proceed to format. Tell the user: "I can't verify <input> exists in the UK legal record. Could you share the source URL, or check the citation for typos?" If `ambiguous`, list the candidates and ask the user to pick.

4. **Format only when resolved.** Build the OSCOLA citation from the resolved source's authoritative fields — not the user's input fields. If the user gave year 1993 and the resolved record says 1994, use 1994 and note the discrepancy.

5. **Tag the output:**
   - Citation text
   - `[uk-legal MCP — verified]` tag
   - The resolved source URI for traceability

6. **Anti-fabrication clause** (shared).

### Test prompts (3)
- "Format this as OSCOLA: R v Brown, 1993, House of Lords, [1994] 1 AC 212."
- "Give me the OSCOLA citation for section 21 of the Housing Act 1988."
- "Cite Lord Pannick's contribution to the Renters' Rights Bill Lords debate in OSCOLA."

## Skill B4 — `statute-amendments-trace`

### Workflow chain
`legislation_search(statute_name)` → `legislation_get_toc` → cross-reference `bills_search_bills(query=statute_short_title)` for pending amendments → optionally `parliament_search_hansard` for the bill debates.

### Plugin location
`regulatory-legal-uk/skills/statute-amendments-trace/` and `commercial-legal-uk/skills/statute-amendments-trace/`.

### SKILL.md frontmatter draft

```yaml
---
name: statute-amendments-trace
description: >
  Trace the current state of a UK Act including in-force amendments AND any
  pending bills that would amend it. Use whenever the user asks "is <Act>
  current", "what's the latest version of <Act>", "have any bills amended
  this", "what's pending for <Act>", or "what changes are proposed to <Act>".
  Statutes are living documents — a citation without amendment-status risks
  citing repealed or superseded text.
---
```

### Instructions outline

1. **Locate the statute.** Call `legislation_search(query="<title>")`. If user gave a partial title, narrow with year if known.

2. **Get the TOC.** Call `legislation_get_toc(type, year, number)` — returns the structure plus the `extent` field (which jurisdictions the Act applies to).

3. **Check for pending amendments.** Call `bills_search_bills(query="<short title>")`. Returns current Bills referencing the Act. For each, report `current_stage`, `house`, `sponsor`.

4. **Surface to the user:**
   - Current statute status with `[uk-legal MCP — legislation.gov.uk]` tag
   - Pending bills (if any) with `[uk-legal MCP — bills]` tag
   - For each pending bill, surface the link to the bill page and the current stage

5. **Optionally** suggest `find-member-contribution` or `bill-debate-trace` (B5) skills if the user wants more depth.

6. **Anti-fabrication clause** (shared).

### Test prompts (3)
- "Is section 21 of the Housing Act 1988 still in force? What bills would amend it?"
- "What's the current state of the Online Safety Act 2023?"
- "Are there any pending amendments to the Equality Act 2010?"

## Skill B5 — `bill-debate-trace`

### Workflow chain
`bills_search_bills(query=bill_name)` → identify the right bill → `parliament_search_hansard(query=bill_short_title)` for debates → `parliament_get_debate_divisions(debate_ext_id)` for votes → `parliament_get_debate_contributions(debate_ext_id)` for key speakers.

### Plugin location
`regulatory-legal-uk/skills/bill-debate-trace/` and `corporate-legal-uk/skills/bill-debate-trace/`.

### SKILL.md frontmatter draft

```yaml
---
name: bill-debate-trace
description: >
  Trace the parliamentary journey of a UK bill — debates, key contributions,
  and divisions. Use whenever the user asks "how did the <bill> progress",
  "who spoke against the <bill>", "what was the vote on <bill>", "show me the
  Lords debates on <bill>", or "trace the <bill> through Parliament". The
  skill assembles a chronological view from Bills API + Hansard + Votes data.
---
```

### Instructions outline

1. **Identify the bill.** Call `bills_search_bills(query="<name>")`. Returns bill records with `current_stage`, `originating_house`, `sponsor`. Pick the right one if multiple match.

2. **Find the debates.** Call `parliament_search_hansard(query="<bill short title>")` — capped at 4 per query, so consider running per-house variants (`filters.house="Lords"`, then `filters.house="Commons"`).

3. **For each debate, get the divisions.** Call `parliament_get_debate_divisions(debate_ext_id)`. Reports `aye_count`, `noe_count`, government_win for each division within the debate. Many debates have zero divisions (motion agreed without vote); report this honestly.

4. **For named key contributions**, call `parliament_get_debate_contributions(debate_ext_id, member_id=...)` only when the user named a specific peer/MP. Don't enumerate all speakers — that's noisy.

5. **Surface a chronological view:**
   - Bill metadata `[uk-legal MCP — bills]`
   - Per-house debate list with date + column refs `[uk-legal MCP — Hansard]`
   - Per-debate divisions (if any) `[uk-legal MCP — votes]`
   - Named contributions if requested

6. **Anti-fabrication clause** (shared).

### Test prompts (3)
- "Trace the Renters' Rights Bill through Parliament — debates, key speakers, votes."
- "How did the Online Safety Bill progress in the Lords?"
- "Show me the divisions on the National Insurance Contributions (Secondary Class 1 Contributions) Bill."

## Authoring procedure for each skill

For each of B1-B5:

1. **Read `regulatory-legal-uk:reg-feed-watcher`** — the reference template.
2. **Invoke `/skill-creator`** (Anthropic's official skill, at `~/.claude/skills/skill-creator/`). It walks through:
   - Capture intent
   - Write SKILL.md draft
   - Write 2-3 test prompts
   - Run claude-with-skill on test prompts AND claude-without-skill (baseline)
   - Eval the outputs in the viewer
   - Iterate on the SKILL.md based on feedback
3. **Apply the trigger-description optimization loop** (skill-creator's Step 3 — "Description Optimization") with a 20-prompt eval set to make sure the skill triggers reliably and doesn't over-trigger.
4. **Manual cross-check the SKILL.md against the dogfeed failure** — would this skill have prevented the actual failure trace?
5. **Commit per skill, not in batches** — each skill commit references its dogfeed-failure target.

## Acceptance criteria

For each skill:

- SKILL.md passes skill-creator's description-optimization loop with ≥80% trigger accuracy on the eval set
- Test prompts (3 per skill) all reach the correct workflow chain
- "No silent supplement" clause is present and tested with at least one "what's <X>" prompt where X doesn't exist (the skill should refuse, not fabricate)
- Skill works when loaded into Claude Code; verify with a manual dogfeed against the deployed `uk-legal-mcp.fly.dev/mcp` (v1.1)

Phase-level:

- All 5 skills authored
- Manchester-landlord-style bypass (16 calls + 14 web sources) does not recur on the dogfeed prompts when these skills are loaded
- The 3 confirmed dogfeed failures (Pannick / Smith / OSCOLA) complete cleanly with skills loaded
- Existing 140 skills remain functional (no skill collisions or trigger overlap)

## Distribution

All 5 skills ship in the existing `uk-legal-plugins` repo (single free public repo per Phase C1). Each is installed automatically when the user installs the relevant plugin (e.g. installing `litigation-legal-uk` brings in `find-case-by-party-verify`).

Dual-manifest: each plugin carries both `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` (see `distribution-strategy.md`). The new skills inherit this automatically — they live under `<plugin>/skills/<skill-name>/SKILL.md` regardless of which manifest references the plugin.

## Out of scope

- Updating existing 140 skills to MCP-native pattern (decision: leave as-is, apply pattern only to new skills)
- Skill authoring via Paul's custom skills (`fastmcp-builder/*`, `mcp-server-dev/*`) — flagged as not-necessarily-best per Obs 201/202; use Anthropic's `skill-creator` only
- Premium / paid skill tiers (deferred — no entitlement infra)
- ChatGPT cohort — skills don't reach ChatGPT; that audience is served by tool-description authority (see `uk-legal-mcp/docs/chatgpt-workflow-encoding.md`)

## Estimated total

~5-7 days for all 5 skills authored, evaluated, and shipped. Roughly 1 day per skill plus integration buffer.
