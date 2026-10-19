# Master Curriculum Map v0.3 — Structural Audit Report

**Audit date:** 2026-10-19  
**Baseline:** Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx  
**Successor:** Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx  
**Purpose:** Structural integrity and review-readiness, not a claim that every curriculum decision is correct.

## Findings

| Check | Result | Interpretation |
|---|---:|---|
| Concept clusters | 104 | Matches the declared workbook count. |
| Directed prerequisite edges | 273 | Matches the declared workbook count. |
| Invalid edge endpoints | 0 | Every dependency endpoint resolves to a concept ID. |
| Duplicate directed edges | 0 | None detected. |
| Directed cycles | None detected | Graph structure only; no cycle is not proof of pedagogical validity. |
| Inventory/edge-list mismatch pairs after field validation | 0 | The Concept Inventory prerequisite fields reconcile with the Dependencies edge list. |
| Invalid concept references in science links | 0 | All science-link references resolve to current concept IDs. |
| Open design decisions | 11 | D-11 has a provisional v0.3 implementation; educator review and learner validation remain pending. |
| Edges labelled Core / presumed prerequisite | 270 | These are provisional proposals, not validated necessities. |
| Template-style edge rationales | 261 | Each needs a specific dependency mechanism and validation check. |

## Changes made in v0.3

1. Preserved the v0.2 workbook unchanged and created v0.3 as a versioned successor.
2. Split CA-001 into Stage 1 algebraic complex numbers; added CA-003 for Stage 2 complex-plane/polar representation; retained CA-002 complex analysis in Stage 6.
3. Updated CA-001/CA-002 prerequisite IDs, reclassified affected edges, added EDGE-269 through EDGE-273, and synchronized the Stage Map and Visual Catalogue.
4. Updated D-11 to record the provisional implementation while leaving educator review and learner testing open.
5. Rebuilt the Dependency Review ledger from the structured registers and reran ID, endpoint, duplicate, cycle, and core-prerequisite reconciliation checks. The current batches contain 47 AI-assisted preliminary classifications; 226 edges remain unreviewed.

## Complex-number scope split (v0.3 provisional implementation)

CA-001 now covers algebraic complex-number meaning and operations in Stage 1. CA-003 covers complex-plane representation, modulus/argument and polar form in Stage 2. CA-002 remains complex functions and complex differentiation in Stage 6. This split is supported as a plausible design by OpenStax’s [elementary complex numbers section](https://openstax.org/books/precalculus/pages/3-1-complex-numbers), its separate [polar-form section](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-5-polar-form-of-complex-numbers), and MIT OCW’s [Complex Variables with Applications syllabus](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/syllabus/). These sources inform the design; they do not prove a unique best order or replace educator review. The patch remains provisional, and diagnostics/pilot-reader checks have not yet been conducted.

## Preliminary dependency-review batches

**Scope:** foundational/algebra review batches plus the complex-number scope split.  
**Preliminary desk-reviewed:** 47 of 273.  
**Still unreviewed:** 226.  
**Review status:** AI-assisted curriculum-design judgement; educator confirmation and learner evidence are pending. This is not an expert sign-off. Proposed validation checks are future checks, not completed experiments.

| Classification | Count |
|---|---:|
| Core required for the mapped outcome (with diagnostic/bridge pathways) | 31 |
| Helpful but not a hard gate for the whole concept cluster | 15 |
| Contextual link | 1 |

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
| EDGE-255 | FND-015 — Rational numbers and signed arithmetic → CA-001 — Complex numbers: algebraic meaning and operations | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-256 | FND-014 — Powers, roots and integer exponents → CA-001 — Complex numbers: algebraic meaning and operations | Helpful | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-257 | ALG-002 — Expressions and equivalence → CA-001 — Complex numbers: algebraic meaning and operations | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-258 | TRI-002 — Unit circle and periodic functions → CA-003 — Complex plane, modulus/argument and polar form | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-259 | CA-001 — Complex numbers: algebraic meaning and operations → CA-002 — Complex functions and complex differentiation | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-260 | CAL-004 — Differentiation rules → CA-002 — Complex functions and complex differentiation | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-261 | ADV-001 — Advanced proof architecture, lemmas and abstraction → CA-002 — Complex functions and complex differentiation | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-269 | ALG-014 — Quadratic equations and graphs → CA-001 — Complex numbers: algebraic meaning and operations | Contextual link | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-270 | ALG-006 — Coordinate plane and plotting points → CA-003 — Complex plane, modulus/argument and polar form | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-271 | GEO-005 — Pythagorean theorem and distance → CA-003 — Complex plane, modulus/argument and polar form | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-272 | CA-001 — Complex numbers: algebraic meaning and operations → CA-003 — Complex plane, modulus/argument and polar form | Core required | COMPLEX-NUMBERS-SPLIT-V03 |
| EDGE-273 | CA-003 — Complex plane, modulus/argument and polar form → CA-002 — Complex functions and complex differentiation | Helpful | COMPLEX-NUMBERS-SPLIT-V03 |

## What the structural audit does not prove

- It does not establish that an edge is required rather than helpful, contextual, or a repair path.
- It does not establish that every concept is covered at appropriate depth or in an ideal order.
- It does not establish that the teaching method improves learning; that requires reader testing.
- It does not replace mathematical review, science-source checking, accessibility review, or qualified educator feedback.

## Next steps

1. Obtain mathematics-educator review of the provisional complex-number split and its core/helpful/contextual links.
2. Validate the highest-leverage core prerequisites through diagnostics and the first reader pilots.
3. Continue focused review of the remaining 226 unreviewed edges.
4. Use reader evidence and qualified review before freezing volumes or making efficacy claims.
