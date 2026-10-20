# Validation Protocol v0.1 — Complex-Number Learning Pathway

**Status:** Proposed formative protocol; not yet piloted  
**Prepared:** 2026-10-20  
**Scope:** D-11, CA-001, CA-003 and affected edges in Master Curriculum Map v0.3

> **Evidence boundary:** This is a test plan, not a report of learner results. Structural graph checks do not establish teaching effectiveness. A small formative pilot cannot establish universal curriculum requirements.

## 1. Questions

1. Can learners with basic signed arithmetic and expression skills learn algebraic complex numbers without first learning polar form or the unit circle?
2. Which parts of complex-plane/polar representation require coordinate, distance/Pythagorean and trigonometric knowledge—and which can be supported by a short in-lesson bridge?
3. Does the map confuse knowledge needed for a full outcome with a hard gate to starting a topic?
4. Are errors caused by prerequisite gaps, task wording, notation, weak explanation, or arithmetic slips?
5. Can learners transfer the idea to unfamiliar problems, not just imitate examples?

## 2. Definitions

- **Full-scope prerequisite:** Knowledge needed to achieve the complete stated outcome reliably.
- **Entry gate:** A rule that blocks a learner from starting a lesson.
- **Just-in-time bridge:** A short, planned refresher taught within the lesson.
- **Core link:** A meaningful dependency for the full outcome. It does not automatically mean the learner must be blocked from beginning.
- **Helpful link:** Knowledge that improves access or efficiency but is not necessary for the stated outcome after reasonable in-lesson support.
- **Contextual link:** An application or motivation that enriches the topic without being needed for its central outcome.

Keep dependency classification distinct from access policy. Test the specific claimed link, and record alternative explanations before changing a classification.

## 3. Pilot procedure

### Phase A — Educator desk review

Before testing, ask a mathematics educator to check mathematical correctness, task wording, answer keys, proposed thresholds, and whether any CA-001 item accidentally assumes polar/trigonometric knowledge. Record reviewer, date, changes and unresolved disagreements. AI review is not independent expert approval.

### Phase B — Formative try-out

1. Try the first draft with 3–5 learners to uncover confusing prompts and timing problems; revise the instrument before drawing conclusions.
2. Then aim for approximately 8–12 learners with varied recent algebra fluency, if feasible. This is exploratory formative evidence, not a representative sample.
3. Collect entry diagnostics, independent work, short reasoning explanations and an immediate transfer task. Mark each response as independent, prompted, completed after a planned bridge, or completed after an unplanned explanation.
4. Participation should be voluntary and no-stakes. Explain what is being observed; obtain permission before recording audio/video; anonymize notes and avoid unnecessary personal data.
5. Report item-level patterns and uncertainty. Do not infer broad effectiveness or causation from a small group.

Planning estimates: CA-001, 35–50 minutes; CA-003, 40–60 minutes. These are not validated timings.

### Phase C — Revision

Keep v0.3 unchanged during this test. Record observations and educator interpretation first. Only then create a versioned map update if the evidence supports one.

## 4. Test A — CA-001: Algebraic meaning and operations

### Intended outcome

After a brief explanation defining i² = −1, a learner can interpret a + bi, identify real and imaginary parts, perform basic operations, and use conjugates for simple division. Prior knowledge of polar form, arguments or the unit circle is not expected. Quadratic roots may motivate the topic but must not become a hidden prerequisite for basic arithmetic.

### A1. Entry diagnostic

Before teaching, ask the learner to:

1. Calculate −3 + 5 and 4 − (−2).
2. Calculate 1/2 + (−3/2).
3. Simplify 3x + 2x and expand 2(x + 3).
4. Explain what it means for two algebraic expressions to be equivalent.

Tag issues as signed arithmetic, fraction arithmetic, distribution, expression equivalence, or unclear explanation. If a learner struggles, provide the same short scripted bridge and record it; do not automatically exclude them from learning.

### A2. Planned lesson

1. Motivate the extension with x² = −1, noting this has no real-number solution.
2. Define i² = −1 and complex numbers in the form a + bi.
3. Identify a as the real part and b as the imaginary-part coefficient; distinguish b from the term bi.
4. Add and subtract component-wise.
5. Multiply by distribution and replace i² with −1.
6. Define the conjugate a − bi; show (a + bi)(a − bi) = a² + b² for real a,b; use it to simplify a division with a non-zero denominator.
7. Do not require prior knowledge of the complex plane or polar form.

Use the same lesson across learners. Log any improvised rescue explanation instead of counting the outcome as unassisted success.

### A3. Guided checks

- (2 + 3i) + (4 − i)
- (3 + 2i) − (1 − 4i)
- (1 + 2i)(3 − i)
- Simplify (1 + i)/(1 − i) by multiplying numerator and denominator by the conjugate.

Ask the learner to explain why i² = −1 changes the product.

### A4. Independent transfer items

Do not show worked examples during this part.

