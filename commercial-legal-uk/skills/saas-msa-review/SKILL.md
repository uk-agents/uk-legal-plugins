---
name: saas-msa-review
description: >
  Reference: review of SaaS subscription agreements under English contract law with
  attention to the terms that matter most in subscription deals — auto-renewal
  mechanics, price escalation, data portability, uptime SLAs, UK GDPR sub-processor
  rights, and UCTA 1977 reasonableness. Loaded by /commercial-legal-uk:review when
  a SaaS or subscription agreement is detected.
user-invocable: false
---

# SaaS / Subscription Agreement Review (UK)

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

SaaS agreements have a distinct risk profile from one-time vendor contracts. The pounds compound over renewals, the data accumulates, and the switching cost grows every month. This skill reviews with that in mind.

It runs the standard playbook check from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` and adds a SaaS-specific overlay on the terms that bite hardest in subscription deals.

## UK Legal Framework

This skill applies **English contract law** as the default. Where the contract's governing law is Scots law or NI law, it notes applicable differences.

Key UK-specific SaaS considerations:
- **Auto-renewal:** No general UK statute specifically regulating B2B auto-renewal (unlike some US states). English law allows auto-renewal if clear — but consider Consumer Rights Act 2015 if any B2C element; CMA guidance on subscription traps for consumers. `[model knowledge — verify]`
- **Price escalation:** No statutory cap in B2B SaaS — market practice. CPI/RPI-linked escalators are common. Check basis (CPI vs. RPI — RPI typically runs higher). `[model knowledge — verify]`
- **Data portability:** UK GDPR Article 20 gives individuals a data portability right (not a business right). Contractual portability clauses are what protect the business on exit. `[model knowledge — verify]`
- **UCTA 1977:** Service credits as sole remedy for SLA breach — check reasonableness if this purports to exclude liability for negligence causing other loss. `[model knowledge — verify]`
- **UK GDPR / DPA 2018:** Sub-processor regime, Article 28 clauses, IDTA / UK Addendum for international transfers, 72-hour breach notification. `[model knowledge — verify]`

## Jurisdiction assumption

SaaS terms are sensitive to governing law. Key UK considerations:
- **Auto-renewal / subscription traps:** CMA has enforcement powers under Enterprise Act 2002 against unfair commercial practices — active enforcement in consumer subscriptions. B2B SaaS less regulated but CMA surveillance increasing. `[model knowledge — verify]`
- **Data-portability mandates:** UK GDPR Article 20 (individual right) is not a business portability right — contractual exit rights are what matter.
- **Liability exclusions:** UCTA 1977 reasonableness applies to B2B standard terms. Consumer Rights Act 2015 applies to any B2C element.
- **International transfers:** Post-Brexit, EEA/EU transfers require IDTA or UK Addendum to EU SCCs. Transfers to US, other third countries: assess adequacy or rely on IDTA. `[model knowledge — verify]`

> **No silent supplement.** If a research query to uk-legal MCP, BAILII, or legislation.gov.uk returns few or no results for a statutory override that might bear on the deal, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking.
>
> **Source attribution.** Tag citations: `[uk-legal MCP]`, `[legislation.gov.uk]`, `[BAILII]`, `[govuk MCP]`, `[statute / regulator site]`, `[web search — verify]`, `[model knowledge — verify]`, or `[user provided]`.

## Load the playbook

**Which side?** Before applying the playbook, determine which side the company is on. Usually obvious: if the counterparty is a SaaS vendor selling you their platform, you're purchasing-side. If you are the SaaS vendor and the counterparty is your customer, you're sales-side. If not obvious, ask. Read the matching playbook section. If the matching side is `[Not configured]`, stop and tell the user to run `/commercial-legal-uk:cold-start-interview --side <side>`.

Read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` first. The general playbook for the matching side (liability, indemnity, termination, governing law, UCTA, UK GDPR) applies fully — run all the standard checks from the vendor-agreement-review skill.

Then look for a `## Playbook` → matching side → `SaaS positions` section. That's where the team records its positions on auto-renewal notice windows, acceptable price escalators, data export rights, SLA thresholds, sub-processor approval rights, and deprecation notice.

If `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` doesn't address a SaaS-specific term, ask and record the answer.

## SaaS-specific overlay

For each category below, list what you found in the contract and compare to the team's position.

### 1. Auto-renewal mechanics

The single most common way a SaaS deal goes wrong: nobody notices the renewal notice window and we're locked in for another year at a higher price.

Check each element against the team's `SaaS positions`:

- **Renewal term length** (e.g., same as initial, longer, multi-year auto-convert)
- **Notice-to-cancel window** (number of days before renewal)
- **Notice method** (email, written notice, portal-only — note: portal-only notice requirements may be harder to evidence; consider requesting confirmation email or registered post for high-value agreements)
- **Price on renewal** (same, CPI-capped, RPI-capped, then-current list, uncapped discretionary)

**Business-day roll-back.** Notice periods ending on a weekend or UK bank holiday (E&W or Scotland as applicable) should roll to the prior business day. Note in the renewal register.

**Extract and record** the exact renewal date and the notice window regardless of whether any item is flagged. This feeds the renewal-tracker skill.

### 2. Price escalation

Check each element against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`:

- **Annual escalator** (fixed %, CPI, RPI — note RPI typically runs higher than CPI, uncapped, etc.)
- **Usage overage pricing** (published rate card, premium rate, unspecified)
- **Scope of "fees"** (subscription only vs. "additional services" broadly defined)

**CPI vs. RPI note:** UK Consumer Prices Index (CPI) and Retail Prices Index (RPI) are both commonly used; RPI has typically run higher. ONS has deprecated RPI for new uses. Check which index and whether there's a cap on annual increase. `[model knowledge — verify]`

### 3. Data portability and exit

When (not if) we leave this vendor, can we get our data out? Check each element:

- **Export format** (open/standard, proprietary-but-documented, "commercially reasonable")
- **Export availability** (self-serve anytime, on request during term, only at termination)
- **Post-termination access** (days available to export after termination)
- **Export cost** (free, T&M, per-GB or per-record)
- **Deletion certification** (certified on request, none, vendor retains derivatives)

**UK GDPR note:** UK GDPR Article 17 (right to erasure) applies to personal data. The contract should provide for deletion/return of personal data on termination per UK GDPR Article 28(3)(g). `[model knowledge — verify]`

Vendor retention of "anonymised" or "aggregated" derivatives — confirm the team's stance and check the anonymisation standard (GDPR Recital 26 / ICO anonymisation guidance). `[model knowledge — verify]`

### 4. Uptime and SLA

Only matters if the business actually depends on this service being up. If it's a nice-to-have tool, skip this section.

Check each element:

- **Uptime commitment** (percentage, or "commercially reasonable efforts")
- **Measurement period** (monthly, quarterly, annual)
- **Remedy** (service credits — how calculated, whether capped, whether sole remedy)
- **Scheduled maintenance exclusions** (defined window, advance notice, unlimited)
- **Credit-as-sole-remedy interaction with the liability cap**

**UCTA 1977 note:** If service credits are the sole remedy for SLA breach (including for negligence causing loss beyond the credits), this is an exclusion clause in standard B2B terms — assess reasonableness under UCTA 1977 s.3 and s.2(2). `[model knowledge — verify]`

### 5. Sub-processors (UK GDPR)

This is a data protection issue but it's SaaS-specific because the sub-processor list *changes* over the life of the subscription.

Check each element against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` and UK GDPR Article 28:

- **Current list** (published, on request, unavailable)
- **Change notification** (advance notice period — UK GDPR requires controller to be informed of sub-processor changes and given opportunity to object, Art.28(2))
- **Objection rights** (blocking, notice-and-terminate, notice-only)
- **International sub-processors** — do they require IDTA or UK Addendum? `[model knowledge — verify]`

Missing sub-processor regime: flag 🔴 Critical (UK GDPR Article 28 compliance).

### 6. Service changes and deprecation

SaaS vendors change their product. Usually fine. Sometimes they deprecate the thing you bought.

Check each element:

- **Material adverse changes** (right to terminate on material degradation, notice-only, unrestricted)
- **Deprecation notice period** for features the team relies on
- **Feature parity on replacement** (same price tier, higher tier)

## AI and machine learning rights (UK-specific)

**AI/ML data rights decision procedure.** Seven dimensions — apply with UK regulatory lens:

1. **Explicit grant.** Does the contract explicitly grant the vendor rights to use Customer Data for AI training or ML development?
2. **Implicit grant via policy.** Does the contract incorporate the vendor's privacy policy or terms of service by reference? Can the vendor add training rights via a unilateral policy update?
3. **Anonymisation standard.** What's the standard? "Anonymised" without a definition is weak. Does it meet GDPR Recital 26 / ICO anonymisation guidance / HIPAA Safe Harbor (for US sub-processors)? `[model knowledge — verify]`
4. **Competitive contamination.** Does the vendor serve your competitors? Is there a competitive isolation commitment?
5. **Opt-out scope and durability.** Does the opt-out cover all AI uses and survive renewals and TOS updates?
6. **Output ownership.** Who owns the outputs? Can the vendor use your outputs as training examples? Check third-party AI sub-processors (OpenAI, Anthropic, Google, etc.) — their sub-processor obligations must be mapped.
7. **Downstream regulatory chain.** Does the vendor's use of your data for AI create regulatory exposure for YOU? **UK-specific:** ICO guidance on AI and data protection; AI Safety Institute; sector-specific AI rules (FCA, MHRA, etc.). `[model knowledge — verify]`

