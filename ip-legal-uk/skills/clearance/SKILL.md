---
name: clearance
description: >
  Trade mark clearance first pass — knockout + similar-marks check producing a
  flag list, not a clearance opinion. Use when a new mark is proposed, when
  asked whether a mark is available or to run a knockout search, or when
  assessing likelihood-of-confusion factors before a full professional search.
  This skill never concludes a mark is clear.
argument-hint: "[describe the proposed mark, goods/services, and jurisdictions — or just the mark and I'll ask]"
---

# /clearance

**This is a triage, not a clearance opinion.** A trade mark clearance opinion
requires a full professional search and registered trade mark counsel's
judgment. A "no obvious conflicts" result means the triage
didn't find anything — it does not mean the mark is clear. Clients have been
sued over marks that passed a knockout search.

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal-uk:cold-start-interview`.
2. Follow the workflow below.
3. Run intake (mark, goods/services, classes, jurisdictions, visual/stylization).
4. Knockout check for intrinsic bars — absolute grounds under TMA 1994 s.3: generic, descriptive, deceptive,
   geographic, surname, false connection, prohibited matter, functional.
5. Similar-marks search against what's connected (uk-legal MCP, govuk MCP, Solve Intelligence, or whatever MCP is available). If nothing is
   connected, say so in the output and proceed with the factor analysis only.
6. Walk the TMA 1994 / EU global-appreciation likelihood-of-confusion factors. Flag each; never conclude.
7. Write the triage memo to the matter folder (if a matter is active) or the
   practice outputs folder. Apply the work-product header per role.
8. End with recommended next steps and the non-lawyer gate if the role is
   non-lawyer.

This skill never concludes a mark is clear. If uncertain, flag — the solicitor or trade mark attorney
decides.

## Examples

```
/ip-legal-uk:clearance "APEXLEAF for an outdoor apparel line, planned launch UK + EU"
```

```
/ip-legal-uk:clearance
```

(And the skill will ask for the mark, goods, classes, and jurisdictions.)

---

## THIS IS A FIRST PASS, NOT A CLEARANCE OPINION

**Say this at the top of every output. Do not drop it. Do not soften it.**

> **This is a first pass, not a clearance opinion.** A trade mark clearance opinion
> requires a full professional search (UK IPO Trade Marks Register, EUIPO eSearch, common law sources,
> international registries, domain and social, trade dress and design marks where
> relevant) and the judgment of a solicitor or Registered Trade Mark Attorney on likelihood of confusion, which depends on
> factors a structured triage cannot fully assess. A "no obvious conflicts" result
> from this skill means the triage didn't find anything — it does not mean the
> mark is clear. Clients have been sued over marks that passed a knockout search.
> A registered trade mark solicitor or Registered Trade Mark Attorney evaluates before anyone adopts, files, or
> invests in this mark.

This is the loudest guardrail in the plugin. Under-calling a conflict is a
one-way door — a logo on products, a product launched, a TM application filed, all
with a problem underneath. Over-calling is a two-way door — the attorney narrows
the list in review. Stay on the two-way door side.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Load the practice profile first

Before running clearance, read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. Pull:

- **Role** from `## Who's using this` (solicitor vs. patent/trade mark attorney vs. non-lawyer changes the work-product header and the non-lawyer gate below).
- **Registered in** and **enforce where** from `## IP practice profile` and `## Enforcement posture` (default jurisdictions — note UK and EU are separate since Brexit).
- **Integrations** from `## Available integrations` (uk-legal MCP / govuk MCP / Solve Intelligence — each determines what searches are available to run).
- **Decision posture** from `## Decision posture on subjective legal calls` — this skill never concludes "not confusingly similar."

