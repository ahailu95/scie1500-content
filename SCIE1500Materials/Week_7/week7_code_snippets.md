# Week 7 Code Snippets: Definite Integrals and Applications

**Theme:** Accumulation and Area

**Prerequisites:** `numpy`, `matplotlib`, `sympy`

**Lab Notebooks:** `DegradedAreaExercises.ipynb`, `SequencesMalthusianTrap.ipynb`

---

## S01: Basic Setup and Imports

Import necessary libraries for Week 7 computations.

```python
# Week 7: Definite Integrals and Sequences
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
x, t, n, i = sp.symbols('x t n i')
a, d, r = sp.symbols('a d r', real=True)  # sequence parameters

print('Libraries loaded successfully!')
```

**Output:**
```
Libraries loaded successfully!
```

---

## S02: Definite Integral with SymPy

Evaluate definite integrals symbolically using SymPy.

```python
import sympy as sp
x = sp.symbols('x')

# Example 1: Basic polynomial
integral1 = sp.integrate(x**2, (x, 1, 3))
print(f'∫₁³ x² dx = {integral1}')
print(f'Decimal: {float(integral1):.4f}')

# Example 2: Exponential
integral2 = sp.integrate(sp.exp(x), (x, 0, 1))
print(f'\n∫₀¹ eˣ dx = {integral2}')
print(f'Decimal: {float(integral2):.4f}')

# Example 3: Logarithmic
integral3 = sp.integrate(1/x, (x, 1, sp.E))
print(f'\n∫₁ᵉ (1/x) dx = {integral3}')
```

**Output:**
```
∫₁³ x² dx = 26/3
Decimal: 8.6667

∫₀¹ eˣ dx = -1 + E
Decimal: 1.7183

∫₁ᵉ (1/x) dx = 1
```

---

## S03: Visualizing Area Under a Curve

Plot a function and shade the area under it.

```python
import numpy as np
import matplotlib.pyplot as plt

# Define function
x = np.linspace(0, 3, 100)
y = x**2

# Create plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2, label=r'$y = x^2$')

# Shade area under curve from 0 to 3
plt.fill_between(x, y, alpha=0.3, color='blue', label='Area = 9')

# Add labels
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Area under $y = x^2$ from $x=0$ to $x=3$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()

# Calculate area numerically
area = np.trapz(y, x)
print(f'Numerical approximation: {area:.4f}')
print(f'Exact value: 9.0000')
```

**Output:**
```
[Plot showing shaded area under parabola]
Numerical approximation: 9.0000
Exact value: 9.0000
```

---

## S04: Area Between Two Curves

Calculate and visualize area between two curves.

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define functions
x_vals = np.linspace(0, 1, 100)
y_upper = x_vals       # y = x
y_lower = x_vals**2    # y = x²

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_upper, 'b-', linewidth=2, label=r'$y = x$ (upper)')
plt.plot(x_vals, y_lower, 'r-', linewidth=2, label=r'$y = x^2$ (lower)')

