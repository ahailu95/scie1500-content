# Week 4 Practice Questions: Limits, Continuity, and Introduction to Derivatives

## Theme: "Measuring Instantaneous Change"

**Exam Alignment:** Q13, Q21, Q25, Q28

**Scientific Contexts:** Bacterial growth rates, Radioactive decay, Schaefer fish model, Plastic production acceleration

---

## Section A: Foundational Questions (8 Questions)

### W4-001: Limit Evaluation (Factoring)

Evaluate: $\displaystyle \lim_{x \to 3} \frac{x^2 - 9}{x - 3}$

**(A)** 0  
**(B)** 3  
**(C)** 6  
**(D)** 9  
**(E)** Does not exist

<details>
<summary>Solution</summary>

Factor the numerator: $x^2 - 9 = (x+3)(x-3)$

$$\lim_{x \to 3} \frac{(x+3)(x-3)}{x-3} = \lim_{x \to 3} (x+3) = 6$$

**Answer: C**

*Key concept:* For 0/0 indeterminate forms, factor to cancel the problematic term before substituting.
</details>

---

### W4-002: Limit Evaluation (Factoring)

Evaluate: $\displaystyle \lim_{x \to 4} \frac{x^2 - 2x - 8}{x - 4}$

**(A)** 2  
**(B)** 4  
**(C)** 6  
**(D)** 8  
**(E)** Does not exist

<details>
<summary>Solution</summary>

Factor the numerator: $x^2 - 2x - 8 = (x-4)(x+2)$

$$\lim_{x \to 4} \frac{(x-4)(x+2)}{x-4} = \lim_{x \to 4} (x+2) = 6$$

**Answer: C**

*Key concept:* Factoring removes the zero in the denominator, allowing direct substitution.
</details>

---

### W4-003: Limit at Infinity

Evaluate: $\displaystyle \lim_{x \to \infty} \frac{3x^2 + 4x - 1}{2x^2 + x - 4}$

**(A)** 0  
**(B)** $\frac{1}{2}$  
**(C)** 1  
**(D)** $\frac{3}{2}$  
**(E)** $\infty$

<details>
<summary>Solution</summary>

Divide every term by $x^2$ (the highest power):

$$\lim_{x \to \infty} \frac{3 + \frac{4}{x} - \frac{1}{x^2}}{2 + \frac{1}{x} - \frac{4}{x^2}}$$

As $x \to \infty$, terms with $x$ in the denominator approach 0:

$$= \frac{3 + 0 - 0}{2 + 0 - 0} = \frac{3}{2}$$

**Answer: D**

*Key concept:* For limits at infinity with polynomials, divide by the highest power of x.
</details>

---

### W4-004: Continuity Definition

A function $f(x)$ is continuous at $x = a$ if and only if which condition holds?

**(A)** $f(a)$ is defined  
**(B)** $\displaystyle \lim_{x \to a} f(x)$ exists  
**(C)** $f'(a)$ exists  
**(D)** $\displaystyle \lim_{x \to a} f(x) = f(a)$  
**(E)** $f(x)$ is differentiable at $x = a$

<details>
<summary>Solution</summary>

Continuity at $x = a$ requires three conditions:
1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists
3. $\lim_{x \to a} f(x) = f(a)$

Option D encapsulates all three conditions in one statement.

**Answer: D**

*Key concept:* Continuity means no gaps, jumps, or holes—the limit equals the function value.
</details>

---

### W4-005: Power Rule

What is the derivative of $f(x) = x^5$?

**(A)** $5x^4$  
**(B)** $5x^5$  
**(C)** $x^4$  
**(D)** $4x^5$  
**(E)** $\frac{x^6}{6}$

<details>
<summary>Solution</summary>

Apply the power rule: $\frac{d}{dx}[x^n] = nx^{n-1}$

$$\frac{d}{dx}[x^5] = 5x^{5-1} = 5x^4$$

**Answer: A**
</details>

---

### W4-006: Power Rule (Negative Exponents)

What is $\frac{d}{dx}\left[\frac{1}{x^2}\right]$?

