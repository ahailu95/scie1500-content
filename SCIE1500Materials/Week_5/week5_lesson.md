# Week 5: Differentiation Techniques and Optimization

## Act I: Understanding Systems — Chapter 5

> *"The analytical scientist doesn't just measure change—they find the best possible outcome. Optimization is the capstone of calculus."*

---

## Theme: "Differentiation Techniques and Optimisation"

**Science Context:** Maximum Economic Yield in fisheries, agricultural profit optimisation, drug dosage modelling

**Learning Outcomes:** At the end of this week you should be able to:

1. Apply the product rule and quotient rule to differentiate products and quotients
2. Apply the chain rule to differentiate composite functions
3. Differentiate exponential and logarithmic functions
4. Find critical points by setting the derivative equal to zero
5. Classify critical points as local maxima or minima using the second derivative test
6. Solve optimisation problems in scientific and economic contexts
7. Interpret Maximum Economic Yield (MEY) as an optimisation of a profit function

**Exam Alignment:** Q28, Q38

---

## 1. The Challenge: Finding the Best Outcome

### Why Optimization Matters

In Week 4, you learned to compute derivatives—the instantaneous rate of change of a function. Now we ask a deeper question: **At what point does a system achieve its best possible value?**

Consider these scientific and economic decisions:

| Domain | Question | Optimization Goal |
|--------|----------|-------------------|
| Fisheries | What stock level maximizes long-term profit? | Maximum Economic Yield (MEY) |
| Agriculture | How much fertilizer maximizes net revenue? | Profit maximization |
| Medicine | What drug dosage maximizes therapeutic effect? | Optimal dose |
| Engineering | What dimensions minimize material cost? | Cost minimization |
| Livestock | When should animals be sold to maximize profit? | Optimal timing |

These problems share a common structure: find the input value $x^*$ that maximizes (or minimizes) an objective function $f(x)$. The derivative is our key tool—**at a maximum or minimum, the derivative equals zero**.

### From MSY to MEY: The Economic Lens

In Week 3, you found the Maximum Sustainable Yield (MSY) for the Schaefer model:

$$G(S) = gS\left(1 - \frac{S}{K}\right), \quad S_{MSY} = \frac{K}{2}$$

But MSY ignores **cost**. Harvesting fish at low stock levels requires more effort (and thus more cost) than at high stock levels. The **Maximum Economic Yield (MEY)** strategy accounts for this:

$$\text{Profit}(S) = \text{Revenue}(S) - \text{Cost}(S)$$

Finding MEY requires derivatives of more complex expressions—products, quotients, and compositions—which we develop this week.

---

## 2. Advanced Differentiation Rules

Week 4 covered the power rule, sum rule, and constant multiple rule. Now we extend our toolkit to handle products, quotients, and compositions of functions.

### 2.1 The Product Rule

**Theorem:** If $f(x)$ and $g(x)$ are differentiable, then:

$$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$

**Memory aid:** "First times derivative of second, plus second times derivative of first."

**Example 5.1:** Differentiate $y = x^2 \cdot e^x$.

*Solution:* Let $f(x) = x^2$ and $g(x) = e^x$.

$$y' = (2x)(e^x) + (x^2)(e^x) = e^x(2x + x^2) = x e^x(2 + x)$$

**Example 5.2:** Differentiate $y = (3x + 1)(x^2 - 4)$.

*Solution:*
$$y' = (3)(x^2 - 4) + (3x + 1)(2x) = 3x^2 - 12 + 6x^2 + 2x = 9x^2 + 2x - 12$$

*Verification by expansion:* $y = 3x^3 - 12x + x^2 - 4 = 3x^3 + x^2 - 12x - 4$
$$y' = 9x^2 + 2x - 12 \checkmark$$

---

### 2.2 The Quotient Rule

**Theorem:** If $f(x)$ and $g(x)$ are differentiable with $g(x) \neq 0$:

$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$

**Memory aid:** "Low d-high minus high d-low, over low squared."

**Example 5.3:** Differentiate $y = \frac{x^2 + 1}{x - 3}$.

