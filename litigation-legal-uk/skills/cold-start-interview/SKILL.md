---
name: cold-start-interview
description: House cold-start for the UK litigation plugin — branches by role (in-house, firm solicitor, barrister, solo) and side (claimant, defendant, both), captures risk calibration, landscape, and house style, and writes the practice profile CLAUDE.md. Use on a fresh install, when the user wants to set up or redo the practice profile, or to re-check available integrations.
argument-hint: "[--redo | --check-integrations]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If already populated and no `--redo`, ask before overwriting.
2. Follow the workflow and reference below.
3. Run Part 0 (role, side, integration check). The interview branches by role and side.
   - **Role** routes the practice profile structure: **in-house** (portfolio of matters, external solicitors oversight, reserve methodology, board/audit reporting), **firm-solicitor** (case work — matter context, case theory and pivot fact, seed skeleton argument in house style, disclosure/LPP-log setup), **barrister** (instructions, brief work, skeleton argument style, advocacy notes), or **solo** (caseload + conditional-fee/retainer economics + client expectations + limitation tracking, then the case-theory and brief-style sections).
   - **Side** routes calibration vocabulary: **claimant** (asserting, case value, CFA/DBA, limitation cliff), **defendant** (responding, exposure, reserves where applicable, insurance tender), or **both/varies** (captures a default and lets per-matter skills re-ask).

   After Part 0, walk the sections that match the selected role. Do not run the in-house path for solo users. Offer defaults; capture freeform overrides. Ask for seed documents at each section.
4. Surface gaps. If the user doesn't have an articulated risk framework or reporting threshold, note it and offer to think through it now or leave `[PLACEHOLDER]` to fill later.
5. Migration: if a populated CLAUDE.md exists at `~/.claude/plugins/cache/uk-legal-plugins/litigation-legal-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.
6. Write `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. Date the footer.
7. Confirm with the user before finalising: "Here's what I captured — anything wrong?"

## Flags

- `--redo` — re-run the full interview and overwrite `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`.
- `--check-integrations` — re-scan available MCP connectors and refresh the `## Available integrations` table without re-running the full interview.

When probing: only report ✓ if an MCP tool call actually succeeded. Never report ✓ based on `.mcp.json` declarations alone.

---

# Cold-Start Interview: UK Litigation

## Purpose

Every matter intake, every chronology build, every skeleton argument draft, every status rollup reads from this file. If the frame isn't captured, the plugin makes weaker triage calls and the user has to think from scratch each time. This interview fills the frame once so everything downstream gets sharper.

The plugin serves four distinct UK litigation roles — in-house counsel managing a portfolio of matters, firm solicitors doing the underlying skeleton argument / disclosure / witness statement work, barristers working from instructions, and sole practitioners running a caseload directly. The vocabulary is different for each, and the interview branches to match.

The interview also asks which side the user mostly represents — claimant (asserting claims), defendant (responding to claims), both, or varies by matter. Risk calibration, Letter Before Action posture, disclosure stance, and chronology framing all differ by side.

**Tone:** socratic, not checklist. If the user doesn't have a written framework, this is often the thing that forces articulation.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → offer to start fresh or resume.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation. If confirmed, skip the company questions.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation, ask the company questions and write them to the shared profile, then continue with the plugin-specific questions.

## Install scope check

