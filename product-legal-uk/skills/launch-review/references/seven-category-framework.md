# UK Eight-Category Launch Review Framework

Default framework if the team doesn't have their own. Adapted from UK product-legal practice. Each category has a key question and an auto-skip condition.

The categories are stable framing concepts. What counts as "Needs work" vs. "Blocker" *within* a category depends on the applicable UK jurisdictions, sector regimes, and the company's own calibration in `~/.claude/plugins/config/uk-legal-plugins/product-legal-uk/CLAUDE.md`. Research the UK regulatory regimes applicable to the product's sector, audience, and jurisdictions before concluding that a specific fact pattern is or isn't a problem.

**Commencement note.** UK legislation may be enacted but not yet in force. Always check commencement provisions on legislation.gov.uk — particularly for recent statutes such as the Digital Markets, Competition and Consumers Act 2024 and the Online Safety Act 2023, where provisions are being commenced in tranches. Model training knowledge may not reflect the current commencement position.

## 1. Contractual commitments

**Key question:** Does this conflict with any customer-facing promise?

Check: Terms and Conditions, SLA commitments, marketing materials, customer contracts (especially enterprise MSAs with custom terms), published documentation.

**Auto-skip if:** No customer-facing changes — internal tool, infra, or change invisible to users.

**Common findings:**
- New feature contradicts a T&C restriction
- SLA implications of a new dependency
- Feature marketed as "included" moving to a paid tier
- Digital content terms under *Consumer Rights Act 2015*, Pt 1, Ch 3 `[CRA-2015-S]` — implied terms of satisfactory quality, fitness for purpose, and conformity with description apply to digital content sold to consumers

## 2. Privacy / UK GDPR

**Key question:** New data collection, new purpose, or new sharing? DPIA trigger under UK GDPR Art 35?

Check: What data is touched, whether it's new or existing, whether the purpose is covered by the current privacy notice, whether any new third party (as controller or processor) sees it. The UK GDPR `[UK-GDPR-ART]` + DPA 2018 impose obligations on lawful basis, purpose limitation, data minimisation, transparency, and security. Check whether a Data Protection Impact Assessment (DPIA) is required (mandatory for systematic processing likely to result in high risk to individuals — UK GDPR Art 35).

**Auto-skip if:** No data changes — pure UI, pure infra without new logging.

**DPIA mandatory triggers (UK ICO guidance):**
- Systematic and extensive profiling with significant effects on individuals
- Large-scale processing of special category data or criminal conviction data
- Systematic monitoring of publicly accessible areas on a large scale
- New technologies or novel uses of existing technologies
- Processing involving children or other vulnerable individuals
- Use of biometric or genetic data to uniquely identify individuals

## 3. Security

**Key question:** New attack surface?

Check: new endpoints, new data at rest, new access paths, new auth requirements. Also check *Network and Information Systems (NIS) Regulations 2018* if the product is a relevant digital service or critical national infrastructure.

**Auto-skip if:** UI-only change, no backend. (But check that it really is UI-only — "UI change" that adds a new API call is not.)

**Not legal's call alone** — loop security team. Legal's role is ensuring the security review happened and any findings are addressed. Note: ICO guidance requires "appropriate technical and organisational measures" under UK GDPR Art 32.

## 4. IP

**Key question:** Any third-party code, content, or potentially infringing output?

Check: new open-source dependencies (licence compatibility — some copyleft licences create obligations inconsistent with a proprietary product; research the specific licence under UK copyright law); third-party content (stock images, fonts, datasets); features that output content that could infringe (AI generation, user uploads displayed publicly).

**Auto-skip if:** No new dependencies, no content generation, no user uploads.

**Common findings:**
- Copyleft licence in a new dependency
- Training data provenance unclear — check whether UK copyright exceptions (e.g., text and data mining exception under CDPA 1988 s 29A) apply
- User-generated content without a notice-and-takedown process — research the applicable safe harbour under the *Electronic Commerce (EC Directive) Regulations 2002* (still in UK law post-Brexit) and the *Online Safety Act 2023* `[OSA-2023-S]`

## 5. Third-party interactions

**Key question:** New vendor, partner, or integration?

Check: is there a contract, is there a data processing agreement under UK GDPR Art 28 if personal data flows, is the third party's failure our problem (uptime, security, DPA breach).

