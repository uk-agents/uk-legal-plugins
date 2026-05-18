---
name: fto-triage
description: >
  Freedom-to-operate triage — a structured first look at potentially blocking
  patents, not an FTO opinion. Use when a product, process, or feature is
  being evaluated for blocking patents, when asked whether anything stops a
  launch, or to build a claim-chart first pass against the most plausible
  patents before patent counsel review. This skill never concludes a product
  is clear to launch.
argument-hint: "[describe the product / process / feature and jurisdictions — or just the subject and I'll ask]"
---

# /fto-triage

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by a Chartered Patent Attorney or registered patent
counsel. Patent infringement is strict liability; wilful infringement can
attract enhanced damages. A "no obvious blocking patents" result from this
skill means the triage didn't find one — it does not mean the product is clear.

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal-uk:cold-start-interview`.
2. Follow the workflow below.
3. Run intake (product/process, technical detail, jurisdictions, known patents,
   timing).
4. Run a preliminary patent search if a connector is available (Solve
   Intelligence Patents, or other patent-research MCP). Otherwise say
   so in the output and proceed with the patents the user has supplied.
5. For the 2–5 most plausible patents, build a claim-chart first pass against
   each independent claim — element by element. Literal read first; flag
   doctrine-of-equivalents separately; flag indirect / divided infringement.
6. List open questions a real FTO study would resolve (enforceability,
   prosecution history, IPR outcomes, licence availability, enforcement
   history of the proprietor).
7. Write the triage memo to the matter folder or practice outputs folder. Apply
   the work-product header per role.
8. End with recommended next steps, a wilfulness note (knowledge of specific
   patents factors into enhanced-damages arguments if the company proceeds
   without further counsel review), and the non-lawyer gate if the role is
   non-lawyer.

This skill never concludes that a product is clear to launch. If uncertain,
flag — a Chartered Patent Attorney decides.

## Examples

```
/ip-legal-uk:fto-triage "an on-device speech recognition model for consumer wearables, UK launch first"
```

```
/ip-legal-uk:fto-triage
```

---

## THIS IS NOT A FREEDOM-TO-OPERATE OPINION

**The loudest guardrail in the plugin. Say this at the top of every output. Do
not drop it. Do not soften it. Do not let the reader skim past it.**

> **This is not a freedom-to-operate opinion.** An FTO opinion is a professional
> legal judgment, usually by a Chartered Patent Attorney or registered patent
> counsel, based on a comprehensive search, full claim construction, and an
> element-by-element infringement analysis against each claim of each relevant
> patent. This triage is a structured first look at what might be out there. A
> "no obvious blocking patents" result means the triage didn't find one — it
> does not mean the product is clear. Patent infringement in the UK is actionable
> regardless of knowledge or intent (Patents Act 1977 s.60); proceeding with
> knowledge of a specific patent can support an argument for additional damages
> under PA 1977 s.63. The decision to launch, make, use, sell, or import is a
> business decision informed by a formal FTO study and a Chartered Patent
> Attorney's judgment — not by this triage.

Under-flagging a blocking patent is a one-way door — a product launched, a
claim a year later, additional damages on the table. Over-flagging is a
two-way door — the attorney narrows the list in a read-through. Stay on the
two-way door side. Always.

### A note on wilfulness and additional damages

Reading this triage is reading something about patents. Reading something about
patents can, in some circumstances, factor into an additional-damages argument
in subsequent proceedings (PA 1977 s.63: "flagrant" infringement). This is one
reason the output is marked as privileged when a solicitor or Chartered Patent
Attorney is using it, and why the non-lawyer output is framed as research to
take to counsel. Do not discuss specific patents surfaced by this triage outside
privileged channels.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is
`✗` (the default for in-house users), skip — skills use practice-level context.
If enabled and there is no active matter, ask: "Which matter is this for? Run
`/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the
active matter's `matter.md` for matter-specific context and overrides. Write
outputs to the matter folder at
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/`.
Never read another matter's files unless `Cross-matter context` is `on`.

Patent FTO matters are particularly common candidates for **clean-team** or
**heightened** confidentiality at matter-open.

---

## Load the practice profile first

Before running triage, read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. Pull:

- **Role** from `## Who's using this` (solicitor/attorney vs. non-lawyer changes the
  work-product header and the non-lawyer gate below).
