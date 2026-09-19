# Decision record format

Architecture decision records live in `docs/adr/` and use sequential numbering: `0001-slug.md`,
`0002-slug.md`, and so on. Scan the directory for the highest existing number and increment it.
Create the directory lazily, only when the first record is needed.

## Template

```md
# {Short title of the decision}

{One to three sentences: the context, what was decided, and why.}
```

That is the whole requirement. A record can be a single paragraph. The value lies in capturing
*that* a decision was made and *why*, not in filling out sections.

## Optional sections

Add these only when they earn their place. Most records need none of them.

- **Status** frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`), useful once
  decisions start being revisited.
- **Considered options**, when the rejected alternatives are worth remembering.
- **Consequences**, when non-obvious downstream effects need calling out.

## What qualifies

A decision earns a record when it is hard to reverse, surprising without context, and the result of
a real trade-off. In practice that tends to mean:

- **Architectural shape.** "We use a monorepo." "The write model is event-sourced; the read model is
  projected into Postgres."
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events,
  not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment
  target. Not every library — the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; others
  reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We use hand-written SQL rather than an ORM
  because X." Anything a reasonable reader would assume the opposite of. These stop the next
  engineer from "fixing" something that was intentional.
- **Constraints invisible in the code.** "Compliance rules us out of AWS." "Responses must stay
  under 200ms because of the partner API contract."
- **Rejected alternatives whose rejection is non-obvious.** If GraphQL was considered and REST won
  for subtle reasons, record it, or someone will propose GraphQL again in six months.
