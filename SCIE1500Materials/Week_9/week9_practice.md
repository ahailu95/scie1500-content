# Week 9 Practice Questions: Probability Foundations

**Theme:** Quantifying Uncertainty  
**Exam Alignment:** Q32, Q35 (setup)

---

## Quick Reference

| Concept | Formula |
|---------|---------|
| Sample space size (n coin tosses) | $\|S\| = 2^n$ |
| Complement rule | $P(A^c) = 1 - P(A)$ |
| Addition rule | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Conditional probability | $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| Independence | $P(A \cap B) = P(A) \cdot P(B)$ |
| Binomial coefficient | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| Binomial probability | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| Bayes' theorem | $P(A\|B) = \frac{P(B\|A) \cdot P(A)}{P(B)}$ |
| Herd immunity threshold | $\pi > 1 - \frac{1}{R_0}$ |

---

## Section A: Foundational Questions (W9-001 to W9-008)

### W9-001: Sample Space Size
**Difficulty:** Foundational | **Topic:** Sample Space

If a fair coin is tossed 4 times, what is the size of the sample space?

- (A) $4$
- (B) $8$
- (C) $12$
- (D) $16$
- (E) $24$

<details>
<summary>Solution</summary>

**Answer: (D)**

Each coin toss has 2 outcomes (H or T). For 4 independent tosses, the total number of outcomes is:

$$|S| = 2 \times 2 \times 2 \times 2 = 2^4 = 16$$

**Common error:** Students sometimes compute $4 \times 2 = 8$, but this undercounts. The correct approach is $2^n$ where $n$ is the number of tosses.

</details>

---

### W9-002: Sample Space (Exam Q32 Style)
**Difficulty:** Foundational | **Topic:** Sample Space | **Exam Reference:** Q32

If five coins are tossed, the size of the sample space is:

- (A) $10$, i.e., $5 \times 2$
- (B) $32$, i.e., $2^5$
- (C) $25$, i.e., $5^2$
- (D) $120$, i.e., $5!$
- (E) None of the above

<details>
<summary>Solution</summary>

**Answer: (B)**

For $n$ coin tosses, each toss has 2 possible outcomes, and the tosses are independent. By the multiplication principle:

$$|S| = 2^n = 2^5 = 32$$

**Why not $5 \times 2$?** This would only count sequences like "HXXXX" and "TXXXX" — it doesn't account for all positions having 2 choices.

**Why not $5!$?** Factorials count arrangements/permutations, not sample spaces from repeated experiments.

The sample space includes all 32 sequences: HHHHH, HHHHT, HHHTH, ..., TTTTT.

</details>

---

### W9-003: Basic Probability
**Difficulty:** Foundational | **Topic:** Basic Probability

Two fair coins are tossed. What is the probability of getting exactly one head?

- (A) $\frac{1}{4}$
- (B) $\frac{1}{3}$
- (C) $\frac{1}{2}$
- (D) $\frac{2}{3}$
- (E) $\frac{3}{4}$

<details>
<summary>Solution</summary>

**Answer: (C)**

The sample space is $S = \{HH, HT, TH, TT\}$ with 4 equally likely outcomes.

The event "exactly one head" is $A = \{HT, TH\}$ with 2 outcomes.

$$P(\text{exactly one head}) = \frac{|A|}{|S|} = \frac{2}{4} = \frac{1}{2}$$

</details>

---

### W9-004: Complement Rule
**Difficulty:** Foundational | **Topic:** Complement Rule

If the probability that a diagnostic test returns positive is 0.15, what is the probability that it returns negative?

- (A) $0.15$
- (B) $0.30$
- (C) $0.50$
- (D) $0.85$
- (E) $1.15$

<details>
<summary>Solution</summary>

**Answer: (D)**

The complement rule states: $P(A^c) = 1 - P(A)$

"Positive" and "Negative" are complementary events (one must occur).

$$P(\text{negative}) = 1 - P(\text{positive}) = 1 - 0.15 = 0.85$$