*Solution:*
$$y' = \frac{(2x)(x - 3) - (x^2 + 1)(1)}{(x - 3)^2} = \frac{2x^2 - 6x - x^2 - 1}{(x - 3)^2} = \frac{x^2 - 6x - 1}{(x - 3)^2}$$

**Example 5.4:** Differentiate $y = \frac{e^x}{x^2}$.

*Solution:*
$$y' = \frac{(e^x)(x^2) - (e^x)(2x)}{x^4} = \frac{e^x(x^2 - 2x)}{x^4} = \frac{e^x(x - 2)}{x^3}$$

---

### 2.3 The Chain Rule

The chain rule handles **composite functions**—functions of functions.

**Theorem:** If $y = f(g(x))$, then:

$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$$

**Leibniz notation:** If $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

**Memory aid:** "Derivative of outer (evaluated at inner) times derivative of inner."

![The Chain Rule Visualized](images/chain_rule.svg "Three-panel diagram showing inner function g(x)=x², outer function f(u)=√u, and composite h(x)=f(g(x)) with derivatives at x=1")

**Example 5.5:** Differentiate $y = (2x + 3)^5$.

*Solution:* Let $u = 2x + 3$, so $y = u^5$.
- Outer: $\frac{dy}{du} = 5u^4$
- Inner: $\frac{du}{dx} = 2$
- Chain rule: $\frac{dy}{dx} = 5u^4 \cdot 2 = 10(2x + 3)^4$

**Example 5.6:** Differentiate $y = e^{3x^2 - x}$.

*Solution:* Let $u = 3x^2 - x$, so $y = e^u$.
- Outer: $\frac{dy}{du} = e^u$
- Inner: $\frac{du}{dx} = 6x - 1$
- Chain rule: $\frac{dy}{dx} = e^{3x^2 - x}(6x - 1)$

**Example 5.7:** Differentiate $y = \ln(x^2 + 1)$.

*Solution:* Let $u = x^2 + 1$, so $y = \ln(u)$.
- Outer: $\frac{dy}{du} = \frac{1}{u}$
- Inner: $\frac{du}{dx} = 2x$
- Chain rule: $\frac{dy}{dx} = \frac{1}{x^2 + 1} \cdot 2x = \frac{2x}{x^2 + 1}$

---

## 3. Derivatives of Exponential and Logarithmic Functions

### 3.1 Revisiting Euler's Number: The Calculus Connection

In Week 2, we introduced Euler's number $e \approx 2.718$ through two approaches:
1. **Compound interest:** $e = \lim_{n \to \infty}(1 + 1/n)^n$
2. **Slope property:** The function $e^x$ has slope equal to height at every point

Now, with derivatives, we can state the slope property precisely and prove it.

#### The Week 2 Discovery (Informal)

Recall that we computed slopes numerically:

| Point $x$ | Height $e^x$ | Slope at that point |
|-----------|--------------|---------------------|
| 0 | 1.000 | ≈ 1.000 |
| 1 | 2.718 | ≈ 2.718 |
| 2 | 7.389 | ≈ 7.389 |

The slope always equaled the height!

#### The Week 5 Statement (Formal)

Using derivative notation, this property becomes:

$$\boxed{\frac{d}{dx}[e^x] = e^x}$$

**The function $e^x$ is its own derivative.** This is the only function (up to constant multiples) with this remarkable property.

### 3.2 Proving That $\frac{d}{dx}[e^x] = e^x$

Let's derive this result from first principles using the limit definition of the derivative.

**Step 1: Write the definition**

$$\frac{d}{dx}[e^x] = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h}$$

**Step 2: Use exponential laws**

Using $e^{x+h} = e^x \cdot e^h$:

$$= \lim_{h \to 0} \frac{e^x \cdot e^h - e^x}{h} = \lim_{h \to 0} \frac{e^x(e^h - 1)}{h}$$

**Step 3: Factor out $e^x$**

Since $e^x$ doesn't depend on $h$, it can come outside the limit:

$$= e^x \cdot \lim_{h \to 0} \frac{e^h - 1}{h}$$

**Step 4: Evaluate the key limit**

The crucial question is: what is $\lim_{h \to 0} \frac{e^h - 1}{h}$?

