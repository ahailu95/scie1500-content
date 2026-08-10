# Week 7: Definite Integrals and Applications

## Act II: Measuring Accumulation — Chapter 2

> *"The definite integral answers the question: what is the total? From pollution to population, from profit to land area, integration transforms rates into accumulated totals."*

---

## Theme: "Definite Integrals and Applications"

**Science Context:** Ocean plastic accumulation, consumer and producer surplus, water reservoir volumes

**Learning Outcomes:** At the end of this week you should be able to:

1. State and apply the Fundamental Theorem of Calculus
2. Evaluate definite integrals using antiderivatives
3. Interpret a definite integral as the area under a curve between two bounds
4. Calculate areas between curves and interpret them in applied contexts
5. Compute consumer surplus and producer surplus from supply and demand functions
6. Apply definite integration to accumulation problems in ecology and economics

---

> **📓 About "Try it in Python" boxes:** Throughout this lesson, these boxes reference specific code examples by ID — e.g. **W7-CS03** means *Week 7, Code Snippet 3*. Find the matching code under **Notes → Python Code Snippets** for this week; each entry there is labelled with its ID.

## 1. From Indefinite to Definite: The Completion of Calculus

### Building on Week 6

In Week 6, we learned to find **antiderivatives** (indefinite integrals):

$$\int f(x)\,dx = F(x) + C$$

This week, we answer a more concrete question: **What is the total accumulated quantity between two points?**

### The Definite Integral

The **definite integral** of $f(x)$ from $a$ to $b$ is written:

$$\int_a^b f(x)\,dx$$

where:
- $a$ = lower limit of integration
- $b$ = upper limit of integration
- $f(x)$ = the integrand
- $dx$ = indicates integration with respect to $x$

**Key Distinction:**
| Indefinite Integral        | Definite Integral                     |
| -------------------------- | ------------------------------------- |
| $\int f(x)\,dx = F(x) + C$ | $\int_a^b f(x)\,dx = \text{a number}$ |
| A family of functions      | A specific numerical value            |
| Includes $+ C$             | No constant of integration            |

---

## 2. The Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus (FTC) is arguably the most important result in all of calculusconnecting differentiation and integration as inverse processes.

### Part 1: Differentiation of an Integral

If $f$ is continuous on $[a, b]$, then the function:

$$F(x) = \int_a^x f(t)\,dt$$

is differentiable, and:

$$\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)$$

**Interpretation:** The derivative of the "area so far" function equals the original function.

### Part 2: Evaluation of Definite Integrals

If $F'(x) = f(x)$ (i.e., $F$ is any antiderivative of $f$), then:

$$\boxed{\int_a^b f(x)\,dx = F(b) - F(a)}$$

This is often written using the notation:

$$\int_a^b f(x)\,dx = \left[F(x)\right]_a^b = F(b) - F(a)$$

**The FTC tells us:** To compute a definite integral, find any antiderivative $F(x)$, then evaluate at the limits and subtract.

### 2.3 Historical Note: Newton and Leibniz

The Fundamental Theorem of Calculus was one of the greatest intellectual breakthroughs in scientific history — and was independently discovered *twice*:

- **Isaac Newton** (England, ~1666) developed his "method of fluxions" during the plague years when Cambridge closed. He used integration to compute planetary orbits and gravitation but did not publish for decades.
- **Gottfried Wilhelm Leibniz** (Germany, ~1675–1684) developed the same ideas independently and invented the notation $\int$ and $dx$ that we still use today.

Their simultaneous discovery sparked one of history's bitterest priority disputes, dividing European mathematicians for a generation. Despite the controversy, both formulations are correct — and equivalent. The notation we use (Leibniz's $\int_a^b f(x)\,dx$) won out because it is far more convenient for computation.

**Why does this matter?** The FTC established that differentiation and integration are inverse operations — a connection so profound it unified centuries of separate mathematical work and made modern physics, engineering, and economics possible.

---

## 3. Computing Definite Integrals

### Example 7.1: Basic Polynomial

Evaluate $\int_1^3 x^2\,dx$

**Solution:**

Step 1: Find antiderivative: $F(x) = \frac{x^3}{3}$

Step 2: Apply FTC Part 2:
$$\int_1^3 x^2\,dx = \left[\frac{x^3}{3}\right]_1^3 = \frac{3^3}{3} - \frac{1^3}{3} = \frac{27}{3} - \frac{1}{3} = \frac{26}{3} \approx 8.67$$

