# Brief and templates

Fill every bracketed field and remove the lines that do not apply. The child receives the brief and,
later, the grounding replies. Your precedent notes never leave you.

## Precedent notes

Write these for yourself before spawning the child, and keep them out of everything it receives.

```md
**How this has been done before.** [past work, conventions, house style, what has worked]

**What the audience is known to like.** [or "nothing known"]

**My own guess at the idea.** [one or two lines]
```

## Isolation probe

Use this when you do not know what your runtime passes to a new agent. Just before spawning, write
a marker in your own message to the user: a made-up string that appears nowhere else, such as a
random run of letters and digits. Then spawn the probe exactly as you will spawn the child.

```text
This is a check of what a newly started agent can see. Do nothing except answer these four points.

1. If any conversation or message came before this one, quote its last few lines verbatim.
   Otherwise say there was none.
2. List any instructions, memory, or notes in your context besides this message, one line each,
   describing them rather than quoting them. Otherwise say there are none.
3. Try to read [the path of an ordinary file in the project]. Say only whether you could, not what
   it contains.
4. List the tools you have.
```

Read the answers against the three parts of isolation:

- **Conversation**: leaked if the marker, or anything else from your conversation, appears in
  point 1.
- **Instruction files and memory**: leaked if point 2 lists anything about the project or the user.
- **File access**: open if the probe could read the file in point 3 or lists tools that read local
  files.

Change how you spawn the child to close what leaked, where the runtime lets you, and report what you
could not close.

## Brief

Give this to a fresh, isolated agent as its whole task.

```text
Someone wants something, and you have been asked to come up with it. You know nothing about who they
are or what they have done before. That is deliberate: ideas from someone who knows the history tend
to repeat it, and you are here to have one of your own.

What they want:
[the want, described by the effect it should have]

What cannot be broken:
[the hard limits, one per line, or "Nothing beyond what is said above."]

What to return:
[how finished the result should be, and its shape]

How to work:

Say in a sentence or two what you understand they want. If you think there is a better want
underneath it, you may follow that instead; just say that you did.

Don't rule anything out because it seems hard to make. Whoever makes it can do more, faster, than
you might assume, and someone who knows the circumstances will tell you what is actually out of
reach.

If you can search the web, use it when it helps, but looking at examples of this exact thing before
you have an idea tends to pull you towards what already exists. Don't read files on this machine or
try to find out who is asking; either would undo the reason you were asked.

Once you have your idea, name its heart: the part that, if lost, would make it a different idea.
Then ask what you need to know to make it real: what is true, what is available, what is possible,
including anything you suspect is out of reach. You may also ask how things like this have been done
before or what has worked; that answer will be marked as precedent, and it is yours to use or
ignore. Someone who knows the circumstances will answer with facts, not opinions about your idea.

Your reply should contain: what you understood they want, your thinking including the paths you
dropped, the idea, its heart, and your numbered questions, or that you have none and whether you
believe the idea can be made as it stands.
```

## Grounding reply

Send to the same child.

```text
Answers to your questions. They are facts about the circumstances, not a judgement of your idea, and
what you do with them is up to you.

1. [the question, briefly]: [what is true, available, or possible; every option when there are
   several]
2. [the question, briefly]: out of reach, because [the fact that makes it impossible or unavailable,
   without an alternative]
3. [the question, briefly]: possible; it would take [what it would take]. Keep it in for now; the
   person who asked will decide whether it is worth that.
4. [the question, briefly]: PRECEDENT, not a limit. [how it has been done, or what has worked]
5. [the question, briefly]: answered by the person who asked: [their reply, verbatim]

Now narrow the idea to what can be made: cut or change the parts that are out of reach, and keep the
heart. If the heart itself cannot be made within what cannot be broken, say so plainly rather than
keeping the name and changing the idea. Return the idea as it now stands and its heart, say what you
cut or changed and why, and say whether the heart changed. Then ask any further questions, or say
you have none and whether the idea can be made.
```

## Report to the user

```md
**Reframed want.** [only when the child followed a different want on purpose: which, and why]

**The idea.** [as it now stands, in the child's words]

**Its heart.** [in the child's words]

**How it got here.** [the idea as first imagined; then each question, the answer, and what the child
cut or changed because of it. Mark answers given as precedent, say whether the heart held, and mark
parts kept despite their cost or cut for cost alone as the user's to decide]

**Beside precedent.** [how this has usually been done, where the idea departs from it, and whether
it matched the parent's own guess]

**Dropped paths.** [one line each]

**Isolation.** Conversation: [held | leaked | unchecked]. Instruction files and memory: [held |
leaked | unchecked]. File access: [closed | open | unchecked]. [Say if the thread was broken.]
```

With several children, repeat the block for each, unranked, and add one line on where their ideas
converged.

## Brief for a session the user runs

When the runtime cannot isolate an agent, put this line above the brief and give it to the user to
paste into a new session that has no access to the project:

```text
Start from nothing: do not read any files, folders, or history on this machine. Work only from what
follows and, if you have it, the web.
```
