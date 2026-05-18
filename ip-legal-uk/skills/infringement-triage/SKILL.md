---
name: infringement-triage
description: >
  Infringement triage across trade mark, copyright, patent, and trade secret —
  a flag list with the factors cutting each way, not a finding. Use when
  assessing whether someone is infringing your IP or whether you might be
  infringing theirs, when a knockoff or copycat surfaces, or when deciding
  whether a matter is worth pursuing and how.
argument-hint: "[describe the facts and which right — or just the facts and I'll ask which right]"
---

# /infringement-triage

**This is a triage, not a finding of infringement or non-infringement.**
Infringement analysis is fact-intensive and legally complex. Acting on a
triage — sending a cease-and-desist, refusing to stop, filing proceedings, or
deciding not to — without solicitor or attorney review is how companies end up
on the wrong side of costs orders, unjustified threats claims (TMA 1994 s.21 /
PA 1977 s.70), declaratory relief applications, and (for patents) additional
damages for flagrant infringement.

## Instructions

1. Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal-uk:cold-start-interview`.
2. Follow the workflow below.
3. Ask which right is at issue — trade mark / copyright / patent / trade secret
   / mixed. If mixed, run each separately; do not blend.
4. Run common intake (party posture — senior or accused, jurisdiction, timing,
   exhibits).
5. Walk the mode-specific factors:
   - **Trade mark** — global appreciation confusion test (TMA 1994 s.10(2)) +
     dilution (s.10(3)) + passing off as a parallel track + unjustified threats
     flag (s.21).
   - **Copyright** — ownership + originality + copying + fair dealing + CDPA
     1988 defences.
   - **Patent** — claim-chart first pass (route to `fto-triage` output
     structure); literal + equivalents (*Actavis*); indirect (PA 1977 s.60(2));
     invalidity defences; unjustified threats flag (PA 1977 s.70).
   - **Trade secret / confidential information** — English law of confidence
     (*Coco v AN Clark* [1969] + Trade Secrets Regulations 2018 framework):
     confidential quality + obligation of confidence + unauthorised use.
6. Produce a flag list with direction — what cuts toward the senior party,
   what cuts toward the accused, what's mixed. Never conclude.
7. Write the triage memo to the matter folder or practice outputs folder. Apply
   the work-product header per role.
8. End with recommended next steps, the non-lawyer gate if the role is
   non-lawyer, and — if the practice posture supports assertion — an offer to
   draft the C&D via `/ip-legal-uk:cease-desist` or the takedown via
   `/ip-legal-uk:takedown`. Do not draft automatically.

This skill never concludes. If uncertain, flag — the solicitor/attorney decides.

## Examples

```
/ip-legal-uk:infringement-triage "competitor launched a tool called APEXSEED in class 9 — we have APEXLEAF registered in class 9; likely confusion?"
```

```
/ip-legal-uk:infringement-triage "former engineer took notes on our model architecture to a competitor — possible trade secret?"
```

```
/ip-legal-uk:infringement-triage
```

---

## THIS IS A TRIAGE, NOT A FINDING

**The loudest guardrail in the plugin. Say this at the top of every output. Do
not drop it. Do not soften it.**

> **This is a triage, not a finding of infringement or non-infringement.**
> Infringement analysis is fact-intensive and legally complex. The triage
> identifies the factors and flags the ones that matter most; it does not
> conclude. A conclusion requires a solicitor or attorney's judgment on the
> facts, the right scope, the relevant jurisdiction's law, and the likely
> defences.
>
> Acting on a triage without professional review is how companies end up on the
> wrong side of costs orders in IPEC or the High Court, unjustified threats
> claims under TMA 1994 s.21 or PA 1977 s.70 (a specific UK regime that can
> result in damages and an injunction against the asserting party),
> declaratory relief applications, and additional damages for flagrant patent
> infringement under PA 1977 s.63.

Under-calling a conflict is a one-way door — a C&D not sent and a mark goes
generic in the market; a claim not chased and limitation runs; a copied work
stays on the site. Over-calling is a two-way door — the solicitor/attorney
narrows. Stay on the two-way door side.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is
`✗` (the default for in-house users), skip — skills use practice-level context.
If enabled and there is no active matter, ask: "Which matter is this for? Run
`/ip-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

