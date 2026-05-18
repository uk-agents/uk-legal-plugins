# Law Student UK Plugin

Learning mode, not answer mode. Socratic drilling that asks YOU questions and pushes back on sloppy reasoning. Case briefing, outline building, flashcards, IRAC/CILAC grading, cold-call prep, writing feedback that never rewrites for you, and exam forecasting from past lecturer exams. Calibrated to you — your modules, your qualification route, whether you want to be drilled or scaffolded.

Built for the UK legal education system: LLB, GDL (Graduate Diploma in Law / CPE), SQE1/SQE2, BPTC (Bar Professional Training Course), CILEx, and the Scottish Diploma in Professional Legal Practice (DPLP). Citations follow OSCOLA. Cases sourced from BAILII and legislation from legislation.gov.uk.

**Every output is a study scaffold, not a model answer. The plugin structures your thinking, drills you Socratically, and flags what you got wrong. It doesn't write the outline, the brief, or the essay for you — that would defeat the purpose. Citations in study materials are tagged for verification.**

## Who this is for

Law students and qualification-route students in England & Wales, Scotland, and Northern Ireland. LLB Year 1 through SQE2 prep and bar (BPTC) preparation.

## UK legal education landscape

**England & Wales qualification routes:**

| Route | Stages | Notes |
|---|---|---|
| **SQE** (solicitor) | LLB or GDL → SQE1 (FLK1 + FLK2 MCQ) → SQE2 (skills) → 2 years QWE | Main new route since 2021 |
| **LPC** (legacy solicitor) | LLB or GDL → LPC → Training Contract (2 years) | Still active for those who started before SQE |
| **Bar** (barrister) | LLB or GDL → BPTC → Pupillage (1 year) | Called to the Bar by an Inn of Court |
| **CILEx** | CILEx Level 3/6 → Fellow → Practising certificate | Paralegal-to-qualified route |
| **Solicitor Apprenticeship** | Degree-level apprenticeship (no law degree needed) | 6 years, employer-sponsored |

**Scotland:** LLB (Scots law, 4 years) → DPLP → 2-year traineeship → Scots solicitor roll. Advocates: LLB → DPLP → devilling (pupillage equivalent). Scots law is a distinct mixed civil/common law system — contract, delict, and property law diverge materially from English law.

**Northern Ireland:** Separate Law Society of Northern Ireland and Bar of Northern Ireland routes, broadly similar to E&W but distinct. NI-specific statutes apply.

## First run: cold-start

This one's about you, not an org. Your modules, your qualification route, your learning style — drill-me vs. explain-to-me. Bring materials: past outlines, graded essays, old exams (especially same-lecturer), SQE1 practice question sets, module guides, papers. Ten to twenty items is the target; below that the practice profile is flagged `LIMITED DATA` and downstream skills will be thinner until more is added.

```
/law-student-uk:cold-start-interview
```

## Skills

Every skill is invoked as `/law-student-uk:<skill-name>`.

| Skill | Does |
|---|---|
| `/law-student-uk:cold-start-interview` | About-you interview + materials intake — modules, qualification route, learning style, materials |
| `/law-student-uk:socratic-drill [subject]` | Socratic drilling — it asks, you answer, it pushes back. Does not give the answer. |
| `/law-student-uk:case-brief [case]` | Case brief in your preferred format — OSCOLA citation, UK court hierarchy |
| `/law-student-uk:outline-builder [subject]` | Build or extend an outline in your format from class materials |
| `/law-student-uk:bar-prep-questions [subject]` | Exam prep questions — SQE1-style FLK MCQ or essay — jurisdiction-aware (E&W / Scots / NI), flags majority vs. jurisdiction-specific rule |
| `/law-student-uk:flashcards [subject]` | Generate or drill flashcards; Leitner-style buckets; per-subject markdown; `--session <n>` mode |
| `/law-student-uk:study-plan` | Build or update a long-term study plan — phases, subjects by weakness, adaptive daily schedule from session history |
| `/law-student-uk:session <subject> <n>` | Focused N-question session on a subject; updates the plan with results |
| `/law-student-uk:irac-practice` | Grade your IRAC/CILAC essay — structure, issues, rules, analysis. Tracks patterns across sessions. Never rewrites. |
| `/law-student-uk:cold-call-prep [case]` | Prep for seminar or cold-call — predict lecturer questions and drill them |
| `/law-student-uk:legal-writing [path-or-paste]` | Structural feedback on any draft — never rewrites, ever |
| `/law-student-uk:exam-forecast [module]` | Analyse past exams from same lecturer; forecast upcoming |

## UK citation style: OSCOLA

This plugin uses OSCOLA (Oxford University Standard for Citation of Legal Authorities) — the UK standard citation format used in all UK courts, law schools, and legal publications. There is no Bluebook in UK legal education.

**Case citation format:** *Case Name* [year] court report abbreviation page — e.g., *Donoghue v Stevenson* [1932] AC 562; *Caparo Industries plc v Dickman* [1990] 2 AC 605.

**Legislation citation format:** Act Name year, s section — e.g., Companies Act 2006, s 172; Equality Act 2010, s 4.

**BAILII** (British and Irish Legal Information Institute) is the free online UK case law database — equivalent to CourtListener for US law. All UK Supreme Court, Court of Appeal, and High Court judgments are freely available.

## IRAC and CILAC

UK law schools use IRAC (Issue, Rule, Application, Conclusion) in a form essentially identical to the US version. Some institutions and the SQE use "CILAC" (Context, Issue, Law, Application, Conclusion) as a variant that adds an introductory context paragraph. The plugin grades either structure; specify which your institution uses in your practice profile.

Problem questions (hypos applying law to facts) are the dominant exam format in UK law schools at all levels. Essay questions (discussing/critically evaluating doctrine or policy) are the second main format. Both are drilled here.

