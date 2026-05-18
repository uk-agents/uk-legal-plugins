---
name: board-minutes
description: >
  Drafts board or committee meeting minutes in your house format under the
  Companies Act 2006. Auto-detects upcoming board and committee meetings from
  your calendar, asks for the agenda and any slides or pre-read materials, and
  produces a complete draft in the format learned from your seed minutes. Handles
  quorum confirmation, conflict of interest disclosures (CA2006 s.177), and
  the distinction between decisions that can be made at a meeting versus by
  written resolution. Trigger: "board minutes", "draft minutes", "upcoming
  board meeting", "committee minutes", or calendar detection of an upcoming
  board or committee event.
---

# Board Minutes (UK)

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Board minutes are a legal record. They need to be accurate, complete, and in a format that will hold up under scrutiny — whether that's a financing due diligence review, an FCA investigation, an M&A data room, or a shareholder dispute. This skill drafts them in your house format so you spend your time reviewing and correcting, not formatting and re-typing.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → `## Board & Secretary` section:
  - Minutes format (long-form narrative / action minutes / hybrid)
  - Minutes template extracted from seed documents (structure, resolution language, header format)
  - Board composition and committees
  - Written resolutions — what they're used for and any articles limits
- If `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` has no minutes format: run cold-start first. Do not proceed with a generic format.

---

## Step 1: Identify the meeting

### Calendar detection

If the calendar connector is authorised, search for upcoming events matching board and committee keywords:

**Search terms:** "Board of Directors", "Board Meeting", "Audit Committee", "Remuneration Committee", "Rem Committee", "Nomination Committee", "Nom Committee", "Strategy Committee", "Special Committee", "Board of Directors — [Company]"

**Time window:** Look 30 days forward. If no upcoming meeting is found, look 14 days back (minutes are often drafted after the fact).

Present what you find:

> I found the following board or committee meetings on your calendar:
>
> 1. **[Meeting name]** — [Date], [Time], [Location/Virtual]
> 2. **[Meeting name]** — [Date], [Time], [Location/Virtual]
>
> Which one are these minutes for? Or is it a different meeting not on here?

If the calendar connector is not authorised or returns nothing: ask directly — what meeting, what date, what type (full board / which committee)?

### Meeting metadata to confirm

Once the meeting is identified, confirm or fill in:

- **Meeting type:** Full Board of Directors / [Committee name]
- **Date and time**
- **Location or platform** (in-person address / Zoom / Teams / telephone)
- **Notice:** Was proper notice given per the articles? (Standard model articles for private companies reg. 9: reasonable notice. Notice waivers can be signed by all directors who are not otherwise in breach of their duties.) Note: if notice was inadequate, resolutions passed at the meeting may be challenged.

---

## Step 2: Attendance

Ask for the attendee list, or offer to pull from the calendar invite if the connector is authorised.

**Directors present:**
- Pull from board composition in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` as the starting point
- Ask who was actually present, who was absent, and whether any absent directors had advance notice
- Note: a director participating by telephone or video conference is generally treated as present if the articles permit it (standard model articles reg. 10 permits this)

**Management present:**
- Who from management attended? (CFO, Company Secretary, Head of Finance, etc.)
- Note: management attendees are typically listed separately from directors

**Guests:**
- Outside solicitors present? (Name and firm)
- Auditors, investment bankers, or other advisers?
- Any guests who attended for specific agenda items only (note their attendance as limited to that item)

**Chair:**
- Who chaired the meeting?
- Who acted as secretary for the meeting?

**Quorum:**

- Check the articles for the quorum requirement. Standard model articles for private companies (CA2006 Sch. 1, reg. 11): quorum is two directors unless the company has only one director. Check if any director has a conflicting interest (CA2006 s.175) that causes them to be excluded from quorum for a particular item.
- Confirm quorum was present. If not: stop and flag before drafting. Do not produce minutes that imply a valid meeting occurred. Surface the question to outside solicitors — the remediation path depends on the articles and the nature of the action.
- **Scottish companies:** same CA2006 rules but confirm with Scottish counsel if any doubt about articles interpretation.

---

## Step 3: Materials

Ask for the meeting materials.

> Can you share the agenda and any pre-read materials for this meeting? Even a rough agenda is enough to structure the minutes. If there were board slides or a management presentation, upload those too — I'll use them to fill in the agenda item summaries.
>
> If materials weren't distributed in advance, tell me the agenda items and I'll draft placeholders for each.

**From the agenda and slides, extract:**
- Agenda items in order
- Any resolutions proposed (look for board approval language: "approve," "authorise," "ratify," "adopt," "declare")
- Any exhibits referenced (management presentations, financial reports, legal memos, valuations)
- Any votes expected

---

## Step 4: Draft the minutes

Use the house format from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. Do not default to a generic format. The seed minutes are the template — replicate the structure, the header, the resolution language, the level of discussion detail.

### Standard structure (adapt to house format)

**Header block:**
```
MINUTES OF A MEETING OF THE BOARD OF DIRECTORS
[OR: MINUTES OF THE [COMMITTEE NAME] OF THE BOARD OF DIRECTORS]
OF [COMPANY NAME] (registered number [XXXXXXXX])

