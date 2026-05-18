---
name: oss-review
description: >
  Open source licence compliance check for a dependency list, a single
  library, or outbound code. Use when reviewing a manifest, SBOM, or repo for
  copyleft obligations and licence compatibility, when asked whether a library
  can ship, or when preparing code to be open-sourced.
argument-hint: "[file path to manifest / SBOM | package name | repo path | paste text]"
---

# /oss-review

Runs an open source licence compliance check against the practice profile in `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. Classifies dependencies by licence family, maps obligations to the deployment model, flags licence-unknown and non-OSI-posing-as-OSS packages, and recommends actions — comply, replace, remove, seek legal review, seek commercial licence.

## Instructions

1. **Load `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`.** If placeholders present, stop and prompt: "Run `/ip-legal-uk:cold-start-interview` first — I need to learn your practice profile (and OSS policy, if any) before I can review." If the practice profile points at an uploaded OSS policy, read that too — it is the source of truth for accepted / review / banned licences on this team.

2. **Establish the scope:** a dependency list (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, pom.xml, SBOM), a single library, or outbound code the team is preparing to open-source.

3. **Establish the deployment model** before classifying obligations — SaaS, distributed binary, internal only, or embedded.

4. **Follow the workflow below.** In particular:
   - Read the actual licence text, not just metadata.
   - Classify each package into permissive / weak copyleft / strong copyleft / public domain / non-OSI / unknown.
   - Flag licence-unknown as "needs review," not permissive by default.
   - Flag non-OSI source-available licences (SSPL, BUSL, Commons Clause, Elastic Licence, fair-source).
   - For outbound code, check that the chosen outbound licence is compatible with every embedded dependency.

5. **Output the memo** per the template below.

6. **Respect the decision posture.** When a copyleft-trigger analysis turns on a contested question, flag for attorney review. Anything classified as strong copyleft or licence-unknown goes to a solicitor/attorney before the dependency ships or the code is released.

## Examples

```
/ip-legal-uk:oss-review ~/code/my-project/package.json
/ip-legal-uk:oss-review ~/code/my-project/requirements.txt
/ip-legal-uk:oss-review redis
/ip-legal-uk:oss-review ~/code/my-project
```

---

## Works better connected

OSS clearance requests usually come in via a ticketing system. Connected to
Jira, Linear, or Asana, this skill can: monitor incoming OSS requests, respond
with guidance directly in the ticket, and track clearance status across requests.

Without a connector, paste the ticket or describe the request and I'll handle
it one at a time.

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is
`✗` (the default for in-house users), skip — skills use practice-level context.
If enabled and there is no active matter, ask: "Which matter is this for? Run
`/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

---

## Purpose

Tell the user what licences are in their dependency tree, what obligations those licences trigger given how the code will be deployed, and what to do about each one.

**This is a first-pass classification.** Copyleft analysis depends on the deployment model, the degree of linking, the jurisdiction, and sometimes on legal questions that have not been tested in court. For anything that classifies as strong copyleft or licence-unknown, a solicitor or attorney evaluates before the dependency ships or the code is released.

## Precondition: load the practice profile

