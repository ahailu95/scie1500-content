<?xml version="1.0" encoding="UTF-8"?>
# Week 2 Python Lab: Exponential and Logarithmic Functions

**Theme:** Modeling Unbounded Growth and Decay

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt

# Set plotting style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 12
```

---

## 1. The Number e: Limit Definition

Demonstrate how $e$ arises from the limit $(1 + 1/n)^n$ as $n \to \infty$:

```python
# Compute (1 + 1/n)^n for increasing n
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]

print("n\t\t(1 + 1/n)^n")
print("-" * 30)
for n in n_values:
    result = (1 + 1/n)**n
    print(f"{n:>10}\t{result:.10f}")

print(f"\nActual e = {np.e:.10f}")
```

---

## 2. Why e? Derivative Investigation

Show that $\frac{d}{dx}[a^x] = a^x \cdot \lim_{h\to 0}\frac{a^h-1}{h}$ and find the base where the limit equals 1:

```python
# Investigate lim(h->0) (a^h - 1)/h for different bases
h_values = [0.1, 0.01, 0.001, 0.0001, 0.00001]
bases = [2, np.e, 3]

print("h\t\t(2^h-1)/h\t(e^h-1)/h\t(3^h-1)/h")
print("-" * 60)
for h in h_values:
    results = [(a**h - 1)/h for a in bases]
    print(f"{h}\t\t{results[0]:.6f}\t{results[1]:.6f}\t{results[2]:.6f}")

print("\nNote: Only for base e does the limit equal 1!")
print(f"ln(2) = {np.log(2):.6f}, ln(3) = {np.log(3):.6f}")
```

---

## 3. Exponential Growth vs Decay

Visualize the difference between growth ($k > 0$) and decay ($k < 0$):

```python
t = np.linspace(0, 10, 100)

# Different growth/decay rates
P0 = 100
k_growth = 0.3   # Growth
k_decay = -0.3   # Decay

P_growth = P0 * np.exp(k_growth * t)
P_decay = P0 * np.exp(k_decay * t)

plt.figure(figsize=(10, 6))
plt.plot(t, P_growth, 'b-', linewidth=2, label=f'Growth: k = {k_growth}')
plt.plot(t, P_decay, 'r-', linewidth=2, label=f'Decay: k = {k_decay}')
plt.axhline(y=P0, color='gray', linestyle='--', label=f'Initial: P₀ = {P0}')

plt.xlabel('Time (t)')
plt.ylabel('Population P(t)')
plt.title('Exponential Growth vs Decay: P(t) = P₀e^{kt}')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 4. Bacteria Growth (Lecture Example)

Model bacteria population: $b(t) = 400e^{1.12567t}$

```python
def bacteria_pop(t):
    return 400 * np.exp(1.12567 * t)

t = np.linspace(0, 5, 100)

plt.figure(figsize=(10, 6))
plt.plot(t, bacteria_pop(t), 'g-', linewidth=2)

# Mark key points
t_points = [0, 1, 2, 3]
for tp in t_points:
    plt.plot(tp, bacteria_pop(tp), 'ro', markersize=8)
    plt.annotate(f'  t={tp}: {bacteria_pop(tp):.0f}', 
                 (tp, bacteria_pop(tp)), fontsize=10)

plt.xlabel('Time (hours)')
plt.ylabel('Bacteria count')
plt.title('Bacteria Growth: b(t) = 400e^{1.12567t}')
plt.grid(True)
plt.show()

# Calculate doubling time
doubling_time = np.log(2) / 1.12567
print(f"\nDoubling time: {doubling_time:.3f} hours ({doubling_time*60:.1f} minutes)")
```

---

## 5. Logarithm as Inverse of Exponential

Visualize the inverse relationship:

```python
x = np.linspace(-3, 3, 200)
x_pos = np.linspace(0.01, 8, 200)  # For ln (needs positive x)

fig, ax = plt.subplots(figsize=(10, 10))

# Plot y = e^x
ax.plot(x, np.exp(x), 'b-', linewidth=2, label='y = e^x')

# Plot y = ln(x)
ax.plot(x_pos, np.log(x_pos), 'r-', linewidth=2, label='y = ln(x)')

# Plot y = x (reflection line)
ax.plot([-2, 8], [-2, 8], 'k--', linewidth=1, label='y = x')

ax.set_xlim(-3, 8)
ax.set_ylim(-3, 8)
ax.set_aspect('equal')
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Exponential and Logarithm are Inverse Functions')
ax.legend()
ax.grid(True)
plt.show()
```

---

## 6. Solving Exponential Equations

