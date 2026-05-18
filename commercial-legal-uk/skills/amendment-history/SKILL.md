---
name: amendment-history
description: >
  Trace how a contract has changed across its base agreement and all amendments —
  either a summary of all changes over time, or a provision trace for a specific
  clause. Use when the user says "what changed in this contract over time", "show
  me the amendment history", "where's the latest [clause]", "how has [provision]
  evolved", or uploads multiple versions of an agreement.
argument-hint: "[file(s) | [CLM ID (coming soon)] | [repository link (coming soon)]] [--provision <clause name>]"
---

# /amendment-history

Loads a base agreement and all amendments, then either summarises what
changed over time or traces a specific provision to its current
controlling language.

## Instructions

1. **Get the documents:** From file upload, CLM ID (coming soon), or repository link (coming soon). Accept multiple files in one invocation. If none provided, ask.

2. **Detect the mode** by parsing the request per the mode detection rules below. If a provision name is clearly stated, go straight to Mode 2. If no provision is mentioned, run Mode 1. Ask only if genuinely ambiguous.

3. **Run the workflow below.** Follow it fully.

4. **Offer follow-ups after output:**
   - "Want me to trace another provision?"
   - "Want a full playbook review of the current agreement as amended?" (routes to vendor-agreement-review)
   - "Want a stakeholder summary of the key changes?" (routes to stakeholder-summary)

## Examples

```
/commercial-legal-uk:amendment-history acme-msa.pdf amendment-1.pdf amendment-2.pdf
```

```
/commercial-legal-uk:amendment-history --provision indemnity
```

```
/commercial-legal-uk:amendment-history
[paste agreement and amendment text]
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Contracts accumulate amendments. By the third amendment, nobody remembers what the original said or which version of a clause controls. This skill reads the base agreement and all amendments in chronological order and either summarises what changed across the whole contract or traces a specific provision through every version to find the current controlling language.

## Mode detection

Parse the user's request to determine which mode to run. Do not ask which mode unless the request is genuinely ambiguous.

**Mode 1 — Summary** (no specific provision mentioned)
Trigger phrases: "what changed", "amendment history", "show me changes over time", "summarise amendments", "what does this contract look like now"

**Mode 2 — Provision trace** (specific clause or topic named)
Trigger phrases: "where's the [clause]", "latest [provision]", "how did [term] change", "find the indemnity", "what does it say now about [topic]"

Common provision mappings:
- "indemnity" / "indemnification" → indemnification section
- "liability" / "liability cap" → limitation of liability (note UCTA 1977 reasonableness context)
- "termination" → term and termination
- "data" / "privacy" / "DPA" / "UK GDPR" → data protection provisions
- "IP" / "intellectual property" → IP ownership and licences
- "price" / "fees" / "payment" → payment terms (note Late Payment of Commercial Debts Act 1998 context)
- "auto-renewal" / "renewal" → renewal mechanics
- "governing law" / "jurisdiction" → governing law and jurisdiction clauses (note: post-Brexit enforcement considerations)
- "competition" / "non-compete" / "exclusivity" → competition and restrictive covenant provisions

If the term is ambiguous and maps to more than one provision, list the candidates and ask which one.

---

## Step 1: Load and order the documents

Accept documents from any of these sources:

**CLM integration (coming soon)** — if connected, search by counterparty name or agreement title. Pull the base agreement and all amendments.

**Document repository integration (coming soon)** — search by counterparty name or filename. Look for files matching patterns like "Amendment", "Addendum", "Variation", "Side Letter", "Amendment No. 1", numbered suffixes.

**Direct upload:** User provides files directly. Order is usually self-explanatory from document titles (e.g., "Amendment No. 1", "Second Amendment", "Addendum A", "Deed of Variation") or dates visible in the filename or document header.

Only ask the user to confirm ordering if:
- Filenames give no indication of sequence
- Dates are absent from both filenames and document headers
- Two documents appear to be the same amendment version

**Ordering rules:**
- Always establish chronological order before reading content.
- Amendments often reference the agreement they modify ("This Amendment to the Master Services Agreement dated [X]") — use these references to confirm the chain.
- **UK-specific:** Look for "Deed of Variation" (used for formal contractual variations in English law, particularly where consideration needs to be evidenced), "Side Letter", or "Letter of Variation" as well as "Amendment".

---

## Privilege inheritance

This skill reads the base agreement and amendments — often subject to legal professional privilege or confidentiality. The output inherits the source's privilege and confidentiality status. Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` `## Outputs` to every output below, distribute only within the privilege circle, and store it where privileged materials live. Strip the header before any external delivery.

