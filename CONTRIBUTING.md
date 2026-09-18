# Contributing

Contributions should make a workflow more reliable without tying it unnecessarily to one model,
agent, operating system, or repository.

## Add or update a skill

1. Put the skill in `skills/<skill-name>/`.
2. Add a `SKILL.md` with `name` and `description` frontmatter.
3. Keep the main instructions concise. Put conditional detail in `references/`, reusable automation
   in `scripts/`, and output resources in `assets/`.
4. Keep all referenced files inside the skill directory and use relative links.
5. Add optional runtime-specific metadata only in a clearly isolated adapter such as
   `agents/openai.yaml`.
6. Add the skill to the catalog in `README.md`.
7. Run `python3 scripts/validate.py` and test any new scripts.

## Authoring standard

- Describe both what the skill does and when it should activate.
- Include only guidance that changes an agent's decisions or improves reliability.
- Preserve user intent and authorization boundaries.
- Prefer capabilities such as “search files” or “spawn an isolated reviewer” over branded tool or
  model names.
- State required dependencies and provide a reasonable fallback where possible.
- Never include secrets, personal filesystem paths, private URLs, or copied proprietary material.
- Do not make one skill silently depend on another skill being installed.
- Keep destructive or externally mutating actions behind explicit user intent and proportional
  confirmation.
- Test meaningful outcomes and invariants; avoid tests that merely lock in generated prose.

See [PORTABILITY.md](PORTABILITY.md) for the cross-agent contract.

## Pull requests

Explain the user problem, the behavioral change, and how you tested it. Keep unrelated formatting or
rewrites out of the same change so reviewers can reason about the instructions an agent will receive.
