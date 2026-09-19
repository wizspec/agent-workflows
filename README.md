# Agent Workflows

[![Validate skills](https://github.com/wizspec/agent-workflows/actions/workflows/validate.yml/badge.svg)](https://github.com/wizspec/agent-workflows/actions/workflows/validate.yml)

Portable skills and repeatable workflows for AI agents.

Each skill is a self-contained folder with a `SKILL.md` entrypoint, following the open
[Agent Skills specification](https://agentskills.io/specification). The instructions are
vendor-neutral, so the same skill works in Claude Code, Codex, Cursor, OpenCode, and the other
agents that read the format.

## Skills

| Skill | What it does |
| --- | --- |
| [`document-writing-orchestrator`](skills/document-writing-orchestrator/) | Plans, drafts, revises, and validates substantial documents through controlled source use and a reviewer derived from the document's real-world job. |
| [`grill`](skills/grill/) | Interrogates a plan or design one question at a time, capturing the agreed vocabulary in a glossary and each hard call as a written decision as they settle. |
| [`persona-interrogate`](skills/persona-interrogate/) | Casts saved personas as isolated agents to judge a subject or answer questions in character, and synthesises their findings and verdicts. |
| [`persona-interview`](skills/persona-interview/) | Creates or revises a persona by interview: derives a draft from the repository, grills the user, dry-runs the result, and saves it. |
| [`personas`](skills/personas/) | Routes persona work to `persona-interview` or `persona-interrogate`. |
| [`wizspec`](skills/wizspec/) | Routes a request to the skill in this repository that fits it. |

## Install

Use the [`skills`](https://github.com/vercel-labs/skills) CLI. It needs Node.js and nothing else:

```bash
npx skills add wizspec/agent-workflows
```

The CLI detects the agents you have installed, asks which skills to put where, and writes them into
each agent's skills directory. Add `--yes` to accept the defaults without prompts.

### Choose skills, agents, and scope

```bash
npx skills add wizspec/agent-workflows --list
```

`--list` prints the catalog and installs nothing, which is the quickest way to see what a skills
repository contains before trusting it.

```bash
npx skills add wizspec/agent-workflows --skill document-writing-orchestrator --agent claude-code --agent codex
```

Repeat `--skill` and `--agent` to select several, or pass `--all` to install every skill for every
detected agent without prompts.

Installs go into the current project by default (`.claude/skills/`, `.agents/skills/`, and the
equivalent path for each agent), so a team can commit the skill alongside the code it supports.
Install into your user directory instead to make a skill available in every project:

```bash
npx skills add wizspec/agent-workflows --global
```

The CLI keeps one canonical copy and symlinks each agent's directory to it, so a single update
reaches every agent. Pass `--copy` when symlinks are unavailable.

### Run a skill without installing it

```bash
npx skills use wizspec/agent-workflows@document-writing-orchestrator | claude
```

This prints the skill as a ready-to-pipe prompt. Pass `--agent claude-code` instead of piping to
start that agent interactively with the skill already loaded.

### Manage installed skills

```bash
npx skills list
npx skills update document-writing-orchestrator
npx skills remove document-writing-orchestrator
```

### Install by hand

A skill is just a directory containing `SKILL.md`, so copying the folder into your agent's skills
directory works without any tooling:

```bash
git clone https://github.com/wizspec/agent-workflows.git
cp -r agent-workflows/skills/document-writing-orchestrator ~/.claude/skills/
```

The `skills` CLI documents the
[project and global skills path for every supported agent](https://github.com/vercel-labs/skills#supported-agents)
if you are installing somewhere else.

## Repository layout

```
skills/<skill-name>/
  SKILL.md       # entrypoint: frontmatter plus the core workflow
  references/    # detail loaded only when the workflow needs it
  scripts/       # optional reusable automation
  assets/        # optional output resources
  agents/        # optional runtime-specific metadata
```

Runtime-specific metadata stays isolated under `agents/` and never changes the portable workflow.
For example, `agents/openai.yaml` supplies Codex UI metadata and is ignored by clients that do not
read it.

## Design principles

- Open-format first: every skill starts with specification-compatible `SKILL.md` metadata.
- Runtime neutral: workflows describe capabilities and outcomes, not branded tool calls.
- Progressive disclosure: detailed prompts and references load only when the workflow needs them.
- Self-contained: a skill never depends on files outside its own directory.
- Safe to adopt: installation is explicit and non-destructive by default.
- Testable: CI validates names, frontmatter, local references, portability, and installation.

## Development

```bash
python3 scripts/validate.py
```

This checks skill names, frontmatter fields, local links, private paths, and catalog entries. CI
runs it on every push, then verifies that the `skills` CLI can still discover and install every
skill in this repository.

To additionally check a skill against the specification's reference implementation:

```bash
npx skills-ref validate skills/document-writing-orchestrator
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [PORTABILITY.md](PORTABILITY.md). Treat skill changes like
code changes: review what an agent will be instructed to do, keep permissions explicit, and test the
observable workflow rather than only its wording.

## Security

Skills are executable instructions for an agent, and they run with your agent's full permissions.
Audit any skill before installing it, especially if the agent can reach credentials, networks,
private data, or destructive tools. See [SECURITY.md](SECURITY.md) for reporting guidance.

## License

[MIT](LICENSE)
