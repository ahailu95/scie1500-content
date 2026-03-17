<?xml version="1.0" encoding="UTF-8"?>
# Week 12 Code Snippets: Simultaneous Equations and Linear Programming

**Theme:** Optimizing with Constraints

**Required Packages:** `numpy`, `matplotlib`, `scipy`

---

## CS01: Solving Simultaneous Equations with NumPy

Use NumPy to solve systems of linear equations using matrix methods.

```python
import numpy as np

# System of equations:
# x + y = 10
# 2x - y = 5

# Matrix form: Ax = b
# [1   1] [x]   [10]
# [2  -1] [y] = [ 5]

A = np.array([[1, 1], 
              [2, -1]])
b = np.array([10, 5])

# Solve using np.linalg.solve
solution = np.linalg.solve(A, b)

print("Solution:")
print(f"x = {solution[0]:.4f}")
print(f"y = {solution[1]:.4f}")

# Verification
print(f"\nVerification:")
print(f"x + y = {solution[0] + solution[1]:.4f} (should be 10)")
print(f"2x - y = {2*solution[0] - solution[1]:.4f} (should be 5)")
```

---

## CS02: Visualizing Two Lines and Their Intersection

Graphically show the solution to a system of linear equations.

```python
import numpy as np
import matplotlib.pyplot as plt

# Solve system: x + y = 10 and 2x - y = 5
# Rearrange to y = f(x) form:
# y = 10 - x
# y = 2x - 5

x = np.linspace(0, 10, 100)
y1 = 10 - x        # From x + y = 10
y2 = 2*x - 5       # From 2x - y = 5

# Solution point
x_sol, y_sol = 5, 5

plt.figure(figsize=(8, 6))
plt.plot(x, y1, 'b-', linewidth=2, label='$x + y = 10$')
plt.plot(x, y2, 'r-', linewidth=2, label='$2x - y = 5$')
plt.plot(x_sol, y_sol, 'go', markersize=12, label=f'Solution ({x_sol}, {y_sol})')

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Graphical Solution of Simultaneous Equations', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()
```

---

## CS03: Market Equilibrium Visualization

Plot supply and demand curves and identify equilibrium (Q39 style).

```python
import numpy as np
import matplotlib.pyplot as plt

# Demand: Qd = 100 - 2P  => P = 50 - Q/2
# Supply: Qs = -100 + 3P => P = (Q + 100)/3

Q = np.linspace(0, 60, 100)

# Inverse demand and supply (Price as function of Quantity)
P_demand = 50 - Q/2
P_supply = (Q + 100)/3

# Equilibrium: P* = 40, Q* = 20
P_star, Q_star = 40, 20
P_max = 50      # Maximum willingness to pay (where Qd = 0)
P_min = 100/3   # Minimum acceptable price (where Qs = 0)

plt.figure(figsize=(10, 7))

# Plot demand and supply curves
plt.plot(Q, P_demand, 'b-', linewidth=2.5, label='Demand: $P = 50 - Q/2$')
plt.plot(Q, P_supply, 'r-', linewidth=2.5, label='Supply: $P = (Q+100)/3$')

# Equilibrium point
plt.plot(Q_star, P_star, 'ko', markersize=10, zorder=5)
plt.annotate(f'Equilibrium\n($Q^*$={Q_star}, $P^*$={P_star})', 
             xy=(Q_star, P_star), xytext=(Q_star+8, P_star+3),
             fontsize=11, arrowprops=dict(arrowstyle='->', color='black'))

# Reference lines
plt.axhline(y=P_star, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=Q_star, color='gray', linestyle='--', alpha=0.5)

# Mark key prices
plt.plot(0, P_max, 'b^', markersize=10, label=f'$P_{{max}}$ = {P_max}')
plt.plot(0, P_min, 'rv', markersize=10, label=f'$P_{{min}}$ = {P_min:.2f}')

plt.xlabel('Quantity (Q)', fontsize=12)
plt.ylabel('Price (P)', fontsize=12)
plt.title('Market Equilibrium: Supply and Demand', fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(0, 60)
plt.ylim(0, 60)

plt.tight_layout()
plt.show()
```

---

## CS04: Consumer and Producer Surplus Visualization

Visualize CS and PS as shaded areas (exam Q39d-e).

