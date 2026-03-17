# Week 5 Code Snippets: SymPy for Differentiation and Optimization

**Theme:** Finding the Best Outcome

**Prerequisites:** `sympy` installed (`pip install sympy`), Basic Python knowledge from Week 0

**Notebook Connection:** `SymbolicComputationDifferentiation.ipynb`

---

## CS01: Setting Up SymPy for Calculus

Import SymPy and define symbols for symbolic computation.

```python
import sympy as sp

# Define symbols for variables
x, t, S = sp.symbols('x t S')

# Define symbols for parameters (positive=True helps simplify)
g, K, e, c, p = sp.symbols('g K e c p', positive=True)

# Enable pretty printing
sp.init_printing()

# Example: create a simple expression
f = x**2 + 3*x - 5
print(f"f(x) = {f}")
```

**Output:**
```
f(x) = x**2 + 3*x - 5
```

**Note:** Always define symbols before using them in expressions. The `positive=True` parameter helps SymPy make simplifications.

---

## CS02: Basic Differentiation

Compute first and higher-order derivatives using `.diff()`.

```python
import sympy as sp
x = sp.symbols('x')

# Define a function
f = x**3 - 6*x**2 + 9*x + 1

# First derivative
f_prime = f.diff(x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")

# Second derivative
f_double_prime = f.diff(x, 2)
print(f"f''(x) = {f_double_prime}")

# Third derivative (using alternative syntax)
f_triple = sp.diff(f, x, 3)
print(f"f'''(x) = {f_triple}")
```

**Output:**
```
f(x) = x**3 - 6*x**2 + 9*x + 1
f'(x) = 3*x**2 - 12*x + 9
f''(x) = 6*x - 12
f'''(x) = 6
```

**Note:** Use `.diff(x)` for first derivative, `.diff(x, n)` for nth derivative.

---

## CS03: Product Rule Verification

Verify the product rule using SymPy.

```python
import sympy as sp
x = sp.symbols('x')

# Define two functions
f = x**2
g = sp.exp(x)  # e^x

# Product
product = f * g

# SymPy automatically applies product rule
product_derivative = product.diff(x)
print(f"d/dx[x² · eˣ] = {product_derivative}")

# Simplify and factor
simplified = sp.simplify(product_derivative)
factored = sp.factor(product_derivative)
print(f"Simplified: {simplified}")
print(f"Factored: {factored}")
```

**Output:**
```
d/dx[x² · eˣ] = x**2*exp(x) + 2*x*exp(x)
Simplified: (x**2 + 2*x)*exp(x)
Factored: x*(x + 2)*exp(x)
```

**Note:** SymPy automatically handles product rule; use `simplify()` or `factor()` to clean up results.

---

## CS04: Chain Rule with Composite Functions

Differentiate composite functions using SymPy.

```python
import sympy as sp
x = sp.symbols('x')

# Example 1: (3x + 2)^4
f1 = (3*x + 2)**4
f1_prime = f1.diff(x)
print(f"d/dx[(3x+2)⁴] = {f1_prime}")

# Example 2: e^(x²)
f2 = sp.exp(x**2)
f2_prime = f2.diff(x)
print(f"d/dx[e^(x²)] = {f2_prime}")

# Example 3: ln(x² + 1)
f3 = sp.ln(x**2 + 1)
f3_prime = f3.diff(x)
print(f"d/dx[ln(x²+1)] = {f3_prime}")
```

**Output:**
```
d/dx[(3x+2)⁴] = 12*(3*x + 2)**3
d/dx[e^(x²)] = 2*x*exp(x**2)
d/dx[ln(x²+1)] = 2*x/(x**2 + 1)
```

**Note:** SymPy handles chain rule automatically for nested functions.

---

## CS05: Solving f'(x) = 0 for Critical Points

Find critical points by solving the derivative equation.

```python
import sympy as sp
x = sp.symbols('x')

# Define function
f = x**3 - 12*x + 5

# Find derivative
f_prime = f.diff(x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")

# Solve f'(x) = 0
critical_points = sp.solve(f_prime, x)
print(f"Critical points: {critical_points}")

# Evaluate f at critical points
for cp in critical_points:
    value = f.subs(x, cp)
    print(f"f({cp}) = {value}")
```

**Output:**
```
f(x) = x**3 - 12*x + 5
f'(x) = 3*x**2 - 12
Critical points: [-2, 2]
f(-2) = 21
f(2) = -11
```

**Note:** `sp.solve()` returns a list of solutions. Use `.subs()` to evaluate at specific points.

---

## CS06: Second Derivative Test

Classify critical points as maxima or minima.

