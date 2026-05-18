---
name: policy-diff
description: Diff a specific UK regulatory change against the indexed policy library. Use when a UK rule has changed and you need to know which policies it touches and what the gap is, when the user says "diff this rule against our policies", "which policy does this affect", or "gap analysis", or when reg-feed-watcher hands off a material item.
argument-hint: "[regulation name, SI reference, FCA rule, or paste regulatory text/summary]"
---

# /policy-diff

1. Load `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → policy library index.
2. Use the workflow below.
3. Extract requirements from the UK regulatory change. Match to indexed policies.
4. Output: per-requirement gap analysis, which policy needs updating.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/regulatory-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A UK rule changed. You have policies. This skill finds which policies the change touches and what the gap is between "what the rule now requires" and "what the policy says."

## Load context

`~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` → policy library index (policies, locations, owners).

## Scope integrity

If the user asks you to exclude a policy section, requirement, or category from the diff:

1. Do it — the user owns the scope.
2. But flag it, loudly and permanently: "⚠️ SCOPE LIMITATION: Section [X] excluded at user request. This diff does not reflect the full policy. Gaps in the excluded area are NOT identified." Above the header, carried to every downstream artifact.
3. Hand the flag to `gap-surfacer`: "This diff was scope-limited. Do not represent it as a complete compliance picture."
4. Note what the exclusion means in the UK regulatory context: "Excluding vendor management from an FCA SYSC diff means the diff will show 'no policy addresses SYSC third-party outsourcing' — which is worse than showing the gap, given FCA oversight of outsourcing arrangements."

## Workflow

### Step 0: Verify rule status before you diff

Before diffing a UK rule against policy, confirm the rule is actually in force. UK-specific red flags:

- The SI's commencement date has passed by more than 30 days but you have no confirmation it wasn't delayed
- The rule is more than 12 months old
- The rule is an FCA policy statement that may have been amended by a subsequent instrument
- Post-Brexit: a retained EU law provision that may have been revoked or modified by REULA 2023 or a subsequent UK statutory instrument

When you see a red flag, check (via uk-legal MCP, legislation.gov.uk, or the regulator's website) for: delays to commencement, amendments, revocations, or superseding SIs. If you can check and the rule is confirmed in force, proceed. If you cannot verify (no tools connected), emit this banner ABOVE the header, before any content:

> `⚠️ RULE STATUS UNVERIFIED — I could not confirm this UK rule is currently in force. SIs and FCA rules are frequently amended, delayed, or subject to transitional provisions. Do not treat any compliance date below as binding until you confirm the rule's status at legislation.gov.uk, the FCA Handbook, or the issuing authority's website.`

Tag every due date in the output: `[commencement date per published instrument — status unverified]`.

Rule-status uncertainty travels downstream. When handing off a gap to `gap-surfacer`, mark the item `status_verified: false` so it never gets routed to an Overdue bucket on the strength of a published date alone.

### Step 1: Extract the new requirements

**No silent supplement.** If the regulatory change text is partial or ambiguous and the fuller rule isn't available from the indexed source, stop and ask. Do NOT fill the gap from web search or model knowledge without asking.

**Source attribution.** Tag every citation with where it came from:
- `[uk-legal MCP]` / `[legislation.gov.uk]` / `[FCA Handbook]` — retrieved from that source in this session
- `[GOV.UK]` / `[ICO guidance]` / `[Ofcom code]` — fetched from official source
- `[web search — verify]` — from web search
- `[model knowledge — verify]` — from training data
- `[user provided]` — pasted in by the user

**UK citation format.** Use OSCOLA throughout:
- Acts: *Financial Services and Markets Act 2000*, s 165
- SIs: *Financial Services and Markets Act 2000 (Market Abuse) Regulations 2016*, SI 2016/680, reg 3
- FCA Handbook: COBS 4.2.1R; SYSC 9.1.1R; MAR 1.3.1C
- ICO guidance: cite as `[ICO guidance — [document name], [date/version]]`

Read the regulatory change. List each discrete new or changed requirement:

| # | Requirement | In force from | Citation (OSCOLA) | Regulator |
|---|---|---|---|---|
| 1 | [what it requires] | [commencement date] | [SI/Act/Handbook ref] | [FCA/ICO/CMA etc.] |

Be specific. "Enhanced disclosure requirements" is not a requirement. "Must disclose X in Y format at Z point in the customer journey under COBS [ref]" is.

### Step 2: Map to policies

For each requirement, which indexed policy is closest?

- Direct hit: policy explicitly covers this topic
- Indirect: policy covers a related topic, this is a new sub-issue
- No match: no policy addresses this — gap is "policy doesn't exist"

### Step 3: Diff

For each direct or indirect hit, read the policy and compare:

```markdown
### Requirement [N]: [name]

**UK rule requires:** [requirement]

**Our policy ([name], last updated [date]) says:**
> "[relevant excerpt]"

