<?xml version="1.0" encoding="UTF-8"?>
# Week 9: Code Snippets — Probability, Combinatorics, and Binomial Distribution

## Overview

This document provides Python code snippets for exploring probability concepts covered in Week 9. These examples align with the lab notebook exercises, covering factorials, permutations, combinations, probability enumeration, and the binomial distribution applied to infection modeling.

**Key libraries:**
```python
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations, combinations
from scipy.stats import binom
```

---

## 1. The Multiplication Principle and Factorials

### 1.1 Understanding the Multiplication Principle

The multiplication principle states: if a decision involves $k$ selections where the first can be made in $n_1$ ways, the second in $n_2$ ways, etc., then total selections = $n_1 \cdot n_2 \cdot \ldots \cdot n_k$.

```python
import math

# Example: Routes from Town A to Town C via Town B
routes_A_to_B = 4
routes_B_to_C = 2
total_routes = routes_A_to_B * routes_B_to_C
print(f"Total routes from A to C: {total_routes}")  # 8

# Example: Arranging letters A, B, C, D, E
# First position: 5 choices, second: 4, third: 3, etc.
arrangements = 5 * 4 * 3 * 2 * 1
print(f"Ways to arrange 5 letters: {arrangements}")  # 120 = 5!
```

**Output:**
```
Total routes from A to C: 8
Ways to arrange 5 letters: 120
```

### 1.2 Computing Factorials

The factorial $n! = n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1$ counts arrangements of $n$ distinct objects.

```python
import math

# Basic factorial calculations
print(f"5! = {math.factorial(5)}")   # 120
print(f"6! = {math.factorial(6)}")   # 720
print(f"0! = {math.factorial(0)}")   # 1 (by definition)

# Verify: 6! = 6 × 5!
print(f"6 × 5! = {6 * math.factorial(5)}")  # 720

# Simplifying factorial expressions
# 12!/10! = 12 × 11 = 132
result = math.factorial(12) / math.factorial(10)
print(f"12!/10! = {result}")

# 6!/(2!4!) = 15
result2 = math.factorial(6) / (math.factorial(2) * math.factorial(4))
print(f"6!/(2!4!) = {result2}")
```

**Output:**
```
5! = 120
6! = 720
0! = 1
6 × 5! = 720
12!/10! = 132.0
6!/(2!4!) = 15.0
```

---

## 2. Permutations and Combinations

### 2.1 Permutations — Order Matters

A permutation is an **ordered arrangement**. The number of ways to arrange $p$ items from $n$ items:

$$P(n,p) = \frac{n!}{(n-p)!}$$

```python
import math
from itertools import permutations

# Calculate P(n,p) using formula
def count_permutations(n, p):
    """Number of ways to arrange p items from n items (order matters)."""
    return math.factorial(n) / math.factorial(n - p)

# P(3,2): arrange 2 items from 3
print(f"P(3,2) = {count_permutations(3, 2)}")  # 6

# P(5,3): arrange 3 items from 5
print(f"P(5,3) = {count_permutations(5, 3)}")  # 60

# List all permutations of A, B, C taken 3 at a time
P33 = permutations(['A', 'B', 'C'], 3)
print("\nPermutations of A,B,C taken 3 at a time:")
for p in list(P33):
    print(p)
```

**Output:**
```
P(3,2) = 6.0
P(5,3) = 60.0

Permutations of A,B,C taken 3 at a time:
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
```

```python
# Permutations of 3 items taken 2 at a time
print("Permutations of A,B,C taken 2 at a time:")
P32 = permutations(['A', 'B', 'C'], 2)
for p in list(P32):
    print(p)
```

**Output:**
```
Permutations of A,B,C taken 2 at a time:
('A', 'B')
('A', 'C')
('B', 'A')
('B', 'C')
('C', 'A')
('C', 'B')
```

### 2.2 Combinations — Order Does Not Matter

A combination selects $p$ items from $n$ **disregarding order**:

$$C(n,p) = \frac{n!}{(n-p)! \cdot p!} = \frac{P(n,p)}{p!}$$

