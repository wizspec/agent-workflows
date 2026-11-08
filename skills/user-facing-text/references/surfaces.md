# Suggestions for each kind of text

Each section adds suggestions to [SKILL.md](../SKILL.md) for one kind of text. Where the project
already has a convention for that kind of text, in its glossary, its instructions, a written
decision, or the existing text itself, the convention wins.

## Buttons, menu items and labels

- A button or menu item usually works best as a verb phrase for what happens: "Save", "Split
  editor", "New file", "Show in folder".
- A label for a value or setting is usually a noun phrase: "Request timeout", "Byte order".
- Match the casing the interface already uses. Glossary terms keep the capitalisation the glossary
  gives them.
- Saying what the control acts on helps when the screen doesn't: "Upload files" rather than
  "Upload".
- Short is good, squashed isn't. "Go to the home" reads oddly because a word is missing, not
  because it is long.
- An icon-only control needs an accessible name, such as an `aria-label` on the web.

## Tooltips

- A tooltip describes what the control does or why you would use it, and doesn't repeat its name.
- Match the form the existing tooltips use, such as verb phrases without a subject or final period:
  "Stop the build and go back to editing".

## Error, warning and toast messages

- What helps most: what happened, in the reader's terms, and what to do about it if anything can be
  done.
    - "Error executing request." leaves the reader with nothing to act on.
- Naming the thing that failed helps: "Could not read `sprites.png`".
- A positive statement is easier to read than an inverted one: "No profile uses `config.yaml` as its
  default."

## Diagnostics and hints

- A diagnostic says what is wrong in the input, at its location. A hint says how to fix it, and
  reads well as an instruction: "Add a `version` field before the first rule."
- The names the reader will look up are the ones the language or tool itself uses for its keywords,
  options and fields.

## Confirmations and empty states

- A confirmation that names the action and its effect, with buttons that repeat the verb ("Delete"
  and "Cancel"), is easier to answer than "Are you sure?" with "Yes" and "No".
- An empty state can say what would appear there and how to get it: "No breakpoints. Click the
  gutter beside a line to add one."

## Documentation entries

- Reference documentation is for the people using the thing: what it is, how to use it, and a small
  example. Implementation internals and specification trivia belong elsewhere unless the reader
  needs them to use it correctly.
- A first sentence that says what it does works well: "`add` adds two numbers and returns the sum."
- Explaining a term the first time it appears, or linking to its entry, saves the reader a search.
- Fixed behaviour reads best stated plainly, without "may".

## Tutorials and lessons

- A lesson can teach a concept before naming it. Once named, using the same term every time helps.
- Introducing each command, notation and action before an example needs it keeps the reader from
  getting stuck.
- Speaking to the reader works well here: "Step through the loop and watch `count`."
- Teaching the subject directly reads better than narrating what the lesson leaves out or why it was
  written that way.
- A mistake beginners really make is worth naming once, with what happens when they make it.

## READMEs

- An opening like "This program ..." or "This library ..." tells the reader at once what they are
  looking at.
- Naming the technique ("It uses binary search", "It uses double buffering") connects the text to
  what the reader can look up.
- Steps worth writing are the ones the reader wouldn't guess. Steps the reader can see on screen,
  or that every project of this kind shares, can usually go.
- A README read on several platforms, or for several variants, reads best when the prose is true for
  all of them, with each one's values and differences in a table.
- A link can be an instruction: "Read the guide for a line-by-line explanation."
- License sections stay as they are.

## Catalogue entries

A one-line description in a manifest, a table cell or a card is a catalogue entry. A fragment
without a subject is natural here ("Finds a value in a sorted array"). Naming the technique still
helps ("using binary search").

## Blog posts

A blog post has a voice: opinions, a reason the writer cares, an aside. Those are worth keeping.
Staging and inflation (the second half of [patterns.md](patterns.md)) show up most often in blog
posts, so that half is the one to read for them.

## Release notes

- Leading with what changed for the user, in their terms, works well: "The preview window now fits
  the screen."
- One item per change, with breaking changes first and what to do about them.
- Describing the previous behaviour is fine here, because the document is about change.
