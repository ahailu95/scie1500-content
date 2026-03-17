# Week 2: Exponential and Logarithmic Functions

## Theme: "Modeling Unbounded Growth and Decay"

**Science Context:** Plastic production growth, radioactive decay, population growth (unlimited)

**Learning Outcomes:** At the end of this week you should be able to:

1. Understand the definition and properties of exponential functions
2. Recognize the special number $e \approx 2.718$ and why it matters
3. Understand the definition of the logarithm function as the inverse of the exponential
4. Apply logarithm rules to simplify expressions
5. Solve exponential equations using logarithms
6. Connect geometric sequences to exponential functions

**Exam Alignment:** Q8, Q17, Q20, Q23, Q27

---

## Introduction: Why Exponential Growth Matters

### The Power of Compounding

There is a fundamental tendency for populations to grow exponentially when unconstrained. Without limits on space, food, or other resources, populations grow geometrically.

**Example: Bacterial Growth**

If a bacterium replicates (doubles) every 20 minutes, after $h$ hours it would become:

$$P(h) = P(0) \cdot 2^{3h} = 1 \times 2^{3h}$$

| Time | Population |
|------|------------|
| 1 hour | 8 bacteria |
| 3 hours | 512 bacteria |
| 10 hours | 1,073,742,000 bacteria (1.07 billion) |

If that same bacterium were to divide every 19 minutes instead, after 10 hours it would become **3.2 billion**!

> **Key Insight:** Compounding effect means small differences in growth rate make huge differences over time.

---

## The Exponential Function

### Definition

A function of the form

$$f(x) = a^x, \quad a > 0$$

is an exponential function. The base $a$ determines the rate of growth or decay.

### Key Examples

| Function | Behaviour |
|----------|-----------|
| $f(x) = 2^x$ | Doubling with each unit increase in $x$ |
| $f(x) = 3^x$ | Tripling with each unit increase in $x$ |
| $f(x) = (0.5)^x$ | Halving with each unit increase (decay) |

---

## The Special Number $e$: The Compound Interest Approach

### A Thought Experiment

Imagine you invest \$1 in a bank account with 100% annual interest rate. How much do you have after 1 year? It depends on how often interest is compounded.

**Scenario A: Interest paid once at year end**
$$A = 1 \times (1 + 1) = \$2.00$$

**Scenario B: Interest paid twice (50% each half-year)**
$$A = 1 \times \left(1 + \frac{1}{2}\right)^2 = 1 \times 1.5^2 = \$2.25$$

**Scenario C: Interest paid quarterly (25% each quarter)**
$$A = 1 \times \left(1 + \frac{1}{4}\right)^4 = 1 \times 1.25^4 = \$2.4414$$

**Scenario D: Interest paid monthly**
$$A = 1 \times \left(1 + \frac{1}{12}\right)^{12} = \$2.6130$$

**Scenario E: Interest paid daily**
$$A = 1 \times \left(1 + \frac{1}{365}\right)^{365} = \$2.7146$$

### 2.3.2 The Pattern: Convergence to a Limit

As we compound more frequently, the final amount increases—but it doesn't grow without bound. It approaches a limit:

| Compounding | Formula | Value |
|-------------|---------|-------|
| Annual ($n=1$) | $(1 + 1/1)^1$ | 2.0000 |
| Semi-annual ($n=2$) | $(1 + 1/2)^2$ | 2.2500 |
| Quarterly ($n=4$) | $(1 + 1/4)^4$ | 2.4414 |
| Monthly ($n=12$) | $(1 + 1/12)^{12}$ | 2.6130 |
| Daily ($n=365$) | $(1 + 1/365)^{365}$ | 2.7146 |
| Hourly ($n=8760$) | $(1 + 1/8760)^{8760}$ | 2.7181 |
| Continuous ($n \to \infty$) | $\lim_{n \to \infty}(1 + 1/n)^n$ | 2.71828... |

### 2.3.3 Definition of Euler's Number

