---
name: written-consent
description: >
  Draft a written resolution of the board, a committee, or the shareholders
  under the Companies Act 2006, in house format, with precedent search from the
  resolutions repository. Handles multi-resolution written resolutions, director
  conflict flags, CA2006 notice requirements, signatory tracking, and a built-in
  scope warning for major one-off actions. Use when user says "written resolution",
  "board resolution", "written consent", "shareholder resolution", "resolution in
  lieu of meeting", or describes an action needing board or shareholder approval
  without a meeting.
argument-hint: "[describe the action needing board or shareholder approval]"
---

# /written-consent

1. Load `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → Board & Secretary (resolutions repository, resolution language, company type and nation, board composition).
2. Use the workflow below.
3. Identify the action and classify (routine / review-flag).
4. If review-flag: show outside solicitors warning and confirm before proceeding.
5. Search resolutions repository for closest precedent. If no repository: use seed resolutions from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`.
6. Draft resolution in house format using precedent as base.
7. Output: resolution draft + signatory checklist + review prompts.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Most routine board approvals don't need a meeting. Officer appointments, dividend declarations, bank authorisations, contract approvals above the officer threshold, intercompany arrangements — these happen by written resolution under the Companies Act 2006. This skill drafts them quickly in your house format, finds the prior resolution that's closest to what you need, and flags the actions where you should be getting outside solicitors' eyes before anyone signs.

## CA2006 written resolution rules — read before drafting

**Private companies (Ltd):**
- CA2006 ss.288–300: a private company may pass a resolution in writing without a meeting.
- Ordinary resolution: simple majority of the total voting rights of eligible members.
- Special resolution: not less than 75% of the total voting rights of eligible members.
- A member who would have been disenfranchised at a meeting (e.g., conflict under articles) is still excluded from the written resolution.
- Written copies of the proposed resolution must be sent to every eligible member simultaneously (or as near as reasonably practicable).
- A written resolution lapses if not passed within 28 days (or such longer period as the articles allow) of the circulation date.
- A member must signify agreement to the resolution in writing. Agreement is irrevocable.

**Public companies (plc):**
- CA2006 s.281(2): shareholder written resolutions are NOT permitted for public companies. Shareholder resolutions require a meeting.
- Board (directors) written resolutions of a plc: permitted if the articles allow it. Standard model articles for public companies do not include a board written resolution provision — check the specific articles.

**Board written resolutions:**
- Directors may pass a board resolution by written means if the articles permit (common in bespoke articles for both Ltd and plc).
- Unanimity is typically required for directors' written resolutions unless the articles say otherwise.
- A conflicted director must still comply with CA2006 s.177 (duty to declare interest in proposed transaction). Depending on the nature of the conflict and the articles, the conflicted director may be excluded from signing.

**Key actions that CANNOT be done by written resolution (private company shareholders):**
- Removal of a director under CA2006 s.168 (requires meeting with special notice)
- Removal of an auditor under CA2006 s.510 (requires meeting with special notice)

## Scope warning — read before drafting

> **This skill is designed for day-to-day resolutions with direct precedents in your repository or seed documents.** Routine actions — officer appointments, dividend declarations, annual authorisations, standard contract approvals — are the right use case.
>
> **For major one-off actions, outside solicitors' review is prudent regardless of what this skill produces.** This includes: M&A transactions (asset purchases, share purchases, mergers, investments), financing rounds, equity issuances to new investors, change-of-control provisions, dissolution or winding up, material real estate transactions, and any action that will be scrutinised in a subsequent due diligence process.
>
> The skill will flag automatically when the action looks like a major one-off. That flag is not a block — you can proceed. It is a prompt to think about whether a clean precedent-adapted draft is sufficient for this particular action.

---

## Major action + urgency = stop

A written resolution for a major one-off action (M&A, financing, dissolution, capital structure change, director appointment tied to a financing or M&A) that the user wants executed TODAY goes through outside solicitors' review. Not because the plugin can't draft it — because a wrong written resolution on a major action is a one-way door, and the urgency pressure is exactly when mistakes happen.

Trigger (both must be true):

1. The action is in the **Review flag — major one-off** category below.
2. The user's ask contains an irreversibility signal — "send for DocuSign," "sign today," "board is signing this afternoon/tonight," "need this before [market open / completion / the meeting at X]."

