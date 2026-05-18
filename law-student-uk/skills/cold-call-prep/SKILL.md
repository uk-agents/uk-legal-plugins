---
name: cold-call-prep
description: >
  Prep for a seminar cold-call — predict the lecturer's likely questions and
  drill them Socratically, flagging where you're shaky so you know what to
  re-read before the session. Use when the user says "prep for seminar
  tomorrow", "cold call [case]", "what might [lecturer] ask on", or points
  at assigned reading.
argument-hint: "[case name, or paste case text, or path to reading]"
---

# /law-student-uk:cold-call-prep

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → module list, lecturers, learning style.
2. Apply the workflow below.
3. Identify reading (case name + OSCOLA citation, lecturer, module, syllabus context).
4. Predict 6-10 likely questions across categories (Facts / Holding / Reasoning / Application / Policy), weighted to lecturer's known tendencies.
5. Drill using Socratic pattern — ask, wait, push back, narrow when stuck. Don't give answers.
6. Post-drill summary: strong/shaky/missed; what to re-check before class.

---

## Real-matter check

If the question the student is asking sounds like it's about a REAL situation — their lease, their parking ticket, their family's business, their friend's arrest, a real pound amount, a real deadline, a real party name — stop.

> "This sounds like a real situation, not a hypothetical. I can't give you legal advice, and you can't give it either — you're not a solicitor or barrister yet. If this is real, [the person] needs an actual solicitor or barrister: Citizens Advice, your law school clinic, your jurisdiction's legal aid provider, or (if there's money) a private solicitor or barrister. I'm happy to help you understand the general legal concepts involved, but that's study, not advice."

Watch for: real names, real addresses, real dates, specific pound amounts, "my landlord/boss/parent/friend," "I got a letter/notice/claim," deadlines measured in days. Any one of these is a trigger.

## Purpose

Cold-calling in UK law seminars lives or dies on preparation. The seminar leader has read the case dozens of times and knows the questions; the student has read it once. This skill narrows the gap — predicts the likely question patterns for the case, drills the student on them, and surfaces what they haven't locked in.

Not a replacement for reading the case. A test that you actually did.

## Confidence discipline

- When the student provides case text or casebook excerpts: I predict questions based on the actual text. Confident.
- When the student provides only a case name: I predict based on what I know about the case. Flag `[UNCERTAIN]` on any question that depends on case details I'm not sure of. Strongly recommend the student pastes the case or casebook treatment first.
- If I don't know the case well: say so. "I don't have a reliable read on this case — paste the text or casebook treatment and I can work from that. Otherwise my questions are educated guesses."

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → current modules, lecturers, learning style
- User-provided: case name / case text / casebook pages / reading list

## Workflow

### Step 1: Identify the reading + lecturer

- Case name and OSCOLA citation (e.g., *Caparo Industries plc v Dickman* [1990] 2 AC 605)
- Lecturer (from `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` module list — tone and focus vary by lecturer)
- Module / subject area
- Where this case falls in the syllabus (for context — is this the first case on the topic, a narrowing case, a counterexample?)

### Step 2: Predict the questions

Lecturers in UK seminars cold-call in recurring patterns. Predict across these categories:

**Facts-level (warm-up):**
- Who are the parties? What happened? Procedural posture?
- What did the court below decide? The Court of Appeal? The House of Lords / Supreme Court?
- Why is this in the casebook? What doctrine is it illustrating?

**Holding / rule:**
- What's the holding? One sentence.
- What's the rule that comes out of this case — the portable takeaway?
- How would you phrase the rule in your outline?

**Reasoning:**
- Why did the court decide this way?
- What arguments did the court reject?
- Was there a dissent? What did it argue?
- What obiter dicta does the case contain?

**Application / hypos:**
- What if [fact X] were different — same outcome?
- How does this case compare to [prior case in the syllabus]?
- What's the limiting principle? Where does this rule stop?
- Is this case consistent with the previous line of authority?

**Policy / theory:**
- What's the policy the court is protecting?
- Does this rule make sense? Alternative approaches?
- Does a law journal article (cite one from the module reading list) challenge this approach?

**Lecturer-specific flavour (from `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` notes):**
- If the lecturer is known for hypo-heavy sessions, weight Application/Hypo questions
- If policy-heavy, weight Policy/Theory
- If fact-heavy Socratic (Paper Chase style), weight Facts + Holding

Pick 6-10 questions across these categories. Rank by likelihood of being asked first (Facts usually go first, then Holding, then the harder categories).

### Step 3: Drill

Use the `socratic-drill` pattern:

1. Ask Question 1. Wait for answer.
2. If right + well-reasoned: acknowledge, move to Question 2.
3. If right but sloppy: don't let it slide. "You got there, but explain — why does the court's reasoning support that?"
4. If wrong: don't give the answer. Ask a narrowing question. "What facts does the court rely on?" Walk them to it.
5. If stuck: narrow further. "Before we go to the holding — what's the procedural posture?"
6. If genuinely lost: tell them to re-read the case. "This is a re-read, not a guess-your-way-through. Come back when you've read it again."

### Step 4: Post-drill summary

At the end:

```markdown
# Cold-Call Prep — [case] — [date]

**Questions drilled:** [N]
**Strong:** [questions where they were confident + right]
**Shaky:** [questions where they guessed or hedged]
**Missed:** [questions where they didn't know]

## Before seminar tomorrow:
- [specific thing to re-check — facts they got wrong, rule they couldn't state]
- [if shaky on policy/theory: "read the dissent again — that's usually where policy questions come from"]
- [if shaky on OSCOLA citation: "confirm cite against BAILII: www.bailii.org"]

## Questions likely to come up in seminar:
- [top 3 of the 10 — the ones the lecturer is most likely to lead with]
```

## Integration

- **case-brief:** if the student hasn't briefed the case yet, offer to run `/law-student-uk:case-brief` before cold-call prep. A brief is a cold-call prep tool too.
- **socratic-drill:** if prep surfaces a weak spot in the subject (not just this case), follow with `/law-student-uk:socratic-drill [subject]`.
- **flashcards:** if the case's rule is one the student should memorise, offer to add to the flashcard deck.

## What this skill does not do

- **Be the lecturer.** The actual seminar can go anywhere. This skill predicts patterns; lecturers surprise.
- **Replace reading the case.** If you haven't read it, the skill can't help you — questions require text you've absorbed.
- **Give you the case's holding without asking you first.** Drill-me pattern: I ask, you answer.
- **Predict jurisdiction-specific niche questions.** If the lecturer has known hobby horses, capture them in `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` module notes and the skill can weight accordingly; otherwise, it works from general patterns.