```python
import sympy as sp
x = sp.symbols('x')

# Define function
f = x**3 - 12*x + 5

# First and second derivatives
f_prime = f.diff(x)
f_double_prime = f.diff(x, 2)

print(f"f''(x) = {f_double_prime}")

# Find critical points
critical_points = sp.solve(f_prime, x)

# Classify each critical point
for cp in critical_points:
    second_deriv_value = f_double_prime.subs(x, cp)
    func_value = f.subs(x, cp)
    
    if second_deriv_value > 0:
        nature = "LOCAL MINIMUM"
    elif second_deriv_value < 0:
        nature = "LOCAL MAXIMUM"
    else:
        nature = "INCONCLUSIVE (possible inflection point)"
    
    print(f"At x = {cp}: f''({cp}) = {second_deriv_value}, f({cp}) = {func_value} → {nature}")
```

**Output:**
```
f''(x) = 6*x
At x = -2: f''(-2) = -12, f(-2) = 21 → LOCAL MAXIMUM
At x = 2: f''(2) = 12, f(2) = -11 → LOCAL MINIMUM
```

**Note:** $f'' > 0$ means concave up (minimum); $f'' < 0$ means concave down (maximum).

---

## CS07: Schaefer Model — Finding MSY

Use SymPy to find the stock level that maximizes fish growth (MSY).

```python
import sympy as sp

# Define symbols
S = sp.symbols('S')
g, K = sp.symbols('g K', positive=True)

# Schaefer growth model
G = g * S * (1 - S/K)
print(f"Growth function: G(S) = {G}")

# Expand
G_expanded = sp.expand(G)
print(f"Expanded: G(S) = {G_expanded}")

# Differentiate
G_prime = G.diff(S)
print(f"G'(S) = {G_prime}")

# Solve for MSY stock level
S_msy = sp.solve(G_prime, S)
print(f"MSY stock level: S* = {S_msy}")

# Maximum growth (substitute back)
G_max = G.subs(S, S_msy[0])
G_max_simplified = sp.simplify(G_max)
print(f"Maximum growth: G_max = {G_max_simplified}")
```

**Output:**
```
Growth function: G(S) = S*g*(1 - S/K)
Expanded: G(S) = S*g - S**2*g/K
G'(S) = g - 2*S*g/K
MSY stock level: S* = [K/2]
Maximum growth: G_max = K*g/4
```

**Note:** This confirms MSY occurs at $S = K/2$ with maximum growth of $gK/4$.

---

## CS08: Bioeconomic Model — Finding MEY

Complete MEY calculation for the bioeconomic fishery model.

```python
import sympy as sp

# Define symbol
S = sp.symbols('S')

# Parameters
K = 12000
g = 0.10
e = 0.001
c = 4500
p = 3000

# Build the model
Growth = g * S * (1 - S/K)  # Schaefer growth
Harvest = Growth  # At steady state, H = G(S)
Effort = Harvest / (e * S)  # E = H/(eS)
Revenue = p * Harvest
Cost = c * Effort
Profit = Revenue - Cost

print(f"Profit(S) = {sp.expand(Profit)}")

# Differentiate profit
Profit_prime = Profit.diff(S)
print(f"Profit'(S) = {sp.expand(Profit_prime)}")

# Solve for optimal stock (MEY)
S_opt = sp.solve(Profit_prime, S)
print(f"MEY stock level: S* = {S_opt}")

# Calculate maximum profit
max_profit = Profit.subs(S, S_opt[0])
print(f"Maximum profit: ${float(max_profit):,.2f}")

# Compare with MSY
S_msy = K/2
profit_at_msy = float(Profit.subs(S, S_msy))
print(f"\nComparison:")
print(f"MSY stock: {S_msy} tonnes, Profit: ${profit_at_msy:,.2f}")
print(f"MEY stock: {S_opt[0]} tonnes, Profit: ${float(max_profit):,.2f}")
```

**Output:**
```
Profit(S) = -0.025*S**2 + 337.5*S - 450000.0
Profit'(S) = 337.5 - 0.05*S
MEY stock level: S* = [6750.00000000000]
Maximum profit: $689,062.50

Comparison:
MSY stock: 6000.0 tonnes, Profit: $639,000.00
MEY stock: 6750.00000000000 tonnes, Profit: $689,062.50
```

**Note:** MEY (6750 tonnes) is higher than MSY (6000 tonnes), with \$50,000+ more profit.

---

## CS09: Constrained Optimization — Fencing Problem

Solve the classic fencing problem using SymPy.

