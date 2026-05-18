---
name: vendor-ai-review
description: >
  Review vendor AI terms — agreement, addendum, or ToS AI provisions — against your
  UK governance positions; flag training-on-data, liability, model changes, and AI
  policy consistency. Use when user says "review this AI agreement", "check vendor
  terms", "what did we agree to with [vendor]", "vendor sent an AI addendum", "is
  this AI contract okay", or attaches vendor AI terms.
argument-hint: "[vendor name, or attach the contract]"
---

# /vendor-ai-review

1. Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. Confirm vendor governance positions are populated — if not, stop and direct to setup.
2. Use the framework below.
3. Confirm document type (AI addendum / main agreement AI provisions / ToS). If only an AUP was provided, ask for the full terms.
4. Term-by-term review: training on data, confidentiality of inputs, model changes, output IP, liability, incident notification, human review rights, use restrictions, audit rights.
5. UK data transfer check: if vendor is based outside the UK, check for adequate UK GDPR international transfer mechanism (UK adequacy decisions, UK IDTA, or UK addendum to SCCs).
6. AI addendum gap check if DPA/UK GDPR addendum exists but no AI addendum.
7. AI policy consistency diff vs. `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
8. Output: bottom line, term-by-term, recommended redlines, if-they-won't-move routing.

```
/ai-governance-legal-uk:vendor-ai-review openai-enterprise-agreement.pdf
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ai-governance-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Vendor AI terms are where your governance positions actually get tested. The cold-start interview captures what you *want*. This skill checks what you *agreed to* — and flags the gaps between those two things.

The direction here is always the same: we are the deployer or buyer reviewing the vendor's terms.

