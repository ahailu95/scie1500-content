# Week 5 Practice Questions: Differentiation Techniques and Optimization

**Theme:** Finding the Best Outcome

**Exam Alignment:** Q13, Q28, Q37, Q38

---

## Foundational Questions (8)

### Q1. Product Rule

What is the derivative of $f(x) = x^2 \cdot e^x$?

**Options:**
- (A) $2xe^x$
- (B) $x^2 e^x$
- (C) $e^x(x^2 + 2x)$
- (D) $e^x(2x + x^2)$
- (E) Both C and D

---

### Q2. Quotient Rule

What is the derivative of $y = \frac{x+1}{x-1}$?

**Options:**
- (A) $\frac{1}{(x-1)^2}$
- (B) $\frac{-2}{(x-1)^2}$
- (C) $\frac{2}{(x-1)^2}$
- (D) $\frac{x}{(x-1)^2}$
- (E) $\frac{-1}{(x-1)^2}$

---

### Q3. Chain Rule

What is the derivative of $y = (3x + 2)^4$?

**Options:**
- (A) $4(3x + 2)^3$
- (B) $12(3x + 2)^3$
- (C) $3(3x + 2)^4$
- (D) $12(3x + 2)^4$
- (E) $4(3x + 2)^4$

---

### Q4. Exponential Derivative

What is the derivative of $y = e^{-0.5x}$?

**Options:**
- (A) $e^{-0.5x}$
- (B) $-e^{-0.5x}$
- (C) $-0.5e^{-0.5x}$
- (D) $0.5e^{-0.5x}$
- (E) $-0.5xe^{-0.5x}$

---

### Q5. Logarithm Derivative

What is the derivative of $y = \ln(5x)$?

**Options:**
- (A) $\frac{5}{x}$
- (B) $\frac{1}{5x}$
- (C) $\frac{1}{x}$
- (D) $\frac{5}{5x}$
- (E) Both C and D

---

### Q6. Second Derivative Test

If $f'(x_0) = 0$ and $f''(x_0) = -3$, what can we conclude about the point $x_0$?

**Options:**
- (A) Local minimum
- (B) Local maximum
- (C) Point of inflection
- (D) Neither maximum nor minimum
- (E) Cannot determine

---

### Q7. Finding Critical Points (Calculation)

Find all critical points of $f(x) = x^3 - 3x + 2$.

---

### Q8. Chain Rule with Exponential

What is the derivative of $y = e^{x^2}$?

**Options:**
- (A) $e^{x^2}$
- (B) $2e^{x^2}$
- (C) $2xe^{x^2}$
- (D) $x^2 e^{x^2}$
- (E) $2x e^{x^2-1}$

---

## Intermediate Questions (8)

### Q9. Combined Rules

Differentiate $y = x \cdot e^{2x}$.

---

### Q10. Product and Quotient Rules

Differentiate $y = \frac{x^2 e^x}{x+1}$.

---

### Q11. Chain Rule with Logarithm

Differentiate $y = \ln(x^2 + 3x + 2)$.

---

### Q12. Local Extrema Classification

Find and classify all local extrema of $f(x) = x^3 - 12x + 5$.

---

### Q13. MEY Concept

In the bioeconomic fishery model, MEY (Maximum Economic Yield) typically occurs at a stock level that is:

**Options:**
- (A) Lower than the MSY stock level
- (B) Equal to the MSY stock level
- (C) Higher than the MSY stock level
- (D) Equal to the carrying capacity K
- (E) Zero

---

### Q14. Rates of Change

The number of bacteria (in thousands) in a colony at time $t$ hours is given by $N(t) = 100t^{1/2} - t^{3/2} + 1$. Find the rate of change of the population at $t = 4$ hours.

---

### Q15. Motion Application

A ball is thrown upward with displacement $h(t) = 20t - 5t^2$ meters at time $t$ seconds. Find:
- (a) the initial velocity
- (b) when the ball reaches its maximum height
- (c) the maximum height

---

### Q16. SymPy Verification

Verify using SymPy that the derivative of $f(x) = x^2 \ln(x)$ is $f'(x) = 2x\ln(x) + x$. Show the SymPy code.

---

