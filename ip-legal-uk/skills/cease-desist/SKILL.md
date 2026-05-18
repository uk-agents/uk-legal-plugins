---
name: cease-desist
description: >
  Draft a cease-and-desist letter (send mode) or triage one you received
  (receive mode). Use when asserting your rights against an infringer with a
  demand letter calibrated to your enforcement posture, or when an incoming
  C&D needs triage into a structured options memo with a recommendation.
argument-hint: "<--send | --receive> [context, counterparty, or path to incoming letter]"
---

# /cease-desist

Two modes. Pick one:

- `/ip-legal-uk:cease-desist --send` — draft a cease-and-desist letter calibrated to your enforcement posture. Loud gate runs before delivery.
- `/ip-legal-uk:cease-desist --receive` — triage a C&D someone sent you. Produces an options memo with a recommendation.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "This plugin needs setup before it can give you useful output. Run `/ip-legal-uk:cold-start-interview` — the C&D skill depends on your enforcement posture, approval matrix, and practice-area mix, none of which are configured yet."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

3. **Dispatch on `$ARGUMENTS`:**
   - If `--send` is present: run send mode (below). Walk through identify-the-right, identify-the-conduct, identify-the-relationship, identify-the-demand, calibrate-to-posture, draft, and the pre-delivery gate.
   - If `--receive` is present: run receive mode (below). Ask for the incoming letter (path or pasted text), then assess, identify exposure, present options, and write the triage memo.
   - If neither flag is present: ask once — "Are we sending a cease-and-desist (you're asserting) or triaging one we received (you're defending)?" — and then dispatch.

4. **Respect the gate.** In send mode, the loud gate runs before any final draft is written to disk. Do not skip it.

5. **Respect the approval matrix.** Pull the approver for the C&D row from `## Enforcement posture → Approval matrix`. Pull automatic escalations. Surface both in the gate; do not smother them.

6. **Hand off where appropriate.** In receive mode, if the recommendation is to respond firmly, offer to chain into `/ip-legal-uk:cease-desist --send` pre-populated with the response context. If the recommendation is to pre-empt with a declaratory relief action or UK IPO cancellation, escalate to outside counsel per the practice profile's IP litigation row — do not draft.

## Examples

```
/ip-legal-uk:cease-desist --send
/ip-legal-uk:cease-desist --receive ~/Downloads/incoming-cd-acme.pdf
/ip-legal-uk:cease-desist
```

## Notes

- The outgoing C&D does not carry the work-product header. The internal draft, the pre-send brief, and the triage memo do.
- UK trade mark rights are territorial; an EUTM does not cover the UK post-Brexit, and a UK mark does not cover the EU. The draft assumes the jurisdictions declared in your practice profile's `Registered in:` footprint. If the conduct or counterparty is somewhere else, flag before drafting.
- Every `[CITE:___]` is unverified until checked against the uk-legal MCP or a primary source. Source attribution tags stay on the draft.
- Non-lawyer users get a one-page brief for the solicitor/attorney conversation before the gate clears.

---

## Purpose

A cease-and-desist letter asserts a legal right and demands that someone stop doing something. It is one of the most consequential letters an IP practice sends or receives. Sending one is a first step toward litigation — recipients can apply for declaratory relief in a forum of their choosing, and overbroad or bad-faith assertions can expose the sender to the UK unjustified threats regime. Receiving one starts a clock and forces a decision. This skill handles both sides with the guardrails the decision deserves.

Two modes:

- `--send` — you are asserting. Draft a C&D calibrated to the posture, gate before delivery.
- `--receive` — you are defending. Triage the incoming letter, produce an options memo, route to matter creation if warranted.

If the user does not pass a flag, ask once: "Are we sending a cease-and-desist (you're asserting) or triaging one we received (you're defending)?"

> **External deliverable (send mode):** the drafted C&D is sent to counterparty. Do NOT include the `PRIVILEGED & CONFIDENTIAL` header on the outgoing letter. Internal drafts, pre-send briefs, and triage memos keep the header per plugin config `## Outputs`.

## Jurisdiction assumption

