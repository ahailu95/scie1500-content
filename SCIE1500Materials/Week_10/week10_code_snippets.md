<?xml version="1.0" encoding="UTF-8"?>
# Week 10: Code Snippets
## Random Variables and Hypothesis Testing

**Theme:** Making Decisions Under Uncertainty  
**Required Packages:** numpy, scipy, matplotlib, pandas

---

## Setup and Imports

```python
# Week 10: Hypothesis Testing - Setup
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, binomtest
import pandas as pd

# Set display options
pd.set_option('display.max_rows', None)
np.set_printoptions(precision=5)

print("Libraries loaded successfully!")
```

---

## Expected Value Calculation (Q33 Style)

Calculate expected value from a probability distribution table.

```python
# Expected Value Calculation (Q33 Style)
# Given probability distribution:
# X:    0    3    4    6
# P(X): 0.2  0.4  0.3  0.1

x_values = np.array([0, 3, 4, 6])
probabilities = np.array([0.2, 0.4, 0.3, 0.1])

# Verify probabilities sum to 1
print(f"Sum of probabilities: {probabilities.sum()}")

# Calculate E[X]
expected_value = np.sum(x_values * probabilities)
print(f"\nE[X] = {x_values[0]}×{probabilities[0]} + {x_values[1]}×{probabilities[1]} + {x_values[2]}×{probabilities[2]} + {x_values[3]}×{probabilities[3]}")
print(f"E[X] = {x_values[0]*probabilities[0]} + {x_values[1]*probabilities[1]} + {x_values[2]*probabilities[2]} + {x_values[3]*probabilities[3]}")
print(f"E[X] = {expected_value}")

# Calculate E[X²] and Variance
expected_x_squared = np.sum(x_values**2 * probabilities)
variance = expected_x_squared - expected_value**2
std_dev = np.sqrt(variance)

print(f"\nE[X²] = {expected_x_squared}")
print(f"Var(X) = E[X²] - (E[X])² = {expected_x_squared} - {expected_value}² = {variance}")
print(f"Standard deviation = {std_dev:.4f}")
```

**Output:**
```
Sum of probabilities: 1.0
E[X] = 0×0.2 + 3×0.4 + 4×0.3 + 6×0.1
E[X] = 0.0 + 1.2 + 1.2 + 0.6
E[X] = 3.0
```

---

## Bernoulli Distribution

Work with Bernoulli distribution for single trial experiments.

```python
# Bernoulli Distribution: Single trial with two outcomes
# Example: Single contact transmission probability

p = 0.6  # Probability of transmission

# Mean and Variance
mean_bernoulli = p
var_bernoulli = p * (1 - p)

print("Bernoulli Distribution (p = 0.6)")
print("="*40)
print(f"P(X = 0) = 1 - p = {1-p}")
print(f"P(X = 1) = p = {p}")
print(f"\nE[X] = p = {mean_bernoulli}")
print(f"Var(X) = p(1-p) = {p}×{1-p} = {var_bernoulli}")

# Visualize
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar([0, 1], [1-p, p], color=['steelblue', 'coral'], edgecolor='black')
ax.set_xlabel('X (0 = No transmission, 1 = Transmission)')
ax.set_ylabel('Probability')
ax.set_title(f'Bernoulli Distribution (p = {p})')
ax.set_xticks([0, 1])
ax.set_ylim(0, 1)
plt.tight_layout()
plt.show()
```

---

## Binomial Distribution - PMF Calculation

Calculate binomial probabilities using scipy.

```python
# Binomial Distribution: Number of successes in n trials
n = 12  # number of trials
p = 0.5  # probability of success per trial

print(f"Binomial Distribution: X ~ Binomial({n}, {p})")
print("="*50)

# Calculate probabilities for all possible outcomes
k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p)

# Create a nice table
df = pd.DataFrame({
    'k (successes)': k_values,
    'P(X = k)': probabilities,
    'P(X = k) rounded': np.round(probabilities, 5)
})
print(df.to_string(index=False))

# Mean and Variance
mean_binom = n * p
var_binom = n * p * (1 - p)

print(f"\nE[X] = np = {n}×{p} = {mean_binom}")
print(f"Var(X) = np(1-p) = {n}×{p}×{1-p} = {var_binom}")
```

