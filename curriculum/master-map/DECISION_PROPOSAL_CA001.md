# Open Decision Proposal D-11: Separate Elementary Complex Numbers from Complex Analysis

**Status:** Open proposal — not yet implemented in the master concept graph  
**Prepared:** 2026-10-19  
**Affected concept IDs:** CA-001, CA-002; proposed new cluster CA-003  
**Decision owner:** Mathematics, Understood project team

## Problem

The current map places **CA-001 — Complex numbers and geometric representation** in Stage 6 (Advanced theory), alongside CA-002 — Complex functions and complex differentiation. The two topics have very different entry requirements. Combining algebraic complex-number operations with geometric/polar representation can also create an all-or-nothing prerequisite cluster: the algebraic idea need not wait for all trigonometric and geometric tools, while polar form does depend on them.

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

**Recommended for the v0.3 design review.** Keep this as a proposal until the graph and workbook changes have been independently checked.

1. **CA-001 — Complex numbers: algebraic meaning and operations** (proposed Stage 1 — Algebra & functions). Outcomes: interpret the imaginary unit (i), write numbers in (a+bi) form, identify real and imaginary parts, perform arithmetic with complex numbers and conjugates, and connect non-real roots to quadratic equations. Candidate prerequisites to review: FND-016 (real numbers), ALG-002 (expressions and equivalence), ALG-016 (radicals and rational exponents), and ALG-014 (quadratic equations and graphs). Each candidate must be classified by whether it is genuinely required for the full outcome or can be bridged inside the lesson.
2. **CA-003 — Complex plane, modulus/argument, polar form and geometric interpretation** (proposed Stage 2 — Geometry, trigonometry & spatial). Candidate prerequisites: CA-001, ALG-006 (coordinate plane), GEO-005 (Pythagorean theorem and distance), and TRI-002 (unit circle and periodic functions). The graph should distinguish prerequisites for a first complex-plane representation from those needed for polar form, powers, and roots.
3. **CA-002 — Complex functions and complex differentiation** remains in Stage 6 — Advanced theory. Review its prerequisites after the split. Do not import one university course's full prerequisite list wholesale; determine which of calculus, multivariable reasoning, differential equations, and proof skills are core for the intended scope.

## Required coordinated edits if approved

- Add CA-003 with observable learning outcomes and appropriate status.
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
4. Preserve v0.2 as the baseline; implement approved scope changes in a new, versioned workbook rather than silently changing the meaning of CA-001.

## Current recommendation

Adopt the **split-as-design-direction** for the next curriculum-map revision, but leave the Stage 6 placement and graph unchanged until the v0.3 scope and prerequisite edits are reviewed together. Keep this proposal marked **Open** meanwhile.