1. Write a complex number whose real part is −2 and whose imaginary-part coefficient is 5.
2. Simplify (2 − i)(1 + 3i).
3. Simplify (2 + i)/(1 + i), showing the conjugate step.
4. Explain the error in the statement: “The imaginary part of 4 − 7i is −7i.”
5. Explain, in words or symbols, why (a + bi)(a − bi) is real for real a,b.

Use equivalent valid reasoning in the answer key. Have an educator check that key before testing.

### A5. Error codes

| Code | Pattern | Follow-up check |
|---|---|---|
| C1 Components | Swaps real and imaginary parts, or confuses coefficient and term | Label a, b, bi in a fresh example |
| C2 Signed arithmetic | Setup is right but sign arithmetic is wrong | Does a short signed-number bridge resolve it? |
| C3 Symbolic equivalence | Expansion or simplification error | Can the learner expand a real algebra expression first? |
| C4 Imaginary-unit rule | Misuses i² or memorizes the sign without applying the definition | Can the learner restate and apply the rule consistently? |
| C5 Conjugate/division | Incorrect conjugate or invalid fraction operation | Can the learner identify a conjugate and simplify a real fraction? |
| C6 Explanation/notation | Correct work, unclear reasoning or notation | Can the learner explain it in another representation? |
| C7 Transfer | Solves a near-copy but not a new example | Can the learner identify what changed and what method remains? |

Codes are hypotheses for follow-up, not diagnoses of ability.

### A6. Provisional scoring

The educator should finalize the scoring key before testing. As an initial working rule, mark the core outcome as met when the learner (a) correctly identifies components, including item 4; (b) solves at least two of transfer items 2–3 and one other applicable operation item; and (c) explains one key rule without an unplanned rescue explanation. Report item-level performance and bridge use, not only pass/fail.

If guided examples succeed but transfer fails, do not call the sequence validated. Check practice similarity, notation, timing and whether the explanation conveys why the method works.

## 5. Test B — CA-003: Complex plane, modulus/argument and polar form

### Intended outcome

A learner can represent a + bi as (a,b), compute modulus using distance/Pythagorean reasoning, determine an argument with correct quadrant and stated angle convention, convert rectangular to polar form, and interpret a simple multiplication geometrically. These are distinct sub-skills; failure at polar angles does not disprove the ability to plot a complex number.

### B1. Entry diagnostic

1. Plot and read ordered pairs in all four quadrants.
2. Find the hypotenuse of a right triangle with legs 3 and 4.
3. Give sine/cosine values for a familiar unit-circle angle and distinguish radians from degrees.
4. Explain how quadrant affects coordinate signs.

Record coordinate, distance, trigonometry, quadrant and angle-unit difficulties separately. Use and record any planned refreshers.

### B2. Planned lesson

1. Map a + bi to (a,b). Real part is the horizontal coordinate; the imaginary-part coefficient is the vertical coordinate.
2. Derive |a + bi| = √(a² + b²) from distance to the origin.
3. Define argument as an angle measured from the positive real axis; state the angle convention and explain quadrant choice.
4. Introduce r(cos θ + i sin θ), with r ≥ 0 and a stated angle convention.
5. Compare multiplication algebraically and geometrically with one carefully chosen example.
6. Treat powers and roots as an extension; state angle/branch conventions explicitly if included.

### B3. Independent transfer items

1. Plot z = 3 + 4i; read a point at (−2,1) into algebraic form.
2. Find the modulus of z = −3 + 4i, showing a distance argument.
3. Give a principal argument and polar form for z = −√3 + i; explain the second-quadrant choice.
4. Explain why tan θ = b/a alone does not settle the argument's quadrant.
5. Multiply (1 + i) by i, compute the result, and explain the corresponding quarter-turn.
6. If an angle is wrong, first ask the learner to plot the point and identify the quadrant before recalculating.

Use one stated angle convention in the lesson, test and answer key. For example, a principal argument may be defined in (−π, π]; accept equivalent angles where appropriate.

### B4. Error codes

| Code | Pattern | Follow-up check |
|---|---|---|
| P1 Coordinates | Axes swapped or signs misplaced | Can ordinary ordered pairs be plotted correctly? |
| P2 Modulus | Wrong distance calculation or no Pythagorean connection | Can the learner explain the right triangle? |
| P3 Argument/quadrant | Uses inverse tangent without quadrant correction | Can the learner identify the quadrant first? |
| P4 Angle units | Radians/degrees mixed | Can the learner translate a familiar angle consistently? |
| P5 Polar equivalence | Conversion does not preserve the same point/value | Can they reconstruct a = r cos θ, b = r sin θ? |
| P6 Geometric multiplication | Algebra works but geometric effect is unclear, or vice versa | Can the learner trace multiplication by i on the plane? |
| P7 Convention/scope | Confuses equivalent arguments or unstated root conventions | Was the convention explicit and the item taught? |

### B5. Score sub-skills separately