**(A)** $\frac{2}{x^3}$  
**(B)** $-\frac{2}{x^3}$  
**(C)** $-\frac{1}{x^3}$  
**(D)** $\frac{1}{x^3}$  
**(E)** $\frac{2}{x}$

<details>
<summary>Solution</summary>

Rewrite: $\frac{1}{x^2} = x^{-2}$

Apply power rule: $\frac{d}{dx}[x^{-2}] = -2x^{-3} = -\frac{2}{x^3}$

**Answer: B**

*Key concept:* Rewrite fractions using negative exponents before differentiating.
</details>

---

### W4-007: Sum Rule

Find $\frac{d}{dx}[4x^3 - 2x^2 + 7x - 5]$

**(A)** $12x^2 - 4x + 7$  
**(B)** $12x^2 - 4x + 7 - 5$  
**(C)** $4x^2 - 2x + 7$  
**(D)** $12x^3 - 4x^2 + 7x$  
**(E)** $x^4 - \frac{2x^3}{3} + \frac{7x^2}{2} - 5x$

<details>
<summary>Solution</summary>

Differentiate term by term:

$$\frac{d}{dx}[4x^3] = 12x^2$$
$$\frac{d}{dx}[-2x^2] = -4x$$
$$\frac{d}{dx}[7x] = 7$$
$$\frac{d}{dx}[-5] = 0$$

Combine: $12x^2 - 4x + 7$

**Answer: A**
</details>

---

### W4-008: Power Rule (Fractional Exponents)

Find $\frac{d}{dx}[\sqrt{x}]$

**(A)** $\frac{1}{\sqrt{x}}$  
**(B)** $\frac{1}{2\sqrt{x}}$  
**(C)** $2\sqrt{x}$  
**(D)** $\frac{\sqrt{x}}{2}$  
**(E)** $-\frac{1}{2\sqrt{x}}$

<details>
<summary>Solution</summary>

Rewrite: $\sqrt{x} = x^{1/2}$

$$\frac{d}{dx}[x^{1/2}] = \frac{1}{2}x^{-1/2} = \frac{1}{2} \cdot \frac{1}{\sqrt{x}} = \frac{1}{2\sqrt{x}}$$

**Answer: B**
</details>

---

## Section B: Intermediate Questions (6 Questions)

### W4-009: Limit at Infinity (Degree Comparison)

Evaluate: $\displaystyle \lim_{x \to \infty} \frac{x - 5}{3x^2 + 2x + 1}$

<details>
<summary>Solution</summary>

The degree of the numerator (1) is less than the degree of the denominator (2).

Divide by $x^2$:

$$\lim_{x \to \infty} \frac{\frac{1}{x} - \frac{5}{x^2}}{3 + \frac{2}{x} + \frac{1}{x^2}} = \frac{0 - 0}{3 + 0 + 0} = 0$$

**Answer:** 0

*Key concept:* When numerator degree < denominator degree, the limit at infinity is 0.
</details>

---

### W4-010: Differentiation Practice

Differentiate: $f(x) = 3x^4 - \frac{2}{x} + 5\sqrt{x} - 8$

<details>
<summary>Solution</summary>

Rewrite: $f(x) = 3x^4 - 2x^{-1} + 5x^{1/2} - 8$

Differentiate term by term:

$$f'(x) = 3(4x^3) - 2(-1)x^{-2} + 5\left(\frac{1}{2}\right)x^{-1/2} - 0$$

$$f'(x) = 12x^3 + 2x^{-2} + \frac{5}{2}x^{-1/2}$$

$$f'(x) = 12x^3 + \frac{2}{x^2} + \frac{5}{2\sqrt{x}}$$
</details>

---

### W4-011: Tangent Line Slope

Find the slope of the tangent line to $y = x^3 - 4x$ at $x = 2$.

<details>
<summary>Solution</summary>

Step 1: Find the derivative
$$y' = 3x^2 - 4$$

Step 2: Evaluate at $x = 2$
$$y'(2) = 3(2)^2 - 4 = 12 - 4 = 8$$

**Answer:** The slope is 8.
</details>

---

### W4-012: Bacterial Growth Rate (Scientific Application)

A bacterial colony grows according to $N(t) = 500 e^{0.05t}$, where $N$ is the number of cells and $t$ is time in minutes.