## Exam-Style Questions (4)

### Q17. Derivative Calculation (Q28 Style)

What is the derivative of the function $y = \frac{3}{4}x^4 + \frac{1}{4}x^2 - 3x + \ln x$?

**Options:**
- (A) $y' = 12x^3 + \frac{3}{x^2} - \frac{1}{2x^{3/2}}$
- (B) $y' = x^3 - 3 + \frac{1}{2}x$
- (C) $y' = \frac{3}{5}x^5 - \frac{3}{2}x^2 - \frac{3}{2}x$
- (D) $y' = 3x^3 + \frac{1}{2}x - 3 + \frac{1}{x}$
- (E) None of the above.

---

### Q18. Profit Maximization (Q38 Style)

A farmer is fattening 100 deer for sale. The deer currently weigh 50 kg each. Weight gain is 2 kg/day initially, declining by 0.1 kg/day each subsequent day. Feed costs \$0.50/animal/day. Market price is \$5/kg. The profit function is $\pi(t) = 25000 + 950t - 25t^2$. When should the farmer sell to maximize profit?

**Options:**
- (A) 10 days
- (B) 15 days
- (C) 19 days
- (D) 20 days
- (E) 25 days

---

### Q19. Schaefer Derivative (Q13 Style)

For the Schaefer model $G(S) = gS(1 - S/K)$, which expression represents $\frac{dG}{dS}$?

**Options:**
- (A) $g(1 - S/K)$
- (B) $g - gS/K$
- (C) $g - 2gS/K$
- (D) $gS - gS^2/K$
- (E) $g(1 - 2S/K)$

---

### Q20. Bioeconomic MEY (MEY Calculation)

For a fishery with $K = 12000$, $g = 0.10$, $e = 0.001$, $c = 4500$, $p = 3000$, the profit function simplifies to $\pi(S) = -0.025S^2 + 337.5S - 450000$. What is the MEY stock level?

**Options:**
- (A) 5000 tonnes
- (B) 6000 tonnes
- (C) 6750 tonnes
- (D) 7500 tonnes
- (E) 8000 tonnes

---

## Answer Key

### Multiple Choice

| Q | Answer | Q | Answer |
|---|--------|---|--------|
| 1 | E | 9 | See solution |
| 2 | B | 10 | See solution |
| 3 | B | 11 | See solution |
| 4 | C | 12 | See solution |
| 5 | E | 13 | C |
| 6 | B | 14 | 22 thousand/hr |
| 7 | x = ±1 | 15 | See solution |
| 8 | C | 16 | See solution |

### Exam-Style

| Q | Answer |
|---|--------|
| 17 | D |
| 18 | C (19 days) |
| 19 | C (or E) |
| 20 | C (6750 tonnes) |

---

## Detailed Solutions

### Q1. Product Rule
Using $(fg)' = f'g + fg'$:

Let $f(x) = x^2$ and $g(x) = e^x$.

$f'(x) = 2x$ and $g'(x) = e^x$

$(x^2 e^x)' = (2x)(e^x) + (x^2)(e^x) = e^x(2x + x^2) = e^x(x^2 + 2x)$

Options C and D are equivalent, just written in different order. **Answer: E**

---

### Q2. Quotient Rule
Using $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$:

$f = x+1$, $f' = 1$; $g = x-1$, $g' = 1$

$y' = \frac{(1)(x-1) - (x+1)(1)}{(x-1)^2} = \frac{x-1-x-1}{(x-1)^2} = \frac{-2}{(x-1)^2}$

**Answer: B**

---

### Q3. Chain Rule
Using chain rule with $u = 3x + 2$, $y = u^4$:

$\frac{dy}{du} = 4u^3$, $\frac{du}{dx} = 3$

$\frac{dy}{dx} = 4u^3 \cdot 3 = 12(3x + 2)^3$

**Answer: B**

---

### Q4. Exponential Derivative
Using $\frac{d}{dx}[e^{kx}] = ke^{kx}$ with $k = -0.5$:

$\frac{d}{dx}[e^{-0.5x}] = -0.5 \cdot e^{-0.5x}$

**Answer: C**

---

