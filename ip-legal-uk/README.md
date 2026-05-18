# IP Counsel Plugin (UK)

UK intellectual property practice: trade marks, copyright, patents, designs, trade secrets, and open source. Handles first-pass trade mark clearance and freedom-to-operate triage under UK IP law, screens invention disclosures for initial patentability under the Patents Act 1977, drafts and triages cease-and-desist letters and online takedown notices (sending and responding), checks open source compliance, reviews IP clauses in agreements, and tracks registrations and renewal deadlines at the UK IPO, EUIPO, and EPO. Built around a practice profile that gets written by a cold-start interview — the plugin learns *your* enforcement posture, portfolio, and approval matrix, not a generic one.

**Key statutes:** Trade Marks Act 1994 (TMA 1994), Copyright, Designs and Patents Act 1988 (CDPA 1988), Patents Act 1977 (PA 1977), Registered Designs Act 1949 (as amended), Trade Secrets (Enforcement, etc.) Regulations 2018. Post-Brexit: UK and EU IP systems are now separate — UK trade marks at the IPO, EU trade marks at EUIPO, no automatic conversion for new applications.

**Every output is a draft for professional review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. A solicitor, Chartered Patent Attorney, or Registered Trade Mark Attorney reviews, verifies, and decides. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **In-house IP counsel / solicitor** | Enforcement decisions, clause review, portfolio oversight, FTO triage |
| **Chartered Patent Attorney / Patent Attorney** | Patent FTO, invention intake, portfolio maintenance — *not patent claim drafting* |
| **Registered Trade Mark Attorney / CITMA Registrant** | Clearance, clause review, portfolio maintenance |
| **IP paralegal / specialist** | Portfolio and renewal tracking, clearance first passes, matter intake |
| **Brand protection manager** | Cease-and-desists, online takedowns, watch-service follow-up |
| **Law firm IP associate** | Matter workspaces per client, clearance and FTO triage, clause review |
| **Legal ops managing an IP portfolio** | Registration tracker, renewal deadlines, OSS compliance checks |