Note: Option (E) is impossible since probabilities cannot exceed 1.

</details>

---

### W9-005: Addition Rule
**Difficulty:** Foundational | **Topic:** Addition Rule

Events A and B have probabilities $P(A) = 0.3$, $P(B) = 0.4$, and $P(A \cap B) = 0.1$. What is $P(A \cup B)$?

- (A) $0.5$
- (B) $0.6$
- (C) $0.7$
- (D) $0.8$
- (E) $0.12$

<details>
<summary>Solution</summary>

**Answer: (B)**

The general addition rule is:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Substituting:
$$P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$$

We subtract $P(A \cap B)$ because outcomes in both events are counted twice when we add $P(A)$ and $P(B)$.

</details>

---

### W9-006: Disjoint Events
**Difficulty:** Foundational | **Topic:** Disjoint Events

Events A and B are mutually exclusive (disjoint). If $P(A) = 0.25$ and $P(B) = 0.35$, what is $P(A \cup B)$?

- (A) $0.0875$
- (B) $0.35$
- (C) $0.50$
- (D) $0.60$
- (E) $1.00$

<details>
<summary>Solution</summary>

**Answer: (D)**

For mutually exclusive (disjoint) events, $A \cap B = \emptyset$, so $P(A \cap B) = 0$.

The addition rule simplifies to:
$$P(A \cup B) = P(A) + P(B) = 0.25 + 0.35 = 0.60$$

**Note:** Option (A) would be $P(A) \cdot P(B)$, which is the multiplication rule for independent events—a different concept entirely.

</details>

---

### W9-007: Conditional Probability
**Difficulty:** Foundational | **Topic:** Conditional Probability

If $P(A) = 0.4$, $P(B) = 0.5$, and $P(A \cap B) = 0.2$, what is $P(A|B)$?

- (A) $0.2$
- (B) $0.4$
- (C) $0.5$
- (D) $0.8$
- (E) $1.0$

<details>
<summary>Solution</summary>

**Answer: (B)**

The conditional probability formula is:

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{0.2}{0.5} = 0.4$$

**Interpretation:** Given that B has occurred, 40% of those outcomes also have A occurring.

</details>

---

### W9-008: Independence
**Difficulty:** Foundational | **Topic:** Independence

Events A and B are independent with $P(A) = 0.3$ and $P(B) = 0.4$. What is $P(A \cap B)$?

- (A) $0.10$
- (B) $0.12$
- (C) $0.35$
- (D) $0.58$
- (E) $0.70$

<details>
<summary>Solution</summary>

**Answer: (B)**

For independent events, the multiplication rule is:

$$P(A \cap B) = P(A) \cdot P(B) = 0.3 \times 0.4 = 0.12$$

**Interpretation:** Independence means knowing one event occurred doesn't change the probability of the other. This allows simple multiplication.

</details>

---

## Section B: Intermediate Questions (W9-009 to W9-016)

### W9-009: Binomial Coefficient
**Difficulty:** Intermediate | **Topic:** Binomial Coefficient

How many ways can you choose 3 items from 5? That is, what is $\binom{5}{3}$?

- (A) $6$
- (B) $10$
- (C) $15$
- (D) $20$
- (E) $60$

<details>
<summary>Solution</summary>

**Answer: (B)**

The binomial coefficient formula is:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

$$\binom{5}{3} = \frac{5!}{3! \cdot 2!} = \frac{5 \times 4 \times 3!}{3! \times 2 \times 1} = \frac{5 \times 4}{2} = \frac{20}{2} = 10$$

**Symmetry check:** $\binom{5}{3} = \binom{5}{2}$ because choosing 3 to include is the same as choosing 2 to exclude.

</details>

---

### W9-010: Binomial Probability (Exam Q32 Style)
**Difficulty:** Intermediate | **Topic:** Binomial Probability | **Exam Reference:** Q32

If five fair coins are tossed, what is the probability of getting exactly three heads?