| $h$ | $\frac{e^h - 1}{h}$ |
|-----|---------------------|
| 0.1 | 1.0517 |
| 0.01 | 1.0050 |
| 0.001 | 1.0005 |
| 0.0001 | 1.00005 |

The limit is exactly **1**:

$$\lim_{h \to 0} \frac{e^h - 1}{h} = 1$$

**Step 5: Conclude**

$$\frac{d}{dx}[e^x] = e^x \cdot 1 = e^x \quad \blacksquare$$

### 3.3 Why $e$ Is the Only Base with This Property

What happens if we try a different base, say $a^x$ where $a \neq e$?

**Derivative of $a^x$:**

$$\frac{d}{dx}[a^x] = \lim_{h \to 0} \frac{a^{x+h} - a^x}{h} = a^x \cdot \lim_{h \to 0} \frac{a^h - 1}{h}$$

The question is: what is $\lim_{h \to 0} \frac{a^h - 1}{h}$ for different bases?

| Base $a$ | $\lim_{h \to 0} \frac{a^h - 1}{h}$ | Derivative of $a^x$ |
|----------|-----------------------------------|---------------------|
| $a = 2$ | 0.693 | $0.693 \cdot 2^x$ |
| $a = e$ | 1.000 | $1 \cdot e^x = e^x$ |
| $a = 3$ | 1.099 | $1.099 \cdot 3^x$ |
| $a = 10$ | 2.303 | $2.303 \cdot 10^x$ |

It turns out that $\lim_{h \to 0} \frac{a^h - 1}{h} = \ln(a)$. This gives us the general formula:

$$\boxed{\frac{d}{dx}[a^x] = a^x \cdot \ln(a)}$$

**Why $e$ is special:** Since $\ln(e) = 1$, the derivative of $e^x$ is simply $e^x$—no extra constant factor. This is why $e$ is called the **natural base** for exponential functions.

### 3.4 Python: Visualizing the Derivative of $e^x$

```python
import numpy as np
import matplotlib.pyplot as plt

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: e^x and its derivative (they're the same!)
x = np.linspace(-1, 2, 200)
y = np.exp(x)

ax1.plot(x, y, 'b-', linewidth=2.5, label='$f(x) = e^x$')
ax1.plot(x, y, 'r--', linewidth=2, label="$f'(x) = e^x$ (same curve!)")

# Show tangent lines at a few points
for x0 in [0, 1]:
    y0 = np.exp(x0)
    slope = y0  # slope = e^x = height
    x_tan = np.linspace(x0 - 0.5, x0 + 0.5, 50)
    y_tan = y0 + slope * (x_tan - x0)
    ax1.plot(x_tan, y_tan, 'g-', linewidth=1.5, alpha=0.7)
    ax1.plot(x0, y0, 'go', markersize=10)
    ax1.annotate(f'slope = height = {y0:.2f}', xy=(x0, y0), 
                 xytext=(x0 + 0.3, y0 + 0.5), fontsize=10)

ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('$e^x$ is its own derivative!', fontsize=13, fontweight='bold')
ax1.legend(loc='upper left', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-1, 2.5)
ax1.set_ylim(0, 8)

# Right plot: Compare derivatives of different exponential bases
x = np.linspace(0, 2, 100)

for base, color, name in [(2, 'blue', '2'), (np.e, 'green', 'e'), (3, 'orange', '3')]:
    y = base**x
    dy = y * np.log(base)  # derivative = a^x * ln(a)
    ax2.plot(x, y, color=color, linewidth=2, linestyle='-', label=f'${name}^x$')
    ax2.plot(x, dy, color=color, linewidth=2, linestyle='--', label=f"d/dx[${name}^x$]")

ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('Comparing $a^x$ (solid) vs its derivative (dashed)', fontsize=13, fontweight='bold')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)

# Add annotation
ax2.annotate('Only for base e:\nfunction = derivative', xy=(1.5, np.e**1.5), 
             xytext=(1.8, 3), fontsize=10, color='green',
             arrowprops=dict(arrowstyle='->', color='green'))

plt.tight_layout()
plt.show()
```

### 3.5 Summary: Why $e$ Matters in Calculus

