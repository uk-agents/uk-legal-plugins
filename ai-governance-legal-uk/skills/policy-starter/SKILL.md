---
name: policy-starter
description: >
  Draft a UK AI usage policy from published UK model policies, adapted to your
  practice profile — a research-and-synthesis tool whose output is a draft for
  solicitor review and adoption, not a finished policy. Sources from Law Society
  AI guidance, ICO AI guidance, SRA risk outlook, sector regulator guidance, and
  peer policies. Use when user says "draft an AI policy", "we need an AI policy",
  "build an AI usage policy", "our firm needs a GenAI policy", or similar requests
  to generate a first-cut internal AI policy.
argument-hint: "[optional — scope hint, e.g. 'firm-wide', 'legal team only', 'update existing']"
---

# /policy-starter

1. Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If the practice profile is unpopulated, stop and direct to `/ai-governance-legal-uk:cold-start-interview`.
2. Use the framework below.
3. Run the scope interview — which sections does the policy need to cover, who's the audience, what's the deployment context. Do not skip to drafting.
4. Web search for the current published UK model policies and guidance relevant to the deployment context (Law Society AI guidance, ICO AI guidance, SRA risk outlook, Bar Council guidance, sector regulator guidance, peer-firm / peer-company policies, EU AI Act Art. 4 AI literacy requirements if EU nexus).
5. Draft the selected sections, sourced from the UK model policies, with `[review]` flags on every choice point and `[review]` open questions at the bottom of each section.
6. Output with the draft header ("DRAFT FOR INTERNAL LEGAL REVIEW — NOT FOR DISTRIBUTION"), the sources block, the reviewer note, and the adoption checklist.
7. Close with the next-steps decision tree.

```
/ai-governance-legal-uk:policy-starter
/ai-governance-legal-uk:policy-starter "we need an AI policy for our 30-solicitor firm"
/ai-governance-legal-uk:policy-starter "update our existing policy for ICO AI guidance"
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ai-governance-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A lot of UK firms and in-house teams don't have a written AI usage policy yet, or are running on one that doesn't mention the ICO AI guidance, the FCA model risk requirements, the Online Safety Act obligations, or what they actually ended up doing with Microsoft Copilot and Claude for Work. This skill produces a **draft** policy to bring to the decision-maker — GC, managing partner, executive committee, board, head of IT, head of HR — not a finished policy to circulate.

The discipline of this skill:

1. **Source from published UK model policies, not from invention.** Search for and read the Law Society AI guidance, SRA risk outlook, ICO AI guidance, Bar Council guidance, sector regulator publications, and peer-firm / peer-company policies that are public. Cite what each source says and adapt it — don't generate policy language out of thin air.
2. **Decision-tree the scope before drafting.** A policy that tries to cover everything covers nothing. Ask the user what sections the policy needs. Let them pick. Then build each picked section with `[review]` flags on every choice point.
3. **Flag every judgment call.** The output is a draft the solicitor reviews and adopts; every threshold, every named tool, every disclosure trigger, every enforcement consequence is a `[review]` line.
4. **Header signals the scope of the audience.** This output may be read beyond legal — by HR, IT, all staff. The header is adapted accordingly.

This skill does NOT finalise, distribute, publish, or even recommend a specific position on the hard calls. It produces a draft and surfaces the choices.

## Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` first

Before drafting, always read the practice profile. The sections that drive the draft:

- `## Company profile` — AI role (Builder / Deployer / Both), regulatory footprint, external commitments, practice setting, UK nations, EU nexus
- `## Use case registry` — what's already approved, conditional, or a red line
- `## AI policy commitments` — what a prior or current policy already says
- `## Vendor AI governance` — what the team already requires from vendors
- `## Governance team and escalation` — who approves, who escalates
- `## Who's using this` — Role (solicitor/barrister vs. non-lawyer) governs the header

If `## AI policy commitments` is populated, this is an UPDATE, not a new draft — treat the existing policy as the base and propose changes. If it's empty, this is a first-cut draft.

## Scope interview (do this BEFORE drafting)

Ask the user which sections the policy should cover.

