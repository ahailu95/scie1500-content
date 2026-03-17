<?xml version="1.0" encoding="UTF-8"?>
# Week 4: Python Code Snippets
## Limits, Continuity, and Introduction to Derivatives

**Theme:** Measuring Instantaneous Change  
**Lab Reference:** DifferentiationUsingSciPy.ipynb

---

## Contents
1. [Lab Setup](#w4-s01-standard-imports)
2. [Limit Concept](#w4-s02-secant-to-tangent)
3. [Limit Computation](#w4-s03-numerical-limits)
4. [SciPy Differentiation](#w4-s04-cubic-splines)
5. [Tangent Line Plotting](#w4-s05-tangent-visualization)
6. [Bacterial Growth Rate](#w4-s06-bacterial-growth)
7. [Schaefer Model (Q13)](#w4-s07-schaefer-derivative)
8. [Power Rule Verification](#w4-s08-power-rule)
9. [Exponential Derivatives](#w4-s09-exponential-derivatives)
10. [Continuity Check](#w4-s10-continuity)
11. [Lab Exercise Solution](#w4-s11-lab-exercise)
12. [Finite Difference Methods](#w4-s12-finite-differences)

---

## W4-S01: Standard Imports for Week 4 {#w4-s01-standard-imports}

**Section:** Lab Setup  
**Description:** Import statements for differentiation and numerical analysis

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

# Set plot style for cleaner visuals
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 11

print("Week 4 imports ready: NumPy, Matplotlib, Pandas, SciPy CubicSpline")
```

---

## W4-S02: Visualizing Limits — Secant Lines Approaching Tangent {#w4-s02-secant-to-tangent}

**Section:** Limit Concept  
**Description:** Animate secant lines converging to the tangent line as h → 0

```python
def f(x):
    """Example function: f(x) = x²"""
    return x**2

def secant_slope(f, a, h):
    """Calculate slope of secant line through (a, f(a)) and (a+h, f(a+h))"""
    return (f(a + h) - f(a)) / h

# Point of tangency
a = 2

# Various values of h (getting smaller)
h_values = [2.0, 1.0, 0.5, 0.25, 0.1, 0.01]

# Create plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the function
x = np.linspace(0, 5, 200)
ax.plot(x, f(x), 'b-', linewidth=2, label='$f(x) = x^2$')

# Plot secant lines for each h
colors = plt.cm.Reds(np.linspace(0.3, 1, len(h_values)))
for i, h in enumerate(h_values):
    slope = secant_slope(f, a, h)
    # Secant line: y - f(a) = slope * (x - a)
    x_line = np.linspace(a - 1, a + h + 0.5, 50)
    y_line = f(a) + slope * (x_line - a)
    ax.plot(x_line, y_line, '--', color=colors[i], alpha=0.7, 
            label=f'h = {h}: slope = {slope:.3f}')
    # Mark the two points
    ax.plot([a, a+h], [f(a), f(a+h)], 'o', color=colors[i], markersize=6)

# True tangent line (derivative at x=2 is 2*2=4)
true_slope = 2 * a  # f'(x) = 2x
x_tangent = np.linspace(a - 1, a + 2.5, 50)
y_tangent = f(a) + true_slope * (x_tangent - a)
ax.plot(x_tangent, y_tangent, 'g-', linewidth=3, label=f'Tangent: slope = {true_slope:.0f}')
ax.plot(a, f(a), 'go', markersize=12, zorder=5)

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Secant Lines Approaching Tangent Line as h → 0', fontsize=14)
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(0, 5)
ax.set_ylim(0, 20)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nAs h → 0, the secant slope → derivative f'(2) = 4")
```

---

## W4-S03: Computing Limits Numerically {#w4-s03-numerical-limits}

**Section:** Limit Computation  
**Description:** Create a table showing function values approaching a limit

```python
def compute_limit_table(f, a, label='f(x)'):
    """Compute function values approaching a point from both sides.
    
    Args:
        f: function to evaluate
        a: point to approach
        label: name for the function in output
    """
    # Values approaching from the left (a⁻)
    h_left = np.array([0.1, 0.01, 0.001, 0.0001, 0.00001])
    x_left = a - h_left
    y_left = f(x_left)
    
    # Values approaching from the right (a⁺)
    h_right = np.array([0.1, 0.01, 0.001, 0.0001, 0.00001])
    x_right = a + h_right
    y_right = f(x_right)
    
    print(f"\nLimit of {label} as x → {a}")
    print("=" * 50)
    print(f"\n{'From Left (x → a⁻)':^25} | {'From Right (x → a⁺)':^25}")
    print(f"{'x':^12} {'f(x)':^12} | {'x':^12} {'f(x)':^12}")
    print("-" * 50)
    
    for i in range(len(h_left)):
        print(f"{x_left[i]:12.6f} {y_left[i]:12.6f} | {x_right[i]:12.6f} {y_right[i]:12.6f}")
    
    print("-" * 50)
    print(f"\nLeft limit ≈ {y_left[-1]:.6f}")
    print(f"Right limit ≈ {y_right[-1]:.6f}")
    
    if np.isclose(y_left[-1], y_right[-1], rtol=1e-4):
        print(f"\n✓ Limit exists: lim(x→{a}) {label} ≈ {y_left[-1]:.6f}")
    else:
        print(f"\n✗ Limit does not exist (left ≠ right)")

# Example 1: Simple polynomial
def f1(x):
    return x**2 - 3*x + 2

compute_limit_table(f1, 2, 'x² - 3x + 2')

# Example 2: The derivative definition limit
a = 3
def derivative_limit(h):
    return ((a + h)**2 - a**2) / h  # Derivative of x² at x=3

print("\n\n" + "=" * 50)
print("Derivative of f(x) = x² at x = 3 using limit definition")
print("=" * 50)

h_values = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
print(f"\n{'h':^15} {'[f(3+h) - f(3)] / h':^20}")
print("-" * 35)
for h in h_values:
    print(f"{h:15.6f} {derivative_limit(h):20.6f}")
print("\nAs h → 0, the limit → 6 = 2×3 = f'(3) ✓")
```

---

## W4-S04: Numerical Differentiation with Cubic Splines {#w4-s04-cubic-splines}

**Section:** SciPy Differentiation  
**Description:** Use scipy CubicSpline to compute derivatives numerically (from lab notebook)

```python
from scipy.interpolate import CubicSpline

# Example: Given data points, compute derivative
# Using metabolic rate vs lifespan example from lab
x_data = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
y_data = np.array([35, 28, 20, 15, 12, 10, 8.5, 7.5, 7.0])  # Hypothetical lifespan data

# Create cubic spline interpolation
cubic_spline = CubicSpline(x_data, y_data)

# Get the derivative function
derivative = cubic_spline.derivative(1)  # First derivative

# Evaluate at specific points
x_eval = np.linspace(0.5, 8, 100)
y_smooth = cubic_spline(x_eval)
dy_dx = derivative(x_eval)

# Plot both the function and its derivative
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Original function
ax1.scatter(x_data, y_data, s=100, c='red', zorder=5, label='Data points')
ax1.plot(x_eval, y_smooth, 'b-', linewidth=2, label='Cubic spline fit')
ax1.set_xlabel('Metabolic Rate (relative)', fontsize=12)
ax1.set_ylabel('Lifespan (years)', fontsize=12)
ax1.set_title('Data with Cubic Spline Interpolation', fontsize=14)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Derivative
ax2.plot(x_eval, dy_dx, 'g-', linewidth=2, label="Derivative (dy/dx)")
ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax2.set_xlabel('Metabolic Rate (relative)', fontsize=12)
ax2.set_ylabel('dLifespan/dMetabolic Rate', fontsize=12)
ax2.set_title('Rate of Change of Lifespan with Metabolic Rate', fontsize=14)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print derivative at specific point
x_point = 3.0
print(f"\nAt x = {x_point}:")
print(f"  y = {cubic_spline(x_point):.2f}")
print(f"  dy/dx = {derivative(x_point):.4f}")
print("\nInterpretation: The slope is negative, indicating")
print("lifespan decreases as metabolic rate increases.")
```

---

## W4-S05: Tangent Line Visualization {#w4-s05-tangent-visualization}

**Section:** Derivative Applications  
**Description:** Plot a function with its tangent line at a specified point

```python
def plot_tangent(f, f_prime, x0, x_range=(-3, 3), title="Function with Tangent Line"):
    """Plot a function and its tangent line at point x0.
    
    Args:
        f: the function
        f_prime: the derivative function
        x0: point of tangency
        x_range: tuple (xmin, xmax) for plotting
        title: plot title
    """
    x = np.linspace(x_range[0], x_range[1], 200)
    y = f(x)
    
    # Point of tangency
    y0 = f(x0)
    slope = f_prime(x0)
    
    # Tangent line: y - y0 = slope * (x - x0)
    y_tangent = y0 + slope * (x - x0)
    
    # Create plot
    plt.figure(figsize=(10, 7))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x)')
    plt.plot(x, y_tangent, 'r--', linewidth=2, 
             label=f'Tangent at x={x0}: y = {slope:.2f}(x - {x0}) + {y0:.2f}')
    plt.plot(x0, y0, 'ro', markersize=12, zorder=5)
    
    # Add annotation
    plt.annotate(f'({x0}, {y0:.2f})\nslope = {slope:.2f}', 
                 xy=(x0, y0), xytext=(x0 + 0.5, y0 + 2),
                 fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend(loc='best', fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='gray', linewidth=0.5)
    plt.axvline(x=0, color='gray', linewidth=0.5)
    plt.tight_layout()
    plt.show()
    
    return slope

# Example 1: Quadratic function f(x) = x² - 2x + 1
def f(x): return x**2 - 2*x + 1
def f_prime(x): return 2*x - 2

slope = plot_tangent(f, f_prime, x0=3, x_range=(-1, 5), 
                     title='$f(x) = x^2 - 2x + 1$ with Tangent at x = 3')

print(f"At x = 3: f(3) = {f(3)}, f'(3) = {f_prime(3)}")
print(f"Tangent line equation: y = {slope}(x - 3) + {f(3)} = {slope}x - {slope*3 - f(3)}")
```

---

## W4-S06: Bacterial Growth Rate Approximation {#w4-s06-bacterial-growth}

**Section:** Scientific Application  
**Description:** Compute instantaneous growth rate for bacterial population N(t) = 500e^(0.05t)

```python
# Bacterial growth model: N(t) = 500 * e^(0.05t)
def N(t):
    """Bacterial population at time t hours"""
    return 500 * np.exp(0.05 * t)

def dN_dt_exact(t):
    """Exact derivative: dN/dt = 500 * 0.05 * e^(0.05t) = 0.05 * N(t)"""
    return 25 * np.exp(0.05 * t)  # = 0.05 * N(t)

def dN_dt_approx(t, h=0.001):
    """Numerical approximation using central difference"""
    return (N(t + h) - N(t - h)) / (2 * h)

# Compare at various times
print("Bacterial Growth: N(t) = 500e^(0.05t)")
print("=" * 60)
print(f"\n{'Time (hr)':^10} {'N(t)':^12} {'dN/dt (exact)':^15} {'dN/dt (approx)':^15}")
print("-" * 60)

for t in [0, 5, 10, 20, 40]:
    print(f"{t:^10} {N(t):^12.1f} {dN_dt_exact(t):^15.3f} {dN_dt_approx(t):^15.3f}")

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

t = np.linspace(0, 50, 200)

# Population over time
ax1.plot(t, N(t), 'b-', linewidth=2)
ax1.set_xlabel('Time (hours)', fontsize=12)
ax1.set_ylabel('Population N(t)', fontsize=12)
ax1.set_title('Bacterial Population Growth', fontsize=14)
ax1.grid(True, alpha=0.3)

# Growth rate over time
ax2.plot(t, dN_dt_exact(t), 'r-', linewidth=2, label='Exact dN/dt')
ax2.plot(t[::10], [dN_dt_approx(ti) for ti in t[::10]], 'go', 
         markersize=6, label='Numerical approx', alpha=0.7)
ax2.set_xlabel('Time (hours)', fontsize=12)
ax2.set_ylabel('Growth Rate dN/dt (bacteria/hour)', fontsize=12)
ax2.set_title('Instantaneous Growth Rate', fontsize=14)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nKey insight: For exponential growth, the rate is proportional to population:")
print("dN/dt = 0.05 × N(t) — the derivative is a constant multiple of the function!")
```

---

## W4-S07: Schaefer Model Derivative Verification {#w4-s07-schaefer-derivative}

**Section:** Exam Preparation (Q13)  
**Description:** Verify derivatives of the Schaefer growth model G(S) = gS(1 - S/K)

```python
# Schaefer model parameters (from exam Q13)
g = 0.1   # intrinsic growth rate
K = 1000  # carrying capacity

def G(S):
    """Schaefer growth function"""
    return g * S * (1 - S/K)

def dG_dS_exact(S):
    """Exact derivative: dG/dS = g - 2gS/K = g(1 - 2S/K)"""
    return g * (1 - 2*S/K)

def dG_dS_numerical(S, h=0.01):
    """Numerical derivative using central difference"""
    return (G(S + h) - G(S - h)) / (2 * h)

# Verify at various stock levels
print("Schaefer Model: G(S) = gS(1 - S/K) with g=0.1, K=1000")
print("=" * 65)
print(f"\n{'Stock S':^10} {'G(S)':^12} {'dG/dS exact':^15} {'dG/dS numerical':^15}")
print("-" * 65)

for S in [0, 100, 250, 500, 750, 1000]:
    print(f"{S:^10.0f} {G(S):^12.2f} {dG_dS_exact(S):^15.4f} {dG_dS_numerical(S):^15.4f}")

# Find S* where growth is maximized (set dG/dS = 0)
S_star = K / 2
print(f"\nMaximum Sustainable Yield (MSY):")
print(f"  Set dG/dS = g(1 - 2S/K) = 0")
print(f"  Solving: S* = K/2 = {S_star:.0f} tonnes")
print(f"  G(S*) = G({S_star:.0f}) = {G(S_star):.2f} tonnes/year")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

S = np.linspace(0, K, 200)

# Growth function
ax1.plot(S, G(S), 'b-', linewidth=2)
ax1.axvline(x=S_star, color='r', linestyle='--', label=f'S* = K/2 = {S_star:.0f}')
ax1.plot(S_star, G(S_star), 'ro', markersize=12, zorder=5)
ax1.set_xlabel('Stock S (tonnes)', fontsize=12)
ax1.set_ylabel('Growth G(S) (tonnes/year)', fontsize=12)
ax1.set_title('Schaefer Growth Model', fontsize=14)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Derivative (actual growth rate)
ax2.plot(S, dG_dS_exact(S), 'g-', linewidth=2)
ax2.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax2.axvline(x=S_star, color='r', linestyle='--', label=f'S* = {S_star:.0f} (dG/dS = 0)')
ax2.plot(S_star, 0, 'ro', markersize=12, zorder=5)
ax2.set_xlabel('Stock S (tonnes)', fontsize=12)
ax2.set_ylabel('dG/dS', fontsize=12)
ax2.set_title('Rate of Change of Growth', fontsize=14)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nExam Q13 insight: The derivative tells us at what stock level")
print("growth is maximized (MSY). This occurs where dG/dS = 0.")
```

---

## W4-S08: Power Rule Verification {#w4-s08-power-rule}

**Section:** Derivative Rules  
**Description:** Numerically verify the power rule: d/dx[x^n] = nx^(n-1)

```python
def power_rule_check(n, x0, h=0.0001):
    """Verify power rule d/dx[x^n] = n*x^(n-1) at point x0"""
    
    def f(x):
        return x**n
    
    # Numerical derivative
    numerical = (f(x0 + h) - f(x0 - h)) / (2 * h)
    
    # Exact derivative using power rule
    exact = n * x0**(n - 1)
    
    return numerical, exact

print("Power Rule Verification: d/dx[x^n] = n·x^(n-1)")
print("=" * 60)

test_cases = [
    (2, 3, "x² at x=3: should give 2×3¹ = 6"),
    (3, 2, "x³ at x=2: should give 3×2² = 12"),
    (0.5, 4, "√x at x=4: should give 0.5×4^(-0.5) = 0.25"),
    (-1, 2, "1/x at x=2: should give -1×2^(-2) = -0.25"),
    (4, 1, "x⁴ at x=1: should give 4×1³ = 4"),
]

print(f"\n{'n':^6} {'x₀':^6} {'Numerical':^12} {'Exact':^12} {'Description'}")
print("-" * 60)

for n, x0, desc in test_cases:
    num, exact = power_rule_check(n, x0)
    print(f"{n:^6.1f} {x0:^6.1f} {num:^12.6f} {exact:^12.6f} {desc}")

print("\n✓ Numerical approximations match exact values (power rule verified!)")
```

---

## W4-S09: Derivative of Exponential Functions {#w4-s09-exponential-derivatives}

**Section:** Derivative Rules  
**Description:** Verify that d/dx[e^x] = e^x and d/dx[a^x] = a^x·ln(a)

```python
import numpy as np
import matplotlib.pyplot as plt

# Define exponential functions
def f_exp(x):
    return np.exp(x)

def f_2x(x):
    return 2**x

def f_10x(x):
    return 10**x

# Numerical derivative
def numerical_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x - h)) / (2 * h)

# Test d/dx[e^x] = e^x
print("Derivative of e^x")
print("=" * 50)
print(f"{'x':^10} {'e^x':^15} {'d/dx[e^x]':^15}")
print("-" * 50)
for x in [-1, 0, 1, 2, 3]:
    print(f"{x:^10} {f_exp(x):^15.4f} {numerical_derivative(f_exp, x):^15.4f}")
print("\n✓ d/dx[e^x] = e^x (the function equals its derivative!)\n")

# Test d/dx[2^x] = 2^x · ln(2)
print("\nDerivative of 2^x")
print("=" * 50)
print(f"{'x':^10} {'2^x':^12} {'d/dx[2^x]':^12} {'2^x·ln(2)':^12}")
print("-" * 50)
for x in [0, 1, 2, 3, 4]:
    exact = f_2x(x) * np.log(2)
    print(f"{x:^10} {f_2x(x):^12.4f} {numerical_derivative(f_2x, x):^12.4f} {exact:^12.4f}")
print(f"\n✓ d/dx[2^x] = 2^x · ln(2) = 2^x · {np.log(2):.4f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

x = np.linspace(-2, 3, 200)

# e^x and its derivative
ax1.plot(x, f_exp(x), 'b-', linewidth=2, label='$f(x) = e^x$')
ax1.plot(x, f_exp(x), 'r--', linewidth=2, label="$f'(x) = e^x$", alpha=0.7)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('$e^x$ is its own derivative!', fontsize=14)
ax1.legend()
ax1.set_ylim(0, 15)
ax1.grid(True, alpha=0.3)

# 2^x and its derivative
ax2.plot(x, f_2x(x), 'b-', linewidth=2, label='$f(x) = 2^x$')
ax2.plot(x, f_2x(x) * np.log(2), 'r--', linewidth=2, label="$f'(x) = 2^x \cdot \ln(2)$")
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('$d/dx[2^x] = 2^x \cdot \ln(2)$', fontsize=14)
ax2.legend()
ax2.set_ylim(0, 10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## W4-S10: Continuity Check with Piecewise Functions {#w4-s10-continuity}

**Section:** Continuity  
**Description:** Visualize continuity and discontinuity in piecewise functions

```python
import numpy as np
import matplotlib.pyplot as plt

# Example 1: Continuous piecewise function
def f_continuous(x):
    """f(x) = x² for x < 1, 2x - 1 for x ≥ 1
    Check: at x=1, left = 1², right = 2(1)-1 = 1 ✓"""
    return np.where(x < 1, x**2, 2*x - 1)

# Example 2: Discontinuous piecewise function (jump)
def f_jump(x):
    """f(x) = x² for x < 1, 2x for x ≥ 1
    Check: at x=1, left = 1, right = 2 ✗"""
    return np.where(x < 1, x**2, 2*x)

# Example 3: Removable discontinuity
def f_removable(x):
    """f(x) = (x² - 1)/(x - 1) = x + 1 for x ≠ 1"""
    # Use the simplified form but mark the hole
    return x + 1

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: Continuous
x1 = np.linspace(-1, 3, 400)
x1_left = x1[x1 < 1]
x1_right = x1[x1 >= 1]

axes[0].plot(x1_left, x1_left**2, 'b-', linewidth=2)
axes[0].plot(x1_right, 2*x1_right - 1, 'b-', linewidth=2)
axes[0].plot(1, 1, 'bo', markersize=10)  # Filled circle at junction
axes[0].set_xlabel('x', fontsize=12)
axes[0].set_ylabel('y', fontsize=12)
axes[0].set_title('Continuous at x = 1', fontsize=14)
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(-1, 3)

# Plot 2: Jump discontinuity
axes[1].plot(x1_left, x1_left**2, 'b-', linewidth=2)
axes[1].plot(x1_right, 2*x1_right, 'b-', linewidth=2)
axes[1].plot(1, 1, 'bo', markersize=10, markerfacecolor='white')  # Open circle (left limit)
axes[1].plot(1, 2, 'bo', markersize=10)  # Filled circle (right limit = value)
axes[1].annotate('Jump!', xy=(1, 1.5), fontsize=12, color='red')
axes[1].set_xlabel('x', fontsize=12)
axes[1].set_ylabel('y', fontsize=12)
axes[1].set_title('Jump Discontinuity at x = 1', fontsize=14)
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(-1, 3)

# Plot 3: Removable discontinuity
x3 = np.linspace(-1, 3, 400)
y3 = x3 + 1
axes[2].plot(x3, y3, 'b-', linewidth=2)
axes[2].plot(1, 2, 'bo', markersize=10, markerfacecolor='white')  # Hole at (1, 2)
axes[2].annotate('Hole at (1, 2)', xy=(1, 2), xytext=(1.5, 2.5),
                  fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))
axes[2].set_xlabel('x', fontsize=12)
axes[2].set_ylabel('y', fontsize=12)
axes[2].set_title('Removable Discontinuity at x = 1', fontsize=14)
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(-1, 3)

plt.tight_layout()
plt.show()

print("Continuity at x = a requires THREE conditions:")
print("  1. f(a) is defined")
print("  2. lim(x→a) f(x) exists")
print("  3. lim(x→a) f(x) = f(a)")
```

---

## W4-S11: Tangent Line for Lab Exercise: y = 3x² - 4x + 5 {#w4-s11-lab-exercise}

**Section:** Lab Exercise  
**Description:** Solve lab exercise: find tangent to y = 3x² - 4x + 5 at x = 5

```python
# Lab Exercise: Find tangent to y = 3x² - 4x + 5 at x = 5

def f(x):
    return 3*x**2 - 4*x + 5

def f_prime(x):
    """Derivative: f'(x) = 6x - 4"""
    return 6*x - 4

# Point of tangency
x0 = 5
y0 = f(x0)
slope = f_prime(x0)

print("Lab Exercise Solution")
print("="*50)
print(f"\nFunction: f(x) = 3x² - 4x + 5")
print(f"Point of tangency: x₀ = {x0}")
print(f"\nStep 1: Find f(x₀)")
print(f"  f({x0}) = 3({x0})² - 4({x0}) + 5 = {3*x0**2} - {4*x0} + 5 = {y0}")
print(f"\nStep 2: Find f'(x₀)")
print(f"  f'(x) = 6x - 4")
print(f"  f'({x0}) = 6({x0}) - 4 = {slope}")
print(f"\nStep 3: Write tangent line equation")
print(f"  y - {y0} = {slope}(x - {x0})")
print(f"  y = {slope}x - {slope*x0} + {y0}")
print(f"  y = {slope}x + {y0 - slope*x0}")

# Verify using numerical derivative
h = 0.0001
numerical_slope = (f(x0 + h) - f(x0 - h)) / (2*h)
print(f"\nVerification: Numerical derivative = {numerical_slope:.4f} ✓")

# Plot
x = np.linspace(0, 8, 200)
y = f(x)
y_tangent = y0 + slope * (x - x0)

plt.figure(figsize=(10, 7))
plt.plot(x, y, 'b-', linewidth=2, label='$f(x) = 3x^2 - 4x + 5$')
plt.plot(x, y_tangent, 'r--', linewidth=2, label=f'Tangent: y = {slope}x + {y0 - slope*x0}')
plt.plot(x0, y0, 'ro', markersize=12, zorder=5)
plt.annotate(f'({x0}, {y0})\nslope = {slope}', 
             xy=(x0, y0), xytext=(x0-2, y0+20),
             fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Lab Exercise: Tangent to $3x^2 - 4x + 5$ at $x = 5$', fontsize=14)
plt.legend(loc='upper left', fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 8)
plt.ylim(0, 150)
plt.tight_layout()
plt.show()
```

---

## W4-S12: Finite Difference Methods Comparison {#w4-s12-finite-differences}

**Section:** Numerical Methods  
**Description:** Compare forward, backward, and central difference approximations

```python
def f(x):
    """Test function: f(x) = sin(x)"""
    return np.sin(x)

def f_prime_exact(x):
    """Exact derivative: f'(x) = cos(x)"""
    return np.cos(x)

def forward_difference(f, x, h):
    """Forward difference: [f(x+h) - f(x)] / h"""
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    """Backward difference: [f(x) - f(x-h)] / h"""
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    """Central difference: [f(x+h) - f(x-h)] / (2h)"""
    return (f(x + h) - f(x - h)) / (2 * h)

# Test at x = π/4 where f'(x) = cos(π/4) = √2/2 ≈ 0.7071
x0 = np.pi / 4
exact = f_prime_exact(x0)

print("Comparing Finite Difference Methods")
print(f"Function: f(x) = sin(x), evaluating f'({x0:.4f}) = cos({x0:.4f}) = {exact:.6f}")
print("="*75)
print(f"\n{'h':^12} {'Forward':^15} {'Backward':^15} {'Central':^15} {'Exact':^12}")
print(f"{'':^12} {'Error':^15} {'Error':^15} {'Error':^15} {'':^12}")
print("-"*75)

for h in [0.5, 0.1, 0.01, 0.001, 0.0001]:
    fwd = forward_difference(f, x0, h)
    bwd = backward_difference(f, x0, h)
    ctr = central_difference(f, x0, h)
    
    print(f"{h:^12.5f} {fwd:^8.6f} ({abs(fwd-exact):.1e})  "
          f"{bwd:^8.6f} ({abs(bwd-exact):.1e})  "
          f"{ctr:^8.6f} ({abs(ctr-exact):.1e})  {exact:^12.6f}")

print("\nObservation: Central difference converges much faster (error ~ h²)")
print("Forward/backward have error ~ h (first-order accurate)")
print("Central difference has error ~ h² (second-order accurate)")
```

---

## Quick Reference: Derivative Rules

| Function | Derivative | Rule |
|----------|------------|------|
| $c$ (constant) | $0$ | Constant |
| $x^n$ | $nx^{n-1}$ | Power |
| $e^x$ | $e^x$ | Exponential |
| $a^x$ | $a^x \ln(a)$ | General exponential |
| $\ln(x)$ | $1/x$ | Logarithm |
| $f(x) + g(x)$ | $f'(x) + g'(x)$ | Sum |
| $cf(x)$ | $cf'(x)$ | Constant multiple |

---

*Materials for SCIE1500 Week 4 Lab — Aligned with DifferentiationUsingSciPy.ipynb*