Infringement triages often lead into cease-and-desist drafting or takedown
routing. Open a matter if one isn't active and the practice is private.

---

## Load the practice profile first

Read `~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md`. Pull:

- **Role** from `## Who's using this`.
- **Enforcement posture** from `## Enforcement posture` — the triage output
  should end with a routing suggestion consistent with the stated posture and
  the named approver for the relevant letter type.
- **Registered in / enforce where** from `## IP practice profile` — determines
  which jurisdiction's test to apply by default.
- **Integrations** from `## Available integrations` — uk-legal MCP, Solve
  Intelligence each affects whether the triage can cite to case law, prior
  rulings, or prior art.
- **Decision posture** from `## Decision posture on subjective legal calls` —
  this skill never concludes on a subjective threshold.

If the config has `[PLACEHOLDER]`:

> I notice you haven't configured your practice profile yet — that's how I
> tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal-uk:cold-start-interview` (2 minutes) to configure your
>   profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — UK
>   jurisdiction, middle risk appetite, solicitor role, no playbook.

### Provisional mode

If the user says "provisional," run normally using generic defaults: middle risk
appetite, solicitor role, UK jurisdiction, no playbook. Tag the reviewer note
and every finding block with `[PROVISIONAL]`. At the end append:

> "That was a generic run against default assumptions. Run
> `/ip-legal-uk:cold-start-interview` to get output calibrated to YOUR practice."

---

## Mode selection

Ask at the top, before anything else:

> Which right are we triaging?
>
> 1. **Trade mark** — confusion, dilution, or passing off
> 2. **Copyright** — copying, fair dealing, online infringement
> 3. **Patent** — claim-chart first pass, literal read + equivalents
> 4. **Trade secret / confidential information** — law of confidence,
>    Trade Secrets Regulations 2018
> 5. **Mixed / not sure** — describe the facts and I'll pick

If the user picks "not sure," help them sort. The same facts can implicate
multiple rights.

**If more than one right is in play, run the triage for each, separately.**

---

## Intake (common to all modes)

> Before I walk factors:
>
> 1. **Posture.** Are you the potentially senior party (they're taking yours)
>    or the potentially accused party (we're the ones being looked at)?
> 2. **Jurisdiction.** England & Wales / Scotland / Northern Ireland / UK-wide?
>    EU jurisdiction? Post-Brexit note: UK and EU IP rights are separate —
>    a EUTM infringement claim in the UK courts does not apply; UK TMA 1994
>    governs UK territory.
> 3. **Timing.** Is a limitation period or laches clock running? Under the
>    Limitation Act 1980, the general limitation period for IP torts is 6 years
>    from the date the cause of action accrued.
> 4. **What exhibits / evidence / source documents do you have?** A screenshot,
>    a URL, a packaging photo, a code excerpt, an ex-employee contract.

Wait for the answer before walking factors.

---

## Trade mark mode

### Confusion (TMA 1994 s.10(2))

The UK test is a **global appreciation** of the likelihood of confusion by the
average consumer. The test derives from TMA 1994 (implementing the EU Trade
Marks Directive, retained in UK law post-Brexit) and the case law of the CJEU,
which UK courts continue to follow on pre-Brexit interpretations.

Key factors per UK/EU case law:

- **Similarity of marks** — visual / aural / conceptual comparison. Consider
  the overall impression. Dominant and distinctive elements weigh more heavily.
- **Similarity of goods or services** — complementary / competing / related
  goods and services; Nice classification not determinative.
- **Distinctive character of the earlier mark** — inherent distinctiveness or
  distinctiveness acquired through use. A more distinctive mark has a wider
  scope of protection.
- **Average consumer** — normally informed, reasonably attentive and
  circumspect, for the goods/services in question.
- **Global appreciation** — marks and goods/services are considered
  interdependently. A lesser degree of similarity between goods may be
  offset by a greater degree of similarity between marks, and vice versa.
- **Actual confusion** — strong evidence if present; absence is not
  determinative.

Walk each factor and flag what cuts each way. Cite UK/EU cases where available
from the uk-legal MCP.

### Dilution / unfair advantage / detriment (TMA 1994 s.10(3) / s.5(3))

Applies where the earlier mark has a reputation in the UK:

- **Reputation in the UK** — unlike dilution under EU law, UK law requires
  reputation in the UK specifically (post-Brexit, EUIPO reputation alone does
  not suffice for s.5(3) purposes in UK proceedings).
- **Blurring** (detriment to distinctive character) vs. **tarnishment**
  (detriment to reputation) vs. **unfair advantage** (free-riding).
- **Without due cause** — defences for comparative advertising, descriptive use.

If the senior mark does not plainly have UK reputation, flag dilution as a
stretch and explain why.

### Passing off (parallel track)

Even where the mark is registered, a passing off claim under English common
law is often run in parallel. Elements per *Reckitt & Colman Products Ltd v
Borden Inc* [1990] 1 WLR 491 (HL) (the "Jif Lemon" case):

- **Goodwill** — the claimant must have goodwill in the UK attached to a mark,
  name, get-up, or other distinctive feature.
- **Misrepresentation** — a representation that is (or is likely to be) believed
  by a substantial part of the relevant public to be the goods/services of the
  claimant.
- **Damage** — actual or likely damage to the claimant's goodwill or business.

Passing off can protect unregistered marks that a UK trade mark registration
would not cover, and can extend to get-up, product shapes, or brand elements.

### Unjustified threats (TMA 1994 s.21)

**Flag before recommending assertion.** The UK unjustified threats regime (TMA
1994 s.21 / Intellectual Property (Unjustified Threats) Act 2017 — which
reformed s.21) means:

- Threatening proceedings for trade mark infringement against a secondary actor
  (retailer, distributor, customer) without a parallel claim against the primary
  infringer (the manufacturer / applicant) exposes the claimant to a
  counterclaim for unjustified threats.
- "Safe" acts: making and importing infringing goods, applying the sign to goods
  or packaging, supplying services in the course of business.
- "Not safe" acts: retailing, stocking, distributing, importing after the
  manufacturer has already exported.

If the proposed enforcement target includes retailers, distributors, or
end-users rather than the primary manufacturer or importer, flag unjustified
threats risk prominently.

### Output

Factors table; what cuts each way; a "not a finding" conclusion line. End with
a routing suggestion against the enforcement posture in the practice profile.

---

## Copyright mode

### Ownership and originality

Is the claimant the owner (or exclusive licensee with standing)?

- **Employed works:** under CDPA 1988 s.11(2), the employer is the first owner
  of copyright in a literary, dramatic, musical, or artistic work made by an
  employee in the course of their employment (unless agreement to the contrary).
  **This differs from US work-for-hire**: UK employed-works rule is broader and
  automatic for employees; independent contractors/freelancers generally own
  the copyright unless expressly assigned (CDPA s.11(1) — author is first owner;
  CDPA s.90 — assignment must be in writing signed by or on behalf of the
  assignor).
- **Originality:** UK copyright subsists in a literary, dramatic, musical, or
  artistic work if it is the author's "own intellectual creation" — reflecting
  the EU standard from *Infopaq* and *SAS Institute v World Programming* [2013]
  EWCA Civ 1482, as retained in UK law post-Brexit.
- **No registration required** — UK copyright is automatic on creation.
- **Duration:** life + 70 years for literary, dramatic, musical, artistic works
  (CDPA 1988 s.12(2)).

### Copying

Two elements:

- **Did the defendant copy?** UK copyright is infringed by *copying* — an
  element of causal connection between claimant's work and defendant's work is
  required. Independent creation is a defence.
- **Has a substantial part been copied?** CDPA 1988 s.16(3): infringement
  occurs when a substantial part is copied. "Substantial" is qualitative, not
  just quantitative — the heart of the work matters more than volume.

### Fair dealing (CDPA 1988 ss.29–30)

UK fair dealing is **purpose-specific** — much narrower than US fair use.
The UK has prescribed fair dealing purposes; there is no general fair dealing
defence. The main purposes:

- **Research or private study** (s.29) — non-commercial research only; fair
  dealing; acknowledgement required for literary, dramatic, musical, artistic
  works.
- **Criticism, review, or reporting current events** (s.30) — fair dealing;
  sufficient acknowledgement required; current-events reporting extends to
  broadcasts.
- **Parody, pastiche, caricature** (s.31A, added by CDPA 2014 amendment) —
  for parodying the original work; fair dealing required.

**There is no UK equivalent to the US four-factor fair use defence.** If the
use does not fit a specific permitted act under CDPA ss.28–76, it is likely
infringing. Flag the applicable permitted act if there is one.

### Online / platform considerations

UK copyright infringement online is actionable under CDPA 1988. For
takedown/notice-and-action, note:

- **UK Online Safety Act 2023** — creates new obligations on regulated platforms
  for illegal content (including copyright infringement in some cases). More
  relevant to the `/ip-legal-uk:takedown` skill.
- **EU Digital Services Act** — does NOT apply in UK (post-Brexit); EUIPO
  notices are separate from UK notices.
- **CDPA 1988 ss.97A / 99A** — High Court has jurisdiction to order injunctions
  against service providers to block access to copyright-infringing material.

### Moral rights (CDPA 1988 ss.77–89)

UK copyright includes moral rights: the right of paternity (s.77 — right to
be identified as author), the right of integrity (s.80 — right to object to
derogatory treatment), and the right against false attribution (s.84). Moral
rights cannot be assigned (only waived in writing under s.87). Flag moral rights
infringement as a separate head of claim if relevant.

### Output

Factors flagged; fair dealing / permitted act analysis with "the triage does
not conclude"; ownership / employed-works / assignment threshold notes.
Routing per posture.

---

## Patent mode

**Route to `/ip-legal-uk:fto-triage` for the detailed framework.** This mode is
the mirror image of the FTO skill — same claim charts, same *Actavis* equivalents
flag, same all-elements rule — applied to an accused product instead of one's own.

### Registered designs (UK) — branch before the workflow

If the right at issue is a UK registered design (Registered Designs Act 1949)
or UK supplementary unregistered design right (UK SUDR), the utility patent
workflow does NOT apply. Branch:

- **UK registered design.** The test is whether an informed user would form a
  different overall impression from the registered design and the accused design
  (RDA 1949 s.7(1), as amended; Design Regulation Articles 6, 10 of retained
  EU law). Do not build a utility patent claim chart.
- **UK unregistered design right (CDPA 1988 s.213).** Protects original designs
  of any aspect of the shape or configuration (internal or external) of the
  whole or part of an article. Infringement = copying the design.
- **UK supplementary unregistered design right (UK SUDR).** Based on the retained
  EU unregistered design right (post-Brexit); protects appearance for 3 years
  from first disclosure.
- **No direct EU unregistered design right coverage in UK** since 31 Dec 2020.

Route UK registered design and unregistered design right matters to a design
specialist; this skill's patent workflow does not apply.

### Utility patent workflow (PA 1977)

Assumes the right is a UK patent (national or EP designating UK). UPC matters
do NOT apply — the UK is not party to the UPC.

> **Patent systems differ by jurisdiction.** The UK claim chart (PA 1977,
> *Actavis* equivalents, IPEC / High Court damages) does not transfer to EU,
> US, or other systems.
> - **EU / UPC:** UPC does not cover UK.
> - **Germany:** bifurcated validity/infringement proceedings.
> - **US:** §284/§289 damages, doctrine of equivalents, IPR/PGR — different
>   from UK entirely.

### Workflow

- Accused product / process / method — described in technical detail.
- Identified patent(s) at issue — PA 1977 / EP(UK) designations.
- Claim chart for each independent claim: element-by-element mapping.
- Literal infringement first. *Actavis* equivalents as a flag (three questions
  from *Actavis UK Ltd v Eli Lilly* [2017] UKSC 48).
- Indirect infringement (PA 1977 s.60(2)) as a flag — contributory
  infringement by supplying means essential for putting the invention into
  effect.
- **Invalidity defences to consider** — lack of novelty (PA 1977 s.2), lack
  of inventive step (s.3), industrial applicability (s.4), excluded subject
  matter (s.1(2)), added matter (s.76), insufficient disclosure (s.14). Flag
  each; do not opine.
- **Unjustified threats (PA 1977 s.70).** As with trade marks, unjustified
  patent threats against secondary actors carry liability under PA 1977 s.70
  as reformed by the Intellectual Property (Unjustified Threats) Act 2017.
  Flag before any assertion recommendation.
- **Damages posture** — UK patent damages: compensatory (to put claimant in
  same position as if infringement had not occurred), or (at claimant's
  election) account of profits; additional damages for flagrant infringement
  under PA 1977 s.63. No punitive/treble damages in UK patent law.

### Output

Claim charts. Element flags. Invalidity and unjustified-threats defence flags.
Routing to Chartered Patent Attorney. See the `fto-triage` skill for the
full output structure.

---

## Trade secret / confidential information mode

UK trade secret law operates on two parallel tracks:

1. **English law of confidence** (*Coco v AN Clark (Engineers) Ltd* [1969] RPC
   41): (a) the information must have the necessary quality of confidence about
   it; (b) it must have been imparted in circumstances importing an obligation
   of confidence; (c) there must be an unauthorised use of that information to
   the detriment of the party communicating it.

2. **Trade Secrets (Enforcement, etc.) Regulations 2018 (SI 2018/597)** —
   implementing the EU Trade Secrets Directive (retained UK law post-Brexit):
   defines a "trade secret" (s.2 — secret, commercial value because of secrecy,
   reasonable steps taken to keep secret), defines misappropriation, provides
   remedies. The Regulations largely codify the existing law of confidence for
   trade secrets, but with clearer definitional frameworks.

### Was it a secret?

- **Not generally known** — to persons in the circles normally dealing with
  this kind of information.
- **Has commercial value** because of its secrecy.
- **Reasonable steps** were taken to keep it secret.
- **Combinations and compilations** — a combination of publicly available
  elements can still constitute a trade secret if the combination is not
  generally known.

### Obligation of confidence

Was the information imparted in circumstances importing an obligation of
confidence?

- Express contracts (NDAs, employment agreements, supplier agreements) —
  check scope and coverage.
- Implied obligation — certain relationships (employment, professional,
  commercial dealings) carry implied obligations of confidence.
- For employee matters: PA 1977 s.42 (employee invention secrecy obligations),
  implied duty of fidelity in employment, post-termination confidentiality
  covenants (governed by restraint of trade principles — must be reasonable in
  scope, duration, and geography to be enforceable).

### Misappropriation

Under Trade Secrets Regs 2018: acquisition by improper means (theft, bribery,
breach of a duty to maintain confidentiality, any other conduct contrary to
honest commercial practice).

- **Former employee fact pattern:** new employer, overlapping work, departure
  timing, documents taken (and returned?), access logs, assignment and
  confidentiality clauses in employment contract.
- **Springboard doctrine:** even if information has become partially public,
  a former employee who acquired it confidentially may be restrained from using
  it to gain a head start (*Terrapin v Builders' Supply Co (Hayes) Ltd* [1967]
  RPC 375; *Vestergaard Frandsen A/S v Bestnet Europe Ltd* [2013] UKSC 31).
- **Reverse engineering and independent derivation** — lawful under Trade
  Secrets Regs 2018 reg.4(2) and at common law.

### Output

Three flag groups — quality of confidence / obligation / misappropriation —
each with what cuts each way. Routing per posture.

---

## Output format (all modes)

Prepend the work-product header from
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER]

# Infringement Triage — [Trade Mark | Copyright | Patent | Trade Secret] (NOT A FINDING)

**This is a triage, not a finding of infringement or non-infringement.** The
triage identifies factors and flags what matters most; it does not conclude.
A conclusion requires a solicitor's or attorney's judgment on the facts, the
right scope, jurisdiction, and defences.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Posture and scope

- **Party posture:** [senior / accused]
- **Right at issue:** [trade mark / copyright / patent / trade secret]
- **Jurisdiction:** [England & Wales / Scotland / UK-wide / EU — note post-Brexit split]
- **Legal framework applied:** [cite the governing test and statute]
- **Limitation / laches clock:** [status — 6 years from accrual under Limitation Act 1980]
- **Exhibits / evidence reviewed:** [list]

## Factor analysis

[Mode-specific factor table — confusion factors / substantial-copying analysis /
claim chart / confidence elements. Each factor has a flag and a direction.
This is a flag list, not a verdict.]

## Defences and thresholds

[Mode-specific: dilution reputation threshold / originality / fair dealing
type / s.1(2) excluded matter / lack of novelty / lack of inventive step /
reasonable measures / reverse engineering / unjustified threats / limitation.
Flag each.]

## What cuts which way — summary

| Factor | Flag | Direction (senior / accused / mixed) |
|---|---|---|
| [factor 1] | [note] | [direction] |

**Conclusion:** *This skill does not conclude.* Solicitor/attorney judgment
required before acting. The factors cutting [direction] are [brief summary];
the factors cutting [direction] are [brief summary].

## Unjustified threats flag

[If relevant to this matter — trade mark TMA s.21 / patent PA s.70. Flag any
risk that proposed assertion targets secondary actors without a parallel primary
claim.]

## Recommended next steps

- [formal opinion from solicitor / attorney / route to IP OC named in the
  practice profile]
- [evidence preservation and legal hold — if a limitation clock is running]
- [fact development needed before a decision — access logs, prosecution history,
  market studies, goodwill evidence]
- [routing per practice profile `## Enforcement posture`, if the posture is
  to assert]

