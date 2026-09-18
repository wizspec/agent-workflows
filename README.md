# Agent Workflows

Portable skills and repeatable workflows for AI agents.

This repository follows the open [Agent Skills specification](https://agentskills.io/specification):
each skill is a self-contained folder with a `SKILL.md` entrypoint and optional references, scripts,
assets, or runtime adapters. The core instructions are vendor-neutral and are intended to work with
Claude, Codex, Gemini, and other agents that support the format.

## Skills

| Skill | What it does |
| --- | --- |
| [`document-writing-orchestrator`](skills/document-writing-orchestrator/) | Plans, drafts, revises, and validates substantial documents through controlled source use and a reviewer derived from the document's real-world job. |

## Install

Clone the repository, then use the included installer:

```bash
git clone https://github.com/Wiz1991/agent-workflows.git
cd agent-workflows

python3 scripts/install.py --list
python3 scripts/install.py --skill document-writing-orchestrator --agent codex
python3 scripts/install.py --skill document-writing-orchestrator --agent claude
```

Use `--agent both` to install into both standard user locations, or use `--target` for any
SKILL.md-compatible agent:

```bash
python3 scripts/install.py --skill document-writing-orchestrator --target /path/to/skills
```

The installer copies skills rather than linking them and refuses to replace an existing skill unless
you pass `--force`.

Manual installation works too: copy the complete skill folder into the skills directory used by your
agent. Common user-level locations are:

| Agent | Skills directory |
| --- | --- |
| Codex and agents using the shared convention | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| Other compatible agents | Consult the agent's documentation or use `--target` |

## Design principles

- Open-format first: every skill starts with specification-compatible `SKILL.md` metadata.
- Runtime neutral: core workflows describe capabilities and outcomes, not branded tool calls.
- Progressive disclosure: detailed prompts and references load only when the workflow needs them.
- Self-contained: a skill does not depend on files outside its own directory.
- Safe to adopt: installation is explicit, copy-based, and non-overwriting by default.
- Testable: CI validates names, frontmatter, local references, portability, and installation.

Runtime-specific metadata may live under a skill's `agents/` directory. It is optional and does not
change the portable workflow. For example, `agents/openai.yaml` provides Codex UI metadata and is
ignored by clients that do not use it.

## Validate

```bash
python3 scripts/validate.py
```

For conformance testing with the reference implementation, you can additionally run:

```bash
skills-ref validate skills/document-writing-orchestrator
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [PORTABILITY.md](PORTABILITY.md). Treat skill changes like
code changes: review what an agent will be instructed to do, keep permissions explicit, and test the
observable workflow rather than only its wording.

## Security

Skills are executable instructions for an agent. Audit any skill before installing it, especially if
the agent can access credentials, networks, private data, or destructive tools. See
[SECURITY.md](SECURITY.md) for reporting guidance.

## License

[MIT](LICENSE)
