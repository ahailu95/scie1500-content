# Week 7: Definite Integrals and Applications — Practice Questions

## Metadata
- **Week:** 7
- **Title:** Definite Integrals and Applications
- **Theme:** Measuring Total Accumulation
- **Exam Alignment:** Q14, Q29, Q30, Q39
- **Total Questions:** 20

---

## Part A: Foundational Questions (W7-001 to W7-008)

### W7-001: Basic Definite Integral
Evaluate $\int_0^2 x\,dx$

**(A)** $2$ &emsp; **(B)** $4$ &emsp; **(C)** $\frac{1}{2}$ &emsp; **(D)** $1$ &emsp; **(E)** $\frac{x^2}{2} + C$

<details>
<summary>Solution</summary>

**Answer: (A)**

Using the FTC:
$$\int_0^2 x\,dx = \left[\frac{x^2}{2}\right]_0^2 = \frac{4}{2} - 0 = 2$$

Note: Option E shows an indefinite integral (with +C), not a definite integral.
</details>

---

### W7-002: Polynomial Integral
Evaluate $\int_1^3 x^2\,dx$

**(A)** $\frac{26}{3}$ &emsp; **(B)** $9$ &emsp; **(C)** $\frac{28}{3}$ &emsp; **(D)** $8$ &emsp; **(E)** $\frac{8}{3}$

<details>
<summary>Solution</summary>

**Answer: (A)**

$$\int_1^3 x^2\,dx = \left[\frac{x^3}{3}\right]_1^3 = \frac{27}{3} - \frac{1}{3} = 9 - \frac{1}{3} = \frac{26}{3}$$
</details>

---

### W7-003: Exponential Integral
Evaluate $\int_0^1 e^x\,dx$

**(A)** $e$ &emsp; **(B)** $e - 1$ &emsp; **(C)** $1$ &emsp; **(D)** $e + 1$ &emsp; **(E)** $\frac{e}{2}$

<details>
<summary>Solution</summary>

**Answer: (B)**

$$\int_0^1 e^x\,dx = \left[e^x\right]_0^1 = e^1 - e^0 = e - 1 \approx 1.718$$
</details>

---

### W7-004: Logarithmic Integral
Evaluate $\int_1^e \frac{1}{x}\,dx$

**(A)** $0$ &emsp; **(B)** $e - 1$ &emsp; **(C)** $1$ &emsp; **(D)** $\ln(e) - \ln(1)$ &emsp; **(E)** Both C and D

<details>
<summary>Solution</summary>

**Answer: (E)**

$$\int_1^e \frac{1}{x}\,dx = \left[\ln|x|\right]_1^e = \ln(e) - \ln(1) = 1 - 0 = 1$$

Both C and D give the same answer.
</details>

---

### W7-005: Identifying Arithmetic Sequences
Which of the following is an arithmetic sequence?

**(A)** $1, 2, 4, 8, 16, \ldots$
**(B)** $3, 6, 12, 24, \ldots$
**(C)** $5, 10, 15, 20, 25, \ldots$
**(D)** $1, 1, 2, 3, 5, 8, \ldots$
**(E)** $2, 4, 8, 16, 32, \ldots$

<details>
<summary>Solution</summary>

**Answer: (C)**

An arithmetic sequence has constant common difference:
- (C): $10-5=5$, $15-10=5$, $20-15=5$ — constant difference $d=5$ ✓
- (A), (B), (E): Geometric sequences
- (D): Fibonacci sequence
</details>

---

### W7-006: Geometric Sequence Definition (Exam Q30 Style)
What is a geometric sequence?

**(A)** A sequence with a common ratio between consecutive numbers
**(B)** A sequence with a constant consecutive difference
**(C)** Any sequence where a number is a product of the preceding number
**(D)** A sequence where the ratio between the $i$-th and $(i+1)$-th term equals the common ratio raised to $i$
**(E)** A sequence with a common ratio between 0 and 1

<details>
<summary>Solution</summary>

**Answer: (A)**

A geometric sequence has a **constant ratio** between consecutive terms: $\frac{a_{n+1}}{a_n} = r$
</details>

---

### W7-007: Arithmetic Sequence nth Term
For the arithmetic sequence $a_n = 7 + 3(n-1)$, what is $a_{10}$?

**(A)** $30$ &emsp; **(B)** $34$ &emsp; **(C)** $37$ &emsp; **(D)** $33$ &emsp; **(E)** $40$

<details>
<summary>Solution</summary>

**Answer: (B)**

$$a_{10} = 7 + 3(10-1) = 7 + 27 = 34$$
</details>

---

