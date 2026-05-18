# UK Privacy Currency Watch

**Last verified: 2026-05-18.**

> **⚠️ Staleness check.** If the last-verified date above is more than 90 days old, treat this file as stale and verify each entry before relying on it. A stale watch list is worse than no watch list — it looks current while being wrong. When a skill reads this file, check the last-verified date first. If stale, say: "The currency watch was last verified [date] — [N] months ago. I'm using it as a checklist of areas to search, not as a source of current status." When you update any entry, also update the last-verified date at the top.

UK data protection law moves. Post-Brexit UK/EU divergence is an active and compounding source of change. Before relying on an effective date, threshold, or obligation, verify it. These are the areas most likely to have moved since model training:

---

## UK GDPR / DPA 2018 — legislative reform

- **Data (Use and Access) Act.** The UK Government introduced the Data (Use and Access) Bill as a successor to the previous DPDI Bill. Track its progress and Royal Assent status — it amends the UK GDPR and DPA 2018 in several areas including recognised legitimate interests, automated decision-making provisions, and the role of the ICO. Verify current status at [Parliament Bills tracker](https://bills.parliament.uk). `[model knowledge — verify]`
- **UK GDPR Art.22 (automated decision-making) reform proposals** may affect triage and DPIA requirements for AI/profiling use cases. Verify enacted status before advising on ADM. `[model knowledge — verify]`
- Verify at [legislation.gov.uk](https://www.legislation.gov.uk) for current text and amendments.

---

## ICO enforcement and penalty levels

- Penalty ceilings: £17.5m or 4% of global annual turnover (higher of the two) for UK GDPR; £8.7m or 2% for other DPA 2018 breaches. Verify current thresholds — secondary legislation can adjust figures. `[model knowledge — verify]`
- ICO enforcement notices and penalty notices: monitor the ICO's [enforcement decisions page](https://ico.org.uk/action-weve-taken/enforcement/). Recent enforcement signals current ICO priorities. Before any DPIA or gap analysis, check whether the relevant sector or processing type has attracted recent ICO enforcement.
- ICO investigation into AI/generative AI: the ICO has made AI a priority enforcement and guidance area. DPIAs for AI processing should reflect current ICO AI guidance. `[ICO-GUIDANCE]`

---

## PECR (Privacy and Electronic Communications Regulations 2003)

- **PECR reform.** The UK Government has consulted on replacing PECR (which implemented the EU ePrivacy Directive) with updated UK legislation. A PECR reform bill has been signalled. Track progress — enacted PECR reform would change cookie consent rules, direct marketing obligations, and traffic data rules materially. Verify current status before advising on any cookies, email/SMS marketing, or electronic communications matter. `[model knowledge — verify]`
- **Current PECR position:** Cookies still require prior informed consent for non-essential cookies (PECR Reg.6 + ICO guidance). Soft opt-in for email/SMS marketing to existing customers still applies (PECR Reg.22(3)). These positions may change on enacted reform.
- Verify at [legislation.gov.uk SI 2003/2426](https://www.legislation.gov.uk/uksi/2003/2426) and the ICO's [direct marketing guidance](https://ico.org.uk/for-organisations/direct-marketing/).

---

## International transfers

- **UK-US Data Bridge.** In force since 18 October 2023 as an adequacy decision for transfers to certified US organisations. The Data Bridge is the UK equivalent of the EU-US Data Privacy Framework. Verify it remains in force — it is subject to review and potential challenge. Verify at the ICO and DCMS/DBT. `[model knowledge — verify]`
- **UK adequacy decisions.** The UK's list of adequate countries differs from the EU's — verify the current UK list before advising on any transfer to a specific country. UK adequacy includes EU/EEA, but additions and revocations can occur. Check [ICO international transfers guidance](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/international-transfers/). `[model knowledge — verify]`
- **IDTA (International Data Transfer Agreement).** The UK's primary post-Brexit transfer mechanism for non-adequate-country transfers (equivalent to EU SCCs). Issued and updated by the ICO. Verify the current IDTA version and its addenda. Previous versions may expire. Verify at [ICO IDTA page](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/international-transfers-after-uk-exit/international-data-transfer-agreement-and-uk-addendum/).
- **UK Addendum to EU SCCs.** Parties using EU SCCs for UK-originating transfers must also execute the UK Addendum (issued by ICO under the International Data Transfer Agreement). Verify whether the version in any existing DPA is current.
- **EU SCC adequacy for UK/EU cross-channel transfers.** Where a transfer involves both UK and EU data subjects, EU SCCs (2021 version) govern the EU side; IDTA or UK Addendum governs the UK side. These are not the same document — a DPA that only includes EU SCCs does not cover UK-originating transfers.

---

## ICO Age Appropriate Design Code (Children's Code)

- The Children's Code (DPA 2018 s.123) is in force and the ICO is actively enforcing it. High-profile enforcement actions have been brought against major platforms. Any online service that is "likely to be accessed by children" must assess compliance.
- ICO announced reviews and audits of services in sectors including gaming, social media, and EdTech. Verify the ICO's current enforcement priorities and whether the relevant service sector is under active review. `[ICO-GUIDANCE]`
- The 15 standards include age-appropriate default settings, best-interests principle, nudge techniques prohibition, and data minimisation. Verify current ICO guidance for the applicable service type.

---

## Online Safety Act 2023

- In force from January 2024 (with staged obligations). Ofcom is the primary regulator, but OSA duties overlap with ICO-regulated data/privacy obligations for in-scope services (illegal content duty, child safety duty, transparency obligations).
- Services regulated under the OSA should assess whether OSA-driven data processing (e.g., age assurance, content moderation signals) requires a DPIA and triggers PECR/UK GDPR obligations. `[model knowledge — verify]`
- Verify current Ofcom implementation timeline and codes of practice at [ofcom.org.uk/online-safety](https://www.ofcom.org.uk/online-safety).

---

## DSAR response timelines and exemptions

- UK GDPR Art.12(3): 1 calendar month from receipt. Extension: up to 2 further months for complex or numerous requests, with notice within month 1. **No fee for standard requests.**
- DPA 2018 Schedule 2: exemptions include legal professional privilege, management forecasts and plans, negotiations, confidential references, examination scripts, and others. Verify the current Schedule 2 text for any exemption relied upon — the DPA 2018 has been amended.
- ICO guidance on manifestly unfounded or excessive requests is evolving. Verify current ICO position before refusing or charging for a DSAR.
- Verify at [legislation.gov.uk/ukpga/2018/12](https://www.legislation.gov.uk/ukpga/2018/12).

---

## NIS Regulations 2018

- Network and Information Systems Regulations 2018 (SI 2018/506) apply to operators of essential services (energy, transport, water, health, digital infrastructure) and digital service providers (online marketplaces, online search engines, cloud computing services). Verify whether the regulated entity falls within scope.
- NIS2 applies to EU entities but not UK ones post-Brexit. The UK has its own NIS reform proposals — verify enacted status. `[model knowledge — verify]`
- Verify at [legislation.gov.uk/uksi/2018/506](https://www.legislation.gov.uk/uksi/2018/506) and NCSC/DSIT guidance.

---

## ICO guidance updates

The ICO regularly publishes new and updated guidance. High-priority areas to re-check before advising:

- **AI and generative AI guidance** (significant ICO activity in 2024-2026) — lawful basis for AI training, purpose compatibility, legitimate interests for AI, DPIA triggers for AI
- **Biometric data guidance** — special category data under UK GDPR Art.9; ICO has published sector-specific guidance
- **Employment data guidance** — monitoring at work, legitimate interests for employment processing
- **Data sharing code** (published under DPA 2018) — verify current version
- **Direct marketing guidance** — reflects current PECR and UK GDPR positions

Check at [ico.org.uk/for-organisations](https://ico.org.uk/for-organisations/) for current guidance.

---

## How to use this file

When a skill cites a UK data-protection rule, effective date, or threshold, it should note: "UK data-protection law is moving — this may have changed since model training. Verify at the ICO website or legislation.gov.uk. See `references/currency-watch.md`."

**This file goes stale.** Current as of May 2026. Update when you notice drift.