- (A) $\frac{3}{5} = 0.60$
- (B) $\frac{10}{32} = 0.3125$
- (C) $\frac{5}{32} = 0.15625$
- (D) $\frac{1}{32} = 0.03125$
- (E) None of the above

<details>
<summary>Solution</summary>

**Answer: (B)**

This uses the binomial probability formula:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

For fair coins, $p = 0.5$, and we want $k = 3$ heads in $n = 5$ tosses:

$$P(X = 3) = \binom{5}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^2 = 10 \times \frac{1}{32} = \frac{10}{32} = 0.3125$$

**Common error:** Option (A) $= 3/5 = 0.60$ is a distractor. The probability is NOT simply $k/n$.

</details>

---

### W9-011: Binomial Probability (Zero Heads)
**Difficulty:** Intermediate | **Topic:** Binomial Probability | **Exam Reference:** Q32

If five fair coins are tossed, what is the probability of getting zero heads?

- (A) $0$
- (B) $\frac{1}{32} \approx 0.03125$
- (C) $\frac{5}{32} \approx 0.15625$
- (D) $\frac{12}{32} = 0.375$
- (E) $\frac{1}{5} = 0.20$

<details>
<summary>Solution</summary>

**Answer: (B)**

Zero heads means all tails: TTTTT.

$$P(X = 0) = \binom{5}{0} \left(\frac{1}{2}\right)^0 \left(\frac{1}{2}\right)^5 = 1 \times 1 \times \frac{1}{32} = \frac{1}{32} \approx 0.03125$$

Alternatively: There's exactly one sequence with no heads out of 32 total sequences.

**Q32 connection:** The probability of zero heads is $\frac{1}{32} \approx 0.03125$, NOT 0.375.

</details>

---

### W9-012: Conditional vs Reverse Probability
**Difficulty:** Intermediate | **Topic:** Conditional Probability

A disease affects 5% of a population. A test has 90% sensitivity (true positive rate). If someone tests positive, we want $P(\text{Disease}|\text{Positive})$. Which statement is correct?

- (A) $P(D|+) = P(+|D) = 0.90$
- (B) $P(D|+) = P(D) = 0.05$
- (C) $P(D|+)$ requires Bayes' theorem and is generally not equal to $P(+|D)$
- (D) $P(D|+) = P(+|D) \times P(D) = 0.045$
- (E) $P(D|+)$ cannot be calculated from the given information

<details>
<summary>Solution</summary>

**Answer: (C)**

This is a crucial distinction:

- $P(+|D) = 0.90$ is the **sensitivity** (given disease, probability of positive test)
- $P(D|+)$ is the **positive predictive value** (given positive test, probability of disease)

These are NOT the same! By Bayes' theorem:

$$P(D|+) = \frac{P(+|D) \cdot P(D)}{P(+)}$$

We need $P(+)$ (which requires specificity) to compute this.

**Option (D)** gives $P(+ \cap D)$, not $P(D|+)$.

</details>

---

### W9-013: Bayes' Theorem Application
**Difficulty:** Intermediate | **Topic:** Bayes' Theorem

A disease has 1% prevalence. A test has 99% sensitivity and 95% specificity. What is the probability that someone with a positive test actually has the disease?

- (A) $0.99$
- (B) $0.95$
- (C) $0.50$
- (D) $0.17$
- (E) $0.01$

<details>
<summary>Solution</summary>

**Answer: (D)**

**Given:**
- $P(D) = 0.01$ (prevalence)
- $P(+|D) = 0.99$ (sensitivity)
- $P(-|D^c) = 0.95$, so $P(+|D^c) = 0.05$ (false positive rate)

**Using Bayes' theorem:**

$$P(D|+) = \frac{P(+|D) \cdot P(D)}{P(+|D) \cdot P(D) + P(+|D^c) \cdot P(D^c)}$$

$$= \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99}$$

