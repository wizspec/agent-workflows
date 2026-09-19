---
name: wizspec
description: Route a request to the skill in this repository that fits it. Use as the entry point when it is unclear which skill applies, or when one workflow needs to hand off to another.
license: MIT
---

# Wizspec

Pick the skill in this repository that fits the request, then run it. This skill routes; it does not
do the work itself.

## Skills

| Skill | Use it when |
| --- | --- |
| `grill` | A plan, design, or decision is still unsettled and has to be interrogated until it holds up. Produces shared understanding, a `CONTEXT.md` glossary, and a written decision for each call that was genuinely hard. |
| `document-writing-orchestrator` | A substantial document has to perform a real job for a real reader. Produces the document through a writer and a reviewer drawn from that job, with sources tracked and claims checked against them. |
| `personas` | The request is about personas: creating or revising one, or casting saved ones to judge a subject or answer in character. Routes on to `persona-interview` or `persona-interrogate`. |

## Routing

Ask what the request is short of, and route on that.

**Unsettled thinking goes to `grill`.** The signs are that the user cannot yet state the decision,
uses a term two ways in consecutive sentences, or has not faced the trade-off the plan turns on.
Drafting now would commit prose to choices nobody has made.

**A deliverable that has to work on someone goes to `document-writing-orchestrator`.** The signs are
a named reader, an evaluator, or an action the document must produce — a proposal, a runbook, a
policy, a report, a guide. The thinking is settled enough that the remaining risk is in the writing.

**Anything persona-shaped goes to `personas`.** The signs are the word persona, a stakeholder the
user wants simulated, or a subject to be judged by the people it affects rather than by a reviewer
derived on the spot. That router decides between defining a persona and interrogating one.

**Grill first, then `personas`, when the user wants a settled plan judged by the people it
affects.** Grill settles the vocabulary and the hard calls; the interrogation then tests the result
against each persona's stakes. Interrogating an unsettled plan produces findings about choices
nobody has made.

**Both, in that order, when the user asks for a document about something they have not decided
yet.** Run `grill` first and let it settle the vocabulary and the hard calls, then hand its
`CONTEXT.md` and decisions to `document-writing-orchestrator` as authoritative sources.
Skipping the first step produces a fluent document that argues for nothing in particular.

**Neither, when the request has one correct answer.** Routine implementation, a factual lookup, a
narrow copyedit, or a format conversion is ordinary work. Do it directly and say that no skill
applied, rather than dressing a small task in a workflow.

State which skill you picked and why in one sentence before you start, so the user can redirect you
before the work rather than after it.