Demonstrate solving $P(t) = P_0 e^{kt}$ for $t$ using logarithms:

```python
def solve_for_time(P0, P_target, k):
    """Solve P0 * e^(kt) = P_target for t"""
    t = np.log(P_target / P0) / k
    return t

# Example: When does population reach 2000?
P0 = 500
k = 0.08
P_target = 2000

t_solution = solve_for_time(P0, P_target, k)

print(f"Given: P(t) = {P0}e^{{{k}t}}")
print(f"Find t when P(t) = {P_target}")
print(f"\nSolution steps:")
print(f"  {P0}e^{{{k}t}} = {P_target}")
print(f"  e^{{{k}t}} = {P_target/P0}")
print(f"  {k}t = ln({P_target/P0}) = {np.log(P_target/P0):.4f}")
print(f"  t = {t_solution:.2f} years")

# Verify
P_check = P0 * np.exp(k * t_solution)
print(f"\nVerification: P({t_solution:.2f}) = {P_check:.0f}")
```

---

## 7. The 70/r Rule for Doubling Time

Compare exact doubling time with the approximation:

```python
rates = np.array([1, 2, 3, 5, 7, 10, 15, 20])  # percent per year

print("Growth Rate (%)\tExact T₂\t70/r Approx\tError (%)")
print("-" * 60)

for r in rates:
    r_decimal = r / 100
    exact = np.log(2) / r_decimal
    approx = 70 / r
    error = 100 * (approx - exact) / exact
    print(f"{r}%\t\t{exact:.2f}\t\t{approx:.2f}\t\t{error:+.1f}%")

print("\nThe 70/r rule works best for rates around 5-10%")
```

---

## 8. Geometric Sequence Visualization

Show geometric sequence as discrete samples of exponential function:

```python
# Geometric sequence: a_n = a * r^(n-1)
a = 100  # first term
r = 1.5  # common ratio
n_terms = 10

# Generate sequence
n = np.arange(1, n_terms + 1)
sequence = a * r**(n - 1)

# Continuous exponential for comparison
t_cont = np.linspace(1, n_terms, 200)
y_cont = a * r**(t_cont - 1)

plt.figure(figsize=(10, 6))
plt.plot(t_cont, y_cont, 'b-', alpha=0.5, label='Continuous: f(x) = 100·1.5^(x-1)')
plt.stem(n, sequence, 'r', markerfmt='ro', basefmt=' ', label='Geometric sequence')

for i, val in enumerate(sequence[:5]):
    plt.annotate(f'  a_{i+1}={val:.0f}', (i+1, val))

plt.xlabel('n (term number)')
plt.ylabel('Value')
plt.title('Geometric Sequence as Discrete Exponential Sampling')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 9. Geometric Series Sum

Calculate and visualize partial sums:

```python
def geometric_sum(a, r, n):
    """Sum of first n terms: S_n = a(1-r^n)/(1-r)"""
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

# Example: a=1, r=0.5 (converging series)
a, r = 1, 0.5

n_values = np.arange(1, 21)
partial_sums = [geometric_sum(a, r, n) for n in n_values]

# Theoretical sum to infinity for |r| < 1
sum_infinity = a / (1 - r)

plt.figure(figsize=(10, 6))
plt.plot(n_values, partial_sums, 'bo-', label='Partial sums S_n')
plt.axhline(y=sum_infinity, color='r', linestyle='--', 
            label=f'Sum to ∞ = {sum_infinity:.2f}')

plt.xlabel('Number of terms (n)')
plt.ylabel('Partial sum S_n')
plt.title(f'Convergence of Geometric Series (a={a}, r={r})')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 10. Compound Interest Calculator

```python
def compound_interest(principal, rate, years, compounds_per_year=1):
    """Calculate compound interest
    For continuous compounding, use compounds_per_year = 'continuous'
    """
    if compounds_per_year == 'continuous':
        return principal * np.exp(rate * years)
    else:
        return principal * (1 + rate/compounds_per_year)**(compounds_per_year * years)

# Example: $10,000 at 6% annual interest
P = 10000
r = 0.06

print(f"Initial: ${P:,.2f}, Rate: {r*100}%\n")
print("Years\tAnnually\tMonthly\t\tContinuous")
print("-" * 55)

for years in [1, 5, 10, 20, 30]:
    annual = compound_interest(P, r, years, 1)
    monthly = compound_interest(P, r, years, 12)
    continuous = compound_interest(P, r, years, 'continuous')
    print(f"{years}\t${annual:,.2f}\t${monthly:,.2f}\t${continuous:,.2f}")
```

---

