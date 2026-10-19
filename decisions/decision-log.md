# Decision log

## 2026-10-19 — Dependency review batch 01: foundation to algebra

- **Scope:** Review the 27 existing edges EDGE-029 through EDGE-055 connecting foundational numeracy to variables, expressions, equations, coordinates, graph literacy, rate/slope, functions, and linear systems.
- **Preliminary classification:** 18 marked Core required for the stated outcome as currently scoped; 9 marked Helpful, with notes on local bridging and sub-outcomes.
- **Reasoning standard:** The edge ledger now records a specific dependency mechanism and a proposed diagnostic/transfer check for each reviewed edge. “Helpful” means the link should support instruction but should not gate access to the whole concept cluster.
- **Status and limitation:** This is an AI-assisted preliminary desk review, not independent educator sign-off; the proposed checks have not yet been run. Educator review and learner evidence are required before promoting these labels to validated curriculum decisions. 241 of 268 edges remain unreviewed.
- **Follow-up:** Review the classifications with a mathematics educator, run the proposed checks with pilot learners where feasible, record disagreements, and update the ledger without silently rewriting the prior proposal set.


## 2026-10-19 — Master Curriculum Map v0.2 structural audit

- **Decision:** Preserve v0.1 as the baseline and publish v0.2 as the audited successor. Add a dependency-review ledger; all 268 current edge classifications remain provisional until their necessity is established.
- **Structural findings:** 103 concept clusters and 268 prerequisite edges; no duplicate directed edges, invalid endpoints, or cycles detected; all science-link references resolve. Concept Inventory prerequisite fields reconcile with the dependency edge list.
- **Data-integrity note:** Cell-level verification confirmed that FND-001's prerequisite field is empty and its representation notes are already in the correct representation column. No correction to this row was needed; the workbook builder checks this condition.
- **Open curriculum question:** Review the stage placement of introductory complex numbers (CA-001) before finalizing stage/volume boundaries.
- **Status and limits:** v0.2 is a working architecture. Structural consistency does not establish that all prerequisites are pedagogically necessary or that the learning method is effective; expert review and learner testing remain required.


Record consequential project decisions; do not rewrite history. Use the format below for new entries.

## 2026-10-19 — Public repository and CC BY 4.0 scope

- **Decision:** Keep the repository public. Offer original educational and project-documentation materials under CC BY 4.0 only to the extent the relevant authors/contributors have the rights needed to grant that license. Exclude third-party material, software/code unless separately licensed, project marks, and rights not granted by CC BY 4.0.
- **Context / alternatives considered:** The repository was made public to support open educational reuse. Leaving it without a clear license would leave users uncertain about reuse permissions; applying a broad license without scope limits could incorrectly imply rights over third-party or code material.
- **Rationale and evidence:** CC BY 4.0 permits sharing and adaptation, including commercially, subject to attribution and other license conditions. The scope statement clarifies that the license only covers material the project authors/contributors can license.
- **Risks / trade-offs:** CC BY 4.0 is generally irrevocable for compliant uses of already-licensed material. Contributors must identify third-party content and must not submit material they lack authority to share. This is a project policy, not legal advice.
- **Impacts on curriculum/manuscripts/templates:** Add license and scope notices to the repository root, README, and rights policy; track sources, licenses, attribution, and permission status for reusable assets.
- **Status / owner / review trigger:** Approved project direction; updates committed on 2026-10-19. Review before adding software/code, third-party assets, or contributions under different terms.

## 2026-10-19 — Problem-first default and visual independence

- **Decision:** For suitable lessons, default to a meaningful problem attempt before intuitive/formal explanation; use exceptions deliberately. Visuals are required when they materially support understanding, but teaching must also build reader independence through embedded prompts to predict, sketch, construct, reconstruct, and transfer representations.
- **Rationale:** Give readers an opportunity to generate and compare approaches before consolidation, while avoiding unproductive or unsupported struggle. Prevent a text filled with beautiful visuals from replacing learners' own representational skill.
- **Guardrails:** Match task challenge and support to prerequisites; allow accessible non-imagery-dependent routes; make visual accuracy and problem-first sequence subject to review and learner testing.
- **Status:** Incorporated into Project Bible v1.3; implementation to be evaluated in pilot chapters.