- **Registered in** and **enforce where** from `## IP practice profile` and
  `## Enforcement posture` (useful for jurisdiction defaults — UK, EU, PCT).
- **Patent OC** from `## IP practice profile` → `Outside counsel roster` for
  the routing step (Chartered Patent Attorney / Patent Attorney firm).
- **Integrations** from `## Available integrations` — specifically Solve
  Intelligence, or any patent-research MCP.
- **Decision posture** from `## Decision posture on subjective legal calls` —
  this skill never concludes "does not infringe."

If `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` contains
`[PLACEHOLDER]` or `[Your Company Name]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I
> tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal-uk:cold-start-interview` (2 minutes) to configure your
>   profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — UK
>   jurisdiction, middle risk appetite, solicitor role, no playbook — and tag
>   every output `[PROVISIONAL — configure your profile for tailored output]`.

### Provisional mode

If the user says "provisional," run the FTO triage normally using these generic
defaults: middle risk appetite, solicitor role, UK jurisdiction, no playbook.
Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end
of the output, append:

> "That was a generic run against default assumptions. Run
> `/ip-legal-uk:cold-start-interview` to get output calibrated to YOUR practice
> — your playbook, your jurisdiction, your risk appetite. 2 minutes."

---

## Intake

Ask in a single batch:

> I'll run an FTO triage. A few questions first:
>
> 1. **Product, process, or feature.** What's being made, used, offered for
>    sale, sold, or imported? Describe it plainly — the technical essence, not
>    the marketing pitch.
> 2. **Technical detail.** Any architectural diagrams, claim-relevant specs, a
>    public product page, or a spec document you can share?
> 3. **Jurisdictions.** Where will it be made, used, sold, offered for sale,
>    imported? In the UK, the acts of infringement are set out in PA 1977 s.60
>    — making, disposing of, using, importing, or keeping. I'll default to the
>    UK (including England & Wales, Scotland, Northern Ireland) if you don't
>    specify. EU / US / other jurisdictions are separate analyses.
> 4. **Known patents.** Are there patents already on your radar — a competitor's
>    portfolio, a known SEP pool, an NPE letter, something an engineer mentioned?
> 5. **Timing.** How close is this to launch? If it's months out, the triage
>    is early and design-around is on the table. If it's already shipping,
>    we're in cover-our-downside mode.

Wait for the answer. If the description is vague ("an AI agent," "a database"),
push once:

> Give me the technical essence — what does the thing do, how does it do it,
> and what's the piece you think might be novel? Patent claims live at that
> level.

---

## Scope — utility patents only

**This skill analyses utility patents.** Flag and route out for any other type:

- **UK registered designs / design patents.** Different test entirely — different doctrine, different regime. Route to `/ip-legal-uk:infringement-triage` design branch and to design patent / registered design counsel.
- **EP(UK) patents.** Treat as UK designations of a European patent — PA 1977 applies to the UK designation.
- **UPC-registered unitary patents.** Note: the UK is NOT party to the Unified Patent Court. UPC patents and UPC proceedings do not cover UK territory. A European patent designating UK is a PA 1977 matter, not a UPC matter. Flag if the user is confused about this.

Also cross-flag **trade dress and passing off**: if the product's appearance is the risk, the same facts may be a passing off or TMA 1994 trade mark claim. Flag as a parallel track.

---

## Search

### What the user has connected

Read `## Available integrations`:

- **Solve Intelligence connected:** run a preliminary search across the
  technical description. Note the date of the search, the query used, the
  jurisdictions covered, and any date window (current in-force patents; recent
  published applications at the EPO / UK IPO / WIPO).
- **Patent-research MCP available:** use it.
- **None of the above:** explicitly say so. Do not infer patents from model
  knowledge and present them as search results.

### Fallback when no patent database is connected

Write this exact statement in the output:

> **No patent database search was run.** This triage did not hit Solve
> Intelligence Patents, EPO Espacenet, Google Patents, UK IPO patent search,
> or any other patent corpus. A structured search across the jurisdictions in
> scope is required before relying on this triage for any launch decision. The
> analysis below is limited to patents and applications the user has named or
> that come up in the conversation.

