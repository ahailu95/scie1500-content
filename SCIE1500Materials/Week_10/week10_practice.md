# Week 10: Practice Questions
## Random Variables and Hypothesis Testing

**Theme:** Making Decisions Under Uncertainty  
**Exam Alignment:** Q33 (Expected Value), Q35 (Hypothesis Testing)

---

### Question 1 (Foundational)
**Topic:** Random Variable Definition

A random variable $X$ represents the number of infected individuals in a sample of 5 contacts. Which of the following is a valid set of values that $X$ can take?

- (A) $\{-1, 0, 1, 2, 3, 4, 5\}$
- (B) $\{0, 1, 2, 3, 4, 5\}$
- (C) $\{0.5, 1.5, 2.5, 3.5, 4.5\}$
- (D) $\{1, 2, 3, 4, 5\}$
- (E) Any real number between 0 and 5

**Answer:** B

---

### Question 2 (Foundational)
**Topic:** Expected Value Concept

If the expected value of a random variable $X$ is $E[X] = 2.7$, which statement is correct?

- (A) $X$ will always equal 2.7
- (B) $X = 2.7$ is the most likely outcome
- (C) The long-run average of $X$ values will approach 2.7
- (D) $X$ must be able to take the value 2.7
- (E) The probability $P(X = 2.7) = 1$

**Answer:** C

---

### Question 3 (Foundational) — Exam Style Q33
**Topic:** Expected Value Calculation

A random variable $X$ has the following probability distribution:

| $x$ | 0 | 3 | 4 | 6 |
|-----|---|---|---|---|
| $P(X=x)$ | 0.2 | 0.4 | 0.3 | 0.1 |

What is $E[X]$?

- (A) 1.0
- (B) 2.0
- (C) 3.0
- (D) 4.0
- (E) 3.25

**Answer:** C

**Solution:**
$$E[X] = 0(0.2) + 3(0.4) + 4(0.3) + 6(0.1) = 0 + 1.2 + 1.2 + 0.6 = 3.0$$

---

### Question 4 (Foundational)
**Topic:** Bernoulli Expected Value

A diagnostic test returns $X = 1$ (positive) with probability 0.15 and $X = 0$ (negative) with probability 0.85. What is $E[X]$?

- (A) 0
- (B) 0.15
- (C) 0.50
- (D) 0.85
- (E) 1

**Answer:** B

---

### Question 5 (Foundational)
**Topic:** Variance Concept

The variance of a random variable measures:

- (A) The most likely value
- (B) The average value
- (C) How spread out the values are around the mean
- (D) The maximum possible value
- (E) The probability of the most common outcome

**Answer:** C

---

### Question 6 (Foundational)
**Topic:** Bernoulli Variance

If $X \sim \text{Bernoulli}(0.3)$, what is $\text{Var}(X)$?

- (A) 0.09
- (B) 0.21
- (C) 0.30
- (D) 0.49
- (E) 0.70

**Answer:** B

**Solution:**
$$\text{Var}(X) = p(1-p) = 0.3 \times 0.7 = 0.21$$

---

### Question 7 (Foundational)
**Topic:** Binomial Distribution

If 10 independent contacts each have a 0.4 probability of resulting in disease transmission, and $X$ = number of transmissions, then $X$ follows which distribution?

- (A) $\text{Bernoulli}(0.4)$
- (B) $\text{Binomial}(10, 0.4)$
- (C) $\text{Normal}(4, 2.4)$
- (D) $\text{Poisson}(4)$
- (E) $\text{Binomial}(0.4, 10)$

**Answer:** B

---

### Question 8 (Foundational)
**Topic:** Binomial Mean

For $X \sim \text{Binomial}(20, 0.6)$, what is $E[X]$?

- (A) 6
- (B) 8
- (C) 10
- (D) 12
- (E) 20

**Answer:** D

**Solution:**
$$E[X] = np = 20 \times 0.6 = 12$$

---

### Question 9 (Intermediate)
**Topic:** Hypothesis Formulation