$$= \frac{0.0099}{0.0099 + 0.0495} = \frac{0.0099}{0.0594} \approx 0.167$$

**Interpretation:** Even with a 99% sensitive test, only about 17% of positive results are true positives when the disease is rare!

</details>

---

### W9-014: Independent vs Disjoint
**Difficulty:** Intermediate | **Topic:** Independence vs Disjoint

If events A and B are disjoint (mutually exclusive) with $P(A) = 0.3$ and $P(B) = 0.4$, are they independent?

- (A) Yes, because $P(A \cup B) = P(A) + P(B)$
- (B) Yes, because knowing one occurred tells us about the other
- (C) No, because $P(A \cap B) = 0 \neq P(A) \cdot P(B) = 0.12$
- (D) No, because $P(A) \neq P(B)$
- (E) Cannot determine without more information

<details>
<summary>Solution</summary>

**Answer: (C)**

**Key distinction:**

- **Disjoint** means $A \cap B = \emptyset$, so $P(A \cap B) = 0$
- **Independent** means $P(A \cap B) = P(A) \cdot P(B)$

For these events:
- $P(A \cap B) = 0$ (disjoint)
- $P(A) \cdot P(B) = 0.3 \times 0.4 = 0.12$

Since $0 \neq 0.12$, they are **NOT independent**.

**Intuition:** If A occurs, we know B didn't occur (they're disjoint). This means knowing A affects the probability of B — the opposite of independence!

**Key concept:** Disjoint events with positive probability are NEVER independent.

</details>

---

### W9-015: Complement with Independence
**Difficulty:** Intermediate | **Topic:** Complement Rule with Independence

The probability of disease transmission per contact is 0.2. What is the probability of at least one transmission in 3 independent contacts?

- (A) $0.008$
- (B) $0.488$
- (C) $0.512$
- (D) $0.60$
- (E) $0.80$

<details>
<summary>Solution</summary>

**Answer: (B)**

**Strategy:** Use complement rule.

$$P(\text{at least one}) = 1 - P(\text{none})$$

For independent contacts with transmission probability $p = 0.2$:

$$P(\text{no transmission in 3 contacts}) = (1 - 0.2)^3 = 0.8^3 = 0.512$$

$$P(\text{at least one transmission}) = 1 - 0.512 = 0.488$$

**Note:** Option (A) = $0.2^3$ is the probability of ALL three transmitting.
Option (D) = $3 \times 0.2$ is incorrect (can exceed 1 for larger n).

**Key concept:** $P(\text{at least one}) = 1 - P(\text{none}) = 1 - (1-p)^n$

</details>

---

### W9-016: Herd Immunity
**Difficulty:** Intermediate | **Topic:** Epidemiology

A disease has $R_0 = 4$. What proportion of the population must be immune to achieve herd immunity?

- (A) $25\%$
- (B) $50\%$
- (C) $75\%$
- (D) $80\%$
- (E) $96\%$

<details>
<summary>Solution</summary>

**Answer: (C)**

The herd immunity threshold is:

$$\pi > 1 - \frac{1}{R_0}$$

For $R_0 = 4$:

$$\pi > 1 - \frac{1}{4} = 1 - 0.25 = 0.75 = 75\%$$

**Interpretation:** At least 75% of the population must be immune (through vaccination or recovery) for the effective reproduction number $R_e = s \cdot R_0 < 1$.

</details>

---

## Section C: Exam-Style Questions (W9-017 to W9-020)

### W9-017: Comprehensive Coin Toss Problem (Q32 Style)
**Difficulty:** Exam Style | **Topic:** Comprehensive | **Exam Reference:** Q32

If five coins are tossed, which of the following is TRUE?

(a) The size of the sample space is 10, i.e., $5 \times 2$.  
(b) The size of the sample space is 32, i.e., $2^5$.  
(c) The probability of getting exactly three heads is 0.60.  
(d) The probability of getting zero heads is 0.375.  
(e) None of the above.

<details>
<summary>Solution</summary>