```python
import numpy as np
import matplotlib.pyplot as plt

# Demand: P = 50 - Q/2, Supply: P = (Q + 100)/3
Q = np.linspace(0, 60, 100)
P_demand = 50 - Q/2
P_supply = (Q + 100)/3

# Equilibrium
P_star, Q_star = 40, 20
P_max, P_min = 50, 100/3

# Create Q values for shading
Q_fill = np.linspace(0, Q_star, 100)
P_demand_fill = 50 - Q_fill/2
P_supply_fill = (Q_fill + 100)/3

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left plot: Consumer Surplus
ax1 = axes[0]
ax1.plot(Q, P_demand, 'b-', linewidth=2, label='Demand')
ax1.plot(Q, P_supply, 'r-', linewidth=2, label='Supply')
ax1.fill_between(Q_fill, P_star, P_demand_fill, alpha=0.3, color='blue', label='Consumer Surplus')
ax1.axhline(y=P_star, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(x=Q_star, color='gray', linestyle='--', alpha=0.5)
ax1.plot(Q_star, P_star, 'ko', markersize=8)
ax1.set_xlabel('Quantity', fontsize=12)
ax1.set_ylabel('Price', fontsize=12)
ax1.set_title('Consumer Surplus (CS)', fontsize=14)
ax1.legend(loc='upper right')
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 55)
ax1.grid(True, alpha=0.3)

# Calculate CS
CS = 0.5 * Q_star * (P_max - P_star)
ax1.text(5, 45, f'CS = {CS:.0f}', fontsize=14, bbox=dict(boxstyle='round', facecolor='lightblue'))

# Right plot: Producer Surplus
ax2 = axes[1]
ax2.plot(Q, P_demand, 'b-', linewidth=2, label='Demand')
ax2.plot(Q, P_supply, 'r-', linewidth=2, label='Supply')
ax2.fill_between(Q_fill, P_supply_fill, P_star, alpha=0.3, color='red', label='Producer Surplus')
ax2.axhline(y=P_star, color='gray', linestyle='--', alpha=0.5)
ax2.axvline(x=Q_star, color='gray', linestyle='--', alpha=0.5)
ax2.plot(Q_star, P_star, 'ko', markersize=8)
ax2.set_xlabel('Quantity', fontsize=12)
ax2.set_ylabel('Price', fontsize=12)
ax2.set_title('Producer Surplus (PS)', fontsize=14)
ax2.legend(loc='upper right')
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 55)
ax2.grid(True, alpha=0.3)

# Calculate PS
PS = 0.5 * Q_star * (P_star - P_min)
ax2.text(5, 45, f'PS = {PS:.2f}', fontsize=14, bbox=dict(boxstyle='round', facecolor='lightcoral'))

plt.tight_layout()
plt.show()

print(f"Consumer Surplus (CS) = {CS:.2f}")
print(f"Producer Surplus (PS) = {PS:.2f}")
print(f"Total Surplus = {CS + PS:.2f}")
```

---

## CS05: Computing CS/PS Using Integration

Use SciPy integration to compute consumer and producer surplus numerically.

```python
import numpy as np
from scipy import integrate

# Inverse demand: P = D(Q) = 50 - Q/2
# Inverse supply: P = S(Q) = (Q + 100)/3

def inverse_demand(Q):
    return 50 - Q/2

def inverse_supply(Q):
    return (Q + 100)/3

# Equilibrium values
P_star = 40
Q_star = 20

# Consumer Surplus = integral of demand from 0 to Q* minus P* * Q*
area_under_demand, _ = integrate.quad(inverse_demand, 0, Q_star)
CS = area_under_demand - P_star * Q_star

print("=== Consumer Surplus ===")
print(f"Area under demand curve (0 to {Q_star}): {area_under_demand:.2f}")
print(f"Revenue rectangle (P* × Q*): {P_star * Q_star}")
print(f"Consumer Surplus = {area_under_demand:.2f} - {P_star * Q_star} = {CS:.2f}")

# Producer Surplus = P* * Q* minus integral of supply from 0 to Q*
area_under_supply, _ = integrate.quad(inverse_supply, 0, Q_star)
PS = P_star * Q_star - area_under_supply

print("\n=== Producer Surplus ===")
print(f"Revenue rectangle (P* × Q*): {P_star * Q_star}")
print(f"Area under supply curve (0 to {Q_star}): {area_under_supply:.2f}")
print(f"Producer Surplus = {P_star * Q_star} - {area_under_supply:.2f} = {PS:.2f}")

print(f"\n=== Total Welfare ===")
print(f"Total Surplus (CS + PS) = {CS + PS:.2f}")
```

---

## CS06: Linear Programming Feasible Region (Diet Problem)

