# Week 6: Practice Questions — Introduction to Integration

## Theme: "From Rates to Totals"

**Exam Alignment:** Q14 (Antiderivatives), Q37 (Lymphocyte Integration)

**Scientific Contexts:** Land rehabilitation, carbon sequestration, agricultural yield response

---

## Section A: Foundational (Questions 1–8)

### Question 1: Power Rule
What is $\int x^3\,dx$?

- (A) $3x^2 + C$
- (B) $\frac{x^4}{4} + C$
- (C) $\frac{x^4}{3} + C$
- (D) $4x^4 + C$
- (E) $x^4 + C$

<details>
<summary><strong>Solution</strong></summary>

Using the power rule: $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$

For $n = 3$: $\int x^3\,dx = \frac{x^{3+1}}{3+1} + C = \frac{x^4}{4} + C$

**Answer: B**
</details>

---

### Question 2: Constant Integration
What is $\int 7\,dx$?

- (A) $7$
- (B) $0$
- (C) $7x$
- (D) $7x + C$
- (E) $\frac{7x^2}{2} + C$

<details>
<summary><strong>Solution</strong></summary>

The integral of a constant $k$ is $kx + C$.

$\int 7\,dx = 7x + C$

Note: Option C is missing the constant of integration.

**Answer: D**
</details>

---

### Question 3: Negative Exponent
What is $\int \frac{1}{x^2}\,dx$?

- (A) $\ln(x^2) + C$
- (B) $-\frac{1}{x} + C$
- (C) $\frac{1}{x} + C$
- (D) $-\frac{2}{x^3} + C$
- (E) $\frac{x^{-1}}{-1} + C$

<details>
<summary><strong>Solution</strong></summary>

First rewrite: $\frac{1}{x^2} = x^{-2}$

Then apply power rule:
$$\int x^{-2}\,dx = \frac{x^{-2+1}}{-2+1} + C = \frac{x^{-1}}{-1} + C = -\frac{1}{x} + C$$

**Answer: B**
</details>

---

### Question 4: Exponential Integration
What is $\int e^x\,dx$?

- (A) $xe^{x-1} + C$
- (B) $e^{x+1} + C$
- (C) $e^x + C$
- (D) $\frac{e^{x+1}}{x+1} + C$
- (E) $xe^x + C$

<details>
<summary><strong>Solution</strong></summary>

$e^x$ is its own antiderivative:

$\int e^x\,dx = e^x + C$

*Verification:* $\frac{d}{dx}[e^x] = e^x$ ✓

**Answer: C**
</details>

---

### Question 5: Logarithmic Integration
What is $\int \frac{1}{x}\,dx$?

- (A) $x^0 + C$
- (B) $\ln x + C$
- (C) $\ln|x| + C$
- (D) $-\frac{1}{x^2} + C$
- (E) $\frac{x^0}{0}$ (undefined)

<details>
<summary><strong>Solution</strong></summary>

The power rule doesn't work when $n = -1$ (division by zero).

Instead: $\int \frac{1}{x}\,dx = \ln|x| + C$

The absolute value is needed because $\ln$ is only defined for positive numbers, but $1/x$ exists for all $x \neq 0$.

**Answer: C**
</details>

---

### Question 6: Sum Rule
What is $\int (3x^2 + 2x)\,dx$?

- (A) $6x + 2 + C$
- (B) $x^3 + x^2$
- (C) $x^3 + x^2 + C$
- (D) $\frac{3x^3}{3} + \frac{2x^2}{2} + C$
- (E) Both C and D

<details>
<summary><strong>Solution</strong></summary>

Using sum rule and power rule:

$\int (3x^2 + 2x)\,dx = 3 \cdot \frac{x^3}{3} + 2 \cdot \frac{x^2}{2} + C = x^3 + x^2 + C$

Option D shows the unsimplified form, which equals option C.

**Answer: E**
</details>

---

### Question 7: Fractional Exponent
What is $\int \sqrt{x}\,dx$?

- (A) $\frac{1}{2\sqrt{x}} + C$
- (B) $\frac{2x^{3/2}}{3} + C$
- (C) $\frac{x^{3/2}}{3/2} + C$
- (D) $\frac{\sqrt{x^3}}{3} + C$
- (E) B, C, and D are all correct

