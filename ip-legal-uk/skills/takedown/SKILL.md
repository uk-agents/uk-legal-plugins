---
name: takedown
description: >
  Draft a copyright takedown notice, triage one you received, or draft a
  counter-notice. Use when asserting copyright through an online notice
  (UK/EU and platform-specific regimes), when an incoming takedown needs
  triage into comply / counter / engage / ignore options, or when drafting a
  counter-notification. Handles UK Online Safety Act, EU Digital Services Act,
  and platform-specific IP notice regimes.
argument-hint: "<--send | --respond | --counter> [context or path to incoming notice]"
---

# /takedown

Three modes. Pick one:

- `/ip-legal-uk:takedown --send` — draft a copyright takedown notice for the relevant regime (UK platform / EU DSA / DMCA where applicable). Fair-dealing gate + false-statement/perjury gate before delivery.
- `/ip-legal-uk:takedown --respond` — triage a takedown someone sent you. Options: comply / counter / engage / ignore.
- `/ip-legal-uk:takedown --counter` — draft a counter-notification / objection. Gate for false-statement exposure and litigation risk before delivery.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "Run `/ip-legal-uk:cold-start-interview` first."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip. If enabled and no active matter, ask which matter.

3. **Dispatch on `$ARGUMENTS`:**
   - `--send` → run send mode. Walk identify-the-work, identify-the-infringing-material, regime selection, fair-dealing gate, good-faith belief, draft, loud gate, output.
   - `--respond` → run respond mode. Read the incoming notice, assess (licence, fair dealing, defects, regime, sender credibility), present options, write the triage memo.
   - `--counter` → run counter mode. Confirm predicate (material taken down in response to a notice), good-faith belief of mistake/misidentification, litigation risk acknowledged, draft counter-notification, loud gate, output.
   - No flag → ask once: "Are we sending a takedown, triaging one we received, or drafting a counter-notice?"

4. **Respect the gates.** In `--send` and `--counter`, the loud gate runs before any final output is written. The fair-dealing gate in `--send` is separate and runs earlier.

5. **Jurisdiction is central.** The UK and EU are separate regimes post-Brexit. The DMCA is US law. Identify the applicable regime before drafting.

6. **Hand off where appropriate.** `--respond` with a counter-notice recommendation chains into `/ip-legal-uk:takedown --counter`, but only after the triage memo has been reviewed and the decision to counter made deliberately.

## Examples

```
/ip-legal-uk:takedown --send
/ip-legal-uk:takedown --respond ~/Downloads/youtube-takedown-notice.pdf
/ip-legal-uk:takedown --counter
/ip-legal-uk:takedown
```

## Notes

- The outgoing notice and counter-notice do not carry the work-product header. Internal drafts, fair-dealing analyses, and triage memos do.
- Notices are element-by-element — every required element must be present or the notice is defective under the applicable regime.
- Counter-notices in some regimes may be treated as evidence in subsequent proceedings. This is not a formality.
- Non-lawyer users get a one-page brief for the solicitor conversation before the gate clears.

---

## Purpose

Online copyright enforcement uses formal notice-and-takedown procedures. A
takedown notice makes representations about copyright ownership and the
allegedly infringing nature of the material — making false representations
exposes the sender to liability. A counter-notice is a formal objection that
can escalate to litigation. This skill handles all three moves with the
guardrails each warrants.

> **External deliverables (send and counter modes):** the outgoing notice/
> counter-notice is not a privileged document — it's a statement made in a
> formal process. Do NOT include the `PRIVILEGED & CONFIDENTIAL` header on the
> outgoing document. Internal drafts, fair-dealing analyses, and triage memos
> keep the header per plugin config `## Outputs`.

## Applicable regimes — choose the right instrument

**This is the most important step.** "Takedown" is used loosely, but the
regimes differ materially:

| Regime | Where it applies | What it does |
|---|---|---|
| **UK Online Safety Act 2023 (OSA)** | UK-regulated platforms | Illegal content regime; Part 3 covers copyright infringement as a category of illegal content for certain platforms. Notice-and-action procedures vary by platform's regulatory obligations. Not yet fully in force as of 2024-2025 rollout. |
| **EU Digital Services Act 2022 (DSA) Art. 16** | EU-established platforms / platforms with significant reach in EU | Requires "trusted flaggers" and a notice-and-action mechanism for illegal content (including IP infringement). Different from DMCA; no automatic takedown with just a notice. |
| **Platform-specific IP enforcement** | All major platforms globally | YouTube Content ID, Meta Rights Manager, Amazon Brand Registry, eBay VeRO, TikTok IP reporting, X/Twitter copyright reporting, GitHub DMCA, Shopify copyright reporting. Each platform has its own intake process. |
| **US DMCA §512** | US-based or US-subject service providers | The US notice-and-takedown regime; perjury statement; §512(f) liability for misuse. Applies to platforms subject to US law. Non-US platforms are not legally obligated to respond to DMCA notices, but many follow the process voluntarily. |
| **UK courts / CDPA 1988 s.97A** | When platform-level action is insufficient | High Court injunction ordering ISPs to block access to infringing material or requiring hosts to take down content. Last resort; requires proceedings. |