## Citation verification

Every case, statute, registration number, claim quote, and exhibit cited here
must be verified against the authoritative source before relying on it.
Post-Brexit, UK and EU IP law have diverged — confirm which jurisdiction's
law applies and which precedents remain binding.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Sending a C&D, deciding
> not to stop, filing proceedings, or relying on "it's fair dealing" based on
> this triage alone has legal consequences — including unjustified threats
> claims under TMA 1994 s.21 or PA 1977 s.70 (damages and an injunction against
> the threatening party), costs orders in IPEC or the High Court, and additional
> damages for flagrant patent infringement.
>
> Here's a brief to bring to a solicitor or Chartered Patent / Trade Mark
> Attorney:
>
> [Generate a 1-page summary: the right at issue, the posture, the facts and
> evidence, the factors surfaced, the defences flagged, the unjustified threats
> risk, and the three questions to ask.]
>
> To find an authorised professional in the UK: SRA register for solicitors;
> CIPA (cipa.org.uk) for Chartered Patent Attorneys; CITMA (citma.org.uk) for
> Registered Trade Mark Attorneys; Bar Council for barristers. For EU IP matters
> post-Brexit, you may need a professional qualified in the relevant EU member
> state or an EUIPO-qualified representative in addition to UK counsel.

Deliver the triage alongside the brief.