Then proceed.

### Supplementary signals (not a substitute)

If available and the user allows, sweep for non-patent signals that flag a
patent concern:

- **Competitor patent filings** around the product area (EPO, UK IPO, USPTO).
- **Known NPE targeting** of the technology class.
- **Standards-essential declarations** (IEEE, ETSI, 3GPP) if the product
  touches a relevant standard. Note *Unwired Planet v Huawei* [2020] UKSC 37
  on FRAND obligations before UK courts.
- **Reported litigation** in the technology space (UK Patents Court, IPEC).

Each signal is a reason to look harder, not a patent hit.

---

## For each relevant patent found or supplied

Capture:

- **Patent number** (with application number if different) and **jurisdiction**
- **Title**
- **Proprietor and inventors**
- **Priority date and grant date**
- **Expiration date** (check term adjustments; supplementary protection certificates (SPCs) for pharma/biotech can extend term beyond 20 years in the UK post-Brexit — handled separately from EU SPCs)
- **Maintenance fee / annuity status / in-force status** — UK IPO annual renewal fees are due on each anniversary of the filing date; if fees have lapsed, the patent may not be in force. Check the UK IPO register.
- **Claim count — independent and dependent**
- **Independent claims as granted** (and any claims amended post-grant)
- **Related proceedings** — any UK IPO post-grant proceedings, revocation actions at the UK IPO or Patents Court, EPO oppositions, appeal outcomes
- **File wrapper highlights** — prosecution disclaimers, amendments that narrowed the claims

**Do not supplement silently.** If a search surfaces a patent, attribute the result. Never invent a patent number, never "fill in" a claim element the file doesn't support, never imagine an expiration date.

---

## Claim-chart first pass

Pick the patents with the most plausible read on the product — usually the
2–5 with the closest technical mapping — and walk each independent claim
element-by-element.

**For each selected patent, write out one claim chart per independent claim:**

| Claim element | Does the product practise this? | Basis |
|---|---|---|
| "A [preamble phrase]" | [yes / no / possibly / depends on construction] | [one sentence — what in the product maps; what doesn't; what's ambiguous] |
| "comprising [element 1]" | [yes / no / possibly] | [mapping or gap] |
| "wherein [element 2]" | [yes / no / possibly] | [mapping or gap] |
| [continue for every element] | | |

**Rules for the chart:**

- **Every element matters.** A claim is infringed only if the accused product
  practises every element of at least one claim (all-elements rule, consistent
  with UK practice). Missing one element literally means no literal
  infringement on that claim. Do not skip.
- **Doctrine of equivalents (Improver questions).** First chart literal
  infringement. Then, for any "no" elements, note whether an equivalents read
  is plausible under the UK *Improver* questions (*Improver Corp v Remington
  Consumer Products Ltd* [1990] FSR 181, as modified in *Actavis UK Ltd v Eli
  Lilly and Company* [2017] UKSC 48). The Supreme Court's *Actavis* approach
  asks: (1) does the variant achieve substantially the same result in
  substantially the same way? (2) would the variant have been obvious at the
  priority date to a person skilled in the art? (3) would the skilled reader
  have understood from the language of the claim that strict compliance was an
  essential requirement? Flag DOE / equivalents analysis as requiring
  Chartered Patent Attorney judgment.
- **Claim construction is the attorney's job.** Where a term could be construed
  narrowly or broadly and the answer changes the infringement read, flag the
  term and note both constructions. Do not pick one silently.
- **Indirect infringement (contributory infringement).** Under PA 1977 s.60(2):
  supplying means essential for putting an invention into effect, when the
  supplier knows such means are suitable and intended for putting the invention
  into effect. Flag if any read depends on this; do not attempt a full analysis.