When both are true, output this and stop:

> ⛔ **Major action + same-day signature — I won't mark this ready to sign.**
>
> This is [action type], which is a one-way door. You've asked for it to be signed today. That combination is exactly when mistakes on a written resolution become hardest to unwind.
>
> I'll draft it — happily — but I won't mark it ready to sign without an outside-solicitors look. If outside solicitors are already engaged on this deal, hand them this draft. If not, this is the thing outside solicitors are for. Contact the SRA at sra.org.uk, the Law Society of Scotland at lawscot.org.uk, or the Law Society of Northern Ireland at lawsoc-ni.org for a solicitor referral service.
>
> Two ways forward:
>
> 1. **I draft, outside solicitors review, then signatures** — the normal path for a major corporate action. Tell me to draft and I will.
> 2. **Outside solicitors are already on this deal and cleared the draft path** — tell me who reviewed and when. I'll proceed and include a note that outside solicitors have the draft.
>
> I will not draft in "ready-to-send" form under same-day pressure without one of those two.

---

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → `## Board & Secretary`:
  - Resolutions repository location
  - House resolution language
  - Company type (Ltd / plc) and nation (E&W / Scotland / NI)
  - Board composition (for signatory list)
  - Written resolutions — scope and any articles limits

### No-precedent hard stop

If (a) no resolutions repository is configured in `## Board & Secretary` → Resolutions repository, AND (b) no seed resolution document has been provided to this skill, **STOP before drafting**. Output exactly this block and wait for a response:

> **No precedent available — stopping before draft.**
>
> I don't have a precedent to match. A written resolution drafted without your house format will need more correction than it saves — resolution language, recital depth, authorisation boilerplate, and signature-block conventions all carry house-specific choices.
>
> Two ways to unblock:
>
> 1. **Paste or upload a prior resolution** (any recent written resolution from this company in any category — I extract the format, not the substance), OR
> 2. **Tell me "draft from a generic template anyway — I'll adjust the formalities myself"** — only pick this if you know you'll rework the resolution language and signature block by hand before circulation. Say it explicitly.
>
> Which do you want to do?

---

## Step 1: Identify the action

Ask the user what action the board or shareholders need to approve. Gather:

- **What is being approved?** (One sentence.)
- **Any supporting detail?** E.g., name of officer being appointed, dividend amount, counterparty and contract value.
- **Effective date:** Today, or a specific date?
- **Who must sign:** Full board, a committee, or the members/shareholders? If the `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` written-resolution scope says certain actions require a meeting rather than a written resolution (e.g., removal of director under s.168), flag it now.
- **Any director conflict?** Does any director have a material interest in the action being approved? If yes: flag it. The conflicted director must comply with CA2006 s.177 (duty to declare interest). Depending on the articles, the conflicted director may be excluded from voting on / signing.
- **Company type:** Confirm Ltd or plc. If plc, shareholder written resolutions are not permitted (CA2006 s.281(2)) — flag and stop if the user is asking for a plc shareholder written resolution.

### Action classification

Classify the action before searching for precedent:

**Routine — direct precedent likely:**
- Director appointment or resignation/removal (but: removal under s.168 requires meeting with special notice — flag)
- Dividend declaration (interim dividend by board; final dividend requires shareholder ordinary resolution)
- Bank account authorisation or signatory update
- Approval of a contract below a material threshold
- Annual authorisation resolutions (tax matters, pension scheme, benefits plans, etc.)
- Intercompany loan or services agreement at arm's length terms
- Change of registered office address
- Allotment of shares under existing authority (CA2006 s.551 authority)

**Review flag — major one-off, outside solicitors prudent:**
- M&A transaction (acquisition, merger, asset purchase, investment)
- New financing round or debt facility
- Equity issuance to a new investor (requires s.551 board authority + disapplication of pre-emption rights under s.570 by shareholder special resolution)
- Change-of-control provision or trigger
- Approval of an agreement that itself requires board approval under CA2006 (e.g., s.190 substantial property transaction — value >£100k or 10% of net asset value; loan to director exceeding £10k under s.197)
- Winding up, dissolution, or entering administration
- Material real estate transaction
- Any action that will appear as a board approval exhibit in a future financing or M&A data room

