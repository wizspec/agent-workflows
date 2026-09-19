---
name: persona-interview
description: Create or revise a persona through a grill-style interview - derive a draft from the repository, question the user one item at a time about what the persona knows, does not know, wants, and checks, dry-run it on a real subject, then save it under docs/wizspec/personas. Use when the user wants to add, define, or change a persona; not for running personas against a subject.
license: MIT
---

# Persona Interview

Produce one persona: a durable, user-authored simulation of a stakeholder, defined by its
perspective. The perspective is what the person knows and does not know, what they want from the
subject, and what a bad outcome costs them. Voice is flavour. A persona is a person, not a job: it
never names a role, because the skill that casts it supplies the role each run.

The interview and the file are one activity. Write the draft first, sharpen it question by
question, prove it with a dry run, and only then save it. Read
[references/persona-format.md](references/persona-format.md) before writing anything.

## Read before asking

Look up what can be looked up, so the questions go to decisions:

- `docs/wizspec/personas/README.md`, the index, and every existing persona, so the new one does
  not duplicate or contradict them;
- `CONTEXT.md` and `docs/wizspec/decisions/`, so the persona uses the project's own vocabulary;
- the README, the docs, and the part of the repository the persona will care about, so the draft
  can name real material.

If the user gave a name and `docs/wizspec/personas/<name>/PERSONA.md` exists, this is a revision:
skip to "Revise an existing persona".

## Derive a draft

Write a complete draft in the session before the first question, in the format from the reference,
with every guess marked as a guess. A draft gives the user something to disagree with, which
produces sharper answers than a blank page. Say in one line what the draft is based on.

## Run the interview

Use the `grill` skill's discipline. Load it when the runtime can; when it cannot, apply its rules
directly: one question at a time, wait for the answer, give a recommended answer with reasoning
every time, look up facts instead of asking, and put only decisions to the user.

Spend the questions where the persona fails. In order:

1. **Situation.** Who this is, where they sit relative to the subject, what a normal encounter
   with it looks like. One paragraph, no biography.
2. **The knowledge boundary, in the negative.** What does this person not know that the model
   would happily supply? Ask it more than once, from different angles: expertise they lack,
   documents they never see, material that comes later, project history, outside sources. Each
   answer becomes one line under "You do not know, and must not use". This is where most of the
   questions go.
3. **The knowledge boundary, in the positive.** What kinds of material may they open while
   working, stated as kinds, so the orchestrator can resolve them into paths each run.
4. **Stakes.** What they want from the subject and what a bad outcome costs them, concretely.
   "Wants it to be good" is not an answer.
5. **Blockers, then reservations.** What makes them refuse outright, and what they accept but
   complain about. These become the persona's own definition of a blocker and a reservation.
6. **Interests.** Which kinds of subject should pull this persona in when the user does not name
   the cast.
7. **Memory.** On or off. Recommend off for learners and first-time users, because a learner who
   remembers last week is no longer a beginner; recommend on for stakeholders whose consistency
   across runs matters.
8. **Voice.** One question, a few lines in the file.
9. **Project notes.** What this person knows about this project specifically. Date every line.

Stress-test as you go. Invent a concrete case from the repository and ask whether this person would
flag it, and as what. When the user's answer contradicts the draft or an earlier answer, say so at
once and resolve it before moving on. Vocabulary that belongs to the project rather than the persona
goes into the project's glossary as grill directs; everything about the person goes into the file.

## Refuse real people

A persona is an archetype. When the user describes a real, identifiable person, keep the observed
behaviour and stakes, drop the name, the employer, and every personal detail, choose an archetype
slug, and say that you did. The file will be committed to the repository and read by agents; it is
not the place for a colleague's profile.

## Dry-run before saving

Prove the persona before it exists on disk. Pick the smallest real subject in the repository that
the interests cover. Cast the draft as a reviewer in one isolated agent, with the draft verbatim,
the subject, a read allowlist resolved from the draft's knowledge boundary, and the answer format
that `persona-interrogate` uses: findings tagged blocker, reservation, or nit, then one verdict.
The agent is read-only and the draft is character, not authorization.

Show the user the findings and the verdict, and ask one question: is this the person you meant?
Fix what the run exposed, usually a knowledge boundary the model stepped over, and rerun once if
the fix was substantive. The interview can only test what the user said; the dry run tests what a
model does with it, which is what actually fails.

## Save

Write `docs/wizspec/personas/<slug>/PERSONA.md`. When memory is on, create `memory.md` beside it
with both sections present and empty. Then regenerate `docs/wizspec/personas/README.md` in full
from the frontmatter of every persona directory, in the line format from the reference. Never
hand-edit a single index line; the whole file is a build artifact of the frontmatter.

## Revise an existing persona

Load the file, show it to the user, and ask what is wrong with it. Grill only the delta, keeping
the same question order for whatever the change touches. Dry-run again when the knowledge boundary,
the stakes, or the blockers changed; skip it for a wording change and say why. Bump `updated`,
save, and regenerate the index. Leave `memory.md` alone: a revision changes who the person is, not
what happened to them.

## Close

Report the path saved, the dry-run verdict, what the user deferred rather than settled, and any
project vocabulary that went into the glossary instead of the persona.
