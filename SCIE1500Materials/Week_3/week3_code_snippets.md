# Week 3 Code Snippets: Logistic Functions and Bounded Growth

**Theme:** "When Growth Has Limits"  
**Prerequisites:** `numpy`, `matplotlib`, `scipy` (optional for curve fitting)

> **Connection to Future Content:** Mastering these growth models is key to understanding subsequent optimization (Weeks 4-5), predator-prey dynamics (Week 8), and constrained decision-making (Week 12).

---

## Snippet 1: Logistic Growth Curve

**Purpose:** Plot a logistic population trajectory showing the S-curve shape and carrying capacity.

```python
import numpy as np
import matplotlib.pyplot as plt

# Logistic function parameters
K = 15000      # Carrying capacity
A = 120        # Initial condition parameter
alpha = 0.15   # Growth rate

# Time array
t = np.linspace(0, 80, 500)

# Logistic function: P(t) = K / (1 + A * exp(-alpha * t))
P = K / (1 + A * np.exp(-alpha * t))

# Calculate inflection point (where P = K/2)
t_inflection = np.log(A) / alpha
P_inflection = K / 2

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t, P, 'b-', linewidth=2, label='Logistic Growth')
plt.axhline(y=K, color='r', linestyle='--', linewidth=1.5, label=f'Carrying Capacity K = {K}')
plt.axhline(y=K/2, color='g', linestyle=':', linewidth=1.5, label=f'Inflection Point P = K/2 = {K/2}')
plt.scatter([t_inflection], [P_inflection], color='green', s=100, zorder=5)
plt.annotate(f't ≈ {t_inflection:.1f}', (t_inflection, P_inflection), 
             xytext=(t_inflection+5, P_inflection-1000), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='green'))

plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Population P(t)', fontsize=12)
plt.title('Logistic Growth: P(t) = K / (1 + Ae^{-αt})', fontsize=14)
plt.legend(loc='right')
plt.grid(True, alpha=0.3)
plt.xlim(0, 80)
plt.ylim(0, 16000)
plt.tight_layout()
plt.show()

print(f"Parameters: K = {K}, A = {A}, α = {alpha}")
print(f"Initial population P(0) = {K/(1+A):.1f}")
print(f"Inflection point at t = {t_inflection:.2f} years")
```

**Expected Output:** S-curve showing population approaching carrying capacity with inflection point marked.

---

## Snippet 2: Schaefer Fish Growth Model

**Purpose:** Visualize the Schaefer growth function $G(S) = gS(1 - S/K)$ and identify MSY.

```python
import numpy as np
import matplotlib.pyplot as plt

# Schaefer model parameters
g = 0.1        # Intrinsic growth rate
K = 12000      # Carrying capacity (tonnes)

# Stock levels
S = np.linspace(0, K, 500)

# Schaefer growth function: G(S) = g * S * (1 - S/K)
G = g * S * (1 - S/K)

# Maximum Sustainable Yield calculations
S_MSY = K / 2
G_MSY = g * K / 4

# Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: Growth vs Stock
ax1.plot(S, G, 'b-', linewidth=2, label='Growth G(S)')
ax1.scatter([S_MSY], [G_MSY], color='red', s=150, zorder=5, label=f'MSY at S = {S_MSY}')
ax1.axvline(x=S_MSY, color='red', linestyle='--', alpha=0.5)
ax1.axhline(y=G_MSY, color='red', linestyle='--', alpha=0.5)
ax1.fill_between(S, G, where=(G > 0), alpha=0.2, color='blue')
ax1.set_xlabel('Stock S (tonnes)', fontsize=12)
ax1.set_ylabel('Growth G(S) (tonnes/year)', fontsize=12)
ax1.set_title('Schaefer Growth Model: G(S) = gS(1 - S/K)', fontsize=14)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, K)
ax1.set_ylim(-50, G_MSY + 50)

# Annotate key values
ax1.annotate(f'MSY = {G_MSY:.0f} tonnes/year', (S_MSY, G_MSY), 
             xytext=(S_MSY + 1000, G_MSY + 30), fontsize=10)

# Right plot: Actual growth rate vs Stock
growth_rate = g * (1 - S/K)
ax2.plot(S, growth_rate * 100, 'g-', linewidth=2, label='Actual Growth Rate')
ax2.axhline(y=g*100, color='orange', linestyle='--', label=f'Intrinsic rate g = {g*100}%')
ax2.set_xlabel('Stock S (tonnes)', fontsize=12)
ax2.set_ylabel('Growth Rate G(S)/S (%)', fontsize=12)
ax2.set_title('Actual Growth Rate Declines Linearly', fontsize=14)
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, K)
ax2.set_ylim(-2, g*100 + 2)

plt.tight_layout()
plt.show()

print(f"\nSchaefer Model Summary:")
print(f"  Intrinsic growth rate g = {g}")
print(f"  Carrying capacity K = {K} tonnes")
print(f"  MSY stock level S_MSY = K/2 = {S_MSY} tonnes")
print(f"  MSY harvest G_MSY = gK/4 = {G_MSY} tonnes/year")
```