Researchers claim a new vaccine reduces infection rates below the baseline of 30%. To test this claim, the correct hypotheses are:

- (A) $H_0: p = 0.30$, $H_a: p \neq 0.30$
- (B) $H_0: p \geq 0.30$, $H_a: p < 0.30$
- (C) $H_0: p \leq 0.30$, $H_a: p > 0.30$
- (D) $H_0: p < 0.30$, $H_a: p \geq 0.30$
- (E) $H_0: p = 0.30$, $H_a: p > 0.30$

**Answer:** B

---

### Question 10 (Intermediate) — Critical for Q35
**Topic:** One-Tailed vs Two-Tailed Tests

Health experts suspect that a new virus variant is **more infectious** than the old one (which had $p = 0.50$). What type of hypothesis test is appropriate?

- (A) Two-tailed test with $H_0: p = 0.50$ vs $H_a: p \neq 0.50$
- (B) One-tailed test with $H_0: p \leq 0.50$ vs $H_a: p > 0.50$
- (C) One-tailed test with $H_0: p \geq 0.50$ vs $H_a: p < 0.50$
- (D) Two-tailed test with $H_0: p \leq 0.50$ vs $H_a: p > 0.50$
- (E) No test is needed—the data will show the answer directly

**Answer:** B

**Key Point:** Since we're testing if the variant is *more* infectious (a specific direction), we use a one-tailed test.

---

### Question 11 (Intermediate)
**Topic:** p-Value Interpretation

A p-value of 0.03 means:

- (A) There is a 3% chance the null hypothesis is true
- (B) There is a 3% chance the alternative hypothesis is true
- (C) If the null hypothesis is true, there is a 3% chance of observing data this extreme or more extreme
- (D) The treatment is 97% effective
- (E) 3% of the population is affected

**Answer:** C

---

### Question 12 (Intermediate)
**Topic:** Decision Rule

At the 5% significance level, a hypothesis test with p-value = 0.07 leads to which conclusion?

- (A) Reject $H_0$ because 0.07 is small
- (B) Reject $H_0$ because 0.07 > 0.05
- (C) Fail to reject $H_0$ because 0.07 > 0.05
- (D) Accept $H_0$ with 93% confidence
- (E) The test is inconclusive and must be repeated

**Answer:** C

---

### Question 13 (Intermediate)
**Topic:** Type I Error

A Type I error occurs when:

- (A) We fail to reject a false null hypothesis
- (B) We reject a true null hypothesis
- (C) We accept the alternative hypothesis
- (D) The p-value is very small
- (E) The sample size is too large

**Answer:** B

---

### Question 14 (Intermediate)
**Topic:** Type II Error

A Type II error occurs when:

- (A) We reject a true null hypothesis
- (B) We fail to reject a false null hypothesis
- (C) The alternative hypothesis is not specified
- (D) We use a two-tailed test instead of one-tailed
- (E) The sample is biased

**Answer:** B

---

### Question 15 (Intermediate)
**Topic:** Binomial Probability Formula

If $X \sim \text{Binomial}(11, 0.5)$, what is $P(X = 9)$?

- (A) $\binom{11}{9}(0.5)^9(0.5)^2$
- (B) $\binom{11}{9}(0.5)^{11}$
- (C) $\binom{9}{11}(0.5)^9(0.5)^2$
- (D) $(0.5)^9(0.5)^2$
- (E) $\frac{9}{11}$

**Answer:** B

---

### Question 16 (Intermediate)
**Topic:** p-Value Calculation

For testing $H_0: p \leq 0.5$ vs $H_a: p > 0.5$ with observed data $X = 9$ out of $n = 11$ and $p_0 = 0.5$, the p-value is:

- (A) $P(X = 9 \;|\; p = 0.5)$
- (B) $P(X \geq 9 \;|\; p = 0.5)$
- (C) $P(X \leq 9 \;|\; p = 0.5)$
- (D) $P(X = 9 \;|\; p > 0.5)$
- (E) $P(X < 9 \;|\; p = 0.5)$

