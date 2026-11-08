# Tendencies to notice

These are habits that make text harder to read. They are things to notice, not rules to enforce.
Each one has cases where it is fine, and a sentence that looks like one of them may be the clearest
way to say something.

When one of them does get in the reader's way, the fix is to say the point directly. Swapping the
words for others usually keeps the problem.

## Saying less than it means

These come from taking "be plain", "be short" and "be accurate" too far.

### No subject

A sentence starts with a verb, as a catalogue entry does, and the reader can't tell who acts.

- "Sorts an array from smallest to largest in the same memory."
- Clearer: "This program sorts an array from smallest to largest."

Fine in labels, buttons, menu items, headings, table cells and one-line catalogue descriptions,
where the subject is obvious from the context.

### Describing instead of naming

The text explains how a technique works but never gives its name, so the reader can't look it up or
connect it to the rest of the documentation.

- "Each failed request waits twice as long as the last one before it tries again."
- Clearer: "Failed requests are retried with exponential backoff."

Fine in the lesson that teaches the concept, where describing it first and naming it afterwards can
be the better order.

### Squeezed-in exceptions

A sentence carries a clause for one variant, so every reader has to step around it.

- "Settings are saved in `~/.config/app`, or `%APPDATA%\app` on Windows, and reload when the file
  changes, except on network drives."
- Clearer: "Settings reload when the settings file changes," with each platform's path in a table
  and the network-drive case in a sentence of its own.

A variant that does something different can have a sentence of its own: "On Windows, the installer
also adds a Start menu entry." Short parallel lists ("`build.sh` on Linux, `build.ps1` on Windows")
are usually fine.

### Squashed phrases

Words are dropped until the phrase reads oddly.

- "one request a retry", "one byte a pixel", "each one a click"
- Clearer: "one request per retry", "one byte per pixel"

### Wrong actor

Something is given a verb it can't do, because the real actor was compressed away.

- "A missing key returns null."
- Clearer: "If the key is not found, the result is null."

### Talking about the product from outside

The text describes the product as a reviewer would, though the reader is already using it.

- "The app's tutorials explain it step by step."
- Clearer: "Open the tutorial to follow it step by step."

Naming the product is fine where it tells the reader something, such as which of two tools has a
feature.

### Steps the screen already shows

- "Click Save, then Close." next to the Save and Close buttons.

Steps the reader wouldn't guess are worth keeping: "Click into the preview so it receives keyboard
input," "Turn your sound on."

### Inverted statements

A statement is turned around so that it is technically true but has to be decoded.

- "`config.yaml` is the default of no profile."
- Clearer: "No profile uses `config.yaml` as its default."

### Details the reader doesn't need

Counts, encodings and bounds added to be safe: "an array of twelve numbers", "an index counting from
0", "(255 unsigned)". Worth keeping when the reader will see the detail or act on it.

### Defensive caveats

Qualifiers that protect the writer rather than inform the reader, often left over from patching an
earlier overstatement.

- "The cache keeps results for an hour, though some results may be removed sooner in some cases."
- Clearer: "The cache keeps results for an hour."

A caveat that changes what the reader does is worth keeping: "On the free plan, the request limit
can stop a long import. To import without it, split the file into parts."

### Changing a term for variety

The workspace, then the project, then the folder: the reader may think these are three things.
Repeating the project's glossary term is usually clearer, and any _Avoid_ list in the glossary names
the words that have confused readers before.

### Vague errors

"Error executing request." says that something failed, but not what or what to do. Naming what
failed, and the fix if there is one, helps the reader more.

### Talking down

_Obviously_, _of course_, _just click_, _it's easy to_. A reader who is stuck feels worse. "Simply"
meaning "only" ("a raw binary is simply a sequence of bytes") is fine.

## Saying more than it means

Adapted from humanizer (see [NOTICE.md](../NOTICE.md)). The fact underneath is usually fine. Keeping
it and removing the staging is usually the fix.

### Not X but Y

A contrast whose negative half denies something no one claimed, to make the positive half sound
bigger: "It's not just an editor, it's a complete learning environment."

A contrast that corrects a mistake readers really make is teaching, and worth keeping.

### Closing lines and sayings

A last line that repeats the paragraph ("That's the key idea."), a saying that sounds deep ("At its
core, caching is about trust."), or a row of fragments for effect. Usually better cut, or replaced
with the specific claim.

### Run-ups

"Let's dive in", "Here's what you need to know", "It's worth noting that". Starting with the point
is usually enough.

### Arguing with no one

Rejecting an option or answering an objection nobody raised. In tutorials and documentation, naming
a mistake beginners really make, with what happens, is different and useful: "If you forget the
terminator, `print` keeps reading past the string."

### Inflated importance and sales language

_Pivotal_, _crucial_, _powerful_, _seamless_, _cutting-edge_, _unlock_, _showcase_, "small but
powerful". Saying what the thing is or does is usually stronger. Technical uses keep their meaning:
a robust parser, a logic gate.

### Avoiding is and has

"Serves as", "stands as", "boasts", "features". _Is_ and _has_ are usually clearer. Literal
technical verbs are fine: "-1 is represented as `0xFF`", "marks the rectangle dirty", "highlights
the line".

### Chat leftovers

"I hope this helps", "Let me know", "Great question". These don't belong in text that stands on its
own.

### Writing about the document

"This section explains ...", "The table below compares ...". Saying the content itself is usually
better. A sentence that points the reader somewhere they can't see is useful.

### Heading repeated as the first sentence

A heading followed by a sentence that says the heading again.

## Formatting

- **Bold** works well for control and setting names as the interface shows them (**Save**,
  **Autosave enabled**), and for a term where it is defined. Bold used for emphasis everywhere stops
  meaning anything.
- **Labelled lists** ("**Keys.** W and S move ...") help in reference text that readers scan. Prose
  often reads better when the labels only repeat what each item says.
- **Headings** read best naming what the section holds ("Installing", "Running on Windows") rather
  than an effect, in the casing the project already uses.
- **Dashes** used everywhere to join clauses can hide how the clauses relate; a comma, colon or new
  sentence often says it better. En dashes in ranges (pages 3–7) are correct.
- **Tables** suit text that covers several platforms, plans or modes: one row each, with "Same as
  Linux." where a row repeats another.
