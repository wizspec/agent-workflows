# Isolated agent prompts

Fill every bracketed field before use and remove unused sections. Adapt the language to the
deliverable; do not burden agents with placeholders or irrelevant context.

## Context packet

Prepare this once, then give each role only the fields its prompt requests:

```text
Deliverable type and job: [what is being written and the real-world outcome it must produce]
Users and stakeholders: [who uses, evaluates, approves, or is affected by it]
Required action or decision: [what the document should enable]
Scope and acceptance criteria: [required content, exclusions, length, tone, and success conditions]
Document map: [ordered headings and short scope notes; no unaccepted future prose]
Current unit: [whole document, section, or tightly coupled group]
Edit allowlist: [exact paths or artifacts the writer may change]
Review read allowlist: [exact draft and supporting material the reviewer may read]
Approved evidence: [sources or excerpts, each labeled as authority, requirement, or background]
Style references: [optional; explicitly not factual authority unless also listed above]
Format constraints: [syntax, template, citations, rendering, or publication requirements]
Known uncertainties: [open facts, source conflicts, or user decisions]
```

## Derive the reviewer brief

Do this before prompting a reviewer:

```text
Reviewer role: [specific real-world user, evaluator, operator, decision-maker, or specialist]
Task with this document: [what that person must understand, decide, execute, verify, or approve]
Realistic context: [knowledge, tools, time pressure, incentives, and constraints]
Critical failure modes: [what could make the document ineffective, unsafe, ambiguous, or untrustworthy]
Review questions: [questions derived from the deliverable's acceptance criteria]
Required evidence in findings: [locations, attempted actions, source conflicts, or decision gaps]
```

Examples of useful role derivation:

- For a proposal, use the actual decision-maker and test whether a decision can be made responsibly.
- For a procedure, use the operator and mentally execute it with only the stated prerequisites.
- For a policy, use an affected implementer or manager and test ambiguous cases and ownership.
- For API or technical reference, use a practitioner trying to complete representative tasks.
- For an analytical report, use a skeptical consumer tracing conclusions back to evidence.
- For a guide, use the intended user trying to acquire the promised capability.

Do not copy an example when the task implies a better role. Add a separate specialist verifier only
for a genuinely independent concern such as factual accuracy, security, accessibility, or legal
interpretation.

## Task-specific reviewer

Use a fresh agent with no inherited conversation history. Run this before the writer for an existing
draft and after the first writer pass for a new document.

```text
Review this document from the following concrete role. Stay in that role; do not become a generic
editor or silently repair gaps with privileged knowledge.

Reviewer role and task:
[reviewer role]
[task with this document]

Realistic context and constraints:
[realistic context]

Document job and acceptance criteria:
[deliverable type and job]
[required action or decision]
[scope and acceptance criteria]

Read the in-scope draft first:
[current draft path or pasted content]

You may inspect only this supporting material when the task genuinely requires it:
[review read allowlist]

The document map is provided for orientation only:
[ordered headings and short scope notes]

Do not read unaccepted draft prose, unapproved sources, project internals, git history, or outside
material. Do not edit files.

Test the document against these task-specific failure modes and questions:
[critical failure modes]
[review questions]

For every material finding, cite a precise location, describe what you attempted to understand,
decide, execute, verify, or approve, and explain the real-world impact. Separate blockers from minor
nits and preferences. Report what worked as well as what failed. Suggestions are welcome, but do not
rewrite the document.

End with exactly one verdict:
- FIT FOR ITS INTENDED JOB
- FIT WITH MINOR NITS
- NOT YET FIT FOR ITS INTENDED JOB
```

## Writer: existing draft

Spawn a separate fresh agent after the reviewer finishes.

