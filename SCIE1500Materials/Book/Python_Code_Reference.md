<?xml version="1.0" encoding="UTF-8"?>
# 💻 SCIE1500 Python Code Reference

## Computational Tools for Analytical Scientists

---

<div align="center">

# 🐍 **PYTHON CODE SNIPPETS** 📊

### Ready-to-Use Code for Every Week

---

*"Programs must be written for people to read, and only incidentally for machines to execute."*
— Harold Abelson

---

</div>

---

# How to Use This Reference

## 🎯 Purpose

This guide provides ready-to-use Python code for each week's concepts. Copy, paste, and modify!

## 📦 Essential Imports

Always start your notebooks with:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom, binomtest
import sympy as sp
import pandas as pd
```

---

# Quick Navigation

> **Note**: Jump links in the table below work in HTML/PDF versions. In the app, use the scroll bar or search feature to navigate to specific weeks.

| Week | Topics | Jump |
|:----:|:-------|:-----|
| 0 | Python Basics | [Week 0](#week-0-python-basics) |
| 1 | Functions & Plotting | [Week 1](#week-1-functions-and-plotting) |
| 2 | Exponentials & Logs | [Week 2](#week-2-exponentials-and-logarithms) |
| 3 | Logistic & Schaefer | [Week 3](#week-3-logistic-and-schaefer-models) |
| 4 | Limits & Derivatives | [Week 4](#week-4-limits-and-derivatives) |
| 5 | Optimization | [Week 5](#week-5-optimization) |
| 6-7 | Integration | [Week 6-7](#weeks-6-7-integration) |
| 8 | Predator-Prey | [Week 8](#week-8-predator-prey-dynamics) |
| 9 | Probability & Combinatorics | [Week 9](#week-9-probability-and-combinatorics) |
| 10 | Hypothesis Testing | [Week 10](#week-10-hypothesis-testing) |
| 11 | Trigonometry | [Week 11](#week-11-trigonometry) |
| 12 | Linear Programming | [Week 12](#week-12-linear-programming) |

---

<div style="page-break-after: always;"></div>

---

# Week 0: Python Basics

## Python as a Calculator

```python
# Basic arithmetic
print(3 + 4 * 2)       # → 11 (BODMAS!)
print((3 + 4) * 2)     # → 14
print(2 ** 10)         # → 1024 (exponent)
print(17 // 5)         # → 3 (floor division)
print(17 % 5)          # → 2 (remainder)
```

## Variables and Data Types

```python
# Variable assignment
temperature = 23.5
name = "ocean"
is_polluted = True
count = 42

# Check types
print(type(temperature))  # float
print(type(name))         # str
print(type(count))        # int
```

## NumPy Arrays

```python
import numpy as np

# Create arrays
x = np.array([1, 2, 3, 4, 5])
y = np.linspace(0, 10, 100)    # 100 points from 0 to 10
z = np.arange(0, 10, 0.5)      # 0 to 10 in steps of 0.5

# Element-wise operations
squared = x ** 2
doubled = 2 * x

# Statistics
print(f"Mean: {np.mean(x)}")
print(f"Sum: {np.sum(x)}")
print(f"Max: {np.max(x)}")
```

## Basic Plotting

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x ** 2

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = x²')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('A Simple Quadratic Function', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

# Week 1: Functions and Plotting

## Plotting Multiple Functions

```python
x = np.linspace(-5, 5, 200)

# Linear function
y_linear = 2*x + 3

# Quadratic function
y_quad = x**2 - 4*x + 3

plt.figure(figsize=(12, 5))

# Left subplot
plt.subplot(1, 2, 1)
plt.plot(x, y_linear, 'b-', label='y = 2x + 3')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function')
plt.legend()
plt.grid(True, alpha=0.3)

# Right subplot
plt.subplot(1, 2, 2)
plt.plot(x, y_quad, 'r-', label='y = x² - 4x + 3')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## Finding Vertex of Parabola

```python
def find_vertex(a, b, c):
    """Find vertex of y = ax² + bx + c"""
    x_vertex = -b / (2*a)
    y_vertex = a*x_vertex**2 + b*x_vertex + c
    return x_vertex, y_vertex

# Example: y = 2x² - 8x + 3
a, b, c = 2, -8, 3
vx, vy = find_vertex(a, b, c)
print(f"Vertex: ({vx}, {vy})")  # (2.0, -5.0)
```

## Domain Restrictions

```python
# Square root function (domain: x ≥ 0)
x = np.linspace(0, 10, 100)  # Start from 0!
y = np.sqrt(x)

# 1/x function (domain: x ≠ 0)
x_neg = np.linspace(-5, -0.1, 50)
x_pos = np.linspace(0.1, 5, 50)

plt.plot(x_neg, 1/x_neg, 'b-')
plt.plot(x_pos, 1/x_pos, 'b-')
plt.ylim(-10, 10)
plt.title('y = 1/x')
plt.show()
```

---

# Week 2: Exponentials and Logarithms

## Exponential Functions

```python
x = np.linspace(-2, 3, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, 2**x, 'b-', label='y = 2ˣ')
plt.plot(x, np.exp(x), 'r-', label='y = eˣ')
plt.plot(x, 3**x, 'g-', label='y = 3ˣ')
plt.plot(x, 0.5**x, 'm--', label='y = 0.5ˣ (decay)')

plt.axhline(y=1, color='k', linestyle=':', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Functions')
plt.legend()
plt.ylim(0, 20)
plt.grid(True, alpha=0.3)
plt.show()
```

## Logarithmic Functions

```python
x = np.linspace(0.01, 10, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, np.log(x), 'b-', label='y = ln(x)')
plt.plot(x, np.log10(x), 'r-', label='y = log₁₀(x)')
plt.plot(x, np.log2(x), 'g-', label='y = log₂(x)')

plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=1, color='k', linestyle=':', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithmic Functions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Population Growth Model

```python
def exponential_growth(P0, r, t):
    """Model: P(t) = P₀ · eʳᵗ"""
    return P0 * np.exp(r * t)

# Parameters
P0 = 1000  # Initial population
r = 0.05  # Growth rate (5% per year)
t = np.linspace(0, 50, 100)

P = exponential_growth(P0, r, t)

plt.figure(figsize=(10, 6))
plt.plot(t, P, 'b-', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title(f'Exponential Growth: P(t) = {P0}e^{{{r}t}}')
plt.grid(True, alpha=0.3)
plt.show()

# When does population double?
doubling_time = np.log(2) / r
print(f"Doubling time: {doubling_time:.2f} years")
```

---

# Week 3: Logistic and Schaefer Models

## Logistic Growth

```python
def logistic(t, K, A, alpha):
    """Logistic function: P(t) = K / (1 + A·e^(-αt))"""
    return K / (1 + A * np.exp(-alpha * t))

# Parameters
K = 10000       # Carrying capacity
P0 = 500        # Initial population
A = (K - P0) / P0  # Computed from initial condition
alpha = 0.1     # Growth rate

t = np.linspace(0, 100, 200)
P = logistic(t, K, A, alpha)

plt.figure(figsize=(10, 6))
plt.plot(t, P, 'b-', linewidth=2)
plt.axhline(y=K, color='r', linestyle='--', label=f'Carrying capacity K={K}')
plt.axhline(y=K/2, color='g', linestyle=':', label='Inflection point')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Logistic Growth Model')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Schaefer Growth Model

```python
def schaefer_growth(S, g, K):
    """Schaefer model: G(S) = gS(1 - S/K)"""
    return g * S * (1 - S/K)

# Parameters
g = 0.08      # Intrinsic growth rate
K = 20000     # Carrying capacity

S = np.linspace(0, K, 200)
G = schaefer_growth(S, g, K)

# Maximum sustainable yield
S_MSY = K / 2
MSY = schaefer_growth(S_MSY, g, K)

plt.figure(figsize=(10, 6))
plt.plot(S, G, 'b-', linewidth=2)
plt.scatter([S_MSY], [MSY], color='red', s=100, zorder=5, 
            label=f'MSY = {MSY:.0f} at S = {S_MSY:.0f}')
plt.xlabel('Stock Size (S)')
plt.ylabel('Growth Rate G(S)')
plt.title('Schaefer Growth Model')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Maximum Sustainable Yield (MSY): {MSY:.0f} tonnes/year")
print(f"Stock at MSY: {S_MSY:.0f} tonnes")
```

## Function Composition

```python
def f(x):
    return x**2 + 1

def g(x):
    return 3*x

# Composition (f ∘ g)(x) = f(g(x))
def f_compose_g(x):
    return f(g(x))

x = np.linspace(-3, 3, 100)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, f(x), 'b-')
plt.title('f(x) = x² + 1')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
plt.plot(x, g(x), 'r-')
plt.title('g(x) = 3x')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 3)
plt.plot(x, f_compose_g(x), 'g-')
plt.title('(f ∘ g)(x) = 9x² + 1')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

# Week 4: Limits and Derivatives

## Numerical Derivatives

```python
def numerical_derivative(f, x, h=1e-8):
    """Calculate derivative using central difference"""
    return (f(x + h) - f(x - h)) / (2 * h)

# Example: f(x) = x³
f = lambda x: x**3
x0 = 2

slope = numerical_derivative(f, x0)
print(f"f'({x0}) ≈ {slope:.6f}")  # Should be 12
```

## Plotting Function and Derivative

```python
def f(x):
    return x**3 - 3*x**2 + 2

def f_prime(x):
    return 3*x**2 - 6*x

x = np.linspace(-1, 4, 200)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(x, f(x), 'b-', linewidth=2)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.set_title('f(x) = x³ - 3x² + 2')
ax1.set_ylabel('f(x)')
ax1.grid(True, alpha=0.3)

ax2.plot(x, f_prime(x), 'r-', linewidth=2)
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.fill_between(x, f_prime(x), 0, where=(f_prime(x) > 0), alpha=0.3, color='green', label='f increasing')
ax2.fill_between(x, f_prime(x), 0, where=(f_prime(x) < 0), alpha=0.3, color='red', label='f decreasing')
ax2.set_title("f'(x) = 3x² - 6x")
ax2.set_xlabel('x')
ax2.set_ylabel("f'(x)")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## SymPy: Symbolic Calculus

SymPy computes exact derivatives and integrals. Use it whenever you need algebraic answers.

```python
import sympy as sp

x = sp.Symbol('x')        # Declare symbolic variable

# Differentiate
f = x**3 - 6*x**2 + 9*x + 1
f_prime = sp.diff(f, x)           # First derivative
f_double_prime = sp.diff(f, x, 2) # Second derivative

# Solve f'(x) = 0
critical_pts = sp.solve(f_prime, x)

# Integrate
area = sp.integrate(x**2, (x, 0, 3))   # Definite: returns 9
indef = sp.integrate(x**2, x)          # Indefinite: returns x³/3

# Substitute a value
val = f.subs(x, 2)                     # f(2)

# Convert to float when needed
print(float(area))
```

## Finding Critical Points

```python
import sympy as sp

x = sp.Symbol('x')
f = x**3 - 6*x**2 + 9*x + 1

# Find critical points (where f'(x) = 0)
f_prime = sp.diff(f, x)
critical_points = sp.solve(f_prime, x)
print(f"Critical points: x = {critical_points}")

# Second derivative test
f_double_prime = sp.diff(f, x, 2)
print("\nSecond Derivative Test:")
for cp in critical_points:
    fpp = f_double_prime.subs(x, cp)
    if fpp > 0:
        print(f"x = {cp}: f''(x) = {fpp} → Local minimum, f(x) = {f.subs(x, cp)}")
    elif fpp < 0:
        print(f"x = {cp}: f''(x) = {fpp} → Local maximum, f(x) = {f.subs(x, cp)}")
```

---

# Week 5: Optimization

## Finding Maximum/Minimum

```python
import sympy as sp

x = sp.Symbol('x')

# Find minimum of f(x) = x² - 4x + 5
f = x**2 - 4*x + 5
f_prime = sp.diff(f, x)
print(f"f'(x) = {f_prime}")

critical_pts = sp.solve(f_prime, x)
x_min = critical_pts[0]
print(f"Minimum at x = {x_min}")
print(f"Minimum value = {f.subs(x, x_min)}")

# Verify via second derivative
f_double_prime = sp.diff(f, x, 2)
print(f"f''({x_min}) = {f_double_prime.subs(x, x_min)} > 0 → minimum ✓")
```

## Optimization with Constraints

```python
import sympy as sp

x = sp.Symbol('x')

# Maximise profit P = 50x - x² - 10, for 0 ≤ x ≤ 30
profit = 50*x - x**2 - 10
dp = sp.diff(profit, x)
print(f"dP/dx = {dp}")

x_star = sp.solve(dp, x)[0]
P_star = profit.subs(x, x_star)
print(f"Optimal quantity: x = {x_star}")
print(f"Maximum profit: P = {P_star}")

# Confirm it's a maximum
d2p = sp.diff(profit, x, 2)
print(f"d²P/dx² = {d2p} < 0 → maximum ✓")
```

## Second Derivative Test

```python
import sympy as sp

x = sp.Symbol('x')
f = x**4 - 8*x**2 + 16
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f, x, 2)

# Find all critical points
critical_pts = sp.solve(f_prime, x)
print(f"f'(x) = {f_prime}")
print(f"Critical points: x = {critical_pts}")

print("\nSecond Derivative Test:")
for cp in critical_pts:
    fpp = f_double_prime.subs(x, cp)
    if fpp > 0:
        classification = "Local minimum"
    elif fpp < 0:
        classification = "Local maximum"
    else:
        classification = "Inconclusive"
    print(f"  x = {cp}: f''(x) = {fpp} → {classification}, f(x) = {f.subs(x, cp)}")
```

---

# Weeks 6-7: Integration

## Symbolic Integration

```python
import sympy as sp

x = sp.Symbol('x')

# Definite integral of x² from 0 to 3
result = sp.integrate(x**2, (x, 0, 3))
print(f"∫₀³ x² dx = {result}")          # 9

# Indefinite integral
indef = sp.integrate(x**2, x)
print(f"∫ x² dx = {indef} + C")         # x³/3

# Area under sin(x) from 0 to π
result2 = sp.integrate(sp.sin(x), (x, 0, sp.pi))
print(f"∫₀^π sin(x) dx = {result2}")    # 2
```

## Riemann Sums

```python
def left_riemann_sum(f, a, b, n):
    """Left Riemann sum approximation"""
    dx = (b - a) / n
    x = np.linspace(a, b - dx, n)
    return np.sum(f(x)) * dx

def right_riemann_sum(f, a, b, n):
    """Right Riemann sum approximation"""
    dx = (b - a) / n
    x = np.linspace(a + dx, b, n)
    return np.sum(f(x)) * dx

def midpoint_riemann_sum(f, a, b, n):
    """Midpoint Riemann sum approximation"""
    dx = (b - a) / n
    x = np.linspace(a + dx/2, b - dx/2, n)
    return np.sum(f(x)) * dx

# Compare approximations for ∫₀¹ x² dx (exact = 1/3)
f = lambda x: x**2
for n in [10, 100, 1000]:
    left = left_riemann_sum(f, 0, 1, n)
    right = right_riemann_sum(f, 0, 1, n)
    mid = midpoint_riemann_sum(f, 0, 1, n)
    print(f"n={n:4d}: Left={left:.6f}, Right={right:.6f}, Mid={mid:.6f}")
```

## Visualizing Area Under Curve

```python
import sympy as sp

x_sym = sp.Symbol('x')
a, b = 0, 2

# Exact area with SymPy
area = sp.integrate(x_sym**2, (x_sym, a, b))
print(f"Exact area = {area}")            # 8/3

# Plot using numpy
x = np.linspace(a, b, 100)
y = x**2

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x²')
plt.fill_between(x, y, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Area under curve from {a} to {b}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.text(1, 2, f'Area = {area}', fontsize=14, ha='center')
plt.show()
```

## Average Value of a Function

```python
import sympy as sp

x = sp.Symbol('x')

# Average value of f over [a, b] = (1/(b-a)) * ∫_a^b f(x) dx
def average_value(f, a, b):
    integral = sp.integrate(f, (x, a, b))
    return integral / (b - a)

# Average value of sin(x) from 0 to π
avg = average_value(sp.sin(x), 0, sp.pi)
print(f"Average value of sin(x) from 0 to π = {avg} ≈ {float(avg):.4f}")  # 2/π ≈ 0.6366
```

## Economic Surplus

```python
import sympy as sp

Q = sp.Symbol('Q')

def demand(q):
    return 100 - 2*q

def supply(q):
    return 20 + q

# Find equilibrium: demand = supply
eq_Q = sp.solve(demand(Q) - supply(Q), Q)[0]
eq_P = demand(eq_Q)
print(f"Equilibrium: Q* = {eq_Q}, P* = {eq_P}")

# Consumer surplus: ∫₀^Q* (demand(Q) - P*) dQ
CS = sp.integrate(demand(Q) - eq_P, (Q, 0, eq_Q))
print(f"Consumer Surplus: ${CS}")

# Producer surplus: ∫₀^Q* (P* - supply(Q)) dQ
PS = sp.integrate(eq_P - supply(Q), (Q, 0, eq_Q))
print(f"Producer Surplus: ${PS}")

# Visualization (convert to floats for numpy)
Q_np = np.linspace(0, 50, 100)
eq_Q_num = float(eq_Q)
eq_P_num = float(eq_P)

plt.figure(figsize=(10, 6))
plt.plot(Q_np, 100 - 2*Q_np, 'b-', label='Demand')
plt.plot(Q_np, 20 + Q_np, 'r-', label='Supply')
Q_fill = np.linspace(0, eq_Q_num, 50)
plt.fill_between(Q_fill, 100 - 2*Q_fill, eq_P_num,
                 alpha=0.3, color='blue', label=f'Consumer Surplus = ${CS}')
plt.fill_between(Q_fill, eq_P_num, 20 + Q_fill,
                 alpha=0.3, color='red', label=f'Producer Surplus = ${PS}')
plt.scatter([eq_Q_num], [eq_P_num], color='green', s=100, zorder=5)
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Equilibrium and Economic Surplus')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

# Week 8: Predator-Prey Dynamics

## Lotka-Volterra Simulation

```python
from scipy.integrate import odeint

def lotka_volterra(y, t, r, a, b, m):
    """
    Lotka-Volterra predator-prey model
    H: prey (herbivore), P: predator
    dH/dt = rH - aHP
    dP/dt = baHP - mP
    """
    H, P = y
    dH = r*H - a*H*P
    dP = b*a*H*P - m*P
    return [dH, dP]

# Parameters
r = 0.5   # Prey birth rate
a = 0.02  # Attack rate
b = 0.5   # Conversion efficiency
m = 0.4   # Predator death rate

# Initial conditions
H0, P0 = 100, 10
y0 = [H0, P0]

# Time points
t = np.linspace(0, 100, 1000)

# Solve ODE
solution = odeint(lotka_volterra, y0, t, args=(r, a, b, m))
H, P = solution[:, 0], solution[:, 1]

# Plot time series
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(t, H, 'b-', label='Prey (H)')
ax1.plot(t, P, 'r-', label='Predator (P)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Population')
ax1.set_title('Lotka-Volterra Predator-Prey Dynamics')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Phase diagram
ax2.plot(H, P, 'g-', linewidth=0.5)
ax2.scatter([H0], [P0], color='blue', s=100, zorder=5, label='Start')
ax2.set_xlabel('Prey Population (H)')
ax2.set_ylabel('Predator Population (P)')
ax2.set_title('Phase Diagram')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Equilibrium
H_eq = m / (b * a)
P_eq = r / a
print(f"Equilibrium: H* = {H_eq:.1f}, P* = {P_eq:.1f}")
```

---

# Week 9: Probability and Combinatorics

## Factorials and Combinatorics

```python
import math
from itertools import permutations, combinations

# Factorials
print(f"5! = {math.factorial(5)}")  # 120
print(f"10! = {math.factorial(10)}")  # 3628800

# Permutations: P(n,k) = n!/(n-k)!
def P(n, k):
    return math.factorial(n) // math.factorial(n - k)

print(f"P(5,3) = {P(5,3)}")  # 60

# Combinations: C(n,k) = n!/[k!(n-k)!]
def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(f"C(5,3) = {C(5,3)}")  # 10

# Using itertools
items = ['A', 'B', 'C', 'D']
print(f"\nPermutations of 2 from {items}:")
for p in permutations(items, 2):
    print(p)

print(f"\nCombinations of 2 from {items}:")
for c in combinations(items, 2):
    print(c)
```

## Binomial Distribution

```python
from scipy.stats import binom

n = 12   # Number of trials
p = 0.5  # Probability of success

# P(X = k) for all k
k_values = np.arange(0, n+1)
probabilities = binom.pmf(k_values, n, p)

# Create a nice table
import pandas as pd
df = pd.DataFrame({
    'k': k_values,
    'P(X = k)': np.round(probabilities, 5)
})
print(df.to_string(index=False))

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(k_values, probabilities, color='steelblue', edgecolor='black')
plt.axvline(x=n*p, color='red', linestyle='--', label=f'Mean = {n*p}')
plt.xlabel('Number of Successes (k)')
plt.ylabel('P(X = k)')
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.xticks(k_values)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# Expected value and variance
print(f"\nE[X] = np = {n*p}")
print(f"Var(X) = np(1-p) = {n*p*(1-p)}")
```

## Bayes' Theorem and Medical Testing

```python
def calculate_ppv(sensitivity, specificity, prevalence):
    """
    Calculate Positive Predictive Value (PPV)
    PPV = P(Disease | Positive Test)
    """
    # P(positive test)
    P_positive = sensitivity * prevalence + (1 - specificity) * (1 - prevalence)
    
    # PPV using Bayes' theorem
    ppv = (sensitivity * prevalence) / P_positive
    return ppv

# Medical test example
sensitivity = 0.95    # P(+|disease) = 95%
specificity = 0.90    # P(-|no disease) = 90%
prevalence = 0.01     # P(disease) = 1%

ppv = calculate_ppv(sensitivity, specificity, prevalence)
print(f"Positive Predictive Value (PPV): {ppv:.4f}")
print(f"Even with a positive test, only {ppv*100:.1f}% chance of disease!")

# Show how PPV varies with prevalence
prevalences = np.linspace(0.001, 0.20, 100)
ppvs = [calculate_ppv(sensitivity, specificity, prev) for prev in prevalences]

plt.figure(figsize=(10, 6))
plt.plot(prevalences * 100, np.array(ppvs) * 100, 'b-', linewidth=2)
plt.xlabel('Disease Prevalence (%)')
plt.ylabel('Positive Predictive Value (%)')
plt.title('How Prevalence Affects PPV\n(Sensitivity=95%, Specificity=90%)')
plt.grid(True, alpha=0.3)
plt.show()
```

## Expected Value Calculation

```python
# Expected Value from probability distribution (Q33 style)
x_values = np.array([0, 3, 4, 6])
probabilities = np.array([0.2, 0.4, 0.3, 0.1])

# Verify probabilities sum to 1
print(f"Sum of probabilities: {probabilities.sum()}")

# Calculate E[X]
expected_value = np.sum(x_values * probabilities)
print(f"\nE[X] = Σ x·P(x)")
for x, p in zip(x_values, probabilities):
    print(f"      + {x} × {p} = {x*p}")
print(f"E[X] = {expected_value}")

# Variance
expected_x_squared = np.sum(x_values**2 * probabilities)
variance = expected_x_squared - expected_value**2
print(f"\nVar(X) = E[X²] - (E[X])² = {expected_x_squared} - {expected_value}² = {variance}")
```

---

# Week 10: Hypothesis Testing

## ⚠️ CRITICAL: One-Tailed vs Two-Tailed Tests

```python
from scipy.stats import binomtest

# The KEY function for hypothesis testing in this course
# binomtest(k, n, p, alternative)
#   k: observed successes
#   n: number of trials
#   p: null hypothesis probability
#   alternative: 'greater', 'less', or 'two-sided'

n = 12
observed_k = 10
p_null = 0.5

print("HYPOTHESIS TESTING WITH binomtest()")
print("="*50)

# One-tailed test (upper): Is p GREATER than 0.5?
result_greater = binomtest(k=observed_k, n=n, p=p_null, alternative='greater')
print(f"\n1. One-tailed (Hₐ: p > 0.5):")
print(f"   p-value = {result_greater.pvalue:.5f}")

# One-tailed test (lower): Is p LESS than 0.5?
result_less = binomtest(k=observed_k, n=n, p=p_null, alternative='less')
print(f"\n2. One-tailed (Hₐ: p < 0.5):")
print(f"   p-value = {result_less.pvalue:.5f}")

# Two-tailed test: Is p DIFFERENT from 0.5?
result_two = binomtest(k=observed_k, n=n, p=p_null, alternative='two-sided')
print(f"\n3. Two-tailed (Hₐ: p ≠ 0.5):")
print(f"   p-value = {result_two.pvalue:.5f}")

# Decision at α = 0.05
alpha = 0.05
print(f"\nDecision at α = {alpha}:")
print(f"  One-tailed (upper): {'REJECT H₀' if result_greater.pvalue < alpha else 'Fail to reject H₀'}")
print(f"  Two-tailed: {'REJECT H₀' if result_two.pvalue < alpha else 'Fail to reject H₀'}")
```

## Worked Example: One-Tailed vs Two-Tailed Hypothesis Test

```python
# Worked example: Is the new variant MORE infectious?
print("="*70)
print("WORKED EXAMPLE: Is the new variant MORE infectious?")
print("="*70)

# Data
n = 11  # contacts
observed = 9  # infections
p_old = 0.50  # old variant rate

print(f"\nData: {observed} infections out of {n} contacts")
print(f"Old variant rate: p = {p_old}")

# CORRECT: One-tailed test (because question asks "MORE infectious")
print("\n" + "-"*70)
print("✓ CORRECT: One-tailed test (alternative='greater')")
print("-"*70)
print("H₀: p ≤ 0.50 (not more infectious)")
print("Hₐ: p > 0.50 (MORE infectious)")

result_correct = binomtest(k=observed, n=n, p=p_old, alternative='greater')
print(f"\np-value = {result_correct.pvalue:.5f}")
print(f"Since {result_correct.pvalue:.3f} < 0.05: REJECT H₀")
print("→ Evidence supports new variant IS more infectious")

# WRONG: Two-tailed test
print("\n" + "-"*70)
print("✗ WRONG: Two-tailed test (alternative='two-sided')")
print("-"*70)

result_wrong = binomtest(k=observed, n=n, p=p_old, alternative='two-sided')
print(f"p-value = {result_wrong.pvalue:.5f}")
print(f"Since {result_wrong.pvalue:.3f} > 0.05: Would FAIL to reject H₀")
print("→ This gives the WRONG conclusion!")

print("\n" + "="*70)
print("KEY: Match test type to research question!")
print("  'MORE infectious' → One-tailed (greater)")
print("  'DIFFERENT' → Two-tailed")
print("="*70)
```

## Manual p-Value Calculation

```python
# Understanding p-value by calculating manually
n = 12
p_null = 0.5
observed_k = 10

k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p_null)

# One-tailed (upper): P(X >= observed)
p_value_upper = sum(probabilities[k_values >= observed_k])
print(f"One-tailed p-value = P(X ≥ {observed_k}) = {p_value_upper:.5f}")

# Two-tailed: Include equally extreme values from both tails
lower_extreme = n - observed_k  # Symmetric point
p_value_lower = sum(probabilities[k_values <= lower_extreme])
p_value_two_tailed = p_value_upper + p_value_lower
print(f"Two-tailed p-value = {p_value_upper:.5f} + {p_value_lower:.5f} = {p_value_two_tailed:.5f}")
```

## Visualizing p-Value and Rejection Region

```python
# Visualize one-tailed test
n = 11
p_null = 0.5
observed_k = 9

k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p_null)