**Expected Output:** Two plots: parabolic growth curve with MSY marked, and linear decline in growth rate.

---

## Snippet 3: Exponential vs Logistic Growth Comparison

**Purpose:** Compare unbounded exponential growth with bounded logistic growth—showing why model choice matters.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 10000      # Carrying capacity (logistic)
P0 = 100       # Initial population (both models)
g = 0.2        # Growth rate (both models)
A = (K - P0) / P0  # Parameter for logistic

# Time array
t = np.linspace(0, 50, 500)

# Exponential growth: P(t) = P0 * exp(g*t)
P_exp = P0 * np.exp(g * t)

# Logistic growth: P(t) = K / (1 + A * exp(-g*t))
P_log = K / (1 + A * np.exp(-g * t))

# Create the plot
plt.figure(figsize=(12, 6))

plt.plot(t, P_exp, 'r-', linewidth=2, label='Exponential (Unbounded)')
plt.plot(t, P_log, 'b-', linewidth=2, label='Logistic (Bounded)')
plt.axhline(y=K, color='green', linestyle='--', linewidth=1.5, label=f'Carrying Capacity K = {K}')

# Shaded region showing divergence
idx = P_exp < 50000
plt.fill_between(t[idx], P_exp[idx], P_log[idx], alpha=0.2, color='purple', label='Divergence Region')

plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Population P(t)', fontsize=12)
plt.title('Why Bounded Growth Models Matter: Exponential vs Logistic', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.xlim(0, 50)
plt.ylim(0, 50000)

# Add annotation
plt.annotate('Exponential:\nUnrealistic for\nreal populations!', 
             xy=(35, P_exp[350]), xytext=(25, 35000),
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('Logistic:\nApproaches\ncarrying capacity', 
             xy=(45, K), xytext=(30, 15000),
             fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))

plt.tight_layout()
plt.show()

print("Model Comparison at t = 50:")
print(f"  Exponential: P(50) = {P_exp[-1]:,.0f}")
print(f"  Logistic: P(50) = {P_log[-1]:,.0f}")
print(f"\nThe exponential model predicts {P_exp[-1]/P_log[-1]:.1f}x the logistic prediction!")
```

**Expected Output:** Plot showing exponential growth diverging while logistic approaches carrying capacity.

---

## Snippet 4: Sustainable Yield Analysis Table

**Purpose:** Generate a table showing growth and sustainable yield at different stock levels.

```python
import numpy as np
import pandas as pd

# Schaefer model parameters
g = 0.1        # Intrinsic growth rate
K = 12000      # Carrying capacity (tonnes)

# Stock levels to analyze
stock_levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

# Calculate growth and related metrics
results = []
for S in stock_levels:
    compensating_factor = 1 - S/K
    growth = g * S * compensating_factor
    growth_rate = g * compensating_factor * 100  # as percentage
    results.append({
        'Stock S (tonnes)': S,
        '(1 - S/K)': f"{compensating_factor:.3f}",
        'Growth G(S) (tonnes/yr)': f"{growth:.1f}",
        'Growth Rate (%)': f"{growth_rate:.2f}"
    })

# Create DataFrame
df = pd.DataFrame(results)

print("="*70)
print("SUSTAINABLE YIELD ANALYSIS - SCHAEFER MODEL")
print(f"Parameters: g = {g}, K = {K}")
print("="*70)
print(df.to_string(index=False))
print("="*70)

# Find MSY
S_MSY = K / 2
G_MSY = g * K / 4
print(f"\nMaximum Sustainable Yield (MSY):")
print(f"  Optimal stock level: S_MSY = {S_MSY} tonnes")
print(f"  Maximum sustainable harvest: G_MSY = {G_MSY} tonnes/year")
print(f"\nNote: Harvesting {G_MSY} tonnes/year maintains stock at {S_MSY} tonnes forever.")
```

**Expected Output:** Table showing sustainable yield at different stock levels with MSY highlighted.

---

## Snippet 5: Fitting Logistic Curve to Real Data

**Purpose:** Demonstrate how to fit logistic parameters to observed population data.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the logistic function
def logistic(t, K, A, alpha):
    return K / (1 + A * np.exp(-alpha * t))

# Simulated "observed" data (e.g., fish stock measurements)
np.random.seed(42)
t_data = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
# True parameters: K=1000, A=99, alpha=0.15
true_values = 1000 / (1 + 99 * np.exp(-0.15 * t_data))
P_data = true_values + np.random.normal(0, 30, len(t_data))  # Add noise

# Fit the logistic curve
initial_guess = [800, 50, 0.1]  # Initial parameter guesses
popt, pcov = curve_fit(logistic, t_data, P_data, p0=initial_guess, maxfev=10000)
K_fit, A_fit, alpha_fit = popt

# Generate fitted curve
t_fit = np.linspace(0, 55, 200)
P_fit = logistic(t_fit, K_fit, A_fit, alpha_fit)

# Calculate initial population from fitted parameters
P0_fit = K_fit / (1 + A_fit)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(t_data, P_data, color='red', s=100, label='Observed Data', zorder=5)
plt.plot(t_fit, P_fit, 'b-', linewidth=2, label='Fitted Logistic Curve')
plt.axhline(y=K_fit, color='green', linestyle='--', 
            label=f'Estimated K = {K_fit:.0f}')

plt.xlabel('Time (years)', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.title('Fitting Logistic Function to Population Data', fontsize=14)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.xlim(0, 55)
plt.ylim(0, 1100)

plt.tight_layout()
plt.show()

print("Fitted Parameters:")
print(f"  Carrying capacity K = {K_fit:.2f}")
print(f"  Parameter A = {A_fit:.2f}")
print(f"  Growth rate α = {alpha_fit:.4f}")
print(f"  Implied initial population P(0) = {P0_fit:.2f}")
print(f"\nTrue parameters: K=1000, A=99, α=0.15, P(0)=10")
```

**Expected Output:** Scatter plot with fitted logistic curve and estimated parameters.

---

## Snippet 6: Interactive MSY Exploration

**Purpose:** Explore how different parameter values affect MSY in the Schaefer model.

```python
import numpy as np
import matplotlib.pyplot as plt

# Create figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Common stock range
S = np.linspace(0, 15000, 500)

# Panel 1: Effect of varying g (intrinsic growth rate)
ax1 = axes[0]
K = 10000  # Fixed carrying capacity
for g in [0.05, 0.10, 0.15, 0.20]:
    G = g * S * (1 - S/K)
    G[G < 0] = np.nan  # Don't show negative growth
    ax1.plot(S, G, linewidth=2, label=f'g = {g}')
ax1.set_xlabel('Stock S')
ax1.set_ylabel('Growth G(S)')
ax1.set_title(f'Effect of Growth Rate g\n(K = {K} fixed)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, K)

# Panel 2: Effect of varying K (carrying capacity)
ax2 = axes[1]
g = 0.1  # Fixed growth rate
for K in [5000, 8000, 10000, 12000]:
    G = g * S * (1 - S/K)
    G[G < 0] = np.nan
    ax2.plot(S, G, linewidth=2, label=f'K = {K}')
ax2.set_xlabel('Stock S')
ax2.set_ylabel('Growth G(S)')
ax2.set_title(f'Effect of Carrying Capacity K\n(g = {g} fixed)')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 15000)

# Panel 3: MSY values for different parameter combinations
ax3 = axes[2]
g_values = np.linspace(0.05, 0.25, 50)
K_values = [5000, 8000, 10000, 12000]
for K in K_values:
    MSY = g_values * K / 4
    ax3.plot(g_values, MSY, linewidth=2, label=f'K = {K}')
ax3.set_xlabel('Intrinsic Growth Rate g')
ax3.set_ylabel('MSY (tonnes/year)')
ax3.set_title('MSY = gK/4 for Different K')
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Key Insight: MSY = gK/4")
print("  - Doubling g doubles MSY")
print("  - Doubling K doubles MSY")
print("  - MSY always occurs at S = K/2, regardless of g")
```

**Expected Output:** Three-panel figure showing parameter sensitivity of the Schaefer model.

---

## Snippet 7: Arithmetic Sequence Visualization

**Purpose:** Visualize arithmetic sequences and their connection to linear functions.

```python
import numpy as np
import matplotlib.pyplot as plt

# Define arithmetic sequences
sequences = [
    {'a1': 2, 'd': 3, 'name': 'Increasing (d > 0)'},
    {'a1': 50, 'd': -5, 'name': 'Decreasing (d < 0)'},
    {'a1': 10, 'd': 0, 'name': 'Constant (d = 0)'}
]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, seq in zip(axes, sequences):
    a1, d = seq['a1'], seq['d']
    
    # Discrete sequence points
    n = np.arange(1, 16)  # Terms 1 to 15
    a_n = a1 + (n - 1) * d
    
    # Continuous linear function for comparison
    x = np.linspace(0.5, 15.5, 100)
    y = d * x + (a1 - d)  # Rearranged: a_n = a1 + (n-1)d = dn + (a1 - d)
    
    # Plot
    ax.plot(x, y, 'b-', alpha=0.3, linewidth=2, label='Linear function')
    ax.scatter(n, a_n, color='red', s=80, zorder=5, label='Sequence terms')
    
    ax.set_xlabel('Term number n', fontsize=11)
    ax.set_ylabel('Term value $a_n$', fontsize=11)
    ax.set_title(f"{seq['name']}\n$a_1$ = {a1}, d = {d}", fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 16)
    
    # Add formula annotation
    formula = f"$a_n = {a1} + (n-1)({d})$"
    ax.text(0.05, 0.95, formula, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat'))

plt.tight_layout()
plt.show()

# Print sequence values
print("Arithmetic Sequence Examples:")
print("="*50)
for seq in sequences:
    a1, d = seq['a1'], seq['d']
    terms = [a1 + (n-1)*d for n in range(1, 8)]
    print(f"{seq['name']}: {terms}...")
    print(f"  Formula: a_n = {a1} + (n-1)({d})")
    print()
```

**Expected Output:** Three-panel figure showing arithmetic sequences as discrete samples of linear functions.

---

## Snippet 8: Function Composition and Inverse Visualization

**Purpose:** Visualize function composition and inverse relationships.

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: Function Composition
ax1 = axes[0]

# Define functions
def f(x): return x**2
def g(x): return 2*x + 1
def fog(x): return f(g(x))  # Composition

x = np.linspace(-2, 2, 200)

ax1.plot(x, g(x), 'b-', linewidth=2, label='g(x) = 2x + 1')
ax1.plot(x, f(x), 'r-', linewidth=2, label='f(x) = x²')
ax1.plot(x, fog(x), 'g-', linewidth=2.5, label='(f∘g)(x) = (2x+1)²')

# Show composition process for x=1
x_val = 1
ax1.scatter([x_val], [g(x_val)], color='blue', s=100, zorder=5)
ax1.scatter([x_val], [fog(x_val)], color='green', s=100, zorder=5)
ax1.annotate(f'g(1)={g(1)}', (1, g(1)), xytext=(1.3, g(1)+0.5), fontsize=9)
ax1.annotate(f'f(g(1))={fog(1)}', (1, fog(1)), xytext=(1.3, fog(1)+0.5), fontsize=9)

ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.set_title('Function Composition: (f∘g)(x)', fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 12)

# Panel 2: Inverse Functions
ax2 = axes[1]

# f(x) = e^x and its inverse ln(x)
x1 = np.linspace(-2, 2, 200)
y_exp = np.exp(x1)

x2 = np.linspace(0.1, 8, 200)
y_ln = np.log(x2)

ax2.plot(x1, y_exp, 'b-', linewidth=2, label='f(x) = eˣ')
ax2.plot(x2, y_ln, 'r-', linewidth=2, label='f⁻¹(x) = ln(x)')
ax2.plot([-2, 8], [-2, 8], 'k--', alpha=0.5, label='y = x (reflection line)')

ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.set_title('Inverse Functions: eˣ and ln(x)', fontsize=12)
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-2, 8)
ax2.set_ylim(-2, 8)
ax2.set_aspect('equal')

