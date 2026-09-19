---
name: personas
description: Route persona work to the right skill - persona-interview to create or revise a persona, persona-interrogate to have saved personas judge a subject or answer questions in character. Use as the entry point for anything involving personas, or when another workflow needs to cast one.
license: MIT
---

# Personas

Pick the persona skill that fits the request, then run it. This skill routes; it does not do the
work itself.

A persona is a durable, user-authored simulation of a stakeholder, defined by its perspective:
what it knows and does not know, what it wants from the subject, and what a bad outcome costs it.
Personas live in the repository the skill is used in, under `docs/wizspec/personas/`, with an
index at `docs/wizspec/personas/README.md`.

## Skills

| Skill | Use it when |
| --- | --- |
| `persona-interview` | A persona has to be created or changed. Derives a draft from the repository, grills the user one question at a time, dry-runs the result on a real subject, and saves it. |
| `persona-interrogate` | Saved personas have to judge a subject or answer questions about it in character. Casts each in an isolated agent, collects findings and verdicts, confronts disagreements, and synthesises. |

## Routing

**Defining a person goes to `persona-interview`.** The signs are a request to add, describe, set
up, edit, or fix a persona, or a subject the user wants judged by someone who does not exist yet.

**Using a person goes to `persona-interrogate`.** The signs are a subject and a question about it:
does this hold up, what would they think, what would they try first, would they accept this.

**Both, in that order, when the request needs a persona that does not exist.** Check the index
first. `persona-interrogate` never invents a persona, so an interrogation with no matching persona
means an interview, then the interrogation.

**Neither, when the user only wants to know what personas exist.** Read the index and answer.

State which skill you picked and why in one sentence before you start, so the user can redirect
you before the work rather than after it.