Visualize the feasible region and corner points for the diet optimization problem (Q40).

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Constraints for Diet Problem:
# 4x + 5y >= 100 (Protein)
# 10x + 25y >= 400, simplified: 2x + 5y >= 80 (Energy)
# 0.8x + 0.4y >= 10, simplified: 2x + y >= 25 (Vitamin A)
# y >= 5 (Calcium)
# x >= 0, y >= 0

fig, ax = plt.subplots(figsize=(10, 8))

x = np.linspace(0, 30, 300)

# Constraint boundaries (as equations)
y_protein = (100 - 4*x) / 5      # 4x + 5y = 100
y_energy = (80 - 2*x) / 5        # 2x + 5y = 80
y_vitaminA = 25 - 2*x            # 2x + y = 25
y_calcium = np.ones_like(x) * 5  # y = 5

# Plot constraints
ax.plot(x, y_protein, 'b-', linewidth=2, label='Protein: $4x + 5y = 100$')
ax.plot(x, y_energy, 'g-', linewidth=2, label='Energy: $2x + 5y = 80$')
ax.plot(x, y_vitaminA, 'r-', linewidth=2, label='Vitamin A: $2x + y = 25$')
ax.axhline(y=5, color='purple', linewidth=2, label='Calcium: $y = 5$')

# Feasible region vertices (approximately):
vertices = np.array([
    [10, 5],      # A
    [18.75, 5],   # B (approximate)
    [10, 12],     # C
    [0, 25],      # E
])

# Shade feasible region
feasible_polygon = Polygon(vertices, alpha=0.3, color='yellow', label='Feasible Region')
ax.add_patch(feasible_polygon)

# Mark vertices
for i, (vx, vy) in enumerate(vertices):
    labels = ['A', 'B', 'C', 'E']
    ax.plot(vx, vy, 'ko', markersize=10)
    ax.annotate(f'{labels[i]} ({vx}, {vy})', xy=(vx, vy), 
                xytext=(vx+1, vy+1), fontsize=10,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax.set_xlabel('Food I (x)', fontsize=12)
ax.set_ylabel('Food II (y)', fontsize=12)
ax.set_title('LP Feasible Region: Diet Problem (Q40)', fontsize=14)
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(-1, 30)
ax.set_ylim(-1, 30)
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()
```

---

## CS07: Evaluating Objective Function at Corner Points

Compute and compare the objective function value at each vertex.

```python
import numpy as np
import matplotlib.pyplot as plt

# Corner points from the diet problem
vertices = {
    'A': (10, 5),
    'B': (18.75, 5),
    'C': (10, 12),
    'E': (0, 25)
}

# Objective function: Z = 2x + 3y (minimize cost)
def objective(x, y):
    return 2*x + 3*y

print("=== Evaluating Z = 2x + 3y at each corner ===")
print("="*50)

results = []
for label, (x, y) in vertices.items():
    z = objective(x, y)
    results.append((label, x, y, z))
    print(f"Vertex {label}: ({x:>6.2f}, {y:>5.2f}) → Z = 2({x}) + 3({y}) = {z:.2f}")

print("="*50)

# Find minimum
min_vertex = min(results, key=lambda r: r[3])
print(f"\n*** OPTIMAL SOLUTION ***")
print(f"Minimum cost at vertex {min_vertex[0]}: ({min_vertex[1]}, {min_vertex[2]})")
print(f"Minimum cost Z = ${min_vertex[3]:.2f}")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6))

labels = [r[0] for r in results]
z_values = [r[3] for r in results]
colors = ['green' if r[0] == min_vertex[0] else 'steelblue' for r in results]