If `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` contains `[PLACEHOLDER]` or `[Your Company Name]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — UK jurisdiction, middle risk appetite, solicitor role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

---

## Intake

Ask once, in a single batch:

> A few questions before I run the triage:
>
> 1. **Proposed mark.** Exact spelling, any stylization, and whether it's a word mark, logo, or both.
> 2. **Goods or services.** What's actually being sold or offered under this mark. A sentence or two — I'll map to Nice classes.
> 3. **Classes.** If you already know the Nice classes, list them. Otherwise describe the goods/services and I'll suggest the likely classes and confirm with you before running the search.
> 4. **Jurisdictions.** Where do you plan to use, register, or enforce? (UK only / EU (EUIPO) / Madrid / specific countries — note UK and EU are separate since Brexit; I'll default to `Registered in` from your practice profile if you don't say.)
> 5. **How it will appear in use.** Any taglines, adjacent product names, trade dress, or design elements that would show up with it in market.

---

## Knockout check (absolute grounds — TMA 1994 s.3)

Before any database search, run the intrinsic problems that kill a mark regardless
of prior registrations. Apply TMA 1994 s.3 (absolute grounds — equivalent to the EU Trade Mark Regulation Art. 7 EUTMR, which is substantially retained in UK law post-Brexit).

| Bar | TMA 1994 | What it means | Flag when |
|---|---|---|---|
| **Generic** | s.3(1)(d) | The term IS the category | The mark names what the thing is |
| **Descriptive** | s.3(1)(c) | Directly describes a feature, quality, or ingredient | A consumer reads the mark and knows what the product does without imagination |
| **Non-distinctive** | s.3(1)(b) | Lacks inherent distinctiveness | The mark is too ordinary to identify trade origin |
| **Deceptive** | s.3(3)(b) | Likely to deceive the public as to nature, quality, or geographical origin | The mark implies a quality the goods don't have |
| **Geographical indication** | s.3(1)(c) | Primarily a place name and goods come from (or don't) that place | Mark = place + generic; or place + goods where customers would assume origin |
| **Surname** | s.3(1)(b) | Primarily a surname with no trade mark significance | Mark reads as someone's last name to the relevant consumer |
| **Contrary to public policy / morality** | s.3(3)(a) | Contrary to public policy or accepted principles of morality | Mark would be refused on public interest grounds |
| **Deceptive as to origin** | s.3(3)(b) | Deceives as to geographical origin | Post-Brexit: UK GI protections are separate from EU GI protections |
| **Prohibited matter** | s.3(5) | Flags, coats of arms, royal arms, specific prohibited categories | Mark contains a prohibited element |
| **Functional (for shape marks)** | s.3(2) | The shape results from the nature of the goods or is necessary to obtain a technical result or gives substantial value | Design mark — and the feature performs a function |

Note: the UK has not adopted equivalents of the post-*Brunetti* US scandalous mark changes; TMA 1994 s.3(3)(a) (contrary to public policy or accepted principles of morality) still applies.

**Output:** for each knockout category, either "no issue identified" or a
specific flag with a one-line reason. Don't produce a blank table of passes.

---

## Similar marks check

The purpose here is to **find potentially confusingly similar prior marks**, not
to decide whether confusion is likely. That is the solicitor's or trade mark attorney's call.

### What the user has connected

Read `## Available integrations` from `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`:

- **If a trade mark search connector is available** (govuk MCP exposing IPO records, uk-legal MCP, or any MCP exposing TM-registry search): run a preliminary search across the relevant classes and jurisdictions. Attribute every result to its source. Note the date of the search and the scope.
- **If no search connector is available:** say so, explicitly, in the output. Do not infer results from model knowledge and present them as search findings.

### Fallback when no database access exists

Write out, in the output, this exact statement:

> **No database search was run.** This triage did not hit the UK IPO Trade Marks Register, EUIPO eSearch, Madrid Monitor, or any common law / unregistered-mark sources. A knockout or full search across those databases is required before any conclusion about availability. The triage below is limited to intrinsic-bar analysis and structured confusion factors against marks the user has identified or that come up in the conversation.

### Adjacent families sweep (required before concluding)

A clearance that only checks exact and near-exact matches misses the marks a competitor adopted *because* yours was taken. Before concluding, identify 3–5 adjacent word families the practitioner should also sweep.

> **Adjacent families to sweep (please confirm or add):**
>
> - [family 1 — e.g., HUB / NEST / LINK / CONNECT]
> - [family 2 — e.g., similar names in the same product category]
> - [family 3 — e.g., HOME / HOUSE / SMART variants]
> - [family 4 — phonetic twins on the root]
>
> A clearance that only checks exact and near-exact matches misses the marks a
> competitor adopted because yours was taken. Confirm this list is complete for
> the category before I continue.