What varies is the *input*:
- A standalone AI agreement or AI addendum (most structured)
- A vendor's universal terms of service with AI provisions embedded (often buried)
- An acceptable use policy (tells you what you can't do; says nothing about what the vendor can do with your data or outputs)
- A combination — master agreement + UK GDPR data processing agreement (DPA) + AI addendum (common for serious enterprise AI vendors)

When there's a UK GDPR DPA already in place, this review complements it — it's not a substitute. The DPA governs data protection obligations under UK GDPR; the AI terms govern model-specific rights and risks.

---

## Load the playbook

Read `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` → `## Vendor AI governance`. Also read `## AI policy commitments` — vendor terms can't be consistent with a use restriction our own policy imposes if we've agreed to something different.

If `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` contains `[PLACEHOLDER]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor vendor governance positions to your practice.
>
> **Two choices:**
> - Run `/ai-governance-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll review tailored to YOUR positions.
> - Say **"provisional"** and I'll review against generic defaults — UK jurisdiction, middle risk appetite, solicitor role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]`.

### Provisional mode

If the user says "provisional," run the vendor AI review normally using these generic defaults: middle risk appetite, solicitor role, UK (E&W) jurisdiction, no playbook (flag all common vendor-AI risks from first principles including UK GDPR data transfer and Art. 22 considerations). Tag the reviewer note and every finding block with `[PROVISIONAL]`.

---

## Before reading the document

If the user hasn't shared the actual vendor terms, ask:

> "Can you share the vendor's AI terms? The most useful thing is the actual contract language — the AI addendum if there is one, or the main agreement with AI provisions highlighted. An acceptable use policy alone won't tell us what the vendor can do with our inputs; it only tells us what we're allowed to do."

---

## The term-by-term review

### Core AI-specific terms (check every vendor AI agreement)

Review each term below. For each, extract what the vendor's contract actually says and compare it against the position in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` → `## Vendor AI governance` (standard / acceptable fallback / automatic no).

| Term | What to look for |
|---|---|
| **Training on our data** | Does the vendor use our inputs to train, fine-tune, or improve models? Is there an explicit opt-out or prohibition? Is training opt-in or opt-out by default? |
| **Confidentiality of inputs** | Are our prompts, documents, and data confidential? Any "quality review" or human-review carveouts that would let vendor staff read inputs? |
| **Model changes** | Any notice obligation for material changes to the model? Version pinning available? |
| **Output ownership / IP** | Who owns AI-generated content? Any licence-back to the vendor on outputs? Any IP indemnity? |
| **Liability for outputs** | Does the vendor accept any liability if the AI produces harmful, incorrect, or infringing outputs? Cap structure? Carve-outs? |
| **Incident notification** | How and when are we notified if the AI system fails, is compromised, or produces systematic errors affecting us? |
| **Human review rights** | Can we require human review of outputs in specific cases? Can we appeal or dispute an AI decision? |
| **Use restrictions** | What are we prohibited from doing? Any definitional terms (e.g., "automated decision-making") that could sweep in our intended uses? |
| **Audit / auditability** | SOC 2, third-party audits, bias testing results — any audit rights? |
| **Subprocessors / model providers** | Does the vendor use sub-vendors for the model? Are they disclosed? Whose terms govern? |
| **Data residency** | Where is our data processed? Where does it go for inference? Is it outside the UK? |
| **UK GDPR data transfer** | If vendor is based outside the UK (including US vendors), what is the transfer mechanism? UK adequacy decision? UK IDTA? UK addendum to EU SCCs? Nothing? — a missing transfer mechanism is a UK GDPR violation. `[model knowledge — verify current list of UK adequacy decisions and IDTA status]` |
| **Term and termination** | What happens to our data when we terminate? Deletion timelines? |
| **Stacked-vendor accountability** | Is this vendor the model provider, or are they a deployer of someone else's model (e.g., a SaaS wrapper of Claude, GPT, or Gemini) or a reseller of infrastructure-hosted foundation models (Claude-on-Bedrock, OpenAI-on-Azure)? If the latter: there are TWO vendors' terms in play. Identify (a) whose terms govern training on inputs, retention, and safety, (b) who is contractually liable for model behaviour, and (c) whether each upstream commitment is flowed down to you. Do not review the two contracts in isolation. |

If `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` doesn't define a position for a term on this list, ask: "Your playbook doesn't cover [term]. What's your default position, your acceptable fallback, and your automatic no? I'll add it to `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md` so the next review is consistent."

---

## UK data transfer check

This is a UK-specific obligation that sits alongside the AI terms review.

**If the vendor is based outside the UK (including in the US, EU/EEA, or elsewhere):**

> "This vendor is based in [jurisdiction], outside the UK. Transferring personal data to them requires a lawful UK transfer mechanism under UK GDPR Chapter V and DPA 2018. The available mechanisms are:
>
> 1. **UK adequacy decision** — the ICO has published the list of countries the UK recognises as adequate. Check current list. `[model knowledge — verify against current ICO adequacy decisions list]`
> 2. **UK IDTA (International Data Transfer Agreement)** — the ICO's standard contractual clauses for international transfers from the UK. A UK IDTA must be incorporated into or attached to the main agreement.
> 3. **UK addendum to EU SCCs** — if the vendor already has EU SCCs in place, a UK addendum (ICO template) can extend them to cover UK transfers.
> 4. **Binding Corporate Rules (BCRs)** — for intra-group transfers within multinationals; must be approved by the ICO.
>
> **What I found in this agreement:** [describe what if anything covers UK transfers]
>
> **Gap:** [None — transfer mechanism present / Partial — SCC present but no UK addendum / Full — no transfer mechanism at all]"

A missing UK transfer mechanism is a 🔴 Critical finding regardless of the AI terms review outcome.

---

## Playbook comparison

For each term above, compare what we found to the positions in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

**Output format for each term:**

> **[Term name]**
> 🟢 / 🟡 / 🟠 / 🔴
> **Vendor says:** [summary of what the contract actually says]
> **Our position:** [from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`]
> **Gap:** [specific delta — or "Aligned"]
> **Proposed fix:** [specific redline language, or "escalate — outside fallback"]

Use the severity ratings consistently:

- 🟢 **Aligned** — at or better than the standard position in the playbook.
- 🟡 **Note** — within fallback but worse than standard; flag for awareness, not a blocker.
- 🟠 **Significant** — outside standard position but within fallback; needs redline before signing.
- 🔴 **Critical** — outside fallback; deployment should not proceed without resolution. Escalate per `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

---

## AI addendum gap check

**If the vendor has a UK GDPR DPA but no AI addendum:**

> "There's a UK GDPR DPA in place but no AI-specific addendum. The DPA covers data protection obligations but doesn't address: training on our data, model change notification, liability for AI outputs, or incident notification for AI system failures.
>
> For a [Standard / Elevated / High] tier use case, this gap is [acceptable at Standard tier / a blocker at Elevated or High tier]. Recommend requesting an AI addendum or at minimum negotiating AI-specific terms into the next renewal."

**If there are no AI terms at all:**

> "There are no AI-specific terms in this agreement. The vendor is providing an AI-powered service under general service terms — which means we have no contractual protection on the highest-risk AI governance items (training, liability, model changes). This is a 🔴 for any Elevated or High tier use case."

---

## AI policy consistency check

Cross-check the vendor's terms against our AI policy commitments in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.

Common conflicts:
- Our policy prohibits vendor training on our data — the vendor's terms permit it by default.
- Our policy requires human review for certain use cases — vendor's terms say AI outputs are final.
- Our approved vendor list doesn't include this vendor — or blocklist does.
- Our policy requires disclosure to affected parties — vendor's terms impose a confidentiality obligation on AI system capabilities that would prevent disclosure.

Flag every mismatch. One of them has to change.

---

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Surgical redlines signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase.
- Replace a **phrase** before a sentence.
- Restructure a **subclause** before replacing the sentence.
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft.

When in doubt, smaller.

## Output

**Before recommending signature of a vendor AI agreement:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Signing this vendor AI agreement has legal consequences. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the vendor and the use case, the key terms reviewed, where vendor positions diverge from policy, what's being accepted, what could go wrong, what to ask the solicitor.]
>
> If you need to find a solicitor or barrister: sra.org.uk (SRA), barcouncil.org.uk (Bar Council) for England & Wales; lawscot.org.uk (Law Society of Scotland); lawsoc-ni.org (Law Society of Northern Ireland).

Do not proceed past this gate without an explicit yes.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

*This review is derived from vendor contract terms that are typically confidential under NDA, and it may itself be privileged. It inherits the source's confidentiality and privilege status. Distributing it beyond the privilege circle (e.g., forwarding to the vendor, sharing in an open channel) can waive privilege and breach the NDA. Mark, store, and route accordingly.*

# Vendor AI Review: [Vendor Name]

**Document reviewed:** [AI addendum / main agreement AI provisions / ToS]
**Reviewed:** [date]
**Use case(s):** [what we're deploying this vendor's AI for]
**Governance tier:** [Standard / Elevated / High]
**Vendor jurisdiction:** [where vendor is incorporated / based]

---

## Bottom line

[Two sentences. Can we deploy under these terms? What has to change first?]

**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

---

## UK data transfer status

[✓ Covered — [mechanism] / 🔴 Not covered — transfer mechanism missing / 🟠 Partial — [what's needed]]

---

## Term-by-term

[For each term above — vendor position, our position, gap, severity, proposed fix]

---

## AI addendum status

[Present / Absent — and what that means for this deployment]

---

## AI policy consistency

[🟢 Consistent | 🟡 Flags: list]

---

## Recommended redlines

[Consolidated draft redlines. Review with solicitor before sending externally.]

---

## If they won't move

[For each 🔴 and 🟠: the fallback from `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`, or "escalate — outside fallback" and routing per escalation table]
```

---

## Practical notes

**The training-on-data clause is the one most people miss.**
Do not assume any particular vendor's current stance without reading the specific agreement in front of you.

**Map the AI stack.** Modern AI deployments are layered. Before reviewing terms, map the layers:
1. **End-user SaaS application** — the tool your org signs up for
2. **API gateway / orchestration layer** (e.g., Azure OpenAI Service, AWS Bedrock, Google Vertex) — often invisible, always has its own terms
3. **Model provider** (e.g., Anthropic, OpenAI, Google, Meta) — the LLM
4. **Hosted knowledge base / RAG source** — the data Claude reads from
5. **Additional subprocessors** — analytics, logging, fine-tuning partners

Ask: "Walk me through the stack — what does [SaaS tool] use under the hood?" Then review terms at EACH layer, not just the top.

**Flow-down test.** For each flagged stacked-vendor term — especially training-on-data, data retention, subprocessor changes, and liability — DO THE CHECK:

1. **Search the contract for flow-down language.** Look for: "subprocessor obligations no less protective than," "back-to-back terms," "equivalent obligations."
2. **If present:** Quote it, verify it covers the specific flagged term, and flag whether it's enforceable.
3. **If absent:** Produce a specific redline requiring it.
4. **Flag the gap with a severity.**

**UK data transfer reminder.** Every time a vendor is non-UK, the UK data transfer check is mandatory — it's not optional even if the rest of the AI terms look fine.

**Renewals are leverage points.** If the current agreement is unfavourable and the vendor won't renegotiate mid-term, document the gaps now and flag them for the renewal.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.

## What this skill does not do

- It doesn't review the UK GDPR DPA provisions of the same agreement — run `/privacy-legal-uk:dpa-review`, if the plugin is installed, for that.
- It doesn't decide whether to accept terms outside the fallbacks. It routes those per the escalation table.
- It doesn't evaluate vendor security posture beyond what's in the agreement.
