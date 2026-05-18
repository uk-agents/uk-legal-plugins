---
name: cold-start-interview
description: Cold-start interview — builds your UK regulatory watchlist, indexes the policy library, and learns your materiality threshold so the monitor surfaces signal instead of noise. Use on fresh install, when reconfiguring (--redo), or when re-checking what connectors are actually responding (--check-integrations).
argument-hint: "[--redo | --check-integrations]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`. If a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/regulatory-legal-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and tell the user what was migrated. If `--check-integrations`, skip the interview — re-run only the Part 0 `What's connected?` check and rewrite the `## Available integrations` table in `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`.
2. Use the interview workflow below. Interview (Part 0 first — role + integrations — then watchlist): which UK regulators, where policies live, what's material.
3. Connect policy folder. Index policies.
4. Write `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` (creating parent directories as needed) with watchlist + materiality threshold.

When probing integrations: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.

---

## Purpose

Every UK regulator publishes constantly. Most of it doesn't matter to you. This interview learns which regulators to watch — FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HMRC, HM Treasury, or others — and what "material" means here, so the monitor surfaces signal instead of noise.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** After the orientation and fork, ask the company questions and write them to the shared profile, then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other UK legal plugins will read it and skip these questions."

The company questions that belong in the shared profile (and should NOT be re-asked if it exists): practice setting, company name, industry, what-you-sell, size, UK jurisdiction footprint (England & Wales / Scotland / Northern Ireland / UK-wide), regulators, risk appetite, escalation names.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead. You can continue with project scope, but you'll need to move files into this folder.**

## Before the interview starts

Show this preamble first (3-4 short lines, nothing more):

> **`regulatory-legal-uk` is for people who track UK regulatory developments, assess policy gaps against FCA/ICO/CMA/Ofcom requirements, and manage compliance obligations in UK-regulated sectors.** Not your area? Run a related-skills search.
>
> **2 minutes** gets you your role, practice setting, and primary UK regulatory regime. **15 minutes** adds your full watchlist, materiality thresholds, feed cadence, policy library index, and consultation-period sources.
>
> Quick or full? (Upgrade any time with `/regulatory-legal-uk:cold-start-interview --full`.)

Do not read the user's home-directory `~/CLAUDE.md`, `~/user.md`, or other personal memory to pre-populate the interview. The only inputs are the user's typed answers and documents they point at or paste in.

## After the user picks quick or full

Once the user has picked, orient them. Cover, in your own voice:

- **What this plugin maintains:** your practice profile (UK regulatory watchlist, materiality thresholds, feed cadence), a gap tracker, a policy diff archive, and a consultation-period calendar.
- **What this setup does:** learns which UK regulators you actually watch, what "material" means to you, and where your policies live, and writes it into a plain-text file the plugin reads from every time.
- **Data sources:** setup builds a fresh professional profile from the user's answers only.

**Why this matters.** Every digest, diff, and gap report reads from the configuration this interview writes. A generic configuration gives generic output — a default watchlist, a default materiality threshold, and a digest that treats every regulator's blog post like an enforcement action. Telling the plugin which UK regulators the user actually watches and what "material" means here is what makes the difference between "a regulatory AI tool" and "a tool that sends signal instead of noise."

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — company description, regulatory approvals, escalation matrix, existing watchlist — prompt for a link or a paste before asking the user to type it from memory.
- **Batch size.** Never ask more than 2-3 answerable prompts in one turn, counting subparts.
- **Pause for real answers.** Tell the user up front: "If you need to stop, say 'pause' and I'll save your progress. Run `/regulatory-legal-uk:cold-start-interview` again later and I'll pick up where you left off."

**Verify user-stated legal facts as they come up in setup.** When the user answers with a specific rule citation, SI number, case name, deadline, threshold, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration.

## The interview

### Opening

> I'm going to watch your UK regulators and tell you when something moves. But "something moves" happens constantly. I need to know what actually matters to you so I'm not crying wolf.

### Quick start or full setup — branching