Determine the applicable regime(s) for the specific platform and content.
In practice, most UK practitioners send platform-specific notices (through the
platform's own reporting tool) rather than formal statutory notices, and fall
back to the DSA Art. 16 process for EU-established platforms or DMCA notices
to US-based platforms as applicable.

**Post-Brexit note.** The DMCA (17 U.S.C. §512) is US federal law. EU DSA
Art. 16 is EU law — it applies to platforms established in the EU or to
"very large online platforms" with significant EU reach. UK platforms fall
under the UK Online Safety Act. UK copyright (CDPA 1988) subsists in UK-authored
works and is the applicable copyright law for UK enforcement, but the
*enforcement mechanism* (which notice regime to use) depends on where the
platform is legally established, not where the infringement is.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` → `## IP practice profile` (copyright in scope?), `## Enforcement posture` → `Approval matrix → Online takedown (ordinary)` row, `## Outputs` (work-product header, role), `## Who's using this` (role)
- **Matter context:** Check `## Matter workspaces` as standard.

## Send mode — drafting an online takedown notice

### Step 1: Identify the copyrighted work

> What is the copyrighted work?
>
> - **Title / description** — what is the work (software, image, text, video, audio)?
> - **UK copyright status** — is this a UK-created or UK-protected work under CDPA 1988? There is no UK copyright registration system — copyright subsists automatically on creation.
> - **Ownership** — is the claimant the author / employer (CDPA s.11 employed works) / exclusive licensee with the right to bring infringement proceedings?
> - **Prior licensing** — have we ever licensed this use, or a broader use that might cover it?

UK copyright arises automatically on creation (CDPA 1988 s.1). The author is
the first owner unless it is an employed work (CDPA s.11(2): employer owns
copyright in works made in the course of employment) or it has been assigned
(CDPA s.90: must be in writing, signed by the assignor).

### Step 2: Identify the infringing material and platform

> Where is the infringing material?
>
> - **Platform / service provider** — YouTube, Meta/Instagram/Facebook,
>   TikTok, X/Twitter, GitHub, Amazon Marketplace, eBay, Etsy, a web host?
> - **URL(s)** — specific links to the infringing material.
> - **Description** — what is the infringing material and how does it infringe?
> - **Evidence** — screenshots, URL captures, timestamps, watch-service report.

From the platform, determine which regime / intake form applies:

- **YouTube:** YouTube's copyright reporting form (separate from DMCA in practice; YouTube uses its own process compatible with DMCA §512).
- **Meta/Instagram:** Meta's Intellectual Property Report portal.
- **TikTok:** TikTok's IP reporting form.
- **X/Twitter:** X's copyright policy reporting form.
- **GitHub:** GitHub's copyright removal request (GitHub follows DMCA §512 process for US law purposes).
- **Amazon:** Amazon Brand Registry / Report a violation.
- **eBay:** eBay VeRO (Verified Rights Owner programme).
- **EU-established platforms:** DSA Art. 16 notice-and-action mechanism where applicable.
- **UK hosts / platforms:** Platform-specific reporting or, as a last resort, CDPA 1988 s.97A injunction application.

### Step 3: Fair-dealing gate

Before drafting a notice, consider whether the accused use may be a **fair dealing** under CDPA 1988 ss.29–31. UK fair dealing is purpose-specific — not a general balancing test like US fair use.

> Walk through the applicable permitted acts before we draft the notice:
>
> 1. **Research or private study (s.29)?** — non-commercial research; probably not for commercial reproductions.
> 2. **Criticism, review, or reporting current events (s.30)?** — does the accused use quote for the purpose of criticism or review with sufficient acknowledgement?
> 3. **Parody, pastiche, or caricature (s.31A)?** — is the accused use a parody of the original work (fair dealing required)?
> 4. **Education (ss.32–36)?** — educational establishments have specific fair dealing rights.
> 5. **Any other CDPA permitted act (ss.28–76)?** — check if any applies.
>
> Your read on each? And your conclusion — fair dealing clearly inapplicable, debatable, likely applicable?

Record the answer. If "debatable" or "likely applicable," do not draft. Stop and route to solicitor review: "A fair dealing defence is debatable/likely on these facts. Sending a takedown notice when the use is arguably protected is the fact pattern for a false-statement liability and potential abuse-of-process criticism. Route this to a solicitor before any notice goes out."

### Step 4: Good-faith belief and accuracy

Before including the standard good-faith statement in any notice:

- Confirm the work is ours to assert (own it outright, or have exclusive licence with enforcement rights).
- Confirm the use is not licensed (no prior deal, no Creative Commons or open-access grant that would cover it).
- Considered fair dealing (Step 3)?
- Reviewed the accused content directly?

If yes on all four, the good-faith belief is defensible. If no on any, pause.

### Step 5: Draft the notice

Tailor the notice to the platform's required format. Core elements common to most regimes:

1. **Sender identification** — name, company, contact details
2. **Identification of the copyrighted work** — title, description, nature of the work, creator, date
3. **Identification of the infringing material** — URL(s), description of the infringing use, why it infringes
4. **Statement of good-faith belief** — "I have a good faith belief that the use of the copyrighted material described above is not authorised by the copyright owner, its licensee, or the law (including any applicable fair dealing provisions)"
5. **Statement of accuracy** — "The information in this notice is accurate and I am [the copyright owner / duly authorised to act on behalf of the copyright owner]"
6. **Signature** — electronic or physical

**Note on false statements.** While the DMCA's specific perjury penalty (17 USC §512(f)) does not apply in UK law, making false representations to a platform to have material removed may constitute: (a) malicious falsehood under English law, (b) misuse of the platform's process which could lead to platform sanctions, or (c) grounds for a counterclaim by the person whose content is removed. The standard should be the same: accuracy and good faith.

### Step 6: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS NOTICE GOES ANYWHERE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A takedown notice makes formal representations about       │
│  copyright ownership and alleged infringement. Sending a    │
│  notice you know to be inaccurate or misleading can         │
│  expose you to liability for:                               │
│                                                             │
│  • Malicious falsehood (under English law)                  │
│  • Platform sanctions for abuse of notice process           │
│  • A counterclaim by the person whose content is removed    │
│                                                             │
│  For DMCA-regime notices (to US-based platforms): the       │
│  penalty for knowing material misrepresentation is          │
│  damages under 17 U.S.C. §512(f).                           │
│                                                             │
│  Confirm before the notice leaves:                          │
│                                                             │
│    1. We own the copyright, or hold an exclusive licence    │
│       with enforcement rights (CDPA 1988 s.90 formalities   │
│       satisfied for any assignment).                        │
│    2. The accused use is not authorised — no licence, no    │
│       fair dealing (CDPA ss.29–31).                         │
│    3. We have considered fair dealing specifically (Step 3) │
│       and our conclusion is on the record.                  │
│    4. Whoever has authority to assert approves sending.     │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Enforcement posture → Approval matrix → Online takedown    │
│  (ordinary) row]                                            │
│                                                             │
│  Automatic escalations that apply here: [list any from      │
│  the practice profile]                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> A takedown notice makes formal representations about copyright ownership and infringement that could be used against you. Have you reviewed this with a solicitor? If not, here's a brief to bring to them: [generate a short summary: work, ownership, accused use, licence check, fair-dealing analysis, signer, platform]. A brief solicitor review now is materially cheaper than a counterclaim later.
>
> To find a solicitor in the UK: SRA register (sra.org.uk). For trade mark and copyright matters, you can also use CITMA (citma.org.uk) for trade mark attorneys with copyright expertise, or the Bar Council's barrister finder for specialist IP barristers.

### Step 7: Output

**Primary:** `<matter-folder>/takedown/<slug>/notice-v<N>.md`. The notice content, ready to submit via the platform's intake form or addressed to its designated contact.