> **Patent systems differ by jurisdiction.** The UK claim chart (all-elements
> rule, *Actavis* equivalents, PA 1977 damages) does not transfer to EU, US,
> or other systems:
> - **EU / EPC:** EPO opposition proceedings, UPC (does NOT cover UK),
>   national court infringement proceedings in each EU member state separately.
> - **Germany:** bifurcated validity/infringement proceedings, utility models
>   (Gebrauchsmuster).
> - **France, Netherlands, etc.:** national court proceedings, possible UPC
>   opt-out consideration (irrelevant for UK designations).
> - **US:** §284/§289 damages, doctrine of equivalents, IPR/PGR,
>   §101/Alice — different test entirely from UK / EPO.
>
> When non-UK jurisdictions are in scope: "This analysis uses the UK
> framework (PA 1977 / *Actavis*). A product sold in France or Germany needs
> national EU analysis, not a UK claim chart. I can flag the issues a UK
> analysis surfaces, but the infringement and validity calls require
> [jurisdiction]-specific review."

**Decision posture:** this skill never concludes "no infringement." Either:

- "Product practises every element of Claim X as written; Chartered Patent
  Attorney review required before proceeding."
- "One or more elements are not clearly present; attorney review required to
  assess literal infringement and equivalents (*Actavis*)."
- "Claim construction is dispositive on element [Y]; attorney construction
  required before proceeding."

---

## Open questions

Every patent surfaced in the triage should produce a list of open questions
that a real FTO study would answer. Examples:

- Is the patent in force — have UK IPO annual renewal fees been paid to date?
- Are there any pending UK IPO post-grant proceedings, UK revocation actions,
  or EPO oppositions that may affect the claims?
- What did the applicant say about term [X] in prosecution, and does that
  limit the claim?
- Is there a licence already available (standards pool, patent marking,
  open patent commitment by the proprietor)?
- What's the real-world enforcement history of this proprietor?
- Are there SPCs that extend term beyond the patent expiry? (Check UK SPC
  register post-Brexit — UK SPCs are separate from EU SPCs since January 2021.)

---

## Recommended next steps

Bucket by what the triage found:

- **If every element of an independent claim maps to the product (literal read):**
  *Stop and get a Chartered Patent Attorney.* Options typically include formal
  FTO opinion, design-around, licence, challenge validity (revocation at UK IPO
  or Patents Court), or proceed at risk with documented advice.
- **If elements cut both ways or claim construction is dispositive:**
  Full FTO study by a Chartered Patent Attorney. Do not launch on this triage.
- **If the patent appears expired, lapsed on fees, or unenforceable:** Attorney
  confirms the in-force status — the triage does not.
- **If no patents were identified in the search but no database access existed:**
  Formal search is the next step, not a launch decision.
- **Always:** flag additional-damages risk. If the triage surfaces a specific
  patent, the company now has knowledge of it. Proceeding without further
  analysis can support a "flagrant infringement" argument under PA 1977 s.63.
  Counsel should document the path forward.

---

## Output format

Prepend the work-product header from
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER]

# FTO Triage — First Pass (NOT AN OPINION)

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by a Chartered Patent Attorney or registered patent
counsel. Patent infringement is actionable regardless of knowledge or intent
(PA 1977 s.60); proceeding with knowledge of a specific patent can support
additional damages arguments (PA 1977 s.63). A "no obvious blocking patents"
result means the triage didn't find one — it does not mean the product is
clear. A Chartered Patent Attorney evaluates before anyone relies on this for
a product decision.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Subject

- **Product / process / feature:** [description, technical essence]
- **Technical detail relied on:** [what was reviewed]
- **Jurisdictions in scope:** [UK national / EP(UK) / other — per PA 1977 s.60 acts]
- **Timing:** [pre-launch / near-launch / shipping]

## Search scope

- **Databases searched:** [Solve Intelligence / Google Patents /
  Espacenet / UK IPO — or "no database search run"]
- **Query / approach:** [query text, technology classes, keywords, classifications]
- **Date / date window:** [search date; in-force patents + applications
  published since YYYY-MM-DD]
- **Jurisdictions covered by the search:** [list]
- **What wasn't searched:** [named-proprietor sweeps, SEP declarations,
  design patents, SPC register, foreign equivalents — as applicable]

*If no database search was run:* **No patent database search was run.**

## Patents identified

| Patent | Jurisdiction | Proprietor | Priority / Grant | Expiration | In-force? | Source |
|---|---|---|---|---|---|---|
| [number] | [UK/EP/...] | [proprietor] | [dates] | [date] | [yes/no/unverified] | [search result or "user-supplied"] |

## Claim charts — first pass