**Gap:** [None — policy already covers this | Partial — policy addresses X but not Y | Full — policy contradicts or doesn't address]

**Change needed:** [specific — "add a paragraph on SYSC 9.1 record-keeping obligations for [product type]" not "update the policy"]

**Policy owner:** [from index]

**UK-specific note:** [e.g., "FCA Handbook rule — R = binding rule, G = guidance, E = evidential provision. This is a binding rule (R)."]
```

### Step 4: No-match gaps

Requirements with no policy match get called out separately:

```markdown
### New policy needed

Requirement [N]: [requirement]

No existing policy covers this. Options:
- Draft new policy (suggested owner: [whoever owns the closest topic])
- Add to existing [related policy] as a new section
- Determine this doesn't need a standalone policy (one-off compliance, not ongoing)
```

### Step 5: Post-Brexit divergence check

If the requirement derives from retained EU law, flag whether the UK rule has diverged from the current EU position:

> **Post-Brexit divergence note:** This requirement derives from [EU source — e.g., GDPR Art. 17, MiFIR Art. 26]. The current UK equivalent is [UK-GDPR Art. 17 / UK MiFIR SI 2018/1403]. As of [date `[model knowledge — verify]`], the UK and EU rules [are identical | diverge on [specific point]]. If your firm operates in both jurisdictions, check whether the EU rule has been amended since the UK retained-law version was domesticated.

## Branches by regulatory input type

### Pre-rule branch (UK consultation paper or draft SI)

If the regulatory input is an FCA CP, ICO consultation, GOV.UK consultation, or draft SI (no imposed requirements yet), do NOT run a full gap-closure diff. Instead, produce a **pre-positioning analysis**:

- Name the policies that will likely need to change once a final policy statement or SI issues.
- Flag whether any of the consultation's issue areas intersect with the company's practice in a way that warrants submitting a consultation response.
- Note the consultation closing date and the team's consultation decision owner from CLAUDE.md.
- Do NOT produce per-requirement "no gap" rows for a consultation — there are no binding requirements to diff against yet.

### Negative-finding branch (final rule diffed against a policy that isn't the right target)

If every requirement comes out as "no gap against [the named policy]," compress to a single short paragraph:

```markdown
## Policy Diff: [Regulation name] — [Policy name]

[REGULATION] doesn't appear to require a change to [POLICY NAME]. [POLICY NAME]
[section] already covers [Y]. The policies this rule actually touches are
[other-policy-1] and [other-policy-2] — rerun `/regulatory-legal-uk:policy-diff` against those.

Review on [next cycle] or if [trigger — e.g., "the FCA issues a further Policy Statement on this topic"].
```

### Gap branch (final rule / UK consultation with at least one gap against the target policy)

Full per-requirement analysis as specified above.

## Output

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Policy Diff: [Regulation name]

**Regulation:** [name, OSCOLA citation, link]
**In force from:** [commencement date]
**Issuing authority:** [FCA / ICO / CMA / Ofcom / HM Treasury / HMRC / etc.]
**Requirements extracted:** [N]

### Bottom line

[N gaps need action by [date] — top 3: X, Y, Z]

### Summary

| # | Requirement | Policy affected | Gap | Regulator | Owner |
|---|---|---|---|---|---|
| 1 | [short] | [policy name or "none"] | None/Partial/Full | [FCA/ICO/etc.] | [name] |

### Detailed diffs

[Each requirement block from Step 3]

### New policies needed

[From Step 4, if any]

### No-gap requirements

[List — useful to know what's already covered]

### Post-Brexit divergence

[From Step 5, if applicable]

---

**Verify citations before relying on them.** Regulatory citations and policy references above were AI-generated and have not been checked against a primary source. Before acting on any requirement here, confirm the rule against legislation.gov.uk, the FCA Handbook (handbook.fca.org.uk), or the issuing authority's website — check accuracy, commencement date, and current status. Citations are in OSCOLA format; verify SI numbers, Act section numbers, and Handbook cross-references before relying on them. Source tags on each requirement (e.g., `[uk-legal MCP]`, `[model knowledge — verify]`) show where the citation came from.
```

## Config-dependent fallbacks

This skill reads the policy library index from `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`. When the index is empty or still `[PLACEHOLDER]`:

- **Policy library empty:** flag every requirement as "no policy match" by default and append: "The policy library in your configuration is empty, so every requirement is flagged as a new-policy gap. If you have policies that address these requirements, add them to the library with `/regulatory-legal-uk:cold-start-interview --redo` or by editing the config, then re-run the diff."
- **Owner missing for a matched policy:** leave the Owner cell blank in the summary and append: "Policy owners aren't set for [list]. Assign them with `/regulatory-legal-uk:cold-start-interview --redo` so gap-surfacer can route."

## Handoff

To gap-surfacer: every Partial or Full gap becomes a tracked item with owner and deadline.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced.

## What this skill does not do

- Draft the policy updates. It identifies what needs updating; policy-redraft drafts.
- Interpret ambiguous FCA Handbook text definitively. The FCA Handbook has binding rules (R), evidential provisions (E), guidance (G), and directions (D) — if the binding vs. non-binding status of a Handbook provision is material to the gap finding, flag it `[review]` for the solicitor.