| Property | Mathematical Statement | Significance |
|----------|------------------------|--------------|
| Compound interest limit | $e = \lim_{n \to \infty}(1 + 1/n)^n$ | Natural limit of continuous growth |
| Self-derivative | $\frac{d}{dx}[e^x] = e^x$ | Simplifies all calculus with exponentials |
| Unit slope at origin | $\lim_{h \to 0}\frac{e^h - 1}{h} = 1$ | Why $e$ is the "natural" base |
| General exponential | $\frac{d}{dx}[a^x] = a^x \ln(a)$ | All other bases need a correction factor |

The number $e$ isn't just a mathematical curiosity—it's the **natural base for calculus**. Whenever you model growth or decay, using base $e$ makes the mathematics cleaner.

### 3.6 Exponential Function Rules

Using the chain rule, we can extend to more general exponential functions:

| Function | Derivative |
|----------|------------|
| $e^x$ | $e^x$ |
| $e^{kx}$ | $k \cdot e^{kx}$ |
| $e^{g(x)}$ | $g'(x) \cdot e^{g(x)}$ |
| $a^x$ | $a^x \cdot \ln(a)$ |

**Example 5.8:** Differentiate $y = 5e^{-0.2x}$.

*Solution:* Using $\frac{d}{dx}[e^{kx}] = ke^{kx}$ with $k = -0.2$:
$$y' = 5 \cdot (-0.2) \cdot e^{-0.2x} = -e^{-0.2x}$$

**Example 5.8b:** Differentiate $y = 3 \cdot 2^x$.

*Solution:* Using $\frac{d}{dx}[a^x] = a^x \ln(a)$:
$$y' = 3 \cdot 2^x \cdot \ln(2) \approx 3 \cdot 2^x \cdot 0.693 = 2.079 \cdot 2^x$$

### 3.7 The Natural Logarithm Function

The derivative of $\ln(x)$ is elegantly simple:

$$\boxed{\frac{d}{dx}[\ln(x)] = \frac{1}{x}}$$

**Proof sketch:** Since $\ln(x)$ and $e^x$ are inverses, we use implicit differentiation. If $y = \ln(x)$, then $e^y = x$. Differentiating both sides:
$$e^y \cdot \frac{dy}{dx} = 1$$
$$\frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}$$

Combined with the chain rule:

$$\frac{d}{dx}[\ln(g(x))] = \frac{g'(x)}{g(x)}$$

**Example 5.9:** Differentiate $y = \ln(3x^2 + 2)$.

*Solution:* $y' = \frac{6x}{3x^2 + 2}$

**Example 5.10 (Exam Q28 style):** Differentiate $y = \frac{3}{4}x^4 + \frac{1}{4}x^2 - 3x + \ln(x)$.

*Solution:*
$$y' = \frac{3}{4}(4x^3) + \frac{1}{4}(2x) - 3 + \frac{1}{x} = 3x^3 + \frac{1}{2}x - 3 + \frac{1}{x}$$

---

## 4. Optimization: Finding Maxima and Minima

### 4.1 The Core Principle

**At a local maximum or minimum, the derivative equals zero.** These points are called **critical points** or **stationary points**.

**Algorithm for Optimization:**
1. Find the derivative $f'(x)$
2. Solve $f'(x) = 0$ for critical points $x^*$
3. Use the second derivative test to classify each critical point
4. Evaluate $f(x^*)$ to find the optimal value

### 4.2 The Second Derivative Test

If $f'(x_0) = 0$:

| Second Derivative | Conclusion | Graph Shape |
|-------------------|------------|-------------|
| $f''(x_0) > 0$ | Local **minimum** at $x_0$ | Concave up (∪) |
| $f''(x_0) < 0$ | Local **maximum** at $x_0$ | Concave down (∩) |
| $f''(x_0) = 0$ | **Inconclusive** (may be inflection point) | Test further |

![Finding Local Extrema](images/optimization.svg "Critical points and the first derivative test for f(x) = x³ - 6x² + 9x + 1, showing local maximum at (1, 5) and local minimum at (3, 1)")

**Example 5.11:** Find all local extrema of $y = x^3 - 6x^2 + 9x + 1$.

*Solution:*

**Step 1:** Find derivative.
$$y' = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3)$$

**Step 2:** Solve $y' = 0$.
$$x = 1 \quad \text{or} \quad x = 3$$

**Step 3:** Second derivative test.
$$y'' = 6x - 12$$
- At $x = 1$: $y''(1) = 6 - 12 = -6 < 0$ → **local maximum**
- At $x = 3$: $y''(3) = 18 - 12 = 6 > 0$ → **local minimum**

**Step 4:** Find optimal values.
- $y(1) = 1 - 6 + 9 + 1 = 5$ (local max)
- $y(3) = 27 - 54 + 27 + 1 = 1$ (local min)

---

### 4.3 Constrained Optimization

Many real problems involve **constraints**. The method is:
1. Write the **objective function** (what to optimize)
2. Write the **constraint equation**
3. Use the constraint to eliminate one variable
4. Optimize the resulting single-variable function

**Example 5.12 (Classic Fencing Problem):** A farmer has 1000 m of fencing to enclose a rectangular paddock along a river (no fencing needed on the river side). What dimensions maximize the enclosed area?

*Solution:*

Let $x$ = width (perpendicular to river), $y$ = length (parallel to river).

**Objective:** Maximize $A = xy$

**Constraint:** $2x + y = 1000$ (three sides of fencing)

**Eliminate $y$:** $y = 1000 - 2x$

**Substitute:** $A(x) = x(1000 - 2x) = 1000x - 2x^2$

**Optimize:**
$$A'(x) = 1000 - 4x = 0 \implies x = 250$$

$$A''(x) = -4 < 0 \implies \text{maximum}$$

**Solution:** $x = 250$ m, $y = 1000 - 500 = 500$ m

**Maximum area:** $A = 250 \times 500 = 125,000$ m²

---

## 5. Economic Optimization: The Bioeconomic Fishery Model

### 5.1 Model Components

The bioeconomic model integrates biology, technology, and economics:

**Biology (Schaefer growth):**
$$G(S) = gS\left(1 - \frac{S}{K}\right)$$

**Technology (harvest production):**
$$H = e \cdot E \cdot S \quad \Rightarrow \quad E = \frac{H}{eS}$$

where $e$ = catchability coefficient, $E$ = fishing effort.

**Economics:**
- Total Revenue: $TR = p \cdot H$ (price × harvest)
- Total Cost: $TC = c \cdot E$ (cost per unit effort × effort)
- Profit: $\pi = TR - TC$

### 5.2 Finding MEY: The Profit Maximization Problem

At steady state, harvest equals growth: $H = G(S)$.

**Revenue:**
$$TR(S) = p \cdot G(S) = p \cdot gS\left(1 - \frac{S}{K}\right)$$

**Effort required:**
$$E(S) = \frac{G(S)}{eS} = \frac{g(1 - S/K)}{e}$$

**Cost:**
$$TC(S) = c \cdot E(S) = \frac{cg}{e}\left(1 - \frac{S}{K}\right)$$

**Profit:**
$$\pi(S) = TR(S) - TC(S) = pgS\left(1 - \frac{S}{K}\right) - \frac{cg}{e}\left(1 - \frac{S}{K}\right)$$

Factor out common terms:
$$\pi(S) = g\left(1 - \frac{S}{K}\right)\left(pS - \frac{c}{e}\right)$$

### 5.3 Numerical Example: MEY Calculation

**Parameters:** $K = 12000$, $g = 0.10$, $e = 0.001$, $c = 4500$, $p = 3000$

**Profit function:**
$$\pi(S) = 0.10\left(1 - \frac{S}{12000}\right)\left(3000S - \frac{4500}{0.001}\right)$$
$$\pi(S) = 0.10\left(1 - \frac{S}{12000}\right)(3000S - 4500000)$$

**Expand:**
$$\pi(S) = 300S - 450000 - \frac{300S^2}{12000} + \frac{450000S}{12000}$$
$$\pi(S) = 300S - 450000 - 0.025S^2 + 37.5S$$
$$\pi(S) = -0.025S^2 + 337.5S - 450000$$

**Optimize:**
$$\pi'(S) = -0.05S + 337.5 = 0$$
$$S^* = \frac{337.5}{0.05} = 6750 \text{ tonnes}$$

**Verify maximum:**
$$\pi''(S) = -0.05 < 0 \checkmark$$

**Compare MSY vs MEY:**

| Strategy | Stock Level | Harvest | Profit |
|----------|-------------|---------|--------|
| MSY | $K/2 = 6000$ tonnes | 300 tonnes | $\$639,000$ |
| MEY | 6750 tonnes | 296.7 tonnes | $\$689,062$ |

**Key insight:** MEY maintains a **higher stock** than MSY, which reduces fishing cost and increases profit despite slightly lower harvest.

---

## 6. Application: Profit Maximization Word Problems (Exam Q38)

### 6.1 The Structure of Optimization Word Problems

Many exam problems follow this pattern:
1. **Read carefully** to identify the variable and time frame
2. **Build the objective function** (often profit = revenue − cost)
3. **Set up component functions** (revenue depends on price and quantity; cost depends on time or quantity)
4. **Differentiate and solve** $\frac{d\pi}{dt} = 0$
5. **Interpret** the result in context

### 6.2 Worked Example: Livestock Fattening (Exam Q38 Style)

**Problem:** A farmer is fattening 100 deer for sale. The deer currently weigh 50 kg each and gain weight according to:
- Current gain rate: 2 kg/day
- Rate decline: 0.1 kg/day per day into the future

Feed and operating costs are \$0.50 per animal per day. Market price is \$5.00 per kg. When should the farmer sell to maximize profit?

**Solution:**

**Step 1: Model the weight gain**

Let $t$ = days from now. Daily weight gain at time $t$:
$$\frac{dW}{dt} = 2 - 0.1t \text{ kg/day}$$

Total weight gained over $t$ days:
$$\Delta W = \int_0^t (2 - 0.1\tau) d\tau = 2t - 0.05t^2$$

Weight per deer at time $t$:
$$W(t) = 50 + 2t - 0.05t^2$$

**Step 2: Build the profit function**

Total Revenue (100 deer at \$5/kg):
$$TR(t) = 100 \times 5 \times W(t) = 500(50 + 2t - 0.05t^2)$$
$$TR(t) = 25000 + 1000t - 25t^2$$

Total Cost (\$0.50 × 100 deer × $t$ days):
$$TC(t) = 0.50 \times 100 \times t = 50t$$

Profit:
$$\pi(t) = TR(t) - TC(t) = 25000 + 1000t - 25t^2 - 50t$$
$$\pi(t) = 25000 + 950t - 25t^2$$

**Step 3: Optimize**

$$\pi'(t) = 950 - 50t = 0$$
$$t^* = 19 \text{ days}$$

**Step 4: Verify maximum**
$$\pi''(t) = -50 < 0 \checkmark$$

**Step 5: Calculate optimal values**

- Optimal time: **19 days**
- Weight per deer: $W(19) = 50 + 38 - 18.05 = 69.95$ kg
- Revenue: $TR(19) = 500 \times 69.95 = \$34,975$
- Cost: $TC(19) = 50 \times 19 = \$950$
- **Maximum profit:** $\pi(19) = 34,975 - 950 = \$34,025$

---

## 7. Symbolic Computation with SymPy

SymPy allows us to perform calculus symbolically—exactly as you would by hand, but with computer assistance.

### 7.1 Basic SymPy Setup

```python
import sympy as sp

# Define symbols
x, t, S = sp.symbols('x t S')

# Define parameters
g, K, e, c, p = sp.symbols('g K e c p', positive=True)
```

### 7.2 Differentiation with SymPy

```python
# Define a function
f = x**3 - 6*x**2 + 9*x + 1

# First derivative
f_prime = f.diff(x)
print(f"f'(x) = {f_prime}")  # Output: 3*x**2 - 12*x + 9

# Second derivative
f_double_prime = f.diff(x, 2)
print(f"f''(x) = {f_double_prime}")  # Output: 6*x - 12

# Evaluate at a point
f_prime_at_2 = f_prime.subs(x, 2)
print(f"f'(2) = {f_prime_at_2}")  # Output: -3
```

### 7.3 Solving Equations

```python
# Find critical points: solve f'(x) = 0
critical_points = sp.solve(f_prime, x)
print(f"Critical points: {critical_points}")  # Output: [1, 3]

# Evaluate function at critical points
for cp in critical_points:
    value = f.subs(x, cp)
    second_deriv = f_double_prime.subs(x, cp)
    nature = "maximum" if second_deriv < 0 else "minimum"
    print(f"At x = {cp}: f(x) = {value}, f''(x) = {second_deriv} → {nature}")
```

### 7.4 Bioeconomic Model with SymPy

```python
# Define parameters numerically
params = {g: 0.10, K: 12000, e: 0.001, c: 4500, p: 3000}

# Growth function
Growth = g * S * (1 - S/K)

# Profit function
TR = p * Growth
E = Growth / (e * S)  # Effort
TC = c * E
Profit = TR - TC

# Substitute parameters
Profit_numeric = Profit.subs(params)
Profit_simplified = sp.expand(Profit_numeric)
print(f"Profit(S) = {Profit_simplified}")

# Differentiate
Profit_deriv = Profit_simplified.diff(S)
print(f"Profit'(S) = {Profit_deriv}")

# Solve for optimal S
S_opt = sp.solve(Profit_deriv, S)
print(f"Optimal stock: S* = {S_opt}")  # Output: [6750]

# Maximum profit
max_profit = Profit_simplified.subs(S, S_opt[0])
print(f"Maximum profit: ${float(max_profit):,.2f}")  # Output: $689,062.50
```

---

## 8. Summary: Key Formulas for Week 5

### Differentiation Rules

| Rule | Formula |
|------|---------|
| Product rule | $(fg)' = f'g + fg'$ |
| Quotient rule | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| Chain rule | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |
| Exponential | $\frac{d}{dx}[e^x] = e^x$ |
| Exponential (general) | $\frac{d}{dx}[e^{kx}] = ke^{kx}$ |
| Any base | $\frac{d}{dx}[a^x] = a^x \ln(a)$ |
| Logarithm | $\frac{d}{dx}[\ln x] = \frac{1}{x}$ |
| Logarithm (chain) | $\frac{d}{dx}[\ln(g(x))] = \frac{g'(x)}{g(x)}$ |

### Optimization

| Concept | Method |
|---------|--------|
| Find critical points | Solve $f'(x) = 0$ |
| Classify critical points | $f''(x) > 0$ → min, $f''(x) < 0$ → max |
| Constrained optimization | Use constraint to eliminate variable, then optimize |

### Bioeconomic Model

| Quantity | Formula |
|----------|---------|
| Growth | $G(S) = gS(1 - S/K)$ |
| Effort | $E = H/(eS)$ |
| Revenue | $TR = p \cdot H$ |
| Cost | $TC = c \cdot E$ |
| Profit | $\pi = TR - TC$ |
| MEY condition | $\frac{d\pi}{dS} = 0$ |

---

## 9. Exam Alignment

| Question | Topic | Week 5 Skill Required |
|----------|-------|----------------------|
| Q28 | Differentiation | Power rule, constant multiple, $\frac{d}{dx}[\ln x] = \frac{1}{x}$ |
| Q37 | Lymphocyte antiderivative | Integration of polynomial (connects to derivatives) |
| Q38 | Profit maximization | Build profit function → differentiate → solve → interpret |
| Q13 | Schaefer model | Setting $G'(S) = 0$ for MSY |

---

## 10. Looking Ahead: Week 6

Week 6 introduces **integration**—the reverse of differentiation. You will learn to:
- Find antiderivatives (indefinite integrals)
- Compute definite integrals for area under curves
- Apply integration to carbon sequestration and accumulated pollution
- Calculate consumer and producer surplus in economic applications

The connection: **differentiation tells us about rates of change; integration tells us about accumulated totals.**

---

## References

- Schaefer, M.B. (1957). Some considerations of population dynamics and economics in relation to the management of marine fisheries. *Journal of the Fisheries Research Board of Canada*, 14(5), 669-681.
- Clark, C.W. (1990). *Mathematical Bioeconomics: The Mathematics of Conservation*. Wiley.

---

*Next: Week 6 — Introduction to Integration: From Rates to Totals*
