<?xml version="1.0" encoding="UTF-8"?>
# Week 6: Code Snippets — SymPy for Integration

## Theme: "From Rates to Totals"

**Lab Notebook:** `SoilQualityAndIntegration.ipynb`

**Scientific Context:** Land rehabilitation, carbon sequestration, agricultural optimization

---

## W6-CS01: Setup and Imports

Import required libraries for symbolic integration and plotting.

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Enable pretty printing for mathematical expressions
sp.init_printing(use_unicode=True)

# Import plotting from sympy
from sympy.plotting import plot

# Define common symbols
x, t, C = sp.symbols('x t C')
```

> **Note:** Always run this cell first. The `init_printing()` makes SymPy output look like proper math notation.

---

## W6-CS02: Basic Indefinite Integration

Find antiderivatives using `sp.integrate()`.

```python
x = sp.symbols('x')

# Example 1: Integrate a constant
expr1 = 2
result1 = sp.integrate(expr1, x)
print(f"∫2 dx = {result1}")

# Example 2: Integrate 5x
expr2 = 5*x
result2 = sp.integrate(expr2, x)
print(f"∫5x dx = {result2}")

# Example 3: Polynomial
expr3 = 3*x**2 - 7*x + 4
result3 = sp.integrate(expr3, x)
print(f"∫(3x² - 7x + 4) dx = {result3}")
```

**Output:**
```
∫2 dx = 2*x
∫5x dx = 5*x**2/2
∫(3x² - 7x + 4) dx = x**3 - 7*x**2/2 + 4*x
```

> **Note:** SymPy omits the constant of integration (+C). Add it manually when needed.

---

## W6-CS03: Exponential and Logarithmic Integration

Integrate exponential and 1/x functions.

```python
x = sp.symbols('x')

# Exponential
print(f"∫e^x dx = {sp.integrate(sp.exp(x), x)}")
print(f"∫e^(3x) dx = {sp.integrate(sp.exp(3*x), x)}")
print(f"∫e^(-0.5x) dx = {sp.integrate(sp.exp(-0.5*x), x)}")

# Logarithmic (1/x)
print(f"∫1/x dx = {sp.integrate(1/x, x)}")
print(f"∫2/x dx = {sp.integrate(2/x, x)}")
```

**Output:**
```
∫e^x dx = exp(x)
∫e^(3x) dx = exp(3*x)/3
∫e^(-0.5x) dx = -2.0*exp(-0.5*x)
∫1/x dx = log(x)
∫2/x dx = 2*log(x)
```

> **Note:** SymPy uses `log(x)` for natural logarithm (ln). The |x| is implied.

---

## W6-CS04: Definite Integrals

Calculate definite integrals with limits.

```python
x = sp.symbols('x')

# Definite integral syntax: sp.integrate(expr, (x, lower, upper))

# Area under y = 3 from x = 4 to x = 8.5
area1 = sp.integrate(3, (x, 4, 8.5))
print(f"∫₄^8.5 3 dx = {area1}")

# Area under y = x² from x = 0 to x = 1
area2 = sp.integrate(x**2, (x, 0, 1))
print(f"∫₀^1 x² dx = {area2}")

# This confirms: parabola sweeps 1/3 of encompassing rectangle
```

**Output:**
```
∫₄^8.5 3 dx = 13.5
∫₀^1 x² dx = 1/3
```

> **Note:** Definite integrals return a number (no +C needed). Format: `(variable, lower_limit, upper_limit)`.

---

## W6-CS05: Initial Value Problems

Find specific antiderivative using initial conditions.

```python
t, C = sp.symbols('t C')

# Problem: r'(t) = -3t² + 6t, r(0) = 2  (soap bubble radius)
# Step 1: Find indefinite integral
rate = -3*t**2 + 6*t
indefinite = sp.integrate(rate, t) + C
print(f"General solution: r(t) = {indefinite}")

# Step 2: Solve for C using initial condition r(0) = 2
C_value = sp.solve(2 - indefinite.subs(t, 0), C)[0]
print(f"Constant of integration: C = {C_value}")

# Step 3: Write specific solution
specific = indefinite.subs(C, C_value)
print(f"Specific solution: r(t) = {specific}")
```

**Output:**
```
General solution: r(t) = C - t**3 + 3*t**2
Constant of integration: C = 2
Specific solution: r(t) = -t**3 + 3*t**2 + 2
```

> This three-step process works for any initial value problem.

---

## W6-CS06: Finding Maximum After Integration

Find when the integrated function reaches its maximum.

```python
t = sp.symbols('t')