```python
from itertools import combinations

# List all combinations of A, B, C taken 2 at a time
C32 = combinations(['A', 'B', 'C'], 2)
print("Combinations of A,B,C taken 2 at a time:")
for c in list(C32):
    print(c)
# Only 3 combinations: (A,B) = (B,A), etc.
```

**Output:**
```
Combinations of A,B,C taken 2 at a time:
('A', 'B')
('A', 'C')
('B', 'C')
```

### 2.3 Application: Committee Assignment

**Problem:** Assign 9 colleagues into 3 committees of 3 people each.

```python
# First committee: select 3 out of 9
n1 = math.factorial(9) / (math.factorial(6) * math.factorial(3))

# Second committee: select 3 out of remaining 6
n2 = math.factorial(6) / (math.factorial(3) * math.factorial(3))

# Third committee: select 3 out of remaining 3
n3 = math.factorial(3) / (math.factorial(0) * math.factorial(3))

# Total ways
answer = n1 * n2 * n3
print(f"Ways to form 3 committees: {n1:.0f} × {n2:.0f} × {n3:.0f} = {answer:.0f}")
```

**Output:**
```
Ways to form 3 committees: 84 × 20 × 1 = 1680
```

---

## 3. Probability via Enumeration

### 3.1 Basic Probability Definition

**Probability** = (favorable outcomes) / (total possible outcomes)

```python
# Example 1: Probability of 2 girls in 3 children
# Total outcomes: 2^3 = 8 (each child can be G or B)
Ns = 2**3  # sample space size

# Favorable outcomes: GGB, GBG, BGG
Na = 3

prob = Na / Ns
print(f"P(2 girls in 3 children) = {Na}/{Ns} = {prob}")
```

**Output:**
```
P(2 girls in 3 children) = 3/8 = 0.375
```

### 3.2 Enumeration Using Loops

When sample spaces become complex, use loops to enumerate all possibilities.

```python
# Enumerate all possible sequences for 3 children
S = ['G', 'B']  # each child can be Girl or Boy

print("All possible sequences for 3 children:")
print("Sequence | Girls")
print("-" * 20)

for first in S:
    for second in S:
        for third in S:
            count_girls = (first == 'G') + (second == 'G') + (third == 'G')
            print(f"  {first} {second} {third}  |   {count_girls}")
```

**Output:**
```
All possible sequences for 3 children:
Sequence | Girls
--------------------
  G G G  |   3
  G G B  |   2
  G B G  |   2
  G B B  |   1
  B G G  |   2
  B G B  |   1
  B B G  |   1
  B B B  |   0
```

### 3.3 Checking Specific Conditions

**Exercise:** List sequences where the middle child is a boy.

```python
# Modified enumeration: check if middle child is a boy
S = ['G', 'B']

print("Sequence | Middle is Boy?")
print("-" * 25)

for first in S:
    for second in S:
        for third in S:
            middle_is_boy = (second == 'B')
            print(f"  {first} {second} {third}  |    {middle_is_boy}")
```

**Output:**
```
Sequence | Middle is Boy?
-------------------------
  G G G  |    False
  G G B  |    False
  G B G  |    True
  G B B  |    True
  B G G  |    False
  B G B  |    False
  B B G  |    True
  B B B  |    True
```

### 3.4 Using Combination Formula for Probability

**Example:** P(2 girls in 5 children)

```python
# C(5,2): ways to choose which 2 of 5 positions are girls
Na = math.factorial(5) / (math.factorial(2) * math.factorial(3))

# Total outcomes: 2^5
Ns = 2**5

prob = Na / Ns
print(f"Na = {Na:.0f} (ways to have 2 girls)")
print(f"Ns = {Ns} (total outcomes)")
print(f"P(2 girls in 5 children) = {prob}")
```

**Output:**
```
Na = 10 (ways to have 2 girls)
Ns = 32 (total outcomes)
P(2 girls in 5 children) = 0.3125
```

### 3.5 Student Exercise A: Specific Sequence Probability