This plugin does **not** draft patent claims. Patent prosecution with claim strategy is a specialist craft that needs a Chartered Patent Attorney and should not be outsourced to a generalist tool. Patent work here is limited to FTO triage (is this product blocked by someone else's patent?), IP clause review in agreements, portfolio renewal tracking, and infringement triage.

## First run: the cold-start interview

On first use, the plugin interviews you — ten to fifteen minutes, conversational — to learn how your practice actually works. It asks about your practice area mix, your jurisdiction footprint (UK/EU/global), your post-Brexit portfolio position, your enforcement posture, your approval matrix, and your escalation triggers.

It writes what it learns to `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` — a plain-English document about your practice that every other skill reads before doing anything. You edit the document, not a config file.

```
/ip-legal-uk:cold-start-interview
```

## UK IP legal framework

This plugin applies UK IP law throughout. Key distinctions from US law:

**Trade marks:** Trade Marks Act 1994 implements the EU Trade Marks Directive (retained in UK law post-Brexit). UK IPO for UK registrations; EUIPO for EU trade marks (separate system since 31 Dec 2020). Confusion analysis under TMA 1994 s.5(2)/(10)(2): global appreciation approach (not US multi-factor circuits). Passing off: English common law (*Reckitt & Colman v Borden* [1990] UKHL) — goodwill + misrepresentation + damage. Well-known marks: TMA 1994 s.56. Madrid System: UK is party; can designate UK (IPO) or EU (EUIPO) via separate Madrid designations.

**Copyright:** CDPA 1988. Originality: "own intellectual creation" threshold (*Infopaq*; *SAS Institute v World Programming*) — not sweat of the brow. Duration: life + 70 years (literary, dramatic, musical, artistic). **No registration system in UK** — automatic protection on creation. Moral rights: CDPA 1988 ss.77–89. Database rights: UK sui generis right (Copyright and Rights in Databases Regulations 1997) retained post-Brexit. Employed works: employer owns copyright (CDPA 1988 s.11(2)). Commissioned works: contractor typically retains copyright unless assigned — different from US work-for-hire.

**Patents:** Patents Act 1977; EPC (UK still participates in EPO). UK national filings at IPO; EP designating UK still valid. Unified Patent Court: UK opted out — UPC proceedings do not cover UK. Patentability exclusions: PA 1977 s.1(2); Aerotel/Macrossan and Symbian tests for software. Employee inventions: PA 1977 ss.39–43 inventor compensation for outstanding benefit. SEPs: *Unwired Planet v Huawei* [2020] UKSC 37 on FRAND.

**Designs:** Registered Designs Act 1949 (as amended); UK Unregistered Design Right (CDPA 1988 s.213); UK supplementary unregistered design right (retained EU unregistered design right). IPO for registered designs.

**Trade secrets / confidential information:** English law of confidence (*Coco v AN Clark Engineers* [1969]); Trade Secrets (Enforcement, etc.) Regulations 2018 (implementing EU Trade Secrets Directive — retained). Springboard doctrine for employees.

**Enforcement venues:** IPEC (Intellectual Property Enterprise Court) for smaller/simpler IP disputes (£500K damages cap); High Court (Patents Court; Chancery Division) for larger cases. UK IPO inter partes proceedings for trade mark and design challenges.

## Commands

| Command | Does |
|---|---|
| `/ip-legal-uk:cold-start-interview` | Run (or re-run) the cold-start interview |
| `/ip-legal-uk:cease-desist [context]` | Cease-and-desist — send, or triage an inbound one, with the approval routing your CLAUDE.md requires |
| `/ip-legal-uk:takedown [context]` | Online takedown — send (UK/EU notice regime), respond to a received notice, or draft a counter-notice |
| `/ip-legal-uk:clearance [mark]` | First-pass trade mark clearance — knockout + confusion analysis under TMA 1994, solicitor/attorney still signs off |
| `/ip-legal-uk:fto-triage [product / claim scope]` | Freedom-to-operate triage — surfaces blocking references for attorney review under PA 1977 / EPC |
| `/ip-legal-uk:invention-intake [disclosure]` | Invention disclosure first-pass screen — novelty, obviousness, excluded subject matter, bar dates, detectability, strategic value |
| `/ip-legal-uk:infringement-triage [context]` | Infringement triage — is this worth pursuing, and how |
| `/ip-legal-uk:ip-clause-review [file]` | Review IP clauses in an agreement — assignment, licence grant, IP indemnity, OSS reps; UK-specific assignment formalities (CDPA s.90, TMA s.24, PA 1977 s.30) |
| `/ip-legal-uk:oss-review [repo / file list]` | Open source licence compliance check — copyleft obligations, attribution, licence compatibility |
| `/ip-legal-uk:portfolio` | Registration and renewal tracker — what's due at the IPO, EUIPO, EPO; what's filed, what needs action |
| `/ip-legal-uk:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | First-run interview that writes `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` |
| **cease-desist** | Draft or triage a C&D; routes through the approval matrix before sending |
| **takedown** | Online takedown notice (UK/EU regime), response to a received notice, or counter-notice |
| **clearance** | Knockout search + likelihood-of-confusion first pass for a proposed mark under TMA 1994 |
| **fto-triage** | FTO triage — flags references an attorney should read before launch under PA 1977 / EPC |
| **invention-intake** | First-pass patentability screen for an invention disclosure — novelty, obviousness, excluded subject matter, bar dates, detectability, strategic value |
| **infringement-triage** | Given an apparent infringement, decide: ignore / soft letter / C&D / file |
| **ip-clause-review** | Reviews IP clauses in MSAs, SOWs, licences, contractor agreements; UK assignment formalities |
| **oss-review** | Checks open source licences in a repo against the OSS policy |
| **portfolio** | Registration register, renewal deadlines, status dashboard; UK IPO + EUIPO + EPO deadlines |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices |

## Interactive commands vs. scheduled agents

The commands above run when you invoke them — for when you're working a matter. The agents below run on a schedule:

| Agent | What it watches | Default cadence |
|---|---|---|
| **ip-renewal-watcher** | Portfolio register — computes what's due (renewals, affidavits, maintenance fees, annuities) in the next 90 days and posts a ranked deadline report | Weekly |

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors in this plugin:

- **uk-legal MCP** — UK case law (TNA Find Case Law), legislation (legislation.gov.uk), Hansard, Bills, HMRC guidance, and OSCOLA citation parsing. Citations retrieved via this connector are tagged `[uk-legal MCP]` and can be traced.
- **govuk MCP** — GOV.UK content, guidance, IPO publications, and government IP policy. Citations tagged `[govuk MCP]`.
- **BAILII** — British and Irish Legal Information Institute — full-text case law. Citations tagged `[BAILII]`.
- **legislation.gov.uk** — official statute text. Citations tagged `[legislation.gov.uk]`.
- **Solve Intelligence** — patent and non-patent literature search, SEP technical standards, prior art, claim analysis. With patent research connected: FTO and prior-art skills pull references automatically.

Citations from model knowledge or web search are tagged `[model knowledge — verify]` or `[web search — verify]` and should be checked against a primary source before anyone relies on them.

## Integrations

Ships with connectors configured in `.mcp.json`:

- **uk-legal MCP** — UK legislation and case law research
- **govuk MCP** — IPO and government guidance
- **uk-due-diligence** — Companies House + other UK registers for counterparty diligence
- **Solve Intelligence** — patent and non-patent literature search
- **Slack** — search messages, read channels, find discussions
- **Google Drive** — search, read, and fetch documents

## Quick start

### 1. Get interviewed

```
/ip-legal-uk:cold-start-interview
```

Ten to fifteen minutes. Have your portfolio list, brand guidelines (if any), a C&D template (if any), and your OSS policy (if any) ready to share.

Your configuration is stored at `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` and survives plugin updates.

### 2. Clear a mark

```
/ip-legal-uk:clearance "APEXLEAF"
```

Output: knockout-hit list (absolute grounds under TMA 1994 s.3), likelihood-of-confusion factor analysis (relative grounds, TMA 1994 s.5(2)), flags for solicitor/attorney review. Not a go/no-go.

### 3. See what's due

```
/ip-legal-uk:portfolio
```

Output: registrations with renewal, affidavit, or maintenance deadlines in the next 90 days, grouped by urgency. Covers UK IPO, EUIPO, EPO, and Madrid Monitor.

## File structure

```
ip-legal-uk/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Your practice profile — written by cold-start, edited by you
├── README.md
├── agents/
│   └── ip-renewal-watcher.md
├── skills/
│   ├── cold-start-interview/
│   ├── cease-desist/
│   ├── takedown/
│   ├── clearance/
│   ├── fto-triage/
│   ├── invention-intake/
│   ├── infringement-triage/
│   ├── ip-clause-review/
│   ├── oss-review/
│   ├── portfolio/
│   └── matter-workspace/
└── hooks/hooks.json
```

## Configuration

The plugin reads user-specific configuration from:

```
~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md
```

This path survives plugin updates. The `CLAUDE.md` that ships with the plugin is a template — it is replaced every upgrade. The cold-start interview writes your populated version to the config path above; from then on, edit that file directly when something changes.

## Post-Brexit note

UK and EU IP rights are now entirely separate systems. Since 31 December 2020:

- **Trade marks:** Existing EUTMs at exit generated comparable UK trade marks automatically. New EUTMs filed after exit do NOT cover the UK; a separate UK IPO application is required. UK trade marks do NOT cover EU. Madrid designations for UK and EU must be filed separately.
- **Designs:** EU registered designs do not cover UK; UK registered designs do not cover EU. EU unregistered design right does not cover UK (and vice versa, though the UK has a supplementary unregistered design right based on the EU model). Check your design portfolio for coverage gaps.
- **Patents:** EPO patents still designate the UK and are fully valid in the UK. The Unified Patent Court does NOT cover the UK — UPC proceedings are irrelevant for UK validity or infringement. UK national patent applications at the IPO remain unchanged.
- **Copyright:** No registration in either system; Berne Convention continuity means UK-authored works remain protected across the EU and vice versa on authorship rules, though enforcement is jurisdiction-specific.

## Notes

- Every skill reads the practice profile first. If it finds placeholders, it stops and tells you to run `/ip-legal-uk:cold-start-interview`. There's no generic fallback — a generic IP posture is worse than no posture.
- Sending a C&D starts a fight. The `/ip-legal-uk:cease-desist` skill will not send anything itself; it drafts, surfaces the approval matrix entry, and waits for the approver.
- `/ip-legal-uk:clearance` and `/ip-legal-uk:fto-triage` are **first-pass** triage. The output is a research package for a solicitor or patent attorney, not a clearance opinion. The skill says so on every run.
- `/ip-legal-uk:oss-review` flags licence obligations and incompatibilities. It does not bless a commercial-use decision — engineering and legal decide that together.
- Patent claim drafting is intentionally out of scope. This plugin plays well alongside a Chartered Patent Attorney; it does not replace one.