bars = ax.bar(labels, z_values, color=colors, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Corner Point', fontsize=12)
ax.set_ylabel('Cost ($)', fontsize=12)
ax.set_title('Objective Function Value at Each Corner Point', fontsize=14)
ax.axhline(y=min_vertex[3], color='red', linestyle='--', alpha=0.7, label=f'Minimum = ${min_vertex[3]:.2f}')

# Add value labels on bars
for bar, z in zip(bars, z_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
            f'${z:.0f}', ha='center', fontsize=11, fontweight='bold')

ax.legend()
ax.set_ylim(0, 85)
plt.tight_layout()
plt.show()
```

---

## CS08: Sensitivity Analysis Visualization

Compare objective function values before and after cost change (Q40d).

```python
import numpy as np
import matplotlib.pyplot as plt

# Corner points
vertices = ['A (10,5)', 'B (18.75,5)', 'C (10,12)', 'E (0,25)']
coords = [(10, 5), (18.75, 5), (10, 12), (0, 25)]

# Original costs: c1 = $2, c2 = $3
# New costs: c1 = $5, c2 = $3

z_original = [2*x + 3*y for x, y in coords]
z_new = [5*x + 3*y for x, y in coords]

# Find optima
opt_orig_idx = np.argmin(z_original)
opt_new_idx = np.argmin(z_new)

print("=== Sensitivity Analysis: Food I cost $2 → $5 ===")
print("\nOriginal (Z = 2x + 3y):")
for v, z in zip(vertices, z_original):
    marker = " ← MIN" if z == min(z_original) else ""
    print(f"  {v}: ${z:.2f}{marker}")

print(f"\nNew (Z = 5x + 3y):")
for v, z in zip(vertices, z_new):
    marker = " ← MIN" if z == min(z_new) else ""
    print(f"  {v}: ${z:.2f}{marker}")

print(f"\nConclusion: Optimal vertex {'changed' if opt_orig_idx != opt_new_idx else 'unchanged'} (still {vertices[opt_new_idx].split()[0]})")
print(f"Cost increased from ${min(z_original):.2f} to ${min(z_new):.2f}")

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))

x_pos = np.arange(len(vertices))
width = 0.35

bars1 = ax.bar(x_pos - width/2, z_original, width, label='Original ($2/unit)', color='steelblue', edgecolor='black')
bars2 = ax.bar(x_pos + width/2, z_new, width, label='New ($5/unit)', color='coral', edgecolor='black')

ax.set_xlabel('Corner Point', fontsize=12)
ax.set_ylabel('Cost ($)', fontsize=12)
ax.set_title('Sensitivity Analysis: Effect of Price Change on Optimal Solution', fontsize=14)
ax.set_xticks(x_pos)
ax.set_xticklabels(vertices, fontsize=10)
ax.legend()

# Mark optimal points
ax.annotate('MIN', (opt_orig_idx - width/2, z_original[opt_orig_idx] + 2), ha='center', fontsize=9, color='blue', fontweight='bold')
ax.annotate('MIN', (opt_new_idx + width/2, z_new[opt_new_idx] + 2), ha='center', fontsize=9, color='red', fontweight='bold')

ax.set_ylim(0, 120)
plt.tight_layout()
plt.show()
```

---

## CS09: Solving LP with SciPy

Use scipy.optimize.linprog to solve the diet problem numerically.

```python
import numpy as np
from scipy.optimize import linprog

# Diet Problem LP Formulation:
# Minimize Z = 2x + 3y
# Subject to:
#   4x + 5y >= 100    (Protein)
#   10x + 25y >= 400  (Energy)
#   0.8x + 0.4y >= 10 (Vitamin A)
#   y >= 5            (Calcium)
#   x, y >= 0

# linprog uses the form: min c'x subject to A_ub @ x <= b_ub
# For >= constraints, multiply by -1 to convert to <=

# Objective: minimize 2x + 3y
c = [2, 3]

# Inequality constraints (convert >= to <=)
A_ub = [
    [-4, -5],      # Protein
    [-10, -25],    # Energy  
    [-0.8, -0.4],  # Vitamin A
    [0, -1]        # Calcium
]

b_ub = [-100, -400, -10, -5]

# Bounds: x >= 0, y >= 0
bounds = [(0, None), (0, None)]

# Solve
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

print("=== Linear Programming Solution (scipy.optimize.linprog) ===")
print(f"\nStatus: {'Optimal solution found' if result.success else 'No solution'}")
print(f"\nOptimal values:")
print(f"  Food I (x) = {result.x[0]:.4f} units")
print(f"  Food II (y) = {result.x[1]:.4f} units")
print(f"\nMinimum cost: ${result.fun:.2f}")