**In-chat:** show the notice as plain text for review before writing. Iterate before committing to disk.

**Reviewer-facing closing note** (in-chat only):

> This is a draft takedown notice for solicitor/attorney review. The representations it contains can be used against you if inaccurate. A solicitor reviews, edits, and takes professional responsibility before submission.

**Post-submission record.** After submission, write `<matter-folder>/takedown/<slug>/submission.md`: platform, intake channel used, date submitted, confirmation ID if returned, URLs targeted, counter-notification watch (platform-dependent, typically 10–14 days), legal hold refreshed.

## Respond mode — triaging a takedown you received

Your content was taken down or you received a notice. You have options.

### Step 1: Read the notice

Extract:

- **Sender** — entity, signer, address, email
- **Platform** — which platform notified you
- **Claimed work** — what they say is theirs
- **Your content alleged to infringe** — URL(s) or identifiers
- **Date of takedown / notice**
- **Regime** — DMCA §512? DSA Art. 16? Platform-specific? UK OSA?
- **Whether the notice appears to meet the applicable regime's requirements on its face** — flag missing elements; a defective notice is a weaker notice

### Step 2: Assess

- **Do we have a licence?** Negotiated, implied, Creative Commons, prior settlement?
- **Is it fair dealing?** Walk the CDPA ss.29–31 permitted acts. Be honest — this is for us.
- **Is the notice defective?** Missing required elements? Signed by someone without apparent authority? Flag any defects.
- **Is the sender a troll?** Repeat pattern of overbroad takedowns?
- **What regime applies?** DMCA counter-notices have specific legal consequences (federal-jurisdiction admission for US disputes). DSA Art. 16 disputes use a different mechanism. Platform-specific counter-notifications vary.

### Step 3: Options

Present 4 options with tradeoffs:

**A — Comply (let the takedown stand)**
- When: they're right, or the fight isn't worth it
- Next step: log, confirm no counter deadline issues

**B — Send a counter-notification / objection**
- When: we have a good-faith belief the material was wrongly removed — use is licensed, is fair dealing, or the claimant doesn't own the right
- **For DMCA-regime disputes (US platforms):** a §512(g)(3) counter-notice consents to federal court jurisdiction in the original sender's district — serious legal step
- **For DSA-regime disputes (EU platforms):** DSA Art. 17 provides for an out-of-court dispute settlement mechanism
- **For platform-specific disputes:** use the platform's counter-notification form
- Next step: `/ip-legal-uk:takedown --counter`

**C — Engage the sender directly**
- When: there's room for a business resolution
- Next step: outreach letter to the sender

**D — Ignore and let it stand**
- When: harm is small, content has a commercial substitute, you'd rather not escalate
- Next step: log the event; note the business decision

Recommend one with two sentences of rationale.

### Step 4: Write triage memo

Output: `<matter-folder>/takedown/inbound/<slug>/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Takedown Notice Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** Structured intake scan. Every authority
> flagged for SME verification; merit calls are counsel's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Platform:** [platform name]
**Regime:** [DMCA / DSA / platform-specific / UK OSA / unclear]

## The notice

**Sender:** [entity, signer, counsel if any]
**Claimed work:** [title, description]
**Our content targeted:** [URLs / identifiers]
**Date of takedown:** [YYYY-MM-DD]
**Notice meets applicable regime requirements on its face:** [yes / no — list any missing elements]

## Assessment

**Licence / authorisation check:** [read]
**Fair dealing analysis (CDPA ss.29–31 permitted acts):** [walk each applicable act; conclusion; `[verify]`]
**Notice defects:** [list or none]
**Platform's notice process compliance:** [were we given notice and opportunity]
**Sender credibility:** [troll / real claimant / repeat takedown pattern]

## Options

### A. Comply
### B. Counter-notification / objection
### C. Engage sender
### D. Ignore

**Recommendation:** [A/B/C/D] — [two sentences why] — `[verify: solicitor/attorney to confirm before executing]`

## Deadlines

- **Counter-notification window:** [platform-dependent — typically 10–14 business days; DMCA §512(g)(2)(C): 10-14 business days from counter-notice; DSA: platform-specific]
- **Any other response deadline:** [from notice or platform terms]

## Immediate actions

- [ ] Legal hold issued on the accused work — [yes/no]
- [ ] Business impact assessed — [yes/no]
- [ ] Matter created — [yes/no/TBD]
- [ ] Counsel assigned — [who]
```