UK trade mark rights are territorial — a UK registration does not cover the EU, and a EUTM does not cover the UK (post-Brexit, since 31 December 2020). Copyright is Berne-multilateral but enforcement is jurisdiction-specific. This skill assumes the jurisdiction declared in the matter or the practice profile's `Registered in:` footprint. If the infringing conduct, counterparty, or forum is somewhere else, flag it — the draft may not apply as written.

**UK unjustified threats regime.** Under TMA 1994 s.21 and PA 1977 s.70, a person aggrieved by an unjustified threat of infringement proceedings may apply to the court for relief, including a declaration that the threats were unjustified, an injunction, and damages. The regime is strict — threats made to the primary infringer (the person who applied the mark or who made / imported the patented product) are generally safe, but threats that reach secondary actors (retailers, distributors, customers) without a corresponding claim against the primary infringer can trigger liability. This is a material UK-specific risk. Flag before drafting if the proposed recipients include anyone other than the primary manufacturer or applicant.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` → `## Enforcement posture` (posture, C&D triggers, soft-letter criteria, approval matrix, automatic escalations), `## IP practice profile` (practice area mix, registered jurisdictions, outside counsel roster), `## Outputs` (work-product header, role), `## Who's using this` (role — solicitor/attorney vs. non-lawyer)
- Any C&D template or enforcement playbook referenced in the practice profile's seed documents — read it, match the structure
- **Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip matter machinery — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific overrides (e.g., posture override, approver override). Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

## Send mode — drafting the C&D

### Step 1: Identify the right

Ask, in one batch:

> Which IP right are we asserting?
>
> - **Trade mark** — is it registered? Where (UK IPO, EUIPO — note: separate systems since 31 Dec 2020, EUIPO does NOT cover UK)? Reg number and class(es)? Or unregistered (first-use date, goodwill in UK market, passing off potential)?
> - **Copyright** — is it registered? (There is no UK copyright registration — protection is automatic under CDPA 1988 on creation.) Title, date of creation, description of the work? If US copyright is also in play, registration status matters for US claims.
> - **Patent** — patent number, jurisdiction (UK national / EP designating UK), claim(s) principally in issue?
> - **Both / mixed** — identify each.

Record each right. Registered rights get cited by number. Unregistered trade marks get the goodwill and misrepresentation paragraph for passing off. Copyright is automatic — confirm the work was created and not assigned away.

### Step 2: Identify the conduct

> Describe the infringing conduct in specifics, not adjectives:
>
> - **Who** is doing it — entity name, individual, platform handle?
> - **What** — the accused mark, the accused copy, the accused product? Attach or describe samples.
> - **Where** — website URL, marketplace listing, physical retail, social media?
> - **Since when** — date first observed, date of the earliest use you can document?
> - **Evidence** — screenshots, receipts, watch-service hit, customer confusion reports?

Facts go in specific. "You sold product X on [URL] bearing the mark [Y] on [date]" beats "You have been infringing our rights." Adjectives tell on a thin record.

### Step 3: Identify the relationship

> What's the relationship between us and the recipient?
>
> - **Competitor** (direct or adjacent) — standard posture applies
> - **Reseller / channel partner** — tone adjusts; consider the soft-letter path; and check the UK unjustified threats risk (below)
> - **Former licensee / ex-employee / former partner** — contract provisions likely apply; cite them
> - **Stranger / random infringer** — standard
> - **Current customer / partner** — automatic escalation per practice profile; flag before drafting

This changes tone, approver, and whether to draft at all without escalation.

**UK unjustified threats flag.** If the proposed recipient is not the primary infringer (i.e., not the manufacturer, importer, or person who applied the mark), surface the unjustified threats risk now. Under TMA 1994 s.21 and PA 1977 s.70, threatening secondary actors (retailers, distributors, end-users) without a contemporaneous claim against the primary can create liability. If the recipient is a secondary actor, escalate to the named IP litigation solicitor/attorney before drafting.

### Step 4: Identify the demand