<details>
<summary><strong>Solution</strong></summary>

Rewrite: $\sqrt{x} = x^{1/2}$

Apply power rule:
$$\int x^{1/2}\,dx = \frac{x^{3/2}}{3/2} + C = \frac{2x^{3/2}}{3} + C$$

All forms B, C, D are equivalent representations.

**Answer: E**
</details>

---

### Question 8: Exponential with Coefficient
What is $\int e^{3x}\,dx$?

- (A) $3e^{3x} + C$
- (B) $\frac{e^{3x}}{3} + C$
- (C) $e^{3x+1} + C$
- (D) $\frac{e^{3x+1}}{3x+1} + C$
- (E) $e^{3x} + C$

<details>
<summary><strong>Solution</strong></summary>

For $\int e^{kx}\,dx$: divide by the coefficient of $x$.

$$\int e^{3x}\,dx = \frac{1}{3}e^{3x} + C$$

*Verification:* $\frac{d}{dx}\left[\frac{e^{3x}}{3}\right] = \frac{1}{3} \cdot 3e^{3x} = e^{3x}$ ✓

**Answer: B**
</details>

---

## Section B: Intermediate (Questions 9–16)

### Question 9: Polynomial Integration
Find $\int (4x^3 + \sqrt{x} + \frac{1}{x^2} + 1)\,dx$

- (A) $x^4 + \frac{2x^{3/2}}{3} - \frac{1}{x} + x + C$
- (B) $12x^2 + \frac{1}{2\sqrt{x}} - \frac{2}{x^3} + C$
- (C) $x^4 + \frac{2\sqrt{x^3}}{3} - x^{-1} + x + C$
- (D) Both A and C
- (E) $4x^4 + x^{3/2} - x^{-1} + x + C$

<details>
<summary><strong>Solution</strong></summary>

Rewrite: $4x^3 + x^{1/2} + x^{-2} + 1$

Integrate term by term:
- $\int 4x^3\,dx = x^4$
- $\int x^{1/2}\,dx = \frac{2x^{3/2}}{3}$
- $\int x^{-2}\,dx = -\frac{1}{x}$
- $\int 1\,dx = x$

Result: $x^4 + \frac{2x^{3/2}}{3} - \frac{1}{x} + x + C$

Options A and C are equivalent since $x^{3/2} = \sqrt{x^3}$.

**Answer: D**
</details>

---

### Question 10: Initial Value Problem
Given $f'(x) = 2x$ and $f(1) = 5$, find $f(x)$.

- (A) $x^2 + C$
- (B) $x^2 + 4$
- (C) $x^2 + 5$
- (D) $x^2$
- (E) $2x^2 + 3$

<details>
<summary><strong>Solution</strong></summary>

Step 1: Find general antiderivative: $f(x) = x^2 + C$

Step 2: Apply $f(1) = 5$: $5 = 1 + C \implies C = 4$

Step 3: $f(x) = x^2 + 4$

**Answer: B**
</details>

---

### Question 11: Integration Rules
Which of the following is TRUE about integration?

- (A) $\int f(x)g(x)\,dx = \left(\int f(x)\,dx\right)\left(\int g(x)\,dx\right)$
- (B) $\int [f(x) + g(x)]\,dx = \int f(x)\,dx + \int g(x)\,dx$
- (C) $\int \frac{f(x)}{g(x)}\,dx = \frac{\int f(x)\,dx}{\int g(x)\,dx}$
- (D) $\int [f(x)]^2\,dx = \left[\int f(x)\,dx\right]^2$
- (E) All of the above are true

<details>
<summary><strong>Solution</strong></summary>

Only the **sum rule** (option B) holds for integration.

Counterexample for A: $\int x \cdot x\,dx = \frac{x^3}{3}$, but $(\frac{x^2}{2})(\frac{x^2}{2}) = \frac{x^4}{4}$

**Answer: B**
</details>

---

### Question 12: Mixed Functions
Find $\int \left(e^{-x} + \frac{2}{x}\right)\,dx$