# From previous: r(t) = -t³ + 3t² + 2
r = -t**3 + 3*t**2 + 2
r_prime = -3*t**2 + 6*t  # The original rate

# Maximum occurs when r'(t) = 0
critical_points = sp.solve(r_prime, t)
print(f"Critical points: t = {critical_points}")

# Evaluate r at critical points
for pt in critical_points:
    value = r.subs(t, pt)
    print(f"r({pt}) = {value}")

print(f"\nMaximum radius = {r.subs(t, 2)} cm at t = 2 seconds")
```

**Output:**
```
Critical points: t = [0, 2]
r(0) = 2
r(2) = 6

Maximum radius = 6 cm at t = 2 seconds
```

---

## W6-CS07: Plotting Areas Under Curves

Visualize definite integrals as shaded areas.

```python
import numpy as np
import matplotlib.pyplot as plt

# Plot area under y = 3 from x = 4 to x = 8.5
plt.figure(figsize=(8, 4))

# Draw the curve (horizontal line y = 3)
plt.plot([0, 10], [3, 3], 'r-', linewidth=2, label='y = 3')

# Shade the area
xfill = [4, 8.5]
yfill_lower = [0, 0]
yfill_upper = [3, 3]
plt.fill_between(xfill, yfill_lower, yfill_upper, 
                  color='lightblue', alpha=0.7, label='Area = 13.5')

# Formatting
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Under y = 3 from x = 4 to x = 8.5')
plt.xlim(0, 10)
plt.ylim(-0.5, 4)
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.show()
```

> `plt.fill_between()` requires x coordinates and y values for lower and upper boundaries.

---

## W6-CS08: Plotting Curved Areas

Shade area under polynomial curves.

```python
import numpy as np
import matplotlib.pyplot as plt

# Area under y = x² - 4x from x = 4 to x = 8.5
x_curve = np.linspace(0, 10, 200)
y_curve = x_curve**2 - 4*x_curve

plt.figure(figsize=(8, 5))

# Plot the curve
plt.plot(x_curve, y_curve, 'b-', linewidth=2, label=r'$y = x^2 - 4x$')

# Shade the area (need many points for smooth curve)
xfill = np.linspace(4, 8.5, 50)
yfill = xfill**2 - 4*xfill
plt.fill_between(xfill, 0, yfill, color='lightgreen', alpha=0.7)

# Calculate area for annotation
import sympy as sp
x = sp.symbols('x')
area = sp.integrate(x**2 - 4*x, (x, 4, 8.5))
plt.text(5.5, 20, f'Area = {float(area):.2f}', fontsize=12)

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Area Under $y = x^2 - 4x$ from $x = 4$ to $x = 8.5$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.show()
```

> For curved areas, use `np.linspace` to generate smooth boundaries.

---

## W6-CS09: Area Between Two Curves

Calculate and visualize area between two functions.

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

# Two curves: y = 8x (upper) and y = x² - 4x (lower)
upper = 8*x
lower = x**2 - 4*x

# Area = ∫(upper - lower) dx from x = 4 to x = 8.5
area = sp.integrate(upper - lower, (x, 4, 8.5))
print(f"Area between curves = {float(area):.2f}")

# Plotting
x_vals = np.linspace(0, 10, 200)
y_upper = 8 * x_vals
y_lower = x_vals**2 - 4*x_vals

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_upper, 'r-', linewidth=2, label=r'$y = 8x$')
plt.plot(x_vals, y_lower, 'b-', linewidth=2, label=r'$y = x^2 - 4x$')

# Shade area between curves
xfill = np.linspace(4, 8.5, 50)
plt.fill_between(xfill, xfill**2 - 4*xfill, 8*xfill, 
                  color='lightblue', alpha=0.7)
plt.text(5.5, 30, f'Area = {float(area):.1f}', fontsize=12)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Between Two Curves')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 10)
plt.ylim(-10, 80)
plt.show()
```

**Output:**
```
Area between curves = 154.10
```

> Area between curves = ∫(upper − lower) dx. Always subtract lower from upper.

---

## W6-CS10: Nitrogen Fertilizer Response (Agricultural Application)

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, C = sp.symbols('x C')

# y'(x) = 0.015 - 0.0001x (yield response to nitrogen)
rate = 0.015 - 0.0001*x

# Step 1: Integrate to get yield function
yield_general = sp.integrate(rate, x) + C
print(f"General yield function: y(x) = {yield_general}")