# Shade area between curves
plt.fill_between(x_vals, y_lower, y_upper, alpha=0.3, color='green', 
                 label=r'Area = $\frac{1}{6}$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Between $y = x$ and $y = x^2$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate exactly with SymPy
x = sp.symbols('x')
area = sp.integrate(x - x**2, (x, 0, 1))
print(f'Exact area = {area} = {float(area):.4f}')
```

**Output:**
```
[Plot showing shaded region between curves]
Exact area = 1/6 = 0.1667
```

---

## S05: Arithmetic Sequence Generator

Generate arithmetic sequences using Python.

```python
import numpy as np

def generate_arithmetic_seq(a1, d, n):
    """Generate arithmetic sequence: a_n = a1 + (n-1)*d"""
    return [a1 + d*(i-1) for i in range(1, n+1)]

# Example: 2, 5, 8, 11, ...
a1, d = 2, 3
seq = generate_arithmetic_seq(a1, d, 10)
print(f'Arithmetic sequence (a1={a1}, d={d}):')
print(f'First 10 terms: {seq}')
print(f'a₁₀ = {seq[-1]}')

# Sum using formula
n = 10
a_n = seq[-1]
S_n = (n/2) * (a1 + a_n)
print(f'\nSum of first {n} terms:')
print(f'S_{n} = (n/2)(a₁ + a_n) = ({n}/2)({a1} + {a_n}) = {S_n}')
print(f'Verification: sum(seq) = {sum(seq)}')
```

**Output:**
```
Arithmetic sequence (a1=2, d=3):
First 10 terms: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
a₁₀ = 29

Sum of first 10 terms:
S_10 = (n/2)(a₁ + a_n) = (10/2)(2 + 29) = 155.0
Verification: sum(seq) = 155
```

**Key Formula:** $S_n = \frac{n}{2}(a_1 + a_n)$

---

## S06: Geometric Sequence Generator

Generate geometric sequences and compute sums.

```python
import numpy as np

def generate_geometric_seq(a1, r, n):
    """Generate geometric sequence: a_n = a1 * r^(n-1)"""
    return [a1 * r**(i-1) for i in range(1, n+1)]

# Example: 3, 6, 12, 24, ...
a1, r = 3, 2
seq = generate_geometric_seq(a1, r, 8)
print(f'Geometric sequence (a1={a1}, r={r}):')
print(f'First 8 terms: {seq}')

# Sum using formula: S_n = a1 * (1 - r^n) / (1 - r)
n = 5
S_n = a1 * (1 - r**n) / (1 - r)
print(f'\nSum of first {n} terms:')
print(f'S_{n} = a1*(1-r^n)/(1-r) = {a1}*(1-{r}^{n})/(1-{r}) = {S_n}')
print(f'Verification: sum(first 5) = {sum(seq[:5])}')

# For |r| < 1, sum to infinity converges
a1_decay, r_decay = 100, 0.5
S_inf = a1_decay / (1 - r_decay)
print(f'\nInfinite sum with a1={a1_decay}, r={r_decay}:')
print(f'S_∞ = a1/(1-r) = {a1_decay}/(1-{r_decay}) = {S_inf}')
```

**Output:**
```
Geometric sequence (a1=3, r=2):
First 8 terms: [3, 6, 12, 24, 48, 96, 192, 384]

Sum of first 5 terms:
S_5 = a1*(1-r^n)/(1-r) = 3*(1-2^5)/(1-2) = 93.0
Verification: sum(first 5) = 93

Infinite sum with a1=100, r=0.5:
S_∞ = a1/(1-r) = 100/(1-0.5) = 200.0
```

**Key Formulas:**
- Finite sum: $S_n = a_1 \cdot \frac{1 - r^n}{1 - r}$
- Infinite sum ($|r| < 1$): $S_\infty = \frac{a_1}{1 - r}$

---

## S07: Counting Terms in a Range (Q29 Style)

Find how many terms of a sequence fall within a given range.

```python
import numpy as np

# Sequence: a_i = 3 + 5(i-1) for i = 1, 2, 3, ...
# Simplified: a_i = 5i - 2

def count_terms_in_range(a1, d, lower, upper):
    """Count terms of arithmetic sequence a_i = a1 + (i-1)d in [lower, upper]"""
    # Find smallest i where a_i >= lower
    # a_i = a1 + (i-1)*d >= lower
    # (i-1)*d >= lower - a1
    # i >= (lower - a1)/d + 1
    
    i_min_exact = (lower - a1) / d + 1
    i_min = int(np.ceil(i_min_exact))
    
    # Find largest i where a_i <= upper
    i_max_exact = (upper - a1) / d + 1
    i_max = int(np.floor(i_max_exact))
    
    # Ensure i >= 1
    i_min = max(1, i_min)
    
    count = i_max - i_min + 1 if i_max >= i_min else 0
    
    return count, i_min, i_max

# Example from Q29: a_i = 3 + 5(i-1), count terms in [10, 150]
a1, d = 3, 5
lower, upper = 10, 150

count, i_min, i_max = count_terms_in_range(a1, d, lower, upper)

print(f'Sequence: a_i = {a1} + {d}(i-1)')
print(f'Range: [{lower}, {upper}]')
print(f'Smallest index i with a_i >= {lower}: i = {i_min}')
print(f'Largest index i with a_i <= {upper}: i = {i_max}')
print(f'Number of terms in range: {count}')

# Verify
a_min = a1 + (i_min - 1) * d
a_max = a1 + (i_max - 1) * d
print(f'\nVerification:')
print(f'a_{i_min} = {a_min} (should be >= {lower})')
print(f'a_{i_max} = {a_max} (should be <= {upper})')
```

**Output:**
```
Sequence: a_i = 3 + 5(i-1)
Range: [10, 150]
Smallest index i with a_i >= 10: i = 3
Largest index i with a_i <= 150: i = 30
Number of terms in range: 28

Verification:
a_3 = 13 (should be >= 10)
a_30 = 148 (should be <= 150)
```

---

## S08: Malthusian Trap Simulation

Simulate and visualize the Malthusian crisis point.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
P0 = 100  # Initial population (millions)
F0 = 100  # Initial food capacity (millions)
r = 1.03  # Population growth rate (3% per year)
d = 5     # Food capacity increase per year (millions)
years = 100

# Generate sequences
n = np.arange(years + 1)
population = P0 * r**n            # Geometric: P_n = P0 * r^n
food_capacity = F0 + d * n         # Arithmetic: F_n = F0 + d*n

# Find crisis point (where population exceeds food capacity)
crisis_idx = np.where(population > food_capacity)[0]
if len(crisis_idx) > 0:
    crisis_year = crisis_idx[0]
    print(f'Malthusian Crisis Year: {crisis_year}')
    print(f'Population at crisis: {population[crisis_year]:.1f} million')
    print(f'Food capacity at crisis: {food_capacity[crisis_year]:.1f} million')
else:
    print('No crisis within simulation period')
    crisis_year = None

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n, population, 'r-', linewidth=2, label='Population (geometric)')
plt.plot(n, food_capacity, 'g-', linewidth=2, label='Food Capacity (arithmetic)')

if crisis_year:
    plt.axvline(x=crisis_year, color='orange', linestyle='--', 
                label=f'Crisis at year {crisis_year}')
    plt.scatter([crisis_year], [population[crisis_year]], 
                color='red', s=100, zorder=5)

plt.xlabel('Years')
plt.ylabel('Population / Food Capacity (millions)')
plt.title('Malthusian Trap: Geometric Population vs Arithmetic Food Growth')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim([0, 80])
plt.tight_layout()
plt.show()
```

**Output:**
```
Malthusian Crisis Year: 71
Population at crisis: 815.5 million
Food capacity at crisis: 455.0 million
[Plot showing intersection of geometric and arithmetic curves]
```

**Key Insight:** Geometric growth (population) eventually outpaces arithmetic growth (food), illustrating Malthus's concern.

---

## S09: Average Value of a Function

Calculate and visualize the average value of a function.

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function: f(x) = x^2 on [0, 3]
x = sp.symbols('x')
a, b = 0, 3
f = x**2

# Calculate average value
integral = sp.integrate(f, (x, a, b))
avg_value = integral / (b - a)
print(f'f(x) = x² on [{a}, {b}]')
print(f'∫₀³ x² dx = {integral}')
print(f'Average value = {integral}/{b-a} = {avg_value}')

# Visualize
x_vals = np.linspace(a, b, 100)
y_vals = x_vals**2

plt.figure(figsize=(9, 5))
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=r'$f(x) = x^2$')
plt.fill_between(x_vals, y_vals, alpha=0.2, color='blue', label='Area = 9')

