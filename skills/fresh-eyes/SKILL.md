---
name: fresh-eyes
description: Get an idea for something new from an agent that knows nothing about the project, then ground it by answering that agent's questions with facts. Use when the user wants something new and the risk is that it comes out like what has been done before; not for developing an idea the user already has, or for work where matching past work is the point.
license: MIT
---

# Fresh eyes

An agent that knows a project well tends to make more of what the project has already made. Its
past work is the strongest pull on whatever it suggests next, and every rule added to steer it pulls
the same way. This skill separates having the idea from knowing the project.

A **child**, a fresh agent that knows only what the user wants and what cannot be broken, has the
idea. You are the **parent**: you hold the project, its history, and the conversation, and you
answer the child's questions about the facts its idea depends on. The idea comes first and the
knowledge second.

The idea also comes before its cost. The child imagines without weighing how hard anything would be
to make, and grounding narrows the idea afterwards to what can actually be made. Agents, like people,
drop ideas that seem hard before anyone has checked, and their sense of hard is usually calibrated
to how long a person would take. Everything below exists to protect these two orders, and when a
situation is not covered here, do whatever keeps them intact.

What the child produces, and how finished it should be, comes from the user's request and goes into
the brief. Nothing in this skill decides it.

Read [references/brief.md](references/brief.md) before spawning anything. It holds the isolation
probe, the brief, the grounding reply, and the report to the user.

## Sort what you know

Before writing anything for the child, sort what you know about the request into three piles.

**The want** is what the user wants to exist or to happen, described by the effect it should have
rather than the form it should take. A form the user named belongs in the want only when they truly
need it, and then it is a hard limit. A form that came from habit is precedent.

**Hard limits** are anything that would make an idea unusable if broken. Keep them few. When you
cannot tell a limit from a habit, treat it as a habit, and ask the user only when getting it wrong
would waste the run. Effort, time, and money are hard limits only when the user has a real ceiling
on them; a sense that something would be a lot of work is not one. Every limit that was really a
habit takes away the room the child is there to use.

**Precedent** is everything else: how the project has done this before, its conventions and house
style, what has worked, what its audience is known to like, and your own sense of what the answer
should be. Write your precedent down, including your own guess at the idea, before the child
returns. You will report the idea beside it, and a child's idea that matches your guess is a sign
that something leaked into the brief.

Ask the user only when the want itself is unclear. The rest you can usually sort yourself.

## Write the brief

The brief holds the want, the hard limits, what to return, and how the exchange works, and nothing
else. When the want needs the subject described, describe it plainly. Leave out the names of the
project, its products, and its people when a name would let the child look up how the subject has
been presented before.

Then read the brief as the child will, with no other knowledge, and look for precedent that slipped
in through the wording: a verb that presumes a form, an adjective that presumes a tone, an example
added just to clarify. Examples leak the most, because the child builds towards them.

## Spawn the child

Spawn a fresh agent and give it the brief as its whole task. It may search the web, and it should
know nothing of the project. Isolation has three separate parts, and starting a new agent does not
guarantee all of them:

- **The conversation.** The child starts with no inherited conversation, so nothing you and the user
  said reaches it except through the brief.
- **Instruction files and memory.** Many runtimes load project and user instruction files, or saved
  memory, into every new agent, including ones described as fresh. Use the runtime's option to
  leave them out where it has one.
- **File access.** A fresh context can still read the project from disk. Where the runtime allows
  it, give the child no tools that read local files, only the web. Where it does not, the brief
  asks the child not to look, which is weaker.

When you do not know what your runtime passes to a new agent, find out rather than assume. Before
the child, spawn a throwaway probe the same way, using the probe in the reference, and judge its
actual output rather than what you expected it to say. The probe is separate from the child because
asking the child to list what it can see would draw its attention to exactly what it should not use.
The result holds for the rest of the session. In the report, give each of the three parts as held,
leaked, or unchecked, and never present the idea as fresher than it is.

