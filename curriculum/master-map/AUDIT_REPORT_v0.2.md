# Master Curriculum Map v0.2 — Structural Audit Report

**Audit date:** 2026-10-19  
**Baseline:** Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx  
**Successor:** Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx  
**Purpose:** Structural integrity and review-readiness, not a claim that every curriculum decision is correct.

## Findings

| Check | Result | Interpretation |
|---|---:|---|
| Concept clusters | 103 | Matches the declared workbook count. |
| Directed prerequisite edges | 268 | Matches the declared workbook count. |
| Invalid edge endpoints | 0 | Every dependency endpoint resolves to a concept ID. |
| Duplicate directed edges | 0 | None detected. |
| Directed cycles | None detected | Graph structure only; no cycle is not proof of pedagogical validity. |
| Inventory/edge-list mismatch pairs after field validation | 0 | The Concept Inventory prerequisite fields reconcile with the Dependencies edge list. |
| Invalid concept references in science links | 0 | All science-link references resolve to current concept IDs. |
| Open design decisions | 11 | D-11 is recorded as an open proposal; no concept-stage or dependency change has been applied. |
| Edges labelled Core / presumed prerequisite | 268 | These are provisional proposals, not validated necessities. |
| Template-style edge rationales | 268 | Each needs a specific dependency mechanism and validation check. |

## Changes made in v0.2

1. Verified the FND-001 row’s field placement against the source. Its prerequisite field is empty and its representation notes are already in the representation/visual-requirements field, so no source correction was necessary; the build retains a regression check for this structure.
2. Updated workbook titles and baseline references to v0.2 while preserving the v0.1 workbook unchanged.
3. Added a Dependency Review ledger preserving v0.1 edge labels and rationale text, with fields for classification, specific dependency mechanism/evidence, proposed validation check, reviewer, and date. The current review batches contain 35 AI-assisted preliminary classifications; 233 edges remain unreviewed.
4. Added an Audit & Review worksheet containing structural checks and a prioritized human-review queue.

## High-priority unresolved judgement

CA-001 — Complex numbers and geometric representation — is currently assigned to 6 — Advanced theory, with listed prerequisites FND-016;FND-014;ALG-004;GEO-006. Introductory complex numbers are commonly useful before a full complex-analysis course, so this placement deserves explicit review. v0.2 does not silently relocate the topic; decide whether to move the introductory concept earlier or separate basic complex-number work from complex analysis, then update links and visuals consistently.

## Preliminary dependency-review batches

**Scope:** foundation-to-algebra and early algebra/function relationships.  
**Preliminary desk-reviewed:** 35 of 268.  
**Still unreviewed:** 233.  
**Review status:** AI-assisted curriculum-design judgement; educator confirmation and learner evidence are pending. This is not an expert sign-off. Proposed validation checks are future checks, not completed experiments.

| Classification | Count |
|---|---:|
| Core required for the mapped outcome (with diagnostic/bridge pathways) | 22 |
| Helpful but not a hard gate for the whole concept cluster | 13 |

The review distinguishes a prerequisite for one sub-outcome (such as graphing a function) from a prerequisite for the entire concept cluster (such as defining a function as a mapping). “Core required” means required for the stated outcome as currently scoped, not that a learner should be excluded: diagnostics and short prerequisite instruction may be integrated into the dependent lesson.