---

## Visualizing Binomial Distribution

Create bar chart of binomial distribution with mean marked.

```python
# Visualize Binomial Distribution
n = 12
p = 0.5

k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(k_values, probabilities, color='steelblue', edgecolor='black', alpha=0.7)

# Mark the mean
mean = n * p
ax.axvline(x=mean, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean}')

# Add labels for probabilities
for k, prob in zip(k_values, probabilities):
    if prob > 0.01:
        ax.text(k, prob + 0.005, f'{prob:.3f}', ha='center', fontsize=8)

ax.set_xlabel('k (Number of Successes)', fontsize=12)
ax.set_ylabel('P(X = k)', fontsize=12)
ax.set_title(f'Binomial Distribution: X ~ Binomial({n}, {p})', fontsize=14)
ax.set_xticks(k_values)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## p-Value Calculation Using binom.pmf

Calculate p-value manually by summing probabilities.

```python
# p-Value Calculation: Manual method using binom.pmf
# Scenario: Testing if coin is fair after observing 10 heads in 12 tosses

n = 12
p_null = 0.5  # Null hypothesis: fair coin
observed_k = 10  # Observed successes

print("Calculating p-value for One-Tailed Test (Upper)")
print("H₀: p ≤ 0.5 vs Hₐ: p > 0.5")
print(f"Observed: {observed_k} successes out of {n} trials")
print("="*50)

# Calculate probabilities for k = 10, 11, 12
print("\nProbabilities for extreme values (k ≥ 10):")
for k in range(observed_k, n + 1):
    prob = binom.pmf(k, n, p_null)
    print(f"P(X = {k}) = {prob:.5f}")

# p-value = P(X ≥ observed_k | H₀)
p_value_upper = sum(binom.pmf(k, n, p_null) for k in range(observed_k, n + 1))
print(f"\np-value (one-tailed, upper) = P(X ≥ {observed_k}) = {p_value_upper:.5f}")
```

---

## p-Value Using binomtest Function

Use scipy's binomtest for quick hypothesis testing (recommended method).

```python
# p-Value Calculation Using binomtest (Recommended Method)
from scipy.stats import binomtest

n = 12
observed_k = 10
p_null = 0.5

print("Using scipy.stats.binomtest()")
print("="*50)

# One-tailed test (upper): Hₐ: p > p₀
result_greater = binomtest(k=observed_k, n=n, p=p_null, alternative='greater')
print(f"\nOne-tailed test (Hₐ: p > 0.5):")
print(f"  Observed proportion: {result_greater.proportion_estimate:.4f}")
print(f"  p-value = {result_greater.pvalue:.5f}")

# One-tailed test (lower): Hₐ: p < p₀
result_less = binomtest(k=observed_k, n=n, p=p_null, alternative='less')
print(f"\nOne-tailed test (Hₐ: p < 0.5):")
print(f"  p-value = {result_less.pvalue:.5f}")

# Two-tailed test: Hₐ: p ≠ p₀
result_two_sided = binomtest(k=observed_k, n=n, p=p_null, alternative='two-sided')
print(f"\nTwo-tailed test (Hₐ: p ≠ 0.5):")
print(f"  p-value = {result_two_sided.pvalue:.5f}")

# Decision at α = 0.05
alpha = 0.05
print(f"\nDecision at α = {alpha}:")
print(f"  One-tailed (upper): {'Reject H₀' if result_greater.pvalue < alpha else 'Fail to reject H₀'}")
print(f"  Two-tailed: {'Reject H₀' if result_two_sided.pvalue < alpha else 'Fail to reject H₀'}")
```

---

## Q35 Exam Question - Complete Solution

Solve the exact exam question about virus variant transmissibility.

```python
# Q35 Exam Question: New Virus Variant Transmissibility
print("Q35: Is the new variant more infectious?")
print("="*60)

# Given data
n = 11  # Number of contacts
observed_infections = 9  # Observed infections
p_old = 0.50  # Old variant infection rate

print(f"\nData: {observed_infections} infections out of {n} contacts")
print(f"Old variant rate: p = {p_old}")
print(f"Question: Is the new variant MORE infectious?")

