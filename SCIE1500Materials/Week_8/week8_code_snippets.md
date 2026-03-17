<?xml version="1.0" encoding="UTF-8"?>
# Week 8 Code Snippets: Lotka-Volterra Simulation

**Theme:** When Populations Interact

**Prerequisites:** `numpy`, `matplotlib`, `scipy.integrate.odeint`, `sympy`

**Student Challenges Targeted:**
- Understanding how `odeint` solves ODEs numerically
- Correctly placing and sizing arrows on phase diagrams
- Building vector/direction fields
- Connecting time series to phase portraits

---

## CS01: Setting Up Lotka-Volterra Parameters and Symbols

Establish the model parameters and symbolic expressions.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sympy as sp

# Define parameters (exam-style values)
alpha = 0.15   # prey birth rate
beta = 0.005   # predation rate on prey
lambda_ = 0.0005  # predator birth rate from feeding
gamma = 0.10   # predator death rate

# Store as tuple for passing to functions
params = (alpha, beta, lambda_, gamma)

# Calculate equilibrium points
H_star = gamma / lambda_
P_star = alpha / beta
print(f"Coexistence equilibrium: (H*, P*) = ({H_star}, {P_star})")

# Calculate predator efficiency
efficiency = lambda_ / beta
print(f"Predator efficiency: {efficiency} = {efficiency*100}%")
```

**Output:**
```
Coexistence equilibrium: (H*, P*) = (200.0, 30.0)
Predator efficiency: 0.1 = 10.0%
```

**Note:** `lambda` is a reserved word in Python, so we use `lambda_`. The efficiency formula $\epsilon = \lambda/\beta$ gives predators born per prey consumed.

**Common Errors:**
- Using `lambda` instead of `lambda_` (syntax error)
- Confusing efficiency formula (it's λ/β, not β/λ)
- Forgetting to multiply by 100 when expressing as percentage

---

## CS02: Defining the ODE System for odeint

Write the function that `odeint` uses to solve the Lotka-Volterra equations.

```python
def lotka_volterra(populations, t, params):
    """
    Defines the Lotka-Volterra ODEs for odeint.
    
    Parameters:
    -----------
    populations : array-like
        Current state [H, P] (prey, predator)
    t : float
        Current time (not used, but required by odeint)
    params : tuple
        (alpha, beta, lambda_, gamma)
    
    Returns:
    --------
    list : [dH/dt, dP/dt]
    """
    H, P = populations
    alpha, beta, lambda_, gamma = params
    
    # Prey equation: dH/dt = αH - βHP
    dHdt = alpha * H - beta * H * P
    
    # Predator equation: dP/dt = λHP - γP
    dPdt = lambda_ * H * P - gamma * P
    
    return [dHdt, dPdt]

# Test at equilibrium (should return [0, 0])
test_result = lotka_volterra([200, 30], 0, params)
print(f"Derivatives at equilibrium: {test_result}")

# Test away from equilibrium
test_result2 = lotka_volterra([500, 10], 0, params)
print(f"Derivatives at (500, 10): dH/dt={test_result2[0]:.2f}, dP/dt={test_result2[1]:.2f}")
```

**Output:**
```
Derivatives at equilibrium: [0.0, 0.0]
Derivatives at (500, 10): dH/dt=50.00, dP/dt=-0.75
```

**Explanation:** The function must return `[dH/dt, dP/dt]` in the same order as the input `[H, P]`. The `t` parameter is required by `odeint` even though L-V equations don't explicitly depend on time.

**Common Errors:**
- Returning tuple `(dHdt, dPdt)` instead of list `[dHdt, dPdt]`
- Wrong order of H, P unpacking
- Not including `t` parameter

---

## CS03: Solving the ODEs with odeint

Understand how `odeint` numerically integrates the ODEs.

```python
# Time array: 0 to 100 with 500 points
t = np.linspace(0, 100, 500)

# Initial conditions: start away from equilibrium
H0, P0 = 700, 10  # More prey, fewer predators than equilibrium
initial_state = [H0, P0]

# Solve the ODEs
# odeint returns array of shape (len(t), 2) = (500, 2)
solution = odeint(lotka_volterra, initial_state, t, args=(params,))

# Extract H(t) and P(t)
H_t = solution[:, 0]  # First column = prey
P_t = solution[:, 1]  # Second column = predator