| Edge ID | Connection | Draft classification | Batch |
|---|---|---|---|
| EDGE-029 | FND-015 — Rational numbers and signed arithmetic → ALG-001 — Variables, unknowns and parameters | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-030 | FND-001 — Mathematical communication and notation → ALG-001 — Variables, unknowns and parameters | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-031 | ALG-001 — Variables, unknowns and parameters → ALG-002 — Expressions and equivalence | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-032 | FND-004 — Whole-number operations and properties → ALG-002 — Expressions and equivalence | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-033 | FND-014 — Powers, roots and integer exponents → ALG-002 — Expressions and equivalence | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-034 | ALG-002 — Expressions and equivalence → ALG-003 — Equality, equations and inequalities as statements | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-035 | FND-006 — Number line, integers, opposites and distance → ALG-003 — Equality, equations and inequalities as statements | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-036 | ALG-003 — Equality, equations and inequalities as statements → ALG-004 — Solving linear equations and inequalities | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-037 | FND-015 — Rational numbers and signed arithmetic → ALG-004 — Solving linear equations and inequalities | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-038 | ALG-004 — Solving linear equations and inequalities → ALG-005 — Rearranging formulas and literal equations | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-039 | ALG-002 — Expressions and equivalence → ALG-005 — Rearranging formulas and literal equations | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-040 | FND-013 — Measurement, units, conversion and dimensional sense → ALG-005 — Rearranging formulas and literal equations | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-041 | FND-006 — Number line, integers, opposites and distance → ALG-006 — Coordinate plane and plotting points | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-042 | FND-001 — Mathematical communication and notation → ALG-006 — Coordinate plane and plotting points | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-043 | ALG-006 — Coordinate plane and plotting points → ALG-007 — Graph reading and construction | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-044 | FND-012 — Proportional relationships and percentages → ALG-007 — Graph reading and construction | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-045 | ALG-007 — Graph reading and construction → ALG-008 — Rates, slope and proportional versus affine relations | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-046 | FND-011 — Ratios, rates and unit rates → ALG-008 — Rates, slope and proportional versus affine relations | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-047 | FND-013 — Measurement, units, conversion and dimensional sense → ALG-008 — Rates, slope and proportional versus affine relations | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-048 | ALG-002 — Expressions and equivalence → ALG-009 — Functions as input-output rules | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-049 | ALG-006 — Coordinate plane and plotting points → ALG-009 — Functions as input-output rules | Helpful | DEPENDENCY-REVIEW-01 |
| EDGE-050 | ALG-008 — Rates, slope and proportional versus affine relations → ALG-010 — Linear functions and intercepts | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-051 | ALG-009 — Functions as input-output rules → ALG-010 — Linear functions and intercepts | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-052 | ALG-003 — Equality, equations and inequalities as statements → ALG-010 — Linear functions and intercepts | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-053 | ALG-004 — Solving linear equations and inequalities → ALG-011 — Systems of equations and inequalities | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-054 | ALG-006 — Coordinate plane and plotting points → ALG-011 — Systems of equations and inequalities | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-055 | ALG-010 — Linear functions and intercepts → ALG-011 — Systems of equations and inequalities | Core required | DEPENDENCY-REVIEW-01 |
| EDGE-057 | FND-014 — Powers, roots and integer exponents → ALG-012 — Polynomial operations and structure | Core required | DEPENDENCY-REVIEW-02 |
| EDGE-059 | FND-007 — Factors, multiples, primes and divisibility → ALG-013 — Factorization and algebraic identities | Helpful | DEPENDENCY-REVIEW-02 |
| EDGE-065 | FND-014 — Powers, roots and integer exponents → ALG-015 — Rational expressions and equations | Helpful | DEPENDENCY-REVIEW-02 |
| EDGE-066 | FND-014 — Powers, roots and integer exponents → ALG-016 — Radicals and rational exponents | Core required | DEPENDENCY-REVIEW-02 |
| EDGE-068 | FND-016 — Real numbers, intervals and absolute value → ALG-016 — Radicals and rational exponents | Core required | DEPENDENCY-REVIEW-02 |
| EDGE-070 | FND-014 — Powers, roots and integer exponents → ALG-017 — Exponential and logarithmic functions | Core required | DEPENDENCY-REVIEW-02 |
| EDGE-072 | FND-016 — Real numbers, intervals and absolute value → ALG-017 — Exponential and logarithmic functions | Helpful | DEPENDENCY-REVIEW-02 |
| EDGE-074 | FND-014 — Powers, roots and integer exponents → ALG-018 — Sequences and elementary patterns | Helpful | DEPENDENCY-REVIEW-02 |

## What the structural audit does not prove

- It does not establish that an edge is required rather than helpful, contextual, or a repair path.
- It does not establish that every concept is covered at appropriate depth or in an ideal order.
- It does not establish that the teaching method improves learning; that requires reader testing.
- It does not replace mathematical review, science-source checking, accessibility review, or qualified educator feedback.

## Next steps

1. Review dependency semantics systematically, starting with foundational-to-algebra links and cross-stage edges.
2. Decide and record the complex-number placement question.
3. Build and test the fractions/ratios pilot and electrostatic interaction/dipole pilot.
4. Use reader evidence and qualified review before freezing volumes or making efficacy claims.