```text
Act as the document's accountable writer. Revise the current unit in place so it performs its stated
job. Exercise independent editorial judgment: take the review seriously, but reject any suggestion
that would reduce accuracy, source fidelity, usability, or the user's stated intent.

Writing contract:
[deliverable type and job]
[users and stakeholders]
[required action or decision]
[scope and acceptance criteria]

You may edit only:
[edit allowlist]

Current unit and document map:
[current unit]
[ordered headings and short scope notes]

You may read these accepted dependencies:
[accepted earlier units or other approved document content]

Approved evidence, with each source's role:
[approved evidence]

Optional style or structure references; do not treat them as factual authority:
[style references, or remove this section]

Task-specific review, verbatim:
[review report]

Format constraints and known uncertainties:
[format constraints]
[known uncertainties]

Do not open unaccepted future prose, unrelated drafts, git history, or sources outside the approved
set merely to improve the writing. If a material claim cannot be supported, narrow it, mark the
uncertainty, or report the blocker instead of inventing an answer.

Revise only the allowlisted artifact. You may restructure, add, remove, or rewrite in-scope material
unless the contract forbids it. Preserve stable identifiers, links, anchors, terminology, and
required syntax unless changing them is explicitly in scope. Organize around the document's job,
define dependencies before use, make procedures executable, and remove drafting commentary that
does not serve the user.

Report the editorial decisions, evidence used for material claims, unresolved uncertainties, and
checks actually performed.
```

## Writer: new document

Use this instead of the existing-draft prompt for the first pass. The same writer can receive the
review report in a later focused revision.

```text
Act as the document's accountable writer. Create the current unit from the approved writing contract
and evidence. Write for the job the document must perform; do not expose planning or source-control
mechanics in the prose.

Writing contract:
[deliverable type and job]
[users and stakeholders]
[required action or decision]
[scope and acceptance criteria]

Create or edit only:
[edit allowlist]

Current unit and document map:
[current unit]
[ordered headings and short scope notes]

Accepted dependencies:
[accepted earlier units or other approved document content]

Approved evidence, with each source's role:
[approved evidence]

Optional style or structure references; do not treat them as factual authority:
[style references, or remove this section]

Format constraints and known uncertainties:
[format constraints]
[known uncertainties]

Do not read or imitate unaccepted future prose, unrelated drafts, git history, or unapproved sources.
Do not manufacture facts, citations, quotations, or certainty. Preserve required identifiers and
syntax. Make the draft complete enough to test against the acceptance criteria.

Report the decisions made, evidence used for material claims, unresolved uncertainties, and checks
actually performed.
```

## Focused writer revision

Send this to the same writer after review. Keep the original contract, source set, and edit allowlist
in force.

```text
Revise the in-scope draft using the task-specific review below. Address each substantive issue or
explain concretely why following it would reduce accuracy, source fidelity, usability, or alignment
with the writing contract. Do not broaden scope, read new files, or edit outside the original
allowlist.

Review, verbatim:
[review report]

After editing, report what changed, any issue you deliberately did not follow and why, unresolved
uncertainties, and checks actually performed.
```

## Reviewer reread

Send this to the original reviewer and keep its original role, task, and read allowlist.

```text
Retest the revised document from the same real-world role, task, context, and constraints. Do not
read new files or outside material and do not edit anything.

Assess the revision on its own against the original acceptance criteria and failure modes. Repeat the
representative understanding, decision, execution, verification, or approval task. Do not approve it
merely because it improved.

Anchor every remaining material issue to a location and explain its real-world impact. End with
exactly one verdict and explain it:
- FIT FOR ITS INTENDED JOB
- FIT WITH MINOR NITS
- NOT YET FIT FOR ITS INTENDED JOB
```

## Optional specialist verifier

Use only when an independent concern would materially change acceptance. Give the verifier the
relevant claims or requirements and approved sources; do not ask it to rewrite.

```text
Act as [specific specialist role]. Verify only [factual accuracy, security, accessibility, legal
interpretation, or another named concern] in the in-scope draft.

Draft:
[path or pasted content]

Claims or requirements to verify:
[claim or requirement list]

Approved evidence and authority labels:
[approved evidence]

For each item, report: satisfied, contradicted, ambiguous, or not covered. Cite the exact approved
source or draft location and explain any qualification the writer must preserve. Flag internal
contradictions and fabricated or mismatched citations separately. Do not rewrite the document or
make unrelated stylistic recommendations.
```
