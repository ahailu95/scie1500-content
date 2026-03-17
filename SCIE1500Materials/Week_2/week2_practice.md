# Week 2 Practice Questions: Exponential and Logarithmic Functions

**Theme:** Modeling Unbounded Growth and Decay  
**Exam Alignment:** Q8, Q17, Q20, Q23, Q27

---

## Multiple Choice Questions

### Q1: Exponential Equation Solving (Q8 style)

A population grows according to $P(t) = 500e^{0.08t}$, where $t$ is in years. How many years will it take for the population to reach 2000?

- (a) 12.5 years
- (b) 17.3 years
- (c) 25.0 years
- (d) 8.7 years
- (e) None of the above

<details>
<summary>Solution</summary>

Set up equation: $500e^{0.08t} = 2000$

Divide by 500: $e^{0.08t} = 4$

Take natural log: $0.08t = \ln(4)$

Solve: $t = \frac{\ln(4)}{0.08} = \frac{1.386}{0.08} = 17.33$ years

**Answer: (b)**
</details>

---

### Q2: Inverse Functions (Q20)

What is the inverse of the function $f(x) = 3 + \frac{1}{4}x$?

- (a) $f^{-1}(x) = -3 + 4x$
- (b) $f^{-1}(x) = -3 - \frac{1}{4}x$
- (c) $f^{-1}(x) = \frac{1}{4} - x$
- (d) $f^{-1}(x) = -12 + 4x$
- (e) None of the above

<details>
<summary>Solution</summary>

1. Start with $y = 3 + \frac{1}{4}x$
2. Swap $x$ and $y$: $x = 3 + \frac{1}{4}y$
3. Solve for $y$: $x - 3 = \frac{1}{4}y$
4. Multiply by 4: $y = 4(x - 3) = 4x - 12 = -12 + 4x$

**Answer: (d)**
</details>

---

### Q3: Function Composition with Exponentials (Q23)

If $f(x) = -e^{-2x+1}$ and $g(x) = -\frac{1}{2}x^2$, what is $f \circ g(x)$?

- (a) $(-e^{-2x+1})(-\frac{1}{2})$
- (b) $-e^{x^2+1}$
- (c) $\frac{1}{2}e^{4x^2-4x+1}$
- (d) $xe^{-2x+1}$
- (e) None of the above

<details>
<summary>Solution</summary>

$f \circ g(x) = f(g(x))$

First: $g(x) = -\frac{1}{2}x^2$

Then substitute into $f$:
$$f(g(x)) = -e^{-2(-\frac{1}{2}x^2)+1} = -e^{x^2+1}$$

**Answer: (b)**
</details>

---

### Q4: Logarithmic Simplification

Simplify: $\ln(e^x) + \ln(e^{3x})$

- (a) $\ln(e^{4x})$
- (b) $3x^2$
- (c) $4x$
- (d) $e^{4x}$
- (e) None of the above

<details>
<summary>Solution</summary>

Using $\ln(e^a) = a$:
- $\ln(e^x) = x$
- $\ln(e^{3x}) = 3x$
- Sum: $x + 3x = 4x$

**Answer: (c)**
</details>

---

### Q5: Properties of Probability Functions (Q27)

The probability $p$ of contracting a disease is: $p = \frac{1}{1+e^{-3x}}$

Which statement is **NOT** correct?

- (a) $p$ is $\frac{1}{2}$ if $x = 0$
- (b) $p$ is below $\frac{1}{2}$ if $x$ is negative
- (c) $p$ is an increasing function of $x$
- (d) $p$ approaches zero if $x \to -\infty$
- (e) None of the above (all are correct)

<details>
<summary>Solution</summary>

Checking each:
- (a) At $x=0$: $p = \frac{1}{1+e^0} = \frac{1}{2}$ ✓
- (b) When $x<0$: $e^{-3x} > 1$, so $p < \frac{1}{2}$ ✓
- (c) As $x$ increases, $e^{-3x}$ decreases, so $p$ increases ✓
- (d) As $x \to -\infty$: $e^{-3x} \to \infty$, so $p \to 0$ ✓

**Answer: (e) — All statements are correct**
</details>

---

### Q9: Domain Identification

In which case is the Domain NOT identified correctly?

- (a) $y = -3 + 6x$, $D = \{x : x \in \mathbb{R}\}$
- (b) $y = \frac{(2x-1)^{1/2}}{2} - 2$, $D = \{x : x \in \mathbb{R}\}$
- (c) $y = \frac{2}{1-e^{-x}}$, $D = \{x \in \mathbb{R} : x \neq 0\}$
- (d) $y = e^{-0.5x+2}$, $D = \{x : x \in \mathbb{R}\}$
- (e) None of the above

<details>
<summary>Solution</summary>

- (a) Linear function — domain is all reals ✓
- (b) Square root requires $2x-1 \geq 0$, so $x \geq 0.5$. Given domain is **wrong** ✗
- (c) Need $1-e^{-x} \neq 0$, means $x \neq 0$ ✓
- (d) Exponential — all reals ✓

**Answer: (b)**
</details>