### Example 7.2: Exponential Function

Evaluate $\int_0^2 e^x\,dx$

**Solution:**
$$\int_0^2 e^x\,dx = \left[e^x\right]_0^2 = e^2 - e^0 = e^2 - 1 \approx 6.39$$

### Example 7.3: Logarithmic Integration

Evaluate $\int_1^4 \frac{1}{x}\,dx$

**Solution:**
$$\int_1^4 \frac{1}{x}\,dx = \left[\ln|x|\right]_1^4 = \ln(4) - \ln(1) = \ln(4) - 0 = \ln(4) \approx 1.386$$

### Example 7.4: Mixed Function

Evaluate $\int_0^1 (3x^2 + 2x - 1)\,dx$

**Solution:**
$$\int_0^1 (3x^2 + 2x - 1)\,dx = \left[x^3 + x^2 - x\right]_0^1$$
$$= (1^3 + 1^2 - 1) - (0 + 0 - 0) = 1 + 1 - 1 = 1$$

> **📓 Try it in Python**
>
> - **W7-CS01** — *Basic Setup and Imports*: Load the libraries used throughout this week.
> - **W7-CS02** — *Definite Integral with SymPy*: Evaluate definite integrals symbolically.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 4. Properties of Definite Integrals

### 4.1 Additivity Over Intervals

$$\int_a^c f(x)\,dx = \int_a^b f(x)\,dx + \int_b^c f(x)\,dx$$

### 4.2 Reversing Limits

$$\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$$

### 4.3 Zero-Width Interval

$$\int_a^a f(x)\,dx = 0$$

### 4.4 Constant Multiple

$$\int_a^b k \cdot f(x)\,dx = k \int_a^b f(x)\,dx$$

### 4.5 Sum/Difference Rule