> **What should the AI policy cover? Pick the sections you want in the draft:**
> 1. **Scope** — who the policy applies to (all staff, certain roles, contractors), what tools it covers (GenAI only, all AI, specific vendors), what data is in/out of scope.
> 2. **Permitted and prohibited uses** — the approved categories, the red lines, the "ask first" cases. Including UK GDPR Art. 22 automated decision-making controls.
> 3. **Approval and review** — who approves a new tool, who approves a new use case, how the review request is filed, what the SLA is.
> 4. **Disclosure** — to clients (for firms — SRA obligations apply), to courts, to counterparties, to employees, to end users of an AI feature.
> 5. **Data handling** — what confidential/client/privileged data can go where, UK GDPR compliance, vendor data transfer mechanisms (UK IDTA for non-UK vendors), vendor retention terms, training-on-data posture.
> 6. **Training and certification** — who has to take training, on what cadence, consequences for non-completion.
> 7. **Incidents and reporting** — what counts as an AI incident, how to report, who handles. ICO reporting obligations for personal data incidents.
> 8. **Enforcement** — what happens when the policy is violated, link to disciplinary framework.
> 9. **Review cadence and ownership** — how often the policy gets updated, who owns updates, how changes are communicated. ICO best practice to review when AI use changes materially.
> 10. **Glossary** — defined terms (GenAI, approved tool, high-risk use, consequential decision, confidential data, solely automated decision, significant effects, etc.).
>
> Default starter pack for a firm / in-house legal team that's never had a policy: 1, 2, 3, 4, 5, 9. Skip the rest for v1.

After the user picks, ask the second question:

> **Two more inputs before I draft:**
> - **Audience** — who's reading this? (All staff / legal team only / solicitors plus staff / client-facing version also needed) This drives tone and the glossary.
> - **Deployment context** — (a) UK law firm, (b) in-house legal at a UK company (policy covers legal or company-wide?), (c) legal aid / clinic, (d) UK public sector body. This drives which UK model policies I search.

## Source the UK model policies

Before drafting, run web searches for the most recent published UK model AI policies and guidance.

**Derive the model policy sources from the practice profile's `## Regulatory footprint`.** UK-first; global sources where EU nexus applies.

| Jurisdiction | Model policy sources |
|---|---|
| **UK (E&W)** | Law Society AI guidance (published 2023, check for updates), SRA risk outlook on AI, Bar Council AI guidance, ILTA model policy (UK-relevant sections), ICO AI guidance (ico.org.uk/for-organisations/ai-and-data-protection), DSIT AI governance framework, sector regulator guidance (FCA, Ofcom, MHRA as applicable), peer firm published AI policies |
| **Scotland** | Law Society of Scotland AI guidance, Scottish Government AI strategy (if public sector) |
| **Northern Ireland** | Law Society of Northern Ireland guidance, Departmental guidance if public sector |
| **EU/international (if EU nexus)** | EU AI Act Art. 4 AI literacy obligation, EDPB AI guidelines, national DPA AI guidance. Note: EU AI Act is not UK law — but if company has EU nexus, Art. 4 AI literacy requirements apply to that activity. |
| **Financial services** | FCA AI feedback statement, PRA SS1/23 model risk management |
| **Health** | MHRA AIaMD guidance, NHS AI deployment guidance, NICE evidence standards |

For each source the draft uses, **record it in a "Sources" block at the top of the output** with: name, URL, date accessed, and what the draft took from it.

If a web search can't be run, note in the reviewer note: "Could not run web search — draft sourced from training knowledge alone, verify against current versions of the cited sources before adopting."

## The draft

Output follows a consistent structure. **Every choice point gets a `[review]` flag.**

### Header

```
DRAFT FOR INTERNAL LEGAL REVIEW — NOT FOR DISTRIBUTION
Prepared for: [firm / company name from practice profile]
Date: [today's date]
Prepared by: ai-governance-legal-uk policy-starter skill, adapted from published UK model policies
Not for adoption, distribution, posting, or reliance until reviewed, adapted, and approved by [solicitor / GC / managing partner / executive committee per the governance team section of the practice profile].
```

When the Role in `## Who's using this` is Non-lawyer: add a second line under the header — "If you are not a solicitor, barrister, or other authorised legal professional, bring this draft to your legal contact ([name from practice profile]) before using any of it. This is a starting draft for their review, not a policy you can adopt."

### Sources block (at the top, under the header)

A table of the UK model policies / guidance / regulations the draft drew from:

| Source | URL | Accessed | What the draft took from it |
|---|---|---|---|
| Law Society AI guidance | [url] | [date] | Competence and supervision framing |
| SRA risk outlook | [url] | [date] | Disclosure to clients, supervision |
| ICO AI guidance | ico.org.uk | [date] | Data handling, Art. 22 controls |
| Bar Council AI guidance | [url] | [date] | Barristers' competence framing |
| [peer firm] published AI policy | [url] | [date] | Scope language |
| FCA AI feedback statement | [url] | [date] | Financial services AI governance |
| EU AI Act, Art. 4 | [url] | [date] | AI literacy obligations (if EU nexus) |

### Executive summary

Three paragraphs max. What the policy does, who it binds, what the reader has to do before it takes effect.

### The sections