### Q5. Logarithm Derivative
Using chain rule: $\frac{d}{dx}[\ln(g(x))] = \frac{g'(x)}{g(x)}$

With $g(x) = 5x$ and $g'(x) = 5$:

$y' = \frac{5}{5x} = \frac{1}{x}$

Alternatively: $\ln(5x) = \ln(5) + \ln(x)$, so $y' = 0 + \frac{1}{x} = \frac{1}{x}$

**Answer: E** (C and D are equivalent)

---

### Q6. Second Derivative Test
The second derivative test states:
- If $f'(x_0) = 0$ and $f''(x_0) > 0$: local minimum
- If $f'(x_0) = 0$ and $f''(x_0) < 0$: local maximum

Since $f''(x_0) = -3 < 0$, we have a **local maximum** at $x_0$.

**Answer: B**

---

### Q7. Finding Critical Points
$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x+1)(x-1)$

Set $f'(x) = 0$: $x = -1$ or $x = 1$

**Answer: $x = -1$ and $x = 1$**

---

### Q8. Chain Rule with Exponential
Let $u = x^2$, then $y = e^u$:

$\frac{dy}{dx} = e^u \cdot \frac{du}{dx} = e^{x^2} \cdot 2x = 2xe^{x^2}$

**Answer: C**

---

### Q12. Local Extrema Classification
$f(x) = x^3 - 12x + 5$

$f'(x) = 3x^2 - 12 = 3(x+2)(x-2)$

Critical points: $x = -2$ and $x = 2$

$f''(x) = 6x$

At $x = -2$: $f''(-2) = -12 < 0$ → **local maximum**, $f(-2) = 21$

At $x = 2$: $f''(2) = 12 > 0$ → **local minimum**, $f(2) = -11$

---

### Q13. MEY Concept
MEY occurs at a **higher stock level** than MSY because at higher stock levels, fish are easier to catch, reducing effort and cost. Although harvest may be slightly lower, the cost savings increase profit.

**Answer: C**

---

### Q17. Derivative Calculation (Q28)
Differentiate term by term:

$\frac{d}{dx}\left[\frac{3}{4}x^4\right] = 3x^3$

$\frac{d}{dx}\left[\frac{1}{4}x^2\right] = \frac{1}{2}x$

$\frac{d}{dx}[-3x] = -3$

$\frac{d}{dx}[\ln x] = \frac{1}{x}$

Combine: $y' = 3x^3 + \frac{1}{2}x - 3 + \frac{1}{x}$

**Answer: D**

---

### Q18. Profit Maximization (Q38)
$\pi(t) = 25000 + 950t - 25t^2$

$\pi'(t) = 950 - 50t$

Set $\pi'(t) = 0$: $t = \frac{950}{50} = 19$ days

Verify: $\pi''(t) = -50 < 0$ ✓

**Answer: C (19 days)**

---

### Q19. Schaefer Derivative (Q13)
$G(S) = gS - \frac{g}{K}S^2$

$\frac{dG}{dS} = g - \frac{2g}{K}S = g - \frac{2gS}{K}$

**Answer: C** (Note: E is also equivalent: $g(1 - 2S/K)$)

---

### Q20. Bioeconomic MEY
$\pi(S) = -0.025S^2 + 337.5S - 450000$

$\pi'(S) = -0.05S + 337.5$

Set $\pi'(S) = 0$: $S = \frac{337.5}{0.05} = 6750$ tonnes

Note: MSY would be at $S = K/2 = 6000$ tonnes, so MEY (6750) is higher than MSY, as expected.

**Answer: C (6750 tonnes)**

---

## Key Formulas Summary

| Rule | Formula |
|------|---------|
| Product rule | $(fg)' = f'g + fg'$ |
| Quotient rule | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| Chain rule | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |
| Exponential | $\frac{d}{dx}[e^{kx}] = ke^{kx}$ |
| Logarithm | $\frac{d}{dx}[\ln x] = \frac{1}{x}$ |
| Chain (log) | $\frac{d}{dx}[\ln(g(x))] = \frac{g'(x)}{g(x)}$ |
| Second derivative test | $f'' > 0$ → min; $f'' < 0$ → max |

---

*Good luck on your exam!*