# Color: red for p-value region
colors = ['coral' if k >= observed_k else 'steelblue' for k in k_values]

plt.figure(figsize=(10, 6))
plt.bar(k_values, probabilities, color=colors, edgecolor='black', alpha=0.7)

# Calculate p-value
p_value = sum(probabilities[k_values >= observed_k])
plt.text(0.02, 0.95, f'p-value = P(X ≥ {observed_k}) = {p_value:.4f}',
         transform=plt.gca().transAxes, fontsize=12,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.xlabel('k (Number of Successes)')
plt.ylabel('P(X = k) under H₀')
plt.title(f'One-Tailed Test: H₀: p ≤ {p_null} vs Hₐ: p > {p_null}\n(Red = p-value region)')
plt.xticks(k_values)
plt.grid(axis='y', alpha=0.3)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='coral', label='p-value region'),
                   Patch(facecolor='steelblue', label='Not in p-value')]
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.show()
```

## Finding Critical Values

```python
# Find the rejection region boundary
n = 20
p_null = 0.40
alpha = 0.05

print(f"Finding critical value for one-tailed test (upper)")
print(f"H₀: p ≤ {p_null}, α = {alpha}")
print("-"*40)

print("\n  k    P(X ≥ k)    Reject?")
critical_value = None
for k in range(5, 16):
    result = binomtest(k=k, n=n, p=p_null, alternative='greater')
    reject = "YES" if result.pvalue < alpha else "NO"
    marker = " ← Critical value" if result.pvalue < alpha and critical_value is None else ""
    if result.pvalue < alpha and critical_value is None:
        critical_value = k
    print(f"  {k:2d}   {result.pvalue:.5f}     {reject}{marker}")