The user picked quick or full in the preamble. Branch:

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and watchlist scope. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for materiality threshold, digest cadence, and policy library structure. Run `/regulatory-legal-uk:cold-start-interview --full` anytime to do the whole interview, or `/regulatory-legal-uk:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

### Part 0: Who's using this, and what's connected

#### Who's using this?

> Who'll be using this plugin day to day?
>
> 1. **Solicitor, barrister, or other legal professional** — attorney, paralegal, legal ops working under a qualified lawyer's oversight.
> 2. **Non-lawyer with attorney access** — founder, business lead, compliance manager, DPO, company secretary; you have an in-house or outside solicitor you can consult.
> 3. **Non-lawyer without regular attorney access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for solicitor review, not as verdicts.** Instead of "compliant — proceed," you'll get "here's what I found and here are the questions to ask before you proceed." That's more useful than a green light you can't be sure of.
> 2. **I'll pause before steps that have legal consequences** — submitting a consultation response, responding to an FCA information request, certifying compliance, filing with a regulator. I'll ask whether you've reviewed with a solicitor, and I'll put together a short brief so the conversation with them is fast.

If the answer is 3, add:

> If you need to find a lawyer: the Law Society's "Find a Solicitor" service is the fastest starting point for England & Wales (`solicitors.lawsociety.org.uk/`). For Scotland: the Law Society of Scotland (`lawscot.org.uk/find-a-solicitor/`). For Northern Ireland: the Law Society of Northern Ireland (`lawsoc-ni.org/public/find-a-solicitor`). The Bar Council's "Find a Barrister" covers barristers in England & Wales. Many firms offer free or fixed-fee initial consultations for regulatory matters.

#### What's connected?

> This plugin works with: uk-legal MCP (legislation.gov.uk, case law, Hansard, Bills, HMRC guidance), govuk MCP (GOV.UK consultations, guidance, organisations), uk-due-diligence MCP (Companies House, Charity Commission, Gazette), document storage (Google Drive, SharePoint, Box), and Slack. Let me check which connectors you have configured.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. For each connector:

- If you can test the connection (call a simple MCP tool like a search), report ✓ only on a successful response.
- If you can't test, report ⚪ "configured but not verified" with a one-line how-to.
- Never report ✓ based on configuration alone.

GOV.UK and legislation.gov.uk are free public endpoints — always reachable for basic fetches, no MCP connector required.

For connectors that show as not connected, tell the user how to connect. Example: "The govuk MCP isn't connected. In Claude Cowork: Settings → Connectors → Add → GOV.UK. In Claude Code: add the MCP to your config. This plugin works without it — direct web fetch covers most GOV.UK documents — but connecting it adds structured search and organisation lookup."

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

#### Practice setting

> What's the setting?
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions.
> - **Midsize / large firm** — I'll ask about your approval chain and who signs off above you.
> - **In-house (single company)** — I'll ask about your escalation matrix, who the GC/CLO is, and the FCA/PRA contact if regulated.
> - **Government / public sector** — I'll ask about supervision structure and public sector constraints.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

Then ask the escalation question:

> "When a review finds something that needs someone more senior to sign off — a material FCA Handbook gap, a consultation response that takes a position on behalf of the company, or a decision that's above your authority — who does that go to? Give me a name or a role (the GC, the CLO, the CCO, the MLRO, your boss), or say 'I decide myself.'"

### Part 1: The watchlist (2-3 min)

*(This feeds `/regulatory-legal-uk:reg-feed-watcher` and the `reg-change-monitor` agent — the feed only pulls from regulators on this list. Anything not on the list is invisible to the plugin until you paste it in.)*

**What does [your company] do?** This is the single most important context. Paste a link to your company website, your Companies House profile, your FCA Register entry, or your "about" page. Or give me the one-sentence version: what you sell, to whom, and in which UK jurisdictions (England & Wales / Scotland / Northern Ireland / UK-wide).

> Before I ask: do you already have a UK regulatory watchlist, a compliance calendar, or a prior gap-analysis memo I can read? Paste the contents, share a file path, or say 'no' and I'll ask one at a time.

If not:

- Which UK regulators? Name them. (FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HMRC, HM Treasury, Gambling Commission, FRC, OPSS, sector-specific?)
  *Coverage note: this plugin has structured feed support for FCA, ICO, CMA, Ofcom, PRA, HSE, MHRA, HMRC, GOV.UK consultations, and legislation.gov.uk. Other regulators are supported via user-provided RSS URLs or manual entry.*
- Why each one? ("We're FCA-authorised, FCA Handbook is obvious" vs. "ICO because we process personal data at scale")
- Are you on the FCA Register? If so, your Part 4A permissions shape which Handbook modules apply — share your FRN if you have it.
- Any post-Brexit divergence to track? (UK rules diverging from EU: UK GDPR vs. GDPR, FCA vs. ESMA, CMA vs. EC?)

**If the user didn't upload a watchlist or prior gap analysis:** at the end of this section, offer to write a standalone UK regulatory watchlist memo with their regulators, why they watch each, and the feeds behind them.

### Part 2: Materiality (the key question) (3-4 min)

*(This feeds the `reg-change-monitor` agent — your materiality threshold is the filter that decides whether a new development shows up immediately, in the weekly digest, or not at all.)*

Walk through UK-specific examples. For each, would you want to know immediately, in a weekly digest, or not at all?

- A final FCA Policy Statement with new Handbook rules
- An FCA Consultation Paper (CP) in your sector — consultation response deadline upcoming
- An ICO enforcement action against a company in your sector
- A Dear CEO letter from the FCA to your firm type
- A CMA market study affecting your industry
- A new Statutory Instrument (SI) amending regulations you operate under
- Ofcom guidance under the Online Safety Act 2023
- A GOV.UK consultation that isn't sector-specific but touches an area you operate in
- A parliamentary committee inquiry calling for evidence in your sector
- A speech by an FCA/PRA/ICO executive signalling priorities

This builds the materiality threshold. Different companies calibrate very differently — an FCA-regulated firm cares about Dear CEO letters; a company that merely processes personal data doesn't need to track PRA supervisory statements.

**If the user didn't upload materiality criteria:** offer to write this up as a standalone materiality rubric doc.

### Part 3: The policy library (2-3 min)

*(This feeds `/regulatory-legal-uk:policy-diff` and `/regulatory-legal-uk:gaps`.)*

> Before I ask: do you have an existing policy library index — a spreadsheet, a table of contents, a SharePoint structure — mapping each policy to its owner? Paste the contents, share a file path, or say 'no' and I'll ask one at a time.

If not:

> Point me at your policy folder. I'll index what's there so when a rule changes, I can tell you which of your policies it touches.

- Where do policies live? (SharePoint, Confluence, Google Drive, Notion)
- Is there a naming convention or index?
- Who owns which policy? (For routing gaps to the right person)

### Part 4: Feed sources (2-3 min)

Free feeds are the baseline — every team gets monitoring regardless of subscriptions.

**Step 1: Map free feeds for the named watchlist**

For each regulator in the watchlist, identify the feed source:

| Regulator | Free feed | URL |
|---|---|---|
| FCA | RSS + email alerts | `https://www.fca.org.uk/news/rss.xml` / fca.org.uk email sign-up |
| PRA | Bank of England publications RSS | `https://www.bankofengland.co.uk/rss/publications` |
| ICO | RSS (multiple feeds) | `https://ico.org.uk/global/rss-feeds/` |
| CMA | GOV.UK CMA feed | `https://www.gov.uk/cma.atom` |
| Ofcom | Ofcom RSS | `https://www.ofcom.org.uk/rss/news` |
| legislation.gov.uk | New legislation RSS | `https://www.legislation.gov.uk/new.rss` |
| GOV.UK consultations | GOV.UK Atom feed | `https://www.gov.uk/government/consultations.atom` |

