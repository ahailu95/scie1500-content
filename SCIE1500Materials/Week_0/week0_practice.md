# Week 0 Practice Questions: Mathematical Foundations

## SCIE1500 — Analytical Methods for Scientists
### Diagnostic Review

---

These questions assess your readiness for the quantitative work ahead. If you find gaps, address them now before Week 1.

---

## Question 1: Order of Operations (BODMAS)

Evaluate: $3 + 2 \times 4^2 - 10 \div 2$

**Options:**
- (a) 30
- (b) 32
- (c) 35
- (d) 25
- (e) 18

---

### Solution

**Step-by-step using BODMAS:**

1. **Orders (exponents) first:** $4^2 = 16$
   - Expression becomes: $3 + 2 \times 16 - 10 \div 2$

2. **Multiplication and Division (left to right):**
   - $2 \times 16 = 32$
   - $10 \div 2 = 5$
   - Expression becomes: $3 + 32 - 5$

3. **Addition and Subtraction (left to right):**
   - $3 + 32 = 35$
   - $35 - 5 = 30$

**Answer: (a) 30**

**Python check:** `print(3 + 2 * 4**2 - 10 / 2)` outputs `30.0`

---

## Question 2: Exponent Rules

Simplify each expression using exponent rules.

**(a)** $\frac{x^5 \cdot x^3}{x^2}$

**(b)** $(2^3)^4$

**(c)** $8^{2/3}$

**(d)** $5^{-2}$

---

### Solutions

**(a)** $\frac{x^5 \cdot x^3}{x^2}$

- Numerator (product rule): $x^5 \cdot x^3 = x^{5+3} = x^8$
- Then (quotient rule): $\frac{x^8}{x^2} = x^{8-2} = x^6$

**Answer: $x^6$**

**(b)** $(2^3)^4$

- Power rule: $(2^3)^4 = 2^{3 \times 4} = 2^{12} = 4096$

**Answer: $2^{12} = 4096$**

**(c)** $8^{2/3}$

- Rewrite: $8^{2/3} = (8^{1/3})^2$
- Cube root: $8^{1/3} = \sqrt[3]{8} = 2$
- Square: $2^2 = 4$

**Answer: 4**

**(d)** $5^{-2}$

- Negative exponent rule: $5^{-2} = \frac{1}{5^2} = \frac{1}{25}$

**Answer: $\frac{1}{25}$ or 0.04**

---

## Question 3: Algebraic Manipulation

Simplify or factor each expression.

**(a)** Expand: $(3x - 2)(x + 5)$

**(b)** Factor: $x^2 - 16$

**(c)** Simplify: $\frac{x^2 - 9}{x - 3}$

---

### Solutions

**(a)** $(3x - 2)(x + 5)$

Using FOIL:
- First: $3x \cdot x = 3x^2$
- Outer: $3x \cdot 5 = 15x$
- Inner: $-2 \cdot x = -2x$
- Last: $-2 \cdot 5 = -10$

Combine: $3x^2 + 15x - 2x - 10 = 3x^2 + 13x - 10$

**Answer: $3x^2 + 13x - 10$**

**(b)** $x^2 - 16$

Recognize as difference of squares: $a^2 - b^2 = (a+b)(a-b)$

$x^2 - 16 = x^2 - 4^2 = (x+4)(x-4)$

**Answer: $(x+4)(x-4)$**

**(c)** $\frac{x^2 - 9}{x - 3}$

Factor numerator: $x^2 - 9 = (x+3)(x-3)$

Simplify: $\frac{(x+3)(x-3)}{x-3} = x+3$ (for $x \neq 3$)

**Answer: $x + 3$ (undefined at $x = 3$)**

---

## Question 4: Solving Equations

Solve each equation for $x$.

**(a)** $5x - 7 = 3x + 9$

**(b)** $x^2 - 7x + 12 = 0$

**(c)** $2x^2 + 5x - 3 = 0$

---

### Solutions

**(a)** $5x - 7 = 3x + 9$

- Subtract $3x$: $2x - 7 = 9$
- Add 7: $2x = 16$
- Divide by 2: $x = 8$

**Answer: $x = 8$**

**(b)** $x^2 - 7x + 12 = 0$

Factor: Find two numbers that multiply to 12 and add to -7 → $-3$ and $-4$

$(x-3)(x-4) = 0$

**Answer: $x = 3$ or $x = 4$**

**(c)** $2x^2 + 5x - 3 = 0$

Use quadratic formula with $a=2$, $b=5$, $c=-3$:

$$x = \frac{-5 \pm \sqrt{25 + 24}}{4} = \frac{-5 \pm 7}{4}$$

- $x = \frac{-5+7}{4} = \frac{2}{4} = \frac{1}{2}$
- $x = \frac{-5-7}{4} = \frac{-12}{4} = -3$

**Answer: $x = \frac{1}{2}$ or $x = -3$**

---

## Question 5: Inequalities

Solve each inequality and express the answer in interval notation.

**(a)** $3x + 5 > 14$