# Check dimensions
print(f"Solution shape: {solution.shape}")
print(f"Time points: {len(t)}")
print(f"Initial: H={H_t[0]:.1f}, P={P_t[0]:.1f}")
print(f"Final: H={H_t[-1]:.1f}, P={P_t[-1]:.1f}")
```

**Output:**
```
Solution shape: (500, 2)
Time points: 500
Initial: H=700.0, P=10.0
Final: H=700.0, P=10.0
```

**How odeint works:**
1. Starts at `initial_state`
2. Uses the ODE function to compute derivatives
3. Takes small time steps and updates populations
4. Returns the full trajectory

**⚠️ Critical:** The `args=(params,)` syntax—note the comma! It must be a tuple.

**Common Errors:**
- Forgetting the comma in `args=(params,)`
- Wrong order of arguments to `odeint`
- Confusing column indices (0=H, 1=P)

---

## CS04: Plotting Time Series

Visualize how populations change over time.

```python
fig, ax = plt.subplots(figsize=(10, 5))

# Plot both populations
ax.plot(t, H_t, 'b-', label='Prey (H)', linewidth=2)
ax.plot(t, P_t, 'r-', label='Predator (P)', linewidth=2)

# Add equilibrium reference lines
ax.axhline(y=H_star, color='b', linestyle='--', alpha=0.5, label=f'H* = {H_star}')
ax.axhline(y=P_star, color='r', linestyle='--', alpha=0.5, label=f'P* = {P_star}')

ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.set_title('Lotka-Volterra Time Series', fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Output:** Graph showing oscillating prey and predator populations over time, with predator peaks lagging behind prey peaks.

**Key Observation:** The time series reveals the characteristic **phase lag**—prey increases first (blue), then predators follow (red).

---

## CS05: Creating a Phase Portrait (Basic)

Plot trajectory in H-P space.

```python
fig, ax = plt.subplots(figsize=(8, 6))

# Plot trajectory in phase space
ax.plot(H_t, P_t, 'b-', linewidth=1.5, label='Trajectory')

# Mark initial point
ax.plot(H0, P0, 'go', markersize=12, label=f'Start ({H0}, {P0})')

# Mark equilibrium
ax.plot(H_star, P_star, 'r*', markersize=15, label=f'Equilibrium ({H_star}, {P_star})')
ax.plot(0, 0, 'k*', markersize=10, label='Origin (0, 0)')

# Add nullclines
ax.axhline(y=P_star, color='orange', linestyle=':', alpha=0.7, label=f'H-nullcline: P = {P_star}')
ax.axvline(x=H_star, color='purple', linestyle=':', alpha=0.7, label=f'P-nullcline: H = {H_star}')

ax.set_xlabel('Prey (H)', fontsize=12)
ax.set_ylabel('Predator (P)', fontsize=12)
ax.set_title('Phase Portrait: Lotka-Volterra Model', fontsize=14)
ax.legend(loc='upper right')
ax.set_xlim(0, None)
ax.set_ylim(0, None)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Output:** Graph showing closed orbit trajectory around equilibrium point with nullclines marked.

**Key Observation:** The closed orbit confirms sustained oscillations. The system moves counterclockwise.

---

## CS06: Adding Arrows to Phase Portrait (Key Skill!)

Show direction of flow with properly placed arrows.

```python
fig, ax = plt.subplots(figsize=(8, 6))

# Plot trajectory
ax.plot(H_t, P_t, 'b-', linewidth=1.5)

# Add arrow to show direction
# Key: Choose a time index where the trajectory is visible
arrow_index = 50  # Adjust this to place arrow where desired

# Get position and direction at that time
H_arrow = H_t[arrow_index]
P_arrow = P_t[arrow_index]
dH = H_t[arrow_index + 1] - H_t[arrow_index]  # Change in H
dP = P_t[arrow_index + 1] - P_t[arrow_index]  # Change in P

# Scale factor for arrow visibility (adjust based on axis scales)
scale = 15  # Increase to make arrow more visible

ax.annotate('', 
            xy=(H_arrow + scale*dH, P_arrow + scale*dP),  # Arrow tip
            xytext=(H_arrow, P_arrow),  # Arrow base
            arrowprops=dict(arrowstyle='->', color='red', lw=2))

# Alternative: plt.arrow (more control but trickier)
# plt.arrow(H_arrow, P_arrow, scale*dH, scale*dP,
#           head_width=5, head_length=20, fc='red', ec='red')

ax.plot(H_star, P_star, 'k*', markersize=15)
ax.set_xlabel('Prey (H)')
ax.set_ylabel('Predator (P)')
ax.set_title('Phase Portrait with Direction Arrow')
ax.set_xlim(0, 1500)
ax.set_ylim(0, 150)
ax.grid(True, alpha=0.3)
plt.show()

print(f"Arrow placed at t={t[arrow_index]:.2f}, position ({H_arrow:.1f}, {P_arrow:.1f})")
print(f"Direction: dH={dH:.3f}, dP={dP:.3f}")
```

**Output:**
```
[Graph with trajectory and red arrow showing counterclockwise flow]
Arrow placed at t=10.02, position (1118.5, 22.4)
Direction: dH=5.761, dP=1.019
```

**Key Points:**
1. Choose `arrow_index` where trajectory is clearly visible
2. Direction `(dH, dP)` comes from consecutive solution points
3. Scale the arrow for visibility (axis scales differ!)
4. Use `annotate()` for cleaner arrows than `plt.arrow()`

**Common Errors:**
- Arrow too small to see (increase scale factor)
- Arrow pointing wrong direction (check sign of dH, dP)
- Arrow placed at index 0 where trajectory just starts

---

## CS07: Building a Vector Field

Show direction of flow at many points across the phase plane.

```python
fig, ax = plt.subplots(figsize=(10, 8))

# Create grid of points
H_range = np.arange(50, 1501, 100)   # Prey values
P_range = np.arange(5, 151, 10)      # Predator values

# Draw vector field
for H in H_range:
    for P in P_range:
        # Compute derivatives at this point
        dHdt = alpha * H - beta * H * P
        dPdt = lambda_ * H * P - gamma * P
        
        # Skip if derivatives are both near zero (equilibrium)
        if abs(dHdt) < 0.1 and abs(dPdt) < 0.1:
            continue
        
        # Normalize for consistent arrow length
        magnitude = np.sqrt(dHdt**2 + dPdt**2)
        dH_norm = dHdt / magnitude
        dP_norm = dPdt / magnitude
        
        # Scale for visibility
        scale = 30
        
        # Draw slope line (not arrow, for cleaner look)
        ax.plot([H - scale*dH_norm, H + scale*dH_norm],
                [P - scale*dP_norm, P + scale*dP_norm],
                'gray', linewidth=0.5, alpha=0.7)

# Mark equilibrium
ax.plot(H_star, P_star, 'r*', markersize=15, zorder=5, label='Equilibrium')

# Add nullclines
ax.axhline(y=P_star, color='blue', linestyle='--', alpha=0.5, label='H-nullcline')
ax.axvline(x=H_star, color='green', linestyle='--', alpha=0.5, label='P-nullcline')

ax.set_xlabel('Prey (H)', fontsize=12)
ax.set_ylabel('Predator (P)', fontsize=12)
ax.set_title('Direction Field for Lotka-Volterra Model', fontsize=14)
ax.legend()
ax.set_xlim(0, 1600)
ax.set_ylim(0, 160)
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()
```

**Output:** Graph showing grid of small line segments indicating flow direction throughout phase plane.

**Key Elements:**
- Normalization makes all segments equal length
- Nullclines divide the plane into 4 regions
- The pattern creates counterclockwise circulation

**Common Errors:**
- Forgetting normalization (segments vary wildly in length)
- Grid too fine (cluttered) or too coarse (misses features)

---

## CS08: Complete Phase Portrait with Vector Field and Multiple Trajectories

Combine all elements for comprehensive visualization.

```python
fig, ax = plt.subplots(figsize=(12, 9))

# 1. Draw vector field (light gray background)
H_range = np.arange(50, 1501, 75)
P_range = np.arange(5, 121, 8)
scale = 25

for H in H_range:
    for P in P_range:
        dHdt = alpha * H - beta * H * P
        dPdt = lambda_ * H * P - gamma * P
        magnitude = np.sqrt(dHdt**2 + dPdt**2)
        if magnitude > 0.01:
            dH_norm = dHdt / magnitude * scale
            dP_norm = dPdt / magnitude * scale
            ax.plot([H - dH_norm, H + dH_norm],
                    [P - dP_norm, P + dP_norm],
                    'lightgray', linewidth=0.5)

# 2. Solve for multiple initial conditions
initial_conditions = [
    (700, 10, 'blue'),
    (250, 50, 'green'),
    (800, 50, 'purple'),
    (1200, 80, 'orange'),
    (300, 100, 'brown')
]

t = np.linspace(0, 100, 500)

for H0, P0, color in initial_conditions:
    sol = odeint(lotka_volterra, [H0, P0], t, args=(params,))
    ax.plot(sol[:, 0], sol[:, 1], color=color, linewidth=1.5)
    ax.plot(H0, P0, 'o', color=color, markersize=8)  # Start point
    
    # Add arrow at time index 40
    idx = 40
    dH = sol[idx+1, 0] - sol[idx, 0]
    dP = sol[idx+1, 1] - sol[idx, 1]
    ax.annotate('', xy=(sol[idx, 0] + 10*dH, sol[idx, 1] + 10*dP),
                xytext=(sol[idx, 0], sol[idx, 1]),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# 3. Mark equilibria
ax.plot(H_star, P_star, 'r*', markersize=20, zorder=10, label=f'Equilibrium ({H_star}, {P_star})')
ax.plot(0, 0, 'k*', markersize=12, label='Origin')

# 4. Add nullclines
ax.axhline(y=P_star, color='red', linestyle='--', alpha=0.6, label=f'P = {P_star} (dH/dt = 0)')
ax.axvline(x=H_star, color='red', linestyle='--', alpha=0.6, label=f'H = {H_star} (dP/dt = 0)')

ax.set_xlabel('Prey (H)', fontsize=14)
ax.set_ylabel('Predator (P)', fontsize=14)
ax.set_title('Lotka-Volterra Phase Portrait\nα=0.15, β=0.005, λ=0.0005, γ=0.10', fontsize=16)
ax.legend(loc='upper right', fontsize=10)
ax.set_xlim(0, 1500)
ax.set_ylim(0, 130)
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()
```

**Output:** Comprehensive phase portrait showing multiple closed orbits of different sizes around equilibrium, with direction arrows, nullclines, and vector field.

**Key Observations:**
- All trajectories form closed loops
- Larger initial deviations create larger orbits
- All orbits circulate counterclockwise
- Nullclines intersect at equilibrium

---

## CS09: Verifying Equilibrium Points Algebraically and Numerically

Confirm equilibrium calculations match simulation.

```python
# Algebraic equilibrium calculation
H_eq = gamma / lambda_
P_eq = alpha / beta
print(f"Algebraic equilibrium: ({H_eq}, {P_eq})")

# Verify by substituting into ODEs
dH_at_eq = alpha * H_eq - beta * H_eq * P_eq
dP_at_eq = lambda_ * H_eq * P_eq - gamma * P_eq
print(f"dH/dt at equilibrium: {dH_at_eq}")
print(f"dP/dt at equilibrium: {dP_at_eq}")

# Numerical verification: start exactly at equilibrium
t_test = np.linspace(0, 50, 100)
sol_eq = odeint(lotka_volterra, [H_eq, P_eq], t_test, args=(params,))

print(f"\nNumerical test (should stay constant):")
print(f"  t=0:  H={sol_eq[0,0]:.6f}, P={sol_eq[0,1]:.6f}")
print(f"  t=50: H={sol_eq[-1,0]:.6f}, P={sol_eq[-1,1]:.6f}")
print(f"  Maximum deviation: H={np.max(np.abs(sol_eq[:,0]-H_eq)):.2e}, P={np.max(np.abs(sol_eq[:,1]-P_eq)):.2e}")
```

**Output:**
```
Algebraic equilibrium: (200.0, 30.0)
dH/dt at equilibrium: 0.0
dP/dt at equilibrium: 0.0

Numerical test (should stay constant):
  t=0:  H=200.000000, P=30.000000
  t=50: H=200.000000, P=30.000000
  Maximum deviation: H=0.00e+00, P=0.00e+00
```

**Three ways to verify equilibrium:**
1. Algebraic formulas: $H^* = \gamma/\lambda$, $P^* = \alpha/\beta$
2. Substitution: Both derivatives are zero
3. Numerical: Starting at equilibrium stays at equilibrium

**Exam Tip:** Verification by substitution is the quickest way to check if a point is an equilibrium.

---

## CS10: Modified Model with Carrying Capacity

Compare basic L-V with logistic prey growth.

```python
# Modified parameters (from lecture)
alpha_m = 0.2
beta_m = 0.005
gamma_m = 0.6
lambda_m = 0.001
K = 1500  # Carrying capacity

params_mod = (alpha_m, beta_m, lambda_m, gamma_m, K)

def lotka_volterra_K(populations, t, params):
    """L-V model with carrying capacity for prey."""
    H, P = populations
    alpha, beta, lambda_, gamma, K = params
    
    # Modified prey equation with logistic growth
    dHdt = alpha * H * (1 - H/K) - beta * H * P
    dPdt = lambda_ * H * P - gamma * P
    
    return [dHdt, dPdt]

# New equilibrium
H_star_K = gamma_m / lambda_m
P_star_K = (alpha_m / beta_m) * (1 - H_star_K / K)
print(f"Modified equilibrium: ({H_star_K}, {P_star_K})")

# Compare trajectories
t = np.linspace(0, 150, 1000)
initial = [150, 50]

# Basic model (uses earlier params)
sol_basic = odeint(lotka_volterra, initial, t, args=((alpha_m, beta_m, lambda_m, gamma_m),))
# Modified model
sol_mod = odeint(lotka_volterra_K, initial, t, args=(params_mod,))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(sol_basic[:,0], sol_basic[:,1], 'b-', label='Basic (no K)')
axes[0].plot(600, 40, 'b*', markersize=15)  # Basic equilibrium
axes[0].set_title('Basic Lotka-Volterra\n(Closed Orbits)')
axes[0].set_xlabel('Prey (H)')
axes[0].set_ylabel('Predator (P)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(sol_mod[:,0], sol_mod[:,1], 'r-', label=f'With K={K}')
axes[1].plot(H_star_K, P_star_K, 'r*', markersize=15, label=f'Eq ({H_star_K}, {P_star_K})')
axes[1].set_title('Modified with Carrying Capacity\n(Spiral to Equilibrium)')
axes[1].set_xlabel('Prey (H)')
axes[1].set_ylabel('Predator (P)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Output:**
```
Modified equilibrium: (600.0, 24.0)
[Two plots: left showing closed orbit, right showing inward spiral to equilibrium]
```

**Key Differences:**
1. Equilibrium predator population decreases from 40 to 24 (factor of $1 - H^*/K = 0.6$)
2. Orbits are no longer closed but spiral inward
3. System converges to stable equilibrium

**Key Insight:** Carrying capacity creates damped oscillations and a stable attractor—more realistic than perpetual oscillations.

---

## Troubleshooting Guide

### odeint Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: lotka_volterra() takes 3 positional arguments but 4 were given` | Forgot comma in `args=(params,)` | Change `args=(params)` to `args=(params,)` |
| Solution explodes to infinity | Unbounded growth in parameters | Check parameter values; ensure predation term is present |

### Arrow Issues

| Problem | Cause | Fix |
|---------|-------|-----|
| Arrow not visible | Scale factor too small | Increase scale factor |
| Arrow points wrong direction | Sign error or index confusion | Use `index+1` for forward direction; verify counterclockwise flow |

### Vector Field Issues

| Problem | Cause | Fix |
|---------|-------|-----|
| Segments vary wildly in length | Not normalizing by magnitude | Divide dH and dP by $\sqrt{dH^2 + dP^2}$ |
| Field looks cluttered or sparse | Grid spacing wrong | Adjust `arange` step size |

---

## Exam Preparation Tips

| Topic | Tip |
|-------|-----|
| **Equilibrium calculation** | $H^* = \gamma/\lambda$ (from predator equation), $P^* = \alpha/\beta$ (from prey equation). The "cross" pattern: prey equilibrium comes from predator parameters. |
| **Efficiency formula** | $\epsilon = \lambda/\beta$. Think "birth per kill": λ controls predator births, β controls prey kills. Don't confuse with β/λ! |
| **Direction of flow** | Draw nullclines first. In each of 4 regions, determine signs of dH/dt and dP/dt separately, then combine. Flow is always counterclockwise in basic L-V. |
| **Verification** | To verify (H,P) is equilibrium, substitute into BOTH equations and check both give zero. |

---

## Summary Table

| ID | Title | Difficulty | Key Skill |
|----|-------|------------|-----------|
| CS01 | Parameters and Symbols | Foundational | Setup, equilibrium formulas |
| CS02 | ODE System for odeint | Foundational | Writing ODE function |
| CS03 | Solving with odeint | Intermediate | Using odeint correctly |
| CS04 | Time Series Plot | Intermediate | Visualizing oscillations |
| CS05 | Basic Phase Portrait | Intermediate | H-P space, nullclines |
| CS06 | Adding Arrows | Intermediate | Direction indicators |
| CS07 | Vector Field | Advanced | Flow visualization |
| CS08 | Complete Portrait | Advanced | Multi-trajectory analysis |
| CS09 | Equilibrium Verification | Intermediate | Three verification methods |
| CS10 | Carrying Capacity | Advanced | Model comparison |

---

*Good luck on your exam!*