# Panel 3: Verifying f(f⁻¹(x)) = x
ax3 = axes[2]

# Linear example: f(x) = 2x - 6, f⁻¹(x) = (x+6)/2
def f_linear(x): return 2*x - 6
def f_inv(x): return (x + 6) / 2

x = np.linspace(-4, 10, 200)

ax3.plot(x, f_linear(x), 'b-', linewidth=2, label='f(x) = 2x - 6')
ax3.plot(x, f_inv(x), 'r-', linewidth=2, label='f⁻¹(x) = (x+6)/2')
ax3.plot(x, x, 'g--', linewidth=1.5, label='f(f⁻¹(x)) = x')

# Verify composition
test_x = 4
ax3.scatter([test_x], [f_inv(test_x)], color='orange', s=100, zorder=5)
ax3.annotate(f'f⁻¹({test_x})={f_inv(test_x)}', (test_x, f_inv(test_x)), 
             xytext=(test_x+0.5, f_inv(test_x)+1), fontsize=9)

ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.set_title('Linear Function and Its Inverse', fontsize=12)
ax3.legend(loc='lower right')
ax3.grid(True, alpha=0.3)
ax3.set_xlim(-4, 10)
ax3.set_ylim(-4, 10)
ax3.set_aspect('equal')

plt.tight_layout()
plt.show()