Before the orientation, if the working directory is inside a project (not the user's home directory), flag it once and ask the user to confirm before proceeding.

## Before the interview starts

Open with the fork-first preamble. Keep it to 3-4 short lines. Ask quick-or-full before anything else.

> **`litigation-legal-uk` is for people who work UK litigation — managing a portfolio of matters in-house, drafting skeletons and handling disclosure at a firm, instructed as a barrister, or both as a sole practitioner.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role (in-house / firm-solicitor / barrister / solo), practice setting, side default (claimant / defendant), and active matter count, plus working defaults for risk calibration, house skeleton style, and LPP conventions. **15 minutes** adds your real severity × likelihood bands, settlement-authority ladder (in-house) or fee economics (solo), external solicitors roster, house skeleton style from a seed skeleton, LPP-log format, Letter Before Action templates, and landscape notes.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

**Quick start path:** ask only Part 0 and the path branch. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. Run `/litigation-legal-uk:cold-start-interview --full` anytime to do the whole interview."

## Part 0: Who's using this + role routing

### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every matter briefing, chronology, LPP log, and Letter of Claim draft — lawyer outputs get the LPP header, non-lawyer outputs get the "research notes, review with a solicitor/barrister" header.)
>
> 1. **Solicitor, barrister, or other authorised legal professional** — practising lawyer, paralegal, legal ops working under authorised-professional oversight.
> 2. **Non-lawyer with solicitor/barrister access** — founder, business lead, contracts manager, HR, procurement; you have an in-house or external solicitor you can consult.
> 3. **Non-lawyer without regular solicitor/barrister access** — you're handling this yourself.

If the answer is 2 or 3, say this once:

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for solicitor/barrister review, not as verdicts.**
> 2. **I'll pause before steps that have legal consequences** — sending a Letter Before Action, responding to a witness summons or third-party disclosure order, issuing or releasing a preservation notice, filing a skeleton argument, submitting a privilege/LPP log, designating documents in disclosure, closing a matter, accepting a settlement.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organisation, structure — and licensed legal judgment about your specific situation.

If the answer is 3, add referral guidance for the SRA/Bar Standards Board referral services, Citizens Advice, and local law centre access.

### Role (the branching question)

> **How do you work UK litigation?**
>
> **(a) In-house managing a portfolio** — matters, external solicitors, CPR deadlines, Letters of Claim, preservation notices. You own many matters at once, most of which are run by external firms.
>
> **(b) At a firm as a solicitor — skeleton drafting, disclosure, witness statements, document review** — you're the solicitor responsible for actually producing the work product.
>
> **(c) Barrister working from instructions** — you're briefed by a solicitor firm; your deliverables are skeleton arguments, advices, and advocacy.
>
> **(d) Sole practitioner running a caseload** — you intake, triage, advise, and draft. CFA / DBA / retainer economics. No partner above you; no in-house reserve / board-memo layer.
>
> **(e) Something else** — describe in a sentence.

Record as `in-house | firm-solicitor | barrister | solo | other`. Branching rules:

- `in-house` → **In-house path** (Pillars 1–3 below). Skip firm-solicitor, barrister, and solo sections.
- `firm-solicitor` → **Firm-solicitor path** (Parts A–D). Skip in-house portfolio / OC / board-memo questions and solo caseload / economics questions.
- `barrister` → **Barrister path** (Parts B1–B3): instructions receipt, brief/instructions structure, skeleton argument house style, advocacy notes — then also run Parts A (matter) and C (seed skeleton).
- `solo` → **Solo path** (Sections S1–S3) — caseload, client expectations, CFA/DBA or retainer economics, practice management — **then** the Firm-solicitor path (Parts A–D) because sole practitioners still write skeletons and work cases.
- `other` → ask for a one-sentence description, then pick the closest branch.

### Which side do you mostly represent?

> **Which side do you mostly represent?**
>
> **(a) Claimant / applicant** — you bring claims for individuals or businesses. Letters of Claim are assertions you draft and send. Disclosure is offensive. Limitation is a cliff you work against.
>
> **(b) Defendant / respondent** — you defend businesses or individuals against claims. Letters of Claim are received and triaged. Disclosure is defensive. Exposure is assessed, reserved (in-house), tendered to insurers.
>
> **(c) Both** — your practice regularly includes both. Ask for a default (claimant or defendant).
>
> **(d) Varies by matter** — no strong default; every matter gets asked.

Record under `## Side` in the practice profile (`claimant | defendant | both [default claimant/defendant] | varies`).

### Practice setting

> Which best describes where you're practising?
>
> 1. Sole practitioner
> 2. Small firm (2–10)
> 3. Midsize firm
> 4. Large firm / Magic Circle / Silver Circle
> 5. In-house (company legal department)
> 6. Government / Crown / Regulatory body
> 7. Legal aid / law centre / clinic
> 8. Chambers (barrister)
> 9. Other

### What's connected?

> This plugin can work with: DMS (iManage), document storage (Google Drive, SharePoint, Box), Gmail, scheduled-tasks, CLM (Ironclad), disclosure platforms, legal research (uk-legal MCP, govuk MCP). Let me check which connectors you have configured.

Check what's actually connected, not just configured. Report ✓ only on a successful tool response. Report ⚪ for configured-but-unverified. Never report ✓ based on configuration alone.

---

## In-house path (role == `in-house`)

> I want to capture the frame you triage matters against — your risk calibration, the dispute landscape, and how you write. Once, so every matter intake reads from it.
>
> I'll also ask for seed documents along the way — prior board memos, reserve memos, preservation notice templates, exemplar Letters Before Action, a sample risk memo.

### Pillar 0 — Company profile

Team-level context. If another UK legal plugin already has a `## Company profile` block populated, copy it here rather than re-enter.

- Org / legal entity (English / Welsh / Scottish / NI incorporated entity type)
- Industry
- Public / private / subsidiary; listed (LSE, AIM, other market)?
- Regulated status (FCA, ICO, Ofcom, CMA, PRA, other)
- Core jurisdictions (England & Wales / Scotland / Northern Ireland / Channel Islands / international)
- Headcount + legal team size
- Key internal contacts (GC, CFO, HR lead, Comms, CISO, Board lit/audit chair) — names + when to loop in
- This counsel's name and reporting line

### Pillar 1 — Risk calibration

> Before the structured questions: do you have an existing risk-calibration memo, a reserve-policy document, or an external solicitor billing-guidelines doc I can read?

**Risk appetite** — in a sentence, how does this company approach litigation?

**Severity × likelihood** — offer the default 3×3. Severity bands (sterling and non-monetary triggers). Likelihood bands.

**Materiality thresholds** — reserve trigger, board/audit committee, GC-only escalation. *Seed doc opportunity.*

**Settlement authority** — sterling ladder, special carve-outs (structural relief requires board regardless of amount).

**Plain-English escalation.** Ask directly:

> When a matter needs something above your authority — a settlement offer above your band, a Letter Before Action you can't answer alone, a preservation decision that needs the GC — who does that go to? Give me a name, a role, or "I decide myself."

**Insurance profile** — lines in force (D&O, EPL, Cyber, GL/PI, ATE), insurers, limits, excesses, tendering protocol.

### Pillar 2 — Landscape

- Business context — one-paragraph on what we do and why we get sued.
- Dispute patterns — matter types, frequency, posture.
- Frequent adversaries.
- External solicitors bench — firms, lead solicitors, matter type, rate posture, retainer / engagement status. *Seed doc:* external solicitor guidelines. (This feeds /oc-status.)
- Frequent fora — courts and arbitration forums we actually see (King's Bench Division, IPEC, CAT, LCIA, ICC, etc.).
- Document storage — where matter docs live, default matter folder pattern, how docs get shared with external solicitors.
- Conflicts clearance — how this shop runs conflicts; who does it; hard block on intake or parallel.

### Pillar 3 — House style

- Board / audit committee memo — format, tone, cadence.
- Reserve memo — format and approver.
- External solicitor directives — email format, cadence, budget posture.
- LPP conventions — marking; default subjective-call posture (mark and flag); review mechanic.
- Preservation notices — template, issuance protocol, refresh cadence.
- Escalation — channel norms, subject-line convention.
- Letter Before Action practice — CPR pre-action protocol compliance note; insurance-tender timing; materiality threshold for matter creation.

---

## Solo path (role == `solo`)

*Solo practitioners run this path **and** the Firm-solicitor path that follows.*

> Solo practice is its own frame — caseload, client expectations, retainer or CFA/DBA economics, practice management. The in-house world (board memos, external solicitors oversight, settlement-authority ladders up to a GC) doesn't apply here.

### Section S1 — Practice shape and caseload

- Caseload size — roughly how many active matters do you carry at once?
- Matter mix — rough percentages: claimant vs defendant, practice areas.
- Jurisdictions — England & Wales / Scotland / Northern Ireland / specialist courts.
- Typical case duration.
- Capacity flags.

### Section S2 — Client expectations and economics

**Fee structure.** Pick the one that fits most of your work:

- **Conditional Fee Agreement (CFA)** — standard percentage of recovery? ATE insurance posture? Costs-shifting expectations?
- **Damages-Based Agreement (DBA)** — percentage and uncapped vs. partial?
- **Hourly / retainer**: hourly rate, standard retainer, client-account mechanics.
- **Flat fee**: which matter types, and the fee range.
- **Mixed**: describe the mix.

**Client expectations.** How often do you update clients? What form do updates take? What's your default posture on settlement conversations?

**When you call for help.** Sole practitioners don't have a GC or a partner above them, but most have someone — counsel at the Bar, a professional indemnity panel solicitor, a local Law Society committee. Who do you call for a second opinion?

### Section S3 — Practice management and landscape

- Limitation tracking — how do you track limitation cutoffs across the caseload?
- Practice management software — Clio, LEAP, Perfect Practice, paper files, other.
- Document storage — where do matter documents actually live?
- Frequent fora.
- Frequent adverse parties / solicitors.
- Conflicts clearance.

### Solo house style

- Client update — format, tone, cadence.
- Retainer / CFA / engagement agreement — template.
- LPP conventions.
- Preservation notices — template if any.
- Letter Before Action practice — CPR protocol compliance note.

After Section S3, continue to the **Firm-solicitor path** below. Sole practitioners write skeleton arguments, build chronologies, and handle disclosure like firm solicitors do.

---

## Firm-solicitor path (role == `firm-solicitor` or `solo`)

> Before I touch a document, I need the theory. What's our story? What's theirs? What does the case turn on? Then I need to see how your firm writes — a skeleton argument you're proud of.

### Part A: The matter (2 min)

- Matter name, client, case number, court
- Our side (claimant / defendant)
- Partner and supervising solicitor (skip if solo / small without hierarchy)
- Stage (pre-action, pleadings, disclosure, witness statements, applications, trial prep)
- Key dates coming up

### Part B: The theory (3–4 min)

> Tell me our theory of the case. Not the Particulars of Claim — the story. If you had to tell the judge why we win in two sentences, what are they?

- Our theory in a paragraph
- Their theory in a paragraph
- **The pivot fact** — the fact the case turns on
- Key facts for us
- Key facts against us
- The legal issue that matters most

### Part C: Seed documents (3–4 min)

> Two things:
>
> 1. **The case theory memo**, if one exists.
> 2. **A prior skeleton argument in house style.** Not from this case — any case. The best one you've got. I'll learn your citation style (OSCOLA), structure, tone, how you organise arguments.

**From the skeleton:** OSCOLA citation format, section structure, heading conventions, tone (measured / assertive), length norms (typical page/word count for interim vs. trial).

### Part D: Disclosure and document review setup (1–2 min)

> Before the questions: do you have an LPP-log format, a chronology format, or a review-protocol doc I can read?

- Disclosure platform (if any)
- Review protocol — coding categories, who makes LPP calls
- LPP log format (for CPR Part 31 extended disclosure or standard disclosure)
- Key custodians and date range
- Whether CPR PD 51U (extended disclosure pilot) applies

---

## Barrister path (role == `barrister`)

*Barristers run Parts B1–B3, then also Parts A (the matter) and C (seed skeleton).*

### Part B1: Instructions intake

- How are you typically instructed — via solicitor, direct access, public access?
- What does a brief/instructions pack typically contain in your practice?
- Preferred format for instructions to you (email with attachments / formal brief / e-bundles)?

### Part B2: Brief / instructions structure

- Typical work products from instructions: written advice, skeleton argument, counsel's note, draft pleadings?
- How do you return deliverables — via chambers email, secure platform, PDF?

### Part B3: Advocacy notes

- Which courts do you regularly appear in?
- Oral or written advocacy style preferences?
- How do you structure openings and closings?

---

## Before writing — re-read

Before committing the plugin config, re-read every captured answer. Catch contradictions, drifted specifics, and skipped gaps worth naming.

## Writing the practice profile

Write using the template at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` as the section scaffold. Fill every section captured; leave `[PLACEHOLDER]` for sections the user skipped. Date the footer.

**Section gating by role:**

- `in-house` → full in-house structure (Company profile, Risk calibration with reserve / board-memo rows, External solicitors bench, Board/audit committee memo). Omit or mark N/A for solo-only sections.
- `firm-solicitor` → firm-world structure (case theory, pivot fact, partner/supervisor review, seed skeleton). Omit reserve / board-memo sections; omit solo fee / retainer sections.
- `barrister` → chambers structure (instructions style, brief format, advocacy notes, seed skeleton) plus Parts A and C from the firm-solicitor path.
- `solo` → solo structure (caseload, fee structure, client expectations, limitation tracking, CFA/retainer, practice management) **plus** the firm-solicitor sections. Omit in-house reserve / board-memo / settlement-authority-ladder-to-GC sections entirely.

**LIMITED DATA flag:** if fewer than 10 seed documents were shared, add a `> LIMITED DATA` note at the top.

## Gap surfacing

After the interview, before writing, summarise and **wait for an answer**:

> Here's what I captured. Gaps I noticed:
> - [list any skipped sections, placeholders left blank, questions where the user said "come back later"]
>
> Want to fill any of these now, or leave them as placeholders?

## After writing

**Show what this plugin can do.** Before closing, offer the tailored list:

> **Here's what I'm good at in UK litigation practice:**
>
> - **Intake a new matter** — Uniform intake questions, writes matter.md + history.md, appends to the portfolio log. Try: `/litigation-legal-uk:matter-intake`
> - **Triage an inbound Letter Before Action** — Options analysis, portfolio cross-check, handoff to matter intake if it graduates. Try: `/litigation-legal-uk:demand-received`
> - **Draft a Letter of Claim** — LPP / settlement-communication gate, .docx output, post-send checklist, matter-creation offer. Try: `/litigation-legal-uk:demand-draft`
> - **Prepare for cross-examination** — Docs + topics + impeachment + exhibits, tied to case theory. Try: `/litigation-legal-uk:witness-examination-prep`
> - **Issue or refresh a preservation notice** — Draft the notice, update the log, schedule a refresh. Try: `/litigation-legal-uk:legal-hold`
> - **Portfolio rollup** — Risk distribution, upcoming CPR deadlines, stale matters across the active portfolio. Try: `/litigation-legal-uk:portfolio-status`
>
> **My suggestion for your first one:** Run `/portfolio-status` — it shows you at a glance where the portfolio sits, and it's zero-input to try.

### Close with the "you can change anything later" note

> "Your practice profile is at `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` — a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change
> - Run `/litigation-legal-uk:cold-start-interview --redo` for a full re-interview
> - Run `/litigation-legal-uk:cold-start-interview --check-integrations` to re-check what's connected
>
> The sections people adjust most: for in-house, the **severity × likelihood thresholds** and the **external solicitors bench**; for firm solicitor, the **case theory** (especially the pivot fact) and the **house skeleton style** extracted from the seed skeleton; for sole practitioner, the **fee structure** (CFA percentage or hourly rate) and the **side default** (claimant / defendant) — a wrong default there skews every Letter Before Action and chronology output."

### Before your first matter

**Connect a research tool.** Without one, I'll flag every citation as unverified — with one, I verify them against a current database. Connect the uk-legal MCP and govuk MCP in your Claude Code config.

### Your practice profile learns

> **Your practice profile learns.** It gets better as you use the plugins. When a skill's output feels off, that's usually a position to tune — the output will tell you which one. Run `/cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.

## What this skill does not do

- Decide the framework for the user. Defaults are starting points; the user's judgment is the actual content.
- Pretend gaps aren't there.
- Fight the user. If they say "I don't have that yet," note it and move on.
- Read personal `~/CLAUDE.md` or other ambient context without asking.