If the action is in the review-flag category, show this before drafting:

> ⚠️ **Outside solicitors' review recommended.** This looks like [action type], which is a major corporate action where a precedent-adapted draft may not be sufficient. Consider having outside solicitors review before circulation. Want me to proceed with a draft anyway?

---

## Step 2: Search for precedent

### If resolutions repository is connected

Search the repository for the closest prior resolution. Return the most recent matching resolution, or ask the user to choose if multiple close matches exist. Read the selected resolution. Extract: resolution language, recital structure, authorisation language, any specific conditions or carve-outs. Note any differences between the prior action and the current one.

### If no repository (seed documents only)

Extract the format from the seed resolutions in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. Note that no precedent search is available.

---

## Step 3: Draft the resolution

Use the house format. The structure below is the standard for a board written resolution — adapt to match the precedent or seed format exactly.

```
WRITTEN RESOLUTION
[OF THE BOARD OF DIRECTORS / OF THE [COMMITTEE NAME]]
OF [COMPANY NAME] (registered number [XXXXXXXX])

[Date]

The undersigned, being all of the directors [members of the [Committee]] of
[Company Name] (registered in England and Wales under number [XXXXXXXX])
(the "Company"), hereby pass the following resolution by way of written
resolution pursuant to [the Company's Articles of Association / Article [X]
of the Company's Articles of Association]:

[AGENDA ITEM / ACTION HEADING — if multiple resolutions]

[Background note (if used in house format) — one or two sentences stating
the relevant facts and why the board is being asked to act.]

IT IS RESOLVED THAT [the specific action being approved, in precise language
— name names, state amounts, reference the specific agreement or instrument
where applicable];

IT IS FURTHER RESOLVED THAT [any related or implementing resolution — e.g.,
the specific officers authorised to sign documents, the authority granted];

IT IS FURTHER RESOLVED THAT the officers of the Company be and are hereby
authorised to do all such acts and things and to execute all such documents,
instruments, and agreements as may be necessary or desirable to give effect
to the foregoing resolution; and

IT IS FURTHER RESOLVED THAT any actions previously taken by any officer of
the Company in connection with the foregoing are hereby ratified and approved.

[Repeat block for each additional action if multi-resolution written resolution]

IN WITNESS WHEREOF the undersigned have signed this written resolution on
the date written above.

[SIGNATURE BLOCKS — one per required signatory]

_______________________________
[Director Name]
Date: _______________

[Repeat for each director / committee member]
```

**For shareholder written resolutions (private company only):**
Adapt the opening to:
```
WRITTEN RESOLUTION OF THE MEMBERS
OF [COMPANY NAME] (registered number [XXXXXXXX])

[Date]

The members of [Company Name] (the "Company") whose signatures appear below,
being not less than the requisite majority of the eligible members of the
Company, hereby pass the following resolution as [an ordinary / a special]
resolution of the members of the Company pursuant to section 288 of the
Companies Act 2006:

[Resolution text...]

[Note: This written resolution was circulated to all eligible members on
[date]. The resolution will lapse if not passed within 28 days of that date.]
```

### Resolution drafting notes

- **Be precise.** Vague resolutions create problems in due diligence. "Approved the transaction" is not useful. "Approved the Share Purchase Agreement dated [date] between [Buyer] and [Sellers] relating to the acquisition of [Target Company Ltd] (registered number [XXXXXXXX]), substantially in the form attached hereto as Exhibit A" is.
- **Name the authorised signatories.** Don't just say "officers" if a specific officer needs authority for a specific thing. Name them.
- **Reference exhibits.** If a document is being approved, attach it as an exhibit and reference it in the resolution.
- **Match the house language exactly.** "IT IS RESOLVED THAT" vs. "RESOLVED THAT" vs. "IT IS HEREBY RESOLVED" — use whatever is in the precedent or seed documents.
- **Include the company registration number.** Standard UK practice to include it in board resolutions.

---

## Step 4: Confirm the CA2006 rules for this company

Check the company type (Ltd / plc), nation of incorporation (E&W / Scotland / NI), and articles of association provisions in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. Research the written-resolution requirements before drafting:

**For board written resolutions:**
- Do the articles permit board written resolutions? (Model Articles for private companies reg. 8 allows this; public company model articles do not have an equivalent — check the specific articles.)
- Is unanimity required, or does a majority suffice? (Standard model articles for private companies: unanimous agreement of all eligible directors.)
- Are there any articles provisions excluding conflicted directors from signing?

**For shareholder written resolutions (Ltd only):**
- CA2006 s.288: confirm private company.
- Ordinary or special resolution? (Ordinary: simple majority of eligible members. Special: 75%+. CA2006 s.282/s.283.)
- Actions requiring special resolution: change of articles (s.21), reduction of capital (s.641), re-registration (s.89), winding up (IA1986 s.84). `[verify]`
- 28-day lapse period unless articles extend it.
- Circulation requirement: send simultaneously to all eligible members.

**Scotland-specific note:** CA2006 applies throughout the UK but confirm with Scottish counsel for any Scottish-incorporated entity where there may be Scots law procedural nuances.

Cite the controlling statute section and any articles provisions relied on. Verify currency. Flag uncertainty for solicitor verification rather than stating a rule you haven't confirmed.

---

## Step 4.5: Consequential-action gate (execute resolution)

**Before proceeding to output:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Executing a written resolution has legal consequences — it binds the company and becomes a corporate record. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
>
> - What the action is (the resolution)
> - What the analysis found (CA2006 articles rule, signature threshold, any flagged conflicts)
> - Open questions (anything flagged for solicitor verification above)
> - What could go wrong (invalid resolution, breach of fiduciary duty, signature defect, conflict not properly handled, CA2006 s.168/s.510 meeting requirement not met)
> - What to ask the solicitor (is this the right vehicle; are there missing recitals; does the articles permit written resolution for this action; is the conflict properly handled)
>
> If you need to find a solicitor: contact the SRA at sra.org.uk, the Law Society of Scotland at lawscot.org.uk, or the Law Society of Northern Ireland at lawsoc-ni.org for a referral service.

Do not produce the final signatory-ready draft past this gate without an explicit yes. Research, format extraction, and a marked-DRAFT for solicitor review are fine.

---

## Step 5: Output

Produce:

1. **The resolution draft** — complete, ready to review and circulate. The executed written resolution itself is a corporate record, not privileged; do not apply the work-product header to the resolution as circulated. The drafting notes, signatory tracker, and analysis below are work product — prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` `## Outputs`.

2. **Signatory checklist:**
```
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

SIGNATORY CHECKLIST — [Action] — [Date]

Required signatories:
□ [Director Name 1]
□ [Director Name 2]
□ [Director Name 3]
[etc. — pulled from board composition in config]

Conflict disclosures:
[None / [Director Name] has a disclosed interest under CA2006 s.177 — confirm whether exclusion or disclosure is appropriate under the articles]

CA2006 rule: [confirmed rule for this company type / confirm with solicitor]
```

3. **Review prompts:**
```
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

BEFORE CIRCULATING — check:
□ Resolution language precisely describes the action (no vague approvals)
□ Correct effective date
□ All required exhibits attached and referenced
□ Authorised signatories named correctly
□ Any director conflicts disclosed or resolved per CA2006 s.177
□ For shareholder written resolutions: all eligible members identified and copies circulated simultaneously
□ 28-day lapse period noted on shareholder written resolutions
□ For major actions: outside solicitors have reviewed
□ Company registration number included
```

4. **Final note on the draft — add before circulation.** Prepend to the resolution draft as a separate pre-execution note, then strip before the resolution is signed:

> This is a draft for solicitor review, not an executed resolution. Executing it binds the company and becomes a corporate record — a qualified solicitor reviews, edits as needed, and takes professional responsibility before it goes out. Do not circulate for signature unreviewed.

---

## What this skill does not do

- It does not determine whether an action legally requires board or shareholder approval — that judgment belongs to the solicitor.
- It does not advise on director fiduciary duties or conflict of interest resolution — it flags conflicts, the solicitor handles them.
- It does not replace outside solicitors' review for major transactions.
- It does not circulate the resolution — output is for the solicitor to review and send via their own process.
- It does not track returned signatures — the signatory checklist is a starting point.
- It does not advise on CA2006 s.168 or s.510 situations (director/auditor removal) — these require a meeting with special notice and cannot be done by written resolution.