## 11. Probability Function (Q27 Preparation)

Explore $p = \frac{1}{1+e^{-kx}}$:

```python
def prob_function(x, k=3):
    """Probability function: p = 1/(1 + e^(-kx))"""
    return 1 / (1 + np.exp(-k * x))

x = np.linspace(-3, 3, 200)

plt.figure(figsize=(10, 6))

for k in [1, 2, 3, 5]:
    plt.plot(x, prob_function(x, k), linewidth=2, label=f'k = {k}')

plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.7)

plt.xlabel('Risk factor (x)')
plt.ylabel('Probability p(x)')
plt.title('Disease Risk Function: p = 1/(1 + e^{-kx})')
plt.legend()
plt.grid(True)
plt.ylim(-0.05, 1.05)
plt.show()

# Key values
print("Key observations for k=3:")
print(f"  p(0) = {prob_function(0, 3):.4f}")
print(f"  p(-1) = {prob_function(-1, 3):.4f}")
print(f"  p(1) = {prob_function(1, 3):.4f}")
```

---

## 12. Acacia Tree Growth Model

From Devaranavadgi et al. (2013):

```python
def acacia_height(t):
    """h(t) = 5.966 * exp(-3.0001/(t + 0.3501))"""
    return 5.966 * np.exp(-3.0001 / (t + 0.3501))

t = np.linspace(0, 30, 200)
h = acacia_height(t)

plt.figure(figsize=(10, 6))
plt.plot(t, h, 'g-', linewidth=2)

# Mark maximum height
h_max = 5.966
plt.axhline(y=h_max, color='r', linestyle='--', label=f'Maximum height: {h_max} m')

# Mark half-max point
t_half = 3.978
plt.plot(t_half, h_max/2, 'bo', markersize=10)
plt.annotate(f'  Half-max at t = {t_half:.1f} years', (t_half, h_max/2))

plt.xlabel('Time (years)')
plt.ylabel('Height (metres)')
plt.title('Acacia catechu Height Growth Model')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 13. Function Composition (Q23 Preparation)

For $f(x) = -e^{-2x+1}$ and $g(x) = -\frac{1}{2}x^2$:

```python
def f(x):
    return -np.exp(-2*x + 1)

def g(x):
    return -0.5 * x**2

def f_compose_g(x):
    """f(g(x)) = -e^(-2*g(x)+1) = -e^(x^2+1)"""
    return -np.exp(x**2 + 1)

x = np.linspace(-2, 2, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(x, f(x), 'b-', linewidth=2)
axes[0].set_title('f(x) = -e^{-2x+1}')
axes[0].grid(True)

axes[1].plot(x, g(x), 'r-', linewidth=2)
axes[1].set_title('g(x) = -(1/2)x²')
axes[1].grid(True)

axes[2].plot(x, f_compose_g(x), 'g-', linewidth=2)
axes[2].set_title('f∘g(x) = -e^{x²+1}')
axes[2].grid(True)

plt.tight_layout()
plt.show()

# Verify
test_x = 1
print(f"\nVerification at x = {test_x}:")
print(f"  g({test_x}) = {g(test_x)}")
print(f"  f(g({test_x})) = {f(g(test_x)):.4f}")
print(f"  Direct: -e^({test_x}²+1) = {f_compose_g(test_x):.4f}")
```

---

## 14. Discrete vs Continuous Growth Comparison

```python
P0 = 1000
r_discrete = 1.1  # 10% growth per period
k_continuous = np.log(r_discrete)

periods = np.arange(0, 20)
t_continuous = np.linspace(0, 19, 200)

P_discrete = P0 * r_discrete**periods
P_continuous = P0 * np.exp(k_continuous * t_continuous)

plt.figure(figsize=(10, 6))
plt.plot(t_continuous, P_continuous, 'b-', linewidth=2, alpha=0.7,
         label=f'Continuous: P(t) = {P0}e^{{{k_continuous:.4f}t}}')
plt.stem(periods, P_discrete, 'r', markerfmt='ro', basefmt=' ',
         label=f'Discrete: Pₙ = {P0}×{r_discrete}ⁿ')

plt.xlabel('Time period')
plt.ylabel('Population')
plt.title('Discrete vs Continuous Exponential Growth')
plt.legend()
plt.grid(True)
plt.show()

print(f"Discrete rate: {(r_discrete-1)*100}% per period")
print(f"Continuous rate: k = ln({r_discrete}) = {k_continuous:.4f}")
print(f"\nNote: Both give same values at integer time points!")
```

---

*Materials aligned with SCIE1500 Sample Final Examination*