The number these values approach is called **Euler's number**:

$$\boxed{e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2.71828...}$$

This is **continuous compounding**—interest being added infinitely often, in infinitely small amounts.

> **Key insight:** The number $e$ emerges naturally from the mathematics of growth. It's not an arbitrary choice—it's what nature "picks" when growth happens continuously.

### 2.3.4 Python: Visualizing Convergence to $e$

```python
import numpy as np
import matplotlib.pyplot as plt

# Calculate (1 + 1/n)^n for various n
n_values = np.array([1, 2, 4, 12, 52, 365, 1000, 10000, 100000])
compound_values = (1 + 1/n_values)**n_values

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart showing convergence
ax.bar(range(len(n_values)), compound_values, color='steelblue', edgecolor='navy')
ax.axhline(y=np.e, color='red', linestyle='--', linewidth=2, label=f'e ≈ {np.e:.5f}')
ax.set_xticks(range(len(n_values)))
ax.set_xticklabels(['1\n(annual)', '2\n(semi)', '4\n(qtr)', '12\n(mth)', 
                   '52\n(wk)', '365\n(day)', '1000', '10000', '100000'], fontsize=9)
ax.set_xlabel('Number of compounding periods (n)', fontsize=11)
ax.set_ylabel('Final amount: $(1 + 1/n)^n$', fontsize=11)
ax.set_title('Compound Interest Converges to e', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.set_ylim(1.8, 2.8)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(compound_values):
    ax.text(i, v + 0.02, f'{v:.4f}', ha='center', fontsize=8)

plt.tight_layout()
plt.show()
```

---

## The Special Number $e$: The Slope Property

### Slopes of Curves

Recall from Week 1 that the **slope** (or **gradient**) of a line measures its steepness: how much $y$ changes when $x$ increases by 1.

For a curve (not a straight line), the slope changes from point to point. At any location, we can approximate the slope by looking at how much the function changes over a small interval:

$$\text{Approximate slope at } x \approx \frac{f(x + h) - f(x)}{h}$$

where $h$ is a small number (like 0.001). The smaller $h$ is, the better the approximation.

### 2.4.2 Comparing Slopes at $x = 0$ for Different Bases

Let's compute the slope of different exponential functions at $x = 0$:

**For $f(x) = 2^x$:**

| $h$ | $\frac{2^{0+h} - 2^0}{h} = \frac{2^h - 1}{h}$ |
|-----|----------------------------------------------|
| 0.1 | 0.7177 |
| 0.01 | 0.6956 |
| 0.001 | 0.6934 |
| 0.0001 | 0.6932 |

The slope of $2^x$ at $x = 0$ is approximately **0.693** (less than 1).

**For $f(x) = 3^x$:**

| $h$ | $\frac{3^{0+h} - 3^0}{h} = \frac{3^h - 1}{h}$ |
|-----|----------------------------------------------|
| 0.1 | 1.1612 |
| 0.01 | 1.1047 |
| 0.001 | 1.0992 |
| 0.0001 | 1.0987 |

The slope of $3^x$ at $x = 0$ is approximately **1.099** (more than 1).

**Observation:** 
- Base 2: slope at $x=0$ ≈ 0.693 (less than 1)
- Base 3: slope at $x=0$ ≈ 1.099 (more than 1)

Since the slope changes continuously with the base, there must be some base between 2 and 3 where the slope at $x = 0$ is **exactly 1**.

### 2.4.3 The Magic of Base $e$

**For $f(x) = e^x$:**

| $h$ | $\frac{e^{0+h} - e^0}{h} = \frac{e^h - 1}{h}$ |
|-----|----------------------------------------------|
| 0.1 | 1.0517 |
| 0.01 | 1.0050 |
| 0.001 | 1.0005 |
| 0.0001 | 1.00005 |

The slope of $e^x$ at $x = 0$ is exactly **1**.

But there's more! Let's check the slope at other points:

