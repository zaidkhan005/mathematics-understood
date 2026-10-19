# Contributing and editorial workflow

## Before drafting

- Identify the reader's prerequisites and observable learning outcomes.
- Put a genuine, well-scoped problem before the explanation when appropriate.
- Specify what readers should attempt before hints or solutions are shown.
- Plan the visual representations and embedded visual-construction prompts.
- Identify important claims requiring proof, source support, computational checks, or scientific qualification.

## Chapter workflow

1. Scope and prerequisite review.
2. Draft using the chapter template.
3. Mathematical review: definitions, assumptions, algebra, units/domains, proof validity, counterexamples, and edge cases as relevant.
4. Independent checks: hand derivation, code/numerical testing, authoritative sources, qualified reviewer, or proof assistant when suitable. A second LLM pass is a challenge check, not independent verification.
5. Pedagogy and accessibility review.
6. Visual audit: mathematical accuracy, readable labels, accessible alternatives, and prompts that develop independent sketching/visualization.
7. Learner pilot where feasible.
8. Resolve blockers and record remaining limitations before release.

## Branch and commit conventions

- Branch examples: `docs/project-bible-v1-4`, `curriculum/dep-map-review`, `chapter/v01-c01-draft`.
- Use focused commits with action-oriented messages.
- Do not silently overwrite approved versions. Preserve baselines and record version changes.
- Avoid committing private learner data, credentials, temporary render outputs, or unlicensed third-party material.

## Review severity

- **S0 — Critical:** invalid theorem/proof, unsafe scientific guidance, fabricated source, or error that fundamentally misleads. Blocks release.
- **S1 — Major:** substantial mathematical, factual, or pedagogical failure. Blocks release.
- **S2 — Moderate:** meaningful clarity, coverage, or usability problem. Resolve or explicitly defer with an owner.
- **S3 — Minor:** cosmetic or low-impact issue. May be scheduled.

## AI use

AI may help draft explanations, candidate exercises, checks, and source leads. It is not the final verifier. Never fabricate sources, citations, quotations, validation results, or reviewer sign-off.
