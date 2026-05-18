---
name: customize
description: >
  Guided customisation of your law-student-uk study profile — change one
  thing without re-running the whole cold-start interview. Adjust current
  modules, learning style, outline preferences, SQE/exam prep subjects, seed
  materials, or study session cadence. Use when the user says "change my
  [thing]", "add a module", "update my profile", "new term", or "customise".
argument-hint: "[section name, or describe what you want to change]"
---

# /law-student-uk:customize

## When this runs

The user typed `/law-student-uk:customize`. They want to change something in
their study profile — a module, a learning style preference, a qualification
exam subject — without re-running the whole cold-start interview and without
hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md`.
   If the plugin config does not exist or still contains `[PLACEHOLDER]`
   values, say:

   > You haven't run setup yet. Run `/law-student-uk:cold-start-interview`
   > first — customise is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Student profile** — name, institution, qualification route, jurisdiction
     (E&W / Scotland / NI), enrolled clinics or journals
   - **Current modules** — module name, lecturer, syllabus path, exam format
     (closed/open book, essay/problem/MCQ/mixed), seminar cold-call style
   - **Learning style** — Socratic vs. summary, how much pushback you want,
     whether the plugin rewrites your work or only critiques structurally
   - **Outline preferences** — outline format (IRAC/CILAC/problem-question
     briefing style), level of rule detail, whether to include policy discussion,
     saved outline templates
   - **SQE / exam prep** — which assessment (SQE1 FLK1/FLK2 / SQE2 / BPTC /
     LLB finals / DPLP), subjects in rotation, weak-subject flagging,
     MCQ vs. essay cadence
   - **Seed materials** — casebook paths, prior outlines, graded essays, old
     exams, SQE1 question sets, module guides, papers
   - **Study workflow** — session length, flashcard Leitner bucket schedule,
     exam forecast cadence, cold-call prep timing
   - **Integrations** — document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new module:* "`/law-student-uk:outline-builder` will scaffold a new outline for this module. `/law-student-uk:flashcards` will add a new subject bucket. `/law-student-uk:cold-call-prep` will ask for a case and a topic when you invoke it for this module."
   - *Learning style Socratic → summary-first:* "`/law-student-uk:socratic-drill` won't ask you to answer first — it'll present the rule and example, then quiz you on application."
   - *Adding an SQE1 subject:* "`/law-student-uk:bar-prep-questions` will include this subject in rotation and weight it higher if you mark it weak."
   - *Changing jurisdiction from E&W to Scotland:* "All skills will now default to Scots law frameworks and flag where Scots law diverges from English law. Check that your outline subjects are Scots-law versions."

5. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/law-student-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a module, offer to
  mark it `[Archived — retain seed materials]` and explain what flashcard
  and outline behaviour changes.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., "summary-first" learning style + "maximum pushback"
  Socratic setting), flag the tension.
- **Flag guardrail degradation.** The "no rewriting your writing" rule on
  `/law-student-uk:legal-writing` and `/law-student-uk:irac-practice` is
  load-bearing — the value of the skill is structural feedback, not
  ghost-writing. If the user asks to turn that off, confirm they understand
  that the plugin will not write their work for them.
- **Jurisdiction change.** If the user changes their jurisdiction (e.g., from
  E&W to Scotland), warn: "Changing jurisdiction to Scotland will mean skills
  default to Scots law. If you have existing outlines written for English law,
  they will need to be re-checked for Scots law accuracy. Do you want to
  proceed?"
- **One change at a time.** Don't re-ask the whole interview.