- **Representation:** plots and reads points correctly.
- **Modulus:** correct result plus a defensible distance explanation.
- **Argument/polar form:** correct quadrant, stated convention and equivalent polar form.
- **Geometric multiplication:** correct product plus a reasonable rotation explanation.

Report a profile rather than one aggregate score. A learner may be ready for complex-plane representation but not polar form; this suggests staging the lesson or bridging a gap, not blocking all of CA-003.

## 6. Edge-by-edge review plan

| Edge | Dependency claim | Evidence to inspect |
|---|---|---|
| EDGE-255 | Signed/rational arithmetic supports component-wise operations | Do errors map to signed/fraction skills, and does the brief bridge repair them? |
| EDGE-256 | Exponent notation helps with i² = −1, but a full powers/roots unit may not be a hard gate | Does a local definition/notation bridge suffice? |
| EDGE-257 | Expression reading/equivalence supports symbolic manipulation | Do expansion errors persist after a fair, brief algebra refresher? |
| EDGE-258 | Unit-circle/trig knowledge supports full polar conversion | Separate quadrant/angle errors from plotting/modulus; test the planned trig bridge |
| EDGE-269 | Quadratics motivate complex numbers but are not required for basic arithmetic | Are CA-001 outcomes achievable before the quadratic application? |
| EDGE-270 | Coordinate conventions support complex-plane plotting | Plot/read performance before and after a compact bridge |
| EDGE-271 | Pythagorean distance supports modulus | Modulus performance and the effect of a right-triangle bridge |
| EDGE-272 | Algebraic complex understanding supports the full geometric/polar cluster | Can learners connect the same number across algebraic and geometric forms? |
| EDGE-273 | Polar/geometric interpretation helps complex analysis but may not be required to begin differentiation | Can the defined initial CA-002 outcome be reached via a limit-based route? |
| EDGE-259–261 | Complex arithmetic, calculus language and proof support CA-002 | Need a separate complex-analysis diagnostic; this pilot cannot validate them |

For each edge, record: (1) precise outcome; (2) pre/post-bridge evidence and error codes; (3) whether a short bridge or lengthy reteaching was needed; (4) which sub-outcomes depend on it; (5) educator interpretation, alternatives, confidence and next test.

### Possible decisions

- **Retain Core:** A clear dependency mechanism remains after reasonable local support, with educator agreement and repeated observations.
- **Reclassify Helpful:** Learners achieve the stated outcome without prior mastery using the planned lesson/bridge; prior knowledge improves efficiency but need not gate entry.
- **Split outcome/edge:** Evidence indicates a dependency is core for one sub-outcome (such as polar conversion) but not an earlier one (such as plotting).
- **Keep open:** Evidence is mixed, task wording is suspect, the sample is small, or multiple explanations remain plausible.

As a cautious review trigger, investigate an edge if at least two learners show the same prerequisite-specific failure that the bridge resolves, or if several learners succeed without the prerequisite currently marked Core. These are prompts for review, not statistically validated cutoffs. Do not demote an edge from one anecdote or retain it only because the map already says Core.

## 7. Data-capture template

Use a non-identifying learner code and record:

| Field | Record |
|---|---|
| Learner/session | Code, date, instrument version |
| Entry diagnostic | Per-skill correct/partial/not yet secure |
| Bridge | None/planned/unplanned; content and approximate duration |
| Task result | Correct/partial/incorrect; preserve working where consented |
| Error code | C1–C7 or P1–P7 plus factual note |
| Prompt level | Independent/neutral prompt/targeted hint/explanation supplied |
| Transfer | Correct/partial/incorrect with reasoning |
| Learner feedback | Confusing wording, useful representation, perceived difficulty |
| Interpretation | Competing explanations and confidence |
| Follow-up | Revise task/lesson, re-test edge, or seek educator review |

Keep raw observations separate from interpretations. Do not use speed, confidence or verbal fluency alone as a proxy for mathematical understanding.

## 8. Exit criteria

Do not mark D-11 as fully validated until: an educator has reviewed the outcomes and keys; at least one instrument revision cycle is complete; learner evidence covers independent transfer and common errors for CA-001 and separate CA-003 sub-skills; mixed results and alternative routes are documented; CA-002 claims (EDGE-259–261 and EDGE-273) are tested separately before making claims about its prerequisites; and any workbook revision passes a new structural audit.

A successful small pilot means the lesson and diagnostic appear workable for the learners tested and produce useful error evidence. It does **not** prove the sequence is optimal for every age, background, language or course.

## 9. Related records

- [D-11 decision record](DECISION_PROPOSAL_CA001.md)
- [Batch 3 structured edge review](reviews/complex-number-split-review-v03.json)
- [Master Curriculum Map v0.3 README](README.md)
- [OpenStax Precalculus §3.1: Complex Numbers](https://openstax.org/books/precalculus/pages/3-1-complex-numbers)
- [OpenStax Algebra and Trigonometry §10.5: Polar Form](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-5-polar-form-of-complex-numbers)
