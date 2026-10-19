# Decision D-11: Separate Elementary Complex Numbers from Complex Analysis

**Status:** Provisionally implemented in Master Curriculum Map v0.3 — educator review and learner validation pending  
**Prepared:** 2026-10-19  
**Affected concept IDs:** CA-001 and CA-002 revised; CA-003 added in v0.3  
**Decision owner:** Mathematics, Understood project team

## Problem

The v0.2 baseline placed **CA-001 — Complex numbers and geometric representation** in Stage 6 (Advanced theory), alongside CA-002 — Complex functions and complex differentiation. The v0.3 patch provisionally separates these different learning milestones: algebraic complex arithmetic in Stage 1, complex-plane/polar geometry in Stage 2, and complex analysis in Stage 6. The goal is to avoid making polar/trigonometric fluency a hard gate for introductory algebraic complex numbers.

## Evidence informing the proposal

- OpenStax's *Precalculus* introduces square roots of negative numbers, plotting in the complex plane, and arithmetic with complex numbers in [§3.1, “Complex Numbers”](https://openstax.org/books/precalculus/pages/3-1-complex-numbers). This is evidence that elementary complex numbers can be introduced within an algebra/precalculus pathway rather than reserved for advanced complex analysis.
- OpenStax's *Algebra and Trigonometry* treats [§10.5, “Polar Form of Complex Numbers”](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-5-polar-form-of-complex-numbers), using magnitude and trigonometric relationships to convert between rectangular and polar form. This outcome relies on tools beyond basic algebraic complex arithmetic.
- MIT OpenCourseWare's [Complex Variables with Applications syllabus](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/syllabus/) lists multivariable calculus and differential equations as prerequisites for that course. This is one university course's requirement—not a universal rule—but supports treating complex analysis as a later milestone than elementary complex arithmetic.

These sources do not dictate one mandatory curriculum sequence. They support separating outcomes whose prerequisite needs differ.

## Options

### Option A — Keep CA-001 and CA-002 together in Stage 6

**Not recommended.** This keeps the current concept count stable, but risks postponing elementary complex numbers unnecessarily and hides the difference between algebraic number-system extension and complex analysis.

### Option B — Move the whole CA-001 cluster into Stage 2

**Better than Stage 6, but not preferred.** The cluster title includes geometric representation, so moving the entire cluster to a geometry/trigonometry stage could force algebraic complex arithmetic to wait for coordinate and trigonometric fluency.

### Option C — Split the learning outcomes by prerequisite structure

**Selected for provisional implementation in v0.3.** The split is now in the workbook, but the design remains open until the updated graph, prerequisite scope, and learner entry routes are reviewed.

1. **CA-001 — Complex numbers: algebraic meaning and operations** (proposed Stage 1 — Algebra & functions). Outcomes: interpret the imaginary unit (i), write numbers in (a+bi) form, identify real and imaginary parts, perform arithmetic with complex numbers and conjugates, and connect non-real roots to quadratic equations. Candidate prerequisites to review: FND-016 (real numbers), ALG-002 (expressions and equivalence), ALG-016 (radicals and rational exponents), and ALG-014 (quadratic equations and graphs). Each candidate must be classified by whether it is genuinely required for the full outcome or can be bridged inside the lesson.
2. **CA-003 — Complex plane, modulus/argument, polar form and geometric interpretation** (proposed Stage 2 — Geometry, trigonometry & spatial). Candidate prerequisites: CA-001, ALG-006 (coordinate plane), GEO-005 (Pythagorean theorem and distance), and TRI-002 (unit circle and periodic functions). The graph should distinguish prerequisites for a first complex-plane representation from those needed for polar form, powers, and roots.
3. **CA-002 — Complex functions and complex differentiation** remains in Stage 6 — Advanced theory. Review its prerequisites after the split. Do not import one university course's full prerequisite list wholesale; determine which of calculus, multivariable reasoning, differential equations, and proof skills are core for the intended scope.

## Coordinated edits applied provisionally in v0.3

- Re-scope CA-001 and move it out of Stage 6 only after its outcome and prerequisites are agreed.
- Re-scope CA-001 and move it out of Stage 6 only after its outcome and prerequisites are agreed.
- Update dependency edges and the Concept Inventory prerequisite IDs together; do not leave duplicate or stale CA-001 edges.
- Update Stage Map coverage and stage counts.
- Update the Visual Catalogue to distinguish algebraic operations from polar/geometric representation.
- Re-check CA-002's prerequisite list and update all cross-references.
- Record the decision and reviewer; regenerate the workbook and rerun structural checks.

## Validation before approval

1. Ask a mathematics educator to review the proposed outcomes and candidate prerequisites.
2. Test a beginner lesson on algebraic complex numbers without polar form, and a later lesson on polar form with prerequisites supplied.
3. Confirm all dependency references resolve, the graph remains acyclic, and the Concept Inventory prerequisite lists match the edge table.
4. Preserve v0.2 as the immutable baseline. The v0.3 patch is provisional; if expert review or learner testing changes the split, make a further versioned revision rather than silently redefining CA-001.

## Current status after the v0.3 patch

The split is provisionally present in [Master Curriculum Map v0.3](Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx):

1. **CA-001 — Complex numbers: algebraic meaning and operations** is now in Stage 1, with core prerequisites FND-015 and ALG-002. FND-014 is recorded as helpful/just-in-time rather than a hard prerequisite.
2. **CA-003 — Complex plane, modulus/argument and polar form** is a new Stage 2 cluster, with core prerequisites CA-001, ALG-006, GEO-005 and TRI-002.
3. **CA-002 — Complex functions and complex differentiation** remains in Stage 6. Polar/geometric representation is recorded as a helpful connection rather than a universal hard gate for starting complex differentiability.
4. The dependency graph now has 104 concept clusters and 273 edges. Structural checks found no invalid endpoints, duplicate edges, directed cycles, or mismatch between core prerequisite IDs and core edge links. These checks establish data consistency, not that the curriculum order is pedagogically optimal.

Batch 3 records 12 AI-assisted preliminary classifications for the affected complex-number edges. Across all three batches, 47 of 273 edges have preliminary classifications and 226 remain unreviewed. **Educator confirmation is pending, and the proposed diagnostic/transfer checks have not yet been run.** Do not present the split as expert-approved or empirically validated until that work is completed.