**Problem:** What is the probability of exactly GGBBB (2 girls followed by 3 boys) in a family of 5 children?

```python
# Mathematical approach:
# Only ONE way to get the specific sequence GGBBB
# Total outcomes: 2^5 = 32

prob_specific = 1 / (2**5)
print(f"P(GGBBB) = 1/32 = {prob_specific}")

# Verification by enumeration
S = ['G', 'B']
count_ggbbb = 0
total = 0

for c1 in S:
    for c2 in S:
        for c3 in S:
            for c4 in S:
                for c5 in S:
                    total += 1
                    sequence = c1 + c2 + c3 + c4 + c5
                    if sequence == 'GGBBB':
                        count_ggbbb += 1
                        print(f"Found: {sequence}")

print(f"\nVerification: {count_ggbbb}/{total} = {count_ggbbb/total}")
```

**Output:**
```
P(GGBBB) = 1/32 = 0.03125
Found: GGBBB

Verification: 1/32 = 0.03125
```

---

## 4. Binomial Distribution

### 4.1 Bernoulli and Binomial Experiments

- **Bernoulli trial:** Single experiment with two outcomes (success/failure), probability $p$
- **Binomial experiment:** Series of $n$ independent Bernoulli trials
- **Interest:** How many successes $k$ occur in $n$ trials?

**Binomial probability formula:**

$$P(X = k) = C(n,k) \cdot p^k \cdot (1-p)^{n-k} = \frac{n!}{k!(n-k)!} \cdot p^k \cdot (1-p)^{n-k}$$

### 4.2 Manual Binomial Calculation

```python
import math

def binomial_prob_manual(n, k, p):
    """Calculate P(X=k) for X ~ Binomial(n, p) using the formula."""
    coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    probability = coefficient * (p**k) * ((1 - p)**(n - k))
    return probability

# Example: Coin toss — P(0 heads), P(1 head), P(2 heads) in 2 tosses
n, p = 2, 0.5
print("Binomial probabilities for 2 fair coin tosses:")
for k in [0, 1, 2]:
    prob = binomial_prob_manual(n, k, p)
    print(f"  P(k={k}) = {prob}")
```

**Output:**
```
Binomial probabilities for 2 fair coin tosses:
  P(k=0) = 0.25
  P(k=1) = 0.5
  P(k=2) = 0.25
```

### 4.3 Using scipy.stats.binom

The `binom.pmf()` function provides a convenient way to calculate binomial probabilities.

```python
from scipy.stats import binom

# Calculate P(X=k) for n=2, p=0.5
n, p = 2, 0.5
print("Using binom.pmf():")
for k in [0, 1, 2]:
    prob = binom.pmf(k=k, n=n, p=p)
    print(f"  P(k={k}) = {prob}")
```

**Output:**
```
Using binom.pmf():
  P(k=0) = 0.25
  P(k=1) = 0.5
  P(k=2) = 0.25
```

### 4.4 Full Distribution with Loop

```python
import numpy as np
from scipy.stats import binom

# Binomial distribution for 3 children (probability of k girls)
n = 3
p = 0.5
success = np.arange(0, n + 1)  # k = 0, 1, 2, 3

karray = []
probarray = []

print(f"Binomial distribution (n={n}, p={p}):")
for ki in success:
    probk = binom.pmf(k=ki, n=n, p=p)
    karray.append(ki)
    probarray.append(probk)
    print(f"  k={ki}: P = {probk:.4f}")
```

**Output:**
```
Binomial distribution (n=3, p=0.5):
  k=0: P = 0.1250
  k=1: P = 0.3750
  k=2: P = 0.3750
  k=3: P = 0.1250
```

### 4.5 Visualizing the Binomial Distribution

```python
import matplotlib.pyplot as plt

# Plot binomial distribution for n=3, p=0.5
girls = [0, 1, 2, 3]
probs = [0.125, 0.375, 0.375, 0.125]

plt.bar(x=girls, height=probs, color="orange")
plt.xlabel('Number of Girls')
plt.ylabel('Probability')
plt.title('Probability of Girls in a Family of 3 Children')
plt.xticks(girls)
plt.show()
```