- (A) $-e^{-x} + 2\ln|x| + C$
- (B) $e^{-x} + 2\ln|x| + C$
- (C) $-e^{-x} + \ln|x^2| + C$
- (D) Both A and C
- (E) $\frac{e^{-x}}{-x} + 2\ln|x| + C$

<details>
<summary><strong>Solution</strong></summary>

$\int e^{-x}\,dx = -e^{-x}$

$\int \frac{2}{x}\,dx = 2\ln|x|$

Result: $-e^{-x} + 2\ln|x| + C$

Note: $2\ln|x| = \ln|x^2|$, so A and C are equivalent.

**Answer: D**
</details>

---

### Question 13: Exponential Initial Value
Given $N'(t) = 100e^{-0.5t}$ and $N(0) = 300$, find $N(t)$.

- (A) $-200e^{-0.5t} + 500$
- (B) $200e^{-0.5t} + 100$
- (C) $-200e^{-0.5t} + 300$
- (D) $500 - 200e^{-0.5t}$
- (E) Both A and D

<details>
<summary><strong>Solution</strong></summary>

$N(t) = \int 100e^{-0.5t}\,dt = -200e^{-0.5t} + C$

Apply $N(0) = 300$: $300 = -200 + C \implies C = 500$

$N(t) = -200e^{-0.5t} + 500 = 500 - 200e^{-0.5t}$

**Answer: E**
</details>

---

### Question 14: Antiderivative Verification
Which function is an antiderivative of $f(x) = 6x^2 - 4x + 1$?

- (A) $12x - 4$
- (B) $2x^3 - 2x^2 + x + 7$
- (C) $2x^3 - 2x^2 + x$
- (D) Both B and C
- (E) $18x^3 - 8x^2 + x$

<details>
<summary><strong>Solution</strong></summary>

Verify by differentiating:
- B: $\frac{d}{dx}[2x^3 - 2x^2 + x + 7] = 6x^2 - 4x + 1$ ✓
- C: $\frac{d}{dx}[2x^3 - 2x^2 + x] = 6x^2 - 4x + 1$ ✓

Both are antiderivatives (differ by constant 7).

**Answer: D**
</details>

---

### Question 15: Carbon Sequestration
The rate of carbon sequestration by a forest is $C'(t) = 50e^{-0.02t}$ tonnes/year. If initially no carbon has been sequestered, what is the total carbon sequestered as $t \to \infty$?

- (A) 50 tonnes
- (B) 100 tonnes
- (C) 2500 tonnes
- (D) 5000 tonnes
- (E) Infinite

<details>
<summary><strong>Solution</strong></summary>

$C(t) = \int 50e^{-0.02t}\,dt = -2500e^{-0.02t} + K$

Apply $C(0) = 0$: $0 = -2500 + K \implies K = 2500$

$C(t) = 2500(1 - e^{-0.02t})$

As $t \to \infty$: $\lim_{t \to \infty} C(t) = 2500$ tonnes

**Answer: C**
</details>

---

### Question 16: Agricultural Application
Yield response to nitrogen fertilizer is $y'(x) = 0.02 - 0.0002x$ (t/ha per kg/ha). If baseline yield is 1.5 t/ha, what nitrogen rate maximizes yield?

- (A) 50 kg/ha
- (B) 100 kg/ha
- (C) 150 kg/ha
- (D) 200 kg/ha
- (E) Cannot be determined

<details>
<summary><strong>Solution</strong></summary>

Maximum yield occurs when $y'(x) = 0$:

$0.02 - 0.0002x = 0$
$x = \frac{0.02}{0.0002} = 100$ kg/ha

**Answer: B**
</details>

---

## Section C: Exam-Style (Questions 17–20)

### Question 17: Lymphocyte Count (Q37 Style) [8 marks]

The rate of change of white blood cell count is:
$$L'(t) = 150e^{-0.2t} \text{ (cells/hour)}$$
Initially, there are 4000 cells.

**(a)** Find $L(t)$. [3 marks]

**(b)** What is the cell count after 5 hours? [2 marks]

**(c)** What is the limiting cell count as $t \to \infty$? [3 marks]