# CORRECT approach: One-tailed test
print("\n" + "-"*60)
print("CORRECT APPROACH: One-tailed test")
print("-"*60)
print("H₀: p ≤ 0.50 (new variant is NOT more infectious)")
print("Hₐ: p > 0.50 (new variant IS more infectious)")

result_one_tailed = binomtest(k=observed_infections, n=n, p=p_old, alternative='greater')
print(f"\np-value = P(X ≥ {observed_infections} | p = 0.5) = {result_one_tailed.pvalue:.5f}")
print(f"         = 67/2048 ≈ 0.033")
print(f"\nSince {result_one_tailed.pvalue:.3f} < 0.05, REJECT H₀")
print("Conclusion: Evidence supports that new variant is more infectious")

# INCORRECT approach: Two-tailed test (for comparison)
print("\n" + "-"*60)
print("INCORRECT APPROACH: Two-tailed test")
print("-"*60)
print("H₀: p = 0.50")
print("Hₐ: p ≠ 0.50")

result_two_tailed = binomtest(k=observed_infections, n=n, p=p_old, alternative='two-sided')
print(f"\np-value = {result_two_tailed.pvalue:.5f}")
print(f"\nSince {result_two_tailed.pvalue:.3f} > 0.05, FAIL TO REJECT H₀")
print("This would lead to the WRONG conclusion for this question!")

print("\n" + "="*60)
print("KEY INSIGHT: Match the test type to the research question!")
print("'More infectious' → One-tailed (upper) test")
print("="*60)
```

---

## Visualizing p-Values and Rejection Regions

Create visualization showing the rejection region and p-value.

```python
# Visualize p-Value and Rejection Region
n = 11
p_null = 0.5
observed_k = 9
alpha = 0.05

k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p_null)

# Determine colors: rejection region (p-value region) in red
colors = ['coral' if k >= observed_k else 'steelblue' for k in k_values]

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(k_values, probabilities, color=colors, edgecolor='black', alpha=0.7)

# Calculate and display p-value
p_value = sum(probabilities[k_values >= observed_k])

# Add annotations
ax.annotate(f'Observed: k = {observed_k}', xy=(observed_k, binom.pmf(observed_k, n, p_null)),
            xytext=(observed_k + 1.5, binom.pmf(observed_k, n, p_null) + 0.05),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=11, color='red', fontweight='bold')