**Analysis of each statement:**

**(a) FALSE:** The sample space is $2^5 = 32$, not $5 \times 2 = 10$. Each of the 5 tosses has 2 outcomes, so we multiply: $2 \times 2 \times 2 \times 2 \times 2 = 32$.

**(b) TRUE:** ✓ The sample space has $2^5 = 32$ elements.

**(c) FALSE:** 
$$P(X=3) = \binom{5}{3} \left(\frac{1}{2}\right)^5 = 10 \times \frac{1}{32} = \frac{10}{32} = 0.3125$$
Not 0.60.

**(d) FALSE:**
$$P(X=0) = \binom{5}{0} \left(\frac{1}{2}\right)^5 = 1 \times \frac{1}{32} = 0.03125$$
Not 0.375.

**Answer: Statement (b) is TRUE**

</details>

---

### W9-018: Medical Test Analysis
**Difficulty:** Exam Style | **Topic:** Bayes' Theorem Application

A medical test for a disease has the following characteristics:
- Sensitivity: 95% (the test correctly identifies 95% of people who have the disease)
- Specificity: 90% (the test correctly identifies 90% of people who do not have the disease)
- Prevalence: 2% of the population has the disease

**(a)** If a person tests positive, what is the probability they actually have the disease?

**(b)** Why is this result perhaps surprising given the high sensitivity?

<details>
<summary>Solution</summary>

**(a) Computing PPV using Bayes' theorem:**

**Given:**
- $P(D) = 0.02$ (prevalence)
- $P(+|D) = 0.95$ (sensitivity)
- $P(-|D^c) = 0.90$, so $P(+|D^c) = 0.10$ (false positive rate)

**Step 1:** Compute $P(+)$ using total probability:
$$P(+) = P(+|D) \cdot P(D) + P(+|D^c) \cdot P(D^c)$$
$$= 0.95 \times 0.02 + 0.10 \times 0.98$$
$$= 0.019 + 0.098 = 0.117$$

**Step 2:** Apply Bayes' theorem:
$$P(D|+) = \frac{P(+|D) \cdot P(D)}{P(+)} = \frac{0.019}{0.117} \approx 0.162$$

**Answer: $P(D|+) \approx 16.2\%$**

**(b) Why surprising?**

Even with 95% sensitivity, only about 16% of positive tests are true positives because:

1. **The disease is rare** (2% prevalence)
2. **False positives dominate:** In 1000 people:
   - 20 have disease → 19 test positive (true positives)
   - 980 healthy → 98 test positive (false positives)
   - Total positives: 117, but only 19 are true

**Key insight:** When prevalence is low, even small false positive rates generate many false positives.

</details>

---

### W9-019: Hypothesis Testing Setup (Q35 Style)
**Difficulty:** Exam Style | **Topic:** Conditional Probability | **Exam Reference:** Q35 Setup

A new virus variant is suspected to be more infectious than an older variant, which had a transmission probability of $p = 0.50$. In 11 contact tracing cases, 9 resulted in infections.

**(a)** If the true transmission probability were still $p = 0.50$, what is the probability of observing 9 or more infections out of 11 contacts?

**(b)** How would this probability help scientists evaluate whether the new variant is more infectious?

<details>
<summary>Solution</summary>

**(a) Computing $P(X \geq 9)$ when $p = 0.50$:**

First, compute the binomial coefficients:
- $\binom{11}{9} = \frac{11!}{9! \cdot 2!} = \frac{11 \times 10}{2} = 55$
- $\binom{11}{10} = \frac{11!}{10! \cdot 1!} = 11$
- $\binom{11}{11} = 1$

Now compute the probability:
$$P(X \geq 9) = (55 + 11 + 1) \times (0.5)^{11}$$
$$= 67 \times \frac{1}{2048}$$
$$= \frac{67}{2048} \approx 0.0327$$

**Answer: $P(X \geq 9) \approx 3.27\%$ or $0.033$**