### [Patent number] — independent Claim [N]

> "[Exact text of Claim N]"

| Element | Practised by the product? | Basis |
|---|---|---|
| [element 1] | [yes/no/possibly] | [mapping or gap] |
| [element 2] | [yes/no/possibly] | [mapping or gap] |

**Literal read:** [every element maps / one or more elements do not clearly
map / claim construction is dispositive on element [Y]]

**Equivalents (Actavis — flag only):** [equivalents read plausible on element
[Y] under *Actavis* — attorney construction required / not plausible / prosecution
history suggests equivalents not available]

**Indirect infringement (PA 1977 s.60(2) — flag only):** [note if any read
depends on contributory infringement — attorney analysis required]

*(Repeat for each independent claim of each selected patent.)*

## Open questions

- [question 1]
- [question 2]

## Signals (not confirmed patents)

- [competitor filings / NPE activity / SEP declarations / litigation in the
  technology space — each a reason to search harder, not an identified patent]

## Recommended next steps

- [full FTO study by Chartered Patent Attorney — first-line recommendation]
- [design-around options if a literal read was found]
- [licence / revocation action / at-risk analysis as counsel directs]
- [routing per `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` —
  patent OC named in the practice profile]

## Additional damages note

This triage surfaces specific patents. Proceeding with the product without
further counsel review after this knowledge can support an argument for
additional damages for flagrant infringement under PA 1977 s.63. The path
forward should be documented by a Chartered Patent Attorney; the business
decision to launch, design around, or licence is informed by a formal FTO
opinion and counsel's judgment, not by this triage.

## Citation verification

Every patent number, claim quote, date, and prosecution fact in this memo must
be verified against the authoritative source (UK IPO register, EPO Online
Register, national equivalent) before relying on it. Claim quotes are the
most common error site — a single word changes the analysis. Do not cite a
result you cannot open.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Launching, continuing to
> sell, or investing in this product based on this triage alone has legal
> consequences — including strict liability for patent infringement (PA 1977
> s.60), with additional damages for flagrant infringement (PA 1977 s.63). A
> Chartered Patent Attorney needs to evaluate before you move.
>
> Here's a brief to bring to a Chartered Patent Attorney — it'll cut the time
> the conversation takes:
>
> [Generate a 1-page summary: the product description, the jurisdictions in
> scope, the search run (and what wasn't searched), the patents surfaced and
> the claim-chart-first-pass reads, the open questions, and the three
> questions to ask the attorney.]
>
> To find a Chartered Patent Attorney: CIPA (the Chartered Institute of Patent
> Attorneys) at cipa.org.uk maintains a public register of Chartered Patent
> Attorneys in the UK. Only registered practitioners may act as patent agents
> and advise on UK patent matters. For EPO prosecution and opposition, a
> European Patent Attorney registered with the EPO is required — the EPO
> register is at epo.org.

Deliver the full triage memo alongside the brief. Do not withhold the analysis.
Flag that the triage itself is a privileged research document (if the header
applies) and should not be forwarded to non-privileged third parties.

---

## Output location

If matter workspaces are enabled and a matter is active, write the output to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`
and surface the path.

Append a one-line entry to the matter's `history.md` if a matter is active.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- **Issue an FTO opinion.** Ever. The loudest guardrail in the plugin.
- **Construe claims.** Where construction is dispositive, it flags the term and
  both plausible constructions. It does not pick one.
- **Adjudicate validity.** It may note known proceedings; it does not opine on
  novelty, obviousness, added matter, or insufficient disclosure.
- **Draft patent claims.** This plugin does not go there; route to a Chartered
  Patent Attorney.
- **Assess damages exposure.** Damages modelling is an expert's job.
- **Handle UPC proceedings.** The UK is not party to the UPC — UPC analysis is
  irrelevant for UK territory.
- **Handle trade-secret or trade mark analysis** — use
  `/ip-legal-uk:infringement-triage` with the right mode.
- **Quote outputs to counterparties or non-privileged audiences.** This is a
  privileged research document.

---

## Tone

Technically precise. Element-by-element. Every flag is specific to a claim
element or a known patent. No hedging prose in the body — the guardrails at
the top and bottom do the scope work, and the analysis does the analysis.