ax.text(0.02, 0.95, f'p-value = P(X ≥ {observed_k}) = {p_value:.4f}',
        transform=ax.transAxes, fontsize=12, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

decision = 'Reject H₀' if p_value < alpha else 'Fail to reject H₀'
ax.text(0.02, 0.85, f'Decision: {decision}',
        transform=ax.transAxes, fontsize=12, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightcoral' if p_value < alpha else 'lightgray', alpha=0.8))

ax.set_xlabel('k (Number of Infections)', fontsize=12)
ax.set_ylabel('P(X = k) under H₀: p = 0.5', fontsize=12)
ax.set_title(f'One-Tailed Test: P(X ≥ {observed_k}) under H₀\n(Red bars = p-value region)', fontsize=14)
ax.set_xticks(k_values)
ax.grid(axis='y', alpha=0.3)

# Add legend for bar colors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='coral', label='p-value region'),
                   Patch(facecolor='steelblue', label='Not in p-value')]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.show()
```

---

## Finding Critical Values

Determine the rejection region boundary (critical value).

```python
# Finding Critical Values for Hypothesis Testing
n = 20
p_null = 0.40
alpha = 0.05

print(f"Finding Critical Value for One-Tailed Test (Upper)")
print(f"H₀: p ≤ {p_null} vs Hₐ: p > {p_null}")
print(f"n = {n}, α = {alpha}")
print("="*50)

# Calculate P(X ≥ k) for each k
print("\nk\tP(X ≥ k)\tReject H₀?")
print("-"*40)

critical_value = None
for k in range(0, n + 1):
    tail_prob = 1 - binom.cdf(k - 1, n, p_null)  # P(X >= k)
    reject = "YES" if tail_prob < alpha else "NO"
    if tail_prob < alpha and critical_value is None:
        critical_value = k
        print(f"{k}\t{tail_prob:.5f}\t\t{reject} ← Critical value")
    elif k >= 8 and k <= 15:
        print(f"{k}\t{tail_prob:.5f}\t\t{reject}")

print(f"\nCritical value k* = {critical_value}")
print(f"Decision rule: Reject H₀ if observed successes ≥ {critical_value}")
```

---

## Comparing One-Tailed vs Two-Tailed Tests

Visualize the difference between test types.

```python
# Compare One-Tailed vs Two-Tailed Tests
n = 20
p_null = 0.5
observed = 14

k_values = np.arange(0, n + 1)
probabilities = binom.pmf(k_values, n, p_null)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# One-tailed test (upper)
ax1 = axes[0]
colors_one = ['coral' if k >= observed else 'steelblue' for k in k_values]
ax1.bar(k_values, probabilities, color=colors_one, edgecolor='black', alpha=0.7)
p_value_one = binomtest(k=observed, n=n, p=p_null, alternative='greater').pvalue
ax1.set_title(f'One-Tailed Test (Hₐ: p > 0.5)\np-value = {p_value_one:.4f}', fontsize=12)
ax1.set_xlabel('k')
ax1.set_ylabel('P(X = k)')
ax1.axvline(x=n*p_null, color='green', linestyle='--', label=f'Mean = {n*p_null}')
ax1.legend()

# Two-tailed test
ax2 = axes[1]
deviation = abs(observed - n*p_null)
lower_extreme = int(n*p_null - deviation)
colors_two = ['coral' if (k >= observed or k <= lower_extreme) else 'steelblue' for k in k_values]
ax2.bar(k_values, probabilities, color=colors_two, edgecolor='black', alpha=0.7)
p_value_two = binomtest(k=observed, n=n, p=p_null, alternative='two-sided').pvalue
ax2.set_title(f'Two-Tailed Test (Hₐ: p ≠ 0.5)\np-value = {p_value_two:.4f}', fontsize=12)
ax2.set_xlabel('k')
ax2.set_ylabel('P(X = k)')
ax2.axvline(x=n*p_null, color='green', linestyle='--', label=f'Mean = {n*p_null}')
ax2.legend()

fig.suptitle(f'Observed: {observed} successes out of {n}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print(f"Summary for observed = {observed}, n = {n}, p₀ = {p_null}:")
print(f"  One-tailed p-value: {p_value_one:.4f} → {'Reject' if p_value_one < 0.05 else 'Fail to reject'} at α = 0.05")
print(f"  Two-tailed p-value: {p_value_two:.4f} → {'Reject' if p_value_two < 0.05 else 'Fail to reject'} at α = 0.05")
```

---

## Key Functions Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `binom.pmf(k, n, p)` | Probability mass function: $P(X = k)$ | `binom.pmf(9, 11, 0.5)` |
| `binom.cdf(k, n, p)` | Cumulative distribution: $P(X \leq k)$ | `binom.cdf(8, 11, 0.5)` |
| `binomtest(k, n, p, alternative)` | Hypothesis test with p-value | `binomtest(9, 11, 0.5, 'greater')` |
| `np.sum(x * p)` | Expected value calculation | `np.sum(x_values * probabilities)` |

---

## Summary: Hypothesis Testing Workflow

```python
# Generic Hypothesis Testing Template
def hypothesis_test(observed_k, n, p_null, alternative='greater', alpha=0.05):
    """
    Perform a binomial hypothesis test.
    
    Parameters:
    - observed_k: observed number of successes
    - n: number of trials
    - p_null: null hypothesis probability
    - alternative: 'greater', 'less', or 'two-sided'
    - alpha: significance level
    
    Returns:
    - Dictionary with test results
    """
    result = binomtest(k=observed_k, n=n, p=p_null, alternative=alternative)
    
    decision = "Reject H₀" if result.pvalue < alpha else "Fail to reject H₀"
    
    return {
        'observed': observed_k,
        'n': n,
        'p_null': p_null,
        'alternative': alternative,
        'p_hat': result.proportion_estimate,
        'p_value': result.pvalue,
        'alpha': alpha,
        'decision': decision
    }

# Example usage
results = hypothesis_test(9, 11, 0.5, 'greater', 0.05)
for key, value in results.items():
    print(f"{key}: {value}")
```