# Verify constraints
print("\n=== Constraint Verification ===")
x, y = result.x
print(f"Protein:   4({x:.2f}) + 5({y:.2f}) = {4*x + 5*y:.2f} >= 100 ✓" if 4*x + 5*y >= 100 - 0.01 else "✗")
print(f"Energy:    10({x:.2f}) + 25({y:.2f}) = {10*x + 25*y:.2f} >= 400 ✓" if 10*x + 25*y >= 400 - 0.01 else "✗")
print(f"Vitamin A: 0.8({x:.2f}) + 0.4({y:.2f}) = {0.8*x + 0.4*y:.2f} >= 10 ✓" if 0.8*x + 0.4*y >= 10 - 0.01 else "✗")
print(f"Calcium:   {y:.2f} >= 5 ✓" if y >= 5 - 0.01 else "✗")
```

---

## CS10: Complete Market Analysis Dashboard

Comprehensive visualization combining equilibrium, surplus, and key metrics.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Market data (Q39 style)
def demand_Q(P): return 100 - 2*P
def supply_Q(P): return -100 + 3*P
def inverse_demand(Q): return 50 - Q/2
def inverse_supply(Q): return (Q + 100)/3

# Equilibrium
P_star, Q_star = 40, 20
P_max, P_min = 50, 100/3
CS = 0.5 * Q_star * (P_max - P_star)
PS = 0.5 * Q_star * (P_star - P_min)

# Create figure with subplots
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(2, 3, figure=fig, hspace=0.3, wspace=0.3)

# Main plot: Supply and Demand with Surplus
ax1 = fig.add_subplot(gs[:, :2])
Q = np.linspace(0, 50, 100)
P_d = inverse_demand(Q)
P_s = inverse_supply(Q)

# Plot curves
ax1.plot(Q, P_d, 'b-', linewidth=2.5, label='Demand')
ax1.plot(Q, P_s, 'r-', linewidth=2.5, label='Supply')

# Shade surplus areas
Q_fill = np.linspace(0, Q_star, 100)
ax1.fill_between(Q_fill, P_star, inverse_demand(Q_fill), alpha=0.3, color='blue', label=f'CS = {CS:.0f}')
ax1.fill_between(Q_fill, inverse_supply(Q_fill), P_star, alpha=0.3, color='red', label=f'PS = {PS:.1f}')

# Mark equilibrium
ax1.plot(Q_star, P_star, 'ko', markersize=12, zorder=5)
ax1.annotate(f'Equilibrium\n($Q^*$={Q_star}, $P^*$={P_star})', 
             xy=(Q_star, P_star), xytext=(Q_star+5, P_star+5),
             fontsize=11, arrowprops=dict(arrowstyle='->', color='black'))
ax1.axhline(y=P_star, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(x=Q_star, color='gray', linestyle='--', alpha=0.5)

ax1.set_xlabel('Quantity (Q)', fontsize=12)
ax1.set_ylabel('Price (P)', fontsize=12)
ax1.set_title('Market Equilibrium with Consumer & Producer Surplus', fontsize=14)
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 55)
ax1.grid(True, alpha=0.3)

# Top right: Key metrics
ax2 = fig.add_subplot(gs[0, 2])
ax2.axis('off')
metrics_text = f"""
=== KEY METRICS ===

Equilibrium:
  P* = ${P_star}
  Q* = {Q_star} units

Price Intercepts:
  Pmax = ${P_max} (demand)
  Pmin = ${P_min:.2f} (supply)

Economic Surplus:
  CS = ${CS:.0f}
  PS = ${PS:.2f}
  Total = ${CS + PS:.2f}
"""
ax2.text(0.1, 0.9, metrics_text, transform=ax2.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Bottom right: Surplus comparison
ax3 = fig.add_subplot(gs[1, 2])
surplus_names = ['Consumer\nSurplus', 'Producer\nSurplus', 'Total\nSurplus']
surplus_values = [CS, PS, CS + PS]
colors = ['steelblue', 'coral', 'green']
bars = ax3.bar(surplus_names, surplus_values, color=colors, edgecolor='black')
ax3.set_ylabel('Value ($)', fontsize=11)
ax3.set_title('Economic Surplus Breakdown', fontsize=12)
for bar, val in zip(bars, surplus_values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
             f'${val:.1f}', ha='center', fontsize=10, fontweight='bold')

plt.suptitle('SCIE1500 Week 12: Complete Market Analysis (Q39 Style)', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()
```

---

## Summary of Code Snippets

| ID | Topic | Description |
|----|-------|-------------|
| CS01 | Simultaneous Equations | NumPy matrix solution |
| CS02 | Simultaneous Equations | Graphical intersection |
| CS03 | Market Equilibrium | Supply/demand curves |
| CS04 | Economic Surplus | CS/PS visualization |
| CS05 | Integration | Numerical CS/PS computation |
| CS06 | Linear Programming | Feasible region plot |
| CS07 | Linear Programming | Objective evaluation |
| CS08 | Sensitivity Analysis | Cost change comparison |
| CS09 | LP Solver | SciPy optimization |
| CS10 | Dashboard | Complete market analysis |

---

*Good luck on your exam!*
