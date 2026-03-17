# Week 3 Practice Questions: Logistic Functions and Bounded Growth

**Theme:** "When Growth Has Limits"  
**Exam Alignment:** Q8, Q13, Q17, Q20, Q23

---

## Foundational Questions (1–8)

### Question W3-001 | Logistic Function Basics

A population follows the logistic equation $P(t) = \frac{K}{1 + Ae^{-\alpha t}}$. What happens to $P(t)$ as $t \to \infty$?

**(A)** $P(t) \to 0$  
**(B)** $P(t) \to K$  
**(C)** $P(t) \to A$  
**(D)** $P(t) \to \infty$  
**(E)** $P(t) \to \alpha$

<details>
<summary>Solution</summary>

**Answer: B**

As $t \to \infty$, $e^{-\alpha t} \to 0$ (assuming $\alpha > 0$). Therefore, $1 + Ae^{-\alpha t} \to 1$, and $P(t) \to \frac{K}{1} = K$. 

**Key Concept:** The carrying capacity $K$ is the horizontal asymptote as $t → ∞$.
</details>

---

### Question W3-002 | Logistic Initial Value

For the logistic function $P(t) = \frac{8000}{1 + 39e^{-0.2t}}$, what is the initial population $P(0)$?

**(A)** 200  
**(B)** 400  
**(C)** 4000  
**(D)** 8000  
**(E)** 39

<details>
<summary>Solution</summary>

**Answer: A**

$$P(0) = \frac{8000}{1 + 39e^{0}} = \frac{8000}{1 + 39} = \frac{8000}{40} = 200$$

**Key Concept:** To find initial value, substitute $t = 0$ and note that $e^0 = 1$.
</details>

---

### Question W3-003 | Schaefer Model Basics

In the Schaefer model $G(S) = gS(1 - S/K)$, what does the term $(1 - S/K)$ represent?

**(A)** The intrinsic growth rate  
**(B)** The carrying capacity  
**(C)** The compensating factor that reduces growth as population increases  
**(D)** The fishing effort  
**(E)** The sustainable yield

<details>
<summary>Solution</summary>

**Answer: C**

The term $(1 - S/K)$ is the **compensating factor**. When $S$ is small relative to $K$, this factor is close to 1 and has little effect. As $S$ approaches $K$, this factor approaches 0, causing growth to slow and eventually stop at the carrying capacity.

**Key Concept:** The compensating factor models resource competition and environmental constraints.
</details>

---

### Question W3-004 | MSY Calculation

A fish population has intrinsic growth rate $g = 0.08$ per year and carrying capacity $K = 20000$ tonnes. Calculate the Maximum Sustainable Yield (MSY).

<details>
<summary>Solution</summary>

**Answer: 400 tonnes/year**

$$\text{MSY} = \frac{gK}{4} = \frac{0.08 \times 20000}{4} = \frac{1600}{4} = 400 \text{ tonnes/year}$$

Alternatively, at $S_{MSY} = K/2 = 10000$ tonnes:

$$G_{MSY} = 0.08 \times 10000 \times (1 - 10000/20000) = 800 \times 0.5 = 400 \text{ tonnes/year}$$

**Key Concept:** MSY $= gK/4$ and occurs when stock is at $K/2$.
</details>

---

### Question W3-005 | Arithmetic Sequence

Find the 15th term of the arithmetic sequence: 7, 12, 17, 22, ...

**(A)** 72  
**(B)** 77  
**(C)** 82  
**(D)** 87  
**(E)** 67

<details>
<summary>Solution</summary>

**Answer: B**

First term $a_1 = 7$, common difference $d = 12 - 7 = 5$.

$$a_n = a_1 + (n-1)d$$
$$a_{15} = 7 + (15-1)(5) = 7 + 14 \times 5 = 7 + 70 = 77$$

**Key Concept:** Arithmetic sequence formula: $a_n = a_1 + (n-1)d$
</details>

---

### Question W3-006 | Function Composition

Given $f(x) = x^2 + 1$ and $g(x) = 3x$, find $(f \circ g)(2)$.

<details>
<summary>Solution</summary>

**Answer: 37**

$(f \circ g)(2) = f(g(2))$

First: $g(2) = 3(2) = 6$

Then: $f(6) = 6^2 + 1 = 36 + 1 = 37$

**Key Concept:** Function composition: first apply the inner function, then the outer.
</details>

---

### Question W3-007 | Inverse Function

What is the inverse of $f(x) = 2x - 6$?