One child is the usual choice: it is cheaper, and one line of thought is easier to follow and to
ground. Spawn more when the user wants range to choose from, give each the same brief, and keep them
apart. Children on the same model share its habits, so expect overlap. Where their ideas converge,
tell the user, because convergence marks the obvious answer.

If the runtime cannot isolate an agent, do not have the idea yourself in this context and call it
fresh. Give the user the brief to run in a new session that has no access to the project, and ground
the child through them by relaying its questions and your answers.

## Ground the idea

The child returns the want in its own words, its thinking, one idea, the idea's heart, and its
questions. Read the restatement first, and tell a misreading from a reframe. A child that says it
followed a different want on purpose has had an idea about the want itself, which is often the most
original move available; carry it through and put it in front of the user. A child that misread the
want without noticing shows that the brief failed, and an idea built on a misunderstanding can look
new for the wrong reason. Fix the brief and spawn a new child rather than correcting this one, whose
idea already rests on the misreading.

The heart is the part that, if lost, would make it a different idea. Answer each question with
facts: what is true, what is available, what is possible, or the fact that makes something
impossible. When there are several ways to do something, give them all, not just the one the
project usually uses. The habitual answer is precedent dressed as a fact, and it is the easiest leak
to miss.

Judge what is realistic by what can actually be done with the means available, including agents
that work quickly and at scale, not by how long a person would take or how much work it sounds like.
Estimates of effort, yours included, tend to be made in human terms and run pessimistic. Something
is out of reach when it is impossible, depends on something that is not available, or costs more
than the user can spend. "Hard" is not a fact; what it would take is. When a cost is real but the
user might choose to pay it, the choice is theirs, not yours or the child's: tell the child what it
would take, have it keep that part for now, and set the cost out in the report.

When something is out of reach, say why and stop there. An alternative from you would be your idea
coming in through the side door. The child then narrows its idea to what can be made, cutting or
changing parts and keeping the heart; finding another way to the same heart is its job.

Do not judge the idea, answer questions it did not ask, or volunteer precedent. When the child asks
for precedent, such as how this has been done or what has worked, answer honestly and mark the
answer as precedent, not a limit, which the child is free to ignore. Giving it is safe at this point
because the child already holds an idea and has named its heart, so precedent is information to
weigh rather than a starting point to copy. Watch whether the heart drifts towards what you told it.
When it does, ask the child once whether that was a choice, and report the answer either way.

Some questions only the user can answer. Relay those word for word and pass the reply back as the
user's, rather than guessing on their behalf.

Continue the same child for every round, so it keeps its own line of thought. If the runtime cannot
continue an agent, start a new one with the brief, the child's last reply, and your answers, and
say in the report that the thread was broken.

Stop when the child has no more questions and says the idea can be made, or when it says the heart
cannot be made within the hard limits. That second outcome is a result for the user, who may lift a
limit. If the exchange keeps going, the child is probably absorbing the project one answer at a
time, which is the slow version of the leak this skill exists to prevent. Say so and stop.

## Report to the user

The user does not see the child's replies, so relay them. When the child reframed the want, say so
first. Give the idea and its heart in the child's own words; polishing them pulls them back towards
the house style, so leave that to the user.

Then show how it got there: the idea as first imagined, and for each question, your answer and what
the child cut or changed because of it. A part kept despite its cost, or cut for cost alone, is the
user's to decide, so mark those, along with any answer that was precedent. Beside all of it, set the
precedent you wrote down: how the project usually does this, where the idea departs from it, and
whether it matched your own guess. List the paths the child considered and dropped, one line each,
since they are sometimes better than the one it kept. Finish with the state of each part of the
isolation.

With several children, report each the same way and do not rank them. A ranking from you would
measure each idea against the project's past, which is the measure this skill keeps out.

## After the user picks

When the chosen idea needs more work, send it to the same child where you can, since it holds the
reasons behind the idea. When you develop it yourself, hold every change against the heart. A change
that loses the heart makes it a different idea, so tell the user rather than making it quietly.