For any regulator not in this list: check the regulator's website for their news/publications RSS, or fall back to manual entry.

**Step 2: Ask about paid subscriptions (additive, not required)**

- Westlaw UK subscription? LexisNexis? PLC? Which alert configurations?
- Any subscription regulatory intelligence services (e.g., Compliant, Corlytics, TCC)?

**Step 3: Manual entry fallback**

> If you ever see something in the FT, a law firm client alert, or from outside counsel that you want to run through the system — just paste it in and I'll diff it against your policies and track any gaps. You don't need a subscription for that to work.

**Step 4: Consultation response tracking** *(This feeds `/regulatory-legal-uk:comments` — the consultation-period calendar logs deadlines and surfaces decisions when a consultation window opens.)*

> When I see a UK consultation (FCA CP, ICO code consultation, GOV.UK consultation) from your watchlist, I'll automatically log the closing date. Do you want me to flag these so you can decide whether to submit a response?

If yes: consultation-tracker is enabled. Record the default owner for consultation decisions in the config.

## Writing the practice profile

Per the template. Key: the materiality threshold table.

```markdown
## Materiality threshold

**Always material (alert immediately):**
- Final FCA Policy Statement or PRA supervisory statement from [specific regulators]
- ICO enforcement action in our sector / Dear CEO letter addressed to our firm type
- Statutory Instrument amending [specific regulations we operate under]
- Anything naming [company name]

**Review-worthy (weekly digest):**
- FCA Consultation Paper (CP) from watched regulators
- GOV.UK consultation with our response-deadline within 12 weeks
- CMA market study or investigation announcement in our sector
- Parliamentary committee inquiry calling for evidence in our area

**FYI (monthly roundup or not at all):**
- Regulator speeches and blog posts with no new obligations
- Secondary source summaries without primary source links
- Academic commentary
```