Match each to a playbook position. If the agreement is silent on all seven: "The agreement is silent on AI/ML training rights — request an explicit prohibition or a defined carve-out tied to each of the seven dimensions above."

## Liability cap decision procedure

**The cap amount is the least important part of the cap.** Work through:

1. **Direct vs. indirect/consequential damages.** State both treatments explicitly. Note UCTA 1977 reasonableness context for B2B standard terms.

2. **The cap base — quote it verbatim.** "12-month cap" could mean fees paid, fees payable, fees under current order, etc. If ambiguous, flag it.

3. **Cap-carveout interaction.** Enumerate what sits ABOVE the cap (carveouts), what sits BELOW. Common UK SaaS carveouts: wilful misconduct, gross negligence, fraud, death/personal injury (void to exclude — UCTA s.2(1)), IP indemnity, data breach, confidentiality breach.

4. **Your playbook position per dimension.** Check against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.

## Jurisdiction delta check

**Check the SaaS contract's actual governing law against the top divergences:**

- **Governing law is Scots law:** Note where Scots law differs; recommend Scotland-qualified solicitor for finalisation.
- **Governing law is foreign (EU, US, etc.):** Rome I (retained) governs choice of law validity. Post-Brexit English court judgments may not be automatically enforced in EU Member States.
- **UCTA 1977 / Consumer Rights Act 2015:** Liability exclusions in B2B standard terms must satisfy UCTA reasonableness regardless of choice-of-law clause if there is a connection to England & Wales. `[model knowledge — verify]`
- **Non-solicits:** Enforceable if reasonable under English restraint of trade doctrine. `[model knowledge — verify]`
- **Confidentiality term:** Enforceable perpetually for trade secrets; courts may limit ordinary confidential information. `[model knowledge — verify]`

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artefact, not a rewrite. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

## Output

Use the vendor-agreement-review memo structure, with a SaaS-specific section added after the standard playbook checks. The vendor-agreement-review memo already carries the privilege header.

**Dual severity.** Every SaaS-specific finding carries both axes (see CLAUDE.md `## Dual severity`):
- **Legal risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
- **Business friction:** 🔴 Blocks deals | 🟠 Slows deals | 🟡 Confuses customers | 🟢 Invisible

```markdown
### Bottom line

[Can you sign / Need to fight for X first / Walk — one-sentence why]

### AI and machine learning rights

[Flag: explicit ML training clauses, policy-incorporation grants, anonymisation standard, competitive contamination, opt-out scope, output ownership, UK regulatory chain (ICO, sector regulators). If silent: "Silent on AI/ML training rights — request explicit prohibition or defined carve-out."]

## SaaS-specific findings

### Auto-renewal
**Renewal date:** [date]
**Notice window:** Cancel by [date] ([N] days before renewal) — business-day adjusted for [E&W / Scotland] bank holidays
**Renewal price mechanism:** [as written — note CPI/RPI basis]
**Playbook fit:** [within position / deviation / not addressed]
**Flag for renewal-tracker:** [yes — and the record the tracker needs]

### Price escalation
[findings against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` positions — note CPI vs. RPI]

### Data exit
[findings — this is the one the business owner should read; note UK GDPR Art.17/28 deletion obligations]

### SLA / UCTA check
[findings, or "Skipped — service is not business-critical per [stakeholder]"; note UCTA reasonableness for sole-remedy clauses]

### UK GDPR Sub-processors
[findings against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` positions; Art.28 compliance; IDTA for international sub-processors]

### Service changes
[findings against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` positions]
```

## Handoffs

**To renewal-tracker:** When you find the renewal date and notice window, hand them off. The renewal-tracker register expects the following fields (see `skills/renewal-tracker/references/renewal-register.yaml` for the full schema). Note `notice_method` and `transit_buffer_days` carefully — UK registered post typically adds 2-3 days; allow for weekends and bank holidays.

**To escalation-flagger:** If any of the SaaS-specific checks hits the team's "never accept" or escalation-trigger list in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`, the escalation-flagger skill routes it — including any CMA, FCA, or ICO triggers.

## A note on what to fight over

SaaS vendors, especially large ones, negotiate their paper reluctantly. Pick battles *per the team's playbook* — the `SaaS positions` section should distinguish between terms the team will always push on, terms it fights over only for material deals, and terms it lets slide. Calibrate based on contract value and switching cost.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.
