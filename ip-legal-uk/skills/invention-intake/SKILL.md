---
name: invention-intake
description: >
  Invention disclosure first-pass screen — novelty, obviousness, subject-matter
  eligibility, bar dates, detectability, and strategic value under PA 1977.
  Use when an invention disclosure comes in and needs triage on whether to
  pursue a prior-art search and Chartered Patent Attorney review, investigate
  further, or decline. This screen never says "patentable."
argument-hint: "[paste or describe the invention disclosure — or just the title and I'll ask]"
---

# /invention-intake

**This is a first-pass screen by a non-specialist, not a patentability
opinion.** The screen never concludes that an invention is patentable — it
concludes that it passes the initial screen and warrants a prior-art search
and Chartered Patent Attorney review, that it needs more information, or that
it hits a disqualifier. A prior-art search is a separate step; this skill
does not do one.

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal-uk:cold-start-interview`. If the
   practice profile shows trade mark- or copyright-only (no patent practice),
   say so and route the user elsewhere — this is the wrong tool.
2. Follow the workflow below.
3. Run intake. If the user pasted or uploaded a disclosure, read it. If not,
   ask the seven intake questions in one batch and wait.
4. Run the six screens: novelty signals, obviousness flags, subject-matter
   eligibility (PA 1977 s.1(2) + Aerotel/Macrossan), public disclosure / bar
   dates, detectability, strategic value. Each screen gets a ✓ / 🟡 / 🔴 verdict
   with one-line reasoning.
5. Write the invention screen memo to the matter folder (if a matter is active)
   or the practice outputs folder. Apply the work-product header per role.
6. Bottom-line verdict: **PURSUE** (schedule prior-art search and Chartered
   Patent Attorney review) / **INVESTIGATE** (needs more info on a specific
   open item) / **DECLINE** (state the concrete reason). Never say "patentable."
7. Close with the decision tree and the non-lawyer gate if the role is
   non-lawyer.
8. If the screen hit a public disclosure with UK / foreign rights in scope, flag
   at the top: **time-sensitive**. UK and EPO practice apply absolute novelty
   with limited exceptions — there is very little grace period.

This skill never concludes that an invention is patentable. If uncertain,
flag — a Chartered Patent Attorney decides.

## Examples

```
/ip-legal-uk:invention-intake "a new cache-eviction algorithm that uses a learned model rather than LRU; conceived Q1 this year, not yet disclosed, engineering prototype in internal staging"
```

```
/ip-legal-uk:invention-intake
```

---

## THIS IS A FIRST-PASS SCREEN, NOT A PATENTABILITY OPINION

**Say this at the top of every output. Do not drop it, do not soften it.**

> **This is a first-pass screen by a non-specialist, not a patentability
> opinion.** A patentability opinion requires a prior-art search, full claim
> construction, and the judgment of a Chartered Patent Attorney or registered
> patent agent. This screen does not do a prior-art search, does not assess
> what is in the art, and does not construct claims. It screens for the obvious
> disqualifiers (the invention is already on the market, it was publicly
> disclosed at a conference, it is plainly an abstract method not qualifying as
> an "invention" under PA 1977 s.1(2)) and the obvious go-aheads (new
> mechanism, technical advance, recent conception, in-use secretly). Everything
> in between needs a prior-art search and a Chartered Patent Attorney's review.
> This screen never concludes that something is "patentable" — it concludes
> that it "passes the initial screen, warrants investigation" or that it
> does not.

Under-flagging an invention that should have been filed is a one-way door —
the absolute novelty bar runs in most countries at first public disclosure,
the competitor files first. Over-flagging just means a prior-art search that
comes back empty. Stay on the two-way door side.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is
`✗` (the default for in-house users), skip — skills use practice-level context.
If enabled and there is no active matter, ask: "Which matter is this for? Run
`/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

Invention disclosures are particularly common candidates for **clean-team** or
**heightened** confidentiality at matter-open. Invention content is inherently
sensitive — do not summarise, quote, or reference it outside privileged channels.

---

## Load the practice profile first