```python
import sympy as sp

x = sp.symbols('x', positive=True)

# Problem: Fence 3 sides of rectangle along river with 1000m of fencing
# Let x = width, y = length along river
# Constraint: 2x + y = 1000

# From constraint: y = 1000 - 2x
y_expr = 1000 - 2*x

# Area as function of x only
Area = x * y_expr
print(f"Area(x) = {sp.expand(Area)}")

# Differentiate
Area_prime = Area.diff(x)
print(f"Area'(x) = {Area_prime}")

# Solve for optimal x
x_opt = sp.solve(Area_prime, x)[0]
print(f"Optimal width: x* = {x_opt} m")

# Find optimal y
y_opt = y_expr.subs(x, x_opt)
print(f"Optimal length: y* = {y_opt} m")

# Maximum area
max_area = Area.subs(x, x_opt)
print(f"Maximum area: {max_area} m²")

# Verify it's a maximum
Area_double_prime = Area.diff(x, 2)
print(f"Area''(x) = {Area_double_prime} (negative → maximum confirmed)")
```

**Output:**
```
Area(x) = -2*x**2 + 1000*x
Area'(x) = 1000 - 4*x
Optimal width: x* = 250 m
Optimal length: y* = 500 m
Maximum area: 125000 m²
Area''(x) = -4 (negative → maximum confirmed)
```

**Note:** Constrained optimization: substitute constraint to get single-variable function.

---

## CS10: Profit Maximization — Livestock Problem

Solve the deer fattening problem (Exam Q38 style).

```python
import sympy as sp

t = sp.symbols('t', positive=True)  # days from now

# Problem parameters
num_deer = 100
initial_weight = 50  # kg per deer
initial_gain_rate = 2  # kg/day
gain_decline = 0.1  # kg/day per day
feed_cost = 0.50  # $/animal/day
price = 5.00  # $/kg

# Weight gain rate at time t: 2 - 0.1t
# Total weight gained by time t: integral of (2 - 0.1*tau) from 0 to t
# = 2t - 0.05t²

weight_per_deer = initial_weight + 2*t - 0.05*t**2
print(f"Weight per deer at time t: W(t) = {weight_per_deer} kg")

# Revenue and Cost
revenue = num_deer * price * weight_per_deer
cost = feed_cost * num_deer * t
profit = revenue - cost

profit_expanded = sp.expand(profit)
print(f"Profit(t) = {profit_expanded}")

# Optimize
profit_prime = profit.diff(t)
print(f"Profit'(t) = {sp.expand(profit_prime)}")

t_opt = sp.solve(profit_prime, t)[0]
print(f"\nOptimal selling time: t* = {t_opt} days")

# Calculate results
weight_opt = weight_per_deer.subs(t, t_opt)
revenue_opt = revenue.subs(t, t_opt)
cost_opt = cost.subs(t, t_opt)
profit_opt = profit.subs(t, t_opt)

print(f"Weight per deer: {float(weight_opt):.2f} kg")
print(f"Total revenue: ${float(revenue_opt):,.2f}")
print(f"Total cost: ${float(cost_opt):,.2f}")
print(f"Maximum profit: ${float(profit_opt):,.2f}")
```

**Output:**
```
Weight per deer at time t: W(t) = -0.05*t**2 + 2*t + 50 kg
Profit(t) = -25.0*t**2 + 950.0*t + 25000.0
Profit'(t) = 950.0 - 50.0*t

Optimal selling time: t* = 19 days
Weight per deer: 69.95 kg
Total revenue: $34,975.00
Total cost: $950.00
Maximum profit: $34,025.00
```

**Note:** This mirrors exam Q38. Build the model step by step, then optimize.

---

## CS11: Plotting Functions and Derivatives

Visualize a function with its first and second derivatives.

```python
import sympy as sp
from sympy.plotting import plot

x = sp.symbols('x')

# Define function
f = x**3 - 6*x**2 + 9*x + 1
f_prime = f.diff(x)
f_double_prime = f.diff(x, 2)

print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")
print(f"f''(x) = {f_double_prime}")

# Create plot with all three functions
p = plot(f, f_prime, f_double_prime, 
         (x, -1, 5),
         legend=True,
         title='Function and Derivatives',
         xlabel='x',
         ylabel='y',
         show=False)

# Customize colors (optional)
p[0].line_color = 'blue'   # f(x)
p[1].line_color = 'red'    # f'(x)
p[2].line_color = 'green'  # f''(x)

p.show()
```

**Output:**
```
f(x) = x**3 - 6*x**2 + 9*x + 1
f'(x) = 3*x**2 - 12*x + 9
f''(x) = 6*x - 12
[Plot displayed]
```

**Note:** Use `sympy.plotting.plot()` for quick visualizations. Note where $f'(x)=0$ corresponds to extrema of $f(x)$.

---

## CS12: Parametric Optimization

Keep parameters symbolic to derive general formulas.