### W7-008: Geometric Sequence nth Term
For the geometric sequence with $a_1 = 5$ and $r = 2$, what is $a_6$?

**(A)** $80$ &emsp; **(B)** $160$ &emsp; **(C)** $64$ &emsp; **(D)** $320$ &emsp; **(E)** $32$

<details>
<summary>Solution</summary>

**Answer: (B)**

$$a_6 = 5 \cdot 2^{6-1} = 5 \cdot 32 = 160$$
</details>

---

## Part B: Intermediate Questions (W7-009 to W7-016)

### W7-009: Mixed Function Integral
Evaluate $\int_0^2 (3x^2 - 2x + 1)\,dx$

**(A)** $4$ &emsp; **(B)** $6$ &emsp; **(C)** $8$ &emsp; **(D)** $10$ &emsp; **(E)** $12$

<details>
<summary>Solution</summary>

**Answer: (B)**

$$\int_0^2 (3x^2 - 2x + 1)\,dx = \left[x^3 - x^2 + x\right]_0^2 = (8 - 4 + 2) - 0 = 6$$
</details>

---

### W7-010: Area Under Curve
Find the area under $y = x^2$ from $x = 0$ to $x = 3$.

**(A)** $3$ &emsp; **(B)** $6$ &emsp; **(C)** $9$ &emsp; **(D)** $18$ &emsp; **(E)** $27$

<details>
<summary>Solution</summary>

**Answer: (C)**

$$\text{Area} = \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{27}{3} = 9$$
</details>

---

### W7-011: Signed Area
Evaluate $\int_{-1}^{1} x^3\,dx$

**(A)** $0$ &emsp; **(B)** $\frac{1}{2}$ &emsp; **(C)** $-\frac{1}{2}$ &emsp; **(D)** $\frac{1}{4}$ &emsp; **(E)** $2$

<details>
<summary>Solution</summary>

**Answer: (A)**

$$\int_{-1}^{1} x^3\,dx = \left[\frac{x^4}{4}\right]_{-1}^{1} = \frac{1}{4} - \frac{1}{4} = 0$$

*Geometric interpretation:* $x^3$ is odd, so positive and negative areas cancel.
</details>

---

### W7-012: Arithmetic Series Sum
Find the sum of the first 10 terms of $2, 5, 8, 11, \ldots$

**(A)** $145$ &emsp; **(B)** $155$ &emsp; **(C)** $165$ &emsp; **(D)** $175$ &emsp; **(E)** $185$

<details>
<summary>Solution</summary>

**Answer: (B)**

$a_1 = 2$, $d = 3$, $a_{10} = 2 + 9(3) = 29$

$$S_{10} = \frac{10}{2}(2 + 29) = 5 \times 31 = 155$$
</details>

---

### W7-013: Geometric Series Sum
Find the sum of the first 5 terms of $3, 6, 12, 24, \ldots$

**(A)** $93$ &emsp; **(B)** $96$ &emsp; **(C)** $90$ &emsp; **(D)** $63$ &emsp; **(E)** $48$

<details>
<summary>Solution</summary>

**Answer: (A)**

$a_1 = 3$, $r = 2$

$$S_5 = 3 \cdot \frac{1 - 2^5}{1 - 2} = 3 \cdot \frac{-31}{-1} = 93$$

Verification: $3 + 6 + 12 + 24 + 48 = 93$ ✓
</details>

---

### W7-014: Counting Terms in Range (Exam Q29 Style)
Consider $a_i = 3 + 5(i-1)$ for $i = 1, 2, 3, \ldots$. How many terms are in $[10, 150]$?

**(A)** $27$ &emsp; **(B)** $28$ &emsp; **(C)** $29$ &emsp; **(D)** $30$ &emsp; **(E)** None

<details>
<summary>Solution</summary>

**Answer: (B)**

Simplify: $a_i = 5i - 2$

For $a_i \geq 10$: $5i - 2 \geq 10 \Rightarrow i \geq 2.4 \Rightarrow i_{\min} = 3$

For $a_i \leq 150$: $5i - 2 \leq 150 \Rightarrow i \leq 30.4 \Rightarrow i_{\max} = 30$

Count: $30 - 3 + 1 = 28$
</details>

---

### W7-015: Average Value
Find the average value of $f(x) = x^2$ on $[0, 3]$.

**(A)** $1$ &emsp; **(B)** $2$ &emsp; **(C)** $3$ &emsp; **(D)** $4.5$ &emsp; **(E)** $9$

<details>
<summary>Solution</summary>

**Answer: (C)**

$$\bar{f} = \frac{1}{3-0}\int_0^3 x^2\,dx = \frac{1}{3} \cdot 9 = 3$$
</details>