print("Key Properties:")
print("  - (f∘g)(x) = f(g(x)): Apply g first, then f")
print("  - Inverse function reflects across y = x")
print("  - f(f⁻¹(x)) = f⁻¹(f(x)) = x")
```

**Expected Output:** Three-panel figure showing composition, exp/ln inverses, and linear function inverse.

---

## Quick Reference: Key Formulas in Code

```python
# Logistic function
def logistic(t, K, A, alpha):
    """P(t) = K / (1 + A * exp(-alpha * t))"""
    return K / (1 + A * np.exp(-alpha * t))

# Schaefer growth model
def schaefer(S, g, K):
    """G(S) = g * S * (1 - S/K)"""
    return g * S * (1 - S/K)

# MSY calculations
def msy_stock(K):
    """S_MSY = K/2"""
    return K / 2

def msy_harvest(g, K):
    """G_MSY = gK/4"""
    return g * K / 4

# Arithmetic sequence
def arithmetic_term(a1, d, n):
    """a_n = a_1 + (n-1)*d"""
    return a1 + (n - 1) * d

def arithmetic_sum(a1, d, n):
    """S_n = n/2 * (2*a_1 + (n-1)*d)"""
    return n / 2 * (2 * a1 + (n - 1) * d)
```

---

*Code snippets aligned with SCIE1500 Week 3 content and Sample Final Examination*