## SQE1 and SQE2

**SQE1** consists of two multiple-choice sittings (FLK1 and FLK2). Subject coverage:

- FLK1: Business Law and Practice, Dispute Resolution, Contract, Tort, Legal System of England and Wales, Constitutional and Administrative Law, EU Law, Human Rights
- FLK2: Property Practice, Wills and Intestacy, Probate Administration and Practice, Solicitors Accounts, Land Law, Trusts, Criminal Law and Practice

**SQE2** consists of six skills assessments: client interview and attendance note, legal research, legal writing, advocacy/persuasive writing, case and matter analysis (written advice), and case and matter analysis (oral). The bar-prep-questions and irac-practice skills cover both SQE1 MCQ practice and SQE2 written task practice.

## What "learning mode" means

Several skills here (socratic-drill, case-brief in drill-me mode, cold-call-prep, irac-practice, legal-writing) are deliberately built to *not* give you the answer or write the thing for you. The point is that you learn by doing. If you want an answer or a draft, use a different tool. This plugin is for the struggle.

**legal-writing is the strictest.** It reads your draft and tells you what's weak, but does not rewrite. Asking it to rewrite will return a polite refusal plus an offer of more specific structural feedback. This is a feature.

**outline-builder and case-brief follow the same rule in a softer form.** Outline builder scaffolds — topic tree, sub-topic slots, case placeholders — and asks Socratic questions as you fill the rules from your own notes and casebook. It won't generate a populated outline from a module guide alone. Case brief works the same way in every mode (drill-me and explain-to-me both): the skill gives the template and pushes back on what you wrote; it doesn't brief the case for you. If you paste the case text, it can extract the court's own language into the slots — that's pointing at the source, not writing for you.

## Academic integrity

Before using this plugin on any graded work — take-home exams, graded writing assignments, journal notes, papers — check your institution's honour code and your lecturer's module handbook policy on AI tools. Many institutions prohibit or restrict AI use on graded work, and the rules vary by module and lecturer. This plugin is designed for study and practice; using it where your institution prohibits it is an academic misconduct issue, and the consequences are yours, not the tool's. When in doubt, ask your lecturer in writing.

The learning-mode skills here (socratic-drill, irac-practice, legal-writing, cold-call-prep) are deliberately designed to not give you the answer or write the thing for you — that's the pedagogy. It's also the design assumption behind treating some permitted uses (unassisted-looking practice drilling) differently from prohibited ones (ghostwriting a graded memo). Don't work around the guardrails.

## Confidence markers

Content-generating skills flag their confidence inline. A rule statement or card without a marker is something the skill is confident on (but still not a substitute for your own source-checking before an exam). Markers used across the plugin:

- `[VERIFY: claim — check source]` — stated as likely correct, but you should confirm against your outline, casebook, prep course materials, or the primary source before relying on it. Used liberally in bar-prep-questions, case-brief, flashcards, legal-writing, irac-practice.
- `[UNCERTAIN: specific reason]` — the skill is not confident on this specific call (minority rule, debatable issue-spot, jurisdiction the skill doesn't know well). Make your own judgment; check the source.
- `[GAP — fill from class notes]` — outline-builder marker for a topic where the skill has no reliable source and won't invent a rule. You fill it from your notes.
- `[NEEDS CASES — rule stated but no illustrating case]` — outline-builder marker where the rule is there but the case illustration is missing.
- `[CHECK CLASS NOTES — lecturer may have emphasised something here]` — outline-builder marker for areas where lecturer-specific emphasis matters and the skill can't know it.
- `[EXCEPTION UNCLEAR — casebook mentions an exception, find the rule]` — outline-builder marker for a known exception with unresolved detail.
- `[UNCERTAIN — framing]` — exam-forecast marker noting that a forecast is a weighting for study time, not a prediction.

Trust the flags more than the absence of flags — an unflagged rule is something the skill is confident on, but exam prep still demands source-checking.

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors in this plugin aren't just data sources — they're the difference between a verified citation and a citation you have to check. Citations retrieved through the **uk-legal MCP** (legislation.gov.uk, TNA Find Case Law, OSCOLA citation parsing) or **govuk MCP** (government guidance, SRA/BSB regulatory material) are tagged with their source and can be traced back. Citations from the model's knowledge are tagged `[verify]` or `[model knowledge — verify]` and should be checked against BAILII, legislation.gov.uk, or your casebook before anyone relies on them.

## Storage

Your practice profile is stored at `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` and survives plugin updates. Everything else is in your working directory:

```
law-student-uk/
├── flashcards/
│   └── [subject]/cards.md             # per-subject flashcard decks
├── irac-sessions/
│   └── [student]/
│       ├── [date]-[topic].md          # individual session feedback
│       └── tracker.md                 # cross-session pattern tracking
├── writing-feedback/
│   └── [student]/
│       ├── [date]-[assignment].md     # individual session feedback
│       └── tracker.md                 # cross-session pattern tracking
└── exam-forecasts/
    └── [module]/
        └── forecast-[YYYY-MM-DD].md   # versioned forecasts
```

## How it learns

Your study profile at `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Notes

- Drill-me vs. explain-to-me is set at cold-start; switch per session.
- Case briefs and outlines use YOUR format. If you have existing outlines, point cold-start at them.
- SQE1 prep targets your weak FLK subjects from `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md`. It will keep coming back to them.
- Scotland: skills will flag where Scots law diverges from English law (contract, delict, land, criminal). If you are studying Scots law, set your jurisdiction in the practice profile.
- Every content-generating skill flags when it's uncertain. Trust the flags more than the absence of flags — an unflagged rule is something I'm confident on; check your source anyway before an exam.