## Step 2: Read and index

Read each document in chronological order. For each, extract:
- Document type (base agreement, amendment number, deed of variation, addendum, side letter, etc.)
- Execution date
- Parties (confirm they match across documents — flag if a new party was added or a party name changed; note: formal assignment under English law (LPA 1925 s.136) requires written notice to the debtor)
- A list of provisions explicitly modified, added, or deleted

Build a working index before producing output.

---

## Mode 1: Summary of all changes

### Section reference rule

Every finding must include an inline section reference so the reader can verify against the source document without searching.

### Output format

```markdown
# Amendment History: [Counterparty] — [Agreement type]

**Base agreement:** [date]
**Amendments:** [N] ([date of first] → [date of last])
**Last amended:** [date]
**Governing law:** [English law / Scots law / NI law / other]

---

## What changed — chronological

### Amendment 1 — [date]
**Document type:** [Amendment / Deed of Variation / Addendum / Side Letter]
**Purpose:** [one sentence — why this amendment existed, from recitals or clear from context. If not stated, omit rather than guess.]

**Material changes:**
- [Provision] (§[X.X]): [what it said before → what it says now, in plain English]
- [New provision added] (§[X.X]): [what it does]
- [Provision deleted] (§[X.X]): [what was removed and why it matters]

### Amendment 2 — [date]
[same structure]

[repeat for each amendment]

---

## Net current state

| Provision | Current position | §Ref | Last changed |
|---|---|---|---|
| [clause] | [plain English summary] | §[X.X] | Amendment N, [date] |
| [clause] | [unchanged from base] | §[X.X] | Base agreement |

---

## Watch items
[Flag anything that looks inconsistent — e.g., an amendment modifying a provision that was already deleted, contradictory language between amendments, a party name that changed without a formal assignment notice (LPA 1925 s.136), a provision where the section number shifted across documents, a Deed of Variation that may require evidence of consideration, a TUPE-related change in a services agreement.]
```

---

## Mode 2: Provision trace

### Output format

Show only what changed. Do not list amendments where the provision was untouched — skip them entirely.

```markdown
# Provision Trace: [Provision name]
## [Counterparty] — [Agreement type]
**Governing law:** [English law / Scots law / NI law / other]

---

### Original — [Base agreement date], §[X.X]
> "[exact quote]"

*Plain English:* [one sentence]

---

### Amendment [N] — [date], §[X.X]

**Was:**
> "[exact quote of prior language]"

**Now:**
> "[exact quote of replacement language]"

*What changed:* [one sentence — practical effect on the parties]

---

[Only subsequent amendments that touched this provision appear here. All others are omitted.]

---

## Current controlling language

**§[X.X] — [source document, date]**
> "[exact quote]"

*Plain English:* [one sentence]

---

## Watch items
[Flags, inconsistencies, open questions — with section references. Common items: whether the provision is subject to or carved out of the liability cap (UCTA 1977 reasonableness context for carveouts); whether the section number shifted across amendments; whether the amendment language conflicts with another provision; whether a Deed of Variation was used correctly (signed as a deed if no consideration).]
```

If the provision was never amended after the base agreement:
> "This provision has not been modified by any amendment. Original language controls. §[X.X], base agreement, [date]."

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.

## What this skill does not do

- It does not determine which document controls in the event of a conflict between the base agreement and an amendment — that is a legal interpretation question. It flags conflicts and routes to Legal.
- It does not draft new amendments or deeds of variation.
- It does not compare against the playbook in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` — that is the vendor-agreement-review skill's job. This skill is purely historical.
- It does not infer what an amendment means if the language is ambiguous — it quotes exactly and flags ambiguity for Legal.
- It does not advise on whether a Deed of Variation requires consideration under English law — it flags the structure and routes to Legal.
