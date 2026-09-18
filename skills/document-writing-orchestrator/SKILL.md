---
name: document-writing-orchestrator
description: Plan, draft, revise, and validate substantial documents with controlled source use and task-specific review. Use for reports, guides, proposals, policies, technical documentation, and other multi-section or high-stakes writing; not for a small one-pass copyedit or format-only conversion.
license: MIT
---

# Document Writing Orchestrator

Produce a document that performs its intended job, stays faithful to its evidence, and remains
coherent as it evolves. Scale the process to the assignment instead of imposing orchestration on
every edit.

## Choose the lightest effective workflow

Handle a short, self-contained draft or narrow copyedit directly. Use an orchestrated workflow when
the document is substantial, its sections depend on one another, source provenance matters, the
document has meaningful real-world consequences, or an independent review would materially improve
confidence.

For orchestrated work, read [references/agent-prompts.md](references/agent-prompts.md) in full before
spawning agents. Keep this skill and its reference in the orchestrator. Give each agent a fresh,
role-specific prompt containing only the context its role needs.

Use the strongest role isolation the runtime offers: separate agents, tasks, or context windows. If
none is available, run explicit sequential role passes with separate context packets and disclose at
handoff that the review was not independently isolated. Do not pretend a same-context review is
independent.

Choose the editing unit deliberately:

- Work on the whole document when the argument, voice, or cross-references dominate and the file fits
  comfortably in context.
- Work section by section when the document is long, later draft prose could bias the current
  section, or an explicit dependency order matters. Finish with a whole-document integration review.
- Group tightly coupled sections instead of forcing an artificial one-section boundary.

## Establish the writing contract

Before drafting, recover or state the smallest useful brief:

- deliverable type and its real-world job;
- intended users, evaluators, or decision-makers;
- the decision, understanding, behavior, or action the document should enable;
- requested scope, tone, length, structure, and acceptance criteria;
- artifact paths and files that may be changed;
- authoritative sources, supporting sources, and known uncertainties;
- existing approved material that must remain consistent; and
- format, rendering, citation, or publication constraints.

Infer missing details from the request and repository when the choice is low risk. Ask the user only
when a missing choice would materially change the result. Do not invent approval, evidence, policy,
or house style.

Create an in-session source register when more than a few inputs are involved. Record each source's
role: factual authority, user requirement, background, or style reference. A style reference can
guide voice and structure but is not factual authority. Resolve conflicting authoritative sources
or surface the conflict; do not silently blend them.

For staged work, maintain an in-session acceptance ledger from explicit user decisions, a durable
handoff, or the current run. Track the outline, accepted units, current unit, and unaccepted units.
Do not create a tracking file unless the user asks for one.

## Derive the review from the document's job

Do not default to a generic reader, copyeditor, or fact-checker. Select the primary reviewer
role and review questions from the deliverable and acceptance criteria. Examples:

- A proposal or decision memo needs a decision-maker who tests the recommendation, evidence,
  alternatives, costs, risks, and requested decision.
- A runbook or procedure needs the person who must execute it under realistic conditions, checking
  prerequisites, sequence, observability, recovery, and completion criteria.
- A policy needs an affected operator or manager who tests scope, interpretation, enforceability,
  exceptions, ownership, and consequences.
- A technical reference needs a practitioner who tests correctness, completeness, findability,
  examples, interfaces, and edge cases.
- A report or analysis needs a skeptical consumer of the findings who tests methods, traceability,
  limitations, and whether conclusions follow from evidence.
- A guide or explanation needs its intended learner or user, checking assumptions, progression,
  examples, and whether the promised capability is actually taught.
- Persuasive or customer-facing copy needs its intended buyer or evaluator, checking relevance,
  differentiation, credibility, objections, and claim support.

These are examples, not a closed taxonomy. Name the reviewer as a concrete role, state the task they
must perform with the document, and define the evidence their verdict must contain. Use a second
specialist review only when another independent dimension is consequential—for example legal,
security, factual, or accessibility verification. Do not make one reviewer simulate incompatible
roles.

## Control context without losing coherence

When staged isolation matters, give agents:

- the complete document map as headings and short scope notes only;
- the current unit and its relevant requirements;
- accepted earlier units that the current unit truly depends on;
- the reviewer baseline and approved source excerpts or paths; and
- any reference artifact explicitly approved for style or structure.