---

## 5. Application: Infection Modeling (Student Exercise B)

### 5.1 Setting Up the Infection Scenario

**Scenario:** An infected traveller has contact with 25 susceptible people. The probability that a contact results in infection is $p = 0.45$.

**Question:** What is the probability distribution of infections?

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Binomial distribution parameters
p = 0.45
n = 25

# Calculate probabilities for k = 0, 1, 2, ..., 25
success = np.arange(0, n + 1)
probarray = [0] * (n + 1)

print(f"Infection probabilities (n={n}, p={p}):")
print("-" * 30)
for ki in success:
    probk = binom.pmf(k=ki, n=n, p=p)
    probarray[ki] = probk
    print(f"  k={ki:2d}: P = {probk:.6f}")
```

### 5.2 Visualizing Infection Distribution

```python
# Bar plot of infection probabilities
plt.figure(figsize=(10, 5))
plt.bar(x=success, height=probarray, color="blue")
plt.xlabel('Number of Infections (k)')
plt.ylabel('Probability')
plt.title(f'Binomial Distribution: Infections from {n} Contacts (p={p})')
plt.xticks(success)
plt.tight_layout()
plt.show()
```

### 5.3 Comparing Different Infection Probabilities

**Exercise:** Repeat with $p = 0.60$ and observe how the distribution shifts.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 25
p_values = [0.45, 0.60]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for idx, p in enumerate(p_values):
    success = np.arange(0, n + 1)
    probarray = [binom.pmf(k=ki, n=n, p=p) for ki in success]
    
    axes[idx].bar(x=success, height=probarray, color=['blue', 'red'][idx])
    axes[idx].set_xlabel('Number of Infections (k)')
    axes[idx].set_ylabel('Probability')
    axes[idx].set_title(f'Binomial Distribution (n={n}, p={p})')
    axes[idx].set_xticks(range(0, n + 1, 5))
    
    # Mark expected value
    expected = n * p
    axes[idx].axvline(x=expected, color='black', linestyle='--', label=f'E[X]={expected:.1f}')
    axes[idx].legend()

plt.tight_layout()
plt.show()
```

### 5.4 Key Observations (Exercise B Discussion)

```python
# Calculate summary statistics for comparison
n = 25

for p in [0.45, 0.60]:
    expected = n * p
    variance = n * p * (1 - p)
    std_dev = np.sqrt(variance)
    
    # Find mode (most likely k)
    probs = [binom.pmf(k=ki, n=n, p=p) for ki in range(n + 1)]
    mode = np.argmax(probs)
    
    print(f"\np = {p}:")
    print(f"  Expected infections: E[X] = {expected:.1f}")
    print(f"  Standard deviation: σ = {std_dev:.2f}")
    print(f"  Most likely outcome: k = {mode}")
    print(f"  P(k = {mode}) = {probs[mode]:.4f}")
```

**Output:**
```
p = 0.45:
  Expected infections: E[X] = 11.2
  Standard deviation: σ = 2.49
  Most likely outcome: k = 11
  P(k = 11) = 0.1602

p = 0.60:
  Expected infections: E[X] = 15.0
  Standard deviation: σ = 2.45
  Most likely outcome: k = 15
  P(k = 15) = 0.1612
```

**Observations when $p$ increases from 0.45 to 0.60:**
1. The distribution **shifts right** (toward more infections)
2. The **expected value** increases from 11.2 to 15.0
3. The **peak (mode)** moves from k=11 to k=15
4. The **spread** (standard deviation) remains similar (~2.5)
5. The distribution remains **bell-shaped** but centered at a higher value

---

## 6. Practice Question Connections

### 6.1 Q32: Sample Space for Coin Tosses

```python
# Q32: Fair coin tossed 5 times — what is sample space size?
n_tosses = 5
sample_space_size = 2**n_tosses
print(f"Sample space for {n_tosses} coin tosses: |S| = {sample_space_size}")

# P(exactly 3 heads)?
from scipy.stats import binom
prob_3_heads = binom.pmf(k=3, n=5, p=0.5)
print(f"P(exactly 3 heads) = {prob_3_heads:.4f}")
# Not 0.60, so that option is incorrect
```