**(a)** What is the average rate of change from $t = 0$ to $t = 20$?

**(b)** What is the instantaneous rate of change at $t = 0$? *(Preview of Week 5)*

<details>
<summary>Solution</summary>

**(a)** Average rate:
$$N(0) = 500, \quad N(20) = 500e^{1} = 500(2.718) = 1359$$

$$\text{Average rate} = \frac{1359 - 500}{20 - 0} = \frac{859}{20} = 42.95 \text{ cells/min}$$

**(b)** Instantaneous rate at $t = 0$ (using derivative of exponential, covered in Week 5):
$$N'(t) = 500 \cdot 0.05 \cdot e^{0.05t} = 25e^{0.05t}$$
$$N'(0) = 25e^0 = 25 \text{ cells/min}$$

Note: The instantaneous rate at $t=0$ is lower than the average rate because the population grows faster as time increases.
</details>

---

### W4-013: Radioactive Decay Rate

A radioactive sample has mass $M(t) = 100 e^{-0.0866t}$ grams after $t$ years (this is Carbon-14 with half-life ~8 years in this simplified model).

Calculate the average rate of decay from $t = 0$ to $t = 8$.

<details>
<summary>Solution</summary>

$$M(0) = 100e^0 = 100 \text{ g}$$
$$M(8) = 100e^{-0.0866 \times 8} = 100e^{-0.693} \approx 50 \text{ g}$$

Average rate of decay:
$$\frac{M(8) - M(0)}{8 - 0} = \frac{50 - 100}{8} = -6.25 \text{ g/year}$$

The negative sign indicates the mass is *decreasing* at an average rate of 6.25 grams per year.
</details>

---

### W4-014: Derivative Evaluation

If $f(x) = 2x^4 - 3x^2 + x - 7$, find $f'(-1)$.

<details>
<summary>Solution</summary>

Step 1: Differentiate
$$f'(x) = 8x^3 - 6x + 1$$

Step 2: Evaluate at $x = -1$
$$f'(-1) = 8(-1)^3 - 6(-1) + 1 = -8 + 6 + 1 = -1$$

**Answer:** $f'(-1) = -1$
</details>

---

## Section C: Exam-Style Questions (4 Questions)

### W4-015: Tangent Line Equation (Q21 Pattern)

What is the equation of the line that is tangent to $y = e^{x-2} + 3$ at $x = 2$?

**(A)** $y = -e^{x-2}$  
**(B)** $y = x - 2$  
**(C)** $y = x + e$  
**(D)** $y = x + 2$  
**(E)** None of the above

<details>
<summary>Solution</summary>

**Step 1:** Find the point of tangency.
$$y(2) = e^{2-2} + 3 = e^0 + 3 = 1 + 3 = 4$$
Point: $(2, 4)$

**Step 2:** Find the derivative.
$$y' = e^{x-2}$$ (derivative of exponential, covered in Week 5)

**Step 3:** Find the slope at $x = 2$.
$$y'(2) = e^{2-2} = e^0 = 1$$

**Step 4:** Write the tangent line equation.
$$y - 4 = 1(x - 2) \implies y = x + 2$$

**Answer: D**
</details>

---

### W4-016: Function Properties (Q25 Pattern)

Which of the following is **NOT** true about the function $y = (x + 2)(x - 3)$?

**(A)** Its range is $\{y \in \mathbb{R} : y \geq -6.25\}$.  
**(B)** It is a concave up function, i.e., it opens up.  
**(C)** The slope of its tangent at the point where $x$ is 2 is 3.  
**(D)** Its second derivative is $y'' = 2$.  
**(E)** None of the above.

<details>
<summary>Solution</summary>

Expand: $y = x^2 - x - 6$

**(A)** Vertex at $x = -\frac{-1}{2(1)} = 0.5$
$$y(0.5) = 0.25 - 0.5 - 6 = -6.25$$
Range: $\{y : y \geq -6.25\}$ ✓

**(B)** Since $a = 1 > 0$, parabola opens upward ✓

**(C)** $y' = 2x - 1$; at $x = 2$: $y'(2) = 4 - 1 = 3$ ✓