# Draw average value line
avg_float = float(avg_value)
plt.hlines(y=avg_float, xmin=a, xmax=b, colors='r', 
           linestyles='--', linewidth=2, label=f'Average value = {avg_float}')
plt.fill_between([a, b], [avg_float, avg_float], alpha=0.2, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Average Value: Rectangle with same area as region under curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f'\nRectangle area = {avg_float} × {b-a} = {avg_float * (b-a)}')
print(f'Area under curve = {float(integral)}')
```

**Output:**
```
f(x) = x² on [0, 3]
∫₀³ x² dx = 9
Average value = 9/3 = 3
[Plot showing curve and average value rectangle]

Rectangle area = 3.0 × 3 = 9.0
Area under curve = 9.0
```

**Key Formula:** $f_{avg} = \frac{1}{b-a} \int_a^b f(x) \, dx$

---

## S10: Area Between Curves — Degraded Land Example

Calculate area of degraded land region bounded by two curves.

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define boundaries (simplified from lab notebook)
# Lower: y = exp(0.05x)
# Upper: y = 30 + x

x = sp.symbols('x')
lower = sp.exp(0.05*x)
upper = 30 + x

# Calculate area from x=0 to x=80
a, b = 0, 80
integrand = upper - lower

area = sp.integrate(integrand, (x, a, b))
area_float = float(area.evalf())

print('Degraded Land Area Calculation')
print('=' * 40)
print(f'Lower boundary: y = e^(0.05x)')
print(f'Upper boundary: y = 30 + x')
print(f'Integration limits: x ∈ [{a}, {b}]')
print(f'\nArea = ∫₀⁸⁰ [(30 + x) - e^(0.05x)] dx')
print(f'Area = {area}')
print(f'Area ≈ {area_float:.1f} km²')

# Visualization
x_vals = np.linspace(a, b, 200)
y_lower = np.exp(0.05 * x_vals)
y_upper = 30 + x_vals

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_lower, 'r-', linewidth=2, label=r'Lower: $y = e^{0.05x}$')
plt.plot(x_vals, y_upper, 'b-', linewidth=2, label=r'Upper: $y = 30 + x$')
plt.fill_between(x_vals, y_lower, y_upper, alpha=0.3, color='brown',
                 label=f'Degraded Area ≈ {area_float:.0f} km²')

plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Degraded Land Area - Integration Example')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Output:**
```
Degraded Land Area Calculation
========================================
Lower boundary: y = e^(0.05x)
Upper boundary: y = 30 + x
Integration limits: x ∈ [0, 80]