## New decision template

### YYYY-MM-DD — [Short decision title]
- **Decision:**
- **Context / alternatives considered:**
- **Rationale and evidence:**
- **Risks / trade-offs:**
- **Impacts on curriculum/manuscripts/templates:**
- **Status / owner / review trigger:**

## 2026-10-19 — Dependency review batches 1 and 2 drafted

- **Scope:** The structured registers cover 35 edges provisionally: 27 early algebra/function links and 8 foundational links into polynomial, rational-expression, radical, exponential/logarithmic, and sequence concepts.
- **Decision status:** The workbook records these as AI-assisted preliminary desk reviews with educator confirmation pending. They are not expert-approved classifications, and the proposed diagnostic/transfer checks have not yet been run.
- **Principle:** Separate prerequisites for full-scope mastery from knowledge useful only for starter examples or contextual applications. Use diagnostics, co-taught bridges, and repair routes so a rigid graph does not block entry unnecessarily.
- **Records:** [Batch 1](../curriculum/master-map/DEPENDENCY_REVIEW_BATCH_01.md) and [Batch 2](../curriculum/master-map/DEPENDENCY_REVIEW_BATCH_02.md), with their structured JSON registers under `curriculum/master-map/reviews/`.

## 2026-10-19 — D-11 proposal: complex-number scope and stage split

- **Status:** Open proposal; no concept stages or dependency edges changed.
- **Recommendation:** Split CA-001 into an algebraic complex-numbers milestone (proposed Stage 1) and a new CA-003 for complex-plane/polar/geometric work (proposed Stage 2); retain CA-002 complex analysis in Stage 6 and recheck its prerequisites.
- **Rationale:** The current CA-001 cluster combines outcomes with different prerequisite needs. OpenStax presents elementary complex numbers separately from polar-form work, while an MIT OCW complex-variables course lists multivariable calculus and differential equations as prerequisites. Those sources inform the design but do not replace educator review.
- **Record:** [D-11 decision proposal](../curriculum/master-map/DECISION_PROPOSAL_CA001.md). Review before a new workbook version is produced.


## 2026-10-19 — D-11 provisional implementation in Master Curriculum Map v0.3

- **Status:** Provisional implementation; mathematics-educator confirmation and learner validation are still pending.
- **Change:** CA-001 now covers algebraic complex numbers in Stage 1. New cluster CA-003 covers complex-plane/modulus/argument/polar representation in Stage 2. CA-002 complex analysis remains in Stage 6.
- **Coordinated edits:** Updated concept outcomes and core prerequisite IDs; reclassified affected links into core, helpful, and contextual types; added EDGE-269 through EDGE-273; updated the Stage Map and Visual Catalogue; retained existing V-16 and added V-17 for polar/geometric representation.
- **Automated structural results:** 104 concept clusters and 273 edges; no invalid endpoints, duplicate directed edges, directed cycles, or mismatches between Concept Inventory core prerequisite IDs and core-labelled edges. This is structural validation only, not evidence that the pedagogical sequencing is optimal.
- **Review state:** Batch 3 supplies 12 AI-assisted preliminary classifications for the affected edges. Across all three batches, 47 edges have preliminary classifications and 226 remain unreviewed. Educator confirmation is pending; proposed diagnostic/transfer checks have not been run.
- **Record:** [D-11 provisional implementation record](../curriculum/master-map/DECISION_PROPOSAL_CA001.md), [v0.3 workbook](../curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx), and [v0.3 audit report](../curriculum/master-map/AUDIT_REPORT_v0.3.md).
