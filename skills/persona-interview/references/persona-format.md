# Persona file format

Personas live in the repository the skill is used in, never in the skill itself.

```
docs/wizspec/personas/
  README.md                  the index, regenerated from frontmatter on every save
  <slug>/
    PERSONA.md               the persona
    memory.md                only when memory is on
```

The slug is a kebab-case archetype such as `beginner-student`, `skeptical-cto`, or
`on-call-operator`. It is never a real person's name.

The `persona-interrogate` skill reads the frontmatter fields, the section headings, and the memory
sections by name. Rename them in both skills or not at all.

## PERSONA.md

Write the body in second person: the file is handed to an agent as the description of who it is.

```md
---
name: beginner-student
summary: First-time assembly learner working through the course in order.
interested-in:
  - lecture prose and exercises
  - anything a learner meets before the course-opening lecture
memory: false
updated: 2026-09-19
---

# Beginner student

## Who you are

One paragraph of situation: what you do, where you sit relative to the subject, what a normal
encounter with it looks like. Not a biography.

## What you know, and what you do not know

### You know

- Kinds of material you have met, with the caveat that you have met them, not mastered them.
- Kinds of material you may open while working, stated as kinds ("earlier accepted lectures"),
  which the orchestrator resolves into paths for each run.

### You do not know, and must not use

- Each thing the model could supply that this person would not have: expertise, internal
  documents, later material, project history, outside sources. Stated in the negative, one per
  line. This is the section that makes the persona worth having.

## What you want, and what failure costs you

What you want from the subject, and what a bad outcome costs you, concretely.

## What you check

### Blockers

- Each thing that makes you refuse outright. A finding that matches one of these is a blocker.

### Reservations

- Each thing you would accept but insist on complaining about. A finding that matches one of
  these is a reservation. Everything smaller is a nit.

## How you talk

A few lines at most. Flavour, never the point.

## Project notes

- 2026-09-19: A fact about this project that this person holds, dated so staleness shows.
```

Frontmatter fields:

- `name`: the slug; must match the directory.
- `summary`: one sentence, reused verbatim in the index.
- `interested-in`: the kinds of subject that should pull this persona in when the user does not
  name the cast. Short phrases, one per line.
- `memory`: `true` or `false`. Off for learners and first-time users unless the user insists,
  because a learner who remembers last week is no longer a beginner.
- `updated`: the date of the last save.

## memory.md

Created only when `memory: true`, with both sections present even while empty. Written by the
orchestrator at the end of a run and never by the persona itself.

```md
# Memory: beginner-student

## Standing positions

- 2026-09-19: A view held across runs, or one the user said to keep, in one line.

## Run log

- 2026-09-19 · docs/lectures/03-registers.md · reviewer · draft · REJECT · top objection: uses
  the stack before it is introduced · user decision: rewrite ordered
```

Standing positions are loaded every time the persona is cast. Run log lines are loaded only when
the same subject returns, or on request, and are presented to the persona as context, not as a
grade. Keep standing positions to a handful of lines; append log lines without editing old ones.

## README.md, the index

One line per persona, regenerated in full from every `PERSONA.md` frontmatter whenever a persona
is saved, so it cannot drift. Consumers read this first and open a persona's own file only when
casting it or deciding whether to.

```md
# Personas

One line per persona, regenerated from frontmatter whenever a persona is saved. Read this first;
open a persona's `PERSONA.md` only when casting it or deciding whether to.

- [beginner-student](beginner-student/PERSONA.md): First-time assembly learner working through
  the course in order. Interested in: lecture prose and exercises; anything a learner meets before
  the course-opening lecture.
- [skeptical-cto](skeptical-cto/PERSONA.md): Owns the budget and the outage pager for whatever
  ships. Interested in: architecture proposals; anything that adds a runtime dependency. Memory on.
```

The line format is the summary, then `Interested in:` with the interests joined by semicolons, then
`Memory on.` only when memory is on.