Only the sections the user picked, in the order above. For each:

- A **header and scope** sentence.
- The **substantive rules**, adapted from the cited UK model policies. Every specific threshold, number, named tool, named vendor, or escalation contact is `[review]`. Example: "Confidential client data may not be entered into [general-purpose consumer AI tools] `[review — list tools, or reference the approved-tools list]`. Use of such data in [approved firm-licensed tools] `[review — list tools]` is permitted subject to the data handling section."
- **Source attribution** inline where a rule is adapted from a specific UK source. Example: "Solicitors must verify the accuracy of all AI-generated work product before using it in representation of a client `[Law Society AI guidance]`."
- **Open questions** at the bottom of each section — 2-3 decisions the solicitor needs to make before the section is ready.

**For the data handling section (Section 5):** Include a sub-section on UK GDPR Art. 22 automated decision-making controls if the company uses AI to make or significantly influence decisions about individuals. Example placeholder: "Where [company] uses AI systems to make or significantly influence decisions with legal or similarly significant effects on individuals, the following controls apply: [review — human-in-the-loop requirement / explicit consent mechanism / meaningful information obligation / right to contest]. These controls are required under UK GDPR Article 22 `[settled — UK GDPR Art. 22 as retained EU law; verify Data (Use and Access) Act 2025 amendments]`."

**For the disclosure section (Section 4) for UK law firms:** The SRA requires solicitors to be competent and to supervise AI-generated work. The Law Society has published guidance on AI and disclosure. Flag: "Disclosure obligations to clients: [review — Law Society guidance recommends transparency about AI use; confirm whether firm will disclose proactively or on request; confirm whether client consent is required for specific use cases]."

### Adoption checklist

At the end of the draft:

- [ ] Review by GC / managing partner / head of legal `[review — name]`
- [ ] Review by IT / security (data handling section) `[review — name]`
- [ ] Review by HR (enforcement / training sections) `[review — name]`
- [ ] DPO review (data handling, Art. 22 controls) `[review — name or confirm DPO role]`
- [ ] Board / executive committee approval (if required) `[review — confirm whether required]`
- [ ] SRA / Law Society compliance check (for UK law firms) `[review]`
- [ ] Training materials drafted
- [ ] Announcement drafted
- [ ] Effective date set `[review]`
- [ ] Review cadence calendared `[review — annual or on material change to AI use, per ICO best practice]`
- [ ] Add policy to the `## AI policy commitments` section of the practice profile once adopted

### Reviewer note

The standard reviewer note above the header, per the `## Outputs` section of the practice profile.

> **⚠️ Reviewer note**
> - **Sources:** web search ✓ / not connected — cites from training knowledge
> - **Read:** practice profile · [N] published UK model policies
> - **Flagged for your judgment:** [N] `[review]` items inline · [N] open questions per section
> - **Currency:** searched for developments since [date]
> - **Before relying:** this is a DRAFT — bring to [approver from practice profile], don't distribute until adopted

## Don'ts

- **Don't invent policy language.** Every substantive rule in the draft must be traceable to a cited UK source or flagged `[review — adapted, no direct UK source]`.
- **Don't pick the hard calls for the solicitor.** "Should paralegals be permitted to use AI for first-draft work?" is a `[review]`, not a recommended position.
- **Don't produce a finished-looking policy.**
- **Don't skip the scope interview.**
- **Don't generate section content the user didn't ask for.**
- **Don't recommend a specific vendor, tool, or consequence.**
- **Don't promise legal sufficiency.**
- **Don't apply non-UK law as UK law.** The EU AI Act does not apply as UK domestic law. If it's relevant (EU nexus), cite it correctly and note it applies to that specific activity, not as general UK law.

## Handoffs

After the draft is produced, close with the decision tree from the practice profile. The most common next steps:

1. **Tune the draft** — the solicitor walks through the `[review]` flags and resolves them; the skill re-runs with the decisions baked in.
2. **Stakeholder summary** — produce a one-page version for the board or executive committee.
3. **Training materials** — once the policy is adopted, `/ai-governance-legal-uk:aia-generation` can be used to produce per-use-case training notes.
4. **Vendor sweep** — once the policy is adopted, `/ai-governance-legal-uk:vendor-ai-review` should be run against the vendors the policy references.
5. **Gap check against new UK regulation** — pair with `/ai-governance-legal-uk:reg-gap-analysis` to test the draft against a specific ICO guidance update, FCA publication, or Ofcom code before adoption.

## Output scope reminder

The document this skill produces reaches HR, IT, and the broader business — not just legal. Keep the language plain enough for non-lawyers to follow. The legal precision is in the `[review]` flags and the UK sources, not in jargon.
