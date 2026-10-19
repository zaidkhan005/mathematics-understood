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

## 2026-10-19 — Dependency review Batch 1 drafted

- **Scope:** 14 high-leverage foundation-to-algebra edges reviewed as an AI-generated triage draft: EDGE-029, 030, 032, 033, 035, 037, 040, 041, 042, 044, 046, 047, 057, and 059.
- **Decision status:** Recommendations are not expert-approved. The v0.2 official review classifications remain UNREVIEWED until a human reviewer checks each specific dependency mechanism and validation test.
- **Principle:** Separate prerequisites required for full-scope mastery from concepts useful only for entry examples or contextual applications. Build repair routes and co-taught entry points where a rigid edge would block learning unnecessarily.
- **Record:** See [DEPENDENCY_REVIEW_BATCH_01.md](../curriculum/master-map/DEPENDENCY_REVIEW_BATCH_01.md).
