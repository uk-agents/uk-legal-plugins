---
name: ip-clause-review
description: >
  Review the IP clauses in an agreement — assignment, ownership, licence
  grants, warranties, indemnities. Use when reviewing IP terms in employment,
  consulting, SOW, vendor, or licensing agreements, when asked to check the
  assignment language or licence scope, or when an agreement with IP provisions
  is pasted or attached. UK assignment formalities under CDPA 1988 s.90, TMA
  1994 s.24, and PA 1977 s.30 are load-bearing.
argument-hint: "[file path | Drive link | paste text]"
---

# /ip-clause-review

Reviews the IP clauses in an agreement against the practice profile in `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. Flags assignment gaps, ownership ambiguity, licence-scope issues, and IP warranty/indemnity problems. Produces a memo with per-clause findings, prioritised by risk, with suggested redline language where appropriate.

## Instructions

1. **Load `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`.** If placeholders present, stop and prompt: "Run `/ip-legal-uk:cold-start-interview` first — I need to learn your practice profile before I can review IP clauses against it."

2. **Get the agreement:** From file path, Drive link, or pasted text. If none provided, ask.

3. **Follow the workflow below.** In particular:
   - Establish the agreement type and which side the company is on for IP.
   - Run the assignment gap check first if the agreement is an employment, consulting, SOW, or services contract.
   - Apply UK assignment formality rules — CDPA 1988 s.90 (copyright assignment must be in writing signed by or on behalf of the assignor), TMA 1994 s.24 (trade mark assignment must be in writing signed by or on behalf of the assignor), PA 1977 s.30 (patent assignment must be in writing signed by both parties unless made by personal representatives). These are not technicalities — an assignment that fails the formality requirement is ineffective and can wreck M&A diligence.
   - Check moral rights under CDPA 1988 ss.77–89 where relevant.
   - Produce per-clause findings prioritised by risk.
   - Check cross-clause consistency.
   - Note jurisdiction implications (moral rights, employed works, UK formalities, post-Brexit considerations).

4. **Output the memo** per the template below — work-product header first, bottom line, assignment gap check, clauses by severity, consistency flags, jurisdiction note, approval routing.

5. **Respect the decision posture.** When a clause could be read to allocate IP either way, flag for attorney review and surface the factors cutting both ways. Never silently decide a subjective allocation question.

## Examples

```
/ip-legal-uk:ip-clause-review ~/Documents/vendor-sow.pdf
/ip-legal-uk:ip-clause-review https://docs.google.com/document/d/...
/ip-legal-uk:ip-clause-review
```

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is
`✗` (the default for in-house users), skip — skills use practice-level context.
If enabled and there is no active matter, ask: "Which matter is this for? Run
`/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

---

## Purpose

Read the IP clauses in an agreement and tell the solicitor/attorney what each one does, how it deviates from market or from the team's standard position, what the risk is, and — where appropriate — the specific redline to propose.

**The highest-stakes clauses in most agreements are IP ownership and assignment.** A failure to get a clean, formally valid assignment on an employment or consulting agreement surfaces in M&A diligence, in financing, and in litigation, sometimes years after the agreement was signed. If assignment language is weak, missing, or fails the UK statutory formality requirements, flag it loudly at the top of the memo.

**UK formality rules are strict and jurisdiction-specific:**

- **CDPA 1988 s.90(3):** An assignment of copyright (including future copyright) must be in writing signed by or on behalf of the assignor. An oral assignment is ineffective. A "beneficial assignment" without s.90 compliance creates an equitable assignment at most, which is not the same thing and will not satisfy standard M&A reps.
- **TMA 1994 s.24(3):** A registered trade mark assignment must be in writing signed by or on behalf of the assignor.
- **PA 1977 s.30(6):** A patent assignment must be in writing signed by the parties (note: both parties must sign, unlike copyright). An agreement to assign a patent is also enforceable in equity but does not vest legal title.
- **Design rights:** UK registered designs (RDA 1949) — no explicit statutory formality requirement, but written assignment is standard and required for recordal at the UK IPO. UK unregistered design right (CDPA 1988 s.222): written assignment, signed by or on behalf of the assignor.

## Precondition: load the practice profile