$$\int_a^b [f(x) \pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$$

---

## 5. Geometric Interpretation: Area Under a Curve

### 5.1 Positive Functions

When $f(x) \geq 0$ on $[a, b]$, the definite integral equals the **area** between the curve and the $x$-axis:

$$\text{Area} = \int_a^b f(x)\,dx$$

### 5.2 Signed Area

When $f(x)$ takes both positive and negative values, the definite integral gives **signed area**:
- Regions above the $x$-axis contribute **positive** area
- Regions below the $x$-axis contribute **negative** area

![Signed Area Illustration](images/signed_area.svg "The definite integral computes signed area - positive above the x-axis, negative below")

**Example 7.5:** Consider $f(x) = x^2 - 2x$ on $[0, 3]$

First, find where $f(x) = 0$: $x(x-2) = 0 \Rightarrow x = 0$ or $x = 2$

The function is negative on $(0, 2)$ and positive on $(2, 3)$.

**Signed area (net area):**
$$\int_0^3 (x^2 - 2x)\,dx = \left[\frac{x^3}{3} - x^2\right]_0^3 = \left(\frac{27}{3} - 9\right) - 0 = 9 - 9 = 0$$

**Total (unsigned) area:**
$$\text{Total Area} = \left|\int_0^2 (x^2 - 2x)\,dx\right| + \int_2^3 (x^2 - 2x)\,dx$$

$$= \left|\frac{8}{3} - 4\right| + \left(9 - 9 - \frac{8}{3} + 4\right) = \frac{4}{3} + \frac{4}{3} = \frac{8}{3}$$

> **📓 Try it in Python**
>
> - **W7-CS03** — *Visualizing Area Under a Curve*: Plot a function and shade the region under it.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 6. Area Between Two Curves

### General Formula

If $f(x) \geq g(x)$ on $[a, b]$, the area between the curves is:

$$\text{Area} = \int_a^b [f(x) - g(x)]\,dx = \int_a^b (\text{upper} - \text{lower})\,dx$$

![Area Between Curves](images/area_between_curves.svg "Computing area between two curves: integrate the difference of upper minus lower function")

### Finding Intersection Points

Before integrating, solve $f(x) = g(x)$ to find where curves intersect.

### Example 7.6: Degraded Land Area Calculation

A degraded land patch has boundaries described by:
- Lower boundary: $y = e^{0.0471x}$
- Upper boundary: $y = -19.96 + 2.999x - 0.02x^2$

The boundaries intersect approximately at $x = 7.4$ and $x = 94.5$ (kilometers).

**Area Calculation:**
$$\text{Area} = \int_{7.4}^{94.5} \left[(-19.96 + 2.999x - 0.02x^2) - e^{0.0471x}\right]\,dx$$

This integral can be evaluated using SymPy (see code snippets):

$$\text{Area} \approx 4,560 \text{ km}^2$$

**Scientific Context:** Such calculations are essential for:
- Estimating rehabilitation costs
- Planning vegetation coverage
- Assessing soil loss extent

> **📓 Try it in Python**
>
> - **W7-CS04** — *Area Between Two Curves*: Calculate and visualize area between two curves.
> - **W7-CS10** — *Degraded Land Example*: Compute the area of a degraded land region bounded by two curves.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 7. Average Value of a Function

### Definition

The **average value** of $f(x)$ over $[a, b]$ is:

$$\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

**Interpretation:** This is the height of a rectangle with width $(b-a)$ that has the same area as the region under $f(x)$.

### Example 7.7: Average Pollution Level

Pollution concentration follows $C(t) = 50e^{-0.1t}$ (ppm) over the first 10 hours.

$$\bar{C} = \frac{1}{10-0}\int_0^{10} 50e^{-0.1t}\,dt = \frac{1}{10}\left[\frac{50}{-0.1}e^{-0.1t}\right]_0^{10}$$

$$= \frac{1}{10}\left[-500e^{-1} + 500e^0\right] = \frac{1}{10}\left[500 - 500(0.3679)\right]$$

$$= \frac{1}{10}(500 - 183.9) = 31.6 \text{ ppm}$$

> **📓 Try it in Python**
>
> - **W7-CS09** — *Average Value of a Function*: Calculate and visualize the average value of a function.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 8. Series: The Discrete Analogue of Integration

Just as integration sums infinitely many infinitesimally small pieces, **series** sum discrete terms. Understanding series helps appreciate how integration works and connects to important applications.

### 8.1 Arithmetic Sequences and Series

**Arithmetic Sequence:** Each term differs from the previous by a constant **common difference** $d$:

$$a_n = a_1 + (n-1)d$$

where:
- $a_1$ = first term
- $d$ = common difference
- $a_n$ = $n$th term

**Examples:**
- $2, 5, 8, 11, 14, \ldots$ (first term $a_1 = 2$, common difference $d = 3$)
- $100, 95, 90, 85, \ldots$ (first term $a_1 = 100$, common difference $d = -5$)

**Arithmetic Series (Sum):**

$$S_n = \sum_{i=1}^{n} a_i = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$$

**Derivation:**
Write the sum forwards and backwards:
$$S_n = a_1 + (a_1+d) + (a_1+2d) + \cdots + a_n$$
$$S_n = a_n + (a_n-d) + (a_n-2d) + \cdots + a_1$$

Adding: $2S_n = n(a_1 + a_n)$, so $S_n = \frac{n}{2}(a_1 + a_n)$

### Example 7.8: Food Production Growth

A country's food production capacity (in millions of people fed) starts at 100 and increases by 5 million per year (arithmetic growth).

$$a_n = 100 + 5(n-1) = 95 + 5n$$

After 20 years: $a_{20} = 95 + 5(20) = 195$ million

Total food produced in first 20 years:
$$S_{20} = \frac{20}{2}(100 + 195) = 10 \times 295 = 2950 \text{ million-years}$$

### Example 7.9: Counting Terms in a Range

Consider the sequence $a_i = 3 + 5(i-1)$ for $i = 1, 2, 3, \ldots$

How many terms are **greater than or equal to 10** and **less than or equal to 150**?

**Solution:**

Step 1: Simplify the formula: $a_i = 3 + 5i - 5 = 5i - 2$

Step 2: Find smallest $i$ where $a_i \geq 10$:
$$5i - 2 \geq 10 \Rightarrow 5i \geq 12 \Rightarrow i \geq 2.4$$
So $i_{\min} = 3$ (smallest integer $\geq 2.4$)

Step 3: Find largest $i$ where $a_i \leq 150$:
$$5i - 2 \leq 150 \Rightarrow 5i \leq 152 \Rightarrow i \leq 30.4$$
So $i_{\max} = 30$

Step 4: Count: $30 - 3 + 1 = \boxed{28}$ terms

### 8.2 Geometric Sequences and Series

**Geometric Sequence:** Each term is multiplied by a constant **common ratio** $r$:

$$a_n = a_1 \cdot r^{n-1}$$

**Definition:** A geometric sequence is a sequence of numbers with a **common ratio between two consecutive numbers**.

**Examples:**
- $2, 6, 18, 54, \ldots$ (first term $a_1 = 2$, common ratio $r = 3$)
- $100, 50, 25, 12.5, \ldots$ (first term $a_1 = 100$, common ratio $r = 0.5$)

**Geometric Series (Sum):**

$$S_n = a_1 \cdot \frac{1 - r^n}{1 - r}, \quad r \neq 1$$

**Derivation:**
$$S_n = a_1 + a_1 r + a_1 r^2 + \cdots + a_1 r^{n-1}$$
$$rS_n = a_1 r + a_1 r^2 + \cdots + a_1 r^n$$
Subtracting: $S_n - rS_n = a_1 - a_1 r^n$, giving $S_n = a_1 \frac{1-r^n}{1-r}$

**Sum to Infinity (when $|r| < 1$):**

$$S_\infty = \lim_{n \to \infty} S_n = \frac{a_1}{1-r}$$

### Example 7.10: Population Growth

A country's population starts at 100 million and grows at 3% per year (geometric growth):

$$P_n = 100 \times 1.03^{n-1}$$

After 20 years: $P_{20} = 100 \times 1.03^{19} \approx 175.4$ million

> **📓 Try it in Python**
>
> - **W7-CS05** — *Arithmetic Sequence Generator*: Generate arithmetic sequences in Python.
> - **W7-CS06** — *Geometric Sequence Generator*: Generate geometric sequences and compute their sums.
> - **W7-CS07** — *Counting Terms in a Range*: Find how many terms of a sequence fall within a given range.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 9. The Malthusian Trap: Arithmetic vs. Geometric Growth

### 9.1 Malthus's Key Insight

Thomas Robert Malthus (1798) observed:
- **Food production** grows **arithmetically** (linearly): $F_n = F_1 + (n-1)d$
- **Population** grows **geometrically** (exponentially): $P_n = P_1 \cdot r^{n-1}$

Since geometric growth eventually outpaces arithmetic growth, population will inevitably exceed food supply—the **Malthusian Crisis**.

### 9.2 Numerical Example

| Year | Food Capacity (million) | Population (million) |
| ---- | ----------------------- | -------------------- |
| 1    | 100                     | 100                  |
| 10   | 145                     | 130.5                |
| 20   | 195                     | 175.4                |
| 50   | 345                     | 381.6                |
| 71   | 450                     | 810.0                |

At year 71, population exceeds food capacity → **Malthusian Crisis**

### 9.3 Modern Perspective

Malthus didn't foresee:
- Agricultural technology and the Green Revolution
- Demographic transition (declining birth rates with development)
- Hence, many parts of the world escaped the "trap"

However, the mathematical relationship between arithmetic and geometric growth remains fundamentally important for understanding sustainability limits.

> **📓 Try it in Python**
>
> - **W7-CS08** — *Malthusian Trap Simulation*: Simulate and visualize the Malthusian crisis point.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 10. Consumer and Producer Surplus

Integration has a powerful application in economics: measuring the **welfare** that buyers and sellers gain from a competitive market.

### 10.1 Market Equilibrium

In a free market, price adjusts until the quantity demanded equals the quantity supplied. This is the **equilibrium price** $P^*$ and **equilibrium quantity** $Q^*$.

**Key insight:** Not every consumer values the good at exactly $P^*$. Some would have been willing to pay *more* — they get a bargain. Similarly, some producers could supply at a cost *below* $P^*$ — they earn a bonus. Integration measures these gains precisely.

### 10.2 Consumer Surplus (CS)

The **inverse demand function** $D(Q)$ gives the maximum price consumers are willing to pay for the $Q$-th unit. Consumer surplus is the total excess value consumers receive:

$$\text{CS} = \int_0^{Q^*} D(Q)\,dQ - P^* \cdot Q^*$$

**Geometric meaning:** Area between the demand curve and the horizontal line at $P^*$, from $Q = 0$ to $Q = Q^*$.

### 10.3 Producer Surplus (PS)

The **inverse supply function** $S(Q)$ gives the minimum price producers need to supply the $Q$-th unit. Producer surplus is the total excess revenue producers receive:

$$\text{PS} = P^* \cdot Q^* - \int_0^{Q^*} S(Q)\,dQ$$

**Geometric meaning:** Area between the horizontal line at $P^*$ and the supply curve, from $Q = 0$ to $Q = Q^*$.

### Example 7.11: Computing CS and PS

**Market:** Demand $P = 50 - Q$, Supply $P = 10 + Q$

**Step 1 — Find equilibrium:**
$$50 - Q = 10 + Q \Rightarrow 40 = 2Q \Rightarrow Q^* = 20,\quad P^* = 30$$

**Step 2 — Consumer Surplus:**
$$\text{CS} = \int_0^{20} (50 - Q)\,dQ - 30 \times 20$$
$$= \left[50Q - \frac{Q^2}{2}\right]_0^{20} - 600 = (1000 - 200) - 600 = \boxed{200}$$

**Step 3 — Producer Surplus:**
$$\text{PS} = 30 \times 20 - \int_0^{20} (10 + Q)\,dQ$$
$$= 600 - \left[10Q + \frac{Q^2}{2}\right]_0^{20} = 600 - (200 + 200) = \boxed{200}$$

**Total welfare (social surplus):** $\text{CS} + \text{PS} = 400$

**Interpretation:** The competitive market generates \$400 of total economic benefit — shared equally between buyers and sellers in this symmetric case.

### 10.4 Deadweight Loss (DWL)

When a market is distorted — by a price ceiling, tax, or monopoly — some mutually beneficial transactions no longer occur. The lost welfare is called **deadweight loss (DWL)**.

**Price ceiling example:** The government imposes a maximum price of $P_c = 25$ on the market above.

At $P_c = 25$:
- Quantity demanded: $Q_d = 50 - 25 = 25$
- Quantity supplied: $Q_s = 25 - 10 = 15$
- Quantity actually traded: $Q_c = \min(25, 15) = 15$ (supply-constrained)

The transactions from $Q = 15$ to $Q = 20$ are lost. At $Q = 15$:
- Demand price: $D(15) = 50 - 15 = 35$ (consumers still willing to pay \$35)
- Supply price: $S(15) = 10 + 15 = 25$ (producers still willing to sell for \$25)

These transactions would benefit both parties by \$10 each, but they don't happen.

$$\text{DWL} = \frac{1}{2}(Q^* - Q_c)(D(Q_c) - S(Q_c)) = \frac{1}{2}(20-15)(35-25) = \frac{1}{2}(5)(10) = \boxed{25}$$

**Visualisation:** DWL is the area of the triangle between the supply and demand curves, over the range of foregone transactions $[Q_c, Q^*]$.

![Consumer Producer Surplus](images/consumer_producer_surplus.svg "Consumer and producer surplus as areas between market price and supply/demand curves")

> **📓 Try it in Python**
>
> - **W7-CS11** — *Consumer and Producer Surplus Preview*: Visualize and set up CS/PS calculations (full calculation in Week 12).
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 11. Riemann Sums: Connecting Series to Integrals

### 11.1 The Big Picture

The definite integral is defined as the limit of **Riemann sums**—discrete approximations using rectangles.

### 11.2 Left Riemann Sum

Divide $[a, b]$ into $n$ equal subintervals of width $\Delta x = \frac{b-a}{n}$.

$$L_n = \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

where $x_i = a + i \cdot \Delta x$

### 11.3 As $n \to \infty$

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

**Key Insight:** Series (discrete sums) → Integrals (continuous sums) as the number of terms approaches infinity and term size approaches zero.

> **📓 Try it in Python**
>
> - **W7-CS12** — *Riemann Sum Visualization*: Watch how Riemann sums approximate the definite integral.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 12. Summary: Key Formulas

| Concept                   | Formula                                                |
| ------------------------- | ------------------------------------------------------ |
| Definite Integral (FTC)   | $\int_a^b f(x)\,dx = F(b) - F(a)$ where $F'(x) = f(x)$ |
| Area under curve          | $\text{Area} = \int_a^b f(x)\,dx$ when $f(x) \geq 0$   |
| Area between curves       | $\text{Area} = \int_a^b [f(x) - g(x)]\,dx$             |
| Average value             | $\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx$             |
| Arithmetic sequence       | $a_n = a_1 + (n-1)d$                                   |
| Arithmetic series         | $S_n = \frac{n}{2}(a_1 + a_n)$                         |
| Geometric sequence        | $a_n = a_1 \cdot r^{n-1}$                              |
| Geometric series          | $S_n = a_1 \frac{1-r^n}{1-r}$                          |
| Infinite geometric series | $S_\infty = \frac{a_1}{1-r}$ for $                     | r | < 1$ |

---