**(b)** $-4x + 2 \leq 10$

**(c)** $-1 < 2x + 3 \leq 9$

---

### Solutions

**(a)** $3x + 5 > 14$

- Subtract 5: $3x > 9$
- Divide by 3: $x > 3$

**Answer: $(3, \infty)$**

**(b)** $-4x + 2 \leq 10$

- Subtract 2: $-4x \leq 8$
- Divide by $-4$ (**reverse inequality!**): $x \geq -2$

**Answer: $[-2, \infty)$**

**(c)** $-1 < 2x + 3 \leq 9$

- Subtract 3 from all parts: $-4 < 2x \leq 6$
- Divide by 2: $-2 < x \leq 3$

**Answer: $(-2, 3]$**

---

## Question 6: Scientific Notation and Unit Conversion

**(a)** Express 4,820,000 in scientific notation.

**(b)** Express 0.000078 in scientific notation.

**(c)** Calculate $(3 \times 10^4) \times (2 \times 10^5)$

**(d)** Convert 12,700,000 metric tonnes to million metric tonnes (MMT).

---

### Solutions

**(a)** 4,820,000

Move decimal 6 places left: $4.82 \times 10^6$

**Answer: $4.82 \times 10^6$**

**(b)** 0.000078

Move decimal 5 places right: $7.8 \times 10^{-5}$

**Answer: $7.8 \times 10^{-5}$**

**(c)** $(3 \times 10^4) \times (2 \times 10^5)$

- Multiply coefficients: $3 \times 2 = 6$
- Add exponents: $10^4 \times 10^5 = 10^9$

**Answer: $6 \times 10^9$**

**(d)** 12,700,000 MT to MMT

$12,700,000 \div 1,000,000 = 12.7$

**Answer: 12.7 MMT** *(This is the upper estimate of plastic entering oceans annually)*

---

## Question 7: Function Notation

Given $f(x) = 3x^2 - 2x + 1$ and $g(x) = 5x - 4$, evaluate:

**(a)** $f(2)$

**(b)** $g(-1)$

**(c)** $f(0) + g(0)$

**(d)** $f(a)$ (leave in terms of $a$)

---

### Solutions

**Remember:** $f(x)$ means "the function $f$ evaluated at $x$" — NOT "$f$ times $x$"!

**(a)** $f(2)$

$f(2) = 3(2)^2 - 2(2) + 1 = 3(4) - 4 + 1 = 12 - 4 + 1 = 9$

**Answer: 9**

**(b)** $g(-1)$

$g(-1) = 5(-1) - 4 = -5 - 4 = -9$

**Answer: -9**

**(c)** $f(0) + g(0)$

$f(0) = 3(0)^2 - 2(0) + 1 = 1$
$g(0) = 5(0) - 4 = -4$
$f(0) + g(0) = 1 + (-4) = -3$

**Answer: -3**

**(d)** $f(a)$

Replace every $x$ with $a$: $f(a) = 3a^2 - 2a + 1$

**Answer: $3a^2 - 2a + 1$**

---

## Question 8: Interval Notation

Match each description with the correct interval notation.

| Description | Interval |
|-------------|----------|
| All real numbers greater than or equal to 5 | $[5, \infty)$ |
| All real numbers between -3 and 7, not including -3 but including 7 | $(-3, 7]$ |
| All real numbers less than 2 | $(-\infty, 2)$ |
| All real numbers from 0 to 10, including both endpoints | $[0, 10]$ |
| All positive real numbers | $(0, \infty)$ |

**Key:**
- Square bracket [ or ] = included (≤ or ≥)
- Round bracket ( or ) = excluded (< or >)
- Infinity always uses round brackets

---

## Question 9: Python Basics

**(a)** What is the output of `print(2 + 3 * 4)`?

**Answer:** 14 (multiplication first: $3 \times 4 = 12$, then $2 + 12 = 14$)

**(b)** What is the output of `print(2 ** 3)`?

**Answer:** 8 (`**` is exponentiation: $2^3 = 8$)

**(c)** What is the output of `print(17 // 5)`?

**Answer:** 3 (`//` is floor division: $17 \div 5 = 3$ remainder $2$)

**(d)** What is wrong with this code: `Print('Hello')`?

**Answer:** Python is case-sensitive. Should be `print('Hello')` with lowercase 'p'.

**(e)** What does `np.linspace(0, 10, 5)` produce?

**Answer:** An array of 5 equally spaced values from 0 to 10: `[0, 2.5, 5, 7.5, 10]`

---

## Self-Assessment

| Score | Recommendation |
|-------|----------------|
| 8-9 correct | You're well-prepared for Week 1 |
| 6-7 correct | Review the topics you missed before Week 1 |
| 4-5 correct | Significant review needed; use Khan Academy or similar |
| Below 4 | Consider additional bridging support; speak with your tutor |

---

## Lab Connection

Complete **Week0_Intro_Python.ipynb** Exercises to reinforce Python skills.

---

*Next: Week 1 — Functions and the Language of Scientific Analysis*