| Point | Function value $e^x$ | Slope at that point |
|-------|---------------------|---------------------|
| $x = 0$ | $e^0 = 1$ | ≈ 1.000 |
| $x = 1$ | $e^1 ≈ 2.718$ | ≈ 2.718 |
| $x = 2$ | $e^2 ≈ 7.389$ | ≈ 7.389 |

### 2.4.4 The Remarkable Property of $e$

$$\boxed{\text{For } f(x) = e^x: \text{ the slope at any point } x \text{ equals the function value } e^x}$$

**In other words:** The function $e^x$ grows at a rate equal to its current value. This is the **only** exponential function with this property!

> **The number $e$ is the unique base for which the exponential function's slope equals its height everywhere.**

This is why $e$ appears everywhere in nature:
- Populations grow at a rate proportional to their size → $e$ appears
- Radioactive decay occurs at a rate proportional to remaining atoms → $e$ appears
- Continuously compounded interest grows proportionally → $e$ appears

### 2.4.5 Python: Visualizing "Slope Equals Height"

```python
import numpy as np
import matplotlib.pyplot as plt

def numerical_slope(f, x, h=0.0001):
    """Calculate approximate slope of f at point x"""
    return (f(x + h) - f(x)) / h

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: e^x with tangent lines showing slope = height
x = np.linspace(-1, 2, 200)
y = np.exp(x)

ax1.plot(x, y, 'b-', linewidth=2.5, label='$f(x) = e^x$')

# Draw tangent lines and annotations at several points
x_points = [0, 0.5, 1, 1.5]
for xi in x_points:
    height = np.exp(xi)
    slope = height  # For e^x, slope = height!
    
    # Tangent line
    x_tan = np.linspace(xi - 0.4, xi + 0.4, 50)
    y_tan = height + slope * (x_tan - xi)
    ax1.plot(x_tan, y_tan, 'r-', linewidth=1.5, alpha=0.7)
    ax1.plot(xi, height, 'go', markersize=10, zorder=5)
    
    # Annotation
    ax1.annotate(f'slope ≈ {slope:.2f}\nheight = {height:.2f}', 
                 xy=(xi, height), xytext=(xi + 0.25, height + 0.3),
                 fontsize=9, ha='left')

ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('$e^x$: At Every Point, Slope = Height', fontsize=13, fontweight='bold')
ax1.legend(loc='upper left', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-1, 2.5)
ax1.set_ylim(0, 6)

# Right plot: Comparing bases - slope at x=0 vs base
bases = np.linspace(1.5, 4, 100)
slopes_at_zero = []
for b in bases:
    h = 0.0001
    slope = (b**h - 1) / h
    slopes_at_zero.append(slope)

ax2.plot(bases, slopes_at_zero, 'b-', linewidth=2)
ax2.axhline(y=1, color='red', linestyle='--', linewidth=1.5, label='Target: slope = 1')
ax2.axvline(x=np.e, color='green', linestyle='--', linewidth=1.5, label=f'e ≈ {np.e:.3f}')
ax2.plot(np.e, 1, 'go', markersize=12)

ax2.set_xlabel('Base', fontsize=12)
ax2.set_ylabel('Slope of $b^x$ at $x = 0$', fontsize=12)
ax2.set_title('Finding e: Which Base Gives Slope = 1?', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Annotate
ax2.annotate('Base 2:\nslope ≈ 0.69', xy=(2, 0.693), xytext=(2.3, 0.5), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='gray'))
ax2.annotate('Base 3:\nslope ≈ 1.10', xy=(3, 1.099), xytext=(3.3, 1.3), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='gray'))

plt.tight_layout()
plt.show()
```

### 2.4.6 Two Equivalent Definitions of $e$ — Summary

| Definition | Formula | Interpretation |
|------------|---------|----------------|
| **Compound Interest Limit** | $e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$ | What you get from continuous compounding of 100% interest |
| **Slope Equals Height** | $e$ is the unique base where slope of $e^x$ equals $e^x$ at every point | The base where exponential growth is "self-similar" |