**Before scanning dependencies, read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`.** If missing or with placeholders, stop and run `/ip-legal-uk:cold-start-interview`. The practice profile tells you:

- Who owns OSS review on this team
- Escalation routing for copyleft obligations
- The work-product header to prepend

If the practice profile has an OSS policy uploaded, read that too.

## Workflow

### Step 1: What's the scope?

> What are we reviewing?
>
> 1. **A dependency list**
> 2. **A single library**
> 3. **Our own code** — we're planning to open-source this

### Step 2: What's the deployment model?

> How will this be deployed?
>
> 1. **SaaS / hosted service** — users access over a network
> 2. **Distributed binary** — we ship compiled code to users
> 3. **Internal only** — used only inside the company
> 4. **Embedded / firmware** — shipped in hardware

| Deployment | Licences that materially matter |
|---|---|
| SaaS | AGPL (network-trigger), permissive attribution in any UI, SSPL/BUSL/Elastic if repurposing as competing service |
| Distributed binary | GPL, LGPL, MPL, EPL (all trigger on distribution), permissive attribution |
| Internal only | Most copyleft does not trigger — no distribution. AGPL still triggers if external users interact over network. |
| Embedded / firmware | GPL is especially hard to comply with here (source disclosure + reproducible build + installation information). |

**Jurisdiction note for UK OSS enforcement.** UK copyright law (CDPA 1988) governs OSS licence enforcement in the UK. The GPL and AGPL are copyright licences — an open source licence is only as enforceable as the underlying copyright law permits. UK courts have generally been willing to treat OSS licence conditions as contractual or copyright conditions. Post-Brexit, EU jurisprudence on OSS licences (e.g., German case law on GPL enforcement) is persuasive but not binding. Where a licence has been interpreted differently in UK vs. EU court practice, flag for solicitor review.

**EUPL (European Union Public Licence).** The EUPL is an EU-issued licence, version 1.2. It is compatible with several other licences (see the compatibility matrix in Annex I of EUPL 1.2). Post-Brexit, UK organisations using EUPL-licensed code should note: the EUPL refers to EU law concepts (e.g., database rights under the EU Database Directive). UK database rights (governed by the Copyright and Rights in Databases Regulations 1997, retained law post-Brexit) remain, but future divergence is possible. Flag EUPL for solicitor review when it is a material dependency.

### Step 3: Classify each dependency

For every package, determine the licence. Read the actual licence text, not just the metadata.

Classify into:

| Bucket | Examples | Key obligations |
|---|---|---|
| **Permissive** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Unlicense | Attribution, preserve licence text, Apache-2.0 adds patent grant + NOTICE requirement |
| **Weak copyleft** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | File-level or library-level source disclosure; linking rules vary |
| **Strong copyleft** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (depending on version and use) | Broad source disclosure; AGPL extends to network use |
| **Public domain / dedication** | CC0, Unlicense, WTFPL | Typically no obligations, but dedication to public domain may not be universally effective in jurisdictions that don't recognise it (e.g., EU moral rights cannot be fully waived in some member states — UK moral rights for certain works can be waived under CDPA s.87 but not extinguished) |
| **Non-OSI source-available** | SSPL, BUSL, Commons Clause, Elastic Licence, Confluent Community, fair-source family | Not open source — restrict commercial use, competing-service use, or both |
| **Other / custom / unknown** | Vendor-specific, proprietary, missing licence file, licence conflict | Stop — do not treat as permissive by default |

Flag:

- **Dual-licensed packages** — which licence are we using?
- **Deprecated packages** — no longer maintained; suggest replacement.
- **Packages with a copyleft dependency in their own tree** — top-level is permissive but transitive is copyleft.
- **Packages that changed licence recently** — confirm the version pinned is under the licence you think.

### Step 4: Map obligations to the deployment model

For each classified dependency:

```markdown
### [package@version] — [Licence]

**Classification:** [Permissive / Weak copyleft / Strong copyleft / Public domain / Non-OSI / Unknown]

**Obligations for our deployment ([SaaS / binary / internal / embedded]):**

- [ ] [Specific obligation]
- [ ] [e.g., "Include attribution in a NOTICES file shipped with the app"]
- [ ] [e.g., "AGPL network trigger — if users access our modified version over a network, source must be offered to them"]

**Risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