print(f"\nCritical value: k* = {critical_value}")
print(f"Reject H₀ if observed ≥ {critical_value}")
```

---

# Week 11: Trigonometry

## Unit Circle Values

```python
# Key angles
angles_deg = [0, 30, 45, 60, 90, 120, 135, 150, 180]
angles_rad = np.radians(angles_deg)

print("θ (deg)  |  θ (rad)  |  sin(θ)  |  cos(θ)")
print("-" * 50)
for deg, rad in zip(angles_deg, angles_rad):
    print(f"{deg:7d}  |  {rad:7.4f}  |  {np.sin(rad):7.4f}  |  {np.cos(rad):7.4f}")
```

## Trigonometric Functions

```python
x = np.linspace(0, 4*np.pi, 500)

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# Sine
axes[0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0].set_title('y = sin(x)')
axes[0].set_ylabel('y')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='k', linewidth=0.5)

# Cosine
axes[1].plot(x, np.cos(x), 'r-', linewidth=2)
axes[1].set_title('y = cos(x)')
axes[1].set_ylabel('y')
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=0, color='k', linewidth=0.5)

# Tangent (with asymptotes)
y_tan = np.tan(x)
y_tan[np.abs(y_tan) > 10] = np.nan  # Hide near asymptotes
axes[2].plot(x, y_tan, 'g-', linewidth=2)
axes[2].set_title('y = tan(x)')
axes[2].set_xlabel('x')
axes[2].set_ylabel('y')
axes[2].set_ylim(-5, 5)
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()
```

## Sinusoidal Transformations

```python
x = np.linspace(0, 4*np.pi, 500)