<details>
<summary><strong>Solution</strong></summary>

**(a)** $L(t) = \int 150e^{-0.2t}\,dt = -750e^{-0.2t} + C$

Apply $L(0) = 4000$: $4000 = -750 + C \implies C = 4750$

$$L(t) = 4750 - 750e^{-0.2t}$$

**(b)** $L(5) = 4750 - 750e^{-1} = 4750 - 276 \approx 4474$ cells

**(c)** As $t \to \infty$: $L(t) \to 4750$ cells
</details>

---

### Question 18: Soap Bubble [8 marks]

The rate of change of a soap bubble's radius is:
$$r'(t) = -3t^2 + 6t \text{ (cm/s)}$$
The initial radius is 2 cm.

**(a)** Find $r(t)$. [3 marks]

**(b)** What is the maximum radius reached? [3 marks]

**(c)** At what time does the maximum occur? [2 marks]

<details>
<summary><strong>Solution</strong></summary>

**(a)** $r(t) = \int (-3t^2 + 6t)\,dt = -t^3 + 3t^2 + C$

Apply $r(0) = 2$: $C = 2$

$$r(t) = -t^3 + 3t^2 + 2$$

**(b) & (c)** Set $r'(t) = 0$: $-3t(t - 2) = 0 \implies t = 0$ or $t = 2$

Maximum at $t = 2$ s: $r(2) = -8 + 12 + 2 = 6$ cm
</details>

---

### Question 19: Comprehensive Antiderivatives (Q14 Style) [9 marks]

Find the following antiderivatives:

**(a)** $\int \left(5x^4 - \frac{3}{x^2} + \frac{2}{\sqrt{x}}\right)\,dx$ [3 marks]

**(b)** $\int \left(e^{-2x} + \frac{4}{x}\right)\,dx$ [3 marks]

**(c)** $\int (x+2)^2\,dx$ [3 marks]

<details>
<summary><strong>Solution</strong></summary>

**(a)** Rewrite: $5x^4 - 3x^{-2} + 2x^{-1/2}$

$$x^5 + \frac{3}{x} + 4\sqrt{x} + C$$

**(b)** $$-\frac{1}{2}e^{-2x} + 4\ln|x| + C$$

**(c)** Expand: $(x+2)^2 = x^2 + 4x + 4$

$$\frac{x^3}{3} + 2x^2 + 4x + C$$
</details>

---

### Question 20: Land Rehabilitation [10 marks]

A degraded land site is being rehabilitated. The rate of vegetation recovery is:
$$V'(t) = 8e^{-0.2t} \text{ (% cover per year)}$$
Initial vegetation cover is 5%.

**(a)** Find the vegetation cover function $V(t)$. [3 marks]

**(b)** Calculate the total vegetation increase from $t=0$ to $t=10$ years. [4 marks]

**(c)** What is the long-term vegetation cover as $t \to \infty$? Interpret this ecologically. [3 marks]

<details>
<summary><strong>Solution</strong></summary>

**(a)** $V(t) = \int 8e^{-0.2t}\,dt = -40e^{-0.2t} + C$

Apply $V(0) = 5$: $5 = -40 + C \implies C = 45$

$$V(t) = 45 - 40e^{-0.2t}$$

**(b)** $V(10) - V(0) = [45 - 40e^{-2}] - 5 = 45 - 5.41 - 5 \approx 34.6$ percentage points

**(c)** As $t \to \infty$: $V(t) \to 45$%

**Interpretation:** The site approaches a maximum of 45% vegetation cover as it reaches ecological equilibrium.
</details>

---

## Quick Reference: Integration Rules

| Function | Antiderivative |
|----------|----------------|
| $k$ (constant) | $kx + C$ |
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $e^{kx}$ | $\frac{1}{k}e^{kx} + C$ |

---

## Exam Question Mapping

| Practice Q | Exam Q | Topic |
|------------|--------|-------|
| Q17 | Q37 | Lymphocyte integration |
| Q19 | Q14 | Basic antiderivatives |
| Q20 | — | Land rehabilitation (scientific application) |

---

*Practice questions aligned with SCIE1500 Week 6 content and Sample Final Examination*
