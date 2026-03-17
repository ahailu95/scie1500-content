# 📋 SCIE1500 Formula Sheet

## Quick Reference for Analytical Methods

---

<div align="center">

# ∑ **FORMULA SHEET** ∫

### Essential Formulas at a Glance

---

</div>

---

# 🔢 Algebra

## Quadratic Formula
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant:** $\Delta = b^2 - 4ac$
- $\Delta > 0$: Two distinct real roots
- $\Delta = 0$: One repeated root
- $\Delta < 0$: No real roots

## Exponent Laws
| Rule | Formula |
|:-----|:--------|
| Product | $a^m \cdot a^n = a^{m+n}$ |
| Quotient | $\frac{a^m}{a^n} = a^{m-n}$ |
| Power | $(a^m)^n = a^{mn}$ |
| Zero | $a^0 = 1$ |
| Negative | $a^{-n} = \frac{1}{a^n}$ |
| Fractional | $a^{m/n} = \sqrt[n]{a^m}$ |

## Logarithm Laws
| Rule | Formula |
|:-----|:--------|
| Product | $\log(AB) = \log A + \log B$ |
| Quotient | $\log\left(\frac{A}{B}\right) = \log A - \log B$ |
| Power | $\log(A^n) = n \log A$ |
| Change of base | $\log_a x = \frac{\ln x}{\ln a}$ |
| Inverse | $\log_a(a^x) = x$ and $a^{\log_a x} = x$ |

---

# 📊 Functions

## Linear Function
$$y = mx + c$$
- Slope: $m = \frac{y_2 - y_1}{x_2 - x_1}$
- y-intercept: $c$

## Quadratic Function
$$y = ax^2 + bx + c$$
- Vertex: $\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)$
- Opens up if $a > 0$, down if $a < 0$

## Exponential Function
$$y = ab^x \quad \text{or} \quad y = ae^{kx}$$
- Growth if $k > 0$, decay if $k < 0$
- Doubling time: $t = \frac{\ln 2}{k}$
- Half-life: $t = \frac{\ln 2}{|k|}$

## Logistic Function
$$P(t) = \frac{L}{1 + Ae^{-kt}}$$
- $L$ = carrying capacity
- Inflection at $P = L/2$

## Schaefer Model
$$G(S) = gS\left(1 - \frac{S}{K}\right)$$
- MSY at $S = K/2$
- $\text{MSY} = \frac{gK}{4}$

---

# 📈 Sequences & Series

## Arithmetic
| Item | Formula |
|:-----|:--------|
| $n$th term | $a_n = a_1 + (n-1)d$ |
| Sum | $S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$ |

## Geometric
| Item | Formula |
|:-----|:--------|
| $n$th term | $a_n = a_1 \cdot r^{n-1}$ |
| Sum (finite) | $S_n = a_1 \cdot \frac{1 - r^n}{1 - r}$ |
| Sum (infinite, $\|r\| < 1$) | $S_\infty = \frac{a_1}{1 - r}$ |

---

# 🔄 Calculus: Derivatives

## Basic Rules
| Function | Derivative |
|:---------|:-----------|
| $c$ (constant) | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

## Differentiation Rules
| Rule | Formula |
|:-----|:--------|
| Sum | $(f + g)' = f' + g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| Chain | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |

## Critical Points & Optimization
- Critical points: where $f'(x) = 0$ or undefined
- Second derivative test:
  - $f''(x) > 0$: local minimum
  - $f''(x) < 0$: local maximum

---

# ∫ Calculus: Integration

## Basic Rules
| Function | Antiderivative |
|:---------|:---------------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln\|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |

## Fundamental Theorem of Calculus
$$\int_a^b f(x)\,dx = F(b) - F(a)$$

## Average Value
$$\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

## Economic Surplus
$$\text{CS} = \int_0^{Q^*} D(Q)\,dQ - P^* \cdot Q^*$$

$$\text{PS} = P^* \cdot Q^* - \int_0^{Q^*} S(Q)\,dQ$$

---

# 🦎 Lotka-Volterra Model

**Prey:** $\frac{dN}{dt} = rN - aNP$

**Predator:** $\frac{dP}{dt} = baNP - mP$

**Equilibrium (non-trivial):**
$$N^* = \frac{m}{ba}, \quad P^* = \frac{r}{a}$$

---

# 🔢 Combinatorics

## Factorials
$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$
$$0! = 1$$