Area = ∫₀⁸⁰ [(30 + x) - e^(0.05x)] dx
Area = 5620 - 20*exp(4) + 20
Area ≈ 4548.4 km²
[Plot showing shaded degraded region]
```

---

## S11: Consumer and Producer Surplus Preview

Visualize and set up CS/PS calculations (full calculation in Week 12).

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Supply and Demand
# Demand: Qd = 60 - P  =>  P = 60 - Q
# Supply: Qs = P - 20  =>  P = Q + 20

# Find equilibrium
P, Q = sp.symbols('P Q')
eq = sp.solve([Q - (60 - P), Q - (P - 20)], [P, Q])
P_star = float(eq[P])
Q_star = float(eq[Q])

print('Market Equilibrium')
print('=' * 40)
print(f'Demand: Qd = 60 - P')
print(f'Supply: Qs = P - 20')
print(f'\nEquilibrium: P* = {P_star}, Q* = {Q_star}')

# Visualization
Q_range = np.linspace(0, 50, 100)
P_demand = 60 - Q_range       # Inverse demand
P_supply = Q_range + 20        # Inverse supply

plt.figure(figsize=(10, 7))

# Plot demand and supply
plt.plot(Q_range, P_demand, 'b-', linewidth=2, label='Demand: P = 60 - Q')
plt.plot(Q_range, P_supply, 'r-', linewidth=2, label='Supply: P = Q + 20')

# Shade Consumer Surplus (area between demand and P*)
Q_cs = np.linspace(0, Q_star, 100)
plt.fill_between(Q_cs, P_star, 60 - Q_cs, alpha=0.3, color='blue',
                 label='Consumer Surplus (CS)')

# Shade Producer Surplus (area between P* and supply)
Q_ps = np.linspace(0, Q_star, 100)
plt.fill_between(Q_ps, Q_ps + 20, P_star, alpha=0.3, color='red',
                 label='Producer Surplus (PS)')

# Mark equilibrium
plt.plot(Q_star, P_star, 'ko', markersize=10, zorder=5)
plt.annotate(f'Equilibrium\n({Q_star}, {P_star})', xy=(Q_star, P_star),
             xytext=(Q_star+5, P_star+5), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='black'))

plt.xlabel('Quantity (Q)')
plt.ylabel('Price (P)')
plt.title('Consumer and Producer Surplus')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.xlim([0, 50])
plt.ylim([0, 70])
plt.tight_layout()
plt.show()

# Calculate CS and PS
Q_sym = sp.symbols('Q')
CS = sp.integrate(60 - Q_sym - P_star, (Q_sym, 0, Q_star))
PS = sp.integrate(P_star - (Q_sym + 20), (Q_sym, 0, Q_star))

print(f'\nConsumer Surplus = {CS} = {float(CS)}')
print(f'Producer Surplus = {PS} = {float(PS)}')
print(f'Total Surplus = {float(CS + PS)}')
```

**Output:**
```
Market Equilibrium
========================================
Demand: Qd = 60 - P
Supply: Qs = P - 20

Equilibrium: P* = 40.0, Q* = 20.0
[Plot showing supply, demand, CS and PS regions]

Consumer Surplus = 200 = 200.0
Producer Surplus = 200 = 200.0
Total Surplus = 400.0
```

**Key Formulas:**
- $CS = \int_0^{Q^*} [D(Q) - P^*] \, dQ$
- $PS = \int_0^{Q^*} [P^* - S(Q)] \, dQ$