---

### W7-016: Area Between Curves
Find the area between $y = x^2$ and $y = x$ from $x = 0$ to $x = 1$.

**(A)** $\frac{1}{6}$ &emsp; **(B)** $\frac{1}{3}$ &emsp; **(C)** $\frac{1}{2}$ &emsp; **(D)** $\frac{2}{3}$ &emsp; **(E)** $1$

<details>
<summary>Solution</summary>

**Answer: (A)**

On $[0,1]$: $x \geq x^2$, so upper curve is $y = x$.

$$\text{Area} = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$
</details>

---

## Part C: Exam-Style Questions (W7-017 to W7-020)

### W7-017: Definite Integral Evaluation (Q14 Style)
Evaluate the following:

**(a)** $\int_1^4 \left(2x - \frac{1}{\sqrt{x}}\right)\,dx$

**(b)** $\int_0^{\ln 2} e^{2x}\,dx$

**(c)** $\int_1^e \left(x + \frac{2}{x}\right)\,dx$

<details>
<summary>Solution</summary>

**(a)** $\left[x^2 - 2\sqrt{x}\right]_1^4 = (16 - 4) - (1 - 2) = 12 + 1 = \boxed{13}$

**(b)** $\left[\frac{e^{2x}}{2}\right]_0^{\ln 2} = \frac{e^{2\ln 2}}{2} - \frac{1}{2} = \frac{4}{2} - \frac{1}{2} = \boxed{\frac{3}{2}}$

**(c)** $\left[\frac{x^2}{2} + 2\ln x\right]_1^e = \frac{e^2}{2} + 2 - \frac{1}{2} = \boxed{\frac{e^2 + 3}{2}}$
</details>

---

### W7-018: Malthusian Trap Analysis
A country has population $P_0 = 80$ million and food capacity for 80 million. Population grows at 2%/year (geometric), food capacity increases by 2 million/year (arithmetic).

**(a)** Write the population formula $P_n$.
**(b)** Write the food capacity formula $F_n$.
**(c)** In which year does population exceed food capacity?

<details>
<summary>Solution</summary>

**(a)** $P_n = 80 \times 1.02^n$ million

**(b)** $F_n = 80 + 2n$ million

**(c)** Solve $80 \times 1.02^n > 80 + 2n$ numerically:
- At $n = 24$: $P \approx 128.7$ vs $F = 128$
- Crisis occurs around **Year 24**
</details>

---

### W7-019: Area Between Curves (Land Degradation)
Lower boundary: $y = e^{0.05x}$, Upper boundary: $y = 30 + x$ (km)

**(a)** Set up the area integral for $x \in [0, 80]$.
**(b)** Evaluate given: $\int e^{0.05x}\,dx = 20e^{0.05x}$

<details>
<summary>Solution</summary>

**(a)** $\text{Area} = \int_0^{80} [(30 + x) - e^{0.05x}]\,dx$

**(b)** $= \left[30x + \frac{x^2}{2} - 20e^{0.05x}\right]_0^{80}$
$= (2400 + 3200 - 20e^4) - (0 - 20)$
$\approx 5600 - 1092 + 20 = \boxed{4528 \text{ km}^2}$
</details>

---

### W7-020: Consumer/Producer Surplus Preview (Q39)
Demand: $Q_d = 60 - P$, Supply: $Q_s = P - 20$

**(a)** Find equilibrium $(P^*, Q^*)$.
**(b)** Maximum price consumers would pay?
**(c)** Minimum price for producers?
**(d)** Set up the CS integral.

<details>
<summary>Solution</summary>

**(a)** $60 - P = P - 20 \Rightarrow P^* = 40, Q^* = 20$

**(b)** Demand intercept: $P_{\max} = 60$

**(c)** Supply intercept: $P_{\min} = 20$

**(d)** $\text{CS} = \int_0^{20} (60 - Q)\,dQ - 40 \times 20 = 200$
</details>

---

## Key Formula Summary

| Concept | Formula |
|---------|---------|
| FTC (Part 2) | $\int_a^b f(x)\,dx = F(b) - F(a)$ |
| Area between curves | $\int_a^b [f(x) - g(x)]\,dx$ |
| Average value | $\frac{1}{b-a}\int_a^b f(x)\,dx$ |
| Arithmetic sequence | $a_n = a_1 + (n-1)d$ |
| Arithmetic series | $S_n = \frac{n}{2}(a_1 + a_n)$ |
| Geometric sequence | $a_n = a_1 \cdot r^{n-1}$ |
| Geometric series | $S_n = a_1\frac{1-r^n}{1-r}$ |
