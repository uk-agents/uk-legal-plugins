---
name: bill-debate-trace
description: >
  Trace the parliamentary journey of a UK bill — debates, key contributions,
  and divisions. Use whenever the user asks "how did the <bill> progress",
  "who spoke against the <bill>", "what was the vote on <bill>", "show me the
  Lords debates on <bill>", or "trace the <bill> through Parliament". The
  skill assembles a chronological view from Bills API + Hansard + Votes data.
---

# /bill-debate-trace

1. Identify the bill: `bills_search_bills(query="<name>")`.
2. Find debates per house: `parliament_search_hansard(query=..., filters.house=...)`.
3. Get divisions per debate: `parliament_get_debate_divisions(debate_ext_id=...)`.
4. For named members only: `parliament_get_debate_contributions(debate_ext_id=..., member_id=...)`.
5. Surface a chronological view: bill metadata, debates, divisions, named contributions.

---

## Purpose

Assemble a chronological view of a UK bill's parliamentary journey — its current
stage, the debates it generated in each House, any divisions (votes), and (if
requested) specific contributions by named peers or MPs. The skill draws on three
data sources via uk-legal MCP: the Bills API for metadata and stage, Hansard for
debates and contributions, and the Votes/Divisions API for division counts and
government-win data.

## Workflow

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

### Step 1 — Identify the bill

Call `bills_search_bills(query="<name>")`. Returns bill records with `current_stage`,
`originating_house`, and `sponsor`. If multiple bills match, list them and ask the
user to confirm the right one before proceeding.

### Step 2 — Find the debates

Call `parliament_search_hansard(query="<bill short title>")`. Because the Hansard
search is capped at four results per query, run it per-house if needed:

1. `parliament_search_hansard(query="<short title>", filters.house="Lords")`
2. `parliament_search_hansard(query="<short title>", filters.house="Commons")`

Collect all `debate_ext_id` values returned across both queries.

### Step 3 — Get divisions per debate

For each `debate_ext_id` collected in Step 2, call
`parliament_get_debate_divisions(debate_ext_id=...)`. Returns `aye_count`,
`noe_count`, and `government_win` for each division within the debate.

Many debates have zero divisions (motion agreed without a vote). Report this
honestly: "No divisions recorded — motion agreed without a vote." Do not omit
debates because they had no divisions; include them in the chronological list.

### Step 4 — Named contributions (only if requested)

Only retrieve individual contributions if the user named a specific peer or MP.
Do NOT enumerate all speakers — that is noisy and unhelpful for most queries.

If a specific member is named:

1. Call `parliament_find_member(name=...)` to confirm the member_id.
2. Call `parliament_get_debate_contributions(debate_ext_id=..., member_id=...)`
   for each relevant debate.
3. Tag each result `[uk-legal MCP — Hansard]`.

For general "who spoke" questions, summarise from the debate metadata rather than
retrieving all individual contribution records.

### Step 5 — Surface a chronological view

Report:

- **Bill metadata:** title, `current_stage`, originating house, sponsor
  tagged `[uk-legal MCP — bills]`
- **Per-house debate list** in chronological order: debate title, sitting date,
  Hansard column refs tagged `[uk-legal MCP — Hansard]`
- **Per-debate divisions** (if any): aye count, noe count, government_win tagged
  `[uk-legal MCP — votes]`
- **Named contributions** if the user requested them (from Step 4)

**Source attribution.** Bill metadata carries `[uk-legal MCP — bills]`. Debate
and contribution data carries `[uk-legal MCP — Hansard]`. Division data carries
`[uk-legal MCP — votes]`. No division result may be reported without a
`parliament_get_debate_divisions` result from this session. No contribution may
be reported without a `parliament_get_debate_contributions` result from this session.

## Output

Surface to the user:

- **Bill:** title, `current_stage`, originating house, sponsor
  `[uk-legal MCP — bills]`
- **Parliamentary journey** (chronological):

  | Date | House | Debate | Divisions |
  |---|---|---|---|
  | [date] | Lords / Commons | [debate title, Hansard col ref] | [N ayes / N noes / gov win: Y/N] or "no divisions" |

  `[uk-legal MCP — Hansard]` on debate entries; `[uk-legal MCP — votes]` on division entries

- **Named contributions** (if the user requested): verbatim text with
  `[uk-legal MCP — Hansard]` and column citation
- **Suggested next steps:**
  - To check the current state of the Act after Royal Assent: `/statute-amendments-trace`
  - To retrieve a specific member's contribution in full: `/find-member-contribution`

**Test prompts:**
- "Trace the Renters' Rights Bill through Parliament — debates, key speakers, votes."
- "How did the Online Safety Bill progress in the Lords?"
- "Show me the divisions on the National Insurance Contributions (Secondary Class 1 Contributions) Bill."