> **When non-English-speaking jurisdictions are in scope,** add:
> - **Translation equivalents.** The UK / EU global-appreciation approach treats a translation as the same mark for confusion purposes (the "foreign equivalents" doctrine).
> - **Transliteration.** The mark written in the relevant script (Cyrillic, Chinese/Japanese/Korean, Arabic, Hangul, Thai).
>
> If you can't perform cross-language analysis, say so: "Cross-language phonetic and translation-equivalent analysis not performed — this is the most common source of cross-border conflicts. A clearance search in [jurisdiction] should include it."

---

## Likelihood-of-confusion factors (TMA 1994)

> **Confusion framework is jurisdiction-specific.**
>
> - **UK (TMA 1994 s.5(2) and s.10(2)):** Global appreciation approach — all relevant factors assessed holistically through the eyes of the average consumer. Key elements: similarity of marks (sight / sound / meaning / overall commercial impression), similarity / identity of goods and services, distinctiveness of the earlier mark (inherent or acquired through use), and risk of association. Post-Brexit, UK courts apply the global appreciation approach derived from EU law but may diverge over time. Check for recent UK IPO and IPEC decisions.
> - **EU (EUTMR Art. 8(1)(b)):** Global appreciation — same approach, but under EUIPO / EU General Court / CJEU jurisprudence. UK and EU now separate proceedings.
> - **Common law passing off:** parallel track in UK. Three elements: goodwill (reputation established in the UK or relevant jurisdiction), misrepresentation (a false representation leading the public to think the goods/services are those of the claimant), and damage (actual or probable damage to the claimant's goodwill).

The relevant test determines the factors to walk through. For UK clearance, apply TMA 1994 global appreciation; flag passing off as a parallel track.

For each factor, produce a **flag**, not a verdict:

- **Similarity of marks** (appearance, sound, meaning / connotation, overall commercial impression).
- **Similarity of goods or services.** Not whether the goods are identical — whether the average consumer would expect them to come from the same source or commercially linked sources.
- **Channels of trade.** Where each side actually sells.
- **Sophistication / attention level of consumers.** The average consumer for the relevant goods/services.
- **Distinctiveness of prior mark.** Inherently distinctive or acquired through use? More distinctive = wider protection.
- **Intent.** Evidence of intent to trade on goodwill.
- **Actual confusion.** Any evidence (misdirected inquiries, surveys, reviews, social posts).
- **Likelihood of association** (EU/UK — broader than mere source confusion; the consumer may believe the marks are economically linked).

Per the decision posture in `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`:

- **Never conclude "not confusingly similar."**
- If uncertain, write: "Similar marks found — confusion assessment required before adoption." Or: "Factors cut both ways; solicitor / trade mark attorney judgment required."

---

## Post-Brexit considerations

When the practice profile includes both UK and EU jurisdictions:

- UK and EU trade marks are separate systems. A UK clearance does not clear the EU.
- Search UK IPO and EUIPO separately.
- Existing EUTMs as of 31 Dec 2020 generated comparable UK marks — these comparable UK marks are in the UK register and may not be obvious from name searches.
- Madrid Protocol: UK and EU (via EUIPO) are separate designations; a Madrid mark designating only EU does not cover UK and vice versa.
- Post-Brexit divergence: UK courts and the IPO may develop their own case law on confusion, distinctiveness, and bad faith over time. Flag when the analysis relies heavily on CJEU jurisprudence that has not been explicitly adopted by UK courts.

---

## Recommended next steps

Every clearance output ends with concrete next steps, bucketed by what the triage found.

---

## Output format

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER]

# Trade Mark Clearance — First Pass (NOT AN OPINION)

**This is a first pass, not a clearance opinion.** A clearance opinion requires
a full professional search and the judgment of a solicitor or Registered Trade Mark Attorney. A "no obvious conflicts"
result here means the triage didn't find anything — it does not mean the mark
is clear. A solicitor or Registered Trade Mark Attorney evaluates before anyone adopts, files,
or invests in this mark.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Proposed mark