**Auto-skip if:** No new external parties.

**Common findings:**
- New processor without a UK GDPR Art 28 data processing agreement
- Integration partner with different data practices — check sub-processor obligations
- API dependency without SLA

## 6. Regulatory / sector-specific (UK)

**Key question:** Does this touch a UK-regulated sector, audience, or jurisdiction?

Research the UK regulatory regimes applicable to the product's sector, audience, and jurisdictions. Also consider accessibility (Public Sector Bodies Accessibility Regulations 2018; EN 301 549 standard) and export-control regimes (Export Control Order 2008 / dual-use goods and software regulations) where relevant.

**Auto-skip if:** Same users, same sectors, same jurisdictions as the existing product — nothing new in regulatory scope.

**Common findings:**
- Expansion into a UK-regulated sector without the supporting infrastructure (contracts, controls, disclosures, authorisations) the regime requires
- Feature that could be used by a UK-regulated audience (e.g., children under the Children's Code, patients under MHRA, retail investors under FCA Consumer Duty) without the protections the applicable regime requires
- Expansion into a new UK nation (Scotland, Northern Ireland) with different applicable law
- Expansion outside the UK into an EEA jurisdiction — UK regulatory frameworks do not apply; EEA / EU law applies

**CMA enforcement note.** The *Digital Markets, Competition and Consumers Act 2024* `[DMCC-ACT-2024]` gives the CMA significantly strengthened enforcement powers. The DMCC Act's consumer protection provisions — subscription traps, drip pricing, fake reviews — are now active CMA enforcement priorities. Check commencement orders for current in-force status.

## 7. Marketing claims (ASA / CAP Code)

**Key question:** Any claims that need CAP Code substantiation? Any financial promotions needing FCA s 21 approval?

See the marketing-claims-review skill. The ASA / CAP Code `[CAP-CODE]` is the primary UK mechanism for advertising substantiation. The CPR 2008 `[CPR-2008-REG]` applies to misleading and aggressive commercial practices more broadly.

**Financial promotions special case.** Any communication that constitutes an invitation or inducement to engage in investment activity must be approved by an FCA-authorised person under FSMA 2000 s 21 `[FSMA-2000-S]` before it is communicated. This is a criminal offence if ignored. If *any* financial promotion is in scope, flag immediately — this is a Blocking finding.

**Green claims.** Environmental and sustainability claims must comply with the CMA Green Claims Code (2021) — substantiation with clear, accurate, relevant, and verifiable evidence is required. Vague or unsubstantiated green claims can constitute misleading commercial practices under the CPR 2008.

**Auto-skip if:** No marketing component — silent launch, internal feature, flag flip.

## 8. AI governance

**Key question:** Does this use AI in any form? Is the use case in the registry? Is a DPIA done for automated decisions? Have vendor AI terms been reviewed?

Check: third-party models, internally built models, AI-powered vendor features, automated scoring or classification, generative content, recommendations, predictions. Research the applicable UK AI governance regimes for the use case type:

- **UK GDPR Art 22** `[UK-GDPR-ART]` — automated individual decision-making (including profiling) with significant effects: individuals have rights; restrictions on solely automated decisions. Verify whether the feature constitutes Art 22 processing and whether an exemption applies.
- **Equality Act 2010** — AI-assisted decisions in hiring, credit, insurance, or access to services must not result in direct or indirect discrimination on protected characteristics.
- **ICO guidance on AI and data protection** — transparency (Art 13/14/15), fairness, and explainability requirements for AI systems processing personal data.
- **EU AI Act (for EEA users)** — if the product serves EEA users, check whether the system constitutes a prohibited practice, high-risk AI system, or general-purpose AI model under the EU AI Act. The EU AI Act does not apply in the UK, but affects UK companies with EEA market presence.
- **AI vendor terms** — does the vendor's terms permit training on inputs? Verify data processing agreement, sub-processor obligations, and confidentiality protections.

**Auto-skip if:** No AI component detected.

**Common findings:**
- Use case not in the AI registry
- Vendor AI terms permit training on customer inputs — flag for review of UK GDPR purpose limitation and customer-facing privacy notice
- Automated decision-making without a human-in-the-loop design where Art 22 safeguards may apply
- No explainability / challenge mechanism for AI-generated decisions affecting individuals
