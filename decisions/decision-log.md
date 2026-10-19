# Decision log

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