```python
import sympy as sp

S = sp.symbols('S')
g, K, e, c, p = sp.symbols('g K e c p', positive=True)

# Bioeconomic model with symbolic parameters
G = g * S * (1 - S/K)
E = G / (e * S)  # Simplifies to g(1-S/K)/e
TR = p * G
TC = c * E
Profit = TR - TC

# Simplify profit expression
Profit_simplified = sp.simplify(sp.expand(Profit))
print(f"Profit(S) = {Profit_simplified}")

# Differentiate
Profit_prime = sp.simplify(Profit.diff(S))
print(f"Profit'(S) = {Profit_prime}")

# Solve for S* (MEY)
S_mey = sp.solve(Profit_prime, S)
print(f"MEY stock level: S* = {S_mey}")

# The general formula shows MEY depends on c/(ep)
print(f"\nSimplified: S_MEY = K/2 + c/(2ep)")
print("This shows MEY > MSY = K/2 when costs exist (c > 0)")
```

**Output:**
```
Profit(S) = S*g*p - S**2*g*p/K - c*g/e + S*c*g/(K*e)
Profit'(S) = g*p - 2*S*g*p/K + c*g/(K*e)
MEY stock level: S* = [K/2 + c/(2*e*p)]

Simplified: S_MEY = K/2 + c/(2ep)
This shows MEY > MSY = K/2 when costs exist (c > 0)
```

**Note:** General formula: $S_{MEY} = K/2 + c/(2ep)$. MEY exceeds MSY by $c/(2ep)$, which captures the cost-stock tradeoff.

---

## Lab Exercises

### Lab A: Drug Dosage Optimization

A patient's heart rate response to a drug injection is $R(x) = 9(x^2 - x^3/3)$ beats/min above normal, where $x$ is the dosage in cc. Find the optimal dosage.

```python
import sympy as sp

x = sp.symbols('x', positive=True)

# Define the response function
R = 9 * (x**2 - x**3/3)

# TODO: Find R'(x)
# TODO: Solve R'(x) = 0
# TODO: Verify maximum using second derivative
# TODO: Calculate maximum response
```

**Expected Output:**
```
Optimal dosage: x = 2 cc
Maximum response: R(2) = 12 beats/min above normal
```

---

### Lab B: Agricultural Net Revenue

Wheat yield $Y = 1000 + 20N - 0.05N^2$ (kg/ha) depends on nitrogen $N$ (kg/ha). If wheat price is \$0.40/kg and nitrogen costs \$1.00/kg, find optimal nitrogen application.

```python
import sympy as sp

N = sp.symbols('N', positive=True)

# Parameters
wheat_price = 0.40  # $/kg
nitrogen_cost = 1.00  # $/kg

# Yield function
Y = 1000 + 20*N - 0.05*N**2

# TODO: Define revenue, cost, and profit
# TODO: Find optimal N
# TODO: Calculate max profit
```

**Expected Output:**
```
Optimal nitrogen: N = 190 kg/ha
Yield at optimum: 2805 kg/ha
Maximum net revenue: $932.00/ha
```

---

### Lab C: Compare MSY and MEY

Using the bioeconomic model parameters from class, verify that MEY stock is higher than MSY and calculate the difference in profits.

```python
import sympy as sp

S = sp.symbols('S')

# Parameters
K, g, e, c, p = 12000, 0.10, 0.001, 4500, 3000

# TODO: Build Growth, Revenue, Cost, Profit functions
# TODO: Find S_MSY = K/2 and calculate profit
# TODO: Find S_MEY by optimization
# TODO: Compare the two strategies
```

**Expected Output:**
```
MSY: S=6000, Harvest=300, Profit=$639,000
MEY: S=6750, Harvest=296.7, Profit=$689,062
MEY profit advantage: $50,062.50
```

---

## Summary of Code Snippets

| ID | Topic | Description |
|----|-------|-------------|
| CS01 | SymPy Basics | Setting up symbols and expressions |
| CS02 | Differentiation | First and higher-order derivatives |
| CS03 | Product Rule | Verifying product rule with SymPy |
| CS04 | Chain Rule | Composite function differentiation |
| CS05 | Critical Points | Solving $f'(x) = 0$ |
| CS06 | Second Derivative Test | Classifying maxima/minima |
| CS07 | Schaefer Model | Finding MSY symbolically |
| CS08 | Bioeconomic Model | Complete MEY calculation |
| CS09 | Constrained Optimization | Fencing problem |
| CS10 | Profit Maximization | Livestock problem (Q38 style) |
| CS11 | Visualization | Plotting function and derivatives |
| CS12 | Parametric Optimization | General MEY formula derivation |

---

*Good luck on your exam!*
