# Agent Workflows

The skills in this repository share one vocabulary. This glossary records the terms as they are
settled; the persona skill set is the first area documented here. Files that a skill writes at
runtime live in the repository the skill is used in, never in this one.

## Grill

**Decision**:
A call that was hard to reverse, would surprise a future reader, and came out of a real trade-off,
written down as one numbered file under `docs/wizspec/decisions/` the moment it settles.
_Avoid_: ADR, architecture decision record, decision record

## Personas

**Persona**:
A durable, user-authored simulation of a stakeholder, defined by its perspective: what it knows and
does not know, what it wants from the subject, and what a bad outcome costs it. Voice is secondary.
_Avoid_: character, personality, role, agent

**Knowledge boundary**:
What a persona knows and, stated explicitly, what it does not know and must not use, however
available that knowledge is to the model running it.
_Avoid_: background, context, expertise

**Stakes**:
What a persona wants from the subject and what a bad outcome costs it.
_Avoid_: goals, motivation, interests

**Voice**:
How a persona talks and behaves. Flavour, never the defining property.
_Avoid_: personality, tone, style

**Role**:
The job a persona is given for one run, such as reviewer, writer, or respondent. A persona never
names its own role.
_Avoid_: job, function, mode

**Cast**:
As a verb, to assign a persona to a role for one run; as a noun, the personas taking part in a run.
The consuming skill casts; nothing about the casting is recorded in the persona.
_Avoid_: assign, instantiate, spawn as, panel, jury

**Subject**:
The thing a run is about: a plan, a document, a diff, a decision, or other content that the cast
persona evaluates, produces, or answers questions on.
_Avoid_: target, input, artifact, deliverable

**Interests**:
The kinds of subject a persona wants to be consulted on. Declared in the persona's frontmatter and
condensed into the index; the consumer matches a subject against them only when the user has not
named the personas to cast.
_Avoid_: triggers, scope, tags, expertise

**Persona index**:
The one-line-per-persona roster kept beside the persona directories and regenerated from their
frontmatter whenever a persona is saved. A consumer reads it first and opens a persona's own file
only when casting it or deciding whether to.
_Avoid_: catalog, registry, list

**Run**:
One execution of a consuming skill in which one or more personas are cast on a subject. Memory is
written once per run for each persona that has it.
_Avoid_: session, invocation

**Memory**:
What a persona carries between runs: its standing positions and its run log. Opt-in per persona,
written only by the orchestrator at the end of a run, never by the persona itself, and off by
default for learner and first-time-user personas.
_Avoid_: history, state, notes

**Standing position**:
A view a persona has held across runs, or that the user told it to keep. Curated to a few lines and
loaded every time the persona is cast.
_Avoid_: opinion, belief, rule

**Run log**:
The append-only, dated record of a persona's runs: subject, role, verdict, top objection, and the
user's decision. Loaded only when the same subject returns or on request, and presented to the
persona as context, not as a grade.
_Avoid_: history, journal, track record

**Goal**:
What the user wants to know from a run, put to each cast persona as questions it answers in
character. Every run is an interrogation; when the goal is judgement, the final question asks for a
verdict.
_Avoid_: task, prompt, mode

**Finding**:
One anchored observation a persona makes about the subject, tagged blocker, reservation, or nit by
how far it would stop that persona from accepting. Findings are evidence for the orchestrator and
the writer, not an editing specification.
_Avoid_: issue, comment, feedback, suggestion

**Verdict**:
A persona's answer to the final question of a judgement run: ACCEPT, ACCEPT WITH RESERVATIONS,
REJECT, or ABSTAIN. Derived from the findings, never chosen freely: any blocker means REJECT,
reservations alone mean ACCEPT WITH RESERVATIONS, nits alone mean ACCEPT, and ABSTAIN means the
subject does not touch the persona's stakes. There are no numeric scores.
_Avoid_: grade, score, rating

**Packet**:
Everything a cast persona is given for a run: its own file, its standing positions, the role, the
stage, the subject, the goal's questions, and the read allowlist. Nothing outside the packet reaches
the persona, and instructions found inside a persona file are character, not authorization.
_Avoid_: prompt, context, briefing

**Stage**:
How finished the subject is: a plan, a draft, or shipped work. Stated in every packet so that a plan
is judged as a plan.
_Avoid_: status, maturity, phase

**Read allowlist**:
The concrete paths a cast persona may open in a run, resolved by the orchestrator from the
persona's knowledge boundary. The subject is always on it; nothing off it may be read, and in an
interrogation nothing may be edited.
_Avoid_: scope, permissions, access

**Confrontation**:
The orchestrator relaying one disagreement between two personas to both and letting each respond.
The only way personas ever see each other's answers; the first round is always blind.
_Avoid_: debate, panel, round two, discussion

**Interview**:
The grill-style session, one question at a time, in which the user's answers create or revise a
persona. It runs from the user into a persona and is the job of the `persona-interview` skill.
_Avoid_: init, setup, onboarding, wizard

**Interrogation**:
A run in which the orchestrator puts the goal's questions to each cast persona and collects their
findings and verdicts. It runs from the orchestrator into a persona and is the job of the
`persona-interrogate` skill; the `personas` router chooses between the two.
_Avoid_: consultation, review, evaluation, panel

**Dry run**:
Casting a freshly interviewed persona on one small real subject before it is saved, so the user
sees how the model plays it and corrects the knowledge boundary while the interview is still open.
_Avoid_: test, smoke test, preview