**Before reading the agreement, read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`.** It tells you:

- The jurisdiction footprint — which affects formality requirements, moral rights waivers, employed-works defaults, and the post-Brexit split between UK and EU IP rights
- Who approves deviations and at what severity
- The work-product header to prepend

## Workflow

### Step 1: Orient

Read the whole agreement once, fast. Answer:

| Question | Answer |
|---|---|
| What kind of agreement is this? | Employment / consulting or SOW / vendor MSA / in-licence / out-licence / collaboration or JDA / settlement / acquisition or asset purchase / other |
| Which side are we on for IP? | Granting rights or receiving them / assigning IP or acquiring it / licensor or licensee |
| Who is the counterparty? | Name, and sophistication |
| Is there consideration flowing for the IP specifically? | Salary, fee, royalty, upfront payment, equity, none |
| Governing law and venue | What does it say? |

The side question is per-document. If the side is ambiguous, ask:

> Which side is [company] on for this agreement's IP? Granting rights, receiving rights, or both?

### Step 2: Assignment gap check (highest priority)

If the agreement is an employment agreement, consulting agreement, SOW, or services contract where the company should be receiving an assignment of the counterparty's IP in work product — check the assignment language first.

Look for:

- **Formal validity.** Does the assignment clause satisfy UK statutory formality? For copyright (CDPA s.90): written, signed by or on behalf of the assignor. For patents (PA 1977 s.30): written, signed by both parties. For trade marks (TMA s.24): written, signed by or on behalf of the assignor. If the assignment is in an unsigned email, a verbal agreement, or a clause that says "assigns" without meeting the formality, flag it 🔴 immediately — it is legally ineffective.
- **Present-tense assignment vs. agreement to assign.** "Hereby assigns" vests title immediately. "Agrees to assign" is a contractual promise — equitable interest only until a formal assignment deed is executed. For M&A and financing, the difference matters materially.
- **Employed works default (CDPA 1988 s.11(2)).** For employees: the employer is the first owner of copyright in works made in the course of employment. No written assignment is needed for the employment relationship to vest ownership, but the scope of "course of employment" is often disputed. Flagging what is and is not within the course of employment is important.
- **Scope.** Does the assignment cover all IP created in the course of the engagement, or only IP related to the company's business? Narrow scope is a gap.
- **Moral rights waiver.** UK law recognises moral rights under CDPA 1988 ss.77–89 — the right of paternity (s.77), the right of integrity (s.80), and the right to object to false attribution (s.84). Moral rights apply to literary, dramatic, musical, and artistic works (but NOT to computer programs, typefaces, or computer-generated works — s.79(2)(a)). They can be waived (CDPA s.87) but not assigned — waiver must be in writing, signed by the rights holder, and should be express and unconditional.
- **Further assurances** clause — counterparty agrees to sign whatever else is needed to perfect the assignment later.
- **Pre-existing IP carveout** — what does the counterparty exclude from the assignment, and is the list specific or open-ended?

If any of the above is missing or weak, flag at the top of the memo:

```markdown
## ⚠️ ASSIGNMENT GAP