---

### Q10: Doubling Time Rule

A population grows at 2% per year. Using the '70 over r' rule, how long to double?

- (a) 14 years
- (b) 35 years
- (c) 70 years
- (d) 140 years
- (e) None of the above

<details>
<summary>Solution</summary>

Doubling time $\approx \frac{70}{r} = \frac{70}{2} = 35$ years

**Answer: (b)**
</details>

---

### Q12: Graph Identification

A population $P(t) = 2e^{0.1t}$. Which property must the graph have?

- (a) Passes through $(0, 2)$ and is always increasing
- (b) Passes through $(0, 1)$ and has horizontal asymptote at $y = 2$
- (c) Passes through $(0, 2)$ and approaches zero as $t \to \infty$
- (d) Is a straight line with slope 0.1
- (e) None of the above

<details>
<summary>Solution</summary>

At $t=0$: $P(0) = 2e^0 = 2$ — passes through $(0, 2)$

Since exponent $0.1t > 0$ when $t > 0$, function is increasing.

**Answer: (a)**
</details>

---

## Multi-Part Questions

### Q6: Logistic Population Model (Q8 Preparation)

Consider $P(t) = \frac{K}{1+Ae^{-\alpha t}}$ with $K=10000$, $A=99$, $\alpha=0.1$.

**(a)** What is $P(0)$?

<details>
<summary>Solution</summary>

$$P(0) = \frac{10000}{1+99 \times e^0} = \frac{10000}{100} = 100$$
</details>

**(b)** What is the carrying capacity?

<details>
<summary>Solution</summary>

As $t \to \infty$, $e^{-\alpha t} \to 0$, so $P \to K = 10000$
</details>

**(c)** How long until $P = 5000$ (50% of $K$)?

<details>
<summary>Solution</summary>

Set $\frac{10000}{1+99e^{-0.1t}} = 5000$

$1 + 99e^{-0.1t} = 2$

$99e^{-0.1t} = 1$

$e^{-0.1t} = \frac{1}{99}$

$-0.1t = \ln\left(\frac{1}{99}\right) = -\ln(99)$

$t = \frac{\ln(99)}{0.1} = \frac{4.595}{0.1} \approx 46$ time periods
</details>

---

### Q7: Logarithm Rules Practice

Simplify each expression:

| Part | Expression | Answer |
|------|------------|--------|
| (a) | $\ln(x^3) + \ln(x^2)$ | $5\ln(x)$ |
| (b) | $\ln(e^5) - \ln(e^2)$ | $3$ |
| (c) | $e^{\ln(x^2)}$ | $x^2$ |
| (d) | $\ln(8) - \ln(2)$ | $\ln(4)$ |
| (e) | $2\ln(3) + \ln(4)$ | $\ln(36)$ |
| (f) | $e^{\ln(\sqrt{x})}$ | $\sqrt{x}$ |

---

### Q8: Geometric Sequences and Exponential Growth

A bacterial colony doubles every 3 hours. Initially: 500 bacteria.

**(a)** Formula for population after $n$ doubling periods?

<details>
<summary>Solution</summary>

Geometric sequence: $a=500$, $r=2$

$$P_n = 500 \times 2^n$$
</details>

**(b)** Population after 4 doubling periods (12 hours)?

<details>
<summary>Solution</summary>

$P_4 = 500 \times 2^4 = 500 \times 16 = 8000$ bacteria
</details>

**(c)** Doubling periods until population exceeds 1 million?

<details>
<summary>Solution</summary>

$500 \times 2^n > 1,000,000$

$2^n > 2000$

$n > \frac{\ln(2000)}{\ln(2)} = \frac{7.64}{0.693} = 10.97$

**Answer: 11 periods**
</details>

**(d)** Write as continuous function $P(t)$ (hours)?

<details>
<summary>Solution</summary>

Doubling time $T = 3$ means $e^{3k} = 2$

$k = \frac{\ln(2)}{3} \approx 0.231$

$$P(t) = 500e^{0.231t}$$
</details>

---

### Q11: Compound Interest

Investment: $10,000 at 6% annual interest, compounded annually.

**(a)** Value after $n$ years?

$$V(n) = 10000(1.06)^n$$

**(b)** Value after 10 years?

$$V(10) = 10000 \times 1.7908 = \$17,908.48$$

**(c)** Years to triple?

$(1.06)^n = 3$

$n = \frac{\ln(3)}{\ln(1.06)} = \frac{1.099}{0.0583} \approx 19$ years

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Exponential growth | $P(t) = P_0 e^{kt}$ |
| Inverse relationship | $e^{\ln(x)} = x$ and $\ln(e^x) = x$ |
| Product rule | $\ln(ab) = \ln(a) + \ln(b)$ |
| Quotient rule | $\ln(a/b) = \ln(a) - \ln(b)$ |
| Power rule | $\ln(a^n) = n\ln(a)$ |
| Doubling time | $T \approx 70/r\%$ |
| Geometric sequence | $a_n = a_1 \cdot r^{n-1}$ |

---

*Aligned with SCIE1500 Sample Final Examination*
