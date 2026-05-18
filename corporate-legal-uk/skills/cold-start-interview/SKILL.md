---
name: cold-start-interview
description: >
  House cold-start interview (request list + prior memo), or --new-deal for
  deal-specific context. Modular: identifies which practice areas apply (M&A,
  Board & Secretary, Public Company, Entity Management), then asks targeted
  questions for each active module and writes only the relevant sections to the
  plugin config under UK law (Companies Act 2006, English M&A practice, FCA/AIM,
  Companies House). Use on fresh install, when CLAUDE.md still has [PLACEHOLDER]
  markers, when starting a new deal, or to re-check integrations or refresh a
  module.
argument-hint: "[--redo | --new-deal | --check-integrations | --module [m&a | board | public | entities]]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If `--new-deal`, skip to per-deal setup. If `--check-integrations`, skip the interview — re-run only the Part 0 `What's connected?` check and rewrite the `## Available integrations` table in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.
2. Run the interview below (Part 0 first — role + integrations — then modules).
3. Seed docs: diligence request list + one prior issues memo.
4. Extract: categories, thresholds, memo format, AI tool config.
5. Migration: if a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/corporate-legal-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and tell the user what was migrated.
6. Write `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` (create parent directories as needed). For `--new-deal`, write `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code]/deal-context.md`.

---

## Purpose

UK corporate counsel roles vary as much as anywhere: a solo GC at a 50-person startup runs M&A under the Companies Act, manages the cap table, and secretaries the board. A corporate counsel at a FTSE 100 might own only inside information management and the disclosure committee process. This interview finds out which areas are live for you and builds only the relevant practice profile — nothing left blank that doesn't apply.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo` or `--module [name]`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/uk-legal-plugins/corporate-legal-uk/*/CLAUDE.md` but not at the config path, copy it forward to the config path before proceeding.

- `--redo` — full re-interview, overwrites all sections
- `--module [m&a | board | public | entities]` — add or refresh a single module
- `--new-deal` — skip house setup, go straight to per-deal context (M&A module only)

---

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation and fork, ask the company questions and write them to the shared profile (per the template at `references/company-profile-template.md` in the plugin root), then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other legal plugins will read it and skip these questions."

The company questions that belong in the shared profile (and should NOT be re-asked if it exists): practice setting, company name, industry, what-you-sell, size, jurisdictions, regulators, risk appetite, escalation names. The plugin-specific questions (playbook positions, review framework, house style, supervision model, etc.) stay per-plugin.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead — see QUICKSTART.md. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding: continue with project scope, or pause to reinstall user-scoped. If the working directory *is* the user's home directory, skip this check silently.

## Before the interview starts

Before asking anything else, show the fork-first preamble — 3-4 short lines, no longer:

> **`corporate-legal-uk` is for people who support M&A deals under English law, board and corporate governance under the Companies Act 2006, public company compliance (FCA/AIM), and entity management at Companies House.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, practice setting, jurisdiction (England & Wales / Scotland / NI), and module selection (M&A, board, public, entity management), plus working defaults for materiality thresholds, issues-memo format, board-minutes format, and disclosure schedule format. **15 minutes** adds your real materiality thresholds, house resolution and minutes formats from seed documents, your entity list and Companies House compliance cadence, deal-team briefing cadence, and escalation matrix.
>
> Quick or full? (Upgrade any time with `/corporate-legal-uk:cold-start-interview --full`.)

Wait for the user's pick before showing anything else.

## After the user picks quick or full

Once the user has chosen, orient them before the first interview question:

> "This plugin maintains your practice profile (materiality thresholds, resolution style, board format), per-deal folders with diligence grids, closing checklists, disclosure schedules, and a Companies House compliance calendar. It supports your UK corporate legal practice — M&A diligence under English law, board resolutions under CA2006, entity compliance at Companies House, closing checklists with CMA / FCA / Panel conditions — in your house format. This setup interview learns which of those areas are live for you and how you actually run them. It writes that into a plain-text file the plugin's skills read from every time. Everything you answer can be changed later. Once it's done, the plugin will work the way you work, not the way a generic template does."
>
> Then: "Ready? A few quick questions first, then we'll go deeper on the modules that apply."