# y = A·sin(Bx + C) + D
A = 2       # Amplitude
B = 2       # Frequency multiplier (period = 2π/B)
C = np.pi/4 # Phase shift
D = 1       # Vertical shift

y = A * np.sin(B*x + C) + D

plt.figure(figsize=(12, 6))
plt.plot(x, np.sin(x), 'b--', alpha=0.5, label='y = sin(x)')
plt.plot(x, y, 'r-', linewidth=2, 
         label=f'y = {A}sin({B}x + π/4) + {D}')

plt.axhline(y=D, color='g', linestyle=':', alpha=0.5, label=f'Midline y={D}')
plt.axhline(y=D+A, color='orange', linestyle=':', alpha=0.5, label=f'Max y={D+A}')
plt.axhline(y=D-A, color='orange', linestyle=':', alpha=0.5, label=f'Min y={D-A}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sinusoidal Transformations')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Amplitude: {A}")
print(f"Period: {2*np.pi/B:.4f}")
print(f"Phase shift: {-C/B:.4f}")
print(f"Vertical shift: {D}")
```

---

# Week 12: Linear Programming

## Graphical LP Solution

```python
from scipy.optimize import linprog

# Problem: Maximize Z = 3x + 4y
# Subject to: x + y ≤ 10
#            2x + y ≤ 16
#            x, y ≥ 0

