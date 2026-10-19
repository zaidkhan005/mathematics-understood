# Dependency Review — Batch 2: Powers, Polynomials, Rational Expressions, Radicals, Exponentials, and Sequences

**Batch ID:** DEPENDENCY-REVIEW-02  
**Prepared:** 2026-10-19  
**Status:** **AI-assisted desk review; educator confirmation pending.** These are draft curriculum-design judgments, not independent expert sign-off or completed empirical validation.

## Method and use

These eight recommendations reason from the current concept-cluster outcomes. Their proposed checks are future checks, not results. The workbook marks these as AI-assisted preliminary recommendations, with educator confirmation pending. Preserve the distinction between a prerequisite for the complete concept cluster and a just-in-time prerequisite for one subtopic.

The governing JSON register is [dependency-review-batch-02.json](reviews/dependency-review-batch-02.json). If this explanatory document and that register diverge, reconcile them before rebuilding the workbook.

## Recommendations

### EDGE-057 — FND-014: Powers, roots and integer exponents → ALG-012: Polynomial operations and structure

**Draft classification:** Core required

**Specific dependency mechanism:** The polynomial cluster uses powers of the variable and interprets degree/coefficient structure; exponent meaning is part of reading polynomial terms, though a brief exponent refresher can be embedded in the first polynomial lesson.

**Proposed validation check (not yet run):** Ask learners to read and compare x, x², and 3x² + 2x; check whether they can explain the exponent/degree meaning and carry out products without an exponent-law prerequisite gap.

### EDGE-059 — FND-007: Factors, multiples, primes and divisibility → ALG-013: Factorization and algebraic identities

**Draft classification:** Helpful

**Specific dependency mechanism:** Integer factors and common multiples can support factor intuition, but polynomial factorization is not simply prime factorization. Treat FND-007 as a source of examples, not a gate to learning algebraic identities.

**Proposed validation check (not yet run):** Test factoring simple polynomials such as x² + 5x + 6 and x² - 9 after teaching polynomial structure; compare performance with a separate numerical-factor diagnostic to see what actually blocks progress.

### EDGE-065 — FND-014: Powers, roots and integer exponents → ALG-015: Rational expressions and equations

**Draft classification:** Helpful

**Specific dependency mechanism:** Rational expressions are quotients of expressions/polynomials and can be introduced without prior fluency with powers and integer exponents. Powers are useful for later rational-expression examples but not for the basic fraction/domain idea.

**Proposed validation check (not yet run):** Assess simplification and excluded-value reasoning on (x² - 1)/(x - 1) and simple linear quotients before using exponent-heavy examples; insert an exponent refresher only when required.

### EDGE-066 — FND-014: Powers, roots and integer exponents → ALG-016: Radicals and rational exponents

**Draft classification:** Core required

**Specific dependency mechanism:** The radicals/rational-exponents cluster directly relies on the meaning of powers and exponent notation. Real-domain rules and equivalence manipulations build on that base.

**Proposed validation check (not yet run):** Use conversion tasks between square roots and fractional exponents, simplify simple powers, then solve a radical equation and check the result. Distinguish exponent meaning errors from domain errors.

### EDGE-068 — FND-016: Real numbers, intervals and absolute value → ALG-016: Radicals and rational exponents

**Draft classification:** Core required

**Specific dependency mechanism:** For the full radicals/rational-exponents outcome, learners need to reason about real-number domains, intervals, and valid values—especially even roots and constraints introduced by transformations. Teach any missing subskill locally as a bridge.

**Proposed validation check (not yet run):** Give real-domain tasks such as √(x - 2), distinguish domain from output range, and ask which values make a proposed equation meaningful; identify whether interval/number-order reasoning is a genuine blocker.

### EDGE-070 — FND-014: Powers, roots and integer exponents → ALG-017: Exponential and logarithmic functions

**Draft classification:** Core required

**Specific dependency mechanism:** Integer-exponent meaning underpins exponential functions as repeated multiplicative change and supports the inverse relationship between exponentials and logarithms.

**Proposed validation check (not yet run):** Translate repeated percentage growth into an exponential rule, compare it with a linear sequence, and explain the role of the exponent; check this before teaching logarithms as the inverse operation.

### EDGE-072 — FND-016: Real numbers, intervals and absolute value → ALG-017: Exponential and logarithmic functions

**Draft classification:** Helpful

**Specific dependency mechanism:** Real-number order and interval notation help state domains/ranges and logarithm constraints, but the essential positive-input restriction for logarithms can be taught explicitly in ALG-017. The whole FND-016 cluster is broader than the minimum needed.

**Proposed validation check (not yet run):** Teach log input restrictions locally, then test domain/range statements and interval notation separately. If learners understand positive inputs but struggle only with notation, treat FND-016 as a repair path rather than a hard gate.

### EDGE-074 — FND-014: Powers, roots and integer exponents → ALG-018: Sequences and elementary patterns

**Draft classification:** Helpful

**Specific dependency mechanism:** Sequences and patterns can be introduced through finite lists, tables, and recursive rules before exponent fluency. Powers are useful for geometric sequences and exponential patterns but not for every sequence.

**Proposed validation check (not yet run):** Assess arithmetic and recursive sequence rules without exponents first, then geometric sequences with powers. Separate the objectives and only require FND-014 for the latter.


## Batch summary

- Edges reviewed provisionally: **8**
- Classifications: Core required: 4; Helpful: 4.
- Educator confirmation: pending.
- Validation checks: proposed, not yet run.

## General observation

The v0.1 edge set contains some relationships that may be useful without being universal prerequisites. For instance, exponent knowledge supports polynomial and exponential content, but not every expression, rational expression, or sequence activity requires it at the outset. Use sub-outcomes, diagnostics, and just-in-time bridges to avoid unnecessary gates.

## Acceptance rule

Treat each recommendation as a hypothesis until a mathematics educator reviews the rationale and the proposed check. Do not present the classification as proven or empirical.