**Why this matters.** Every command in this plugin reads from the configuration this interview writes. A generic configuration gives you generic output — a default materiality threshold, a default issues-memo format, a default resolution style, a default closing-checklist structure. Telling the plugin how you actually run M&A, board, public, or entity work is what makes the difference between "a UK corporate AI tool" and "a tool that works the way you work." The more specific your answers — your real materiality cuts, your real resolution language, your real house format — the more the outputs will look like they came from your desk.

**Fresh professional profile.** Setup builds a fresh professional profile from the user's answers and documents they explicitly share. It does not read the user's personal Claude history, unrelated conversations, or their home-directory CLAUDE.md. If something relevant surfaces in the current conversation context (e.g., they mentioned the company earlier), ask before using it — do not fold anything personal into the corporate practice profile unless the user types it or approves it.

Corollary: the interview's inputs are the user's typed answers and documents they explicitly share. Do not pull from ambient context, prior sessions, or user memory to fill in gaps.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — company description, playbook, escalation matrix, style guide, handbook, jurisdiction list, matter portfolio — prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. One question with 5 subparts is 5 questions. The test: can the user answer without scrolling? If the questions don't fit on one screen, it's too many.

**Pause for real answers.** Some questions are quick (entity type, exchange, fiscal year end). Others need the user to type, describe, or upload (prior issues memo, board minutes, resolution precedent, org chart). When a question needs more than a quick tap:

- **Ask and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the user responds.
- **For uploads (issues memo, minutes, resolutions, org chart):** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in your practice profile so you can fill it later." Then actually wait.
- **Before writing the practice profile:** review the interview and list any questions that were skipped or answered with placeholders. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait.
- **Never** write a practice profile with silent gaps.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' and I'll save your progress. Run `/corporate-legal-uk:cold-start-interview` again later and I'll pick up where you left off." When the user pauses, write a partial configuration with a `<!-- SETUP PAUSED AT: [section name] — run /corporate-legal-uk:cold-start-interview to resume -->` comment at the top.

---

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration. A wrong fact written into CLAUDE.md propagates into every future output; catching it here is one of the highest-leverage moments in the product.

## The interview

### Opening

> Before I ask about your specific workflows, I want to understand which areas of UK corporate work are actually live for you. That way I only set up what you need and skip the rest.

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and which modules are active. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for materiality thresholds, disclosure schedule format, and board-minutes format. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/corporate-legal-uk:cold-start-interview --full` anytime to do the whole interview, or `/corporate-legal-uk:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

---

### Part 0: Who's using this, and what's connected

Three quick questions before we get into UK corporate specifics. These shape how the plugin works, not what it can do.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every memo, resolution, minutes draft, and diligence memo — solicitor/barrister outputs get the legal professional privilege header, non-lawyer outputs get the "research notes, review with a qualified solicitor or barrister" header.)
>
> 1. **Solicitor, barrister, or legal professional** — qualified lawyer, paralegal, legal ops working under solicitor/barrister oversight.
> 2. **Non-lawyer with solicitor/barrister access** — founder, business lead, contracts manager, FD, procurement; you have an in-house or outside solicitor/barrister you can consult.
> 3. **Non-lawyer without regular legal access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for solicitor/barrister review, not as verdicts.** Instead of "GREEN — sign it," you'll get "here's what I found and here are the questions to ask before you sign." That's more useful than a green light you can't be sure of.
> 2. **I'll pause before steps that have legal consequences** — signing a resolution, submitting a Companies House filing, executing an SPA, responding to the FCA or Panel. I'll ask whether you've reviewed with a solicitor/barrister, and I'll put together a short brief so the conversation with them is fast.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organisation, structure — and licensed legal judgment about your specific situation, which a tool can't give you.

If the answer is 3, add:

> If you need to find a solicitor or barrister in England & Wales: contact the Solicitors Regulation Authority (SRA) at sra.org.uk or the Bar Standards Board — most offer a find-a-solicitor / find-a-barrister service. In Scotland: the Law Society of Scotland (lawscot.org.uk). In Northern Ireland: the Law Society of Northern Ireland (lawsoc-ni.org). Many offer free or low-cost initial consultations for small businesses. For individuals, Citizens Advice and legal aid organisations cover many areas.

#### What's connected?

> This plugin can work with: VDR (Datasite, Box, iManage), board portal (Diligent, BoardEffect), document storage, and Slack. Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified — open your MCP settings to confirm" with a one-line how-to.
- Never report ✓ based on configuration alone.

Also check the UK research MCPs specifically:
- **uk-legal MCP** — test with a simple legislation search. Report ✓ only on a successful result.
- **uk-due-diligence MCP** — test with a simple Companies House search. Report ✓ only on a successful result.
- **govuk MCP** — test with a simple GOV.UK search. Report ✓ only on a successful result.

These research MCPs are what makes the citation guardrails meaningful — if none are connected, flag it prominently: "Without a UK research MCP connected, every statutory and case law citation will be tagged `[model knowledge — verify]`. Connect uk-legal MCP and uk-due-diligence MCP first for best results."

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]
>
> You don't need all of these. Core features work with file access alone.

#### Practice setting

Ask once, early:

> Practice setting? (This feeds every skill's escalation framing — in-house gets "loop in GC," solo/small firm gets "call outside counsel," clinic gets "route to supervising solicitor.")
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, billing thresholds, and who signs off above you.
> - **In-house** — I'll ask about your escalation matrix, who the GC/CLO is, and when something goes to the business.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

Branching notes:

- **Solo or small firm without a hierarchy:** skip or reframe internal escalation-chain questions. Instead of "who approves above your authority," ask "when do you bring in outside counsel for a second opinion."
- **In-house, midsize, or large firm:** ask the escalation chain as currently designed.
- **Legal aid / clinic:** route toward a supervision-model framing.

Record this on a `**Practice setting:**` line in `## Company profile`.

#### Write to the config

Write `## Who's using this`, `## Available integrations`, and `## Outputs` sections immediately after the first section of the config, per the template. These drive work-product header choice and feature-fallback behaviour across every skill in this plugin.

---

### Part 0.5: Module selection (1–2 min)

Ask which of the following apply. More than one is common. All four is not unusual for a GC.

> Which of these are part of your regular work? (This determines which sections get built in your practice profile and which skills light up — picking only M&A skips the board, public company, and entity management interviews entirely.)
>
> 1. **M&A** — deals: buying, selling, investing, or divesting business units (under English / Scots law)
> 2. **Board & Secretary** — board meeting prep, minutes, resolutions under CA2006, committee management
> 3. **Public Company** — FCA reporting, disclosure committee, PDMR/PCA notifications, UK MAR inside information management; or AIM Rules compliance
> 4. **Entity Management** — subsidiary management, Companies House filings, PSC register, Confirmation Statements, cap table
>
> Tell me the numbers that apply. You can always add a module later with `/corporate-legal-uk:cold-start-interview --module [name]`.

Record active modules. Proceed to the section for each active module only. Skip the rest entirely.

---

### Part 1: Company profile (2 min, always)

These questions apply regardless of which modules are active.

> Before I ask the structured questions: do you have a delegation-of-authority policy, a board-approved authority matrix, or a prior corporate-governance memo I can read? Paste the contents, share a file path, or say 'no' and I'll ask the questions one at a time. If you share one, I'll extract the approval levels and escalation points rather than making you re-type them.

If not:

> **What does [your company] do?** This is the single most important context — a SaaS vendor's playbook, a manufacturing distributor's playbook, and a professional services firm's playbook are completely different. You don't have to type it out: paste a link to your company website, your "about" page, your latest Annual Report, or your Companies House filing, and I'll extract what I need. Or give me the one-sentence version: what you sell, to whom, and how.

- What's the company name (or the name you want to use in outputs)?
- What industry are you in?
- Private (Ltd), public (plc), AIM-listed, or a subsidiary of a listed company?
- Primary jurisdiction of incorporation? (England & Wales / Scotland / Northern Ireland — flag if entity is registered in Scotland or NI, as some CA2006 provisions and procedures differ)
- How big is the legal team — just you, or a team?
- "When a review finds something that needs someone more senior to sign off — a novel issue in diligence, a materiality threshold decision, a consent matter with director conflicts, a schedule item that needs judgment, or a decision that's above your authority — who does that go to? Give me a name or a role (the GC, your partner, the deal lead), or say 'I decide myself.' This is how the plugin knows when to say 'you can handle this' versus 'loop in [X].' (This feeds /diligence-issue-extraction, /material-contract-schedule, /written-consent, and every other skill's escalation routing.)"

Write to `## Company profile` in the config.

---

### Part 2M: M&A module (4–6 min, if active)

#### 2M-a: Deal posture

- Buy-side, sell-side, or both? Note: most companies have experienced both over time, so this sets the default for house setup — the per-deal flag (`--new-deal`) captures the actual side for any live deal.
- Serial acquirer with a standard playbook, or does each deal get designed from scratch?
- Who runs deals on your end — corp dev, legal, outside solicitors as lead, or a mix?
- Do you typically use locked-box or completion accounts mechanics?

#### 2M-b: Diligence structure

> Before the questions: do you have a standard diligence request list or a prior issues memo I can read? Paste the contents, share a file path, or say 'no' and I'll ask the questions one at a time. If you share them, I'll extract the category structure, materiality thresholds, and house format and skip the corresponding questions.

If not:

- Do you have a standard diligence request list? How is it organised — by function (legal/finance/HR) or by document type?
- What's your materiality threshold for contract review? (All contracts? Above £X? Top N by revenue?) (This feeds /diligence-issue-extraction and /material-contract-schedule — the threshold decides which contracts get full review and which get triaged.)
- What's your usual VDR — Datasite, iManage, Box, SharePoint, something else?
- Do you use AI-assisted review tools — Luminance, Kira, anything else? For what specifically?

#### 2M-c: Issues memo format

> Two things I need:
>
> 1. Your standard diligence request list — the one you use on the buy side, or expect to see on the sell side.
> 2. One prior deal's issues memo — a closed deal, nothing live. I want to see how you structure findings: what you call things, how you categorise issues, what severity scheme you use, what depth you write at.
>
> These two documents become the backbone. Your categories, your format, your standards — not a generic template.

From the request list, extract: category structure, materiality thresholds if stated, standard carve-outs.
From the issues memo, extract: section structure, severity scheme, finding format, depth, who it's addressed to.

#### 2M-d: Sell-side specifics (if sell-side is active)

If the solicitor works sell-side at all, ask these additional questions:

- When you're preparing a data room, who decides what goes in?
- Do you prepare a Disclosure Letter or issues log anticipating what the buyer will flag?
- Who do you co-ordinate with on the business side for data room population — corp dev, CFO, functional heads?

Sell-side is about anticipating the buyer's findings and managing information flow outward, not reviewing inbound documents.

#### 2M-e: Closing checklist and deal team briefing

- Where does the closing checklist live — Excel, Smartsheet, a deal management tool?
- Who owns updates to it?
- How do you brief the deal team — daily, weekly, milestone-based? Email, Slack, call?
- What does the business side actually read versus what's for the file?

Write to `## M&A` in the config.

---

### Part 2B: Board & Secretary module (3–4 min, if active)

- What's your formal role — company secretary, joint secretary, or do you act in an advisory capacity without the formal title?
- How big is the board, and what's the composition — mostly independent NEDs, executive-heavy, any shadow directors to be aware of?
- Which committees exist? (Audit, Remuneration, Nomination, Strategy, anything else?)
- What tool do you use for board materials — Boardvantage, Diligent, BoardEffect, just email, nothing formal?
- How many regular board meetings per year, and roughly what months?

**Minutes:**
- Long-form narrative minutes, action minutes, or something in between?
- How quickly do you turn minutes around after a meeting?
- How do they get approved — circulated for written comments, or ratified at the next meeting?

**Written resolutions (CA2006):**
- Private company: do you routinely use written resolutions in lieu of meetings? For what types of board or shareholder action — routine officer appointments, dividend declarations, share allotments, annual actions, or more broadly?
- Public company (plc): shareholder written resolutions are not permitted under CA2006 s.281(2) — confirm if the company is a plc. Board written resolutions may be permitted by the company's articles.
- Any limits on what can be approved by resolution without a meeting (articles restrictions, shareholders' agreement provisions, or just practice)?

**Seed minutes (required for board-minutes skill):**

> Upload 5–6 prior board or committee minutes. Closed meetings only, nothing currently active. These teach the skill your house format — how minutes are structured, what level of discussion detail you capture, how resolutions are worded, how attendance is recorded. One full-board set and one committee set if you have both formats.
>
> If you don't have shareable minutes right now, you can add them later with `/corporate-legal-uk:cold-start-interview --module board`. The board-minutes skill will prompt you for them if they're missing.

From the seed minutes, extract:
- Overall structure and section order
- Header format (company name, meeting type, date, location)
- Attendance recording format (directors present/absent, management, guests)
- Discussion depth — long-form narrative, action minutes, or hybrid
- Resolution language (exact phrasing: "IT IS RESOLVED THAT" / "RESOLVED THAT" / other)
- Exhibit referencing convention
- Signature block format

Write extracted format as a `**Minutes template:**` block in `## Board & Secretary` in the config.

**Resolutions repository (required for written-consent skill):**

> Do you have a folder or repository where executed written resolutions are stored? (This feeds /written-consent — the skill searches the repository for the closest prior resolution and uses it as the substantive starting point, not just for format but for specific resolution language already approved for that type of action.)
>
> If you have one: tell me where it lives (folder path, Google Drive folder, SharePoint library, Box folder). The skill will search it at runtime.
>
> If you don't have a centralised repository: upload 3–5 prior resolutions now for format learning. The skill will still work — it just won't have precedent search capability until a repository is set up.

From the repository or seed resolutions, extract:
- House resolution language (exact phrasing: "IT IS RESOLVED THAT" / "RESOLVED THAT" / other)
- Recital structure (depth and style)
- Authorisation language (officer delegation language)
- Counterparts and electronic signature language (if present — Electronic Communications Act 2000)
- Signature block format

Write to `## Board & Secretary` → `**Resolutions repository:**` and `**Resolution format:**` in the config.

**Annual governance cycle:**
- What annual items do you manage? (Director re-election, auditor reappointment, approval of accounts and reports, Confirmation Statement (CS01), AGM business if plc, equity plan approvals, annual board self-assessment — whatever applies.)

Write to `## Board & Secretary` in the config.

---

### Part 2P: Public Company module (3–4 min, if active)

- What exchange are you on — Main Market (Premium / Standard), AIM, AQSE, other?
- What's your fiscal year end?
- What's your filing status — premium listed, standard listed, or AIM?

**Disclosure committee:**
- Do you have a formal disclosure committee? Who's on it — CFO, General Counsel, Head of IR, Company Secretary, others?
- How often does it meet — quarterly pre-results, or as needed?

**Inside information / UK MAR Art. 17:**
- Who is responsible for identifying and assessing inside information?
- How do you document the delay-to-disclosure assessment when delay is used (MAR Art. 17(4))? Note: FCA must be notified at the end of any delay period.
- Do you maintain a Disclosure Assessment Record (DAR)?

**PDMR / PCA notifications (UK MAR Art. 19):**
- Who tracks PDMR and PCA transactions — legal, company secretary, IR, outside counsel, or a combination?
- What's your target for submitting the MAR Art. 19 notification? (Regulatory requirement: within 3 business days of transaction.)
- Does your dealing policy require pre-clearance? Who approves?
- What are your closed periods relative to results announcements?

**Results announcement prep:**
- What's legal's role in results call / RNS announcement prep — reviewing draft announcements, preparing Q&A, something else, or no direct role?
- How far in advance of the announcement are you typically involved?

Write to `## Public Company` in the config.

---

### Part 2E: Entity Management module (2–3 min, if active)

> If you have an org chart or entity list — even a rough one, even a spreadsheet — upload it now. I'll read it and extract the entity structure, jurisdictions, ownership percentages, and entity types. That's faster and more accurate than answering these questions from memory. (This feeds /entity-compliance — the skill initialises the compliance calendar from this list and surfaces Confirmation Statement and accounts filing deadlines.)
>
> If you don't have one handy, answer the questions below and I'll build a starter entity table from your answers.

**From uploaded org chart or entity list, extract:**
- Entity names and entity types (Ltd, plc, LLP, LP, unlimited, branch, etc.)
- Nation of incorporation for each (England & Wales / Scotland / Northern Ireland / non-UK)
- Companies House registration number where available
- Ownership chain and percentages
- Any entities flagged as dormant or inactive

**If no upload, ask:**

- How many active legal entities are you managing, roughly?
- What are the key nations — just England & Wales, or a meaningful multi-nation footprint (Scotland, NI, international)?
- Are any entities incorporated in Scotland? If yes, note that charges over Scottish property must also be registered at the Scottish Registers, and some Scots law provisions differ from E&W.
- Who handles Companies House filings — legal, legal ops, the company secretary, or does an outsourced company secretarial service handle it automatically?
- What's your cap table situation — Carta, Shareworks, manual, or not applicable if wholly owned with no external equity?
- Do you maintain the PSC register internally, or is it managed by a company secretarial service? When was it last reviewed?
- Do your subsidiaries have their own governance cadence, or are they effectively dormant holding companies?
- Do you have intercompany agreements in place — services agreements, IP licences, loans?

Write to `## Entity Management` in the config.

---

### After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list (not a generic template — these are the concrete things this plugin does best):

> **Here's what I'm good at in UK corporate and M&A practice:**
>
> - **Extract diligence issues from the data room** — e.g., "Point at a VDR folder and get findings categorised per your house materiality thresholds, flagged for CA2006 / FSMA / CMA issues." Try: `/corporate-legal-uk:diligence-issue-extraction`
> - **Build the material contracts schedule** — e.g., "From diligence findings, build the disclosure schedule in the SPA's format, including consent requirements under English law." Try: `/corporate-legal-uk:material-contract-schedule`
> - **Draft a board or committee written resolution** — e.g., "Precedent search from your resolutions repository, then drafted in house format under CA2006." Try: `/corporate-legal-uk:written-consent`
> - **Entity compliance tracker** — e.g., "See what Companies House filings are due in the next 30 / 60 / 90 days across your subsidiaries — Confirmation Statements, accounts, PSC updates." Try: `/corporate-legal-uk:entity-compliance`
> - **Closing checklist status** — e.g., "What's left to close — conditions precedent (CMA clearance, FCA change of control), documents, consents, filings — with critical path." Try: `/corporate-legal-uk:closing-checklist`
> - **Post-closing integration** — e.g., "Phased workplan, consent tracking, contract assignment at scale for a just-closed deal." Try: `/corporate-legal-uk:integration-management`
>
> **My suggestion for your first one:** If you have an active deal, run `/corporate-legal-uk:closing-checklist` — it shows immediately where the plugin fits in your workflow. Or tell me what's on your plate and I'll pick.

**Research connector prompt.** Before showing the active modules, say:

> "Before your first diligence extraction or resolution draft: connect the uk-legal MCP and uk-due-diligence MCP. Without them, I'll flag every citation as `[model knowledge — verify]` — with them, I can verify statutory provisions against legislation.gov.uk and company data against Companies House in real time. In Cowork: Settings → Connectors. In Claude Code: authorise when a skill prompts you."

Then show the active modules and the populated sections:

> Here's what I've captured: [list active modules]. Practice Profile is written. A few things to check:
> - [Flag any thin or ambiguous answers worth revisiting]
> - [If M&A active and no seed docs provided: "Ping me with your request list and a prior issues memo when you have them — I'll update the diligence structure and memo format sections."]
> - [If M&A active: "When a deal comes in, run `/corporate-legal-uk:cold-start-interview --new-deal` to set up deal-specific context on top of the house approach. M&A skills available now: diligence extraction, deal team summaries, material contracts schedule, closing checklist, and post-closing integration."]
> - [If Board & Secretary active: "Board skills available now: `/corporate-legal-uk:written-consent` for written resolutions under CA2006, and the board-minutes skill for drafting minutes in your house format."]
> - [If Entity Management active: "Entity skill available now: `/corporate-legal-uk:entity-compliance` initialises a compliance tracker from your entity list and surfaces what's due at Companies House."]
> - [If Public Company active: "Public Company skills covering FCA disclosure, MAR notifications, and PDMR/PCA tracking are coming in a future release — the practice profile section is ready to populate when they ship."]

Close with a note on changeability:

> "Your practice profile is at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` — it's a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change (a new threshold, a jurisdiction added, a committee renamed)
> - Run `/corporate-legal-uk:cold-start-interview --redo` for a full re-interview
> - Run `/corporate-legal-uk:cold-start-interview --module [m&a | board | public | entities]` to add or refresh one module
> - Run `/corporate-legal-uk:cold-start-interview --check-integrations` to re-check what's connected
>
> The sections most often adjusted after first setup are the M&A materiality thresholds, the disclosure schedule format / issues memo template, and the entity tracker cadence."

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/corporate-legal-uk:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

---

## Per-deal setup (`--new-deal`, M&A module only)

When a live deal starts, run a lighter interview focused only on deal-specific context. House approach stays from the plugin config.

Ask:
- Deal code name
- Side for this deal (buy-side or sell-side — may differ from the house default)
- Target or acquirer name
- Target entity type (Ltd / plc / LLP) and nation of incorporation (E&W / Scotland / NI) — Scotland flag if relevant
- VDR location (folder path or URL)
- Deal lead name
- Signing date and closing date (if known)
- Any deal-specific threshold differences
- Outside solicitors firm and lead partner for this deal
- Is this a public company deal requiring Panel involvement? If so, note PUSU clock and offer timetable constraints.
- CMA filing required? (Enterprise Act 2002 merger control thresholds — check with outside counsel)
- FCA change of control approval required? (FSMA 2000 Part XII — relevant for regulated entities)

Write to `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/deals/[code-name]/deal-context.md`. Skills read both the plugin config (house) and `deal-context.md` (this deal), with deal-context.md taking precedence on conflicts.

---

## Practice Profile quality check

Before finishing, re-read what was written. Flag:
- Any section still showing a placeholder because the answer was skipped or vague — ask again
- Any active module where no seed document was provided — note it and ask the user to provide one when available
- The `*Active modules:*` line at the top of the plugin config — update it to list exactly which modules are on
- Whether the entity jurisdiction includes Scotland or NI — flag if the Scottish law divergences reminder was not surfaced

---

## Failure modes

- **Don't assume all modules are active.** Ask first, interview only for what's live.
- **Don't hard-code buy-side.** The practice profile captures the house tendency; the per-deal flag handles the actual side.
- **Don't write generic placeholders.** If the answer was vague ("standard materiality thresholds"), ask what that means in pounds sterling. The practice profile is only useful if thresholds are actual thresholds.
- **Sell-side posture is not buy-side reversed.** On sell-side you're preparing the Disclosure Letter and managing outward information flow, not reviewing inbound documents.
- **Don't conflate Ltd and plc rules.** Private company rules (written resolutions, 9-month accounts window) differ significantly from plc rules (no shareholder written resolutions, 6-month accounts window, FCA obligations). Confirm entity type before setting defaults.
- **Don't apply E&W procedure to Scottish entities without noting the divergence.**