**Recommendation:** [Comply / Replace with [alternative] / Remove / Solicitor review before shipping / Seek commercial licence from [vendor]]
```

> **How is the copyleft dependency consumed?** The linking relationship determines whether copyleft actually triggers. Ask or determine:
> - **Static linking / compilation together:** Strong signal that copyleft triggers.
> - **Dynamic linking / shared library:** LGPL explicitly permits this ("work that uses the Library"). GPL's position is contested.
> - **Subprocess / IPC:** Separate processes over well-defined interfaces. Generally not derivative.
> - **Network API call:** For most licences, no. For **AGPL**, the network-interaction clause means serving the software over a network IS distribution.
> - **File-scope copyleft (MPL):** Only modified files carry copyleft.
>
> **The severity rating depends on this.** Static-linked LGPL in a proprietary product is 🔴 Critical. Dynamic-linked LGPL is 🟢 Low. Same licence, opposite rating.

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Strong copyleft in a deployment that triggers it (GPL in a distributed binary, AGPL in SaaS). Non-OSI licence that conflicts with business model. Licence cannot be determined and package is load-bearing. |
| 🟠 High | Weak copyleft with obligations the team hasn't set up for. Dual-licensed with ambiguous choice. Licence file says one thing, headers say another. |
| 🟡 Medium | Permissive with attribution requirements not yet wired into build. Transitive copyleft in a position that may or may not trigger. |
| 🟢 Low | Permissive with obligations already satisfied. Copyleft in a deployment model that doesn't trigger it. |

### Step 5: Flag failure modes

Call out any of the following in a top-of-memo section:

- **Licence unknown** — classify as "needs review," not permissive.
- **Licence file conflicts with file headers** — report the conflict.
- **Incompatible combinations** — GPL-2.0 only + Apache-2.0 historically a known incompatibility; check MPL / EPL / GPL combinations.
- **Non-OSI licences posing as open source** — SSPL, BUSL, Commons Clause, Elastic Licence. Read the licence; don't rely on GitHub's "open source" badge.
- **Licence changes** — if a prior version was permissive and the current version is source-available, the pin matters.
- **EUPL or EU-specific licences** — note UK post-Brexit position and flag for solicitor review.

### Step 6: Outbound check (if reviewing our own code before open-sourcing)

If the user is preparing to open-source code:

- Confirm the chosen outbound licence is compatible with every embedded dependency's licence
- Confirm LICENSE file is present and correct
- Confirm NOTICE file is present and lists required attributions (Apache-2.0 and others)
- Confirm third-party licence texts are bundled where required
- Confirm no proprietary or confidential code, no customer data, no embedded credentials in the repo history
- Confirm trade mark and brand policy for any project name (separate from the copyright licence)

### Step 7: Assemble the memo

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` → `## Outputs`.

> **No silent supplement.** If a research query returns few or no results for a rule the memo needs, report what was found and stop. Don't fill the gap from web search or model knowledge without asking.
>
> **Source attribution.** Tag citations: `[OSI]`, `[SPDX]`, `[FSF]`, `[SFC/SFLC]`, `[uk-legal MCP]`, `[web search — verify]`, `[model knowledge — verify]`, `[user provided]`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# OSS Review: [Project / Dependency List / Package]

**Reviewed:** [date]
**Scope:** [Dependency list / Single library / Outbound code]
**Deployment model:** [SaaS / Binary / Internal / Embedded]

---

## Bottom line

[Two sentences. Can this ship? What has to happen first?]

**Packages reviewed:** [N]
**By classification:** [N permissive, N weak copyleft, N strong copyleft, N public domain, N non-OSI, N unknown]
**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name, per practice profile]

---

## Top-of-memo flags

[Licence-unknown list, licence-conflict list, non-OSI-posing-as-OSS list,
incompatible combinations, EUPL / post-Brexit notes]

---

## By package

[Blocks from Step 4, grouped by severity]

---

## Jurisdiction note

OSS licence enforceability in the UK is governed by CDPA 1988. Post-Brexit,
EU case law on OSS licence enforcement (notably German courts' rigorous GPL
enforcement) is persuasive but not binding. The AGPL network trigger has not
been broadly tested in UK courts. EUPL contains EU-law references that may
interact differently with retained UK law. Flag any licence where UK and EU
enforcement practice may differ materially, and route to a solicitor for
affected dependencies.

---

## Outbound check (if applicable)

[From Step 6]

---

## Approval routing

[From practice profile — who approves, what triggers automatic escalation]
```

## Decision posture

When a licence cannot be confidently classified, flag it as **"needs review"** — do not call it permissive. Under-classifying is a one-way door.

## Quality checks before delivering

- [ ] Practice profile and any OSS policy were loaded
- [ ] Deployment model established before classifying obligations
- [ ] Every dependency has a classification, including transitives where available
- [ ] Licence-unknown packages flagged, not defaulted to permissive
- [ ] Licence text was read (not just metadata) for any copyleft or non-OSI finding
- [ ] UK jurisdiction note included for post-Brexit and EUPL implications
- [ ] Source tags applied; no stripped `verify` tags
- [ ] Approver named per practice profile

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

If the scan surfaced more than ~10 packages, offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`).