Close with:

> This is a triage memo, not advice. The assessment above is a first read from the four corners of the notice. A solicitor or authorised professional evaluates before you counter-notify or decide not to respond.

## Counter mode — drafting a counter-notification

Counter-notifications put content back up. In the DMCA context, they consent to federal court jurisdiction. In all contexts, they are a formal objection that may escalate to proceedings.

### Step 1: Confirm the predicate

- The content was taken down in response to a copyright notice (not a terms-of-service action by the platform).
- You have a good-faith belief the material was removed by mistake or misidentification — the use is licensed, is fair dealing, or the claimant does not own the right.
- You are aware of the escalation risk: if the original claimant is willing to litigate, a counter-notification may trigger proceedings against you.
- The decision has been made deliberately — with solicitor input where litigation is a real risk.

### Step 2: Draft per applicable regime

**For DMCA-regime disputes (US-established platforms following §512):**

§512(g)(3) elements:
1. Subscriber's physical or electronic signature
2. Identification of the material removed and its location before removal
3. Statement under penalty of perjury of good faith belief that the material was removed by mistake or misidentification
4. Subscriber's name, address, telephone number, and consent to jurisdiction of federal district court and acceptance of service of process

**For DSA Art. 17 disputes (EU-established platforms):**

Use the platform's out-of-court dispute settlement mechanism or the DSA Art. 17 internal complaint mechanism. The DSA does not require a specific perjury statement but requires identification, grounds for the counter-notification, and contact details.

**For platform-specific processes (UK platforms, other non-DMCA):**

Use the platform's counter-notification form. Include identification, identification of the material, grounds for the objection (licenced, fair dealing, claimant doesn't own the right), and contact details for follow-up.

### Step 3: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS COUNTER-NOTIFICATION GOES ANYWHERE             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A counter-notification formally disputes a copyright       │
│  claim. It may escalate to legal proceedings.               │
│                                                             │
│  For DMCA-regime counter-notices: you are consenting to     │
│  federal court jurisdiction in the claimant's district      │
│  and making a statement under penalty of perjury. If the    │
│  claimant sues within 10-14 business days, the content      │
│  stays down pending the suit. 17 U.S.C. §512(g)(2)(C).      │
│                                                             │
│  For any regime: the counter-notification may be used as    │
│  evidence that you knew the material was at issue and        │
│  disputed the takedown — be accurate and in good faith.     │
│                                                             │
│  Confirm before the counter-notification leaves:            │
│                                                             │
│    1. The material was taken down in response to a          │
│       copyright notice (not a TOS action).                  │
│    2. You have a good-faith belief the removal was a        │
│       mistake — because the use is licensed, fair dealing,  │
│       or the claimant doesn't own the right.                │
│    3. You are aware of and have budgeted for the risk of     │
│       proceedings by the claimant.                          │
│    4. A solicitor has reviewed this where litigation is a   │
│       real possibility.                                     │
│                                                             │
│  Approver per your practice profile: [approver — typically  │
│  above the ordinary-takedown approver due to escalation     │
│  risk]                                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer, add the "find-a-solicitor" routing paragraph from send mode.

### Step 4: Output

**Primary:** `<matter-folder>/takedown/<slug>/counter-notice-v<N>.md`.

**Reviewer-facing closing note** (in-chat only):

> This is a draft counter-notification for solicitor review. Sending it may escalate to proceedings. A solicitor reviews before submission.

## Decision posture

When uncertain whether the use is fair dealing, whether the right holder is us, whether the work is actually ours, whether fair dealing defeats the claim — do not silently decide. Flag for solicitor review; surface the factors.

## What this skill does not do

- **Submit the notice.** Drafting only.
- **Decide fair dealing as a matter of law.** Walks the CDPA permitted acts; flags. A solicitor decides whether to proceed.
- **Handle US copyright registration requirements.** UK copyright is automatic; for US matters, copyright registration requirements under 17 USC §411 are handled separately.
- **Bypass the gate.** The gate runs every time in `--send` and `--counter` modes.
- **Handle defamation, malicious falsehood, or data protection notices.** This skill covers copyright takedowns only.
- **Advise on CDPA s.97A blocking injunctions.** That is High Court litigation; route to IP litigation counsel.