**Output:**
```
Sample space for 5 coin tosses: |S| = 32
P(exactly 3 heads) = 0.3125
```

### 6.2 Q35: Testing Infection Rate

```python
from scipy.stats import binom

# Q35: New virus variant — 9 of 11 contacts infected
# Test H0: p = 0.5 vs H1: p > 0.5
n = 11
observed_k = 9
p_null = 0.5

# P-value = P(X >= 9 | p = 0.5)
p_value = sum(binom.pmf(k=ki, n=n, p=p_null) for ki in range(9, n + 1))
print(f"P-value = P(X >= {observed_k} | n={n}, p={p_null})")
print(f"P-value = {p_value:.6f}")
print(f"Reject H0 at α=0.05? {p_value < 0.05}")
```

**Output:**
```
P-value = P(X >= 9 | n=11, p=0.5)
P-value = 0.032715
Reject H0 at α=0.05? True
```

---

## 7. Complete Lab Code Template

Here is a complete template integrating all lab exercises:

```python
"""
Week 9 Lab: Probability and Binomial Distribution
Complete this template for lab submission.
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations, combinations
from scipy.stats import binom

# ==========================================
# PART 1: Factorials and Combinations
# ==========================================

# Calculate 12!/10!
result1 = math.factorial(12) / math.factorial(10)
print(f"12!/10! = {result1}")

# Calculate 6!/(2!4!)
result2 = math.factorial(6) / (math.factorial(2) * math.factorial(4))
print(f"6!/(2!4!) = {result2}")

# ==========================================
# STUDENT EXERCISE A: P(GGBBB)
# ==========================================

# Mathematical solution
prob_ggbbb = 1 / (2**5)
print(f"\nExercise A: P(GGBBB) = {prob_ggbbb}")

# Verification by enumeration (write your code)
# ...

# ==========================================
# STUDENT EXERCISE B: Infection Modeling
# ==========================================

def infection_analysis(n, p):
    """Analyze infection distribution for n contacts with probability p."""
    success = np.arange(0, n + 1)
    probarray = [binom.pmf(k=ki, n=n, p=p) for ki in success]
    
    # Print probabilities
    print(f"\nInfection probabilities (n={n}, p={p}):")
    for ki in success:
        print(f"  k={ki:2d}: P = {probarray[ki]:.6f}")
    
    return success, probarray

# Part 1: p = 0.45
success, probs1 = infection_analysis(n=25, p=0.45)

# Part 2: p = 0.60
success, probs2 = infection_analysis(n=25, p=0.60)

# Plot comparison
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(success, probs1, color='blue')
axes[0].set_title('Infections (p=0.45)')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(k)')

axes[1].bar(success, probs2, color='red')
axes[1].set_title('Infections (p=0.60)')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(k)')

plt.tight_layout()
plt.show()

# ==========================================
# STUDENT EXERCISE C: Quiz Answers
# ==========================================
# Record your answers from the probability practice quiz
# Q1: ___
# Q2: ___
# Q3: ___
# Q4: ___
# Q5: ___
```

---

## Summary

| Topic | Key Functions | Lab Section |
|-------|---------------|-------------|
| Factorials | `math.factorial(n)` | Part 1 |
| Permutations | `permutations(items, r)` | Part 2 |
| Combinations | `combinations(items, r)` | Part 2 |
| Enumeration | Nested `for` loops | Part 3 |
| Binomial PMF | `binom.pmf(k, n, p)` | Part 4–5 |
| Visualization | `plt.bar()` | Part 5 |

**Key formulas:**
- Permutations: $P(n,p) = \frac{n!}{(n-p)!}$
- Combinations: $C(n,p) = \frac{n!}{(n-p)!p!}$
- Binomial probability: $P(X=k) = C(n,k) \cdot p^k \cdot (1-p)^{n-k}$