---

## Output location

If matter workspaces are enabled and a matter is active, write to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/matters/<matter-slug>/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/uk-legal-plugins/ip-legal-uk/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`
and surface the path.

---

## Handoff to enforcement skills

If the triage output points toward an assertion and the practice profile's
posture supports it, offer:

> Want me to draft a cease-and-desist on this? Run `/ip-legal-uk:cease-desist`.
> I'll use the flag list from this triage as the factual basis and apply the
> approval chain from your practice profile — the letter won't go anywhere
> without the approver signing off. Note: unjustified threats risk will also
> be surfaced in the C&D gate before any draft goes out.

Or, if the mode is copyright and the accused is hosted content:

> Want me to prepare a notice-and-action (UK Online Safety Act / platform
> takedown)? Run `/ip-legal-uk:takedown`.

Do not draft the letter automatically from the triage.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- **Conclude infringement or non-infringement.** Ever.
- **Substitute for survey evidence, damages experts, or claim construction.**
- **Evaluate jurisdiction-specific defences outside the triage's jurisdiction
  scope.** Post-Brexit: UK and EU IP systems are separate — UK and EU claims
  require separate analysis and separate proceedings.
- **Decide fair dealing as a matter of law.** UK fair dealing is narrower and
  purpose-specific — an attorney decides whether a particular use fits.
- **Draft the C&D, takedown, or claim form.** Those are separate skills
  (`/ip-legal-uk:cease-desist`, `/ip-legal-uk:takedown`) gated by the approval
  chain and the unjustified threats check.
- **Handle UPC proceedings.** The UK is not party to the UPC.

---

## Tone

Factor-by-factor, flag-by-flag. No hedging prose. The guardrail at the top
does the scope work; the analysis does the analysis. A solicitor or attorney
should leave the output knowing exactly which factors are flagged, which
defences apply, and what they need to do next.