> **Preview:** In Week 5, when you learn about **derivatives**, you'll see that "slope at a point" has a formal name and precise definition. The "slope equals height" property will be written elegantly as: $\frac{d}{dx}[e^x] = e^x$. This makes $e$ the most important base in calculus.

---

## Graph of $\exp(x)$

We often write $\exp(x)$ to denote $e^x$.

- **Domain:** $\{x \in \mathbb{R}\}$ (all real numbers)
- **Range:** $\{y \in \mathbb{R} : y > 0\}$ (positive reals only)
- Always passes through $(0, 1)$ since $e^0 = 1$
- Always increasing
- Horizontal asymptote at $y = 0$ as $x \to -\infty$

### Exponential Laws

All the standard exponential laws hold:

| Law | Expression |
|-----|------------|
| Product | $e^x \cdot e^y = e^{x+y}$ |
| Quotient | $\frac{e^x}{e^y} = e^{x-y}$ |
| Power | $(e^x)^y = e^{xy}$ |
| Negative exponent | $e^{-x} = \frac{1}{e^x}$ |

---

## Growth and Decay Models

### General Form

The general exponential model is:

$$P(t) = P_0 \cdot e^{kt}$$

where:
- $P_0$ = initial value (at $t = 0$)
- $k$ = growth/decay rate constant
- If $k > 0$: exponential **growth**
- If $k < 0$: exponential **decay**

### Example 2.1: Bacteria Population Growth

A bacteria population starts with 400 bacteria and grows according to:

$$b(t) = 400e^{1.12567t}$$

where $t$ is in hours.

**Questions:**
1. How many bacteria will there be after 3 hours?
2. At what time will the population double?

**Solution:**

1. $b(3) = 400e^{1.12567 \times 3} = 400e^{3.377} \approx 11,713$ bacteria

2. We need $b(t) = 800$:
   $$400e^{1.12567t} = 800$$
   $$e^{1.12567t} = 2$$
   $$1.12567t = \ln(2)$$
   $$t = \frac{\ln(2)}{1.12567} = \frac{0.693}{1.12567} \approx 0.616 \text{ hours}$$

### Example 2.2: Tree Growth (Devaranavadgi et al., 2013)

The height-age growth of *Acacia catechu* is modelled as:

$$h(t) = 5.966 \exp\left(-\frac{3.0001}{t + 0.3501}\right)$$

where $h(t)$ is height in metres and $t$ is time in years.

**Questions:**
1. What is the maximum height of the tree?
2. What is the initial height?
3. How long does it take to reach half its final height?

**Solution:**

1. Maximum height: As $t \to \infty$, the exponential term approaches $e^0 = 1$, so $h_{\max} = 5.966$ m

2. Initial height: $h(0) = 5.966 \exp\left(-\frac{3.0001}{0.3501}\right) = 5.966 \times e^{-8.57} \approx 0.0004$ m

3. Half final height: Solve $h(t) = 2.983$ m, yielding $t \approx 3.978$ years

---

## The Logarithm Function

### The Inverse of the Exponential

Since the exponential function is one-to-one, it has an inverse. We call this inverse the **natural logarithm function**, denoted $\ln(x)$.

$$y = e^x \iff x = \ln(y)$$

### Graph of $\ln(x)$

The graph of $\ln(x)$ is the reflection of $e^x$ across the line $y = x$:

- **Domain:** $\{x \in \mathbb{R} : x > 0\}$ (positive reals only)
- **Range:** $\{y \in \mathbb{R}\}$ (all real numbers)
- Passes through $(1, 0)$ since $\ln(1) = 0$
- Vertical asymptote at $x = 0$

### Fundamental Inverse Relationships

Since $\exp$ and $\ln$ are inverses:

$$e^{\ln(x)} = x \quad \text{and} \quad \ln(e^x) = x$$

Or equivalently:

$$\exp(\ln(x)) = \ln(\exp(x)) = x$$

### Logarithm Laws