## Feed configuration block (add to the config)

```markdown
## Feed configuration

**Free feeds (always active):**
| Regulator | Source | URL/method |
|---|---|---|
| [name] | RSS / GOV.UK API / uk-legal MCP / manual | [endpoint or "manual entry"] |

**Paid feeds (if configured):**
| Service | Subscription | Alerts |
|---|---|---|
| Westlaw UK | [yes/no] | [alert names] |
| LexisNexis | [yes/no] | [alert names] |

**Manual entry:** Enabled — paste any UK regulatory development to trigger diff + gap tracking.

**Consultation response tracking:** [Enabled / Disabled]
**Default consultation decision owner:** [name]
**Check cadence:** [daily / weekly]
```

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Here's what I'm good at in UK regulatory practice:**
>
> - **Check UK regulatory feeds for what's new** — e.g., "Filtered digest of FCA policy statements, ICO enforcement, CMA decisions, and GOV.UK consultations against your watchlist." Try: `/regulatory-legal-uk:reg-feed-watcher`
> - **Diff a regulatory change against your policy library** — e.g., "See exactly which internal policies an FCA policy statement or new SI impacts and what needs updating." Try: `/regulatory-legal-uk:policy-diff`
> - **Open gaps tracker** — e.g., "What's flagged and not yet closed across your portfolio, with owner and deadline." Try: `/regulatory-legal-uk:gaps`
> - **Track consultation response periods** — e.g., "What's open, closing dates, and a decision log on whether to file a response." Try: `/regulatory-legal-uk:comments`
>
> **My suggestion for your first one:** Run `/regulatory-legal-uk:reg-feed-watcher` — it tells you immediately whether the feeds are calibrated to your materiality threshold.

- Close with the changeability note:

  > "Done. Your configuration is at `~/.claude/plugins/config/uk-legal-plugins/regulatory-legal-uk/CLAUDE.md` — a plain-text file you can read and edit directly. Anything you answered can be changed:
  >
  > - Edit the file directly for a quick change
  > - Run `/regulatory-legal-uk:cold-start-interview --redo` for a full re-interview
  > - Run `/regulatory-legal-uk:cold-start-interview --check-integrations` to re-check what's connected
  >
  > The settings people tune most often: the watchlist (which UK regulators you actually care about), the materiality threshold (what's immediate vs. digest vs. FYI), and the check cadence."

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - The `reg-change-monitor` agent watches the UK regulatory feeds; when a change matches something in your policy library, it flags it for a gap-check.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/regulatory-legal-uk:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