**(D)** $y'' = 2$ ✓

All statements are true, so answer is **(E)**.

**Answer: E**
</details>

---

### W4-017: Derivative Calculation (Q28 Pattern)

What is the derivative of the function $y = \frac{3}{4}x^4 + \frac{1}{4}x^2 - 3x + \ln x$?

**(A)** $y' = 12x^3 + \frac{3}{x^2} - \frac{1}{2x^{3/2}}$  
**(B)** $y' = x^3 - 3 + \frac{1}{2}x$  
**(C)** $y' = \frac{3}{5}x^5 - \frac{3}{2}x^2 - \frac{3}{2}x$  
**(D)** $y' = 3x^3 + \frac{1}{2}x - 3 + \frac{1}{x}$  
**(E)** None of the above.

<details>
<summary>Solution</summary>

Differentiate term by term:

$$\frac{d}{dx}\left[\frac{3}{4}x^4\right] = \frac{3}{4}(4)x^3 = 3x^3$$

$$\frac{d}{dx}\left[\frac{1}{4}x^2\right] = \frac{1}{4}(2)x = \frac{1}{2}x$$

$$\frac{d}{dx}[-3x] = -3$$

$$\frac{d}{dx}[\ln x] = \frac{1}{x}$$ (covered formally in Week 5)

Combine: $y' = 3x^3 + \frac{1}{2}x - 3 + \frac{1}{x}$

**Answer: D**

*Note:* The logarithm derivative appears on the exam even though it's formally covered in Week 5.
</details>

---

### W4-018: Schaefer Model Analysis (Q13 Pattern)

Consider the Schaefer (1957) model of growth:
$$G(S) = g \cdot S \cdot \left(1 - \frac{S}{K}\right)$$
where $G(S)$ is fish growth, $g$ is the intrinsic growth rate, $S$ is the stock level and $K$ is the carrying capacity. Which of the following statements is true?

**(A)** The actual fish growth rate, defined as the ratio of $G(S)$ to $S$, declines as stock increases.  
**(B)** Fish growth (or $G(S)$) is highest when the stock ($S$) is half the maximum carrying capacity ($K$).  
**(C)** Fish growth (or $G(S)$) is always non-negative.  
**(D)** All of the above.  
**(E)** Only (A) and (B) are correct.

<details>
<summary>Solution</summary>

**(A) TRUE:** Actual growth rate = $\frac{G(S)}{S} = g(1 - S/K)$

This decreases linearly from $g$ (at $S=0$) to $0$ (at $S=K$).

**(B) TRUE:** Expand $G(S) = gS - \frac{g}{K}S^2$

Differentiate: $G'(S) = g - \frac{2g}{K}S$

Set $G'(S) = 0$: $S^* = \frac{K}{2}$

The parabola opens downward ($a = -g/K < 0$), so this is a maximum.

**(C) FALSE:** If $S > K$, then $(1 - S/K) < 0$, so $G(S) < 0$.

Growth becomes negative when stock exceeds carrying capacity (population crashes).

**Answer: (A) and (B) are correct, but not (C).**

**Answer: E**

*Key concept:* This question tests understanding of the Schaefer model AND the ability to use differentiation to confirm the MSY stock level.
</details>

---

## Summary: Key Formulas

### Limits

| Technique | When to Use |
|-----------|-------------|
| Direct substitution | When limit exists directly |
| Factor and cancel | When you get $\frac{0}{0}$ |
| Divide by highest power | For limits at infinity |

### Differentiation Rules

| Rule | Formula |
|------|---------|
| Constant | $\frac{d}{dx}[c] = 0$ |
| Power | $\frac{d}{dx}[x^n] = nx^{n-1}$ |
| Constant Multiple | $\frac{d}{dx}[cf] = c \cdot f'$ |
| Sum/Difference | $\frac{d}{dx}[f \pm g] = f' \pm g'$ |

### Tangent Line

At point $(a, f(a))$ with slope $f'(a)$:

$$y = f(a) + f'(a)(x - a)$$

---

*Practice these problems until you can solve them quickly and accurately—this foundation is essential for the optimization techniques in Week 5.*