# For linprog, we minimize, so negate coefficients
c = [-3, -4]  # Minimize -Z = Maximize Z

# Inequality constraints (Ax ≤ b)
A_ub = [[1, 1], [2, 1]]
b_ub = [10, 16]

# Variable bounds
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A_ub, b_ub=b_ub, 
                 bounds=[x_bounds, y_bounds], method='highs')

print(f"Optimal solution: x = {result.x[0]:.2f}, y = {result.x[1]:.2f}")
print(f"Maximum Z = {-result.fun:.2f}")

# Graphical visualization
x = np.linspace(0, 12, 100)

# Constraint lines
y1 = 10 - x      # x + y = 10
y2 = 16 - 2*x    # 2x + y = 16

plt.figure(figsize=(10, 8))

# Plot constraints
plt.plot(x, y1, 'b-', label='x + y ≤ 10')
plt.plot(x, y2, 'r-', label='2x + y ≤ 16')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# Fill feasible region
y_upper = np.minimum(y1, y2)
y_upper = np.maximum(y_upper, 0)
plt.fill_between(x[x <= 8], y_upper[x <= 8], 0, 
                 where=(y_upper[x <= 8] >= 0), 
                 alpha=0.3, color='green', label='Feasible Region')

# Corner points
corners = [(0, 0), (8, 0), (6, 4), (0, 10)]
for (cx, cy) in corners:
    plt.scatter([cx], [cy], color='red', s=100, zorder=5)
    z = 3*cx + 4*cy
    plt.annotate(f'({cx},{cy})\nZ={z}', xy=(cx, cy), 
                 xytext=(cx+0.3, cy+0.3))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Programming: Maximize Z = 3x + 4y')
plt.legend()
plt.xlim(-1, 12)
plt.ylim(-1, 12)
plt.grid(True, alpha=0.3)
plt.show()
```

## Systems of Equations

```python
import numpy as np

# Solve: 2x + 3y = 12
#        4x - y = 5

A = np.array([[2, 3], [4, -1]])
b = np.array([12, 5])

solution = np.linalg.solve(A, b)
print(f"Solution: x = {solution[0]:.4f}, y = {solution[1]:.4f}")

# Verify
print(f"\nVerification:")
print(f"2({solution[0]:.4f}) + 3({solution[1]:.4f}) = {2*solution[0] + 3*solution[1]:.4f}")
print(f"4({solution[0]:.4f}) - ({solution[1]:.4f}) = {4*solution[0] - solution[1]:.4f}")
```

---

<div align="center">

---

# 🐍 End of Code Reference 🐍

---

**Happy Coding!**

*SCIE1500: Analytical Methods for Scientists*

---

</div>