**(A)** $f^{-1}(x) = \frac{x + 6}{2}$  
**(B)** $f^{-1}(x) = \frac{x - 6}{2}$  
**(C)** $f^{-1}(x) = 2x + 6$  
**(D)** $f^{-1}(x) = \frac{1}{2x - 6}$  
**(E)** $f^{-1}(x) = -2x + 6$

<details>
<summary>Solution</summary>

**Answer: A**

Let $y = 2x - 6$. Solve for $x$:
$$y + 6 = 2x$$
$$x = \frac{y + 6}{2}$$

Swap $x$ and $y$: $f^{-1}(x) = \frac{x + 6}{2}$

**Verification:** 
$$f(f^{-1}(x)) = f\left(\frac{x+6}{2}\right) = 2 \cdot \frac{x+6}{2} - 6 = x + 6 - 6 = x \checkmark$$

**Key Concept:** To find inverse: solve $y = f(x)$ for $x$, then swap $x$ and $y$.
</details>

---

### Question W3-008 | Schaefer Growth Rate

In the Schaefer model with $g = 0.1$ and $K = 10000$, what is the actual growth rate (as a proportion) when $S = 2500$?

**(A)** 2.5%  
**(B)** 5.0%  
**(C)** 7.5%  
**(D)** 10.0%  
**(E)** 12.5%

<details>
<summary>Solution</summary>

**Answer: C**

Actual growth rate $= g(1 - S/K) = 0.1(1 - 2500/10000) = 0.1(1 - 0.25) = 0.1 \times 0.75 = 0.075 = 7.5\%$

**Key Concept:** Actual growth rate $= g(1 - S/K)$, which declines linearly with stock.
</details>

---

## Intermediate Questions (9–16)

### Question W3-009 | Logistic Time Calculation ⭐ [Exam Q8]

A population follows $P(t) = \frac{15000}{1 + 120e^{-0.15t}}$. How many time periods does it take to reach 50% of carrying capacity? Round to a whole number.

<details>
<summary>Solution</summary>

**Answer: 32 time periods**

50% of carrying capacity $= 15000/2 = 7500$

$$7500 = \frac{15000}{1 + 120e^{-0.15t}}$$

$$1 + 120e^{-0.15t} = 2$$

$$120e^{-0.15t} = 1$$

$$e^{-0.15t} = \frac{1}{120}$$

$$-0.15t = \ln(1/120) = -\ln(120) \approx -4.787$$

$$t = \frac{4.787}{0.15} \approx 31.9 \approx 32 \text{ time periods}$$

**Key Concept:** This is Q8 from the exam. Use logarithms to solve for time in logistic equations.
</details>

---

### Question W3-010 | Schaefer Growth Calculation

A fishery has $g = 0.12$ and $K = 8000$ tonnes. Calculate the growth $G(S)$ when the stock is at 2000 tonnes.

<details>
<summary>Solution</summary>

**Answer: 180 tonnes/year**

$$G(S) = gS(1 - S/K)$$

$$G(2000) = 0.12 \times 2000 \times (1 - 2000/8000)$$

$$= 240 \times (1 - 0.25)$$

$$= 240 \times 0.75$$

$$= 180 \text{ tonnes/year}$$

**Key Concept:** Direct application of the Schaefer growth formula.
</details>

---

### Question W3-011 | Composition Order

If $f(x) = e^x$ and $g(x) = \ln(x)$, which statement is TRUE?

**(A)** $(f \circ g)(x) = (g \circ f)(x) = x$ for all $x > 0$  
**(B)** $(f \circ g)(x) = x$ for $x > 0$, but $(g \circ f)(x) = x$ for all real $x$  
**(C)** $(f \circ g)(x) \neq (g \circ f)(x)$ for any $x$  
**(D)** $(f \circ g)(x) = e^{\ln(x)} = x^e$  
**(E)** Neither composition equals $x$

<details>
<summary>Solution</summary>

**Answer: B**

$(f \circ g)(x) = f(g(x)) = f(\ln(x)) = e^{\ln(x)} = x$ (valid for $x > 0$)

$(g \circ f)(x) = g(f(x)) = g(e^x) = \ln(e^x) = x$ (valid for all real $x$)

Both equal $x$, but with different domains. Since $\ln(x)$ requires $x > 0$, $(f \circ g)(x) = x$ only for $x > 0$.

**Key Concept:** $\exp$ and $\ln$ are inverse functions, but domain restrictions matter.
</details>

---

### Question W3-012 | Arithmetic Series

Find the sum of the first 20 terms of the arithmetic sequence: 3, 8, 13, 18, ...

<details>
<summary>Solution</summary>