Held on [Date] at [Location / by video conference / by telephone]
at [Time]
```

**Opening:**
- Meeting called to order by [Chair name] at [time]
- Notice: [proper notice given per articles / notice waived by all directors]
- Quorum confirmed: [N of M directors present]
- Secretary for the meeting: [name]

**Attendees:**
- Directors present: [list — note participation by telephone/video if relevant]
- Directors absent: [list, if any]
- Also present: [management, outside solicitors, guests — with roles]

**Declaration of interests (CA2006 s.177):**
Standard entry when conflicts arise:
> [Director Name] declared an interest in [item/agenda point] pursuant to section 177 of the Companies Act 2006. [Director Name] [withdrew from the meeting during discussion of this item / remained but did not participate in the vote] in accordance with the Company's Articles of Association.

If no conflicts: brief note — "No director declared an interest in any of the matters to be discussed."

**Previous minutes:**
Standard language: approval of minutes from prior meeting. Pull date of prior meeting from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` board calendar if available.

**Agenda items — one section per item:**

```
[AGENDA ITEM TITLE]

[Chair/presenter name] [presented / reported on / led a discussion of] [topic].

[Discussion summary — see drafting notes below]

[If resolution follows:]
After discussion, the following resolution was passed [unanimously / by [N] votes to [N]]:

IT IS RESOLVED THAT [resolution text in house language from config].
```

**Adjournment:**
Standard language: meeting adjourned at [time], there being no further business.

**Signature block:**
Chairman/chair signature line. Some formats include a company secretary countersignature.

---

### Drafting notes

**Discussion summaries:** Follow the house format from seed documents exactly:

- *Long-form narrative:* Summarise the substance of the discussion — what questions were raised, what information was presented, what factors the board considered. Do not quote individuals unless the specific attribution matters legally.
- *Action minutes:* Note only what was presented and what action was taken. No discussion content beyond "the board discussed the matter."
- *Hybrid:* Full narrative for major items (acquisitions, financials, significant approvals), action-only for routine items.

When materials were provided: pull summary content from the slides and management presentation. The board "received and considered" a presentation — summarise what the presentation covered.

When no materials: insert `[PLACEHOLDER — summarise discussion here]` and flag it clearly. Do not fabricate discussion content.

**Resolutions:** Use the exact resolution language from the seed minutes — "IT IS RESOLVED THAT" vs. "RESOLVED THAT" vs. "IT IS HEREBY RESOLVED" vs. "BE IT RESOLVED THAT". The language is house style, not interchangeable.

**CA2006 s.177 declarations:** If a director has a material interest in a proposed transaction, the declaration must be made at the meeting (or as soon as practicable after the director becomes aware) and recorded in the minutes. This is a statutory obligation — do not omit conflict disclosures.

**Exhibit references:** Number exhibits in the order they appear (Exhibit A, B, C). Common exhibits: management presentation, financial statements, valuation reports, legal opinions, waivers of notice.

---

## Step 4.5: Consequential-action gate (adopt minutes)

**Before adopting minutes as final:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Adopting minutes makes them the official record of what the board decided — they're the primary evidence of authorisation for the actions taken at the meeting. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
>
> - What was decided (resolutions, votes, who was present)
> - What the draft captures and what is still a placeholder
> - Open questions (any flagged attendance, quorum, or conflict notes)
> - What could go wrong (misstated resolutions, missing conflict declarations under CA2006 s.177, quorum defects, privilege leakage in discussion summaries)
> - What to ask the solicitor (is the discussion depth right for this board's practice; are conflict declarations correctly recorded; do any items need more documentation)
>
> If you need to find a solicitor: contact the SRA at sra.org.uk, the Law Society of Scotland at lawscot.org.uk, or the Law Society of Northern Ireland at lawsoc-ni.org for a referral service.

Do not produce the final adoption-ready version past this gate without an explicit yes. A marked-DRAFT for solicitor review is fine.

---

## Step 5: Output and review prompts

Produce the full draft. The minutes themselves are a corporate record, not privileged; do not apply the work-product header to the minutes as circulated. The drafting notes, placeholder flags, and review checklist below are work product — prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` `## Outputs`.

After the draft, add a review checklist:

```
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

REVIEW CHECKLIST — please verify before circulating:

□ All directors confirmed present/absent (check against actual attendance)
□ Quorum confirmed correct (check articles)
□ Any director joining by telephone/video conference — confirm articles permit this
□ CA2006 s.177 conflict declarations recorded where required
□ Resolution language matches what was actually approved (check wording carefully)
□ Votes recorded correctly — any abstentions or dissents to note?
□ Exhibits numbered and referenced correctly
□ Any executive sessions held? (Add separate executive session note if so)
□ Notice of meeting confirmed (or waiver signed)
□ Company registration number included in header
□ Outside solicitors reviewed? (If required by your process)
□ Time of adjournment to fill in
```

Flag any sections where content is a placeholder and needs the solicitor's input before the minutes are accurate.

Add as a final pre-adoption note on the draft, stripped before adoption:

> This is a draft for solicitor review, not adopted minutes. Adopted minutes are the official record of board action and carry legal consequences — a qualified solicitor reviews, edits, and takes professional responsibility before adoption. Do not adopt this draft unreviewed.

---

## Written resolutions

For drafting written resolutions in lieu of a meeting, use `/corporate-legal-uk:written-consent`. That skill handles precedent search, CA2006 rules confirmation, and the scope warning for major one-off actions.

---

## What this skill does not do

- It does not attend the meeting or capture real-time discussion — it drafts from materials and solicitor input.
- It does not determine whether a resolution is legally valid or sufficient — it drafts in house format; legal judgment on adequacy is the solicitor's call.
- It does not finalise minutes — the draft requires solicitor review before circulation.
- It does not distribute minutes — output is for the solicitor to review, edit, and circulate via their own process.
- It does not advise on whether a meeting quorum was valid — it flags the question, the solicitor decides.