| Law | Expression |
|-----|------------|
| Product | $\ln(xy) = \ln(x) + \ln(y)$ |
| Quotient | $\ln\left(\frac{x}{y}\right) = \ln(x) - \ln(y)$ |
| Power | $\ln(x^r) = r \ln(x)$ |
| Special values | $\ln(1) = 0$, $\ln(e) = 1$ |

### Example 2.3: Simplifying Logarithmic Expressions

Simplify the following:

**(a)** $\ln(e^x) + \ln(e^{3x})$

$$= x + 3x = 4x$$

**(b)** $e^{\ln(x^2)}$

$$= x^2$$

**(c)** $e^{\ln(\sqrt{x})}$

$$= \sqrt{x}$$

**(d)** $\exp(\ln(x^2 + x + 2))$

$$= x^2 + x + 2$$

---

## Solving Exponential and Logarithmic Equations

The key strategy: use the inverse relationship between $\exp$ and $\ln$.

### Example 2.4: Solve for $x$

**(a)** $e^{2x} = 1$

$$2x = \ln(1) = 0 \implies x = 0$$

**(b)** $e^{x^2} = 4$

$$x^2 = \ln(4) \implies x = \pm\sqrt{\ln(4)} = \pm\sqrt{1.386} \approx \pm 1.177$$

**(c)** $\ln(x^2) = 4$

$$x^2 = e^4 \implies x = \pm e^2 \approx \pm 7.389$$

**(d)** $\ln(x^2) = 8$

$$x^2 = e^8 \implies x = \pm e^4 \approx \pm 54.60$$

---

## The "70 over r" Rule

A useful approximation for doubling time:

> **The doubling time of a population growing at rate $r$% per unit time is approximately $\frac{70}{r}$ time units.**

**Derivation:**

We want to find $T$ such that $P_0 e^{rT} = 2P_0$:

$$e^{rT} = 2$$
$$rT = \ln(2) \approx 0.693$$
$$T = \frac{0.693}{r}$$

When $r$ is expressed as a percentage (e.g., $r = 0.03$ for 3%), we have:

$$T = \frac{0.693}{0.03} = 23.1 \text{ years}$$

Which equals $\frac{69.3}{3} \approx \frac{70}{3}$ years.

**Example:** A population growing at 5% per year doubles every $\frac{70}{5} = 14$ years.

### Tripling Time?

Following similar logic: $\frac{\ln(3)}{r} = \frac{1.099}{r} \approx \frac{110}{r\%}$

---

## Geometric Sequences as Discrete Exponentials

### Definition

A sequence $\{a_1, a_2, a_3, \ldots\}$ is a **geometric sequence** if:
- $a_1 = a$ (first term)
- $a_k = a \cdot r^{k-1}$ for $k > 1$

where $r \neq 0$ is the **common ratio**.

| Condition | Behaviour |
|-----------|-----------|
| $r > 1$ | Increasing sequence |
| $0 < r < 1$ | Decreasing sequence |
| $r = 1$ | Constant sequence |

### Connection to Exponential Functions

A geometric sequence is essentially a **discrete sampling** of an exponential function:

$$a_n = a \cdot r^{n-1} \longleftrightarrow f(x) = a \cdot r^{x-1}$$

The sequence values lie exactly on the exponential curve at integer points.

### Example 2.5: Compound Interest

Chork Meng invests $100,000 in a fixed deposit with 5% monthly interest.

**(a)** How much after 3 years (36 months)?

$$a_{36} = 100,000 \times (1.05)^{36} = \$579,181.60$$

**(b)** How long to double?

$$100,000 \times (1.05)^k = 200,000$$
$$(1.05)^k = 2$$
$$k \ln(1.05) = \ln(2)$$
$$k = \frac{\ln(2)}{\ln(1.05)} = \frac{0.693}{0.0488} = 14.2 \text{ months}$$

So it takes **15 months** to double.

### Example 2.6: Petroleum Usage

Petroleum oil use increases at 7% annually. In 2022, usage was 3.95 million barrels/day.

