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

# /find-member-contribution

1. Resolve the member_id first: call `parliament_find_member(name=...)`.
2. Search Hansard by topic or bill name — NOT by member name: `parliament_search_hansard(query=...)`.
3. Retrieve contributions filtered by member: `parliament_get_debate_contributions(debate_ext_id=..., member_id=...)`.
4. If multiple debates returned, retrieve contributions from each and present in date order.
5. Tag every contribution `[uk-legal MCP — Hansard]` with a full column citation.

---

## Purpose

Retrieve verbatim Hansard contributions by a named peer or MP for a specific debate,
bill, or topic. The principal failure mode for this task is text-searching Hansard
directly by member name — that returns debates where the name appears incidentally,
not the member's own contributions. This skill addresses it: resolve member_id first,
search by topic second, filter by member_id third.

## Workflow

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

### Step 1 — Resolve the member_id

Call `parliament_find_member(name=...)` using the name or title the user provided.

- If multiple members match (e.g. "Lord Smith" matches several peers), list all
  candidates with their full parliamentary titles and ask the user to disambiguate.
- If `parliament_find_member` returns empty or `not_found`, the name or title may
  be incomplete or misspelled — ask the user for the member's full parliamentary
  title and do not proceed to Step 2 without a confirmed member_id.

### Step 2 — Find the debate

Call `parliament_search_hansard(query=...)` using the BILL NAME or TOPIC the user
mentioned — NOT the member's name. The tool returns up to four debates with
`debate_ext_id`, `sitting_date`, and `house`.

- If the user provided a specific date, pass it as `filters.date` to narrow results.
- If no debates match the initial query, try a broader or alternative term before
  reporting no results to the user.

### Step 3 — Retrieve contributions

Call `parliament_get_debate_contributions(debate_ext_id=..., member_id=<from Step 1>)`
for each debate returned in Step 2. This filters contributions to the specified member
and returns verbatim text with `column_ref`, `sitting_date`, and `house`.

- If the tool returns empty for a debate the user specifically named, report this
  honestly: the member may not have spoken in that debate, or the debate may not yet
  be in the Hansard index.

### Step 4 — Multiple debates

If Step 2 returned multiple debates, retrieve contributions from each using the
member_id confirmed in Step 1. Collect all non-empty results and present them in
chronological `sitting_date` order.

### Step 5 — Surface with provenance tags

Tag every extracted contribution:

- `[uk-legal MCP — Hansard]` on each contribution block
- Full citation: `[Hansard column: HL Deb vol N col M (date)]` or
  `[HC Deb vol N col M (date)]`, using the `column_ref` and `sitting_date` fields
  returned by the tool
- Where multiple contributions appear within the same debate, list them in
  `column_ref` order

**Source attribution.** No contribution may be tagged `[uk-legal MCP — Hansard]`
unless it appears verbatim in a `parliament_get_debate_contributions` result from
this session. A member's name appearing only in a `parliament_search_hansard` snippet
is not a confirmed contribution — do not quote it as one.

## Output

Surface to the user:

- **Member confirmed:** full parliamentary title as returned by `parliament_find_member`
- **Debates searched:** list of debate titles, sitting dates, and houses queried
- **Contributions found:** verbatim text of each contribution, formatted as:

  > [verbatim contribution text]
  > `[Hansard column: HL/HC Deb vol N col M (date)]` `[uk-legal MCP — Hansard]`

- If no contributions found in a specific debate: "No contribution by [member]
  recorded in this debate in the Hansard index."
- **Suggested next steps** (if contributions found): offer to build an OSCOLA
  Hansard citation via `/oscola-build-citation`, or trace the full bill journey
  via `/bill-debate-trace`

**Test prompts:**
- "What did Lord Pannick say about the Renters' Rights Bill in the Lords on 14 October 2025?"
- "Find Baroness Hale's contribution to the Online Safety Bill Lords debates."
- "Did Hilary Benn speak on the Northern Ireland Troubles legacy bill?"