> What does the claimant actually want?
>
> - **Stop** — cease the infringing use
> - **Account** — report sales, profits, volumes (for damages baseline)
> - **Destroy** — destroy or recall infringing inventory
> - **Damages** — monetary settlement
> - **Transfer / assign** — transfer the domain, hand over the account, assign the accused mark
> - **Public correction** — takedown of offending content, public statement
> - **Confirm in writing** — compliance undertaking by a date

Pick the actual remedies. The demand must be proportionate to the harm — an overbroad demand is evidence of bad faith if the matter is ever litigated, and may itself constitute an unjustified threat.

**Channel-takedown parallel path (marketplace infringement).** If the accused conduct is on a marketplace (Amazon, eBay, Etsy, Alibaba, TikTok Shop, Shopify-hosted storefronts), flag the platform's IP-infringement reporting path as a faster, cheaper parallel track:

- **Amazon Brand Registry** (trade mark and copyright takedown, counterfeit removal)
- **eBay VeRO** (Verified Rights Owner programme)
- **Etsy IP Infringement reporting**
- **TikTok Shop IP Protection**
- **Shopify copyright / trade mark reporting**
- **UK IPO's fast-track process for online trade mark infringement** (gov.uk/trade-marks/stop-others)

A marketplace takedown often resolves in days; a C&D gives the infringer time to sell through inventory while negotiating. Recommend filing both when the conduct is marketplace-based, with the C&D covering off-platform conduct that the platform report cannot reach. Note in the pre-send brief whether the parallel-path has been filed, is queued, or is declined (and why).

### Step 5: Calibrate to posture

Read `## Enforcement posture` → `Default posture:` and apply:

- **Aggressive** — firm letter, short deadline (often 7–14 days), explicit consequence language (IPEC / High Court proceedings, injunctive relief, damages, costs), no settlement softening
- **Measured** — firm but professional, standard deadline (14–30 days), consequences noted without theatrics, openness to discussion if they respond
- **Conservative** — soft letter framing, longer deadline or no hard deadline, "we'd like to discuss" opening, consequence language muted or absent

Also read `When we send a C&D`, `When we send a soft letter first`, and `When we just file`. If the facts suggest this should be a soft letter or a direct filing per the practice profile, flag it before drafting.

Matter-level overrides in `matter.md` beat the practice default.

### Step 5.5: Counterparty diligence — REQUIRED PRECONDITION

**Before drafting, run counterparty diligence and present the results to the user.** Every C&D assertion carries declaratory relief / unjustified threats / costs exposure calibrated to *who* the recipient is. The skill does not draft a C&D until the user has seen the diligence and confirmed they still want to proceed.

Collect and present — in one block, for user sign-off — the following:

- **Legal entity** — exact corporate name (check Companies House via uk-due-diligence MCP), registered office, any trading names or aliases. UK IPO / EUIPO ownership records. Flag `[verify]` if the source is unconfirmed.
- **Size and resources** — approximate headcount, revenue band if publicly known, parent company if a subsidiary. Companies House filings, public sources. Flag honestly if size cannot be determined.
- **IP portfolio** — do they hold registered marks, patents, or copyrights in adjacent classes? A counterparty with its own IP portfolio is more likely to (a) understand the posture, (b) counter-assert, and (c) apply for declaratory relief. UK IPO / EUIPO quick search on the accused entity and affiliates.
- **Litigation history** — any known IPEC or High Court IP cases as claimant or defendant? Any UK IPO inter partes proceedings? Flag any prior C&D campaigns.
- **Counsel** — do they have known outside IP counsel? Firm and lead name if identifiable from prior filings or proceedings. "No counsel on file" is itself a data point.
- **Declaratory relief / unjustified threats risk** — given size, IP portfolio, litigation history, counsel, and forum: is this a counterparty likely to welcome a C&D as an invitation to apply for declaratory relief or bring an unjustified threats claim? Flag high / medium / low with a one-sentence reason.
- **Relationship risk** — are we a customer of theirs, do we share investors, are they a potential acquirer or partner? Confirm not a current customer or strategic partner.

Present this as a short memo in-chat BEFORE the draft:

```
## Counterparty diligence — [Entity Name]

- **Entity:** [name, Companies House number if UK, parent if any]
- **Size:** [headcount band, revenue band] — [source, `[verify]` where applicable]
- **IP portfolio:** [registered marks / patents / copyrights in adjacent classes — or "none found"]
- **Litigation history:** [prior IP cases as claimant or defendant — or "none found in quick pass"]
- **Counsel:** [known outside IP counsel — or "none identified"]
- **DJ / unjustified threats risk:** [high / medium / low — reasoning]
- **Relationship risk:** [any customer / investor / partner / acquirer overlap — or "none identified"]

**Automatic escalations this triggers** (per practice profile `## Enforcement posture` → Automatic escalations):
- [list each trigger that this diligence surfaces]

**Confirm before I draft:**
- Do you want to proceed with a C&D against this counterparty, given the diligence above?
- Any of the automatic escalations applicable? If yes, the approver named in the profile signs off before drafting, not after.
```

**Do not proceed to Step 6 (Draft) until the user has engaged with the diligence block.**

If diligence surfaces anything in the practice profile's automatic-escalation list (current customer, bigger counterparty, patent matter, press-attracting, etc.), route to the named approver per the profile — do not draft until the approver has signed off on going forward.

### Step 6: Draft

Draft structure:

1. **Sender / letterhead and date**
2. **Recipient block**
3. **Re: line** — concise, does not reveal privileged strategy. `Re: Unauthorised use of [MARK] (UK Trade Mark Reg. No. [•])`
4. **Opening** — identify the sender, the right, the registration (if any), and the fact of the letter
5. **The right** — trade mark: reg number, class, date of registration, proprietor; copyright: title, date of creation / publication, description, author / employer-owner; patent: patent number, claim(s), jurisdiction; passing off: first use, goodwill, misrepresentation, damage
6. **The infringing conduct** — specific: who, what, where, when, evidence
7. **The legal basis** — `[CITE: TMA 1994 s.10(1)/(2)/(3) / CDPA 1988 s.16 / PA 1977 s.60 / common law passing off]` as applicable
8. **The demand** — numbered, specific, proportionate
9. **The deadline** — calendar date, method of confirmation
10. **Consequences of non-compliance** — calibrated to posture (proceedings in the Intellectual Property Enterprise Court / High Court, injunctive relief, damages, account of profits, costs)
11. **Preservation demand** — documents, communications related to the accused conduct
12. **Reservation of rights** — "without prejudice to any other rights or remedies available to [client]"
13. **Signature block** — approver per practice profile

**Drafting rules:**

- **Specificity over adjectives.** Dates, URLs, reg numbers, samples. Adjectives are a draftsperson's tell that the facts are thin.
- **No overbroad assertions.** If the mark is registered in one class and the accused use is in a different class, say so — don't pretend the registration covers both. Overbroad C&Ds can ground unjustified threats claims (TMA 1994 s.21, PA 1977 s.70).
- **Citations as placeholders unless verified.** `[CITE: TMA 1994 s.10(2)]` stays as a placeholder unless the user provided the cite or the uk-legal MCP returned it. Tag every citation with source — `[uk-legal MCP]`, `[legislation.gov.uk]`, `[user provided]`, `[model knowledge — verify]`. Never strip the tags.
- **Consequence language matches posture.** Aggressive → specific relief threatened (injunction, damages, account of profits, costs). Measured → "we reserve all rights." Conservative → "we'd like to discuss before considering further steps."
- **Post-Brexit hooks** — if the infringement straddles UK and EU (e.g., EUIPO mark holder also wants UK relief on a separate UK mark), distinguish the claims and flag that the EU action requires separate proceedings before the EUIPO or national EU courts, not the UK courts.
- **Passing off alongside registered trade mark.** Where the mark is unregistered, the cause of action is passing off under English common law (*Reckitt & Colman Products Ltd v Borden Inc* [1990] 1 WLR 491 (HL)): goodwill, misrepresentation, and damage. Where the mark is registered, running TMA 1994 and passing off claims in parallel is common.

### Step 7: The loud gate before delivery

Before presenting the draft in-chat or writing the file, display this gate verbatim. **The user must engage with it.**

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS DRAFT GOES ANYWHERE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  This is a draft for solicitor/attorney review — not a      │
│  letter to send. Sending a cease-and-desist letter is an    │
│  assertion of legal rights with real consequences:          │
│                                                             │
│  • It can trigger a declaratory relief application in a     │
│    court of the recipient's choosing. A well-funded         │
│    recipient can use a C&D as an invitation to pick a       │
│    hostile forum.                                           │
│                                                             │
│  • An unjustified threats claim under TMA 1994 s.21 /       │
│    PA 1977 s.70 — a specific UK regime — can result in      │
│    damages and an injunction against YOU if the threats     │
│    are unjustified. Secondary actors (retailers,            │
│    distributors) are especially sensitive.                  │
│                                                             │
│  • It starts a dispute that may not settle cheaply.         │
│                                                             │
│  Confirm before the letter leaves:                          │
│                                                             │
│    1. The rights asserted are valid — registered (pulled    │
│       from the UK IPO / EUIPO register, not assumed) or     │
│       solidly unregistered with evidence of goodwill.       │
│    2. The claim is colorable — a reasonable solicitor /     │
│       attorney would make it on these facts.                │
│    3. The demand is proportionate — we are asking for       │
│       relief the conduct warrants, not everything.          │
│    4. Whoever has authority to start a fight has approved.  │
│    5. Counterparty diligence (Step 5.5) was presented       │
│       and confirmed — entity, size, IP portfolio, prior     │
│       proceedings, counsel, DJ risk, and relationship       │
│       risk. Not conditional. Required.                      │
│    6. Unjustified threats risk assessed — recipients are    │
│       the primary infringer, not downstream secondary       │
│       actors only.                                          │
│                                                             │
│  Approver per your practice profile: [approver name/role    │
│  from Enforcement posture → Approval matrix → C&D row]      │
│                                                             │
│  Automatic escalations that apply here: [list any from the  │
│  practice profile that this matter triggers]                │
│                                                             │
│  Parallel-path status (marketplace conduct): [filed /       │
│  queued / declined — from Step 4. "Not applicable" if       │
│  conduct is not on a marketplace.]                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> Sending a C&D has legal consequences that go beyond the recipient's response — it is an affirmative assertion of rights that can be held against you, and in the UK the unjustified threats regime creates specific exposure. Have you reviewed this with a solicitor or other authorised legal professional? If not, here's a brief to bring to them: [generate a 1-page summary: parties, rights asserted, infringing conduct, demand, posture, risks flagged above, what could go wrong, specific questions for the solicitor/attorney].
>
> If you need to find an authorised legal professional in the UK: the SRA's online register for solicitors; CITMA's finder for Registered Trade Mark Attorneys; CIPA's finder for Chartered Patent Attorneys; the Bar Council's barrister finder; and many Law Centres offer free or subsidised advice on IP for small businesses.

Do not write the file or mark the draft as ready without explicit engagement with the gate.

### Step 8: Output

**Primary:** `<matter-folder>/cease-desist/<slug>/draft-v<N>.docx` (or `cease-desist/<slug>/draft-v<N>.docx` at practice level). Letter-formatted per the draft structure above. Strip the work-product header from the outgoing letter.

**In-chat:** show the draft as plain text for review before writing the file. Iterate before committing to disk.

**Reviewer-facing closing note** (appended to the in-chat preview only, stripped from the file output):

> This is a draft cease-and-desist letter for solicitor/attorney review, not a letter ready to send. Sending it is an assertion of legal rights with the consequences described in the pre-delivery gate. A solicitor, barrister, Chartered Patent Attorney, or Registered Trade Mark Attorney reviews, edits, and takes professional responsibility before sending. Do not send this draft unreviewed.

**Citation verification.** Every `[CITE:___]` and every cite carried from a template or provided authority is unverified until checked against the uk-legal MCP or a primary source. Before sending, verify each cite against legislation.gov.uk or the relevant registry. Preserve the source-attribution tags — `[uk-legal MCP]`, `[govuk MCP]`, `[legislation.gov.uk]`, `[user provided]`, `[model knowledge — verify]` — tags flagged `verify` get checked first.

**Post-send checklist.** After the draft is approved, write `<matter-folder>/cease-desist/<slug>/checklist.md` with: final read by approver, all `[verify]` resolved, all `[CITE]` filled and verified, privilege markings stripped from the outgoing letter, approver signed, delivery method executed, proof of delivery retained, compliance deadline calendared, escalation plan if no response, unjustified threats risk reviewed and cleared, matter created in `matters/` if not already.

## Receive mode — triaging the incoming C&D

### Step 1: Read the letter

Extract:

- **Sender** — entity, signer, outside counsel if any
- **Recipient** — which of our entities/people
- **Delivery method and date**
- **Asserted right** — trade mark (reg number? jurisdiction? UK / EU / both?), copyright, patent, passing off, something else
- **Alleged conduct** — their version of what we're doing
- **Legal basis** — statutes, contract provisions, theories cited
- **Demand** — what they want; is the deadline stated?
- **Threats** — what they say they'll do (IPEC / High Court / UK IPO proceedings?)
- **Tone** — firm / soft / scorched-earth; solicitor/attorney signature usually signals seriousness

### Step 2: Assess the assertion

Not a legal opinion — a structured read:

- **Rights validity.** Are the asserted registrations real and active? (Check UK IPO ™ search / EUIPO eSearch — they are separate registries since Brexit.) For unregistered trade mark / passing off claims, what evidence of goodwill do they actually cite?
- **Plausibility of confusion / similarity / infringement.** On the facts as alleged, is this a colorable claim or is it stretching? For trade mark: likelihood of confusion is the global appreciation test under TMA 1994 s.5(2) — mark similarity, goods/services similarity, distinctive character, visual / aural / conceptual comparison, global assessment. For copyright: has the copyright term expired? Is there a defensible originality or non-copying argument? For passing off: is goodwill credibly established?
- **Overbreadth.** Are they demanding more than the conduct warrants? Overbroad demands weaken leverage and may give us a basis for a threat-is-unjustified counter under TMA 1994 s.21 / PA 1977 s.70.
- **Timing.** Limitation periods under the Limitation Act 1980 (generally 6 years for claims in tort / breach of contract), laches — flag any date issues on the face of the letter.
- **Forum.** Where would they sue — IPEC or High Court? Is there a declaratory relief opportunity for us? Is there a UK IPO inter partes (invalidity / revocation) option that takes the instrument off the board?

### Step 3: Assess our exposure

- **Are we actually infringing?** Honest look. What does the record show?
- **Could we stop easily?** Cost of compliance vs. cost of fight.
- **Is the sender a troll or a real claimant?** Repeat-plaintiff? Known-willing-to-fight?
- **What's at stake beyond this dispute?** Brand equity, customer relationships, precedent.

### Step 4: Options

Present 4-5 options with tradeoffs:

**A — Comply quickly**
- When: the claim is colorable, compliance is cheap, and the fight isn't worth it
- Tradeoff: establishes a concession they may point to later
- Next step: confirm compliance in writing (narrow), do not concede broader theory

**B — Negotiate**
- When: there's a middle-ground business deal (licence, coexistence, rebranding timeline) that resolves it
- Tradeoff: commits time; requires care on without-prejudice / settlement-communication posture (without-prejudice communications are generally inadmissible in UK courts on liability; practical not labelling protection)
- Next step: holding letter + opening negotiation track

**C — Respond firmly (reject)**
- When: their claim is weak, overbroad, or factually wrong; we want to close this down without litigating
- Tradeoff: locks in a position
- Next step: draft a response letter — consider running it through `/ip-legal-uk:cease-desist --send` reframed as a response

**D — Ignore (and preserve)**
- When: the claim is frivolous, the sender has no apparent capacity to sue, the deadline has no legal consequence
- Tradeoff: silence is not necessarily a concession in UK proceedings, but litigation can still follow; legal hold required regardless
- Next step: issue legal hold; log the demand; assess whether a limitation-period-protective application is needed

**E — Pre-empt with declaratory relief or UK IPO proceedings**
- When: we face real business uncertainty, the claim is weak, and we benefit from our own forum; or the registered right can be challenged
- UK options: (1) apply to the High Court or IPEC for a declaration of non-infringement; (2) file a cancellation / invalidity / revocation action at the UK IPO
- Tradeoff: we go on offence; budget and leadership sign-off required
- Next step: escalate to outside counsel per practice profile, do not draft

**F — Counterclaim under unjustified threats (TMA s.21 / PA s.70)**
- When: the letter threatens proceedings against secondary actors without also naming the primary infringer, or the threats are otherwise unjustified on the face of the claim
- Tradeoff: separate positive claim; goes on our docket
- Next step: escalate to outside counsel

Recommend one with two sentences of rationale. Be specific about why.

### Step 5: Deadline triage

- Their stated deadline — note it; UK law does not treat a C&D deadline as legally binding, but ignoring it usually means proceedings follow.
- Our internal decision deadline — typically stated deadline minus enough time to draft, review, and approve a response.
- Legal deadlines — limitation periods under Limitation Act 1980 (6 years for IP torts from the date the cause of action accrued), any contractual cure periods.

### Step 6: Write the triage memo

Output: `<matter-folder>/cease-desist/inbound/<slug>/triage.md` (or at practice level if matter workspaces are off).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# C&D Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** This is an intake scan and options analysis — not a legal merit opinion. The assessment below is a structured read to support counsel's decision on routing and response. Every cited statute, rule, or case is flagged for SME verification; every merit call is the solicitor's/attorney's, not this skill's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Received by:** [entity / person]
**Incoming file:** [path]

## The assertion

**Sender:** [entity, signer, counsel]
**Asserted right:** [trade mark / copyright / patent / passing off — with specifics, reg numbers, jurisdictions]
**Alleged conduct:** [their version, one paragraph]
**Demand:** [list — specific asks]
**Their stated deadline:** [date]
**Tone:** [firm / soft / scorched-earth]

## Rights validity

[Registrations as asserted — `[verify]` against the UK IPO / EUIPO register; passing off claims evaluated against the evidence cited; post-Brexit note if UK and EU marks are in play]

## Legal basis cited

[Each citation inline-tagged with `[verify: applicability / currency / jurisdiction]` and source `[uk-legal MCP / legislation.gov.uk / user provided / model knowledge — verify]`. Do not rely on any citation here without independent check.]

## Plausibility assessment

- **Confusion / similarity / infringement on the facts:** [read]
- **Overbreadth:** [read; note any unjustified threats exposure]
- **Timing issues (limitation period, laches):** [read]
- **Forum:** [their likely forum IPEC / High Court / UK IPO; declaratory relief / counter-action opportunity]

## Our exposure

- **Actually infringing?** [honest look]
- **Cost of compliance vs. cost of fight:** [read]
- **Sender credibility:** [troll / real claimant / prior proceedings — with any evidence]
- **Collateral stakes:** [brand, customers, precedent]

**Triage rating:** [substantial / debatable / weak / frivolous] — *structured read for routing, not a merit opinion; `[verify]`*

## Options

### A. Comply quickly
[Rationale, tradeoffs, next step]

### B. Negotiate
[Rationale, tradeoffs, next step]

### C. Respond firmly
[Rationale, tradeoffs, next step]

### D. Ignore + preserve
[Rationale, tradeoffs, next step]

### E. Pre-empt (declaratory relief / UK IPO)
[Rationale, tradeoffs, next step]

### F. Counterclaim — unjustified threats
[Rationale, tradeoffs, next step]

**Recommendation:** [A/B/C/D/E/F] — [two sentences why] — `[verify: solicitor/attorney to confirm before executing]`

## Deadlines

- **Their stated deadline:** [date]
- **Our internal decision deadline:** [date]
- **Legal deadlines:** [limitation period, cure periods — with dates]

## Immediate actions

- [ ] Legal hold issued — [yes/no]
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
- [ ] Insurance tendered — [yes/no/N-A]
- [ ] Internal escalation — [who/when]
```