**(a)** Daily usage in 2032?

$$P_{11} = 3.95 \times (1.07)^{10} = 7.77 \text{ million b/d}$$

---

## Geometric Series (Sum of Geometric Sequence)

### Formula Derivation

Let $S_n = a + ar + ar^2 + \cdots + ar^{n-1}$

Multiply by $r$: $rS_n = ar + ar^2 + \cdots + ar^n$

Subtract:
$$S_n - rS_n = a - ar^n$$
$$S_n(1 - r) = a(1 - r^n)$$
$$S_n = \frac{a(1 - r^n)}{1 - r}, \quad r \neq 1$$

### Sum to Infinity

If $|r| < 1$, the series converges:

$$\lim_{n \to \infty} S_n = \frac{a}{1 - r}$$

---

## Connecting Growth Rates

### Population Dynamics Terminology

From population studies (especially Andrewartha, 1970), several growth measures are connected:

| Measure | Symbol | Meaning |
|---------|--------|---------|
| Intrinsic rate of increase | $r_m$ | Per capita instantaneous growth rate |
| Finite rate of increase | $\lambda$ | Multiplicative factor: $\lambda = e^{r_m}$ |
| Net reproductive rate | $R_0$ | Offspring per individual per generation |
| Generation time | $T$ | Mean time between generations |

**Relationships:**

$$\lambda = e^{r_m}$$
$$R_0 = e^{r_m T}$$

**Example: Rice Weevil**

- $r_m = 0.76$ per week
- $T = 6.2$ weeks
- $\lambda = e^{0.76} = 2.14$ (population multiplies by 2.14 each week)
- $R_0 = e^{0.76 \times 6.2} = e^{4.71} = 111$ (each individual produces 111 offspring per generation)

---

## Application: Probability and Risk

Exponential and logistic functions appear frequently in probability modelling.

### Example 2.7: Disease Risk

Suppose the probability $p$ of contracting a disease is a function of risk $x$:

$$p = \frac{1}{1 + e^{-3x}}$$

**Properties:**
- When $x = 0$: $p = \frac{1}{1 + 1} = \frac{1}{2}$
- When $x < 0$ (negative risk): $p < \frac{1}{2}$
- When $x > 0$ (positive risk): $p > \frac{1}{2}$
- $p$ is always an increasing function of $x$
- As $x \to -\infty$: $p \to 0$
- As $x \to +\infty$: $p \to 1$

> **Note:** This logistic function will be studied in detail in Week 3.

---

## Summary: Key Formulas for Week 2

| Topic | Key Formula |
|-------|-------------|
| Euler's number (limit) | $e = \lim_{n \to \infty}(1 + 1/n)^n \approx 2.718$ |
| Euler's number (slope) | $e$ is the unique base where slope of $e^x$ = value $e^x$ |
| Exponential function | $f(x) = e^x$ |
| General growth/decay | $P(t) = P_0 e^{kt}$ |
| Logarithm definition | $y = \ln(x) \iff e^y = x$ |
| Log of product | $\ln(ab) = \ln(a) + \ln(b)$ |
| Log of quotient | $\ln(a/b) = \ln(a) - \ln(b)$ |
| Log of power | $\ln(a^n) = n\ln(a)$ |
| Geometric sequence | $a_n = a_1 \cdot r^{n-1}$ |
| Geometric series | $S_n = \frac{a(1-r^n)}{1-r}$ |
| Doubling time | $T = \frac{\ln(2)}{r} \approx \frac{70}{r\%}$ |

---

## Looking Ahead: Week 3

In Week 3, we will explore what happens when growth has **limits** — the logistic function:

$$P(t) = \frac{K}{1 + Ae^{-\alpha t}}$$

where $K$ is the carrying capacity. We'll also introduce the Schaefer fish growth model, which connects to optimization problems later in the course.

---

*Materials adapted from SCIE1500 lecture notes (Khan, Hailu) and aligned with Final Examination S2 2025.*
