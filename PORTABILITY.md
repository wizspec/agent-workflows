# Portability contract

The canonical skill content in this repository targets the open Agent Skills format rather than one
agent runtime.

Every skill must:

- live directly under `skills/<name>/` and contain `SKILL.md`;
- use a frontmatter `name` that exactly matches its directory;
- keep required files and references inside its own directory;
- describe actions in capability terms unless a named product is intrinsic to the task;
- avoid hard-coded model names, private paths, credentials, and machine-specific assumptions;
- state external dependencies and degrade clearly when an optional capability is unavailable;
- preserve the user's authorization boundaries across runtimes; and
- remain useful when optional runtime metadata is ignored.

Vendor adapters are allowed under `agents/` or another clearly named integration directory. They may
improve discovery or UI behavior, but the portable workflow must not require them.

Project-specific conventions belong in that project's agent instructions or configuration, not in a
global reusable skill. A portable skill may discover local conventions at runtime, but it must not
assume one repository's layout is universal.
