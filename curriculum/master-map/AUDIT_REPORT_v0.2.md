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
| Inventory/edge-list mismatch pairs after repair | 0 | The Concept Inventory prerequisite fields reconcile with the Dependencies edge list. |
| Invalid concept references in science links | 0 | All science-link references resolve to current concept IDs. |
| Edges labelled Core / presumed prerequisite | 268 | These are provisional proposals, not validated necessities. |
| Template-style edge rationales | 268 | Each needs a specific dependency mechanism and validation check. |

## Corrections made in v0.2

1. Corrected the FND-001 row: its representation notes (Annotated examples; symbol maps; number sentences.) had been entered in the core prerequisite field. The prerequisite field is now empty and the notes are in the representation/visual-requirements field.
2. Updated workbook titles and baseline references to v0.2 while preserving the v0.1 workbook unchanged.
3. Added a Dependency Review ledger preserving the prior edge labels and rationale text, with new fields for reviewed classification, specific dependency mechanism/evidence, validation check, reviewer, and review date. Each row starts UNREVIEWED.
4. Added an Audit & Review worksheet containing structural checks and a prioritized human-review queue.

## High-priority unresolved judgement

CA-001 — Complex numbers and geometric representation — is currently assigned to 6 — Advanced theory, with listed prerequisites FND-016;FND-014;ALG-004;GEO-006. Introductory complex numbers are commonly useful before a full complex-analysis course, so this placement deserves explicit review. v0.2 does not silently relocate the topic; decide whether to move the introductory concept earlier or separate basic complex-number work from complex analysis, then update links and visuals consistently.

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