**Privilege inheritance block.** Insert one of the following blocks per `## Who's using this`:

- **Role = Solicitor / legal professional:**
  > **Privilege inheritance.** This triage records our first-pass merit read and response posture on an adverse assertion. It is likely subject to legal professional privilege (advice privilege or litigation privilege, if proceedings are reasonably in contemplation). Do not forward, attach to an insurance tender without scrubbing, or share with counterparty. Store with privileged matter material and mark per house privilege conventions. Note: UK LPP is narrower than US work product — see `## Outputs` in the practice profile.

- **Role = Chartered Patent Attorney / Patent Attorney AND patent matter:**
  > **Privilege (patent attorney — CDPA 1988 s.280).** This triage relates to a patent matter and is prepared by or at the direction of a Chartered Patent Attorney. It may be privileged under CDPA 1988 s.280 (patent attorney-client privilege) in connection with the protection of patents before the IPO / EPO. That privilege is limited to patent practice; it does not extend to trade mark, copyright, OSS, contracts, or other non-patent matters. Do not forward or share with counterparty. Bring to supervising solicitor for privilege decisions on non-patent elements.

- **Role = Chartered Patent Attorney / Patent Attorney AND non-patent matter:**
  > **CONFIDENTIAL — NOT PRIVILEGED.** This triage concerns a non-patent matter. A Chartered Patent Attorney's privilege under CDPA 1988 s.280 does not extend beyond patent practice. Treat this document as confidential, bring it to a solicitor, and let them advise on privilege marking. Do not forward it as a privileged document.