**(b) Scientific interpretation:**

This probability (≈ 3.3%) represents how likely we would observe such extreme results **if the null hypothesis ($p = 0.50$) were true**.

Since this probability is less than 5% (a common significance threshold):
- The observed data would be considered **statistically significant**
- Scientists would have evidence to **reject the null hypothesis**
- This supports the claim that the new variant is more infectious

**This is the foundation for hypothesis testing (Week 10):** comparing observed data to what we'd expect under a null hypothesis.

</details>

---

### W9-020: Two-Stage Screening Protocol
**Difficulty:** Exam Style | **Topic:** Comprehensive Probability

Consider a two-stage screening protocol for HIV:
- Stage 1: ELISA test with 99.5% sensitivity and 99.9% specificity
- Stage 2 (if Stage 1 positive): Western Blot with 99.9% sensitivity and 99.9% specificity
- Population prevalence: 0.1%

**(a)** What is the positive predictive value (PPV) after just the first test?

**(b)** What is the PPV after both tests are positive?

**(c)** Why is two-stage testing used despite the first test being very accurate?

<details>
<summary>Solution</summary>

**(a) PPV after Stage 1 only:**

**Given:** $P(D) = 0.001$, $P(T_1^+|D) = 0.995$, $P(T_1^+|D^c) = 0.001$

$$P(T_1^+) = 0.995 \times 0.001 + 0.001 \times 0.999 = 0.000995 + 0.000999 = 0.001994$$

$$PPV_1 = P(D|T_1^+) = \frac{0.000995}{0.001994} \approx 0.499$$

**Answer: $PPV_1 \approx 49.9\%$**

**(b) PPV after both stages positive:**

Among those who test positive in Stage 1:
- $P(D|T_1^+) = 0.499$ (from part a)
- $P(D^c|T_1^+) = 0.501$

Stage 2 probabilities:
- $P(T_2^+|D) = 0.999$
- $P(T_2^+|D^c) = 0.001$

$$P(D \cap T_2^+|T_1^+) = 0.499 \times 0.999 = 0.4985$$
$$P(D^c \cap T_2^+|T_1^+) = 0.501 \times 0.001 = 0.000501$$

$$PPV_2 = \frac{0.4985}{0.4985 + 0.000501} \approx \frac{0.4985}{0.499} \approx 0.999$$

**Answer: $PPV_2 \approx 99.9\%$**

**(c) Why two-stage testing?**

Even with a 99.5% sensitive and 99.9% specific first test:
- **Single-stage PPV ≈ 50%** — half of positives are false positives
- **Two-stage PPV ≈ 99.9%** — nearly all positives are true positives

**Reasons for two-stage:**
1. Dramatically reduces false positives
2. More cost-effective than running expensive confirmatory tests on everyone
3. Reduces psychological harm from false positive diagnoses
4. Ethical imperative for life-altering diagnoses

</details>

---

## Answers Summary

| Question | Answer |
|----------|--------|
| W9-001 | D |
| W9-002 | B |
| W9-003 | C |
| W9-004 | D |
| W9-005 | B |
| W9-006 | D |
| W9-007 | B |
| W9-008 | B |
| W9-009 | B |
| W9-010 | B |
| W9-011 | B |
| W9-012 | C |
| W9-013 | D |
| W9-014 | C |
| W9-015 | B |
| W9-016 | C |
| W9-017 | (b) TRUE |
| W9-018 | See solution |
| W9-019 | See solution |
| W9-020 | See solution |

---

## Lab Connection

These practice questions connect to the Python lab exercises:

| Lab Exercise | Topic | Related Questions |
|--------------|-------|-------------------|
| A | Coin toss simulation | W9-001, W9-002, W9-010 |
| B | Binomial probability computation | W9-009, W9-011 |
| C | Bayes' theorem calculator | W9-013, W9-018 |
| D | Disease screening simulation | W9-020 |
| E | Herd immunity threshold visualization | W9-016 |