Do not expose draft prose from later or unaccepted units merely for background. Do not infer what a
reviewer knows from a role label; state the concrete context, constraints, and capabilities that the
real user of the document would have.

Isolation is a tool, not a ritual. If the assignment requires whole-document consistency, allow the
reviewer and writer to read the whole in-scope document. After staged units are accepted, always run
an integration pass over the complete document for duplicated content, terminology drift, broken
cross-references, inconsistent claims, and uneven structure.

## Run the writing loop

Use separate task-specific reviewer and writer roles. The reviewer tests whether the document works;
the writer owns editorial decisions and edits.

For an existing draft:

1. Spawn a fresh task-specific reviewer and wait for its evidence-based report.
2. Spawn a fresh writer with the writing contract, approved sources, in-scope draft, and review.
3. Inspect the writer's diff or artifact and confirm it stayed within the edit allowlist.
4. Return the revision to the original reviewer after any substantive change to meaning, order,
   claims, instructions, examples, or requested action.

For a new document:

1. Spawn a fresh writer to create the first complete in-scope draft from the writing contract and
   source register.
2. Spawn a fresh task-specific reviewer to test that draft.
3. Return substantive issues to the same writer for a focused revision.
4. Have the same reviewer reread the result.

A reread is optional after a narrow spelling, punctuation, formatting, or metadata-only edit; record
why it was unnecessary. Continue the writer-reviewer loop until the result is ready or only minor
nits remain that the orchestrator explicitly accepts. If the same substantive disagreement survives
two revision cycles, stop and ask the user rather than looping indefinitely.

For section-by-section work, finish and accept one unit before beginning the next when acceptance
changes what later units may assume. Otherwise, parallel work is acceptable only when sections are
genuinely independent and the integration pass can reconcile them safely.

## Keep the roles honest

The reviewer inhabits the real role selected from the writing contract. It tests the document using
that role's realistic goals, constraints, and failure modes; it does not become a generic prose
critic or silently repair gaps using privileged knowledge. It anchors findings to the draft,
explains operational impact, and distinguishes blockers from preferences. Its report is evidence,
not an editing specification.

The writer should take the review seriously while rejecting suggestions that would reduce factual
accuracy, source fidelity, usability, or the user's stated intent. It may restructure, add, remove,
or rewrite in-scope material unless the brief restricts those changes. Preserve stable identifiers,
links, anchors, terminology, and public interfaces unless changing them is part of the request.

When independent factual verification is warranted, use a separate verifier after drafting. Give it
the claims to check and the approved evidence, not a mandate to rewrite. The orchestrator decides how
verified findings affect the document.

## Apply durable writing principles

- Organize around the job the document must perform, not around the source material's order.
- Lead each section with what its user needs to understand, decide, or do.
- Define specialized terms before relying on them. Restore essential context at the point of use.
- Make each section earn its place. Remove repetition that does not aid navigation, trust, or recall.
- Prefer concrete explanations, examples, and deliberate transitions over dense lists or ornamental
  prose.
- Address the subject directly. Do not narrate drafting decisions, source restrictions, or deliberate
  omissions unless that disclosure serves the document's purpose.
- Prefer affirmative statements. Keep corrective “X, not Y,” “rather than,” and similar contrasts
  only when they resolve a likely misconception.
- Calibrate certainty to the evidence. State verified behavior directly, qualify genuine uncertainty,
  and never manufacture facts, citations, quotations, or consensus.
- Introduce every dependency before an instruction, example, recommendation, or conclusion relies on
  it.
- Make examples representative and procedures executable from the information provided.
- Preserve the user's voice when editing; do not homogenize intentional style into generic polish.

These are decision criteria, not a required house style. The writing contract takes precedence.

## Validate proportionally

Preserve unrelated workspace changes. Before acceptance, inspect the changed files or artifact and
check:

- scope and structural integrity;
- factual claims against their designated sources;
- terminology, citations, links, cross-references, examples, and actionable steps;
- fitness for the document's job and unsupported assumptions; and
- visual rendering when layout is part of the deliverable.

Run the narrowest meaningful automated checks. Do not run an entire repository suite for prose-only
work unless the user requests it or a concrete dependency requires it. For format-sensitive files,
use the appropriate document tooling and inspect the rendered result, not just the source.

At handoff, identify changed artifacts, summarize the important editorial decisions, name material
uncertainties or deliberate exclusions, report the final reviewer verdict when used, and list only
the checks actually performed.