- **Role = Registered Trade Mark Attorney / CITMA Registrant:**
  > **Privilege (trade mark attorney — TMA 1994 s.87).** This triage relates to a trade mark matter and may be privileged under TMA 1994 s.87. Do not forward or share with counterparty.

- **Role = Non-lawyer (with or without professional access):**
  > **CONFIDENTIAL — NOT PRIVILEGED.** This document is not privileged unless and until reviewed by a solicitor, barrister, or other authorised legal professional. Treat it as confidential; bring it to counsel and let counsel mark it. Forwarding this document as "privileged" before a solicitor reviews it does not make it so.

Close the in-chat presentation with:

> This is a triage memo, not advice. The strength assessment above is a first read based on the letter alone — it does not account for facts you haven't told me, registrations I can't verify, or jurisdictional issues. A solicitor or authorised legal professional evaluates before you respond, decide to ignore, or commit to a path.

If the user is a non-lawyer, add the "find-a-professional" routing paragraph from send mode.

### Step 7: Hand off

Based on the recommendation and user confirmation:

- Respond firmly → hand off to `/ip-legal-uk:cease-desist --send` with context pre-populated as a response letter.
- Negotiate → start a holding letter / negotiation track in the matter.
- Pre-empt or file to cancel → escalate to outside counsel per the practice profile's IP litigation row; do not draft.
- Matter creation → offer `/ip-legal-uk:matter-workspace new <slug>` pre-populated.
- Comply / ignore → log the decision in the matter history; issue or confirm the legal hold; close the triage record.

## Decision posture

Per `## Decision posture on subjective legal calls` in the practice profile: when uncertain whether there is infringement, whether a mark is confusingly similar, whether a work is substantially similar, whether a claim is colorable, or whether sending is safe — do not silently decide it's fine. Flag for attorney review, surface the factors cutting both ways, note the uncertainty.

## What this skill does not do

- **Send the letter.** Drafting only. The user sends, after approval.
- **Research citations.** Placeholders stay as placeholders unless the user provides authorities or the uk-legal MCP returns them.
- **Bypass the gate.** The send-mode gate runs every time.
- **Decide merit definitively on the receive side.** The rating is a structured read for routing; a formal merit opinion lives with solicitor/attorney.
- **Handle EUIPO proceedings.** UK and EU are separate systems. For EUIPO actions, route to EU-qualified counsel.
- **Make the matter-creation call.** Surfaces the recommendation; user decides.