**Answer:** B

---

### Question 17 (Exam Style)
**Topic:** Expected Value Advanced

A random variable $X$ has probability distribution:

| $x$ | 1 | 2 | 5 | 8 |
|-----|---|---|---|---|
| $P(X=x)$ | 0.1 | 0.3 | 0.4 | 0.2 |

What is $E[X]$?

- (A) 3.0
- (B) 4.0
- (C) 4.3
- (D) 5.0
- (E) 5.5

**Answer:** C

**Solution:**
$$E[X] = 1(0.1) + 2(0.3) + 5(0.4) + 8(0.2) = 0.1 + 0.6 + 2.0 + 1.6 = 4.3$$

---

### Question 18 (Exam Style) — Q35 Type
**Topic:** Complete Hypothesis Testing

Health experts suspect that a new variant of a virus is more infectious than an older one, which had an infection rate of 50%. Out of 11 recent contacts, 9 resulted in infections. The probability of observing 9 or more infections out of 11 if $p = 0.50$ is $\frac{67}{2048} \approx 0.033$. If you test at the 5% significance level, which conclusion is correct?

- (A) Using $H_0: p \leq 0.50$, $H_a: p > 0.50$: reject $H_0$ at 5% significance
- (B) Using $H_0: p = 0.50$, $H_a: p \neq 0.50$: reject $H_0$ at 5% significance
- (C) Using $H_0: p \leq 0.50$, $H_a: p > 0.50$: fail to reject $H_0$ at 5% significance
- (D) Using $H_0: p = 0.50$, $H_a: p \neq 0.50$: fail to reject $H_0$ at 5% significance
- (E) Using $H_0: p \geq 0.50$, $H_a: p < 0.50$: reject $H_0$ at 5% significance

**Answer:** A

**Critical Explanation:**
- The question asks if the variant is *more* infectious → use one-tailed test
- $H_0: p \leq 0.50$ vs $H_a: p > 0.50$
- p-value = 0.033 < 0.05 → Reject $H_0$

---

### Question 19 (Exam Style)
**Topic:** Two-Tailed Test

A coin is tested for fairness. In 100 flips, 62 heads are observed. For a two-tailed test of $H_0: p = 0.5$ vs $H_a: p \neq 0.5$, which values would be included in the p-value calculation?

- (A) Only $P(X = 62)$
- (B) $P(X \geq 62)$
- (C) $P(X \leq 38)$
- (D) $P(X \leq 38) + P(X \geq 62)$
- (E) $P(38 \leq X \leq 62)$

**Answer:** D

---

### Question 20 (Exam Style)
**Topic:** Critical Value

For a one-tailed test of $H_0: p \leq 0.40$ vs $H_a: p > 0.40$ with $n = 20$ and $\alpha = 0.05$, the critical value $k^*$ is the smallest integer such that $P(X \geq k^*) < 0.05$. Given:

- $P(X \geq 10) \approx 0.245$
- $P(X \geq 11) \approx 0.128$
- $P(X \geq 12) \approx 0.057$
- $P(X \geq 13) \approx 0.021$

What is $k^*$?

- (A) 10
- (B) 11
- (C) 12
- (D) 13
- (E) 14

**Answer:** D

**Solution:** We need $P(X \geq k^*) < 0.05$. The first value satisfying this is $k^* = 13$ with $P(X \geq 13) = 0.021 < 0.05$.

---

## Summary of Key Formulas

| Concept | Formula |
|---------|---------|
| Expected value | $E[X] = \sum_x x \cdot P(X = x)$ |
| Variance | $\text{Var}(X) = E[X^2] - (E[X])^2$ |
| Bernoulli | $E[X] = p$, $\text{Var}(X) = p(1-p)$ |
| Binomial PMF | $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$ |
| Binomial mean | $E[X] = np$ |
| p-value (upper tail) | $P(X \geq k \;|\; H_0)$ |