# Step 2: Apply y(0) = 1.2 (baseline yield)
C_val = sp.solve(1.2 - yield_general.subs(x, 0), C)[0]
yield_func = yield_general.subs(C, C_val)
print(f"Specific yield function: y(x) = {yield_func}")

# Step 3: Find optimal nitrogen rate (where y'(x) = 0)
opt_nitrogen = sp.solve(rate, x)[0]
max_yield = yield_func.subs(x, opt_nitrogen)
print(f"\nOptimal nitrogen: {opt_nitrogen} kg/ha")
print(f"Maximum yield: {max_yield} tonnes/ha")

# Plot
x_vals = np.linspace(0, 200, 100)
y_vals = 1.2 + 0.015*x_vals - 0.00005*x_vals**2

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, 'g-', linewidth=2)
plt.axvline(x=150, color='r', linestyle='--', label=f'Optimal N = 150 kg/ha')
plt.scatter([150], [2.325], color='r', s=100, zorder=5)
plt.xlabel('Nitrogen Application (kg/ha)')
plt.ylabel('Yield (tonnes/ha)')
plt.title('Crop Yield Response to Nitrogen Fertilizer')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Output:**
```
General yield function: y(x) = C + 0.015*x - 5.0e-5*x**2
Specific yield function: y(x) = 0.015*x - 5.0e-5*x**2 + 1.2

Optimal nitrogen: 150 kg/ha
Maximum yield: 2.325 tonnes/ha
```

> This mirrors the bioeconomic models from Week 5—integration followed by optimization.

---

## W6-CS11: Land Rehabilitation — Vegetation Recovery

Connects to Dr. Santini's land degradation lecture.

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')

# V'(t) = 8e^(-0.2t) (vegetation recovery rate, % cover/year)
rate = 8 * sp.exp(-0.2*t)

# Integrate with V(0) = 5 (initial 5% cover)
V_general = sp.integrate(rate, t)
C_val = 5 - V_general.subs(t, 0)  # Solve for constant
V_func = V_general + C_val
print(f"Vegetation function: V(t) = {V_func}")
print(f"Simplified: V(t) = {sp.simplify(V_func)}")

# Long-term limit
limit = sp.limit(V_func, t, sp.oo)
print(f"\nLong-term vegetation cover: {limit}%")

# Plot trajectory
t_vals = np.linspace(0, 30, 100)
V_vals = 45 - 40*np.exp(-0.2*t_vals)

plt.figure(figsize=(8, 5))
plt.plot(t_vals, V_vals, 'g-', linewidth=2)
plt.axhline(y=45, color='r', linestyle='--', label='Equilibrium (45%)')
plt.xlabel('Time (years)')
plt.ylabel('Vegetation Cover (%)')
plt.title('Land Rehabilitation: Vegetation Recovery')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 50)
plt.show()
```

**Output:**
```
Vegetation function: V(t) = -40.0*exp(-0.2*t) + 45.0
Simplified: V(t) = 45.0 - 40.0*exp(-0.2*t)

Long-term vegetation cover: 45%
```

> Exponential decay integration leads to finite equilibrium—the ecosystem stabilizes.

---

## W6-CS12: SymPy Plotting for Quick Visualization

Use SymPy's built-in plot function.

```python
import sympy as sp
from sympy.plotting import plot

t = sp.symbols('t')

# Soap bubble radius: r(t) = -t³ + 3t² + 2
r = -t**3 + 3*t**2 + 2

# SymPy's plot function
p = plot(r, (t, 0, 4), 
         title=r'Soap Bubble Radius: $r(t) = -t^3 + 3t^2 + 2$',
         xlabel='Time (seconds)',
         ylabel='Radius (cm)',
         show=False)

# Customize and show
p[0].line_color = 'blue'
p.show()
```

> SymPy's `plot()` is quick for symbolic expressions. Use matplotlib for more customization.

---

## Summary: Key SymPy Integration Commands

| Task | Command |
|------|---------|
| Indefinite integral | `sp.integrate(expr, x)` |
| Definite integral | `sp.integrate(expr, (x, a, b))` |
| Substitute value | `expr.subs(x, value)` |
| Solve equation | `sp.solve(equation, variable)` |
| Compute limit | `sp.limit(expr, x, sp.oo)` |
| Plot symbolic function | `from sympy.plotting import plot` |

---

*Run these snippets in Jupyter to visualize integration concepts and practice for the lab exercises.*
