# Documentation templates

## Contents
- Documentation index
- Roadmap item and evidence
- Changelog entry
- Architecture decision record (ADR)
- Writing rules

## Documentation index

`docs/README.md`:

```markdown
# Documentation

| Document | Purpose |
| --- | --- |
| [Requirements](requirements.md) | What the product must do and its limits |
| [Architecture](architecture.md) | Components, data flow and boundaries |
| [Technology choices](technology.md) | Stack, versions, rationale and alternatives |
| [Roadmap](roadmap.md) | Work packages, dependencies and exit checks |
| [Testing](testing.md) | How to verify, with exact commands |
| [Operations](operations.md) | Install, run, upgrade, troubleshoot |
| [Risks](risks.md) | Known problems, open questions and owners |
| [Decisions](decisions/) | One ADR per material decision |
```

Small projects may keep only the README, the roadmap, decisions and a testing note.

## Roadmap item and evidence

```markdown
## 3. P02 — Import existing projects

**Depends on:** P01. **Areas:** import, storage.

- [x] P02.1 Import a Git bundle into an isolated workspace.
- [ ] P02.2 Export a completed evolution as a bundle.

Exit: an import never writes to the original checkout; export refuses dirty or
unverified work.

P02.1 evidence (2026-10-27): 12 import tests pass on Linux; manual import of a
50 MB bundle succeeded. Export remains open.
```

Check an item only after its exit checks pass. Record dated evidence with exact
numbers, and name what remains.

## Changelog entry

Use an `Unreleased` section with `Added`, `Changed`, `Fixed` and `Removed`
subsections. Describe the behavior from the user's side, not the implementation:

```markdown
## Unreleased

### Fixed

- A service restart now resumes the running project instead of requiring a
  manual Resume.
```

## Architecture decision record (ADR)

`docs/decisions/0003-short-title.md`:

```markdown
# ADR 0003: Short decision title

Status: accepted (2026-10-27). Supersedes: none.

## Context
The problem, the forces and constraints, and who asked.

## Decision
What was chosen, stated so it can be checked.

## Alternatives
The options considered and why they were not chosen.

## Consequences
What becomes easier or harder, follow-up work and the evidence that will confirm it.
```

## Writing rules

- Use English, the present tense and short sentences. Give exact commands,
  versions and paths.
- Keep one topic per document and link instead of duplicating.
- Label planned work as planned. Never present a mock-up, sample data or an
  unexecuted check as real.
- Update the docs in the same commit as the change they describe.
