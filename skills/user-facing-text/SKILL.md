---
name: user-facing-text
description: Write or review text that the people using a product read, so that it says what it means directly. Use for documentation, tutorials and lessons, READMEs, blog posts, release notes, button labels, menu items, tooltips, error and toast messages, diagnostics and hints, and any other prose or interface string; not for code comments, commit messages, or internal design notes.
license: MIT
---

# User-facing text

The aim is text that tells the reader what they need, in the words they would use, without making
them work out what it means.

This is guidance, not a set of rules. Each suggestion describes something that has made real text
worse. Use a suggestion where it helps the reader, and ignore it where it doesn't. If following one
makes a passage harder to read, the passage wins.

## Why guidance and not rules

Rules like "be plain", "avoid jargon" and "be accurate" sound safe. Applied everywhere, they produce
text that avoids the term it should have used, drops the subject from sentences, and squeezes every
exception into the main sentence. Each rule is reasonable. Following them mechanically is the
problem.

Any list of patterns can fail the same way, this one included. So don't rewrite a sentence just
because it resembles an example below. Rewrite it because a reader would stumble on it.

## Read the project first

Before writing or reviewing, find what the project has already settled:

- **The glossary.** A root `CONTEXT.md`, a `CONTEXT-MAP.md` pointing to several, or whatever the
  project uses instead. Its terms are the ones the interface and the docs use, and its _Avoid_ lists
  name the words that have confused readers before.
- **Written conventions.** The project's agent instructions, a style guide, and any written
  decisions about interface text or documentation (often under `docs/wizspec/decisions/` or an ADR
  directory).
- **Existing text of the same kind.** The casing and form of the labels next to the one you are
  writing, the shape of the other READMEs, the tone of past release notes.

The project's conventions win over the suggestions here. Where it has none, use these suggestions,
and don't present them as house rules.

## The reader

Work out who reads this text, what they already know, and what they can see around it. Most readers
of user-facing text know less than the writer, can see the screen or page around the text, and came
to do something. A good test for a sentence: would you say it this way to a person sitting next to
you, looking at the same screen?

## Two ways text goes wrong

- **Saying less than it means.** Fragments with no subject, a description where the term belongs,
  squashed phrases, exceptions squeezed in everywhere. The text is correct, but the reader has to
  work out what it says. This is common in text written to be short, or under strict style rules.
- **Saying more than it means.** Run-ups, dramatic contrasts, inflated importance, sales language.
  The text sounds important but adds nothing. This is common in generated text and marketing copy.

Fixing one often causes the other. Cutting padding too hard leads to the first; adding explanation
to fix the first can lead to the second.

## Questions to ask of a draft

These usually find the problems.

- **Who does what?** If a sentence has no clear actor, the reader has to guess.
    - "Looks for 91 in a sorted array of twelve numbers" reads better as "This program looks for 91
      in a sorted array."
    - "A missing key returns null" reads better as "If the key is not found, the result is null."
- **Did I use the name the reader would look up?** If a sentence explains how something works
  instead of naming it, the reader can't search for it.
    - "Each comparison with the middle element rules out half of the remaining range" reads better
      as "It uses binary search to find the match."
    - In the lesson that teaches a concept, describing it before naming it can be the right order.
- **Does the reader need this detail?** Counts, encodings and bounds added to be safe make the
  useful part harder to find.
    - "The result is an index counting from 0 into the twelve-element array" reads better as "The
      result is the index of the element in the array." A detail earns its place where the reader
      will see it and be surprised by it.
- **Is this true for everyone who reads it?** When one text covers several platforms, plans or
  modes, a clause for one of them ("..., or `%APPDATA%` on Windows") makes every reader work around
  it. The common case usually belongs in the prose, and the differences in a table or a sentence of
  their own.
- **Does the screen already say this?** "Click Save, then Close" next to those two buttons tells the
  reader nothing new. A step they wouldn't guess, such as clicking into the preview so it receives
  keyboard input, is worth writing.
- **Am I talking to the reader, or about the product?** "The app's tutorials explain it step by
  step" describes the product from outside. "Open the tutorial to follow it step by step" speaks to
  someone who is already using it.
- **Did I fix a fact by adding a clause?** Corrections that pile up clauses are how a clear sentence
  becomes hard to read. Rebuilding the sentence usually works better.
- **Am I using the same word for the same thing?** Switching terms for variety (the workspace, the
  project, the folder) suggests three different things. The glossary's terms are the ones to repeat.
- **Would a person say it this way?** Squashed phrases ("one request a retry"), inverted statements
  ("is the default of no profile") and stiff verbs ("serves as") often pass every other question and
  still read oddly.

[references/patterns.md](references/patterns.md) describes these tendencies in more detail, with
examples and the cases where they are fine. [references/surfaces.md](references/surfaces.md) has
suggestions for each kind of text: labels, tooltips, errors, documentation, tutorials, READMEs, blog
posts and release notes.

## Writing

1. Work out what kind of text it is and what the reader can already see around it. The section for
   it in [references/surfaces.md](references/surfaces.md) may help.
2. Get the facts from the source: read the code, run the program, or look at the feature. A value,
   a setting or a key you haven't checked is better left out, or asked about.
3. Start with what the thing is or does, using its name. Then what the reader does with it. Then the
   details they need.
4. Read the draft against the questions above, then once more as the reader would.

For a substantial document whose sources, structure and review matter, run
`document-writing-orchestrator` for the process and use this guidance for the prose it produces.

## Reviewing

1. Read the whole text before judging any line. Some problems only show at the paragraph level, such
   as the same exception in every sentence or the same closing line after every section.
2. Check the facts against the source.
3. For each finding, say what the reader would struggle with, quote the text and suggest a rewrite.
   Describe the effect on the reader rather than naming a pattern: the point is the reader, not the
   list.
4. Leave alone what already works, even if it resembles an example in the references.
5. Apply the rewrites only when the user asks for fixes. When you do, rewrite the passage around its
   point rather than swapping out the flagged words.

## What a rewrite keeps

- The facts. A rewrite shouldn't add or drop a value, a name, a step or a claim. If a sentence needs
  a detail you don't have, ask, or write a simpler sentence.
- Code, commands, paths, URLs, identifiers, keyboard shortcuts, and control names as the interface
  spells them.
- License, copyright and attribution text. Problems in it are worth reporting, but rewording it is
  the user's call.
- Text the user wrote and asked to keep, and a deliberate voice: an author's opinions and asides are
  not padding.