## Permutations (Order Matters)
$$P(n,k) = \frac{n!}{(n-k)!}$$

*Number of ways to arrange $k$ items from $n$ distinct items*

## Combinations (Order Doesn't Matter)
$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

*Number of ways to choose $k$ items from $n$ distinct items*

---

# 🎲 Probability

## Basic Rules
| Rule | Formula |
|:-----|:--------|
| Complement | $P(A^c) = 1 - P(A)$ |
| Addition | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Conditional | $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |

## Sample Space
- $n$ coin tosses: $|S| = 2^n$
- Rolling a die $k$ times: $|S| = 6^k$

## Bayes' Theorem
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

## Medical Testing (PPV)
$$\text{PPV} = P(\text{Disease}|\text{Positive}) = \frac{\text{Sensitivity} \times \text{Prevalence}}{P(\text{Positive})}$$

where:
$$P(\text{Positive}) = \text{Sensitivity} \times \text{Prevalence} + (1 - \text{Specificity}) \times (1 - \text{Prevalence})$$

## Expected Value
$$E[X] = \sum_i x_i \cdot P(x_i)$$

## Variance
$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

## Binomial Distribution
$$P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$$

where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

- $E[X] = np$
- $\text{Var}(X) = np(1-p)$

---

# 📊 Hypothesis Testing

## The Four Steps
1. **State hypotheses** ($H_0$ and $H_a$)
2. **Calculate test statistic** (e.g., $\hat{p} = k/n$)
3. **Compute p-value**
4. **Make decision** (reject or fail to reject $H_0$)

## ⚠️ One-Tailed vs Two-Tailed (CRITICAL)

| Question Type | Hypotheses | Test Type |
|:--------------|:-----------|:----------|
| "Is it **greater** than...?" | $H_0: p \le p_0$ vs $H_a: p > p_0$ | One-tailed (upper) |
| "Is it **less** than...?" | $H_0: p \ge p_0$ vs $H_a: p < p_0$ | One-tailed (lower) |
| "Is it **different** from...?" | $H_0: p = p_0$ vs $H_a: p \ne p_0$ | Two-tailed |

## p-Value Calculation (Binomial)

**One-tailed (upper):** $\text{p-value} = P(X \ge k \;|\; H_0)$

**One-tailed (lower):** $\text{p-value} = P(X \le k \;|\; H_0)$

**Two-tailed:** $\text{p-value} = P(\text{values as extreme as } k \text{ in either direction})$

## Decision Rule
At significance level $\alpha = 0.05$:
- **p-value < 0.05:** Reject $H_0$ (statistically significant)
- **p-value ≥ 0.05:** Fail to reject $H_0$ (insufficient evidence)

## Sample Proportion
$$\hat{p} = \frac{k}{n}$$

where $k$ = observed successes, $n$ = total trials

---

# 🔄 Trigonometry

## Degree-Radian Conversion
$$\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$$

## Key Values

| $\theta$ | 0 | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|:---------|:-:|:---------------:|:---------------:|:---------------:|:---------------:|
| $\sin\theta$ | 0 | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | 1 |
| $\cos\theta$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | 0 |
| $\tan\theta$ | 0 | $\frac{1}{\sqrt{3}}$ | 1 | $\sqrt{3}$ | undef |

## Identities
$$\sin^2\theta + \cos^2\theta = 1$$

$$\tan\theta = \frac{\sin\theta}{\cos\theta}$$

## Sinusoidal Function
$$y = A\sin(Bx + C) + D$$

| Parameter | Meaning |
|:----------|:--------|
| $\|A\|$ | Amplitude |
| $\frac{2\pi}{\|B\|}$ | Period |
| $-\frac{C}{B}$ | Phase shift |
| $D$ | Vertical shift |

---

# 📊 Linear Programming

## Standard Form
**Maximize (or Minimize):** $Z = c_1x_1 + c_2x_2 + ...$

**Subject to:**
- Constraints (inequalities)
- $x_1, x_2, ... \geq 0$

## Corner Point Theorem
> The optimal solution occurs at a **vertex** (corner point) of the feasible region.

## Solution Method
1. Graph constraints
2. Identify feasible region
3. Find corner points
4. Evaluate objective function at each corner
5. Select optimal solution

---

<div align="center">

---

# 🎓 Good Luck! 🎓

---

*SCIE1500: Analytical Methods for Scientists*

---

</div>