**Section [X]** assigns IP in the work product, but: [specific issue — e.g.,
"clause says 'shall assign' rather than 'hereby assigns' — this is an
agreement to assign, not an effective assignment. Under CDPA 1988 s.90(3)
copyright must be assigned by instrument in writing signed by the assignor.
A future signature is needed to vest title."]

**Risk:** This is the kind of gap that surfaces in M&A diligence years later.

**Proposed redline:**
> "[specific replacement language]"

**Escalation:** Per `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`,
assignment-scope gaps escalate to [approver].
```

> **Can the assignment convey AI-assisted content?** The UK Intellectual Property Office has issued guidance on AI and copyright. Currently, for computer-generated works (where there is no human author), CDPA 1988 s.9(3) vests copyright in the person who makes the arrangements necessary for the work to be created — typically the company or employer. For AI-assisted works where there is a human author who exercises creative judgment, normal copyright rules apply. Nonetheless, if the contractor uses AI tools for substantial portions of the deliverables:
>
> - Check: does the agreement have an AI-use disclosure obligation? A representation about the role of AI?
> - If absent and AI-assisted creation is foreseeable: flag as 🟠 High and suggest adding an AI-use representation.

> **AI-assisted inventorship in patents.** UK law currently requires a human inventor (PA 1977 s.7; *Thaler v Comptroller-General* [2023] UKSC 49 confirmed the UKIPO's position). An AI system cannot be named as an inventor. If AI tools contributed to the inventive concept, inventorship is complicated. Flag for any agreement with patent assignment provisions covering potentially patentable work product.

### Step 3: Clause-by-clause review

For every IP-relevant clause, produce a block. Clauses to look for:

- **Assignment / employed works** — who owns what's created under the agreement
- **Ownership of deliverables** — distinct from assignment
- **Improvements and derivatives** — who owns improvements to pre-existing IP
- **Background IP vs. foreground IP** — pre-existing IP and newly-created IP
- **Licence grants** — scope, exclusivity, territory, field of use, sublicensability, term, termination triggers
- **IP warranties** — non-infringement, authority to grant, original work, no encumbrances
- **IP indemnities** — scope, cap, procedure, exclusions
- **Moral rights waiver** — must be express, in writing, signed; note scope (CDPA s.87)
- **Open source representations** — what OSS is or is not embedded in deliverables
- **Trade mark use** — any grant or restriction; quality control requirements for licensor
- **Confidentiality / trade secrets** — treatment under English law of confidence / Trade Secrets Regulations 2018, post-term obligations, return or destruction

For each clause present, produce:

```markdown
### [Section X.X]: [Clause name]

**What it says:** [plain-English summary]

**What's market (for this agreement type, this side, this jurisdiction):**
[brief reference point]

**Risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

**Why it matters:** [one or two sentences]

**Proposed redline (if needed):**
> "[specific replacement language]"

**Decision call:** [if uncertain, flag for attorney review]
```

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Don't sign without fixing. Assignment clause fails UK formality (CDPA s.90 / TMA s.24 / PA s.30). Unlimited licence where a narrow one was intended. Exclusive grant where non-exclusive was intended. |
| 🟠 High | Strongly push; escalate if they won't move. Ambiguous scope, missing moral rights waiver in a work for which it matters, missing further assurances, narrow indemnity. |
| 🟡 Medium | Push in first round; accept if it's the last open item. Imprecise language, survival periods shorter than standard. |
| 🟢 Low | Note it, don't spend capital. Stylistic deviation that doesn't change the allocation. |

### Step 4: Cross-clause consistency

IP clauses fail as a system. Check:

- **Does the licence grant match the scope of what's being licensed?**
- **Do the warranties cover everything the grant covers?**
- **Does the indemnity cover what the warranty promises?**
- **Does termination pull the licence back?** Or does a paid-up licence survive? Either is defensible — check intent.
- **Is the IP allocation between this agreement and any related SOW, order form, or side letter consistent?**

### Step 5: Jurisdiction note

Flag if the agreement implicates any of these:

- **UK employed-works rule (CDPA s.11(2)):** employer is first owner of copyright in works made in the course of employment. Independent contractors/freelancers OWN their copyright unless it is expressly assigned. This is a key UK/US divergence — the US work-for-hire doctrine (17 USC §101) automatically covers certain categories of commissioned works; UK law does not.
- **Moral rights (CDPA ss.77–89):** UK moral rights apply to literary, dramatic, musical, and artistic works (but not computer programs or computer-generated works). They can only be waived in writing, not assigned. Check whether the moral rights waiver in the agreement is sufficient in scope.
- **UK assignment formalities:** as above — CDPA s.90(3), TMA s.24(3), PA 1977 s.30(6). If any clause purports to assign IP without meeting the formality, it is legally ineffective.
- **Post-Brexit IP split:** if the agreement relates to trade marks or patents with both UK and EU coverage, ensure the assignment or licence explicitly covers both UK and EU registrations separately. A licence or assignment of "all trade marks" may not automatically cover both UK and EU marks now that they are separate registrations.
- **Governing law:** if the agreement is governed by non-UK law, the UK statutory assignment formality rules may not apply in the same way. Flag and route to local counsel for the relevant jurisdiction.

State what jurisdiction the agreement is governed by, and whether the practice profile flags that jurisdiction as standard, escalate, or never.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artefact, not a rewrite. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position. Only replace a whole clause when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and say so in the transmittal.

### Step 6: Assemble the memo

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` → `## Outputs`.

This memo and the underlying agreement may be privileged, confidential, or both. Distribute only within the privilege circle; strip the work-product header before any external delivery.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a rule the memo needs, report what was found and stop. A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag citations: `[uk-legal MCP]`, `[legislation.gov.uk]`, `[govuk MCP]`, `[user provided]`, `[web search — verify]`, `[model knowledge — verify]`. Never strip tags.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# IP Clause Review: [Counterparty] [Agreement Type]

**Reviewed:** [date]
**Our side for IP:** [Granting / Receiving / Both]
**Governing law:** [jurisdiction]

---

## Bottom line

[Two sentences. Can the IP allocation stand? What has to change first?]

**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name, per practice profile]

---

## Assignment gap check

[✅ Clear | ⚠️ Gap present — see above]

---

## Clauses by severity

[All clause blocks from Step 3, grouped Critical → Low]

---

## Cross-clause consistency

[Flags from Step 4]

---

## Jurisdiction note

[Flags from Step 5 — UK formalities, employed works, moral rights, post-Brexit split]

---

## Approval routing

[From practice profile — who approves, what triggers automatic escalation]
```

## Decision posture

When a clause could be read to allocate IP either way, or when it is unclear whether the drafter's chosen words achieve the stated intent, **flag it for attorney review and surface the factors cutting both ways**. An unresolved IP allocation that gets signed is a one-way door.

## Quality checks before delivering

- [ ] Practice profile was loaded and the jurisdiction note reflects what's there
- [ ] UK assignment formality checked for every assignment clause (CDPA s.90 / TMA s.24 / PA s.30)
- [ ] Assignment gap checked first (for employment/consulting/SOW/services)
- [ ] Employed-works default noted where applicable (CDPA s.11(2))
- [ ] Moral rights waiver noted and assessed (CDPA ss.77–89)
- [ ] Post-Brexit UK/EU IP split flagged if relevant
- [ ] Every 🔴 and 🟠 issue has specific replacement language
- [ ] Cross-clause consistency checked, not just clause-by-clause
- [ ] Source tags applied; no stripped `verify` tags
- [ ] Approver named per practice profile
- [ ] Output marked with the work-product header

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.
