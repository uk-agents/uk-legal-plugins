# UK Privacy & Data Protection Plugin

In-house and private-practice UK data-protection workflows under UK GDPR and the Data Protection Act 2018: DPIA generation following the ICO template, DPA review (Art.28 processor obligations, IDTA/UK Addendum for international transfers), DSAR response within the 1-month statutory deadline, lawful-basis and Children's Code triage, PECR and NIS compliance, and ICO-focused regulatory gap analysis.

**Primary legislation:** UK GDPR (retained EU law, as amended) · Data Protection Act 2018 · Privacy and Electronic Communications Regulations 2003 (PECR) · Network and Information Systems Regulations 2018 · Online Safety Act 2023

**Regulator:** ICO (Information Commissioner's Office)

**Every output is a draft for DPO or solicitor review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A qualified professional reviews, verifies, and decides. Citations carry UK-law source tags so you know which ones came from the uk-legal MCP and which need checking. Privilege markers are applied conservatively. Consequential actions — sending, executing, notifying the ICO — are gated behind explicit confirmation.

---

## Who this is for

| Role | Primary workflows |
|---|---|
| **DPO / privacy counsel** | DPIA sign-off, DPA review, reg gap analysis |
| **Privacy programme manager** | DSAR handling, DPIA intake, vendor privacy review |
| **Product / technology counsel** | DPIA generation for product launches and AI features |
| **Support / CS** | DSAR first-line response (with escalation) |

---

## First run: the cold-start interview

The plugin interviews you to learn: are you a controller or processor, which UK regulations actually apply (UK GDPR / PECR / Children's Code / NIS / OSA), what you will and won't agree to in a DPA. Then it reads three seed documents — your privacy notice, your DPA template, one DPIA you're happy with — and learns your real positions and house style.

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` and survives plugin updates.

```
/privacy-legal-uk:cold-start-interview
```

---

## Commands

| Command | Does |
|---|---|
| `/privacy-legal-uk:cold-start-interview` | Cold-start interview |
| `/privacy-legal-uk:use-case-triage [activity]` | Lawful basis + DPIA triage; Children's Code check; classify and set conditions |
| `/privacy-legal-uk:dpa-review [file]` | Review a DPA against your Art.28 playbook (auto-detects processor/controller) |
| `/privacy-legal-uk:dsar-response` | Walk through a DSAR and draft the response (1-month clock) |
| `/privacy-legal-uk:dpia-generation [feature]` | Generate a DPIA following the ICO template structure |
| `/privacy-legal-uk:reg-gap-analysis [regulation]` | Diff a new ICO guidance / statute / regulation against current policy and practice |
| `/privacy-legal-uk:policy-monitor` | Sweep for policy drift, or direct query for a proposed new practice |
| `/privacy-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |
| `/privacy-legal-uk:customize` | Adjust one thing in your practice profile without re-running the full interview |

---

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Writes CLAUDE.md from interview + seed docs (privacy notice, DPA template, reference DPIA) |
| **use-case-triage** | UK GDPR lawful basis + special category triage; DPIA mandatory trigger check; Children's Code check; policy conflict check |
| **dpa-review** | Bi-directional (processor/controller) DPA term-by-term review; Art.28 obligations; IDTA/UK Addendum for transfers |
| **dsar-response** | Identity verification → system walk → DPA 2018 Sch.2 exemptions → 1-month response draft |
| **dpia-generation** | DPIA in house format following ICO template; Art.35(3) mandatory trigger check; policy consistency check |
| **reg-gap-analysis** | New UK GDPR/DPA 2018/PECR/NIS/OSA requirement vs. current state; ICO guidance updates; UK/EU post-Brexit divergence |
| **policy-monitor** | Crawls outputs for practice drift; drafts privacy-notice language updates |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices |
| **customize** | Adjust one section of the practice profile without re-running the full interview |

---

## Quick start

### 1. Setup

```
/privacy-legal-uk:cold-start-interview
```

Have ready: your published privacy notice URL, your standard DPA / processor agreement, one DPIA you're happy with.

### 2. Triage a new feature or processing activity

```
/privacy-legal-uk:use-case-triage "Marketing wants to use behavioural data for ad personalisation"
```

Output: PROCEED / DPIA REQUIRED / DPIA MANDATORY / STOP — with conditions table, lawful basis determination, Children's Code check, and offer to kick off the DPIA in the same conversation.

### 3. Review a customer DPA

```
/privacy-legal-uk:dpa-review customer-dpa.pdf
```

Output: direction auto-detected, term-by-term review against your Art.28 playbook, proposed redlines, international-transfer mechanism check (IDTA / UK Addendum / adequacy), privacy-notice consistency check.

### 4. Handle a DSAR

```
/privacy-legal-uk:dsar-response
```

Walks you through: classify → verify → locate → DPA 2018 Sch.2 exemptions → draft. Deadline: 1 calendar month from receipt (UK GDPR Art.12(3)). Uses your systems list from the config CLAUDE.md.

### 5. DPIA a new feature

```
/privacy-legal-uk:dpia-generation "Location sharing feature"
```

Intake questions → DPIA in your house format → policy diff → conditions list. Follows ICO DPIA template structure. DPO consultation required for mandatory DPIAs (Art.35(2)).

---

## How it learns

Your practice profile at `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `policy-monitor` skill watches for drift between your privacy notice and your practice and proposes updates. You can re-run setup, edit the file directly, or tell a skill to record a new position.

---

## Key UK law reference

| Concept | UK instrument | Notes |
|---|---|---|
| Core data protection law | UK GDPR + DPA 2018 | UK GDPR is the post-Brexit retained version; DPA 2018 supplements and modifies it |
| Cookies and direct marketing | PECR (SI 2003/2426) | Separate consent regime for cookies; opt-in for email/SMS marketing to individuals |
| Network and information systems | NIS Regulations 2018 (SI 2018/506) | Applies to operators of essential services and digital service providers |
| Content platforms / child safety | Online Safety Act 2023 | Overlaps with data/privacy obligations for in-scope services |
| Children's Code | ICO Age Appropriate Design Code (DPA 2018 s.123) | Applies to online services likely accessed by children; 15 standards |
| Regulator | ICO | ico.org.uk — enforcement notices, penalty notices, guidance |
| ICO penalty ceiling | £17.5m or 4% global annual turnover (UK GDPR); £8.7m or 2% (other DPA 2018 breaches) | Whichever is higher |
| DSAR deadline | 1 calendar month (UK GDPR Art.12(3)) | Extension: up to 2 further months for complex/numerous |
| Breach notification to ICO | 72 hours from awareness (UK GDPR Art.33) | |
| International transfers | IDTA / UK Addendum to EU SCCs / UK adequacy decisions | UK-US Data Bridge in force since October 2023 |

---

## File structure

```
privacy-legal-uk/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md
├── README.md
├── hooks/hooks.json
├── logs/.gitkeep
├── references/currency-watch.md
└── skills/
    ├── cold-start-interview/
    ├── customize/
    ├── use-case-triage/
    ├── dpa-review/
    ├── dsar-response/
    ├── dpia-generation/
    ├── reg-gap-analysis/
    ├── policy-monitor/
    └── matter-workspace/
```

---

## Notes

- DPA review is bi-directional: same skill handles customer DPAs (defend operational flex as processor) and vendor DPAs (protect data as controller). Direction auto-detected, or ask.
- DPIA format comes from your seed DPIA. If you didn't provide one during setup, it uses the ICO template structure — re-run setup with a reference DPIA to fix.
- Gap analysis (`reg-gap-analysis`) handles incoming regulations including ICO guidance updates. Policy monitor handles internal practice drift. Different tools for different directions of change.
- Policy monitor requires an outputs folder to be configured (set during setup) for the sweep to work. Direct-query mode works without it.
- The plugin tracks UK/EU post-Brexit divergence: UK adequacy decisions, IDTA vs. EU SCCs, ICO vs. EDPB guidance divergence. Flag cross-border matters with both UK and EU data subjects for dual-regime analysis.