**Before reading the disclosure, read
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`.** The practice
profile tells you:

- The company's **patent filing strategy** — offensive, defensive, hybrid, or
  licensing-revenue. This determines the strategic-value bar.
- The **technology areas of interest** — where the company files and where it
  does not.
- The **filing budget posture** — aggressive, selective, or minimal.
- The **approval chain** — who signs off on a filing decision, and who the
  invention gets routed to if it passes the screen (usually the Chartered Patent
  Attorney or outside patent firm named in the practice profile).

If the practice profile shows trade mark-only or copyright-only (no patent
practice), this skill is the wrong tool.

---

## Workflow

### Step 1: Intake the disclosure

If the user pastes or uploads a disclosure, read it. If not, ask — in one
batch, not one at a time:

> To screen this, I need:
>
> 1. **What is the invention?** In plain language — what does it do, what makes
>    it work, what is the key idea.
> 2. **What problem does it solve?** What was broken or missing before.
> 3. **How does it differ from what existed before?** What did people do
>    previously? What does this do differently?
> 4. **Who invented it, and when?** Names and rough conception date. Note: UK
>    and EPO law considers the first to file, not the first to invent — but
>    conception date matters for bar-date calculations and employee invention
>    provisions.
> 5. **Has it been publicly disclosed?** Published, sold, offered for sale,
>    demonstrated at a conference, shown to a customer (NDA or not), posted to
>    a public repo, written up in a paper, included in a product release note.
>    If yes, when and where.
> 6. **Is it in use or planned?** Shipping now? In a limited pilot? On the
>    roadmap? Still on paper?
> 7. **What technology area?** (Software, hardware, mechanical, biotech,
>    method, AI/ML, etc.)

Wait for answers.

### Step 2: Screen against the checklist

Walk the six screens in order. Each produces a per-screen verdict:
`✓ clear`, `🟡 flagged — needs further look`, or `🔴 red flag`.

#### Screen 1: Novelty signals

Does the disclosure describe something new? Not a full novelty analysis — this
screens for self-evident novelty problems.

**Red flags (🔴):**
- "We just applied [known technique] to [new domain]"
- "It's like [existing product] but for [X]"
- "Competitors do something similar" — if the disclosure itself says this, novelty is in question
- The disclosure describes a feature of an existing public product with minor tuning

**Green flags (✓):**
- A new **mechanism** — a new way of doing the thing, not a new application
- A new **combination** that produces an unexpected result
- Solving a problem the field **had not solved** — the disclosure explains why prior approaches failed

**Flagged (🟡):** anything ambiguous. Prior-art search settles it.

#### Screen 2: Obviousness flags

Would a person skilled in the art (PSITA) have arrived at this combination based on what's known? This is a screen, not a PA 1977 s.3 analysis — flag for further investigation.

**Red flags (🔴):**
- Combining **known elements in a predictable way**
- **Routine optimisation** — tuning a known parameter
- **Obvious to try** with a reasonable expectation of success

**Green flags (✓):**
- **Teaching away** — prior art said this approach wouldn't work
- **Unexpected result**
- **Long-felt need** — problem was known, attempts to solve it had failed

#### Screen 3: Subject-matter eligibility (PA 1977 s.1(2) + Aerotel/Macrossan)

UK patent law excludes from patentability certain things "as such": discoveries, scientific theories, mathematical methods, mental acts, methods of playing games, schemes, rules and methods for performing mental acts, doing business, presenting information, and (importantly) computer programs as such (PA 1977 s.1(2)).

**The key UK/EPO test for software and AI inventions:**

The Court of Appeal in *Aerotel Ltd v Telkom Ltd; Macrossan's Application* [2006] EWCA Civ 1371 sets out a four-step test now overlaid with the EPO's "technical character" approach: (1) properly construe the claim, (2) identify the actual contribution, (3) ask whether the contribution falls solely within excluded subject-matter, (4) check whether the contribution is actually technical in nature.

The EPO (relevant because UK patents are frequently filed via the EPO route) applies a "technical effect" requirement — software inventions are eligible if they produce a technical effect going beyond the normal physical interactions between the program and the computer. The EPO is generally MORE permissive than UK domestic practice for software/AI, particularly on the "computer program as such" exclusion.

**Red flags (🔴) for PA 1977 s.1(2):**
- Pure **business method** — "a method of pricing, scheduling, organising" without a technical implementation
- **Mathematical algorithm** on its own
- **Presentation of information** — displaying data differently, UI improvements
- AI/ML invention where the claim is the **function** (recommend, classify, predict) without the specific technical means

**Green flags (✓) for software/AI inventions:**
- Technical improvement to the **computer itself** — new architecture, new training technique, new hardware/software interface
- **Specific technical means**, not just results
- Improvement to a **technical field** (image processing, compression, cryptography, robotics)

**Anything borderline gets a 🟡 with "s.1(2) / Aerotel — route to Chartered Patent Attorney for eligibility analysis."** A non-specialist should not call a close UK s.1(2) question.

For **biotech / diagnostic** inventions, also flag if the claim recites:
- A method of treatment of the human or animal body by surgery or therapy, or a diagnostic method (*Note:* patentable *second medical use* claims are an exception under PA 1977 s.4A — flag and route to specialist)
- A naturally occurring substance without inventive step in its isolation or application

> **UK/EPO vs. US.** The US §101/*Alice/Mayo* framework is materially different from UK/EPO. An invention that screens 🔴 under *Alice* may be eligible under UK/EPO practice. An invention that seems clear under UK/EPO may still have *Alice* issues for US filing. Do not decline for all jurisdictions based on a UK s.1(2) screen alone if the company has US filing plans — note the issue and route both tracks to a Chartered Patent Attorney.

#### Screen 4: Public disclosure / bar dates

**This is the most urgent screen.** UK and EPO patent law apply an **absolute novelty** rule — any public disclosure anywhere in the world before the filing date destroys novelty for the UK and EPO.

**CRITICAL: the UK grace period is extremely limited.** Unlike US law (35 USC §102(b), one-year grace period), there is no general grace period under UK / EPC law for pre-filing disclosures. The only partial exception is:

- **UK national filing:** PA 1977 s.2(4) excludes from anticipation disclosures made within 6 months before the filing date if the disclosure was due to (a) an evident abuse in relation to the applicant, or (b) display at an international exhibition as defined. These are narrow exceptions. A conference presentation, a product launch, a journal paper, or a public demo — even in the week before filing — destroys novelty under EPC and UK practice with no grace.

Categorise the disclosure status:

**🔴 LIKELY BARRED:**
- Publicly disclosed anywhere, before filing — absolute novelty rule. **Even one day before filing is fatal.** There is no general grace period.
- An offer for sale made before filing — UK law follows EPC absolute novelty and will typically treat this as prior art.

**🟡 CLOCK IS RUNNING (or urgency to investigate):**
- Public disclosure imminent — e.g., conference in two weeks, product launch in two months. File before any public disclosure; do not wait.
- Disclosure was within the narrow PA 1977 s.2(4) exception — confirm with a Chartered Patent Attorney immediately.

**✓ CLEAR (provisionally):**
- No public disclosure. Confidential disclosures to customers under NDA, internal use, beta releases to named parties under NDA — usually not "public" for PA 1977 purposes, but depends on the facts. When the disclosure was to an external party, even under NDA, flag the specifics for the prosecution team.

**Ask specifically about:**
- Conference submissions, preprints, arXiv / SSRN / bioRxiv posts
- Public GitHub commits, documentation, or release notes
- Customer demonstrations not covered by a signed NDA
- Product sales, beta releases, or offers for sale
- Investor presentations not under NDA

**URGENT: if any public disclosure has already occurred**, flag at the top of the memo in red:

> ⚠️ TIME-SENSITIVE: A public disclosure appears to have occurred on [date]. Under UK/EPC absolute novelty rules, any patent application must be filed BEFORE this disclosure. If the disclosure occurred before this intake, novelty may already be destroyed for UK and EPO filings (no general grace period applies). Route to a Chartered Patent Attorney immediately for assessment. For US filing, a one-year grace period from the date of applicant's own disclosure may preserve the US application — confirm with US patent counsel.

#### Screen 5: Detectability

If a competitor were to infringe, could you tell? An invention that's practised in secret may be better protected as a **trade secret** under English law of confidence or the Trade Secrets (Enforcement, etc.) Regulations 2018.

**🔴 Low detectability flags:**
- Server-side algorithm with no observable output pattern
- Internal manufacturing process
- Data-pipeline or analytics methodology running inside a competitor's infrastructure
- Training data composition or training technique for an ML model

For these, flag for the **patent vs. trade secret decision**. Route to whoever in the practice profile owns trade-secret classification decisions.

**✓ High detectability:**
- Consumer product — visible in the product
- Published API, SDK, protocol
- Physical mechanism reverse-engineerable from a distributed product

#### Screen 6: Strategic value

Does this align with the company's patent strategy? This is company-specific:

- **Offensive strategy:** is this assert-worthy? A narrow claim easily designed around has lower offensive value.
- **Defensive strategy:** does this cover a technology area where competitors are filing? A defensive filing where nobody files is wasted spend.
- **Licensing / revenue strategy:** is this licensable and commercially meaningful?
- **Core vs. peripheral technology:** core product differentiation vs. incidental feature.
- Is the technology area on the company's list of **tech areas of interest** from the practice profile?

Also consider the **employee invention provisions under PA 1977 ss.39–43**. If the inventor is an employee, the employer normally owns the invention if it was made in the normal course of the employee's duties. However, PA 1977 s.40 provides a right to an employee to claim compensation where an employer-owned patent (or patented invention) is of *outstanding benefit* to the employer. This is rare but not unknown. Flag for the Chartered Patent Attorney if the invention appears commercially significant and the inventor may claim outstanding-benefit compensation.

### Step 3: Assemble the invention screen memo

Format:

> **Invention screen memo — [invention title]**
>
> **Bottom line: [PURSUE / INVESTIGATE / DECLINE]**
>
> *[One sentence — the reason in plain language.]*
>
> ---
>
> ### Screen results
>
> | Screen | Verdict | Notes |
> |---|---|---|
> | Novelty signals | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Obviousness flags | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Subject-matter eligibility (PA 1977 s.1(2) / Aerotel) | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Public disclosure / bar dates | [✓ / 🟡 / 🔴] | [one-line reasoning + dates] |
> | Detectability | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Strategic value | [✓ / 🟡 / 🔴] | [one-line reasoning, referenced to profile] |
>
> ---
>
> ### Open questions
>
> - [question]
>
> ### Next steps (decision tree)
>
> Pick one and I'll help you build it out:
>
> 1. **Commission the prior-art search** — I'll draft the search request for
>    [Chartered Patent Attorney / search vendor] with the claim concepts,
>    inventors, technology classification, and any known references.
> 2. **Go back to the inventor for more facts** — I'll draft the follow-up
>    questions on [specific open items above].
> 3. **Route to a Chartered Patent Attorney for s.1(2) / patent-vs-trade-secret
>    judgment** — I'll draft a transmittal summarising what the screen found
>    and what specialist judgment is needed.
> 4. **Decline and send the standard thank-you** — I'll draft the inventor
>    thank-you and archive the disclosure with the declination reason.
> 5. **Flag for trade secret instead** — I'll draft a note to whoever owns
>    trade-secret classification explaining why a trade-secret approach is a
>    better fit (noting the Trade Secrets Regulations 2018 and English law of
>    confidence framework).

Apply the work-product header per role.

### Step 4: Recommend the bottom-line verdict

One of three:

- **PURSUE** — enough screens are clear (or clearly fixable) to warrant a
  prior-art search and Chartered Patent Attorney review. This is NOT "patentable"
  — it is "passes the initial screen, investigation warranted."
- **INVESTIGATE** — one or more screens flagged something that needs more
  information or specialist review before a pursue/decline decision.
- **DECLINE** — a screen hit a fatal flag (absolute novelty bar has already run,
  plainly obvious, plainly excluded under s.1(2), outside the company's technology
  areas of interest, fundamentally undetectable with no trade-secret path).

A DECLINE should always be backed by a concrete reason: "The invention was
publicly disclosed at the AI Summit on [date]. Under UK/EPC absolute novelty
rules (no general grace period), patent protection for the UK and most other
countries is not available" is a DECLINE reason. "Not patentable" is not.

## Guardrails

**Never say "patentable."** The closest you can come is "passes the initial
screen, warrants further investigation." Patentability is a conclusion a
Chartered Patent Attorney reaches after a prior-art search and claim
construction.

**Never do a prior-art search in this skill.** A web search for "does this
already exist" is not a prior-art search — it's a sanity-check. If you want
to sanity-check novelty, say so explicitly and flag it as `[web — verify]`.

**Defer on s.1(2) calls.** For anything borderline under *Aerotel*, flag for
specialist review. UK s.1(2) is where practitioners routinely disagree.

**Flag detectability before strategic value.** An undetectable invention that
would be "high strategic value" as a patent is usually higher strategic value
as a trade secret under English law of confidence / Trade Secrets Regulations
2018. Do not recommend PURSUE on an undetectable invention without addressing
the trade-secret alternative.

**Urgent cases get urgent flagging.** If the screen hits any public disclosure
with foreign rights in scope — or any public disclosure at all — flag at the
top of the memo. UK / EPC absolute novelty is binary: file before disclosure
or rights are gone. No general grace period.

**Employee invention provisions.** For employee inventors, note PA 1977 ss.39–43.
The employer usually owns the invention (s.39), but outstanding-benefit
compensation claims (s.40) can arise. Route to the Chartered Patent Attorney
for any commercially significant employee invention.

## Non-lawyer gate

If the role is **non-lawyer** (with or without professional access):

> **This is a screening tool for your disclosure, not a patentability opinion.
> The decision about whether to file — and how — belongs to a Chartered Patent
> Attorney or registered patent agent. If this screen says PURSUE or INVESTIGATE,
> your next step is not to file or draft claims; it is to share this memo (and
> the underlying disclosure) with a Chartered Patent Attorney. UK and EPO law
> apply absolute novelty — any public disclosure before filing destroys patent
> rights in most countries with no general grace period.**
>
> To find a Chartered Patent Attorney in the UK: CIPA (cipa.org.uk) maintains
> a register of qualified practitioners. For EPO filings, a European Patent
> Attorney registered with the EPO is required. The IPO's website (gov.uk/topic/
> intellectual-property/patents) has general guidance for first-time applicants.