**Answer: 1010**

First term $a_1 = 3$, common difference $d = 5$

Last term: $a_{20} = 3 + (20-1)(5) = 3 + 95 = 98$

Sum: $S_{20} = \frac{20}{2}(a_1 + a_{20}) = 10(3 + 98) = 10 \times 101 = 1010$

Alternatively: $S_n = \frac{n}{2}[2a_1 + (n-1)d] = \frac{20}{2}[6 + 19(5)] = 10[6 + 95] = 1010$

**Key Concept:** Arithmetic series formula: $S_n = \frac{n}{2}(a_1 + a_n)$
</details>

---

### Question W3-013 | Logistic Parameter A

A logistic function has carrying capacity $K = 5000$ and initial value $P(0) = 100$. What is the value of parameter $A$?

**(A)** 49  
**(B)** 50  
**(C)** 99  
**(D)** 4900  
**(E)** 5000

<details>
<summary>Solution</summary>

**Answer: A**

From $P(0) = \frac{K}{1 + A}$, we have $A = \frac{K}{P(0)} - 1$

$$A = \frac{5000}{100} - 1 = 50 - 1 = 49$$

**Key Concept:** $A = K/P(0) - 1$ relates initial value to carrying capacity.
</details>

---

### Question W3-014 | Inverse Verification

Given $f(x) = \frac{2x + 3}{5}$, find $f^{-1}(x)$ and verify that $f(f^{-1}(3)) = 3$.

<details>
<summary>Solution</summary>

**Finding inverse:**

Let $y = \frac{2x + 3}{5}$

$5y = 2x + 3$

$2x = 5y - 3$

$x = \frac{5y - 3}{2}$

So $f^{-1}(x) = \frac{5x - 3}{2}$

**Verification:**

$f^{-1}(3) = \frac{5(3) - 3}{2} = \frac{12}{2} = 6$

$f(6) = \frac{2(6) + 3}{5} = \frac{15}{5} = 3 \checkmark$

**Key Concept:** Always verify inverse by checking $f(f^{-1}(x)) = x$.
</details>

---

### Question W3-015 | Schaefer Properties ⭐ [Exam Q13]

Which of the following statements about the Schaefer model $G(S) = gS(1 - S/K)$ is TRUE?

**(A)** Growth is always positive for any stock level  
**(B)** The actual growth rate $G(S)/S$ increases linearly with stock  
**(C)** Maximum growth occurs at $S = K$  
**(D)** Growth $G(S)$ is highest when stock is at half the carrying capacity  
**(E)** Growth is independent of stock level

<details>
<summary>Solution</summary>

**Answer: D**

The Schaefer model is a quadratic in $S$ that opens downward. Its vertex (maximum) occurs at $S = K/2$.

- Option A is false: $G(S) < 0$ when $S > K$
- Option B is false: actual growth rate $g(1-S/K)$ decreases linearly
- Option C is false: $G(K) = 0$
- Option E is false: $G(S)$ clearly depends on $S$

**Key Concept:** MSY occurs at $S = K/2$ where the parabola reaches its vertex.
</details>

---

### Question W3-016 | Nested Composition

If $f(x) = x + 2$, $g(x) = 3x$, and $h(x) = x^2$, find $(f \circ g \circ h)(2)$.

<details>
<summary>Solution</summary>

**Answer: 14**

Work from inside out:

$h(2) = 2^2 = 4$

$g(h(2)) = g(4) = 3(4) = 12$

$f(g(h(2))) = f(12) = 12 + 2 = 14$

So $(f \circ g \circ h)(2) = 14$

**Key Concept:** For multiple compositions, work from innermost function outward.
</details>

---

## Exam-Style Questions (17–20)

### Question W3-017 | Logistic Comprehensive ⭐ [Exam Q17]

Consider a population trajectory described by the logistic equation: $P(t) = \frac{K}{1+Ae^{-\alpha t}}$ where $K$, $A$, and $\alpha$ are positive values. Which of the following statements is TRUE?

(a) The equation can be used to describe biological growth constrained by space and competition for resources.

(b) The value $K$ represents the carrying capacity beyond which the population cannot grow.

(c) The growth in population is always non-negative, increases at first and then declines.

(d) The value of parameter $A$ equals $(K/P(0)) - 1$.

**(A)** Only (a) and (b)  
**(B)** Only (b) and (c)  
**(C)** Only (a), (b), and (d)  
**(D)** Only (c) and (d)  
**(E)** All of the above

<details>
<summary>Solution</summary>

**Answer: E**

All statements are true:

**(a) TRUE:** The logistic model captures resource constraints through the carrying capacity.

**(b) TRUE:** As $t \to \infty$, $P(t) \to K$, which is the maximum sustainable population.

**(c) TRUE:** The rate of change $dP/dt > 0$ initially (population increases), reaches maximum at $P = K/2$, then declines toward zero.

**(d) TRUE:** From $P(0) = K/(1+A)$, solving gives $A = K/P(0) - 1$.

**Key Concept:** Comprehensive understanding of logistic function properties.
</details>

---

### Question W3-018 | Schaefer Analysis ⭐ [Exam Q13]

Consider the Schaefer (1957) model of growth: $G(S) = gS(1 - S/K)$ where $G(S)$ is fish growth, $g$ is the intrinsic growth rate, $S$ is the stock level and $K$ is the carrying capacity. Which of the following statements is TRUE?

(a) The actual fish growth rate, defined as the ratio of $G(S)$ to $S$, declines as stock increases.

(b) Fish growth (or $G(S)$) is highest when the stock ($S$) is half the maximum carrying capacity ($K$).

(c) Fish growth (or $G(S)$) is always non-negative.

**(A)** Only (a)  
**(B)** Only (b)  
**(C)** Only (a) and (b)  
**(D)** All of the above  
**(E)** Only (b) and (c)

<details>
<summary>Solution</summary>

**Answer: C**

**(a) TRUE:** Actual growth rate $= g(1 - S/K)$ decreases linearly from $g$ (at $S=0$) to $0$ (at $S=K$).

**(b) TRUE:** $G(S)$ is a downward parabola with vertex at $S = K/2$, where growth is maximum.

**(c) FALSE:** If $S > K$, then $(1 - S/K) < 0$, so $G(S) < 0$ (population declines when exceeding carrying capacity).

Answer: (a) and (b) are correct, but not (c).

**Key Concept:** Growth can be negative if stock exceeds carrying capacity.
</details>

---

### Question W3-019 | Composition Exam ⭐ [Exam Q23]

If $f(x) = -e^{-2x+1}$ and $g(x) = -\frac{1}{2}x^2$, what is $(f \circ g)(x)$?

**(A)** $(-e^{-2x+1})(-\frac{1}{2})$  
**(B)** $-e^{x^2+1}$  
**(C)** $\frac{1}{2}e^{4x^2-4x+1}$  
**(D)** $xe^{-2x+1}$  
**(E)** None of the above

<details>
<summary>Solution</summary>

**Answer: B**

$(f \circ g)(x) = f(g(x)) = f\left(-\frac{1}{2}x^2\right)$

$$= -e^{-2(-\frac{1}{2}x^2)+1}$$

$$= -e^{x^2+1}$$

**Key Concept:** Substitute the entire inner function into the outer function.
</details>

---

### Question W3-020 | Inverse Exam ⭐ [Exam Q20]

What is the inverse of the function $f(x) = 3 + \frac{1}{4}x$?

**(A)** $f^{-1}(x) = -3 + 4x$  
**(B)** $f^{-1}(x) = -3 - \frac{1}{4}x$  
**(C)** $f^{-1}(x) = \frac{1}{4} - x$  
**(D)** $f^{-1}(x) = -12 + 4x$  
**(E)** None of the above

<details>
<summary>Solution</summary>

**Answer: D**

Let $y = 3 + \frac{1}{4}x$

$y - 3 = \frac{1}{4}x$

$x = 4(y - 3) = 4y - 12$

Swap: $f^{-1}(x) = 4x - 12 = -12 + 4x$

**Verification:** 
$$f(f^{-1}(x)) = 3 + \frac{1}{4}(4x - 12) = 3 + x - 3 = x \checkmark$$

**Key Concept:** Inverse of a linear function is also linear with reciprocal slope.
</details>

---

## Summary Statistics

| Category | Questions | Topics Covered |
|----------|-----------|----------------|
| Foundational | W3-001 to W3-008 | Logistic basics, Schaefer model, sequences, composition, inverses |
| Intermediate | W3-009 to W3-016 | Time calculations, growth analysis, series, verification |
| Exam-Style | W3-017 to W3-020 | Comprehensive analysis, multi-part reasoning |

**Exam Questions Mapped:**
- Q8: Logistic time to 50% capacity (W3-009)
- Q13: Schaefer model properties (W3-015, W3-018)
- Q17: Logistic function comprehensive (W3-017)
- Q20: Inverse functions (W3-020)
- Q23: Function composition (W3-019)

---

*Practice aligned with SCIE1500 Sample Final Examination*