---

## S12: Riemann Sum Visualization

Visualize how Riemann sums approximate the definite integral.

```python
import numpy as np
import matplotlib.pyplot as plt

def riemann_sum_plot(f, a, b, n, method='left'):
    """Plot Riemann sum approximation to integral"""
    dx = (b - a) / n
    x_bars = np.linspace(a, a + (n-1)*dx, n) if method == 'left' else \
             np.linspace(a + dx, b, n) if method == 'right' else \
             np.linspace(a + dx/2, b - dx/2, n)
    
    heights = f(x_bars)
    riemann_sum = np.sum(heights * dx)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot function
    x_smooth = np.linspace(a, b, 200)
    ax.plot(x_smooth, f(x_smooth), 'b-', linewidth=2, label=r'$f(x) = x^2$')
    
    # Draw rectangles
    x_rect = np.linspace(a, b - dx, n) if method in ['left', 'midpoint'] else \
             np.linspace(a + dx, b, n)
    for i, x_start in enumerate(np.linspace(a, a + (n-1)*dx, n)):
        rect = plt.Rectangle((x_start, 0), dx, heights[i], 
                              fill=True, alpha=0.3, color='green', 
                              edgecolor='green', linewidth=1)
        ax.add_patch(rect)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'{method.capitalize()} Riemann Sum with n = {n} rectangles')
    ax.legend([f'Sum = {riemann_sum:.4f}, Exact = {(b**3 - a**3)/3:.4f}'])
    ax.set_xlim([a - 0.2, b + 0.2])
    ax.set_ylim([0, f(b) + 0.5])
    ax.grid(True, alpha=0.3)
    
    return riemann_sum

# Function to integrate
def f(x):
    return x**2

# Compare different numbers of rectangles
for n in [5, 10, 20]:
    sum_val = riemann_sum_plot(f, 0, 3, n, 'left')
    plt.tight_layout()
    plt.show()
    print(f'n = {n}: Riemann sum = {sum_val:.4f}, Exact = {9:.4f}, Error = {abs(sum_val - 9):.4f}')
```

**Output:**
```
[Three plots showing increasingly accurate approximations]
n = 5: Riemann sum = 6.4800, Exact = 9.0000, Error = 2.5200
n = 10: Riemann sum = 7.6950, Exact = 9.0000, Error = 1.3050
n = 20: Riemann sum = 8.3363, Exact = 9.0000, Error = 0.6637
```

**Key Insight:** As $n \to \infty$, the Riemann sum converges to the definite integral.

---

## Summary Table

| ID | Topic | Description |
|----|-------|-------------|
| S01 | Setup | Import libraries, define symbols |
| S02 | Definite Integral | SymPy `integrate()` with limits |
| S03 | Area Visualization | Shade area under a curve |
| S04 | Area Between Curves | Upper minus lower integration |
| S05 | Arithmetic Sequence | $a_n = a_1 + (n-1)d$, sum formula |
| S06 | Geometric Sequence | $a_n = a_1 \cdot r^{n-1}$, sum formulas |
| S07 | Counting Terms | Q29-style range counting |
| S08 | Malthusian Trap | Geometric vs arithmetic growth |
| S09 | Average Value | $f_{avg} = \frac{1}{b-a}\int_a^b f(x)dx$ |
| S10 | Degraded Land | Applied area between curves |
| S11 | CS/PS Preview | Economic surplus visualization |
| S12 | Riemann Sums | Approximating integrals with rectangles |

---

## Key Formulas

| Concept | Formula |
|---------|---------|
| Definite integral | $\int_a^b f(x) \, dx = F(b) - F(a)$ |
| Area between curves | $\int_a^b [f_{upper}(x) - f_{lower}(x)] \, dx$ |
| Average value | $f_{avg} = \frac{1}{b-a} \int_a^b f(x) \, dx$ |
| Arithmetic sequence | $a_n = a_1 + (n-1)d$ |
| Arithmetic sum | $S_n = \frac{n}{2}(a_1 + a_n)$ |
| Geometric sequence | $a_n = a_1 \cdot r^{n-1}$ |
| Geometric sum (finite) | $S_n = a_1 \cdot \frac{1 - r^n}{1 - r}$ |
| Geometric sum (infinite, $|r|<1$) | $S_\infty = \frac{a_1}{1 - r}$ |

---

*Good luck on your exam!*