- **Mark:** [exact text, stylization noted]
- **Mark type:** [word / device / composite]
- **Goods / services:** [description]
- **Classes:** [Nice class numbers with one-line descriptions]
- **Jurisdictions:** [UK / EU (EUIPO) / Madrid / specific countries — note post-Brexit separation]
- **Confusion test applied:** [TMA 1994 global appreciation / EUTMR Art. 8(1)(b) — with the reason it's the right one]

## Knockout issues (Absolute grounds — TMA 1994 s.3)

| Bar | TMA provision | Flag | Note |
|---|---|---|---|
| Generic / descriptive / non-distinctive / deceptive / geographic / surname / contrary to public policy / prohibited / functional (shape) | [s.3 subsection] | [none / flagged] | [one line if flagged] |

## Similar marks check

**Sources searched:** [registries and databases hit, with dates — or "no database search run; see scope note below."]
**Scope:** [classes, jurisdictions, exact-vs-fuzzy, device search or not]

**Adjacent families swept (confirmed with user):**
- [family 1]
- [family 2]
- [family 3]
- [family 4]

| Mark | Source | Classes / G&S | Owner | Status | First use / date | Note |
|---|---|---|---|---|---|---|

## Confusion factors — flags for attorney review (TMA 1994 s.5(2) global appreciation)

| Factor | Flag | Direction |
|---|---|---|
| Similarity of marks (sight / sound / meaning / commercial impression) | [note] | [weighs toward / against conflict / mixed] |
| Similarity of goods or services | [note] | [direction] |
| Channels of trade | [note] | [direction] |
| Consumer sophistication / attention level | [note] | [direction] |
| Distinctiveness of prior mark (inherent / acquired) | [note] | [direction] |
| Intent | [note] | [direction] |
| Actual confusion / likelihood of association | [note or "no evidence surfaced"] | [direction] |

**Passing off parallel track:** [brief note on whether passing off is a relevant parallel claim and the state of the three elements: goodwill / misrepresentation / damage]

**Post-Brexit note:** [any specific UK/EU coverage gaps or divergence points relevant to this mark and these jurisdictions]

**Conclusion on confusion:** *This skill does not conclude.* [one of the standard non-conclusion options]

## Recommended next steps

- [specific next step 1 — e.g., "Full professional search across UK IPO, EUIPO, Madrid Monitor, common law sources before adoption"]
- [routing per practice profile — trade mark OC or in-house IP counsel named in the practice profile]

## Citation verification

Every case, registration number, statute, and database result in this memo must
be verified against the authoritative source before relying on it.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Adopting, filing, or
> investing in this mark based on this triage alone has legal consequences —
> including being sued for infringement over a mark that "passed" this check.
> A solicitor or Registered Trade Mark Attorney needs to evaluate before you move.
>
> Here's a brief to bring to a professional — it'll cut the time the conversation takes:
>
> [Generate a 1-page summary: the proposed mark, the goods/services and classes,
> the knockout issues (if any), the similar marks surfaced (if any), what was
> and wasn't searched, and the three questions to ask the solicitor/attorney.]
>
> If you need to find a solicitor or other authorised legal professional in the UK: the SRA's online register for solicitors; the CITMA finder for Registered Trade Mark Attorneys (citma.org.uk); the IPO's 'Find a trade mark attorney' service; and the INTA (International Trademark Association) member directory for international practitioners.

Deliver the full triage memo alongside the brief. Do not withhold the analysis.

---

## Output location

If matter workspaces are enabled and a matter is active, write the output to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`
and surface the path to the user.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- **Conclude a mark is clear.** Ever. The loudest guardrail in the plugin.
- **Substitute for a full professional search** across the UK IPO, EUIPO, Madrid Monitor, common law sources, international registries, domain/social, and device marks.
- **File a trade mark application.** Filing is a solicitor's / trade mark attorney's task.
- **Evaluate trade mark dilution beyond a preliminary flag.** Dilution under TMA 1994 s.5(3) requires a fame and unfair advantage/detriment analysis this skill does not attempt.
- **Address foreign local-law bars** beyond flagging that foreign analysis is required when a foreign jurisdiction is in scope.
- **Quote outputs to customers, counterparties, or the press.** This is internal research.
