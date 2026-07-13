#!/usr/bin/env python3
"""
Generate SCIE1500 S2 2026 lab notebooks with integrated problem briefs.

Usage:
    python generate_lab_notebooks.py 2        # generate Week 2 (STUDENT + A + B)
    python generate_lab_notebooks.py 2 3 4    # multiple weeks
    python generate_lab_notebooks.py all      # all implemented weeks

Output goes to: ~/scie1500-content/SCIE1500Materials/Week_N/LabFiles/

Decisions baked in:
  - A/B notebooks open straight into the scenario (no generic prefix)
  - Submission exercise tone: mix of Python tasks + written responses
  - Submission exercises in: Weeks 3, 6, 9, 12
"""

import json
import sys
import uuid
from pathlib import Path

BASE = Path.home() / "scie1500-content" / "SCIE1500Materials"

# ─────────────────────────────────────────────────────────────────────────────
# NOTEBOOK ASSEMBLY HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _cid():
    return uuid.uuid4().hex[:8]

def _src(text):
    """Convert multiline string to notebook source list."""
    lines = text.split('\n')
    out = [line + '\n' for line in lines[:-1]]
    if lines[-1]:
        out.append(lines[-1])
    return out or ['']

def md(text):
    return {"cell_type": "markdown", "id": _cid(), "metadata": {}, "source": _src(text)}

def code(text):
    return {
        "cell_type": "code", "execution_count": None, "id": _cid(),
        "metadata": {}, "outputs": [], "source": _src(text),
    }

def notebook(cells):
    return {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py", "mimetype": "text/x-python",
                "name": "python", "version": "3.10.0",
            },
        },
        "cells": cells,
    }

def write_nb(nb, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"  ✓ {path.relative_to(Path.home())}")


SETUP_IMPORTS = """\
# Run this cell first — loads libraries for today's lab
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'figure.dpi': 120, 'font.size': 11})"""

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 1 — Functions and the Language of Scientific Analysis
# ─────────────────────────────────────────────────────────────────────────────

def week1_student():
    return notebook([

        md("""\
# Week 1 Lab: Functions and the Language of Scientific Analysis
**SCIE1500 — Analytical Methods for Scientists | Semester 2, 2026**

**Group:** _________________ &nbsp;&nbsp; **Lab Instructor:** _________________ &nbsp;&nbsp; **Date:** _________________

---

> **How this notebook works:** Read each section, then run the code cells in order by pressing **Shift + Enter** (or the ▶ button).
> Work through this as a group — discuss every answer before writing it down.
> If a cell gives an unexpected result, re-read the text above it before asking for help."""),

        md("""\
---
## 🌊 Scientific Scenario: Global Plastic Production

The United Nations Environment Programme (UNEP) is preparing a report on plastic waste in oceans. You are part of a team analysing historical data on global plastic production.

**Data: Global plastic production (million tonnes)**

| Year | 1950 | 1970 | 1990 | 2010 | 2015 |
|------|------|------|------|------|------|
| Production (Mt) | 2 | 35 | 120 | 270 | 380 |

The relationship between year and production can be modelled as a function $P(t)$, where $t$ is years since 1950.

*Over the course of this lab you will:*
1. Build and interrogate this function mathematically
2. Visualise it in Python
3. Use it to evaluate an Australian policy question"""),

        md("""\
---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Explore function basics: compute average rates of change, domain and range | ~20 min |
| B | Interpret slope to explain how growth changes across decades | ~15 min |
| C | Apply functions to analyse population growth and mismanagement rates | ~20 min |

**By the end of this lab you should be able to:**
- Define a mathematical function and state its domain and range
- Calculate and interpret average rates of change with units
- Write and call a Python function
- Plot a dataset and read trends from a graph"""),

        md("""\
### Before you start: loading the tools

The cell below loads two Python libraries we need today:
- **numpy** (`np`): handles arrays of numbers and mathematical operations
- **matplotlib** (`plt`): creates plots and graphs

Run it now — you should see a short confirmation message. If you see an error instead, raise your hand."""),

        md("""\
Run this cell first — it loads the libraries we need through."""),

        code("""\
# Run this cell first — it loads the libraries we need throughout the lab
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams['figure.dpi'] = 100

print("Libraries loaded successfully!")"""),

        md("""\
---
## Part A: Function Basics (~20 min)

### What is a function?

A **function** $f$ assigns to each valid input $x$ exactly one output $f(x)$.
We write: $f : \\text{Domain} \\to \\text{Range}$

- The **domain** is the set of all valid inputs.
- The **range** is the set of all possible outputs.

For the plastic production data, we define:
$$P(t) = \\text{production (million tonnes)}, \\quad t = \\text{years since 1950}$$

So $P(0) = 2$, $P(20) = 35$, $P(65) = 380$, etc."""),

        md("""\
### Loading the data into Python

Python stores sequences of numbers as **arrays** — you can think of them like a column of values in a spreadsheet. We use `np.array([...])` to create them.

Run the cell below. It creates two arrays (one for $t$, one for $P$) and prints them side by side so you can confirm the values match the table above."""),

        md("""\
The data from the UNEP report."""),

        code("""\
# The data from the UNEP report
t_values = np.array([0, 20, 40, 60, 65])    # years since 1950
P_values = np.array([2, 35, 120, 270, 380])  # million tonnes

# Convert t back to calendar years for readability
years = 1950 + t_values

print("Year:       ", years)
print("t (yrs):    ", t_values)
print("P(t) (Mt):  ", P_values)"""),

        md("""\
### A.1 Average Rate of Change

The **average rate of change** of $P$ from $t = a$ to $t = b$ is:
$$\\frac{P(b) - P(a)}{b - a}$$

This is the slope of the straight line joining the two points $(a, P(a))$ and $(b, P(b))$.
Its units here are: **million tonnes per year**.

We'll compute this for the full 65-year period (1950 to 2015) first."""),

        md("""\
**What to expect:** We're computing a single number — the average slope over 65 years. It tells us how fast production was growing *on average* across the whole period. Run the cell and read the result before moving on."""),

        code("""\
# Average rate of change from 1950 to 2015 (t = 0 to t = 65)
P_1950 = 2     # P(0)
P_2015 = 380   # P(65)
delta_t = 65

avg_rate = (P_2015 - P_1950) / delta_t

# Raw output first — just the number
print("Average rate of change:", avg_rate)
print("Units: million tonnes per year")"""),

        md("""\
### A.2 Domain and Range

✏️ **Activity A.2 — Answer as a group:**

1. What is the **mathematical domain** of $P(t)$?
   *(All values of $t$ for which the formula is defined)*

2. What is the **physical domain**?
   *(Values of $t$ that make sense for plastic production — when did production start? Can $t$ be negative?)*

3. What is the approximate **range** of $P$ based on the data?

Write your answers in the cell below (use `#` to comment them out — Python will skip commented lines)."""),

        md("""\
A.2 GROUP ANSWERS — replace the ... with your answers."""),

        code("""\
# A.2 GROUP ANSWERS — replace the ... with your answers

# 1. Mathematical domain:
#    ...

# 2. Physical domain (realistic t values):
#    ...

# 3. Range of P based on the data:
#    ...
"""),

        md("""\
---
## Part B: Interpreting Slope (~15 min)

The overall average rate from Part A (1950–2015) hides a lot of detail.
Does production grow at the same pace in every decade, or does the rate change over time?

**We'll find out by computing the average rate for each 20-year period separately.**"""),

        md("""\
### B.1 — One decade by hand first

Before looking at all four periods at once, let's do the 1950–1970 calculation manually so the arithmetic is visible. This is the same formula as A.1, just applied to a shorter window."""),

        md("""\
Rate of change for 1950–1970 only (t = 0 to t = 20)."""),

        code("""\
# Rate of change for 1950–1970 only (t = 0 to t = 20)
P_at_0  = P_values[0]    # P(0)  — first element of the array
P_at_20 = P_values[1]    # P(20) — second element

rate_1950_70 = (P_at_20 - P_at_0) / (20 - 0)

print("Production in 1950:", P_at_0, "Mt")
print("Production in 1970:", P_at_20, "Mt")
print("Rate of change (1950-1970):", rate_1950_70, "Mt/yr")"""),

        md("""\
### B.1 — All four periods

Now a **loop** repeats the same three-line calculation for each period automatically.
Each time through the loop, `t1`, `t2`, and `label` take the next row of values from the list.

The output uses `f"..."` — an *f-string* — to embed the variable values directly in text.
`:.2f` means "show 2 decimal places". You'll see this format again in later labs."""),

        md("""\
Calculate average rate of change for all four periods."""),

        code("""\
# Calculate average rate of change for all four periods
periods = [
    (0,  20, '1950–1970'),
    (20, 40, '1970–1990'),
    (40, 60, '1990–2010'),
    (60, 65, '2010–2015'),
]

print(f"{'Period':<12}  {'Rate (Mt/yr)':>14}")
print("-" * 30)
for t1, t2, label in periods:
    P1 = P_values[t_values == t1][0]    # find P at t = t1
    P2 = P_values[t_values == t2][0]    # find P at t = t2
    rate = (P2 - P1) / (t2 - t1)
    print(f"  {label:<12}  {rate:>12.2f}")"""),

        md("""\
✏️ **Activity B.1 — Answer as a group:**

1. Is the rate of change constant across decades? What does this tell you about the shape of $P(t)$?

2. The 2010–2015 rate looks lower than 1990–2010 — but can you trust this comparison?
   *(Hint: think about what the different time intervals mean for the calculation.)*

Write your answers below."""),

        md("""\
B.1 GROUP ANSWERS."""),

        code("""\
# B.1 GROUP ANSWERS

# 1. Is the rate constant? What does this imply about the shape of P(t)?
#    ...

# 2. Why might the 2010–2015 comparison be misleading?
#    ...
"""),

        md("""\
### B.2 Plotting P(t)

A graph often reveals patterns that a table of numbers hides. Let's plot the data.

**Reading the code below:**
- `fig, ax = plt.subplots()` — creates a blank figure and axes (canvas + coordinate system)
- `ax.scatter(...)` — draws the five data points as dots
- `ax.plot(...)` — draws connecting line segments between the points
- `ax.set_xlabel / ylabel / title` — labels the axes and adds a title

Run it, then look at the shape before answering the activity below."""),

        md("""\
Run the next cell."""),

        code("""\
fig, ax = plt.subplots()
ax.scatter(1950 + t_values, P_values, color='steelblue', s=80, zorder=5, label='Data points')
ax.plot(1950 + t_values, P_values, color='steelblue', linewidth=1.5, alpha=0.6)

ax.set_xlabel('Year')
ax.set_ylabel('Production (million tonnes)')
ax.set_title('Global Plastic Production, 1950–2015')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity B.2 — Answer as a group:**
1. Does the graph look linear (straight) or curved? How does this match what the rates in B.1 told you?
2. If you extended this graph to 2030, what shape would you expect? Why?

```
Answers:
1. ...
2. ...
```"""),

        md("""\
---
## Part C: Australian Policy Application (~20 min)

Now we apply what we know about functions and rates of change to a real policy question.

**Context:**
Australia's coastal population in 2010 was approximately 20 million, with each person generating 50 kg of plastic waste per year. Of this waste, **2% is mismanaged** (enters the ocean).

We'll work in three steps:
1. Calculate the baseline (how much waste enters the ocean in 2010)
2. Build a function $W(t)$ that projects this forward as population grows
3. Test whether a government policy reduces waste enough to make a difference

**Define $t$ = years since 2010 for this part.**"""),

        md("""\
### Step 1: Baseline waste in 2010

Before building a model, let's compute the 2010 starting point in plain arithmetic — no functions yet. We multiply population × plastic per person × mismanagement rate, then convert kg to tonnes."""),

        md("""\
Given values."""),

        code("""\
# Given values
population_2010 = 20e6       # 20 million people  (20e6 = 20,000,000)
plastic_per_person_kg = 50   # kg/person/year
mismanagement_rate = 0.02    # 2%

# Annual mismanaged plastic entering the ocean (kg, then convert to tonnes)
annual_waste_kg     = population_2010 * plastic_per_person_kg * mismanagement_rate
annual_waste_tonnes = annual_waste_kg / 1000

print("Annual mismanaged plastic (tonnes):", annual_waste_tonnes)
print("Daily mismanaged plastic (tonnes):", annual_waste_tonnes / 365)"""),

        md("""\
### Step 2: Writing the function W(t)

If Australia's coastal population grows at **1.5% per year**, then at time $t$ years after 2010:
$$\\text{Population}(t) = 20{,}000{,}000 \\times 1.015^t$$

✏️ **Activity C.1:** What is the full formula for $W(t)$, annual mismanaged plastic (tonnes/year), as a function of $t$?

In Python, `def` packages a formula under a name. Once defined, calling `W(10)` substitutes $t = 10$ and returns the result. The structure below already has the population formula — your job is to read it and confirm it matches what you expect."""),

        md("""\
W(0) should match the 2010 value you computed above."""),

        code("""\
def W(t):
    'Annual mismanaged plastic waste (tonnes/year), t years after 2010.'
    population_t = 20e6 * 1.015**t                              # population grows 1.5%/yr
    waste = population_t * plastic_per_person_kg * mismanagement_rate / 1000  # kg -> tonnes
    return waste

# W(0) should match the 2010 value you computed above
print("W(0) =", W(0))      # baseline -- does it match?
print("W(10) =", W(10))    # projection for 2020
print("W(20) =", W(20))    # projection for 2030"""),

        md("""\
### Step 3: Testing the policy

The government proposes reducing the mismanagement rate from **2% to 0.5%** by 2030.
We define a second function $W_{\\text{policy}}(t)$ — identical to $W(t)$ except for the mismanagement rate.

✏️ **Activity C.2:** Before running the cell, predict: will the policy bring 2030 waste *below* the 2010 level? Discuss with your group, then check."""),

        md("""\
Compare at 2030 (t = 20)."""),

        code("""\
def W_policy(t):
    'Annual mismanaged waste (tonnes/year) under the 0.5% policy.'
    population_t   = 20e6 * 1.015**t
    policy_rate    = 0.005      # 0.5% — the only change from W(t)
    waste = population_t * plastic_per_person_kg * policy_rate / 1000
    return waste

# Compare at 2030 (t = 20)
t_2030 = 20
print(f"Business as usual in 2030:    {W(t_2030):>10,.0f} tonnes/year")
print(f"Policy scenario in 2030:      {W_policy(t_2030):>10,.0f} tonnes/year")
print(f"2010 baseline:                {W(0):>10,.0f} tonnes/year")
print()
diff = W_policy(t_2030) - W(0)
direction = "above" if diff > 0 else "below"
print(f"Policy 2030 is {abs(diff):,.0f} tonnes/year {direction} the 2010 baseline.")"""),

        md("""\
✏️ **Group discussion — write your conclusion below:**

Does the 2% → 0.5% reduction fully offset the effect of 1.5%/year population growth?
What does this suggest about the effectiveness of mismanagement-reduction policies alone?"""),

        md("""\
GROUP CONCLUSION."""),

        code("""\
# GROUP CONCLUSION

# Does the policy fully offset population growth? (yes / no / partially)
#    ...

# In one sentence, what does this imply for ocean plastic policy?
#    ...
"""),

        md("""\
### C.3 Visualise the Two Scenarios

The plot below shows both trajectories from 2010 to 2040. Look for:
- Where the two lines diverge (the effect of the policy kicks in immediately)
- Whether the policy line ever drops back to the 2010 baseline (horizontal dashed line)"""),

        md("""\
Mark the 2010 baseline for reference."""),

        code("""\
t_range = np.linspace(0, 30, 100)

fig, ax = plt.subplots()
ax.plot(2010 + t_range, [W(t) for t in t_range],
        label='Business as usual (2% mismanagement)', color='tomato', linewidth=2)
ax.plot(2010 + t_range, [W_policy(t) for t in t_range],
        label='Policy scenario (0.5% mismanagement)', color='steelblue', linewidth=2, linestyle='--')

# Mark the 2010 baseline for reference
ax.axhline(W(0), color='gray', linestyle=':', alpha=0.7, label='2010 baseline')

ax.set_xlabel('Year')
ax.set_ylabel('Mismanaged plastic (tonnes/year)')
ax.set_title("Australia's Ocean Plastic Waste — Two Scenarios")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## ✅ Lab Wrap-Up

Before finishing, check that your group has:

- [ ] Stated the domain and range of $P(t)$ (Part A)
- [ ] Calculated rates of change for all four periods and explained the pattern (Part B)
- [ ] Written and tested the function $W(t)$ in Python (Part C)
- [ ] Compared the two policy scenarios with a plot (Part C)
- [ ] Written a group conclusion about the policy effectiveness (Part C)

**Self-check questions (discuss — no submission needed):**

1. Can a relation assign two different outputs to the same input and still be a function? Why / why not?
2. The slope from 1950–1970 is much lower than from 1990–2010. Does this mean plastic wasn't a problem in the 1950s?
3. What additional data would you need to make $W(t)$ more accurate?

> **Next week:** We'll study exponential and logarithmic models — which turn out to describe
> plastic production far better than a linear model does."""),
    ])

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 2 — Exponential & Logarithmic Functions
# ─────────────────────────────────────────────────────────────────────────────

def week2_student():
    return notebook([

        md("""\
# Week 2 Lab: Doubling Times — From Plastic to Pandemics
**SCIE1500 — Analytical Methods for Scientists | Semester 2, 2026**

> **Lab format:** Work in your group. Discuss answers before typing code.
> **Today's session:** ~2 hours | Ask your tutor when stuck."""),

        md("""\
---
## 🌍 Scientific Scenario

Your team is preparing educational materials comparing **exponential growth** across three domains — to help policymakers understand why percentage growth rates can be deceptive and why early intervention matters.

| Domain | System | Behaviour |
|--------|--------|-----------|
| Environment | Global plastic production | 8.4% annual growth since 1950 |
| Biology | *E. coli* bacteria | Doubles every 20 minutes |
| Physics | Carbon-14 | Half-life 5,730 years (decay) |

> *All three follow the same mathematical structure — exponential functions — differing only in timescale and direction.*"""),

        md("""\
---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Build exponential models for all three scenarios | ~25 min |
| B | Calculate doubling times and verify the Rule of 70 | ~15 min |
| C | Use logarithms to find when thresholds are crossed | ~15 min |

**By the end of today you will be able to:**
- Write exponential models in both $P_0 e^{kt}$ and $P_0 b^t$ form and convert between them
- Derive the doubling time formula and apply the Rule of 70
- Use logarithms to solve for unknown time in any exponential scenario"""),

        code(SETUP_IMPORTS),

        md("""\
---
## Part A: Exponential Models (~25 min)

The general exponential model is:
$$P(t) = P_0 \\, e^{kt}, \\qquad k > 0 \\text{ (growth)}, \\quad k < 0 \\text{ (decay)}$$

An equivalent form is $P(t) = P_0 \\, b^t$ where $b = e^k$. All three scenarios in today's lab use this same structure — they differ only in what $P_0$, $k$, and $t$ represent."""),

        md("""\
### A.1 — Plastic Production

We know plastic grew at **8.4% per year** since 1950, starting from 2 million tonnes. But that 8.4% is a *discrete* annual rate — our model needs a *continuous* rate $k$.

The conversion is: $k = \\ln(1 + r)$, where $r$ is the decimal rate (0.084 here). Run the cell below, look at the raw value of $k$, then use it to predict production in 2025."""),

        md("""\
Plastic production: 8.4% annual growth, P0 = 2 M tonnes in 1950."""),

        code("""\
# A.1 — Plastic production: 8.4% annual growth, P0 = 2 M tonnes in 1950
P0_plastic = 2        # million tonnes in 1950
r = 0.084             # 8.4% per year as a decimal

k_plastic = np.log(1 + r)           # k = ln(1 + r)
print("k_plastic =", k_plastic)     # raw value first

# How much plastic in 2025? t = 2025 - 1950 = 75 years
t_2025 = 2025 - 1950
P_2025 = P0_plastic * np.exp(k_plastic * t_2025)
print("Predicted 2025 production (million tonnes):", P_2025)
print("Actual ~500 M tonnes — is the model a good fit?")"""),

        md("""\
✏️ **Activity A.1:**
1. In 2015 (t = 65 years), actual production was ~380 M tonnes. Evaluate the model at t = 65 and compare.
2. What does $k \\approx 0.0807$ mean in plain English?

```python
# A.1 answers — fill in the blanks
P_2015 = P0_plastic * np.exp(k_plastic * 65)
print("Model at 2015:", P_2015)
# 1. Model vs actual:
#    ...
# 2. Interpretation of k:
#    ...
```"""),

        md("""\
### A.2 — Bacterial Growth

For bacteria we're given the **doubling time** directly (every 20 minutes for *E. coli*). This lets us write the model in two equivalent forms:

- **Doubling form:** $N(t) = N_0 \\times 2^{t/T_{\\text{double}}}$ — reads naturally as "doubles every 20 min"
- **Continuous-rate form:** $N(t) = N_0 \\, e^{kt}$ where $k = \\ln(2)/T_{\\text{double}}$

Both forms describe exactly the same population at every time $t$. The cell below runs both side by side so you can confirm they agree."""),

        md("""\
Bacterial growth: N0 = 1000 cells, doubles every 20 minutes."""),

        code("""\
# A.2 — Bacterial growth: N0 = 1000 cells, doubles every 20 minutes
N0 = 1000
T_double = 20          # doubling time in minutes

k_bact = np.log(2) / T_double
print(f"k = ln(2)/20 = {k_bact:.4f} per minute")

def N_v1(t): return N0 * 2**(t / T_double)      # doubling form
def N_v2(t): return N0 * np.exp(k_bact * t)     # continuous-rate form

print()
print("Both forms should give identical counts:")
for t_hrs in [1, 2, 3]:
    t = t_hrs * 60
    print(f"  t = {t_hrs}h ({t} min):  doubling form = {N_v1(t):.0f}   k-form = {N_v2(t):.0f}")"""),

        md("""\
✏️ **Activity A.2:**
1. How many cells after 3 hours? After how many minutes do you first exceed 1 million cells?
2. Starting from 1,000 cells, how many doublings are needed to reach 1 billion?

```python
# A.2 answers
# 1. Time to 1 million cells:
t_million = T_double * np.log2(1_000_000 / N0)
print("Minutes to 1 million:", t_million)
# 2. Doublings needed:
#    ...
```"""),

        md("""\
### A.3 — Carbon-14 Decay

Radioactive decay follows the same exponential law as growth, but the quantity **shrinks** over time. The model is:
$$A(t) = A_0 \\, e^{-\\lambda t}$$
where $\\lambda = \\ln(2)/T_{\\text{half}}$ is the *decay constant* — a positive number. The **negative sign in the exponent** is what makes the function decrease rather than increase.

For Carbon-14 (half-life 5,730 years): after each half-life, exactly 50% remains. We'll check this algebraically and verify with code."""),

        md("""\
Carbon-14 decay: A0 = 100 units, half-life = 5,730 years."""),

        code("""\
# A.3 — Carbon-14 decay: A0 = 100 units, half-life = 5,730 years
A0_c14 = 100            # initial amount (treat as % of original)
T_half = 5730           # years

lambda_c14 = np.log(2) / T_half    # decay constant λ (positive)

def A_c14(t):
    return A0_c14 * np.exp(-lambda_c14 * t)    # negative exponent → decreasing

print(f"Decay constant λ = ln(2)/5730 = {lambda_c14:.6f} per year")
print()
print("Checking successive half-lives (should halve each time):")
for n in [1, 2, 3]:
    t = n * T_half
    print(f"  After {n} half-life(s) ({t:,} years):  A = {A_c14(t):.2f}   expected = {100 / 2**n:.2f}")"""),

        md("""\
✏️ **Activity A.3:**
1. Confirm: after 2 half-lives, exactly 25% remains. Does the code agree?
2. Why is the exponent **negative** for decay but **positive** for growth?

```python
# A.3 answers:
# 1. After 2 half-lives:
print("After 2 half-lives:", A_c14(2 * T_half))
# 2. Why negative:
#    ...
```"""),

        md("""\
---
## Part B: Doubling Time & the Rule of 70 (~15 min)

For any exponential growth model $P(t) = P_0 e^{kt}$, setting $P(T) = 2P_0$ and solving gives the **exact doubling time**:
$$T_{\\text{double}} = \\frac{\\ln 2}{k}$$

For percentage rates (small $r$), this simplifies to the **Rule of 70**:
$$T_{\\text{double}} \\approx \\frac{70}{r} \\quad (r \\text{ in percent})$$

The Rule of 70 is a useful mental shortcut — but how accurate is it, and when does it break down?"""),

        md("""\
### B.1 — Comparing Exact Formula vs Rule of 70

We'll first check the Rule for our plastic scenario (8.4% growth), then scan a range of growth rates.

**Note on the table below:** The code uses column alignment specifiers like `>9` (right-align in 9 characters). You'll see these again in later labs — for now, just read the output and notice how error grows with rate."""),

        md("""\
How accurate is Rule of 70 for plastic growth (8.4% per year)?"""),

        code("""\
# B.1 — How accurate is Rule of 70 for plastic growth (8.4% per year)?
r_pct = 8.4

T_exact  = np.log(2) / k_plastic
T_rule70 = 70 / r_pct

print(f"Exact doubling time:      {T_exact:.2f} years")
print(f"Rule of 70 approximation: {T_rule70:.2f} years")
print(f"Error: {abs(T_exact - T_rule70) / T_exact * 100:.1f}%")

# Scan across a range of growth rates
print()
print(f"{'Rate':>8} | {'Exact (y)':>9} | {'Rule 70':>7} | {'Error':>6}")
print("-" * 40)
for r in [1, 2, 4, 8.4, 10, 15, 20]:
    T_e = np.log(2) / np.log(1 + r / 100)
    T_r = 70 / r
    print(f"{r:>7.1f}% | {T_e:>9.2f} | {T_r:>7.2f} | {abs(T_e - T_r) / T_e * 100:>5.1f}%")"""),

        md("""\
✏️ **Activity B.1:**
1. At what growth rates is the Rule of 70 most accurate? When does it break down and why?
2. For bacteria doubling every 20 min, what is the **annual** equivalent percentage growth rate?
   *(Hint: 1 year ≈ 525,600 minutes. The per-minute k is already computed as `k_bact`.)*

```python
# B.1 answers:
# 1. Accuracy pattern:
#    ...
# 2. Annual rate for bacteria:
k_per_year = k_bact * 525600
annual_pct = (np.exp(k_per_year) - 1) * 100
print(f"Annual equivalent: {annual_pct:.2e}%")
```"""),

        md("""\
### B.2 — Logarithmic Solving: When Are Thresholds Crossed?

Until now we've asked "how much at time t?" — plugging t into the model.
Now we flip the question: **"when does the population reach a given target?"**

Starting from $P_0 e^{kt} = C$, taking logarithms of both sides gives:
$$t = \\frac{\\ln(C / P_0)}{k}$$

We'll apply this to find when global plastic production crosses two major milestones."""),

        md("""\
When does plastic production reach 1 billion and 10 billion tonnes?"""),

        code("""\
# B.2 — When does plastic production reach 1 billion and 10 billion tonnes?
def years_to_reach(target_M):
    t = np.log(target_M / P0_plastic) / k_plastic
    return t, 1950 + t

t_1b,  yr_1b  = years_to_reach(1_000)     # 1 billion = 1,000 M tonnes
t_10b, yr_10b = years_to_reach(10_000)    # 10 billion = 10,000 M tonnes

print(f"1 billion tonnes:  t = {t_1b:.1f} years from 1950  →  year {yr_1b:.0f}")
print(f"10 billion tonnes: t = {t_10b:.1f} years from 1950  →  year {yr_10b:.0f}")
print()
print("Caveat: these projections assume constant 8.4% growth indefinitely.")
print("Discuss with your group: is that realistic?")"""),

        md("""\
---
## Part C: Practice — Applying the Pattern (~15 min)

You now have all the tools: build the model, evaluate forward, or solve backwards with logarithms.
**Pattern to remember:** write model → set equal to target → take log → solve for t."""),

        md("""\
### C.1 — Invasive Carp

An invasive carp population is modelled as $P(t) = 50 \\, e^{0.15t}$ (t in months).
Ecologists warn that once the population exceeds **1,000 fish**, manual eradication becomes infeasible.
We'll find when several thresholds are crossed, then plot the full trajectory to see the window for intervention."""),

        md("""\
Invasive carp: P(t) = 50 * e^(0.15t), t in months."""),

        code("""\
# C.1 — Invasive carp: P(t) = 50 * e^(0.15t), t in months
P0_carp = 50
k_carp  = 0.15
limit   = 1000     # eradication becomes infeasible above this

def carp(t): return P0_carp * np.exp(k_carp * t)
def t_to_reach(target): return np.log(target / P0_carp) / k_carp

print("Time to reach each threshold:")
for target in [500, 1000, 5000]:
    t = t_to_reach(target)
    print(f"  {target:>5} fish:  {t:.1f} months  ({t / 12:.1f} years)")
        """),

        md("""\
The chart below shows the growth trajectory."""),

        code("""\
# Plot the growth trajectory
t_vals = np.linspace(0, 55, 300)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_vals, carp(t_vals), "steelblue", lw=2)
ax.axhline(limit, color="red", ls="--", label=f"Eradication limit ({limit} fish)")
ax.axvline(t_to_reach(limit), color="orange", ls=":",
           label=f"Limit at t = {t_to_reach(limit):.0f} months")
ax.set_xlabel("Time (months)")
ax.set_ylabel("Carp population")
ax.set_title("Invasive Carp Population Growth")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
### C.2 — Carbon Dating

Carbon dating works *backwards* through the decay model: given the fraction of C-14 that remains, we solve for the sample's age. If fraction $f$ remains:
$$f \\cdot A_0 = A_0 \\, e^{-\\lambda t} \\implies t = \\frac{-\\ln(f)}{\\lambda}$$

Note: the $A_0$ cancels — we only need the *fraction* remaining, not the original amount."""),

        md("""\
A fossil has 25% of its original C-14 remaining. How old is it?"""),

        code("""\
# C.2 — A fossil has 25% of its original C-14 remaining. How old is it?
fraction = 0.25

t_fossil = -np.log(fraction) / lambda_c14
print(f"25% remaining → age = {t_fossil:.0f} years")
print(f"That is {t_fossil / T_half:.2f} half-lives")

# Try your own value:
# my_fraction = 0.10        # 10% remaining
# print(f"At 10%: age = {-np.log(my_fraction) / lambda_c14:.0f} years")"""),

        md("""\
---
## ✅ Lab Wrap-Up

Before finishing, confirm your group has:

- [ ] Built exponential models for all three scenarios (Part A)
- [ ] Verified both forms ($P_0 e^{kt}$ and $P_0 b^t$) give the same answer (A.2)
- [ ] Applied the Rule of 70 and noted when it breaks down (Part B)
- [ ] Solved for unknown time using logarithms (Parts B.2, C)
- [ ] **Groups 1 & 2:** Opened your assigned Presentation Brief (Lab A or Lab B) and started Part A

> 💡 **Key pattern:** *Write the model → set equal to target → take log → solve for t.* This three-step process works across every exponential scenario."""),
    ])


def week2_lab_a():
    return notebook([

        md("""\
# Week 2 Presentation Brief — Variation A
## 🦠 Bacterial Growth: The Hospital Infection Challenge
**SCIE1500 — Semester 2, 2026 | Group 1 — presenting in Week 3**

> Work through all parts during the Week 2 lab. Your **10-minute Week 3 presentation** should cover: the problem, your model, key results, and policy implications.
> Do not show raw code in your presentation — show graphs and equations."""),

        md("""\
---
## 📋 Scenario

You are a consultant for **Royal Perth Hospital's** infection control team. A strain of antibiotic-resistant *Staphylococcus aureus* (MRSA) has been detected on a surgical instrument.

- Doubling time at room temperature: **25 minutes**
- Initial contamination: **800 cells**
- **Hospital policy:** If count exceeds **1,000,000 cells**, the surgical suite shuts down for sterilization — cost: $50,000 + 48-hour delay.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Build growth models in two forms; find shutdown time | ~20 min |
| B | Model the effect of refrigeration on bacterial growth | ~15 min |
| C | Make a sterilisation decision and write a policy recommendation | ~10 min |
| D | Verify the Rule of 70 for this scenario | ~10 min |"""),

        md("""\
### Getting started — what does the model look like?

We're modelling MRSA growing exponentially from an initial count of 800 cells. Because we know the **doubling time** (25 minutes at room temperature), we can write:

$$N(t) = 800 \\times 2^{t/25}$$

or equivalently, converting to the continuous-rate form with $k = \\ln(2)/25$:

$$N(t) = 800 \\, e^{kt}$$

Run the setup cell to define these parameters and check what $k$ looks like numerically."""),

        md("""\
Setup — run first."""),

        code("""\
# Setup — run first
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'figure.dpi': 120, 'font.size': 11})

N0        = 800
T_room    = 25           # doubling time at room temperature (minutes)
threshold = 1_000_000    # shutdown threshold (cells)

k_room = np.log(2) / T_room
print("k_room =", k_room)           # raw value — continuous growth rate per minute
print("N0 =", N0, "cells")
print("Shutdown threshold:", threshold, "cells")"""),

        md("""\
---
## Part A: Modeling Bacterial Growth (~20 min)

We'll write the growth model in both forms and verify they give identical results, then find when the population hits the shutdown threshold."""),

        md("""\
### A.1 — Two equivalent forms of the model

Define both forms as Python functions, then evaluate them at 1, 2, and 3 hours to confirm they agree. Note: at room temperature, each 25-minute interval is one doubling — so after 1 hour (60 min) there are $60/25 = 2.4$ doublings."""),

        md("""\
Both forms of the growth model."""),

        code("""\
# A.1 — Both forms of the growth model
def N_v1(t): return N0 * 2**(t / T_room)         # doubling form
def N_v2(t): return N0 * np.exp(k_room * t)      # continuous-rate form

print("Verifying both forms agree:")
for t_h in [1, 2, 3]:
    t = t_h * 60
    print(f"  t = {t_h}h ({t} min):  2^(t/T) = {N_v1(t):.0f}   e^(kt) = {N_v2(t):.0f}")"""),

        md("""\
### A.2 — Finding the shutdown time

We need to find when $N(t) = 1{,}000{,}000$. Starting from the doubling form:
$$800 \\times 2^{t/25} = 1{,}000{,}000$$

Taking $\\log_2$ of both sides and solving for $t$ gives $t = 25 \\times \\log_2(1{,}000{,}000 / 800)$.

After computing the shutdown time, we'll plot the full growth curve on a **log scale** — this makes exponential growth appear as a straight line and makes the threshold easy to read off."""),

        md("""\
Time to reach shutdown threshold."""),

        code("""\
# A.2 — Time to reach shutdown threshold
t_shutdown = T_room * np.log2(threshold / N0)
print(f"Time to shutdown threshold: {t_shutdown:.1f} minutes = {t_shutdown / 60:.2f} hours")

t_vals = np.linspace(0, 350, 600)
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_vals, N_v1(t_vals), "steelblue", lw=2, label="MRSA count (room temp)")
ax.axhline(threshold, color="red",    ls="--", lw=1.5, label=f"Shutdown threshold (1M cells)")
ax.axvline(t_shutdown, color="orange", ls=":",  lw=1.5, label=f"Threshold at {t_shutdown:.0f} min")
ax.set_yscale("log")
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Bacterial count (log scale)")
ax.set_title("MRSA Growth — Royal Perth Hospital")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Group discussion A:**
1. Express the shutdown time as "X hours and Y minutes". If contamination is detected at 8:00 AM, what is the latest safe action time?
2. Why does the log scale make this plot more informative than a linear scale?

```python
# Answers:
# 1. Hours and minutes:
hrs = int(t_shutdown // 60)
mins = t_shutdown % 60
print(f"Shutdown at {hrs}h {mins:.0f}min")
# 2. Why log scale:
#    ...
```"""),

        md("""\
---
## Part B: Effect of Refrigeration (~15 min)

At **4°C**, bacterial growth slows significantly — the doubling time increases from 25 minutes to **180 minutes**. We model this as a separate exponential function with a smaller $k$. The question for the hospital: does refrigeration buy enough time to make a considered decision?"""),

        md("""\
### B.1 — Comparing room temperature vs refrigerated growth

We'll compute the new $k$ for 4°C, plot both growth curves on the same axes, and calculate the shutdown time for each condition. The ratio of shutdown times tells us directly how much time refrigeration buys."""),

        md("""\
Cold storage model (4°C, doubling time = 180 min)."""),

        code("""\
# B.1 — Cold storage model (4°C, doubling time = 180 min)
T_cold = 180
k_cold = np.log(2) / T_cold

def N_cold(t): return N0 * np.exp(k_cold * t)

t_shutdown_cold = T_cold * np.log2(threshold / N0)
print(f"Room temp: shutdown at {t_shutdown:.1f} min ({t_shutdown / 60:.2f} h)")
print(f"At 4°C:    shutdown at {t_shutdown_cold:.0f} min ({t_shutdown_cold / 60:.1f} h)")
print(f"Refrigeration buys {t_shutdown_cold / t_shutdown:.1f}x more time")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t_vals, N_v1(t_vals),   "steelblue", lw=2, label=f"Room temp (T = {T_room} min)")
ax.plot(t_vals, N_cold(t_vals), "seagreen",  lw=2, label=f"4°C refrigerated (T = {T_cold} min)")
ax.axhline(threshold, color="red", ls="--", label="Shutdown threshold")
ax.set_yscale("log")
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Bacterial count (log scale)")
ax.set_title("MRSA Growth: Room Temp vs Refrigeration")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Group discussion B:**
1. Can the hospital safely refrigerate overnight (8 hours = 480 min) before deciding?
2. What does this imply for hospital protocols about instrument handling?

```python
# Answers:
# 1. Count after 8h refrigeration:
print("Count after 8h cold:", N_cold(480))
print("Still below threshold?", N_cold(480) < threshold)
# 2. Protocol implication:
#    ...
```"""),

        md("""\
---
## Part C: Sterilization Decision (~10 min)

The hospital administrator faces a choice:
- **Option 1:** Immediate sterilization — $50,000 + 48-hour delay
- **Option 2:** Refrigerate for 12 hours, re-test, then decide

Your job is to determine what the bacterial count will be after 12 hours of refrigeration, then make a data-backed recommendation."""),

        code("""\
# C.1 — Bacterial count after 12 hours of refrigeration
t_12h = 12 * 60       # convert to minutes
N_after = N_cold(t_12h)

print("Count after 12h refrigeration:", round(N_after))
print("Still below threshold?", N_after < threshold)
print(f"Safety margin: {threshold / N_after:.1f}x below threshold")"""),

        md("""\
✏️ **Policy recommendation (write as a group):**

Write 3–4 sentences recommending Option 1 or Option 2 to the hospital administrator. Include:
- Which option you recommend and why
- Specific numbers supporting the recommendation
- One key uncertainty or limitation in your model

```
RECOMMENDATION:
...
```"""),

        md("""\
---
## Part D: Rule of 70 Verification (~10 min)

We claimed the doubling time is 25 minutes. But the Rule of 70 is an *approximation* based on the percentage growth rate. How well does it hold up for bacterial growth?

The key step: find the exact per-minute percentage growth rate from $k$, then apply $T \\approx 70/r$."""),

        code("""\
# D.1 — Exact % growth per minute vs Rule of 70 prediction
r_per_min_pct = (np.exp(k_room) - 1) * 100    # exact per-minute % rate

T_rule70 = 70 / r_per_min_pct

print(f"Exact % growth per minute:  {r_per_min_pct:.4f}%")
print(f"Rule of 70 doubling time:   {T_rule70:.2f} min")
print(f"Actual doubling time:       {T_room} min")
print(f"Error: {abs(T_rule70 - T_room) / T_room * 100:.1f}%")
print()
print("Note: the Rule of 70 works best for small percentage rates per period.")
print("Per-minute bacterial growth is large, so the approximation is less accurate.")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 3, 10 minutes)

1. **The Problem** (~2 min): What question were you answering?
2. **The Model** (~3 min): Why exponential? Show the equation and what $k$ means physically.
3. **Key Results** (~3 min): Shutdown times at room temp and refrigerated — show the comparison plot.
4. **Implications** (~2 min): What should hospital administrators take away?

> **Tips:** Speak to numbers — "the hospital has X hours" is more compelling than "t equals...". Practice timing."""),
    ])


def week2_lab_b():
    return notebook([

        md("""\
# Week 2 Presentation Brief — Variation B
## ☢️ Radioactive Waste: The Fukushima Legacy
**SCIE1500 — Semester 2, 2026 | Group 2 — presenting in Week 3**

> Work through all parts during the Week 2 lab. Your **10-minute Week 3 presentation** should cover: the problem, your model, key results, and policy implications.
> Do not show raw code in your presentation — show graphs and equations."""),

        md("""\
---
## 📋 Scenario

You are advising the **Japanese government** on long-term storage of radioactive waste from the Fukushima disaster. The primary isotope of concern is **Caesium-137** (half-life: **30.17 years**).

- Initial container activity: **500 TBq** (terabecquerels)
- **Regulatory threshold:** Activity must drop below **10 TBq** before the container can be reclassified as "low-level waste" (enabling cheaper storage).

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Build decay models in two forms; find reclassification year | ~20 min |
| B | Add Sr-90 isotope; find when activities equalise | ~15 min |
| C | Analyse storage costs over 150 years | ~10 min |
| D | Apply carbon dating to connect half-life to an archaeological question | ~10 min |"""),

        md("""\
### Getting started — what does the model look like?

Radioactive decay is exponential *decrease*. The activity of Cs-137 at time $t$ (years after 2011) is:
$$A(t) = 500 \\times e^{-\\lambda t}, \\quad \\lambda = \\frac{\\ln 2}{30.17}$$

The decay constant $\\lambda$ is always positive; the **negative sign** in the exponent is what makes the function decrease. The larger $\\lambda$ is, the faster the isotope decays.

Run the setup cell to define $\\lambda$ and inspect its value."""),

        md("""\
Setup — run first."""),

        code("""\
# Setup — run first
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'figure.dpi': 120, 'font.size': 11})

A0_cs     = 500        # initial Cs-137 activity (TBq)
T_half_cs = 30.17      # half-life in years
threshold = 10         # reclassification threshold (TBq)

lambda_cs = np.log(2) / T_half_cs
print("lambda_cs =", lambda_cs)    # raw value — per year
print("A0 =", A0_cs, "TBq")
print("Reclassification threshold:", threshold, "TBq")"""),

        md("""\
---
## Part A: Modeling Radioactive Decay (~20 min)

We'll write the Cs-137 decay model in two equivalent forms, verify they agree, then solve for the year when the container activity drops below the regulatory threshold."""),

        md("""\
### A.1 — Two equivalent forms of the decay model

Just as bacteria can be modelled using either the doubling form or the $e^{kt}$ form, radioactive decay can be written as:
- **Half-life form:** $A(t) = A_0 \\times (0.5)^{t/T_{\\text{half}}}$ — each half-life, multiply by 0.5
- **Decay-constant form:** $A(t) = A_0 \\times e^{-\\lambda t}$ — continuous decay at rate $\\lambda$

Run the cell and confirm both forms give the same activity at 0, 1, 2, and 3 half-lives."""),

        md("""\
Two forms of the Cs-137 decay model."""),

        code("""\
# A.1 — Two forms of the Cs-137 decay model
def A_cs_v1(t): return A0_cs * (0.5)**(t / T_half_cs)     # half-life form
def A_cs_v2(t): return A0_cs * np.exp(-lambda_cs * t)      # decay-constant form

print("Verifying both forms agree:")
for label, t in [("t=0", 0), ("1 half-life", T_half_cs),
                 ("2 half-lives", 2*T_half_cs), ("100 years", 100)]:
    print(f"  {label:>15} ({t:>6.1f} y):  form1 = {A_cs_v1(t):.3f} TBq   form2 = {A_cs_v2(t):.3f} TBq")"""),

        md("""\
### A.2 — When does the activity reach the reclassification threshold?

We need to find $t$ such that $A(t) = 10$ TBq. Starting from the decay-constant form:
$$500 \\, e^{-\\lambda t} = 10 \\implies t = \\frac{-\\ln(10/500)}{\\lambda}$$

After finding $t$, we add it to 2011 to get the calendar year of reclassification."""),

        md("""\
Time to reach the 10 TBq threshold."""),

        code("""\
# A.2 — Time to reach the 10 TBq threshold
t_threshold = -np.log(threshold / A0_cs) / lambda_cs
print(f"Time to reach {threshold} TBq: {t_threshold:.1f} years")
print(f"Reclassification year: {2011 + t_threshold:.0f}")

t_vals = np.linspace(0, 250, 500)
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_vals, A_cs_v1(t_vals), "steelblue", lw=2, label="Cs-137 activity")
ax.axhline(threshold, color="red",     ls="--", lw=1.5, label=f"Threshold ({threshold} TBq)")
ax.axvline(t_threshold, color="orange", ls=":",  lw=1.5, label=f"Threshold at {t_threshold:.0f} yrs")
ax.set_yscale("log")
ax.set_xlabel("Years since 2011")
ax.set_ylabel("Activity (TBq, log scale)")
ax.set_title("Cs-137 Decay — Fukushima Waste Container")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Group discussion A:**
1. In what calendar year can the container be reclassified? How many half-lives is that?
2. Why does activity never actually reach zero?

```python
# Answers:
# 1. Number of half-lives to reclassification:
print(f"Number of half-lives: {t_threshold / T_half_cs:.2f}")
# 2. Why never zero:
#    ...
```"""),

        md("""\
---
## Part B: Multiple Isotopes (~15 min)

The waste also contains **Strontium-90**: half-life **28.8 years**, initial activity **200 TBq**. Both isotopes are present simultaneously and decay independently. Because Cs-137 starts with higher activity but the two half-lives are similar, their activity curves will cross at some point."""),

        md("""\
### B.1 — Adding Sr-90 to the model

We define a separate decay function for Sr-90 using its own $\\lambda$, then plot both curves together. Notice that despite Cs-137 starting higher, the curves converge — we'll find exactly when they cross in B.2."""),

        md("""\
Sr-90 decay model."""),

        code("""\
# B.1 — Sr-90 decay model
A0_sr     = 200
T_half_sr = 28.8
lambda_sr = np.log(2) / T_half_sr

def A_sr(t): return A0_sr * np.exp(-lambda_sr * t)

print(f"Cs-137: λ = {lambda_cs:.5f} /yr  (T½ = {T_half_cs} y)")
print(f"Sr-90:  λ = {lambda_sr:.5f} /yr  (T½ = {T_half_sr} y)")
print(f"Sr-90 decays faster than Cs-137? {lambda_sr > lambda_cs}")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t_vals, A_cs_v1(t_vals), "steelblue",  lw=2, label=f"Cs-137 (500 TBq, T½ = {T_half_cs} y)")
ax.plot(t_vals, A_sr(t_vals),    "darkorange", lw=2, label=f"Sr-90  (200 TBq, T½ = {T_half_sr} y)")
ax.axhline(threshold, color="red", ls="--", label="Reclassification threshold")
ax.set_yscale("log")
ax.set_xlabel("Years since 2011")
ax.set_ylabel("Activity (TBq)")
ax.set_title("Fukushima Waste: Cs-137 vs Sr-90 Decay")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
### B.2 — Finding the crossover analytically

When do the two activities equalise? We set $A_{\\text{Cs}}(t) = A_{\\text{Sr}}(t)$ and solve:
$$500 \\, e^{-\\lambda_{\\text{Cs}} t} = 200 \\, e^{-\\lambda_{\\text{Sr}} t}$$

Taking logarithms of both sides and rearranging gives $t = \\ln(500/200) / (\\lambda_{\\text{Cs}} - \\lambda_{\\text{Sr}})$."""),

        md("""\
Crossover time: when do Cs-137 and Sr-90 have equal activity?"""),

        code("""\
# B.2 — Crossover time: when do Cs-137 and Sr-90 have equal activity?
delta_lambda = lambda_cs - lambda_sr
t_equal = np.log(A0_cs / A0_sr) / delta_lambda

print(f"Equal activity at t = {t_equal:.1f} years  (calendar year {2011 + t_equal:.0f})")
print(f"Activity at crossover: Cs = {A_cs_v2(t_equal):.2f} TBq   Sr = {A_sr(t_equal):.2f} TBq")"""),

        md("""\
✏️ **Group discussion B:**
1. Cs-137 starts with more activity but has a *slightly longer* half-life than Sr-90. Why do they eventually equalise?
2. After the crossover, which isotope dominates total activity? Does the plot confirm this?

```python
# Answers:
# 1. Why they equalise:
#    ...
# 2. Which dominates post-crossover:
#    ...
```"""),

        md("""\
---
## Part C: Storage Cost Analysis (~10 min)

High-level nuclear waste is expensive to store. Once the Cs-137 activity drops below 10 TBq, the container can be reclassified, cutting storage costs substantially.

- High-level storage: ¥50 million/year
- Low-level storage: ¥5 million/year
- Planning horizon: 150 years from 2011

We'll calculate total costs with and without reclassification."""),

        code("""\
# C.1 — Storage cost over 150 years
yrs_high = t_threshold           # high-level until threshold
yrs_low  = 150 - t_threshold     # low-level after

cost_high       = yrs_high * 50
cost_low        = yrs_low  * 5
cost_total      = cost_high + cost_low
cost_no_reclas  = 150 * 50       # counterfactual: never reclassified

print(f"High-level period:  {yrs_high:.1f} years")
print(f"Low-level period:   {yrs_low:.1f} years")
print()
print(f"High-level cost:  ¥{cost_high:,.0f}M")
print(f"Low-level cost:   ¥{cost_low:,.0f}M")
print(f"Total:            ¥{cost_total:,.0f}M")
print(f"Saving vs always-high: ¥{cost_no_reclas - cost_total:,.0f}M")"""),

        md("""\
✏️ **Policy summary (write as a group):**

Write 3–4 sentences for policymakers. Include:
- When reclassification occurs and the cost saving it enables
- One key assumption in your model that could change the answer
- A concrete recommendation

```
SUMMARY:
...
```"""),

        md("""\
---
## Part D: Carbon Dating — Connecting Half-Life to Archaeology (~10 min)

The same exponential decay mathematics applies across wildly different timescales. Carbon-14 has a half-life of 5,730 years — compared to Cs-137's 30 years. Yet the equation is identical; only the numbers change. Here we use C-14 to date a fossil and compare the timescales."""),

        code("""\
# D.1 — Carbon dating: fossil has 12.5% of original C-14
T_half_c14  = 5730
lambda_c14  = np.log(2) / T_half_c14

fraction     = 0.125    # 12.5% = (0.5)^3 → exactly 3 half-lives
t_fossil     = -np.log(fraction) / lambda_c14
n_halflives  = np.log(1 / fraction) / np.log(2)

print(f"12.5% = (0.5)^{n_halflives:.0f}  →  {n_halflives:.0f} half-lives")
print(f"Age: {t_fossil:.0f} years  ({n_halflives:.0f} × {T_half_c14} = {int(n_halflives*T_half_c14)} years)")

t_c14 = np.linspace(0, 45000, 400)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_c14 / 1000, 100 * np.exp(-lambda_c14 * t_c14), "purple", lw=2)
ax.axhline(12.5, color="green",  ls="--", label="12.5% remaining")
ax.axvline(t_fossil / 1000, color="orange", ls=":", label=f"{t_fossil:.0f} years")
ax.set_xlabel("Time (thousand years)")
ax.set_ylabel("C-14 remaining (%)")
ax.set_title("Carbon-14 Decay — Archaeological Dating")
ax.legend()
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Connecting the concepts:**

Compare the timescales: Cs-137 (30 y half-life), Sr-90 (29 y), C-14 (5,730 y). All three use the formula $A(t) = A_0 e^{-\\lambda t}$.

What determines whether a decay process is "fast" or "slow" in practical terms? How does $\\lambda$ capture this?

```
Your answer:
...
```"""),

        md("""\
---
## ✅ Presentation Checklist (Week 3, 10 minutes)

1. **The Problem** (~2 min): What question were you answering?
2. **The Model** (~3 min): Why exponential decay? Show the equation and what $\\lambda$ means.
3. **Key Results** (~3 min): Reclassification year, cost savings, crossover point — show the two-isotope plot.
4. **Implications** (~2 min): What should Japanese policymakers take away?

> **Tips:** Contrast Cs-137 and C-14 timescales — it makes the math feel real. "30 years vs 5,730 years — same equation, wildly different consequences." """),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# Shared setup cell for standalone A/B notebooks
# ─────────────────────────────────────────────────────────────────────────────

LAB_SETUP = """\
# Run first — loads libraries for this session
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'figure.dpi': 120, 'font.size': 11})"""


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 3 — Logistic Functions and Bounded Growth
# ─────────────────────────────────────────────────────────────────────────────

def week3_student():
    return notebook([

        md("""\
# Week 3 Lab: The Fishery Manager's Dilemma
**SCIE1500 — Analytical Methods for Scientists | Semester 2, 2026**

> **Lab format:** Work in your group. Discuss answers before typing code.
> **Today's session:** ~2 hours | Ask your tutor when stuck."""),

        md("""\
---
## 🌍 Scientific Scenario

You are a scientific advisor to the **Western Australian Fisheries Authority**. The authority manages a sardine fishery showing signs of overfishing.

Marine biologists use the **Schaefer model** for sardine population growth:

$$G(S) = g \\cdot S \\cdot \\left(1 - \\frac{S}{K}\\right)$$

| Parameter | Value | Meaning |
|-----------|-------|---------|
| $g$ | 0.4 /yr | Intrinsic growth rate |
| $K$ | 1500 t | Carrying capacity |
| $S$ | 1200 t | Current stock |
| $H$ | 120 t/yr | Current harvest |

> *Is this harvest sustainable?*"""),

        md("""\
---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Use a Schaefer model to compute growth rates and Maximum Sustainable Yield | ~20 min |
| B | Analyse sustainability by finding equilibria for current and proposed harvest levels | ~25 min |
| C | Write a policy recommendation based on your analysis | ~10 min |

**By the end of today you will be able to:**
- Explain bounded growth and Maximum Sustainable Yield (MSY)
- Find equilibrium stock levels by solving a quadratic equation
- Interpret the stability of two equilibria in a fishery context"""),

        code(SETUP_IMPORTS),

        md("""\
---
## Part A: The Schaefer Model (~20 min)

Expanding the Schaefer model:
$$G(S) = 0.4S\\left(1 - \\frac{S}{1500}\\right) = 0.4S - \\frac{0.4}{1500}S^2$$

This is a **downward-opening parabola** — growth is zero at $S = 0$ and $S = K$, and peaks at $S^* = K/2$."""),

        code("""\
# A.1 — Define the Schaefer growth function and evaluate at three stock levels
g = 0.4      # intrinsic growth rate
K = 1500     # carrying capacity (tonnes)

def G(S):
    'Annual population growth (tonnes/year).'
    return g * S * (1 - S / K)

for S_level in [400, 750, 1200]:
    print(f"G({S_level:4d}) = {G(S_level):.1f} tonnes/year")

S_msy = K / 2
G_msy = G(S_msy)
print(f"\\nMSY at S = K/2 = {S_msy:.0f} t  →  G_max = {G_msy:.1f} t/yr")"""),

        md("""\
Plot the Schaefer growth curve."""),

        code("""\
# A.2 — Plot the Schaefer growth curve
S_vals = np.linspace(0, K, 400)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(S_vals, G(S_vals), "steelblue", lw=2, label="Growth G(S)")
ax.plot(S_msy, G_msy, "go", ms=10, label=f"MSY: S={S_msy:.0f} t, G={G_msy:.0f} t/yr")
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("Stock Level S (tonnes)")
ax.set_ylabel("Growth Rate G(S) (tonnes/year)")
ax.set_title("Sardine Fishery: Schaefer Growth Model")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity A — discuss as a group:**
1. Why does growth peak at $S = K/2$ rather than near the maximum stock level?
2. What does $G(K) = 0$ represent ecologically?
3. At $S = 1200$ t (above $K/2$), is growth increasing or decreasing as stock rises?

```
Answers:
1. ...
2. ...
3. ...
```"""),

        md("""\
---
## Part B: Sustainability Analysis (~25 min)

A harvest $H$ is **sustainable** when growth replaces what is removed: $G(S) \\geq H$.

Setting $G(S) = H$ gives the **equilibrium stock levels** — states where stock stays constant.

Rearranging: $\\frac{g}{K}S^2 - gS + H = 0$ → solve with the quadratic formula."""),

        code("""\
# B.1 — Sustainability check at current stock
S_current = 1200
H = 120    # current harvest (tonnes/year)

G_current = G(S_current)
print(f"G(1200) = {G_current:.1f} t/yr")
print(f"H       = {H} t/yr")
print(f"Sustainable? {G_current >= H}  (need G >= H)")"""),

        md("""\
Equilibrium stock levels for H = 120: quadratic formula."""),

        code("""\
# B.2 — Equilibrium stock levels for H = 120: quadratic formula
a_coef =  g / K
b_coef = -g
c_coef =  H

disc = b_coef**2 - 4 * a_coef * c_coef
S1 = (-b_coef - np.sqrt(disc)) / (2 * a_coef)   # lower (unstable)
S2 = (-b_coef + np.sqrt(disc)) / (2 * a_coef)   # upper (stable)

print(f"Equilibria for H = {H} t/yr:")
print(f"  S₁ = {S1:.1f} t  (lower — unstable collapse threshold)")
print(f"  S₂ = {S2:.1f} t  (upper — stable management target)")
print(f"  Current stock {S_current} t is {'above' if S_current > S1 else 'below'} collapse threshold.")"""),

        md("""\
What if harvest increases to 140 t/yr?"""),

        code("""\
# B.3 — What if harvest increases to 140 t/yr?
H_proposed = 140

c_new = H_proposed
disc_new = b_coef**2 - 4 * a_coef * c_new
if disc_new < 0:
    print(f"H = {H_proposed} t/yr exceeds MSY — no sustainable equilibrium!")
else:
    S1_new = (-b_coef - np.sqrt(disc_new)) / (2 * a_coef)
    S2_new = (-b_coef + np.sqrt(disc_new)) / (2 * a_coef)
    print(f"Equilibria for H = {H_proposed} t/yr:")
    print(f"  S₁ = {S1_new:.1f} t  (collapse threshold rises by {S1_new - S1:.1f} t → riskier)")
    print(f"  S₂ = {S2_new:.1f} t  (stable target falls by {S2 - S2_new:.1f} t → lower stock)")
        """),

        md("""\
The chart below shows both scenarios."""),

        code("""\
# Plot both scenarios
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(S_vals, G(S_vals), "steelblue", lw=2, label="Growth G(S)")
ax.axhline(H,          color="red",    ls="--", lw=1.5, label=f"Current H = {H} t/yr")
ax.axhline(H_proposed, color="orange", ls="--", lw=1.5, label=f"Proposed H = {H_proposed} t/yr")
ax.axvline(S_current,  color="gray",   ls=":",  alpha=0.6, label=f"Current stock {S_current} t")
ax.plot(S_msy, G_msy, "go", ms=8, label=f"MSY = {G_msy:.0f} t/yr")
ax.set_xlabel("Stock Level S (tonnes)")
ax.set_ylabel("Growth / Harvest (tonnes/year)")
ax.set_title("Sardine Fishery: Sustainability Analysis")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity B:**
1. The current stock (1200 t) is *above* $S_2$ for $H = 120$. What happens to the stock over time?
2. Increasing harvest to 140 t/yr raises the collapse threshold. By how many tonnes?
3. The MSY is 150 t/yr. Why must harvest never exceed MSY?

```python
print("MSY =", G(K/2))
# Answers:
# 1. ...
# 2. ...
# 3. ...
```"""),

        md("""\
---
## Part C: Policy Recommendation (~10 min)

Write a **4–5 sentence recommendation** to the Fisheries Authority:
- Is the current 120 t/yr harvest sustainable?
- Should the proposed 140 t/yr increase be approved?
- What harvest level do you recommend for long-term stability?

```
RECOMMENDATION TO WA FISHERIES AUTHORITY:

...
```"""),

        md("""\
---
## ✅ Lab Wrap-Up

- [ ] Computed $G(S)$ at three stock levels and identified the MSY (Part A)
- [ ] Found equilibrium stock levels for both harvest scenarios (Part B)
- [ ] Written a policy recommendation with specific numbers (Part C)
- [ ] **Groups 3 & 4:** Opened your Presentation Brief (Lab A or Lab B) and started Part A

> 💡 **Key insight:** There are always *two* equilibria — one stable (recovery target), one unstable (collapse threshold). Higher harvest brings these closer together."""),

        md("""\
---
---
## ✅ Submission Exercise — Batch 1

**Due: Monday 11 August, 11:59 pm — submit on LMS**
**Covers: Weeks 1–3 (functions, exponential models, logistic growth)**

Submit individually. Show full mathematical working for all calculations.

---
### Q1 — Functions and Rates of Change (Week 1)

Southern bluefin tuna population data:

| Year | $t$ (yrs since 2000) | $P(t)$ (thousand fish) |
|------|---------------------|------------------------|
| 2000 | 0  | 90 |
| 2005 | 5  | 82 |
| 2010 | 10 | 71 |
| 2015 | 15 | 65 |
| 2020 | 20 | 61 |

**a)** Calculate the average rate of change of $P$ over each of the four 5-year intervals. Show working.

**b)** Is the decline rate constant? Describe the pattern and what it implies about the shape of $P(t)$.

**c)** [Python] Plot $P(t)$ from $t = 0$ to $t = 20$. Does a linear model fit this data well? Explain.

---
### Q2 — Exponential Decay (Week 2)

A marine toxin degrades as $C(t) = 250\\,e^{-0.08t}$ μg/L ($t$ in days).

**a)** Find the half-life algebraically. Show working using logarithms.

**b)** Safe-swimming threshold is 5 μg/L. Find the crossing day algebraically, then verify in Python.

**c)** [Python] Plot $C(t)$ from $t = 0$ to $t = 60$. Mark the threshold as a horizontal dashed line and the crossing day as a vertical marker.

---
### Q3 — Logistic Fishery (Week 3)

A Carpentaria prawn fishery: $G(S) = 0.5S(1 - S/2000)$.

**a)** Find the MSY and the stock level at which it occurs. Show the algebraic derivation.

**b)** Current stock is 1400 t, harvest is 200 t/yr. Is this sustainable? Justify by computing $G(1400)$.

**c)** Find both equilibrium stock levels for $H = 200$ t/yr using the quadratic formula. Identify which is stable and which is unstable.

**d)** [Written, no Python] The manager reduces harvest to 150 t/yr while stock is 1400 t. What happens to the stock over time? Justify from the model."""),
    ])


def week3_lab_a():
    return notebook([

        md("""\
# Week 3 Presentation Brief — Variation A
## 🦪 Abalone Fishery: Sustainable Harvest in Western Australia
**SCIE1500 — Semester 2, 2026 | Group 3 — presenting in Week 4**

> Work through all parts during the Week 3 lab. Your **10-minute Week 4 presentation** should cover: the problem, your model, key results, and policy recommendation.
> Do not show raw code — show graphs and equations."""),

        md("""\
---
## 📋 Scenario

The WA Department of Fisheries manages a commercial abalone (*Haliotis roei*) fishery. Population surveys have produced the Schaefer model:

$$G(S) = 0.35 \\cdot S \\cdot \\left(1 - \\frac{S}{1200}\\right)$$

- $g = 0.35$, $K = 1200$ tonnes
- **Current stock:** 950 tonnes
- **Proposed harvest:** 100 tonnes/year (industry also wants to try 120 t/yr)

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Apply the Schaefer model to compute growth rates and MSY | ~15 min |
| B | Find and compare equilibria for H = 100 and H = 120 | ~20 min |
| C | Write a policy recommendation with supporting evidence | ~15 min |
| D | Build a Python visualisation of the harvest equilibria | ~10 min |"""),

        code(LAB_SETUP + """

# Abalone Schaefer parameters
g = 0.35
K = 1200

def G(S):
    'Annual growth rate (tonnes/year).'
    return g * S * (1 - S / K)

S_msy = K / 2
G_msy = G(S_msy)
print(f"MSY stock level  S* = {S_msy:.0f} tonnes")
print(f"Max Sustainable Yield = {G_msy:.2f} tonnes/year")
print(f"Verify MSY = g*K/4 = {g * K / 4:.2f}")"""),

        md("""\
---
## Part A: Schaefer Model (~15 min)"""),

        code("""\
# A.1 — Evaluate G(S) at three stock levels and current stock
for S_level in [300, 600, 900]:
    print(f"G({S_level:4d}) = {G(S_level):.2f} tonnes/year")
print(f"G( 950) = {G(950):.2f} tonnes/year  (current stock)")"""),

        md("""\
✏️ **Activity A:** At which stock level does growth peak? Is $S = 950$ on the ascending or descending side of the parabola? What does that mean for natural recovery rate?

```
Answer: ...
```"""),

        md("""\
---
## Part B: Sustainability Analysis (~20 min)"""),

        code("""\
# B.1 — Sustainability check: is G(950) >= H?
S_current = 950
H = 100

print(f"G(950) = {G(S_current):.2f} t/yr")
print(f"H      = {H} t/yr")
print(f"Sustainable? {G(S_current) >= H}")"""),

        md("""\
Equilibria for H = 100 and H = 120 using quadratic formula."""),

        code("""\
# B.2 — Equilibria for H = 100 and H = 120 using quadratic formula
def equilibria(H_val):
    'Lower and upper equilibria for harvest H_val. Returns (S1, S2) or (None, None).'
    a, b, c = g / K, -g, H_val
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None, None
    return (-b - np.sqrt(disc)) / (2*a), (-b + np.sqrt(disc)) / (2*a)

for H_val, label in [(100, "Proposed H = 100"), (120, "Alternative H = 120")]:
    S1, S2 = equilibria(H_val)
    if S1 is None:
        print(f"{label}: EXCEEDS MSY — no sustainable equilibrium!")
    else:
        print(f"{label} t/yr:  S₁ = {S1:.1f} t (unstable)   S₂ = {S2:.1f} t (stable)")"""),

        md("""\
✏️ **Activity B:**
1. For $H = 100$ t/yr, the current stock (950 t) is above $S_2$. What happens to stock over time?
2. How much does the collapse threshold ($S_1$) rise when harvest increases from 100 to 120 t/yr?

```
Answers:
1. ...
2. ...
```"""),

        md("""\
---
## Part C: Policy Recommendation (~15 min)

Write 4–5 sentences to the Fisheries Minister:
- Is $H = 120$ t/yr sustainable?
- What risk does it create relative to $H = 100$ t/yr?
- What harvest level do you recommend?

```
RECOMMENDATION:
...
```"""),

        md("""\
---
## Part D: Python Visualisation (~10 min)"""),

        code("""\
# D.1 — Schaefer growth curve with harvest lines and equilibria
S_vals = np.linspace(0, K, 400)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(S_vals, G(S_vals), "steelblue", lw=2, label="Growth G(S)")
for H_val, clr, lbl in [(100, "orange", "H = 100 t/yr"), (120, "red", "H = 120 t/yr")]:
    ax.axhline(H_val, color=clr, ls="--", lw=1.5, label=lbl)
    S1, S2 = equilibria(H_val)
    if S1 is not None:
        ax.plot([S1, S2], [H_val, H_val], "o", color=clr, ms=8, zorder=5)
ax.plot(S_msy, G_msy, "gs", ms=10, label=f"MSY = {G_msy:.1f} t/yr at S = {S_msy} t")
ax.axvline(S_current, color="gray", ls=":", alpha=0.7, label=f"Current stock ({S_current} t)")
ax.set_xlabel("Stock Level S (tonnes)")
ax.set_ylabel("Growth / Harvest (tonnes/year)")
ax.set_title("Abalone Fishery: Schaefer Model")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## ✅ Presentation Checklist (Week 4, 10 minutes)

1. **Problem** (~2 min): State the management question and why MSY matters.
2. **Model** (~3 min): Present the Schaefer equation and explain what MSY means.
3. **Results** (~3 min): Show equilibria for both harvest levels and walk through your graph.
4. **Recommendation** (~2 min): State your harvest advice and back it with numbers."""),
    ])


def week3_lab_b():
    return notebook([

        md("""\
# Week 3 Presentation Brief — Variation B
## 🦞 Rock Lobster Recovery: From Overfishing to Sustainability
**SCIE1500 — Semester 2, 2026 | Group 4 — presenting in Week 4**

> Work through all parts during the Week 3 lab. Your **10-minute Week 4 presentation** should cover: the problem, your model, key results, and climate risk."""),

        md("""\
---
## 📋 Scenario

WA's rock lobster (*Panulirus cygnus*) fishery was severely overfished in the 1990s. After recovery efforts, the Schaefer model is:

$$G(S) = 0.42 \\cdot S \\cdot \\left(1 - \\frac{S}{800}\\right)$$

- $g = 0.42$, $K = 800$ tonnes
- **Current stock (recovering):** 350 tonnes
- **Proposed harvest:** 70 tonnes/year
- **Climate projection:** Warming reduces $K$ to 720 tonnes by 2040

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Apply the Schaefer model to find MSY and growth rates | ~15 min |
| B | Assess sustainability at a harvest rate of H = 70 | ~20 min |
| C | Evaluate the impact of climate change on sustainability | ~15 min |
| D | Compare your results with the abalone scenario (Brief W3A) | ~10 min |"""),

        code(LAB_SETUP + """

# Rock lobster Schaefer parameters
g = 0.42
K = 800

def G(S):
    'Annual growth rate (tonnes/year).'
    return g * S * (1 - S / K)

def G_warm(S):
    'Growth under warming scenario (K = 720).'
    return g * S * (1 - S / 720)

S_msy = K / 2
G_msy = G(S_msy)
print(f"MSY stock level  = {S_msy:.0f} tonnes")
print(f"Max Sustainable Yield = {G_msy:.2f} tonnes/year")"""),

        md("""\
---
## Part A: Schaefer Model (~15 min)"""),

        code("""\
# A.1 — Growth at three stock levels and current stock
for S_level in [200, 400, 700]:
    print(f"G({S_level:3d}) = {G(S_level):.2f} tonnes/year")
print(f"G(350) at current stock = {G(350):.2f} tonnes/year")

# MSY from formula
print(f"\\nMSY = g*K/4 = {g * K / 4:.2f} t/yr  at  S* = K/2 = {K/2:.0f} t")"""),

        md("""\
---
## Part B: Sustainability Analysis (~20 min)"""),

        code("""\
# B.1 — Is H = 70 t/yr sustainable at S = 350?
S_current = 350
H = 70

print(f"G(350) = {G(350):.2f} t/yr")
print(f"H      = {H} t/yr")
print(f"Sustainable? {G(350) >= H}")
print(f"Harvest fraction: {H / G(350) * 100:.1f}% of current growth")"""),

        md("""\
Equilibria for H = 70 using quadratic formula."""),

        code("""\
# B.2 — Equilibria for H = 70 using quadratic formula
def equilibria(H_val, K_val=K):
    'Lower and upper equilibria for given H and K.'
    a, b, c = g / K_val, -g, H_val
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None, None
    return (-b - np.sqrt(disc)) / (2*a), (-b + np.sqrt(disc)) / (2*a)

S1, S2 = equilibria(70)
print(f"Equilibria for H = 70 t/yr (K = {K}):")
print(f"  S₁ = {S1:.1f} t  (unstable — collapse threshold)")
print(f"  S₂ = {S2:.1f} t  (stable   — recovery target)")
print(f"  Current stock 350 t is {'above' if 350 > S1 else 'below'} collapse threshold.")"""),

        md("""\
✏️ **Activity B:**
1. The current stock (350 t) is below the stable equilibrium $S_2$. Will stock grow or shrink over time under H = 70?
2. Why are there two equilibria rather than one?

```
Answers:
1. ...
2. ...
```"""),

        md("""\
---
## Part C: Climate Change Impact (~15 min)"""),

        code("""\
# C.1 — Warming scenario: K drops from 800 to 720
K_warm = 720
MSY_warm = g * K_warm / 4
print(f"Warming scenario (K = {K_warm}):")
print(f"  New MSY = {MSY_warm:.2f} t/yr  at  S* = {K_warm/2:.0f} t")

S1_w, S2_w = equilibria(70, K_val=K_warm)
if S1_w is None:
    print(f"  H = 70 t/yr EXCEEDS the warming-scenario MSY — unsustainable!")
else:
    print(f"  Lower equilibrium S₁ = {S1_w:.1f} t")
    print(f"  Upper equilibrium S₂ = {S2_w:.1f} t")
        """),

        md("""\
The chart below compares current and warming scenarios."""),

        code("""\
# Plot current vs warming
S_vals = np.linspace(0, 800, 400)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(S_vals, G(S_vals),      "steelblue", lw=2, label=f"Current (K = {K})")
ax.plot(S_vals, G_warm(S_vals), "firebrick", lw=2, ls="--", label=f"Warming (K = {K_warm})")
ax.axhline(70, color="green", ls=":", lw=1.5, label="Proposed H = 70 t/yr")
ax.axvline(S_current, color="gray", ls=":", alpha=0.6, label=f"Current stock ({S_current} t)")
ax.set_xlabel("Stock Level S (tonnes)")
ax.set_ylabel("Growth Rate (tonnes/year)")
ax.set_title("Rock Lobster: Climate Change Impact")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity C — Climate adaptation strategy (3–4 sentences):**
- Short-term harvest while stock rebuilds
- Long-term harvest adjustment for warming
- What monitoring would you require?

```
STRATEGY:
...
```"""),

        md("""\
---
## Part D: Comparative Analysis (~10 min)

Compare rock lobster to abalone (Brief W3A: $g = 0.35$, $K = 1200$, $H = 100$ t/yr):

| Metric | Rock lobster | Abalone |
|--------|-------------|---------|
| Intrinsic growth rate $g$ | 0.42 | 0.35 |
| Carrying capacity $K$ | 800 t | 1200 t |
| MSY | ? | ? |
| Proposed harvest as % of MSY | ? | ? |

✏️ Fill in the table, then discuss: what biological factors explain the different $K$ values?

```python
# Fill in:
print("Rock lobster MSY:", g * K / 4, "t/yr")
print("Abalone MSY:", 0.35 * 1200 / 4, "t/yr")
print("Rock lobster H/MSY:", 70 / (g * K / 4) * 100, "%")
print("Abalone H/MSY:", 100 / (0.35 * 1200 / 4) * 100, "%")
```"""),

        md("""\
---
## ✅ Presentation Checklist (Week 4, 10 minutes)

1. **Problem** (~2 min): State the recovery question and what a sustainable harvest means.
2. **Model** (~3 min): Present the Schaefer equation, explain MSY, and show equilibria for H = 70.
3. **Climate risk** (~3 min): Show how warming affects sustainability and walk through your comparison plot.
4. **Recommendation** (~2 min): Recommend a harvest level and outline a monitoring plan."""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 4 — Derivatives and Rates of Change
# ─────────────────────────────────────────────────────────────────────────────

def week4_student():
    return notebook([

        md("""\
# Week 4 Lab: Optimizing Chemical Reactions
**SCIE1500 — Analytical Methods for Scientists | Semester 2, 2026**

> **Lab format:** Work in your group. Discuss answers before typing code.
> **Today's session:** ~2 hours | Ask your tutor when stuck."""),

        md("""\
---
## 🌍 Scientific Scenario

A pharmaceutical company is optimizing production of a critical antibiotic. Drug yield depends on reaction temperature:

$$Y(T) = -0.05T^2 + 8T - 200$$

where $Y$ is yield (g/batch) and $T$ is temperature (°C), valid for $50 \\leq T \\leq 110$ °C.

> *What temperature maximizes yield within the safe operating range?*"""),

        md("""\
---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Interpret the derivative $Y'(T)$ as a rate of change | ~20 min |
| B | Find the optimal temperature using calculus | ~25 min |
| C | Apply practical constraints and conduct a cost-benefit analysis | ~15 min |

**By the end of today you will be able to:**
- Apply the power rule to find a derivative
- Interpret the derivative as a rate of change with units
- Use the first and second derivative tests to classify critical points"""),

        code(SETUP_IMPORTS),

        md("""\
---
## Part A: Derivatives as Rates of Change (~20 min)

The derivative $Y'(T) = \\frac{dY}{dT}$ tells us how yield changes per degree of temperature change.

Applying the power rule to $Y(T) = -0.05T^2 + 8T - 200$:
$$Y'(T) = -0.1T + 8$$

This is the **marginal yield** — the extra grams per batch gained by raising temperature 1°C."""),

        code("""\
# A.1 — Define yield function and derivative
def Y(T):
    'Drug yield (grams/batch).'
    return -0.05 * T**2 + 8 * T - 200

def dY(T):
    'Marginal yield (grams per batch per °C).'
    return -0.1 * T + 8

# Evaluate at three temperatures
print(f"{'T (°C)':>8} | {'Y(T) (g)':>10} | {'Y\\'(T) (g/°C)':>14} | Yield trend")
print("-" * 55)
for T in [60, 80, 100]:
    trend = "increasing" if dY(T) > 0 else "decreasing"
    print(f"{T:>8} | {Y(T):>10.1f} | {dY(T):>14.2f} | {trend}")"""),

        md("""\
✏️ **Activity A.1:**
1. At $T = 70$ °C, $Y'(70) = ?$ g/°C. Interpret: what does a positive value mean here?
2. At $T = 90$ °C, $Y'(90) = ?$ g/°C. Interpret: should the company *increase* or *decrease* temperature to gain yield?
3. What does it mean when $Y'(T) = 0$?

```python
print("Y'(70) =", dY(70), "g/°C")
print("Y'(90) =", dY(90), "g/°C")
# Answers:
# 1. ...
# 2. ...
# 3. ...
```"""),

        md("""\
Plot yield and marginal yield side by side."""),

        code("""\
# A.2 — Plot yield and marginal yield side by side
T_vals = np.linspace(50, 110, 300)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8))

ax1.plot(T_vals, Y(T_vals), "steelblue", lw=2)
ax1.set_ylabel("Yield Y(T) (g/batch)")
ax1.set_title("Drug Yield vs Reaction Temperature")
ax1.grid(alpha=0.3)

ax2.plot(T_vals, dY(T_vals), "darkorange", lw=2)
ax2.axhline(0, color="k", lw=0.8)
ax2.set_xlabel("Temperature T (°C)")
ax2.set_ylabel("Marginal yield Y'(T) (g/°C)")
ax2.set_title("Rate of Change of Yield")
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part B: Finding the Optimal Temperature (~25 min)

A **critical point** occurs where $Y'(T) = 0$ — a candidate for maximum or minimum yield.

Solving $-0.1T + 8 = 0$ gives $T_{\\text{opt}} = 80$ °C.

The **second derivative** $Y''(T)$ confirms the type:
- $Y'' < 0$: concave down → **maximum** ✓
- $Y'' > 0$: concave up → minimum"""),

        code("""\
# B.1 — Critical point and second derivative test
def d2Y(T):
    'Second derivative (curvature).'
    return -0.1      # constant — negative everywhere → always concave down

T_opt = 8 / 0.1    # solve -0.1T + 8 = 0  →  T = 80
Y_opt = Y(T_opt)
Y2    = d2Y(T_opt)

print(f"Critical point: T_opt = {T_opt:.1f} °C")
print(f"Y(80) = {Y_opt:.1f} g/batch  (maximum yield)")
print(f"Y''(80) = {Y2:.1f}  (< 0 → confirmed maximum)")
print(f"\\nFeasible? 50 ≤ {T_opt:.0f} ≤ 110 → {50 <= T_opt <= 110}")"""),

        md("""\
Plot yield curve with optimal point and safe range."""),

        code("""\
# B.2 — Plot yield curve with optimal point and safe range
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(T_vals, Y(T_vals), "steelblue", lw=2, label="Yield Y(T)")
ax.plot(T_opt, Y_opt, "ro", ms=12, label=f"Optimum: T={T_opt:.0f}°C, Y={Y_opt:.1f} g")
ax.axvline(50,    color="gray", ls="--", alpha=0.5, label="Safe range [50, 110]°C")
ax.axvline(110,   color="gray", ls="--", alpha=0.5)
ax.set_xlabel("Temperature T (°C)")
ax.set_ylabel("Yield (g/batch)")
ax.set_title("Drug Yield: Optimal Temperature")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part C: Practical Constraints (~15 min)

Real reactors maintain temperature within ±3°C of the setpoint. At $T_{\\text{opt}} = 80$ °C, the vessel operates between 77°C and 83°C."""),

        code("""\
# C.1 — Yield range due to temperature uncertainty
T_low  = T_opt - 3
T_high = T_opt + 3

print(f"Temperature range: [{T_low:.0f}, {T_high:.0f}] °C")
print(f"Yield range:       [{Y(T_low):.1f}, {Y(T_high):.1f}] g/batch")
print(f"Variation: ±{(Y(T_high) - Y(T_low))/2:.1f} g")

# Compare to T = 70°C (competitor's process)
Y_comp = Y(70)
print(f"\\nCompetitor at T = 70°C: Y = {Y_comp:.1f} g/batch")
print(f"Yield gain at optimum: {Y_opt - Y_comp:.1f} g ({(Y_opt - Y_comp)/Y_comp*100:.1f}% increase)")"""),

        md("""\
Cost-benefit analysis."""),

        code("""\
# C.2 — Cost-benefit analysis
energy_cost_per_deg = 0.50    # $/°C above 50°C per batch
price_per_gram      = 5.00    # $/gram of drug

for T_s in [70, T_opt]:
    energy = (T_s - 50) * energy_cost_per_deg
    revenue = Y(T_s) * price_per_gram
    profit = revenue - energy
    print(f"T = {T_s:.0f}°C: yield = {Y(T_s):.1f}g, energy = ${energy:.2f}, "
          f"revenue = ${revenue:.2f}, profit = ${profit:.2f}")"""),

        md("""\
✏️ **Activity C:**
1. How much additional profit per batch does the optimal temperature generate versus 70°C?
2. If the reactor drifts to 77°C instead of 80°C, how much yield is lost?
3. Write a 2-sentence recommendation to the production manager.

```
Answers:
1. ...
2. ...
Recommendation: ...
```"""),

        md("""\
---
## ✅ Lab Wrap-Up

- [ ] Computed and interpreted $Y'(T)$ at multiple temperatures (Part A)
- [ ] Found the critical point and confirmed it as a maximum (Part B)
- [ ] Analysed yield sensitivity to temperature variation (Part C)
- [ ] **Groups 5 & 6:** Opened your Presentation Brief (Lab A or Lab B) and started Part A

> 💡 **Key pattern:** derivative → set to zero → critical point → second derivative test → check feasibility."""),
    ])


def week4_lab_a():
    return notebook([

        md("""\
# Week 4 Presentation Brief — Variation A
## 🌾 Pesticide Degradation: Optimizing Spray Timing
**SCIE1500 — Semester 2, 2026 | Group 5 — presenting in Week 5**

> Work through all parts during the Week 4 lab. Your **10-minute Week 5 presentation** should cover: the problem, your model, key results, and agronomic implications."""),

        md("""\
---
## 📋 Scenario

A wheat farm in the Wheatbelt uses a pesticide that degrades over time:

$$C(t) = 120\\,e^{-0.15t}$$

where $C$ is concentration (mg/L) and $t$ is days after application.

**Agronomic constraints:**
- Minimum effective: 30 mg/L (below this, pest control fails)
- Maximum safe: 150 mg/L (above, phytotoxicity)
- Aphids most vulnerable: days 5–10 after wheat head emergence

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Compute and interpret the instantaneous rate of change $C'(t)$ | ~20 min |
| B | Determine the effective protection window | ~20 min |
| C | Design an optimal re-application strategy | ~15 min |
| D | Verify the half-life algebraically and in Python | ~10 min |"""),

        code(LAB_SETUP + """

# Pesticide parameters
C0 = 120    # initial concentration (mg/L)
k  = 0.15   # degradation rate constant (per day)

def C(t):
    'Pesticide concentration (mg/L), t days after application.'
    return C0 * np.exp(-k * t)

def dC(t):
    'Rate of change of concentration (mg/L/day).'
    return -k * C0 * np.exp(-k * t)

print("Initial concentration C(0) =", C(0), "mg/L")
print("At t=5:", f"{C(5):.2f}", "mg/L")
print("At t=10:", f"{C(10):.2f}", "mg/L")"""),

        md("""\
---
## Part A: Instantaneous Rate of Change (~20 min)

The rule $(e^{kt})' = k e^{kt}$ gives:
$$C'(t) = -k \\cdot 120\\,e^{-0.15t} = -0.15 \\cdot C(t)$$

The rate of decrease is **proportional to the current concentration** — fast when concentrated, slower as it degrades."""),

        code("""\
# A.1 — Concentration and rate at key days
print(f"{'Day':>5} | {'C(t) mg/L':>10} | {'C\\'(t) mg/L/day':>16} | {'% per day':>9}")
print("-" * 50)
for t in [0, 5, 10, 15, 20]:
    pct = abs(dC(t) / C(t) * 100)
    print(f"{t:>5} | {C(t):>10.2f} | {dC(t):>16.2f} | {pct:>9.1f}%")"""),

        md("""\
✏️ **Activity A:**
1. Evaluate $C'(5)$ and interpret in words including units.
2. Why is the percentage rate of decrease constant at 15%/day?
3. On day 10, is concentration decreasing faster or slower than on day 1?

```
Answers:
1. ...
2. ...
3. ...
```"""),

        md("""\
---
## Part B: Effective Protection Window (~20 min)"""),

        code("""\
# B.1 — When does concentration drop below effective threshold?
C_min = 30    # minimum effective (mg/L)

# Solve: 120 * exp(-0.15 * t) = 30  →  t = -ln(30/120) / 0.15
t_end = -np.log(C_min / C0) / k
print(f"Protection ends at t = {t_end:.2f} days  ({t_end * 24:.0f} hours)")
print(f"Protection window: {t_end:.1f} days from application")

# If protection needed for 20 days, what initial concentration is required?
t_need = 20
C0_need = C_min * np.exp(k * t_need)
print(f"\\nFor 20-day coverage, initial concentration needed: {C0_need:.1f} mg/L")
print(f"Safe? (< 150 mg/L limit): {C0_need < 150}")"""),

        md("""\
Plot concentration with protection window."""),

        code("""\
# B.2 — Plot concentration with protection window
t_vals = np.linspace(0, 30, 300)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9))

ax1.plot(t_vals, C(t_vals), "steelblue", lw=2, label="Concentration C(t)")
ax1.axhline(C_min, color="red", ls="--", lw=1.5, label=f"Min effective ({C_min} mg/L)")
ax1.axhline(150,   color="orange", ls="--", lw=1.5, label="Max safe (150 mg/L)")
ax1.fill_between(t_vals, C_min, np.minimum(C(t_vals), 150),
                 where=(C(t_vals) >= C_min), alpha=0.2, color="green", label="Effective zone")
ax1.axvline(t_end, color="red", ls=":", label=f"Protection ends at {t_end:.1f} days")
ax1.set_ylabel("Concentration (mg/L)")
ax1.set_title("Pesticide Degradation")
ax1.legend(fontsize=9)
ax1.grid(alpha=0.3)

ax2.plot(t_vals, dC(t_vals), "purple", lw=2, label="C'(t) = dC/dt")
ax2.axhline(0, color="k", lw=0.8)
ax2.set_xlabel("Days after application")
ax2.set_ylabel("Rate of change (mg/L/day)")
ax2.set_title("Rate of Pesticide Degradation")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part C: Re-Application Strategy (~15 min)"""),

        code("""\
# C.1 — Re-apply when concentration drops to 40 mg/L
C_reapply = 40

t_reapply = -np.log(C_reapply / C0) / k
print(f"Re-apply when C = {C_reapply} mg/L:  at t = {t_reapply:.1f} days")

# For 30-day coverage
n_applications = np.ceil(30 / t_reapply)
print(f"Days between applications: {t_reapply:.1f} days")
print(f"Total applications for 30-day coverage: {n_applications:.0f}")

# Total pesticide used
dose_per_ha = C0 * 500 / 1e6   # 120 mg/L × 500 L/ha → kg/ha
total_use = n_applications * dose_per_ha
print(f"\\nDose per application: {dose_per_ha:.4f} kg/ha")
print(f"Total pesticide over 30 days: {total_use:.4f} kg/ha")"""),

        md("""\
---
## Part D: Half-Life Verification (~10 min)"""),

        code("""\
# D.1 — Half-life: time for concentration to halve
t_half = np.log(2) / k
t_half_direct = -np.log(0.5) / k    # same formula

print(f"Half-life = ln(2)/k = ln(2)/{k} = {t_half:.2f} days")
print(f"Verification: C(0)/2 = {C0/2:.1f} mg/L")
print(f"C(t_half) = {C(t_half):.2f} mg/L  ✓" if abs(C(t_half) - C0/2) < 0.01 else "Check calculation")

# After two half-lives
print(f"\\nAfter 2 half-lives ({2*t_half:.1f} days): {C(2*t_half):.2f} mg/L = {C(2*t_half)/C0*100:.1f}% of original")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 5, 10 minutes)

1. **Problem** (~2 min): What is the spray timing challenge?
2. **Model** (~3 min): Show $C(t)$ equation; explain what $k = 0.15$ means.
3. **Results** (~3 min): Protection window, re-application schedule — show the two-panel plot.
4. **Implications** (~2 min): What does this mean for aphid control in the critical growth window?"""),
    ])


def week4_lab_b():
    return notebook([

        md("""\
# Week 4 Presentation Brief — Variation B
## 💊 Drug Pharmacokinetics: Dosing for Diabetes Management
**SCIE1500 — Semester 2, 2026 | Group 6 — presenting in Week 5**

> Work through all parts during the Week 4 lab. Your **10-minute Week 5 presentation** should cover: the problem, your model, key results, and dosing implications."""),

        md("""\
---
## 📋 Scenario

A pharmacologist is designing a dosing protocol for metformin (diabetes medication). Blood concentration after oral administration:

$$C(t) = 85\\left(e^{-0.12t} - e^{-0.45t}\\right)$$

where $C$ is blood concentration (μg/mL) and $t$ is hours after ingestion.

**Therapeutic constraints:**
- Minimum effective: 15 μg/mL
- Maximum safe: 100 μg/mL
- Need therapeutic levels for 12-hour dosing intervals

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Concentration profile and peak time | ~20 min |
| B | Analyse the therapeutic window and safe dosing boundaries | ~20 min |
| C | Design a multiple dosing strategy | ~15 min |
| D | Calculate and interpret the rate of elimination | ~10 min |"""),

        code(LAB_SETUP + """
from scipy.optimize import fsolve

# Metformin pharmacokinetic parameters
D = 85     # dose factor

def C(t):
    'Blood concentration (μg/mL), t hours after ingestion.'
    return D * (np.exp(-0.12*t) - np.exp(-0.45*t))

def dC(t):
    'Rate of change of concentration (μg/mL/hour).'
    return D * (-0.12*np.exp(-0.12*t) + 0.45*np.exp(-0.45*t))

print("C(0) =", C(0), "μg/mL  (starts at zero — absorption not instant)")
print("C(1) =", round(C(1), 2), "μg/mL")
print("C(4) =", round(C(4), 2), "μg/mL")"""),

        md("""\
---
## Part A: Concentration Profile (~20 min)"""),

        code("""\
# A.1 — Concentration at key times
print(f"{'t (h)':>6} | {'C(t) μg/mL':>12} | {'C\\'(t)':>10} | Trend")
print("-" * 50)
for t in [0, 1, 2, 4, 8, 12]:
    trend = "↑ rising" if dC(t) > 0 else "↓ falling"
    print(f"{t:>6} | {C(t):>12.2f} | {dC(t):>10.3f} | {trend}")"""),

        md("""\
Find exact peak time by solving C'(t) = 0."""),

        code("""\
# A.2 — Find exact peak time by solving C'(t) = 0
# C'(t) = 85 * (-0.12*exp(-0.12t) + 0.45*exp(-0.45t)) = 0
# Rearranging: 0.45*exp(-0.45t) = 0.12*exp(-0.12t)
# → 0.45/0.12 = exp(0.33t) → t = ln(0.45/0.12) / 0.33

t_peak_analytic = np.log(0.45 / 0.12) / 0.33
C_peak = C(t_peak_analytic)

print(f"Peak time (analytic): t = {t_peak_analytic:.3f} hours = {t_peak_analytic*60:.0f} minutes")
print(f"Peak concentration:   C = {C_peak:.2f} μg/mL")
print(f"Safe? (< 100 μg/mL): {C_peak < 100}")"""),

        md("""\
Full concentration profile plot."""),

        code("""\
# A.3 — Full concentration profile plot
t_vals = np.linspace(0, 24, 500)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9))

ax1.plot(t_vals, C(t_vals), "steelblue", lw=2, label="Concentration C(t)")
ax1.axhline(15,  color="red",    ls="--", lw=1.5, label="Min therapeutic (15 μg/mL)")
ax1.axhline(100, color="orange", ls="--", lw=1.5, label="Max safe (100 μg/mL)")
ax1.fill_between(t_vals, 15, np.minimum(C(t_vals), 100),
                 where=(C(t_vals) >= 15), alpha=0.2, color="green", label="Therapeutic window")
ax1.plot(t_peak_analytic, C_peak, "ro", ms=10, label=f"Peak: t={t_peak_analytic:.2f}h, C={C_peak:.1f}")
ax1.set_ylabel("Concentration (μg/mL)")
ax1.set_title("Metformin Pharmacokinetics")
ax1.legend(fontsize=9)
ax1.grid(alpha=0.3)

ax2.plot(t_vals, dC(t_vals), "purple", lw=2, label="C'(t) = dC/dt")
ax2.axhline(0, color="k", lw=0.8)
ax2.axvline(t_peak_analytic, color="red", ls=":", alpha=0.5, label=f"Peak at {t_peak_analytic:.2f}h")
ax2.set_xlabel("Time (hours)")
ax2.set_ylabel("Rate of change (μg/mL/h)")
ax2.set_title("Rate of Concentration Change")
ax2.legend(fontsize=9)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part B: Therapeutic Window (~20 min)"""),

        code("""\
# B.1 — When does C(t) drop below therapeutic threshold of 15 μg/mL?
C_min = 15

# Numerical solution: find t > t_peak where C(t) = 15
def C_minus_min(t):
    return C(t) - C_min

# Search after the peak
t_end_guess = 12
t_end = fsolve(C_minus_min, t_end_guess)[0]
print(f"Therapeutic coverage ends at t = {t_end:.2f} hours")
print(f"Duration above threshold: {t_end:.2f} hours")
print(f"12-hour dosing interval sufficient? {t_end >= 12}")"""),

        md("""\
✏️ **Activity B:**
1. Can patients safely use a 12-hour dosing interval? What is the concentration at t = 12 hours?
2. If coverage is insufficient, what dose multiplier $D$ is needed to ensure $C(12) = 15$?

```python
# 1. Concentration at 12 hours:
print("C(12) =", round(C(12), 3), "μg/mL")
# 2. Required dose multiplier:
D_need = 15 / (np.exp(-0.12*12) - np.exp(-0.45*12))
print("Required D:", round(D_need, 2))
print("Peak with new D:", round(D_need * (np.exp(-0.12*t_peak_analytic) - np.exp(-0.45*t_peak_analytic)), 2), "μg/mL")
```"""),

        md("""\
---
## Part C: Multiple Dosing (~15 min)"""),

        code("""\
# C.1 — What concentration remains from first dose when second dose is taken?
C_residual = C(12)
C_peak_dose2 = C_residual + D    # residual + peak of new dose (at t=12+)

print(f"Residual from first dose at t=12h: {C_residual:.3f} μg/mL")
print(f"Immediately after second dose:     {C_peak_dose2:.2f} μg/mL")
print(f"Exceeds safe limit (100 μg/mL)?   {C_peak_dose2 > 100}")"""),

        md("""\
---
## Part D: Rate of Elimination (~10 min)"""),

        code("""\
# D.1 — Compare elimination rate near peak vs late phase
for t_s in [2, 10]:
    rate = dC(t_s)
    pct  = rate / C(t_s) * 100
    phase = "absorption-dominant" if t_s < t_peak_analytic else "elimination-dominant"
    print(f"t = {t_s}h: C'(t) = {rate:.3f} μg/mL/h  ({pct:.1f}%/h)  [{phase}]")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 5, 10 minutes)

1. **Problem** (~2 min): Why does dosing protocol matter for this drug?
2. **Model** (~3 min): Double-exponential form; what each term represents (absorption vs elimination).
3. **Results** (~3 min): Peak time, therapeutic window duration, safety at 12h — show the two-panel plot.
4. **Recommendation** (~2 min): Is 12-hour dosing adequate? What dose adjustment is needed?"""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 5 — Optimization
# ─────────────────────────────────────────────────────────────────────────────

def week5_student():
    return notebook([

        md("""\
# Week 5 Lab: Designing an Optimal Wildlife Corridor
**SCIE1500 — Analytical Methods for Scientists | Semester 2, 2026**

> **Lab format:** Work in your group. Discuss answers before typing code.
> **Today's session:** ~2 hours | Ask your tutor when stuck."""),

        md("""\
---
## 🌍 Scientific Scenario

The Department of Biodiversity is designing a **rectangular wildlife corridor** to connect two nature reserves. Available fencing: **2000 metres**.

Ecologists need the corridor to be as wide as possible (minimum 200 m) to prevent edge effects. The goal: **maximize area** within the fencing budget.

> *What dimensions give the largest corridor area?*"""),

        md("""\
---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Set up and formulate the constrained optimisation problem | ~15 min |
| B | Find optimal dimensions using calculus | ~25 min |
| C | Conduct a sensitivity analysis with tighter constraints | ~15 min |

**By the end of today you will be able to:**
- Translate a word problem into a constrained optimization
- Use constraint substitution to reduce to a single-variable problem
- Check feasibility of the mathematical solution against physical constraints"""),

        code(SETUP_IMPORTS),

        md("""\
---
## Part A: Problem Setup (~15 min)

Let $x$ = width of corridor (m), $y$ = length (m).

**Constraint:** $2x + 2y = 2000$ → $y = 1000 - x$

**Objective:** Maximize $A(x) = x \\cdot y = x(1000 - x)$

**Domain:** $x \\geq 200$ (minimum width) and $x \\leq 800$ (ensures $y \\geq 200$ by symmetry)"""),

        code("""\
# A.1 — Define area as a function of x only (after constraint substitution)
def A(x):
    'Area of corridor (m²) as function of width x.'
    return x * (1000 - x)    # A(x) = x(1000 - x) after substituting y = 1000 - x

# Check boundaries
print(f"A(200) = {A(200):,} m²  (minimum width, x = 200)")
print(f"A(500) = {A(500):,} m²  (candidate optimum)")
print(f"A(800) = {A(800):,} m²  (maximum width, y = 200)")
print()
print("The feasible domain is x ∈ [200, 800]")"""),

        md("""\
✏️ **Activity A:**
1. Why is the feasible domain $[200, 800]$ and not $[0, 1000]$?
2. What happens to the corridor if $x = 1000$? Is this physically meaningful?

```
Answers:
1. ...
2. ...
```"""),

        md("""\
---
## Part B: Optimal Dimensions (~25 min)

Take the derivative $A'(x) = \\frac{dA}{dx}$:

$$A(x) = 1000x - x^2 \\implies A'(x) = 1000 - 2x$$

Setting $A'(x) = 0$ gives $x = 500$ m."""),

        code("""\
# B.1 — Derivative and critical point
def dA(x):
    'Marginal area (m²/m) — rate of area gain per metre of added width.'
    return 1000 - 2 * x

# Critical point
x_crit = 1000 / 2
y_crit = 1000 - x_crit
A_crit = A(x_crit)

print(f"A'(x) = 1000 - 2x = 0  →  x_crit = {x_crit:.0f} m")
print(f"Second derivative A''(x) = -2 < 0  (confirms maximum)")
print(f"Optimal dimensions: width = {x_crit:.0f} m, length = {y_crit:.0f} m")
print(f"Maximum area: A({x_crit:.0f}) = {A_crit:,.0f} m²")"""),

        md("""\
Check feasibility: is x_crit in [200, 800]?"""),

        code("""\
# B.2 — Check feasibility: is x_crit in [200, 800]?
feasible = 200 <= x_crit <= 800
print(f"x_crit = {x_crit:.0f} m  feasible? {feasible}")
print()
        """),

        md("""\
The chart below shows how total border area varies with width."""),

        code("""\
# Plot area vs width
x_vals = np.linspace(200, 800, 300)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x_vals, A(x_vals) / 1e4, "steelblue", lw=2, label="Area A(x) (hectares)")
ax.plot(x_crit, A_crit / 1e4, "ro", ms=12, label=f"Optimum: x={x_crit:.0f}m, A={A_crit/1e4:.1f} ha")
ax.axvline(200, color="orange", ls="--", alpha=0.6, label="Min width = 200 m")
ax.axvline(800, color="orange", ls="--", alpha=0.6, label="Max width (y=200) = 800 m")
ax.set_xlabel("Width x (metres)")
ax.set_ylabel("Area (hectares)")
ax.set_title("Wildlife Corridor: Area vs Width")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity B:**
1. The optimal corridor is a square ($x = y = 500$ m). Is this surprising? Why does a square maximize area?
2. $A'(300) = ?$ What does the sign tell you about whether area is increasing or decreasing at $x = 300$?
3. $A'(700) = ?$ What does this tell you?

```python
print("A'(300) =", dA(300), "m²/m")
print("A'(700) =", dA(700), "m²/m")
# Answers:
# 1. ...
# 2. ...
# 3. ...
```"""),

        md("""\
---
## Part C: Sensitivity Analysis (~15 min)"""),

        code("""\
# C.1 — What if budget drops to 1800 m of fencing?
def A_budget(x, perim):
    'Area given perimeter budget.'
    y = perim / 2 - x
    return x * y

perim_new = 1800
x_opt_new = perim_new / 4   # optimal is still square: x = perimeter/4
A_opt_new = A_budget(x_opt_new, perim_new)

print(f"Budget 2000 m: optimal x = {x_crit:.0f} m, A = {A_crit:,.0f} m²")
print(f"Budget 1800 m: optimal x = {x_opt_new:.0f} m, A = {A_opt_new:,.0f} m²")
print(f"Area lost from 200 m less fencing: {A_crit - A_opt_new:,.0f} m² ({(A_crit - A_opt_new)/A_crit*100:.1f}%)")

# C.2 — What if minimum width increases to 250 m?
x_constrained = max(x_crit, 250)   # if optimal is inside constraint, use it; else use boundary
A_constrained = A(x_constrained)
print(f"\\nWith minimum width 250 m:")
print(f"  x* = {x_constrained:.0f} m  (still the unconstrained optimum? {x_crit >= 250})")
print(f"  A  = {A_constrained:,.0f} m²")"""),

        md("""\
✏️ **Activity C — group recommendation:**

Write a 3–4 sentence recommendation to the Department including:
- Optimal corridor dimensions for both budget scenarios
- How much area is lost per 100 m of fencing removed
- Whether the 250 m minimum width requirement changes the design

```
RECOMMENDATION:
...
```"""),

        md("""\
---
## ✅ Lab Wrap-Up

- [ ] Set up the objective function and constraint (Part A)
- [ ] Found the critical point and confirmed it as a maximum (Part B)
- [ ] Analysed sensitivity to budget and minimum width (Part C)
- [ ] **Groups 7 & 1:** Opened your Presentation Brief (Lab A or Lab B) and started Part A

> 💡 **Key pattern:** constraint → substitute → single-variable function → derivative → critical point → check feasibility."""),
    ])


def week5_lab_a():
    return notebook([

        md("""\
# Week 5 Presentation Brief — Variation A
## ☀️ Solar Farm Economics: Optimal Panel Configuration
**SCIE1500 — Semester 2, 2026 | Group 7 — presenting in Week 6**

> Work through all parts during the Week 5 lab. Your **10-minute Week 6 presentation** should cover: the problem, your model, optimal configuration, and climate sensitivity."""),

        md("""\
---
## 📋 Scenario

A renewable energy company designs a 50-ha solar farm near Geraldton. Annual revenue (thousands of dollars) depends on panel row spacing $x$ (metres):

$$R(x) = -2x^2 + 180x - 1600$$

**Constraints:** $8 \\leq x \\leq 60$ metres

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Find and classify critical points of the revenue function | ~25 min |
| B | Identify constraint boundaries and find the break-even range | ~20 min |
| C | Conduct a climate sensitivity and upgrade analysis | ~15 min |"""),

        code(LAB_SETUP + """

# Solar farm revenue model
def R(x):
    'Annual revenue (thousands $) for panel spacing x metres.'
    return -2*x**2 + 180*x - 1600

def dR(x):
    'Marginal revenue ($/m of spacing change).'
    return -4*x + 180

def d2R(x):
    'Second derivative.'
    return -4    # constant negative → always concave down → critical point is maximum

print("R(8)  =", R(8),  "($000)")
print("R(45) =", R(45), "($000)")
print("R(60) =", R(60), "($000)")"""),

        md("""\
---
## Part A: Critical Point Analysis (~25 min)"""),

        code("""\
# A.1 — Find the critical point: solve R'(x) = 0
# -4x + 180 = 0  →  x = 45
x_crit = 180 / 4
R_crit = R(x_crit)
R2 = d2R(x_crit)

print(f"R'(x) = -4x + 180 = 0  →  x* = {x_crit} metres")
print(f"R''(x) = {R2}  (< 0 → maximum confirmed)")
print(f"R({x_crit:.0f}) = ${R_crit:,.0f} thousand/year")"""),

        md("""\
Check feasibility and compare to boundaries."""),

        code("""\
# A.2 — Check feasibility and compare to boundaries
for x_s, label in [(x_crit, "Optimal (x=45)"), (8, "Min spacing (x=8)"), (60, "Max spacing (x=60)")]:
    feasible = 8 <= x_s <= 60
    print(f"{label}: R = ${R(x_s):,.0f}k  feasible? {feasible}")"""),

        md("""\
Plot revenue curve with constraint boundaries."""),

        code("""\
# A.3 — Plot revenue curve with constraint boundaries
x_vals = np.linspace(5, 65, 300)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x_vals, R(x_vals), "steelblue", lw=2, label="Revenue R(x)")
ax.plot(x_crit, R_crit, "ro", ms=12, label=f"Optimal: x={x_crit:.0f}m, R=${R_crit:.0f}k")
ax.axvline(8,  color="orange", ls="--", alpha=0.7, label="Min spacing (8m)")
ax.axvline(60, color="orange", ls="--", alpha=0.7, label="Max spacing (60m)")
ax.axhline(0,  color="k", lw=0.8)
ax.set_xlabel("Panel Row Spacing x (metres)")
ax.set_ylabel("Annual Revenue ($000)")
ax.set_title("Solar Farm Revenue Optimization")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
ax.set_ylim(-500, 2500)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Activity A:**
1. Why does revenue *decrease* both below and above the optimal spacing?
2. The unconstrained optimum $x^* = 45$ m falls inside $[8, 60]$. What if it fell outside?

```
Answers:
1. ...
2. ...
```"""),

        md("""\
---
## Part B: Break-Even Analysis (~20 min)"""),

        code("""\
# B.1 — Break-even points: solve R(x) = 0
# -2x² + 180x - 1600 = 0  →  x² - 90x + 800 = 0
a, b, c = -2, 180, -1600
disc = b**2 - 4*a*c
x_be1 = (-b + np.sqrt(disc)) / (2*a)
x_be2 = (-b - np.sqrt(disc)) / (2*a)

if x_be1 > x_be2:
    x_be1, x_be2 = x_be2, x_be1

print(f"Break-even points: x = {x_be1:.1f} m and x = {x_be2:.1f} m")
print(f"Farm is profitable for x ∈ [{x_be1:.1f}, {x_be2:.1f}] metres")
print(f"Both within operational constraints [8, 60]? {8 <= x_be1 and x_be2 <= 60}")"""),

        md("""\
---
## Part C: Climate Sensitivity (~15 min)"""),

        code("""\
# C.1 — Climate change: 15% revenue reduction, and high-efficiency panel upgrade
def R_climate(x):
    'Revenue under climate change (−15%).'
    return 0.85 * R(x)

def R_upgrade(x):
    'Revenue with high-efficiency panels (+20%).'
    return 1.20 * R(x)

for fn, label in [(R, "Baseline"), (R_climate, "Climate (−15%)"), (R_upgrade, "Upgrade (+20%)")]:
    x_opt = 45    # optimal spacing doesn't change (quadratic, same derivative structure)
    print(f"{label:>20}: optimal R = ${fn(x_opt):,.0f}k at x = {x_opt} m")
        """),

        md("""\
The chart below shows all three scenarios."""),

        code("""\
# Plot all three scenarios
fig, ax = plt.subplots(figsize=(9, 5))
x_vals = np.linspace(5, 65, 300)
ax.plot(x_vals, R(x_vals),         "steelblue", lw=2, label="Baseline")
ax.plot(x_vals, R_climate(x_vals), "firebrick", lw=2, ls="--", label="Climate (−15%)")
ax.plot(x_vals, R_upgrade(x_vals), "green",     lw=2, ls=":",  label="Upgrade (+20%)")
ax.axvline(8,  color="orange", ls="--", alpha=0.5)
ax.axvline(60, color="orange", ls="--", alpha=0.5)
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("Panel Row Spacing x (metres)")
ax.set_ylabel("Annual Revenue ($000)")
ax.set_title("Solar Farm: Scenario Comparison")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **CEO Recommendation (4–5 sentences):**
- Optimal spacing and expected revenue
- Climate risk: how much revenue could be lost?
- Whether the panel upgrade is financially justified

```
RECOMMENDATION:
...
```"""),

        md("""\
---
## ✅ Presentation Checklist (Week 6, 10 minutes)

1. **Problem** (~2 min): Explain why tree spacing affects revenue.
2. **Model** (~3 min): Present the revenue function, derivative, and critical point.
3. **Results** (~3 min): State optimal spacing, break-even range, and climate scenario outcomes.
4. **Recommendation** (~2 min): Give a spacing decision and upgrade advice with supporting numbers."""),
    ])


def week5_lab_b():
    return notebook([

        md("""\
# Week 5 Presentation Brief — Variation B
## 🐟 Aquaculture Profit: Optimal Stocking Density for Barramundi
**SCIE1500 — Semester 2, 2026 | Group 1 (second presentation) — presenting in Week 6**

> Work through all parts during the Week 5 lab. Your **10-minute Week 6 presentation** should cover: the problem, your model, optimal stocking density, and disease risk."""),

        md("""\
---
## 📋 Scenario

A barramundi farm in Exmouth optimizes stocking density. Profit (thousands of dollars/year) as a function of stocking density $d$ (fish per 100 m³):

$$P(d) = -0.5d^2 + 55d - 800$$

**Constraints:** $10 \\leq d \\leq 80$ fish/100 m³

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Optimise stocking density using calculus | ~25 min |
| B | Find break-even density and interpret marginal profit | ~20 min |
| C | Compare profit outcomes under disease and aeration scenarios | ~15 min |"""),

        code(LAB_SETUP + """

# Barramundi profit model
def P(d):
    'Annual profit (thousands $) at stocking density d fish/100m³.'
    return -0.5*d**2 + 55*d - 800

def dP(d):
    'Marginal profit ($/fish per 100m³).'
    return -d + 55

d_min, d_max = 10, 80    # operational constraints

print("P(10) =", P(10), "($000)")
print("P(55) =", P(55), "($000)")
print("P(80) =", P(80), "($000)")"""),

        md("""\
---
## Part A: Optimization (~25 min)"""),

        code("""\
# A.1 — Critical point: P'(d) = -d + 55 = 0  →  d* = 55
d_crit = 55
P_crit = P(d_crit)
print(f"P'(d) = -d + 55 = 0  →  d* = {d_crit} fish/100m³")
print(f"P''(d) = -1 < 0  →  maximum confirmed")
print(f"P({d_crit}) = ${P_crit:,.0f} thousand/year")

# Feasibility check
feasible = d_min <= d_crit <= d_max
print(f"Feasible (within [{d_min}, {d_max}])? {feasible}")"""),

        md("""\
Compare critical point to boundaries."""),

        code("""\
# A.2 — Compare critical point to boundaries
for d_s, label in [(d_crit, "Optimal (d=55)"), (d_min, "Min density (d=10)"), (d_max, "Max density (d=80)")]:
    print(f"{label}: P = ${P(d_s):,.0f}k  feasible? {d_min <= d_s <= d_max}")"""),

        md("""\
Plot profit curve."""),

        code("""\
# A.3 — Plot profit curve
d_vals = np.linspace(5, 90, 300)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(d_vals, P(d_vals), "steelblue", lw=2, label="Profit P(d)")
ax.plot(d_crit, P_crit, "ro", ms=12, label=f"Optimal: d={d_crit}, P=${P_crit:.0f}k")
ax.axvline(d_min, color="orange", ls="--", alpha=0.7, label=f"Min density ({d_min})")
ax.axvline(d_max, color="orange", ls="--", alpha=0.7, label=f"Max density ({d_max})")
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("Stocking Density d (fish per 100 m³)")
ax.set_ylabel("Annual Profit ($000)")
ax.set_title("Barramundi Aquaculture: Stocking Density Optimization")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part B: Break-Even and Marginal Profit (~20 min)"""),

        code("""\
# B.1 — Break-even densities: solve P(d) = 0
# -0.5d² + 55d - 800 = 0  →  d² - 110d + 1600 = 0
a, b, c = -0.5, 55, -800
disc = b**2 - 4*a*c
d_be1 = (-b - np.sqrt(disc)) / (2*a)
d_be2 = (-b + np.sqrt(disc)) / (2*a)
if d_be1 > d_be2: d_be1, d_be2 = d_be2, d_be1

print(f"Break-even densities: d = {d_be1:.1f} and d = {d_be2:.1f} fish/100m³")
print(f"Farm is profitable for d ∈ [{d_be1:.1f}, {d_be2:.1f}]")

# Marginal profit at current operating density
d_current = 40
mp = dP(d_current)
print(f"\\nMarginal profit at d = {d_current}: P'({d_current}) = {mp} ($k / fish per 100m³)")
print(f"→ Increasing density by 1 {'increases' if mp > 0 else 'decreases'} profit by ${abs(mp):.0f}k")"""),

        md("""\
---
## Part C: Scenario Analysis (~15 min)"""),

        code("""\
# C.1 — Disease and aeration scenarios
def P_disease(d):
    'Profit under disease outbreak (-400k fixed costs).'
    return -0.5*d**2 + 55*d - 1200

def P_aeration(d):
    'Profit with aeration upgrade (improved yield).'
    return -0.4*d**2 + 60*d - 900

d_aer_crit = 60 / 0.8    # P_aeration'(d) = -0.8d + 60 = 0
d_vals = np.linspace(5, 90, 300)

print("Optimal results by scenario:")
print(f"  Baseline:  d* = {d_crit:.0f}, P* = ${P_crit:.0f}k")
print(f"  Disease:   d* = {d_crit:.0f}, P* = ${P_disease(d_crit):.0f}k  (same d, lower profit)")
print(f"  Aeration:  d* = {d_aer_crit:.0f}, P* = ${P_aeration(d_aer_crit):.0f}k")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(d_vals, P(d_vals),         "steelblue", lw=2, label="Baseline")
ax.plot(d_vals, P_disease(d_vals), "firebrick", lw=2, ls="--", label="Disease outbreak")
ax.plot(d_vals, P_aeration(d_vals),"green",     lw=2, ls=":",  label="Aeration upgrade")
ax.axvline(d_min, color="orange", ls="--", alpha=0.5)
ax.axvline(d_max, color="orange", ls="--", alpha=0.5)
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("Stocking Density d (fish per 100 m³)")
ax.set_ylabel("Annual Profit ($000)")
ax.set_title("Barramundi: Scenario Comparison")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Farm Manager Advisory (4–5 sentences):**
- Recommended stocking density and expected profit
- Disease risk: does the farm still break even under the disease scenario?
- Aeration upgrade: is it worthwhile? (Estimate the cost it would need to pay off at)

```
ADVISORY:
...
```"""),

        md("""\
---
## ✅ Presentation Checklist (Week 6, 10 minutes)

1. **Problem** (~2 min): Explain the trade-off between stocking density, yield, and mortality.
2. **Model** (~3 min): Present the profit function, take the derivative, and find the critical point.
3. **Results** (~3 min): Report optimal density, break-even range, and scenario comparison.
4. **Recommendation** (~2 min): Recommend a stocking density and propose risk mitigation steps."""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 6
# ─────────────────────────────────────────────────────────────────────────────

def week6_student():
    return notebook([

        md("""\
# Week 6 Lab — Carbon Sequestration and Integration
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Work in your groups. Read each section, run the code cells, and answer the written prompts.

---
**This week:** We apply integration to model cumulative carbon captured by a reforestation project."""),

        md("""\
---
## 📋 Scientific Scenario

A reforestation project in the Wheatbelt plants native trees across 500 ha. The rate of carbon sequestration (tonnes CO₂ per hectare per year) declines over time as trees mature:

$$R(t) = 12 e^{-0.05t}$$

where $t$ is years since planting ($t = 0$ to $t = 40$). Carbon credits sell at **$25 per tonne**.

---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Distinguish rates from totals by interpreting R(t) and F(t) | ~20 min |
| B | Find antiderivatives and determine the constant of integration | ~20 min |
| C | Value the carbon project over 40 years | ~20 min |

By the end you should be able to: compute antiderivatives of exponential functions; evaluate definite integrals; interpret the constant of integration; and translate carbon totals into revenue."""),

        code(SETUP_IMPORTS + """

# Carbon sequestration model
def R(t):
    'Sequestration rate (t CO2/ha/yr) at year t.'
    return 12 * np.exp(-0.05 * t)

t_vals = np.arange(0, 41)
print("Year | Rate (t CO2/ha/yr)")
print("-" * 28)
for t in [0, 5, 10, 20, 40]:
    print(f"  {t:2d} |   {R(t):6.2f}")"""),

        md("""\
---
## Part A: Rates vs Totals (~20 min)

$R(t) = 12e^{-0.05t}$ is the **instantaneous rate** — how fast carbon is captured at year $t$.

The **total** carbon captured from $t=0$ to $t=T$ is the definite integral:

$$F(T) = \\int_0^T R(t)\\,dt = \\int_0^T 12e^{-0.05t}\\,dt$$

**A.1** Plot $R(t)$ over 40 years. Describe the shape: is the rate increasing or decreasing? Why does this make biological sense?"""),

        code("""\
# A.1 — Plot the sequestration rate
t_vals = np.linspace(0, 40, 200)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_vals, R(t_vals), "forestgreen", lw=2.5)
ax.fill_between(t_vals, R(t_vals), alpha=0.15, color="forestgreen")
ax.set_xlabel("Years since planting (t)")
ax.set_ylabel("Rate (tonnes CO₂/ha/yr)")
ax.set_title("Carbon Sequestration Rate R(t) = 12 e^{−0.05t}")
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Rate at t=0 : {R(0):.2f} t CO2/ha/yr")
print(f"Rate at t=20: {R(20):.2f} t CO2/ha/yr")
print(f"Rate at t=40: {R(40):.2f} t CO2/ha/yr")"""),

        md("""\
Numerical approximation of total carbon in first 5 years."""),

        code("""\
# A.2 — Numerical approximation of total carbon in first 5 years
# Riemann sum (trapezoidal) for ∫₀⁵ R(t) dt
from numpy import trapz
t_fine = np.linspace(0, 5, 1000)
total_5yr = trapz(R(t_fine), t_fine)
print(f"Approximate total carbon (0–5 yr, per hectare): {total_5yr:.2f} tonnes CO2")
print(f"On 500 ha: {500 * total_5yr:,.0f} tonnes CO2")"""),

        md("""\
---
## Part B: Antiderivatives (~20 min)

Recall: $\\int e^{kt}\\,dt = \\dfrac{1}{k}e^{kt} + C$

**B.1** Find the general antiderivative $F(t)$ of $R(t) = 12e^{-0.05t}$.

$$F(t) = \\int 12e^{-0.05t}\\,dt = \\frac{12}{-0.05}e^{-0.05t} + C = -240e^{-0.05t} + C$$

**B.2** Use the initial condition $F(0) = 0$ (no carbon captured at $t=0$) to find $C$.

$$F(0) = -240e^{0} + C = 0 \\implies C = 240$$

So: $F(t) = 240(1 - e^{-0.05t})$

✏️ **Interpret $C$:** What would $F(0)$ equal if $C \\neq 240$? What does the constant of integration represent in this context?"""),

        code("""\
# B.1 — Antiderivative F(t) = 240(1 - e^{-0.05t}) per hectare
def F(t):
    'Cumulative CO2 captured (t CO2/ha) from year 0 to year t.'
    return 240 * (1 - np.exp(-0.05 * t))

# Verify: F(0) = 0
print(f"F(0) = {F(0):.4f}  (should be 0)")
print(f"F(5) = {F(5):.2f} t CO2/ha")
print(f"F(20) = {F(20):.2f} t CO2/ha")
print(f"F(40) = {F(40):.2f} t CO2/ha")

# Long-run limit
print(f"Long-run limit as t→∞: {240:.0f} t CO2/ha")"""),

        md("""\
Plot cumulative carbon F(t)."""),

        code("""\
# B.2 — Plot cumulative carbon F(t)
t_vals = np.linspace(0, 40, 200)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(t_vals, R(t_vals), "forestgreen", lw=2.5)
axes[0].fill_between(t_vals, R(t_vals), alpha=0.15, color="forestgreen")
axes[0].set_title("Rate R(t)")
axes[0].set_xlabel("Years")
axes[0].set_ylabel("t CO2/ha/yr")
axes[0].grid(alpha=0.3)

axes[1].plot(t_vals, F(t_vals), "darkblue", lw=2.5)
axes[1].axhline(240, color="red", ls="--", alpha=0.6, label="Asymptote: 240 t/ha")
axes[1].set_title("Cumulative Carbon F(t)")
axes[1].set_xlabel("Years")
axes[1].set_ylabel("t CO2/ha")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part C: Project Valuation (~20 min)

The project covers **500 ha** and carbon credits sell at **$25/tonne CO₂**.

**C.1** Calculate total carbon captured across the full 500 ha over 40 years.

**C.2** Calculate total revenue from selling carbon credits.

**C.3** At what year does the project capture half of its 40-year total?"""),

        code("""\
# C.1 — Total carbon: 500 ha × F(40)
area_ha = 500
price_per_tonne = 25

F_40 = F(40)
total_carbon = area_ha * F_40
print(f"Carbon per hectare (0–40 yr): {F_40:.1f} t CO2/ha")
print(f"Total carbon (500 ha):        {total_carbon:,.0f} t CO2")"""),

        md("""\
Revenue."""),

        code("""\
# C.2 — Revenue
total_revenue = total_carbon * price_per_tonne
print(f"Carbon credit revenue: ${total_revenue:,.0f}")

# C.3 — Year at which half the 40-year total is captured
half_target = F_40 / 2
# Solve F(t) = half_target → 240(1 - e^{-0.05t}) = half_target
# → e^{-0.05t} = 1 - half_target/240
# → t = -ln(1 - half_target/240) / 0.05
t_half = -np.log(1 - half_target / 240) / 0.05
print(f"\\nHalf the 40-year total = {half_target:.1f} t CO2/ha")
print(f"Reached at year t = {t_half:.1f}")

# Verify
print(f"F({t_half:.1f}) = {F(t_half):.1f}  (check ≈ {half_target:.1f})")"""),

        md("""\
Annual revenue stream."""),

        code("""\
# C.4 — Annual revenue stream
years = np.arange(1, 41)
annual_carbon_per_ha = np.array([F(t) - F(t-1) for t in years])
annual_revenue = annual_carbon_per_ha * area_ha * price_per_tonne

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(years, annual_revenue / 1e3, color="seagreen", alpha=0.7)
ax.set_xlabel("Year")
ax.set_ylabel("Annual Revenue ($000)")
ax.set_title("Annual Carbon Credit Revenue — 500 ha Reforestation")
ax.grid(alpha=0.3, axis="y")
plt.tight_layout()
plt.show()

print(f"Year 1 revenue: ${annual_revenue[0]:,.0f}")
print(f"Year 40 revenue: ${annual_revenue[39]:,.0f}")
print(f"Total 40-year revenue: ${annual_revenue.sum():,.0f}")"""),

        md("""\
✏️ **Group Discussion (2–3 sentences each):**

1. Why does the sequestration rate decrease over time? What biological process does this reflect?
2. The long-run limit of $F(t)$ is 240 t CO₂/ha. What does this mean for an infinite project?
3. Should landholders sell carbon credits annually or wait? What does the revenue profile suggest?

```
DISCUSSION:
...
```"""),

        md("""\
---
## ✅ Submission Exercise — Batch 2 (due Tuesday 8 September, 11:59 pm)

**Submit via LMS. Covers Weeks 4–6 (limits, differentiation, integration).**

Work individually. Show all working. Write Python code where indicated.

---
### Q1 — Limits and Continuity (Week 4)

A population model uses:

$$P(t) = \\frac{1000t}{t + 5}$$

**(a)** Evaluate $\\lim_{t \\to \\infty} P(t)$. Show your working algebraically (divide numerator and denominator by $t$).

**(b)** Is $P(t)$ continuous for all $t \\geq 0$? Justify briefly.

**(c)** Write Python code to verify your limit answer numerically by evaluating $P(t)$ at $t = 100, 1000, 10000$.

```python
# Q1c — numerical limit verification
import numpy as np

def P(t):
    return 1000*t / (t + 5)

# Evaluate at large t values
# YOUR CODE HERE
```

---
### Q2 — Differentiation and Optimisation (Week 5)

A timber company's profit (thousands of dollars) as a function of harvest age $a$ (years) is:

$$\\pi(a) = 80a - 2a^2 - 150 \\quad \\text{for } 5 \\leq a \\leq 30$$

**(a)** Find $\\pi'(a)$ using the power rule. Show each step.

**(b)** Find the harvest age $a^*$ that maximises profit. Use the second derivative to confirm it is a maximum.

**(c)** Write Python code to: (i) evaluate $\\pi(a^*)$ and (ii) check the boundary values $\\pi(5)$ and $\\pi(30)$.

```python
# Q2c — profit at critical point and boundaries
# YOUR CODE HERE
```

**(d)** Interpret: what does $\\pi'(20) = -0$ (if it were zero) mean in harvesting terms?

---
### Q3 — Integration and Accumulation (Week 6)

A bushfire recovery site sequesters carbon at rate $R(t) = 8e^{-0.04t}$ tonnes CO₂/ha/yr.

**(a)** Find the antiderivative $F(t)$ with $F(0) = 0$. Show the rule you used.

**(b)** Calculate the total carbon captured per hectare over 30 years. Give an exact expression and a decimal approximation.

**(c)** Write Python code to: plot $R(t)$ for $t \\in [0, 30]$; shade the area under the curve; annotate with the definite integral value from part (b).

```python
# Q3c — plot and shade
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# YOUR CODE HERE
```

**(d)** If carbon credits sell at $30/tonne and the site covers 250 ha, calculate total project revenue over 30 years."""),
    ])


def week6_lab_a():
    return notebook([

        md("""\
# Week 6 Presentation Brief — Variation A
## 🌱 Soil Carbon Sequestration: Integration in Agriculture
**SCIE1500 — Semester 2, 2026 | Group 2 (first presentation) — presenting in Week 7**

> Work through all parts during the Week 6 lab. Your **10-minute Week 7 presentation** should cover: the sequestration model, antiderivative derivation, cumulative carbon estimate, and policy recommendation."""),

        md("""\
---
## 📋 Scenario

A soil carbon project converts 800 ha of cropland to improved pasture. Lab measurements show the soil carbon sequestration rate declines as soils reach a new equilibrium:

$$R(t) = 15e^{-0.08t} \\quad \\text{(tonnes CO}_2\\text{-e/ha/yr)}$$

Carbon is reported as CO₂-equivalent (multiply raw soil carbon by **3.67** for CO₂-e). Credits sell at **$28/tonne CO₂-e**. The project runs for **25 years**.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Derive the antiderivative and apply the initial condition | ~25 min |
| B | Calculate cumulative carbon capture and total project revenue | ~20 min |
| C | Conduct a sensitivity analysis on the decay rate | ~15 min |"""),

        code(LAB_SETUP + """

# Soil carbon model
def R(t):
    'Sequestration rate (t CO2-e/ha/yr) at year t.'
    return 15 * np.exp(-0.08 * t)

area_ha = 800
price   = 28   # $/tonne CO2-e

print("Year | Rate (t CO2-e/ha/yr)")
print("-" * 30)
for t in [0, 5, 10, 20, 25]:
    print(f"  {t:2d} |   {R(t):6.3f}")"""),

        md("""\
---
## Part A: Antiderivative (~25 min)

Using $\\int e^{kt}\\,dt = \\frac{1}{k}e^{kt} + C$:

$$F(t) = \\int 15e^{-0.08t}\\,dt = \\frac{15}{-0.08}e^{-0.08t} + C = -187.5e^{-0.08t} + C$$

**A.1** Apply $F(0) = 0$:

$$F(0) = -187.5e^{0} + C = 0 \\implies C = 187.5$$

$$\\boxed{F(t) = 187.5(1 - e^{-0.08t})}$$"""),

        code("""\
# A.1 — Cumulative soil carbon per hectare
def F(t):
    'Cumulative CO2-e captured (t/ha) from year 0 to year t.'
    return 187.5 * (1 - np.exp(-0.08 * t))

print(f"F(0)  = {F(0):.2f}  (should be 0)")
print(f"F(5)  = {F(5):.2f} t CO2-e/ha")
print(f"F(25) = {F(25):.2f} t CO2-e/ha")
print(f"Long-run limit = 187.5 t CO2-e/ha")"""),

        md("""\
Plot rate and cumulative together."""),

        code("""\
# A.2 — Plot rate and cumulative together
t_vals = np.linspace(0, 25, 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(t_vals, R(t_vals), "saddlebrown", lw=2.5)
ax1.fill_between(t_vals, R(t_vals), alpha=0.2, color="saddlebrown")
ax1.set_xlabel("Years"); ax1.set_ylabel("Rate (t CO2-e/ha/yr)")
ax1.set_title("Sequestration Rate R(t)"); ax1.grid(alpha=0.3)

ax2.plot(t_vals, F(t_vals), "darkgreen", lw=2.5)
ax2.axhline(187.5, color="red", ls="--", alpha=0.5, label="Limit: 187.5")
ax2.set_xlabel("Years"); ax2.set_ylabel("Cumulative (t CO2-e/ha)")
ax2.set_title("Cumulative Carbon F(t)"); ax2.legend(); ax2.grid(alpha=0.3)

plt.tight_layout(); plt.show()"""),

        md("""\
---
## Part B: Project Revenue (~20 min)"""),

        code("""\
# B.1 — Total carbon and revenue over 25 years
F_25 = F(25)
total_carbon = area_ha * F_25
total_revenue = total_carbon * price

print(f"Cumulative carbon per ha (25 yr): {F_25:.2f} t CO2-e/ha")
print(f"Total carbon (800 ha):            {total_carbon:,.0f} t CO2-e")
print(f"Total revenue @ $28/t:            ${total_revenue:,.0f}")"""),

        md("""\
Year at which 50% of 25-year total is reached."""),

        code("""\
# B.2 — Year at which 50% of 25-year total is reached
half = F_25 / 2
# F(t) = half → 187.5(1 - e^{-0.08t}) = half
# e^{-0.08t} = 1 - half/187.5 → t = -ln(1 - half/187.5) / 0.08
t_half = -np.log(1 - half / 187.5) / 0.08
print(f"50% of 25-yr total = {half:.2f} t CO2-e/ha")
print(f"Reached at year t = {t_half:.1f}")"""),

        md("""\
---
## Part C: Sensitivity Analysis (~15 min)"""),

        code("""\
# C.1 — How does revenue change with decay rate k?
for k, label in [(0.05, "Slow (k=0.05)"), (0.08, "Baseline (k=0.08)"), (0.12, "Fast (k=0.12)")]:
    F_alt = (15 / k) * (1 - np.exp(-k * 25))
    rev = area_ha * F_alt * price
    print(f"{label}: F(25)={F_alt:.1f} t/ha, Revenue=${rev:,.0f}")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 7, 10 minutes)

1. **Problem** (~2 min): Explain why the sequestration rate declines over time.
2. **Model** (~3 min): Derive $F(t) = 187.5(1 - e^{-0.08t})$ and interpret the constant $C = 187.5$.
3. **Results** (~3 min): Report total carbon captured, total revenue, and the half-life year.
4. **Policy** (~2 min): Argue whether 25 years is the optimal project length."""),
    ])


def week6_lab_b():
    return notebook([

        md("""\
# Week 6 Presentation Brief — Variation B
## 💧 Groundwater Recharge: Cumulative Infiltration
**SCIE1500 — Semester 2, 2026 | Group 1 (second presentation) — presenting in Week 7**

> Work through all parts during the Week 6 lab. Your **10-minute Week 7 presentation** should cover: the infiltration model, antiderivative, total volume, and whether the seasonal target is met."""),

        md("""\
---
## 📋 Scenario

A managed aquifer recharge (MAR) scheme in the Murray-Darling Basin diverts floodwater. The infiltration rate declines as soil pores fill:

$$I(t) = 20e^{-0.12t} \\quad \\text{(ML/day)}$$

where $t$ is days into the recharge season. The scheme runs for a **120-day season**. The seasonal target is **1,500 ML**. Water entitlement costs **$1,500/ML**.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Derive the antiderivative and calculate cumulative recharge volume | ~25 min |
| B | Determine whether the scheme meets its 1,500 ML target | ~20 min |
| C | Find the optimal season length based on marginal infiltration | ~15 min |"""),

        code(LAB_SETUP + """

# Groundwater infiltration model
def I(t):
    'Infiltration rate (ML/day) at day t.'
    return 20 * np.exp(-0.12 * t)

target_ML   = 1500
season_days = 120
cost_per_ML = 1500

print("Day | Rate (ML/day)")
print("-" * 22)
for t in [0, 10, 30, 60, 120]:
    print(f"  {t:3d} |  {I(t):6.3f}")"""),

        md("""\
---
## Part A: Antiderivative (~25 min)

$$V(t) = \\int_0^t 20e^{-0.12\\tau}\\,d\\tau = \\frac{20}{-0.12}\\left[e^{-0.12\\tau}\\right]_0^t = \\frac{20}{0.12}(1 - e^{-0.12t})$$

$$V(t) = \\frac{500}{3}(1 - e^{-0.12t}) \\approx 166.7(1 - e^{-0.12t})$$"""),

        code("""\
# A.1 — Cumulative volume V(t)
def V(t):
    'Cumulative volume (ML) recharged from day 0 to day t.'
    return (20 / 0.12) * (1 - np.exp(-0.12 * t))

print(f"V(10)  = {V(10):.1f} ML")
print(f"V(30)  = {V(30):.1f} ML")
print(f"V(120) = {V(120):.1f} ML")
print(f"Long-run limit = {20/0.12:.1f} ML")"""),

        md("""\
Plot both."""),

        code("""\
# A.2 — Plot both
t_vals = np.linspace(0, 120, 300)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(t_vals, I(t_vals), "steelblue", lw=2.5)
ax1.fill_between(t_vals, I(t_vals), alpha=0.2, color="steelblue")
ax1.set_xlabel("Day"); ax1.set_ylabel("Infiltration rate (ML/day)")
ax1.set_title("Infiltration Rate I(t)"); ax1.grid(alpha=0.3)

ax2.plot(t_vals, V(t_vals), "darkblue", lw=2.5)
ax2.axhline(target_ML, color="red", ls="--", label=f"Target: {target_ML} ML")
ax2.axhline(20/0.12, color="gray", ls=":", alpha=0.5, label="Limit: 166.7 ML")
ax2.set_xlabel("Day"); ax2.set_ylabel("Cumulative Volume (ML)")
ax2.set_title("Cumulative Recharge V(t)"); ax2.legend(); ax2.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
---
## Part B: Does the Scheme Meet Its Target? (~20 min)"""),

        code("""\
# B.1 — Volume at end of season
V_season = V(season_days)
print(f"Volume recharged over {season_days} days: {V_season:.1f} ML")
print(f"Target: {target_ML} ML")
print(f"Target met? {V_season >= target_ML}")
print(f"Shortfall/surplus: {V_season - target_ML:+.1f} ML")
print(f"\\nNote: long-run limit is {20/0.12:.1f} ML — target {target_ML} ML {'can' if 20/0.12 >= target_ML else 'CANNOT'} be met.")"""),

        md("""\
Cost of water used."""),

        code("""\
# B.2 — Cost of water used
cost_total = V_season * cost_per_ML
print(f"Cost of {V_season:.0f} ML @ ${cost_per_ML}/ML: ${cost_total:,.0f}")"""),

        md("""\
---
## Part C: Optimal Season Length (~15 min)

At what day does the marginal rate of recharge drop to 1 ML/day (not worth running pumps)?"""),

        code("""\
# C.1 — Day when rate drops to 1 ML/day
# I(t) = 1 → 20 e^{-0.12t} = 1 → t = -ln(1/20)/0.12
t_cutoff = -np.log(1 / 20) / 0.12
V_cutoff = V(t_cutoff)
print(f"Rate drops to 1 ML/day at t = {t_cutoff:.1f} days")
print(f"Volume by then: {V_cutoff:.1f} ML")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 7, 10 minutes)

1. **Problem** (~2 min): Explain why infiltration declines over the season.
2. **Model** (~3 min): Derive $V(t)$ and explain why the long-run limit is 166.7 ML.
3. **Results** (~3 min): Show whether the 1,500 ML target can be met and present the cost analysis.
4. **Recommendation** (~2 min): Recommend a practical season length with supporting evidence."""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 7
# ─────────────────────────────────────────────────────────────────────────────

def week7_student():
    return notebook([

        md("""\
# Week 7 Lab — Consumer and Producer Surplus
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Work in your groups. Run all code cells in order, fill in the written prompts.

---
**This week:** We use definite integrals to measure welfare — how much buyers and sellers gain from trading at market equilibrium."""),

        md("""\
---
## 📋 Scientific Scenario

The Australian domestic wheat market has the following supply and demand functions:

- **Demand:** $Q_d = 500 - 4P$ (thousand tonnes per year)
- **Supply:** $Q_s = -100 + 2P$ (thousand tonnes per year)

where $P$ is the price in dollars per tonne.

Consumer surplus (CS) is the area between the demand curve and the equilibrium price — what buyers would have paid minus what they actually pay. Producer surplus (PS) is the area between the equilibrium price and the supply curve.

---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Find market equilibrium algebraically and verify with Python | ~20 min |
| B | Calculate consumer and producer surplus graphically | ~20 min |
| C | Verify surplus using definite integration | ~20 min |

By the end you should be able to: solve supply-demand systems algebraically; derive inverse functions; compute CS and PS as definite integrals; and interpret welfare measures."""),

        code(SETUP_IMPORTS + """

# Demand: Qd = 500 - 4P  →  P = (500 - Q)/4
# Supply: Qs = -100 + 2P →  P = (Q + 100)/2

def demand_P(Q):
    'Inverse demand: price as a function of quantity.'
    return (500 - Q) / 4

def supply_P(Q):
    'Inverse supply: price as a function of quantity.'
    return (Q + 100) / 2

# Equilibrium: Qd = Qs → 500 - 4P = -100 + 2P → 6P = 600 → P* = 100
P_star = 100
Q_star = 500 - 4 * P_star
print(f"Equilibrium: P* = ${P_star}, Q* = {Q_star} thousand tonnes")
print(f"Demand intercept (P when Q=0): P = {demand_P(0):.0f}")
print(f"Supply intercept (P when Q=0): P = {supply_P(0):.0f}")"""),

        md("""\
---
## Part A: Finding Equilibrium (~20 min)

**A.1** Verify the equilibrium algebraically: set $Q_d = Q_s$ and solve for $P^*$, then find $Q^*$.

✏️ Show your working here:
```
Qd = Qs
500 - 4P = -100 + 2P
...
P* = ?, Q* = ?
```"""),

        code("""\
# A.1 — Solve equilibrium numerically (confirm algebra)
from numpy.linalg import solve

# Qd = Qs: 500 - 4P = -100 + 2P → 6P = 600 → written as: [-4P + Qd = 500] and [2P - Qs = 100]
# In matrix form for P: 6P = 600
P_eq = 600 / 6
Q_eq = 500 - 4 * P_eq
print(f"Equilibrium Price:    P* = ${P_eq:.1f}/tonne")
print(f"Equilibrium Quantity: Q* = {Q_eq:.0f} thousand tonnes")"""),

        md("""\
Plot supply and demand."""),

        code("""\
# A.2 — Plot supply and demand
Q_vals = np.linspace(0, 250, 300)
P_demand = demand_P(Q_vals)
P_supply = supply_P(Q_vals)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(Q_vals, P_demand, "steelblue", lw=2.5, label="Demand: P = (500−Q)/4")
ax.plot(Q_vals, P_supply, "firebrick", lw=2.5, label="Supply: P = (Q+100)/2")
ax.plot(Q_eq, P_eq, "ko", ms=12, zorder=5, label=f"Equilibrium (Q={Q_eq:.0f}, P=${P_eq:.0f})")
ax.axhline(P_eq, color="k", ls="--", alpha=0.4)
ax.axvline(Q_eq, color="k", ls="--", alpha=0.4)
ax.set_xlabel("Quantity (thousand tonnes/yr)")
ax.set_ylabel("Price ($/tonne)")
ax.set_title("Australian Wheat Market: Supply and Demand")
ax.legend()
ax.set_ylim(0, 160)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part B: Surplus — Graphical (~20 min)

**CS** is the triangle above $P^*$ and below the demand curve:
$$CS = \\frac{1}{2} \\times Q^* \\times (P_{max} - P^*) = \\frac{1}{2} \\times 100 \\times (125 - 100) = 1{,}250 \\text{ (\\$000)}$$

**PS** is the triangle below $P^*$ and above the supply curve:
$$PS = \\frac{1}{2} \\times Q^* \\times (P^* - P_{min}) = \\frac{1}{2} \\times 100 \\times (100 - 50) = 2{,}500 \\text{ (\\$000)}$$"""),

        code("""\
# B.1 — Shade surplus areas
Q_vals = np.linspace(0, Q_eq, 300)

fig, ax = plt.subplots(figsize=(8, 5))

# Demand and supply curves
ax.plot(np.linspace(0, 200, 300), demand_P(np.linspace(0, 200, 300)), "steelblue", lw=2.5, label="Demand")
ax.plot(np.linspace(0, 200, 300), supply_P(np.linspace(0, 200, 300)), "firebrick", lw=2.5, label="Supply")

# Shade CS (above P*, below demand curve)
ax.fill_between(Q_vals, demand_P(Q_vals), P_eq, alpha=0.3, color="steelblue", label=f"CS = $1,250k")
# Shade PS (below P*, above supply curve)
ax.fill_between(Q_vals, P_eq, supply_P(Q_vals), alpha=0.3, color="firebrick", label=f"PS = $2,500k")

ax.axhline(P_eq, color="k", ls="--", alpha=0.5)
ax.axvline(Q_eq, color="k", ls="--", alpha=0.5)
ax.plot(Q_eq, P_eq, "ko", ms=10, zorder=5)
ax.set_xlabel("Quantity (thousand tonnes/yr)")
ax.set_ylabel("Price ($/tonne)")
ax.set_title("Consumer and Producer Surplus — Wheat Market")
ax.set_ylim(0, 150)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part C: Surplus via Integration (~20 min)

$$CS = \\int_0^{Q^*} D(Q)\\,dQ - P^* \\cdot Q^*$$

$$PS = P^* \\cdot Q^* - \\int_0^{Q^*} S(Q)\\,dQ$$"""),

        code("""\
# C.1 — CS and PS by numerical integration
from numpy import trapz

Q_fine = np.linspace(0, Q_eq, 10000)

area_under_demand = trapz(demand_P(Q_fine), Q_fine)
area_under_supply = trapz(supply_P(Q_fine), Q_fine)
price_times_qty   = P_eq * Q_eq

CS = area_under_demand - price_times_qty
PS = price_times_qty   - area_under_supply

print(f"Area under demand curve: {area_under_demand:,.1f}")
print(f"Area under supply curve: {area_under_supply:,.1f}")
print(f"P* × Q* = {price_times_qty:,.1f}")
print(f"\\nConsumer Surplus (CS): ${CS:,.1f} thousand")
print(f"Producer Surplus (PS): ${PS:,.1f} thousand")
print(f"Total Surplus:         ${CS + PS:,.1f} thousand")"""),

        md("""\
Analytic check (triangles)."""),

        code("""\
# C.2 — Analytic check (triangles)
CS_analytic = 0.5 * Q_eq * (demand_P(0) - P_eq)
PS_analytic = 0.5 * Q_eq * (P_eq - supply_P(0))
print(f"CS (triangle formula): ${CS_analytic:,.1f}k")
print(f"PS (triangle formula): ${PS_analytic:,.1f}k")
print(f"Numerical matches analytic? CS: {abs(CS - CS_analytic) < 1}, PS: {abs(PS - PS_analytic) < 1}")"""),

        md("""\
✏️ **Group Discussion:**

1. Which group — buyers or sellers — benefits more from this wheat market? What does the ratio PS/CS tell you?
2. What would happen to CS and PS if the government imposed a price floor of $120/tonne?
3. Why is total surplus maximised at the competitive equilibrium?

```
DISCUSSION:
...
```"""),
    ])


def week7_lab_a():
    return notebook([

        md("""\
# Week 7 Presentation Brief — Variation A
## 🍷 Wine Market Surplus: Integration in Agricultural Economics
**SCIE1500 — Semester 2, 2026 | Group 2 (first presentation) — presenting in Week 8**

> Work through all parts during the Week 7 lab. Your **10-minute Week 8 presentation** should cover: equilibrium derivation, graphical surplus, integration method, and a policy scenario."""),

        md("""\
---
## 📋 Scenario

The Australian domestic wine market:

- **Demand:** $Q_d = 800 - 5P$ (thousand litres/yr)
- **Supply:** $Q_s = -200 + 3P$ (thousand litres/yr)

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Find equilibrium and inverse functions | ~20 min |
| B | Compute CS and PS graphically (triangles) | ~20 min |
| C | Verify with integration; policy scenario | ~20 min |"""),

        code(LAB_SETUP + """

# Wine market: Qd = 800 - 5P, Qs = -200 + 3P
# Equilibrium: 800 - 5P = -200 + 3P → 8P = 1000 → P* = 125, Q* = 175
P_star = 125
Q_star = 175

def demand_P(Q):
    'Inverse demand.'
    return (800 - Q) / 5

def supply_P(Q):
    'Inverse supply.'
    return (Q + 200) / 3

print(f"P* = ${P_star}, Q* = {Q_star}k litres")
print(f"Demand intercept: P = {demand_P(0):.0f}")
print(f"Supply intercept: P = {supply_P(0):.0f}")"""),

        md("""\
Run the next cell."""),

        code("""\
        """),

        md("""\
The chart below plots wine supply and demand curves."""),

        code("""\
# Plot wine supply and demand
Q_vals = np.linspace(0, 300, 300)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(Q_vals, demand_P(Q_vals), "purple",    lw=2.5, label="Demand: P=(800−Q)/5")
ax.plot(Q_vals, supply_P(Q_vals), "goldenrod", lw=2.5, label="Supply: P=(Q+200)/3")

Q_shade = np.linspace(0, Q_star, 300)
ax.fill_between(Q_shade, demand_P(Q_shade), P_star, alpha=0.25, color="purple",    label=f"CS")
ax.fill_between(Q_shade, P_star, supply_P(Q_shade), alpha=0.25, color="goldenrod", label=f"PS")

ax.plot(Q_star, P_star, "ko", ms=10, zorder=5, label=f"Eq. (Q={Q_star}, P=${P_star})")
ax.axhline(P_star, color="k", ls="--", alpha=0.4)
ax.axvline(Q_star, color="k", ls="--", alpha=0.4)
ax.set_xlabel("Quantity (000 litres/yr)"); ax.set_ylabel("Price ($/litre)")
ax.set_title("Australian Wine Market"); ax.legend(fontsize=9)
ax.set_ylim(0, 200); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
Triangle formulas."""),

        code("""\
# Triangle formulas
CS = 0.5 * Q_star * (demand_P(0) - P_star)
PS = 0.5 * Q_star * (P_star - supply_P(0))
print(f"CS = ½ × {Q_star} × ({demand_P(0):.0f} − {P_star}) = ${CS:,.1f}k")
print(f"PS = ½ × {Q_star} × ({P_star} − {supply_P(0):.0f}) = ${PS:,.1f}k")
print(f"Total Surplus = ${CS + PS:,.1f}k")"""),

        md("""\
Integration verification."""),

        code("""\
# Integration verification
from numpy import trapz
Q_fine = np.linspace(0, Q_star, 10000)
CS_int = trapz(demand_P(Q_fine), Q_fine) - P_star * Q_star
PS_int = P_star * Q_star - trapz(supply_P(Q_fine), Q_fine)
print(f"CS (integration): ${CS_int:,.1f}k  — matches triangle? {abs(CS_int - CS) < 1}")
print(f"PS (integration): ${PS_int:,.1f}k  — matches triangle? {abs(PS_int - PS) < 1}")"""),

        md("""\
Policy scenario: export price $150/litre."""),

        code("""\
# Policy scenario: export price $150/litre
P_export = 150
Q_domestic = 800 - 5 * P_export   # domestic consumption at P_export
Q_supplied  = -200 + 3 * P_export  # total domestic supply at P_export
Q_exported  = Q_supplied - Q_domestic

print(f"At export price P = ${P_export}:")
print(f"  Domestic Q demanded: {Q_domestic}k litres")
print(f"  Domestic Q supplied: {Q_supplied}k litres")
print(f"  Export volume:       {Q_exported}k litres")

# New CS (at higher price, buyers are worse off)
Q_sh = np.linspace(0, Q_domestic, 5000)
CS_export = trapz(demand_P(Q_sh), Q_sh) - P_export * Q_domestic
PS_export = P_export * Q_supplied - trapz(supply_P(np.linspace(0, Q_supplied, 5000)), np.linspace(0, Q_supplied, 5000))
print(f"\\nNew CS = ${CS_export:,.1f}k  (was ${CS:,.1f}k → change: ${CS_export-CS:+,.1f}k)")
print(f"New PS = ${PS_export:,.1f}k  (was ${PS:,.1f}k → change: ${PS_export-PS:+,.1f}k)")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 8, 10 minutes)

1. **Equilibrium** (~2 min): Solve algebraically; confirm with Python.
2. **Surplus** (~3 min): Draw and shade CS/PS triangles; state values.
3. **Integration** (~3 min): Verify with `trapz`; explain why both methods agree.
4. **Policy** (~2 min): Does the export price help consumers or producers? By how much?"""),
    ])


def week7_lab_b():
    return notebook([

        md("""\
# Week 7 Presentation Brief — Variation B
## 🥑 Avocado Market: Surplus and Export Shock
**SCIE1500 — Semester 2, 2026 | Group 1 (second presentation) — presenting in Week 8**

> Work through all parts during the Week 7 lab. Your **10-minute Week 8 presentation** should cover: equilibrium, CS and PS, export demand shock, and welfare comparison."""),

        md("""\
---
## 📋 Scenario

The Australian avocado market:

- **Demand:** $Q_d = 600 - 4P$ (million avocados/yr)
- **Supply:** $Q_s = -120 + 2P$ (million avocados/yr)

An export deal is struck: new effective demand becomes $Q_d^{\\text{export}} = 720 - 4P$.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Find domestic equilibrium and calculate consumer and producer surplus | ~25 min |
| B | Determine the effect of an export shock on equilibrium and surplus | ~25 min |
| C | Compare welfare outcomes before and after the export deal | ~10 min |"""),

        code(LAB_SETUP + """

# Avocado domestic market
def demand_P(Q):
    'Domestic inverse demand.'
    return (600 - Q) / 4

def supply_P(Q):
    'Inverse supply.'
    return (Q + 120) / 2

def demand_export_P(Q):
    'Export inverse demand: Qd_export = 720 - 4P.'
    return (720 - Q) / 4

# Domestic equilibrium: 600 - 4P = -120 + 2P → 6P = 720 → P*=120, Q*=120
P_dom = 120
Q_dom = 120
print(f"Domestic equilibrium: P*=${P_dom}, Q*={Q_dom}M avocados")"""),

        md("""\
Domestic CS and PS."""),

        code("""\
# Domestic CS and PS
CS_dom = 0.5 * Q_dom * (demand_P(0) - P_dom)
PS_dom = 0.5 * Q_dom * (P_dom - supply_P(0))
print(f"Domestic CS: ${CS_dom:,.1f}M")
print(f"Domestic PS: ${PS_dom:,.1f}M")
print(f"Total Surplus: ${CS_dom + PS_dom:,.1f}M")"""),

        md("""\
Export equilibrium: 720 - 4P = -120 + 2P → 6P = 840 → P*=140."""),

        code("""\
# Export equilibrium: 720 - 4P = -120 + 2P → 6P = 840 → P*=140, Q*=160
P_exp = 140
Q_exp = 160
print(f"Export equilibrium: P*=${P_exp}, Q*={Q_exp}M avocados")

CS_exp = 0.5 * (720 / 4 - P_exp) * Q_exp   # demand_export_P(0) = 180
PS_exp = 0.5 * Q_exp * (P_exp - supply_P(0))
print(f"\\nExport CS: ${CS_exp:,.1f}M  (change: ${CS_exp - CS_dom:+,.1f}M)")
print(f"Export PS: ${PS_exp:,.1f}M  (change: ${PS_exp - PS_dom:+,.1f}M)")
print(f"Net welfare change: ${(CS_exp + PS_exp) - (CS_dom + PS_dom):+,.1f}M")"""),

        md("""\
Run the next cell."""),

        code("""\
        """),

        md("""\
The chart below shows the domestic vs export equilibrium."""),

        code("""\
# Plot: domestic vs export equilibrium
Q_vals = np.linspace(0, 250, 300)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

for ax, (P_star, Q_star, Pinv_d, label, cs, ps) in [
    (ax1, (P_dom, Q_dom, demand_P,        "Domestic",  CS_dom, PS_dom)),
    (ax2, (P_exp, Q_exp, demand_export_P, "With Export", CS_exp, PS_exp))]:
    Q_sh = np.linspace(0, Q_star, 300)
    ax.plot(Q_vals, Pinv_d(Q_vals), "seagreen", lw=2.5, label="Demand")
    ax.plot(Q_vals, supply_P(Q_vals), "coral",  lw=2.5, label="Supply")
    ax.fill_between(Q_sh, Pinv_d(Q_sh), P_star, alpha=0.25, color="seagreen", label=f"CS=${cs:.0f}M")
    ax.fill_between(Q_sh, P_star, supply_P(Q_sh), alpha=0.25, color="coral",  label=f"PS=${ps:.0f}M")
    ax.plot(Q_star, P_star, "ko", ms=9, zorder=5)
    ax.set_title(f"Avocado Market — {label}")
    ax.set_xlabel("Quantity (M avocados/yr)"); ax.set_ylabel("Price ($/avocado)")
    ax.set_ylim(0, 200); ax.legend(fontsize=8); ax.grid(alpha=0.3)

plt.tight_layout(); plt.show()"""),

        md("""\
✏️ **Welfare Interpretation:**

1. Who wins and who loses from the export deal? Quantify using your results above.
2. If consumers can lobby for a price ceiling of $120, how much production would occur?
3. Is total welfare (CS + PS) higher or lower with exports? Explain the trade-off.

```
DISCUSSION:
...
```

---
## ✅ Presentation Checklist (Week 8, 10 minutes)

1. **Domestic market** (~2 min): Present equilibrium, CS and PS values, and interpret them.
2. **Export shock** (~3 min): Show the new equilibrium and use integration to verify surplus.
3. **Welfare comparison** (~3 min): Present a table comparing CS, PS, and total welfare before and after.
4. **Policy** (~2 min): Should government support or restrict the export deal? Justify with numbers."""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 8
# ─────────────────────────────────────────────────────────────────────────────

def week8_student():
    return notebook([

        md("""\
# Week 8 Lab — Predator-Prey Dynamics and Differential Equations
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Work in your groups. Run all code cells in order, fill in the written prompts.

---
**This week:** We model two interacting populations using a system of ordinary differential equations (ODEs) — the Lotka-Volterra predator-prey model."""),

        md("""\
---
## 📋 Scientific Scenario

Feral cats threaten numbats in the Western Australian wheatbelt. The population dynamics can be modelled as:

$$\\frac{dN}{dt} = 0.4N - 0.002NC$$

$$\\frac{dC}{dt} = -0.3C + 0.001NC$$

where $N$ is the numbat population and $C$ is the feral cat population.

- The $+0.4N$ term: numbats grow at 40%/yr in the absence of cats.
- The $-0.002NC$ term: cats reduce numbat growth (predation rate).
- The $-0.3C$ term: cats decline at 30%/yr without numbats.
- The $+0.001NC$ term: cat population grows from numbat predation.

---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Find equilibria and derive the nullclines algebraically | ~20 min |
| B | Plot the phase plane and interpret the vector field | ~20 min |
| C | Simulate and plot population trajectories over time | ~20 min |

By the end you should be able to: find equilibria of ODE systems algebraically; plot phase planes and nullclines; and simulate predator-prey dynamics numerically."""),

        code(SETUP_IMPORTS + """

# Lotka-Volterra parameters
r_N = 0.4    # numbat growth rate
a   = 0.002  # predation rate (cats kill numbats)
d   = 0.3    # cat death rate
b   = 0.001  # cat growth from predation

# Equilibrium: set dN/dt = 0 AND dC/dt = 0
# dN/dt = 0: N(0.4 - 0.002C) = 0 → C* = 0.4/0.002 = 200
# dC/dt = 0: C(-0.3 + 0.001N) = 0 → N* = 0.3/0.001 = 300
C_star = r_N / a
N_star = d   / b
print(f"Coexistence equilibrium: N* = {N_star:.0f} numbats, C* = {C_star:.0f} cats")
print(f"Trivial equilibrium:     N = 0, C = 0")"""),

        md("""\
---
## Part A: Equilibrium and Nullclines (~20 min)

The **nullclines** are curves where one population's rate of change is zero:

- **Numbat nullcline** ($dN/dt = 0$): $C = 200$ (horizontal line)
- **Cat nullcline** ($dC/dt = 0$): $N = 300$ (vertical line)

✏️ **A.1** What happens to the numbat population when $C > 200$? When $C < 200$?

✏️ **A.2** What happens to the cat population when $N > 300$? When $N < 300$?

```
ANSWERS:
...
```"""),

        code("""\
# A.1 — Check rates at a point to understand direction
# Start: N=400 numbats, C=100 cats
N, C = 400, 100
dN = r_N*N - a*N*C
dC = -d*C  + b*N*C
print(f"At N={N}, C={C}:")
print(f"  dN/dt = {dN:.1f}  ({'increasing' if dN > 0 else 'decreasing'})")
print(f"  dC/dt = {dC:.1f}  ({'increasing' if dC > 0 else 'decreasing'})")

# Try another point
N, C = 200, 300
dN = r_N*N - a*N*C
dC = -d*C  + b*N*C
print(f"\\nAt N={N}, C={C}:")
print(f"  dN/dt = {dN:.1f}  ({'increasing' if dN > 0 else 'decreasing'})")
print(f"  dC/dt = {dC:.1f}  ({'increasing' if dC > 0 else 'decreasing'})")"""),

        md("""\
---
## Part B: Phase Plane (~20 min)"""),

        code("""\
# B.1 — Phase plane with quiver (vector field)
N_grid = np.linspace(0, 600, 20)
C_grid = np.linspace(0, 400, 20)
NN, CC = np.meshgrid(N_grid, C_grid)

dN_dt = r_N*NN - a*NN*CC
dC_dt = -d*CC  + b*NN*CC

# Normalise arrows for display
magnitude = np.sqrt(dN_dt**2 + dC_dt**2) + 1e-6
dN_norm = dN_dt / magnitude
dC_norm = dC_dt / magnitude

fig, ax = plt.subplots(figsize=(8, 6))
ax.quiver(NN, CC, dN_norm, dC_norm, magnitude, cmap="RdYlGn", alpha=0.7)

# Nullclines
ax.axvline(N_star, color="steelblue", lw=2, ls="--", label=f"Cat nullcline: N={N_star:.0f}")
ax.axhline(C_star, color="firebrick", lw=2, ls="--", label=f"Numbat nullcline: C={C_star:.0f}")
ax.plot(N_star, C_star, "ko", ms=14, zorder=5, label=f"Coexistence eq. ({N_star:.0f},{C_star:.0f})")

ax.set_xlabel("Numbat Population N")
ax.set_ylabel("Feral Cat Population C")
ax.set_title("Feral Cat–Numbat Phase Plane")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
---
## Part C: Population Trajectories (~20 min)"""),

        code("""\
# C.1 — Simulate using Euler's method
dt   = 0.01   # time step (years)
T    = 30     # total time (years)
steps = int(T / dt)

N0, C0 = 400, 80   # initial populations

N_traj = np.zeros(steps + 1)
C_traj = np.zeros(steps + 1)
t_traj = np.zeros(steps + 1)

N_traj[0], C_traj[0] = N0, C0

for i in range(steps):
    dN = (r_N * N_traj[i] - a * N_traj[i] * C_traj[i]) * dt
    dC = (-d  * C_traj[i] + b * N_traj[i] * C_traj[i]) * dt
    N_traj[i+1] = N_traj[i] + dN
    C_traj[i+1] = C_traj[i] + dC
    t_traj[i+1] = t_traj[i] + dt

print(f"Initial:  N={N0}, C={C0}")
print(f"Year 10:  N={N_traj[int(10/dt)]:.0f}, C={C_traj[int(10/dt)]:.0f}")
print(f"Year 20:  N={N_traj[int(20/dt)]:.0f}, C={C_traj[int(20/dt)]:.0f}")"""),

        md("""\
Plot time series."""),

        code("""\
# C.2 — Plot time series
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t_traj, N_traj, "steelblue", lw=2, label="Numbats N(t)")
ax1.axhline(N_star, color="steelblue", ls="--", alpha=0.4, label=f"Equilibrium N*={N_star:.0f}")
ax1.set_ylabel("Numbat Population")
ax1.legend(fontsize=9); ax1.grid(alpha=0.3)

ax2.plot(t_traj, C_traj, "firebrick", lw=2, label="Feral Cats C(t)")
ax2.axhline(C_star, color="firebrick", ls="--", alpha=0.4, label=f"Equilibrium C*={C_star:.0f}")
ax2.set_xlabel("Years"); ax2.set_ylabel("Cat Population")
ax2.legend(fontsize=9); ax2.grid(alpha=0.3)

plt.suptitle("Numbat–Feral Cat Population Dynamics (N₀=400, C₀=80)")
plt.tight_layout()
plt.show()"""),

        md("""\
Management scenario: cat culling + numbat translocation."""),

        code("""\
# C.3 — Management scenario: cat culling + numbat translocation
print("Management scenario: remove 50 cats/year, add 20 numbats/year")
N_mgmt = np.zeros(steps + 1)
C_mgmt = np.zeros(steps + 1)
N_mgmt[0], C_mgmt[0] = 200, 250   # low numbats, high cats (stressed state)

for i in range(steps):
    dN = (r_N * N_mgmt[i] - a * N_mgmt[i] * C_mgmt[i] + 20) * dt
    dC = (-d  * C_mgmt[i] + b * N_mgmt[i] * C_mgmt[i] - 50) * dt
    N_mgmt[i+1] = max(0, N_mgmt[i] + dN)
    C_mgmt[i+1] = max(0, C_mgmt[i] + dC)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t_traj, N_mgmt, "steelblue", lw=2, label="Numbats (managed)")
ax.plot(t_traj, C_mgmt, "firebrick", lw=2, label="Feral Cats (managed)")
ax.axhline(N_star, color="steelblue", ls=":", alpha=0.5)
ax.axhline(C_star, color="firebrick", ls=":", alpha=0.5)
ax.set_xlabel("Years"); ax.set_ylabel("Population")
ax.set_title("Managed Scenario: Culling 50 Cats/yr + 20 Numbat Translocations/yr")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("""\
✏️ **Group Discussion:**

1. Do the populations oscillate or converge to equilibrium? How does your phase plane explain this?
2. Under the management scenario, does the numbat population recover? What is the long-run outcome?
3. What are the limitations of the Lotka-Volterra model for real conservation planning?

```
DISCUSSION:
...
```"""),
    ])


def week8_lab_a():
    return notebook([

        md("""\
# Week 8 Presentation Brief — Variation A
## 🐱 Feral Cats and Numbats: Phase Plane Analysis
**SCIE1500 — Semester 2, 2026 | Group 2 (first presentation) — presenting in Week 9**

> Work through all parts during the Week 8 lab. Your **10-minute Week 9 presentation** should cover: the ODE model, equilibrium analysis, phase plane interpretation, and conservation implications."""),

        md("""\
---
## 📋 Scenario

Same Lotka-Volterra model as the main lab:

$$\\frac{dN}{dt} = 0.4N - 0.002NC, \\qquad \\frac{dC}{dt} = -0.3C + 0.001NC$$

Your focus: **deeper phase plane analysis** using `scipy.integrate.odeint` and multiple trajectories from different starting conditions.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Find equilibria and assess local stability | ~20 min |
| B | Plot a phase portrait with multiple trajectories using odeint | ~25 min |
| C | Identify conservation thresholds for population recovery | ~15 min |"""),

        code(LAB_SETUP + """
from scipy.integrate import odeint

r_N = 0.4; a = 0.002; d = 0.3; b = 0.001
N_star = d / b   # 300
C_star = r_N / a  # 200

print(f"Equilibrium: N*={N_star:.0f}, C*={C_star:.0f}")

def lotka_volterra(state, t):
    N, C = state
    dN = r_N*N - a*N*C
    dC = -d*C  + b*N*C
    return [dN, dC]"""),

        md("""\
Multiple trajectories from different initial conditions."""),

        code("""\
# Multiple trajectories from different initial conditions
t_span = np.linspace(0, 40, 2000)
initial_conditions = [
    (400, 80),   # high numbats, low cats
    (200, 250),  # low numbats, high cats
    (350, 150),  # moderate both
    (500, 200),  # very high numbats
]

colors = ["steelblue", "firebrick", "seagreen", "purple"]
labels = ["N₀=400, C₀=80", "N₀=200, C₀=250", "N₀=350, C₀=150", "N₀=500, C₀=200"]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: phase plane
N_grid = np.linspace(0, 700, 18)
C_grid = np.linspace(0, 350, 18)
NN, CC = np.meshgrid(N_grid, C_grid)
dN_dt = r_N*NN - a*NN*CC
dC_dt = -d*CC  + b*NN*CC
mag = np.sqrt(dN_dt**2 + dC_dt**2) + 1e-6
axes[0].quiver(NN, CC, dN_dt/mag, dC_dt/mag, mag, cmap="Greys", alpha=0.5)

for ic, col, lbl in zip(initial_conditions, colors, labels):
    sol = odeint(lotka_volterra, ic, t_span)
    axes[0].plot(sol[:, 0], sol[:, 1], col, lw=2, label=lbl)
    axes[0].plot(ic[0], ic[1], "o", color=col, ms=8)

axes[0].axvline(N_star, color="k", ls="--", alpha=0.5, label=f"N*={N_star:.0f}")
axes[0].axhline(C_star, color="k", ls=":",  alpha=0.5, label=f"C*={C_star:.0f}")
axes[0].plot(N_star, C_star, "k*", ms=16, zorder=6, label="Equilibrium")
axes[0].set_xlabel("Numbats N"); axes[0].set_ylabel("Cats C")
axes[0].set_title("Phase Portrait"); axes[0].legend(fontsize=7)
axes[0].set_xlim(0, 700); axes[0].set_ylim(0, 350)

# Right: time series for first IC
sol0 = odeint(lotka_volterra, initial_conditions[0], t_span)
axes[1].plot(t_span, sol0[:, 0], "steelblue", lw=2, label="Numbats")
axes[1].plot(t_span, sol0[:, 1], "firebrick", lw=2, label="Feral Cats")
axes[1].axhline(N_star, color="steelblue", ls="--", alpha=0.4)
axes[1].axhline(C_star, color="firebrick", ls="--", alpha=0.4)
axes[1].set_xlabel("Years"); axes[1].set_ylabel("Population")
axes[1].set_title("Time Series (N₀=400, C₀=80)"); axes[1].legend()

plt.tight_layout(); plt.show()"""),

        md("""\
Conservation threshold: if N drops below what level do cats."""),

        code("""\
# Conservation threshold: if N drops below what level do cats go extinct?
# Cats go extinct if dC/dt < 0 always → N < d/b = 300 at all times
# Find minimum N across all trajectories
for ic, lbl in zip(initial_conditions, labels):
    sol = odeint(lotka_volterra, ic, t_span)
    N_min = sol[:, 0].min()
    C_max = sol[:, 1].max()
    print(f"{lbl}: N_min={N_min:.0f}, C_max={C_max:.0f}")"""),

        md("""\
---
## ✅ Presentation Checklist (Week 9, 10 minutes)

1. **Model** (~2 min): State the ODEs; explain each parameter ecologically.
2. **Equilibrium** (~2 min): Derive $N^* = 300$, $C^* = 200$; interpret the nullclines.
3. **Phase portrait** (~4 min): Show the plot; trace one trajectory; explain the closed-orbit pattern.
4. **Conservation** (~2 min): What starting conditions lead to cat dominance vs. numbat recovery?"""),
    ])


def week8_lab_b():
    return notebook([

        md("""\
# Week 8 Presentation Brief — Variation B
## 🦘 Dingo-Kangaroo Dynamics: Predator-Prey Modelling
**SCIE1500 — Semester 2, 2026 | Group 1 (second presentation) — presenting in Week 9**

> Work through all parts during the Week 8 lab. Your **10-minute Week 9 presentation** should cover: the ODE model, equilibria, phase plane, and management implications for dingo control."""),

        md("""\
---
## 📋 Scenario

In the Kimberley, dingoes prey on kangaroos. Population dynamics:

$$\\frac{dK}{dt} = 0.5K - 0.0015KD$$

$$\\frac{dD}{dt} = -0.25D + 0.0008KD$$

where $K$ = kangaroo population and $D$ = dingo population.

---
## 🎯 Your Task

| Part | Topic | Time |
|------|-------|------|
| A | Derive and interpret the coexistence equilibrium | ~15 min |
| B | Plot the phase plane and simulate trajectories using odeint | ~30 min |
| C | Simulate a dingo culling scenario and evaluate long-run outcomes | ~15 min |"""),

        code(LAB_SETUP + """
from scipy.integrate import odeint

r_K = 0.5;  alpha = 0.0015   # kangaroo growth, predation
d_D = 0.25; beta  = 0.0008   # dingo death, conversion efficiency

# Coexistence equilibrium
K_star = d_D / beta    # = 0.25/0.0008 = 312.5
D_star = r_K / alpha   # = 0.5/0.0015 ≈ 333.3

print(f"Coexistence equilibrium:")
print(f"  K* = {K_star:.1f} kangaroos")
print(f"  D* = {D_star:.1f} dingoes")

def dingo_kangaroo(state, t):
    K, D = state
    dK = r_K*K  - alpha*K*D
    dD = -d_D*D + beta*K*D
    return [dK, dD]"""),

        md("""\
Phase plane with odeint trajectories."""),

        code("""\
# Phase plane with odeint trajectories
t_span = np.linspace(0, 50, 3000)
ICs = [(500, 100), (300, 400), (600, 300)]
colors = ["steelblue", "firebrick", "seagreen"]
labels = ["K₀=500,D₀=100", "K₀=300,D₀=400", "K₀=600,D₀=300"]

K_grid = np.linspace(0, 900, 18)
D_grid = np.linspace(0, 600, 18)
KK, DD = np.meshgrid(K_grid, D_grid)
dK_grid = r_K*KK - alpha*KK*DD
dD_grid = -d_D*DD + beta*KK*DD
mag = np.sqrt(dK_grid**2 + dD_grid**2) + 1e-6

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.quiver(KK, DD, dK_grid/mag, dD_grid/mag, mag, cmap="Greys", alpha=0.5)
for ic, col, lbl in zip(ICs, colors, labels):
    sol = odeint(dingo_kangaroo, ic, t_span)
    ax1.plot(sol[:, 0], sol[:, 1], col, lw=2, label=lbl)
    ax1.plot(ic[0], ic[1], "o", color=col, ms=8)
ax1.axvline(K_star, color="k", ls="--", alpha=0.5, label=f"K*={K_star:.0f}")
ax1.axhline(D_star, color="k", ls=":",  alpha=0.5, label=f"D*={D_star:.0f}")
ax1.plot(K_star, D_star, "k*", ms=14, zorder=5, label="Equilibrium")
ax1.set_xlabel("Kangaroos K"); ax1.set_ylabel("Dingoes D")
ax1.set_title("Dingo–Kangaroo Phase Plane"); ax1.legend(fontsize=7)

sol0 = odeint(dingo_kangaroo, ICs[0], t_span)
ax2.plot(t_span, sol0[:, 0], "steelblue", lw=2, label="Kangaroos")
ax2.plot(t_span, sol0[:, 1], "firebrick", lw=2, label="Dingoes")
ax2.axhline(K_star, color="steelblue", ls="--", alpha=0.4)
ax2.axhline(D_star, color="firebrick", ls="--", alpha=0.4)
ax2.set_xlabel("Years"); ax2.set_ylabel("Population")
ax2.set_title("Time Series (K₀=500, D₀=100)"); ax2.legend()

plt.tight_layout(); plt.show()"""),

        md("""\
Dingo culling scenario: remove 30 dingoes/year."""),

        code("""\
# Dingo culling scenario: remove 30 dingoes/year
cull_rate = 30

N_steps = 3000
dt = 50 / N_steps
K_c = np.zeros(N_steps + 1); D_c = np.zeros(N_steps + 1); t_c = np.zeros(N_steps + 1)
K_c[0], D_c[0] = 400, 200

for i in range(N_steps):
    dK = r_K*K_c[i] - alpha*K_c[i]*D_c[i]
    dD = -d_D*D_c[i] + beta*K_c[i]*D_c[i] - cull_rate
    K_c[i+1] = max(0, K_c[i] + dK * dt)
    D_c[i+1] = max(0, D_c[i] + dD * dt)
    t_c[i+1] = t_c[i] + dt

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t_c, K_c, "steelblue", lw=2, label="Kangaroos (culled)")
ax.plot(t_c, D_c, "firebrick", lw=2, label="Dingoes (culled)")
ax.axhline(K_star, color="steelblue", ls="--", alpha=0.4)
ax.axhline(D_star, color="firebrick", ls="--", alpha=0.4)
ax.set_xlabel("Years"); ax.set_ylabel("Population")
ax.set_title(f"Dingo Culling: Remove {cull_rate} dingoes/yr")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()

print(f"Year 50: K = {K_c[-1]:.0f}, D = {D_c[-1]:.0f}")
print(f"Without culling eq: K* = {K_star:.0f}, D* = {D_star:.0f}")"""),

        md("""\
✏️ **Management Discussion:**

1. Does culling 30 dingoes/year lead to dingo extinction or a new equilibrium? What does this imply for kangaroo population management?
2. What cull rate would be needed to reduce dingo population below 100?
3. What are the ecological risks of reducing dingo numbers in the Kimberley?

```
DISCUSSION:
...
```

---
## ✅ Presentation Checklist (Week 9, 10 minutes)

1. **ODEs** (~2 min): State and interpret each term in the dingo-kangaroo model.
2. **Equilibrium** (~2 min): Derive $K^*$, $D^*$; compare to feral cat model parameters.
3. **Phase plane** (~4 min): Show plots; trace one orbit; explain oscillation pattern.
4. **Culling** (~2 min): Is culling effective? What are the long-run implications?"""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 9
# ─────────────────────────────────────────────────────────────────────────────

def week9_student():
    return notebook([

        md("""\
# Week 9 Lab — Probability, Bayes' Theorem, and Medical Testing
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Work in your groups. Run all code cells in order, fill in the written prompts.

---
**This week:** We use probability and Bayes' theorem to evaluate the real-world performance of diagnostic tests — a critical skill in public health and clinical science."""),

        md("""\
---
## 📋 Scientific Scenario

During a COVID-19 wave, health authorities use a rapid antigen test with the following properties:

- **Sensitivity** (true positive rate): 85% — if you have COVID, the test detects it 85% of the time.
- **Specificity** (true negative rate): 95% — if you don't have COVID, the test correctly gives a negative 95% of the time.
- **Community prevalence**: 2% of the population currently has COVID.

**Question:** If a randomly chosen person tests positive, what is the probability they actually have COVID?

---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Bayes' theorem: algebra and intuition | ~25 min |
| B | Python calculation and verification | ~20 min |
| C | Sensitivity analysis: how prevalence changes everything | ~15 min |

By the end you should be able to: apply Bayes' theorem to diagnostic testing; interpret sensitivity, specificity, and positive predictive value (PPV); and explain why prevalence drives PPV."""),

        code(SETUP_IMPORTS + """

# Test parameters
sensitivity  = 0.85   # P(T+ | Disease)
specificity  = 0.95   # P(T- | No Disease)
prevalence   = 0.02   # P(Disease)

false_pos_rate = 1 - specificity   # P(T+ | No Disease)

print("Test characteristics:")
print(f"  Sensitivity:       {sensitivity:.0%}")
print(f"  Specificity:       {specificity:.0%}")
print(f"  False positive:    {false_pos_rate:.0%}")
print(f"  Prevalence:        {prevalence:.0%}")"""),

        md("""\
---
## Part A: Bayes' Theorem (~25 min)

We want $P(D \\mid T^+)$ — the probability of disease given a positive test (the **Positive Predictive Value**, PPV).

**Step 1** — Law of Total Probability for $P(T^+)$:
$$P(T^+) = P(T^+ \\mid D) \\cdot P(D) + P(T^+ \\mid \\bar{D}) \\cdot P(\\bar{D})$$
$$= 0.85 \\times 0.02 + 0.05 \\times 0.98 = 0.017 + 0.049 = 0.066$$

**Step 2** — Bayes' theorem:
$$P(D \\mid T^+) = \\frac{P(T^+ \\mid D) \\cdot P(D)}{P(T^+)} = \\frac{0.017}{0.066} \\approx 0.257$$

✏️ **A.1** In plain English: if 10,000 people are tested, how many true positives and false positives do you expect? Fill in the table:

| Group | Count | Test result |
|-------|-------|-------------|
| Have COVID (2% of 10,000) | 200 | T+ : ?, T- : ? |
| No COVID (98% of 10,000) | 9,800 | T+ : ?, T- : ? |
| **Total T+** | ? | |

```
ANSWERS:
...
```"""),

        code("""\
# A.1 — Verify Bayes' theorem
P_D    = prevalence
P_Dbar = 1 - P_D

# Joint probabilities
P_Tplus_and_D    = sensitivity * P_D
P_Tplus_and_Dbar = false_pos_rate * P_Dbar

P_Tplus = P_Tplus_and_D + P_Tplus_and_Dbar

PPV = P_Tplus_and_D / P_Tplus

print("Calculation:")
print(f"  P(T+ ∩ D)    = {sensitivity}×{P_D}   = {P_Tplus_and_D:.4f}")
print(f"  P(T+ ∩ D̄)   = {false_pos_rate}×{P_Dbar:.2f} = {P_Tplus_and_Dbar:.4f}")
print(f"  P(T+)        = {P_Tplus:.4f}")
print(f"  PPV = P(D|T+) = {PPV:.4f} ≈ {PPV:.1%}")
print(f"\\n→ Only {PPV:.1%} of positive tests are truly positive!")"""),

        md("""\
The 10,000 person table."""),

        code("""\
# A.2 — The 10,000 person table
N = 10000
n_D    = N * P_D
n_Dbar = N * P_Dbar

TP = sensitivity     * n_D       # true positives
FN = (1-sensitivity) * n_D       # false negatives
FP = false_pos_rate  * n_Dbar    # false positives
TN = specificity     * n_Dbar    # true negatives

print("Confusion matrix (10,000 people):")
print(f"{'':20s} {'T+':>8} {'T-':>8} {'Total':>8}")
print(f"{'Have COVID':20s} {TP:>8.0f} {FN:>8.0f} {n_D:>8.0f}")
print(f"{'No COVID':20s} {FP:>8.0f} {TN:>8.0f} {n_Dbar:>8.0f}")
print(f"{'Total':20s} {TP+FP:>8.0f} {FN+TN:>8.0f} {N:>8.0f}")
print(f"\\nPPV = TP / (TP+FP) = {TP:.0f} / {TP+FP:.0f} = {TP/(TP+FP):.1%}")"""),

        md("""\
---
## Part B: Python Verification and NPV (~20 min)"""),

        code("""\
# B.1 — Negative Predictive Value (NPV): P(no disease | T-)
P_Tminus = 1 - P_Tplus
P_D_given_Tminus = ((1 - sensitivity) * P_D) / P_Tminus
NPV = 1 - P_D_given_Tminus

print(f"P(T-)   = {P_Tminus:.4f}")
print(f"P(D|T-) = {P_D_given_Tminus:.4f}  (prob. you have COVID despite negative test)")
print(f"NPV     = {NPV:.4f} = {NPV:.2%}  (prob. truly disease-free given negative test)")"""),

        md("""\
---
## Part C: Sensitivity Analysis (~15 min)

How does PPV change as community prevalence changes?"""),

        code("""\
# C.1 — PPV vs prevalence curve
prev_vals = np.linspace(0.001, 0.50, 500)

def bayes_PPV(prev, sens=sensitivity, spec=specificity):
    'Positive Predictive Value for given prevalence.'
    fpr = 1 - spec
    P_pos = sens * prev + fpr * (1 - prev)
    return sens * prev / P_pos

ppv_vals = bayes_PPV(prev_vals)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(prev_vals * 100, ppv_vals * 100, "steelblue", lw=2.5)
ax.axvline(prevalence * 100, color="red", ls="--", label=f"Current prevalence ({prevalence:.0%})")
ax.axhline(PPV * 100, color="red", ls=":", alpha=0.7, label=f"Current PPV ({PPV:.1%})")
ax.fill_between(prev_vals * 100, ppv_vals * 100, alpha=0.15, color="steelblue")
ax.set_xlabel("Community Prevalence (%)")
ax.set_ylabel("Positive Predictive Value (%)")
ax.set_title(f"PPV vs Prevalence (Sensitivity={sensitivity:.0%}, Specificity={specificity:.0%})")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"PPV at 2% prevalence:  {bayes_PPV(0.02):.1%}")
print(f"PPV at 10% prevalence: {bayes_PPV(0.10):.1%}")
print(f"PPV at 30% prevalence: {bayes_PPV(0.30):.1%}")"""),

        md("""\
✏️ **Group Discussion:**

1. Why is the PPV only ~26% even though the test is 85% sensitive? Where do the false positives come from?
2. At what prevalence does the PPV reach 50%? Use your plot to estimate, then verify with Python.
3. Should health authorities use this test for population screening at 2% prevalence? What are the consequences of a false positive for the patient?

```
DISCUSSION:
...
```"""),

        md("""\
---
## ✅ Submission Exercise — Batch 3 (due Tuesday 29 September, 11:59 pm)

**Submit via LMS. Covers Weeks 7–9 (definite integrals, ODEs, probability).**

Work individually. Show all working. Write Python code where indicated.

---
### Q1 — Consumer and Producer Surplus (Week 7)

A freshwater prawn market in the Ord River region has:
- Demand: $Q_d = 400 - 2P$ (kg/week)
- Supply: $Q_s = -60 + 3P$ (kg/week)

**(a)** Find the equilibrium price $P^*$ and quantity $Q^*$ algebraically.

**(b)** Derive the inverse demand and inverse supply functions.

**(c)** Calculate CS and PS using the triangle formulas. Show all working.

**(d)** Write Python code to verify CS and PS using numerical integration (`numpy.trapz`).

```python
# Q1d — verify with integration
import numpy as np

def demand_P(Q): ...
def supply_P(Q): ...

# YOUR CODE HERE
```

---
### Q2 — Predator-Prey Dynamics (Week 8)

A quoll-rat system in the Pilbara:

$$\\frac{dR}{dt} = 0.6R - 0.003RQ, \\qquad \\frac{dQ}{dt} = -0.2Q + 0.001RQ$$

where $R$ = rat population, $Q$ = quoll population.

**(a)** Find the coexistence equilibrium $(R^*, Q^*)$. Show your algebra.

**(b)** Identify the rat nullcline and quoll nullcline. What does each represent biologically?

**(c)** Write Python code to simulate the system for 30 years starting from $R_0 = 500$, $Q_0 = 80$ using Euler's method (dt = 0.01). Plot both populations over time.

```python
# Q2c — Euler method simulation
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Parameters
r_R = 0.6; a = 0.003; d_Q = 0.2; b = 0.001

# YOUR CODE HERE
```

**(d)** Interpret: do the populations oscillate or converge? Is the equilibrium reached?

---
### Q3 — Bayes' Theorem (Week 9)

A breast cancer screening test has sensitivity 90% and specificity 92%. The background prevalence of breast cancer in the 50–60 age group is 1.5%.

**(a)** Calculate $P(T^+)$ — the probability a randomly selected person tests positive.

**(b)** Calculate the PPV using Bayes' theorem. Show each step.

**(c)** Write Python code to plot PPV vs prevalence for prevalence ranging from 0.1% to 20%. Annotate the 1.5% prevalence point.

```python
# Q3c — PPV vs prevalence
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

sensitivity = 0.90
specificity = 0.92

# YOUR CODE HERE
```

**(d)** At what prevalence would PPV reach 50%? Solve algebraically or numerically."""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 10
# ─────────────────────────────────────────────────────────────────────────────

def week10_student():
    return notebook([

        md("""\
# Week 10 Lab — Mock Exam Workshop
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Mock exam simulation — work **individually** for 40 minutes, then debrief as a group.

---
**Today:** Four exam-style questions drawn from the full semester. This session is low-stakes practice, not assessed."""),

        md("""\
---
## 📋 Instructions

- Work individually without notes for the first **40 minutes**.
- Use Python only to check arithmetic — write your reasoning first.
- After 40 minutes, compare answers with your group and discuss differences.
- The tutor will lead a full-class debrief at the end.

**Permitted:** Calculators, Python. **Not permitted (for the solo phase):** textbooks, asking others.

---
## ⏱️ Question Overview

| Q | Topic | Marks | Approx. time |
|---|-------|-------|--------------|
| 1 | Hypothesis testing | 25 | ~15 min |
| 2 | Optimisation (differentiation) | 25 | ~10 min |
| 3 | Integration (area/energy) | 25 | ~10 min |
| 4 | ODE (first-order, separable) | 25 | ~5 min |"""),

        code(SETUP_IMPORTS),

        md("""\
---
## Question 1 — Hypothesis Testing (25 marks)

A pharmaceutical company claims a new painkiller reduces pain scores by **at least 30%** on average. In a clinical trial:
- Sample size: $n = 50$ patients
- Sample mean reduction: $\\bar{x} = 28\\%$
- Sample standard deviation: $s = 8\\%$

Test the company's claim at the **5% significance level** using a one-tailed $t$-test.

**(a)** State $H_0$ and $H_1$. [4 marks]

**(b)** Calculate the test statistic $t = \\dfrac{\\bar{x} - \\mu_0}{s/\\sqrt{n}}$. [6 marks]

**(c)** Find the critical value for a one-tailed test with $\\alpha = 0.05$, $df = 49$. [4 marks]

**(d)** State your conclusion in plain language — is the company's claim supported? [4 marks]

**(e)** Write Python code to compute the $t$-statistic and $p$-value. [7 marks]

```
WORKING:
...
```"""),

        code("""\
# Q1e — t-test
from scipy import stats

n     = 50
x_bar = 28    # %
s     = 8     # %
mu_0  = 30    # % (null hypothesis value)

t_stat = (x_bar - mu_0) / (s / np.sqrt(n))
df     = n - 1

# One-tailed p-value (testing H1: mu < 30)
p_val = stats.t.cdf(t_stat, df)   # lower tail

print(f"t-statistic: {t_stat:.4f}")
print(f"Degrees of freedom: {df}")
print(f"p-value (one-tailed): {p_val:.4f}")
print(f"Critical value (α=0.05, one-tailed): {stats.t.ppf(0.05, df):.4f}")
print(f"\\nConclusion: {'Reject H0' if p_val < 0.05 else 'Fail to reject H0'}")"""),

        md("""\
---
## Question 2 — Optimisation (25 marks)

A dairy cooperative models daily cost (dollars) as a function of output $x$ (thousand litres):

$$C(x) = 2x^2 - 80x + 1{,}200$$

Milk sells for $\\$1.20$ per litre ($\\$1{,}200$ per thousand litres). The cooperative operates for $5 \\leq x \\leq 25$.

**(a)** Write the profit function $\\Pi(x) = R(x) - C(x)$. [4 marks]

**(b)** Find $\\Pi'(x)$ and set it to zero to find the profit-maximising output $x^*$. [8 marks]

**(c)** Verify $x^*$ is a maximum using the second derivative test. [4 marks]

**(d)** Calculate maximum daily profit. [4 marks]

**(e)** Check boundary values and confirm $x^*$ is the global maximum on $[5, 25]$. [5 marks]

```
WORKING:
...
```"""),

        code("""\
# Q2 — Dairy profit optimisation
def C(x):
    return 2*x**2 - 80*x + 1200

def Revenue(x):
    return 1200 * x   # $1200 per thousand litres

def Pi(x):
    return Revenue(x) - C(x)

def dPi(x):
    return 1200 - (4*x - 80)   # Pi'(x) = R'(x) - C'(x)

# Critical point: dPi(x) = 0 → 1200 - 4x + 80 = 0 → 4x = 1280 → x* = 320
x_star = (1200 + 80) / 4
print(f"x* = {x_star}")
print(f"Pi''(x) = -4 < 0 → maximum confirmed")
print(f"Pi(x*) = ${Pi(x_star):,.2f}")
print(f"Pi(5)  = ${Pi(5):,.2f}")
print(f"Pi(25) = ${Pi(25):,.2f}")
        """),

        md("""\
The chart below shows profit as a function of output."""),

        code("""\
# Plot
x_vals = np.linspace(5, 25, 200)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x_vals, Pi(x_vals), "steelblue", lw=2.5)
ax.axvline(min(x_star, 25), color="red", ls="--", label=f"x*={min(x_star,25):.0f}")
ax.set_xlabel("Output x (000 litres)"); ax.set_ylabel("Profit ($)")
ax.set_title("Dairy Cooperative: Profit vs Output")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
---
## Question 3 — Integration (25 marks)

A solar panel array generates power:

$$P(t) = 500 \\sin\\!\\left(\\frac{\\pi t}{12}\\right) \\text{ watts}, \\quad 0 \\leq t \\leq 12 \\text{ hours}$$

**(a)** Sketch $P(t)$ over 12 hours. What is peak power and when does it occur? [4 marks]

**(b)** Set up the integral for total energy generated (watt-hours) over the full day. [4 marks]

**(c)** Evaluate $\\displaystyle\\int_0^{12} 500 \\sin\\!\\left(\\frac{\\pi t}{12}\\right)dt$ analytically. [10 marks]

**(d)** Convert to kWh. If electricity sells at 30 cents/kWh, what is daily revenue? [4 marks]

**(e)** Write Python code to verify your answer numerically. [3 marks]

```
WORKING:
...
```"""),

        code("""\
# Q3 — Solar energy integration
def P(t):
    return 500 * np.sin(np.pi * t / 12)

# Analytic: ∫₀¹² 500 sin(πt/12) dt = 500 × [-12/π cos(πt/12)]₀¹²
# = 500 × (-12/π)(cos(π) - cos(0)) = 500 × (-12/π)(-1 - 1) = 500 × 24/π
energy_Wh_analytic = 500 * 24 / np.pi
print(f"Analytic energy: {energy_Wh_analytic:.2f} Wh = {energy_Wh_analytic/1000:.4f} kWh")

# Numerical verification
from numpy import trapz
t_fine = np.linspace(0, 12, 10000)
energy_Wh_num = trapz(P(t_fine), t_fine)
print(f"Numerical energy: {energy_Wh_num:.2f} Wh")

# Revenue
energy_kWh = energy_Wh_analytic / 1000
revenue = energy_kWh * 0.30
print(f"Daily revenue: ${revenue:.4f}")

t_vals = np.linspace(0, 12, 200)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_vals, P(t_vals), "goldenrod", lw=2.5)
ax.fill_between(t_vals, P(t_vals), alpha=0.2, color="goldenrod")
ax.set_xlabel("Hour of day"); ax.set_ylabel("Power (W)")
ax.set_title("Solar Panel Output P(t) = 500 sin(πt/12)")
ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
---
## Question 4 — ODE (25 marks)

A water tank drains according to Torricelli's law:

$$\\frac{dV}{dt} = -0.5\\sqrt{V}, \\quad V(0) = 100 \\text{ L}$$

**(a)** This is a separable ODE. Separate variables and integrate both sides. [10 marks]

**(b)** Apply the initial condition $V(0) = 100$ to find the constant of integration. [4 marks]

**(c)** Solve for $V(t)$ explicitly. [4 marks]

**(d)** At what time $t^*$ does the tank empty ($V = 0$)? [4 marks]

**(e)** Write Python code to solve numerically using Euler's method and compare to your analytic solution. [3 marks]

```
WORKING:
Separating: dV/√V = -0.5 dt
Integrating: 2√V = -0.5t + C
Apply V(0)=100: 2√100 = C → C = 20
So: 2√V = -0.5t + 20 → √V = 10 - t/4 → V(t) = (10 - t/4)²
Tank empties when V=0: 10 - t/4 = 0 → t* = 40 min
```"""),

        code("""\
# Q4 — Draining tank: analytic vs Euler
def V_analytic(t):
    'Analytic solution: V(t) = (10 - t/4)^2'
    val = 10 - t / 4
    return val**2 if val > 0 else 0

# Euler method
dt = 0.01
T  = 42
steps = int(T / dt)
V_euler = np.zeros(steps + 1)
t_euler = np.zeros(steps + 1)
V_euler[0] = 100

for i in range(steps):
    dV = -0.5 * np.sqrt(max(V_euler[i], 0))
    V_euler[i+1] = max(0, V_euler[i] + dV * dt)
    t_euler[i+1] = t_euler[i] + dt

t_analytic = np.linspace(0, 40, 500)
V_an_vals  = np.array([V_analytic(t) for t in t_analytic])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_euler,    V_euler,   "steelblue", lw=2, label="Euler method")
ax.plot(t_analytic, V_an_vals, "red",       lw=2, ls="--", label="Analytic V(t)=(10-t/4)²")
ax.set_xlabel("Time (min)"); ax.set_ylabel("Volume (L)")
ax.set_title("Tank Draining: Analytic vs Euler")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()

print(f"Tank empties at t = 40 min (analytic)")
print(f"Euler: V(40) ≈ {V_euler[int(40/dt)]:.4f} L")"""),

        md("""\
---
## 📋 Group Debrief (after 40 minutes)

Compare your answers with your group:
1. Which question was hardest? Why?
2. Where did your working differ from your group member's? Who is correct?
3. What topics do you most need to review before the final exam?

```
DEBRIEF NOTES:
...
```"""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 11
# ─────────────────────────────────────────────────────────────────────────────

def week11_student():
    return notebook([

        md("""\
# Week 11 Lab — Peer Review: Trigonometric Modelling
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Creation (25 min) → Exchange → Solving (25 min) → Review and Discussion (10 min)

---
**Today:** You will design a sinusoidal science problem, exchange it with another group, and solve each other's problem using Python."""),

        md("""\
---
## 📋 Background: Sinusoidal Models

Many natural phenomena are periodic and can be modelled using:

$$f(t) = A \\cos(B(t + C)) + D$$

or equivalently $A \\sin(B(t + C)) + D$, where:

| Parameter | Meaning |
|-----------|---------|
| $A$ | **Amplitude** — half the range (max − min)/2 |
| $B$ | **Angular frequency** — $B = 2\\pi / T$ where $T$ is the period |
| $C$ | **Phase shift** — horizontal shift |
| $D$ | **Vertical shift** (midline) — (max + min)/2 |

**Example — Perth temperatures:**
Monthly mean max temperatures range from 18°C (July) to 32°C (January).
- $A = (32 - 18)/2 = 7$
- $D = (32 + 18)/2 = 25$
- $T = 12$ months, so $B = 2\\pi/12 = \\pi/6$
- Peak at month 1 (January): use $\\cos$ with no phase shift if we define $t=1$ = January.

$$T(t) = 7\\cos\\!\\left(\\frac{\\pi}{6}(t - 1)\\right) + 25$$"""),

        code(SETUP_IMPORTS + """

# Perth temperature example
def T_perth(t):
    'Monthly mean max temperature (°C), t = 1 (Jan) to 12 (Dec).'
    return 7 * np.cos(np.pi / 6 * (t - 1)) + 25

months = np.arange(1, 13)
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

print("Perth monthly mean max temperatures (model):")
for m, name in zip(months, month_names):
    print(f"  {name}: {T_perth(m):.1f} °C")"""),

        md("""\
Run the next cell."""),

        code("""\
        """),

        md("""\
The chart below shows the Perth temperature model."""),

        code("""\
# Plot Perth temperature model
t_fine = np.linspace(1, 13, 300)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_fine, T_perth(t_fine), "firebrick", lw=2.5, label="T(t) = 7cos(π(t−1)/6) + 25")
ax.scatter(months, [T_perth(m) for m in months], color="firebrick", s=60, zorder=5)
ax.axhline(25, color="gray", ls="--", alpha=0.5, label="Midline (25°C)")
ax.set_xticks(months); ax.set_xticklabels(month_names, fontsize=8)
ax.set_ylabel("Temperature (°C)")
ax.set_title("Perth Monthly Mean Maximum Temperature — Sinusoidal Model")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
---
## Part 1: Create Your Problem (25 minutes)

**Your group's task:**

1. Choose a **natural or agricultural phenomenon** with a seasonal or periodic pattern.
   Ideas: tidal height, crop yield, daylight hours, fish migration counts, power demand, rainfall.

2. Decide on realistic **parameter values** ($A$, $B$, $C$, $D$, period, units).

3. Write a brief scenario (3–5 sentences) and pose **three questions**:
   - Q1: What is the period and amplitude? Interpret them.
   - Q2: Find the maximum and minimum values, and when they occur.
   - Q3: Use integration to find the **total** (area under curve) over one full period.

4. Write the **answer key** (for checking after exchange).

Use the cells below to develop and test your problem:"""),

        md("""\
--- YOUR PROBLEM DEVELOPMENT ---."""),

        code("""\
# --- YOUR PROBLEM DEVELOPMENT ---
# Replace the example below with your own scenario

# Example: Ocean tidal height at a coastal research station
def h(t):
    'Tidal height (m) at hour t. Period = 12.5 hr, amplitude = 1.8 m.'
    return 1.8 * np.cos(2 * np.pi / 12.5 * t) + 3.2

t_vals = np.linspace(0, 25, 300)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_vals, h(t_vals), "steelblue", lw=2.5)
ax.axhline(3.2, color="gray", ls="--", alpha=0.5, label="Midline 3.2 m")
ax.set_xlabel("Hours"); ax.set_ylabel("Tidal height (m)")
ax.set_title("Example: Tidal Height h(t) = 1.8cos(2πt/12.5) + 3.2")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()

print(f"Period: 12.5 hours")
print(f"Maximum: {h(0):.1f} m at t = 0, 12.5, ... hours")
print(f"Minimum: {3.2 - 1.8:.1f} m at t = 6.25, 18.75, ... hours")"""),

        md("""\
Integration over one period (total tidal volume per unit wid."""),

        code("""\
# Integration over one period (total tidal volume per unit width)
from numpy import trapz

T_period = 12.5
t_one = np.linspace(0, T_period, 10000)
total = trapz(h(t_one), t_one)
average = total / T_period

print(f"Total area over one period: {total:.2f} m·hr")
print(f"Average tidal height: {average:.2f} m")

# YOUR PROBLEM'S integration answer here:
# ...
"""),

        md("""\
---
## 📋 Problem Statement (for exchange)

**Write your problem here so the other group can read it without seeing your code:**

```
SCENARIO:
...

FUNCTION:
f(t) = ...

QUESTIONS:
Q1: ...
Q2: ...
Q3: ...
```"""),

        md("""\
---
## Part 2: Solve the Other Group's Problem (25 minutes)

**Instructions:** Receive the other group's problem statement. Solve it in the cells below. Do not look at their code until after you have finished.

Write your function, plot it, and answer each of their three questions. Show Python calculations for Q3."""),

        md("""\
--- SOLVING THE OTHER GROUP'S PROBLEM ---."""),

        code("""\
# --- SOLVING THE OTHER GROUP'S PROBLEM ---

# Step 1: Define their function
def f_other(t):
    'Other group function — replace with their parameters.'
    A = 1     # amplitude
    B = 1     # angular frequency
    C = 0     # phase shift
    D = 0     # vertical shift
    return A * np.cos(B * (t + C)) + D

# Step 2: Plot it
T_other = 2 * np.pi   # period — adjust to their period
t_vals = np.linspace(0, 2 * T_other, 400)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_vals, f_other(t_vals), "seagreen", lw=2.5)
ax.set_xlabel("t"); ax.set_ylabel("f(t)")
ax.set_title("Other Group's Function")
ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
Q1: Period and amplitude."""),

        code("""\
# Q1: Period and amplitude
print("Q1 Answers:")
print(f"  Amplitude A = ...")
print(f"  Period T    = ...")
print(f"  Interpretation: ...")

# Q2: Maximum and minimum
print("\\nQ2 Answers:")
print(f"  Maximum value = ... at t = ...")
print(f"  Minimum value = ... at t = ...")

# Q3: Integration over one period
t_one = np.linspace(0, T_other, 10000)
total_other = trapz(f_other(t_one), t_one)
print(f"\\nQ3 Answer:")
print(f"  Total over one period = {total_other:.4f}")"""),

        md("""\
---
## Part 3: Review and Discussion (10 minutes)

1. Exchange answer keys and check your solutions.
2. Discuss any discrepancies — where did the working differ?

```
REVIEW NOTES:
Q1: Correct / Incorrect — ...
Q2: Correct / Incorrect — ...
Q3: Correct / Incorrect — ...
Main learning points:
...
```"""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# WEEK 12
# ─────────────────────────────────────────────────────────────────────────────

def week12_student():
    return notebook([

        md("""\
# Week 12 Lab — Linear Programming and Gallery Walk
## SCIE1500 Science and Quantitative Reasoning — Semester 2, 2026

**Lab format:** Groups work on the LP problem (50 min) → Gallery Walk (20 min) → Debrief (10 min)

---
**Today:** We solve a dietary optimisation problem using linear programming (LP). Groups post their graphical solutions; everyone walks around and critiques each other's work."""),

        md("""\
---
## 📋 Scientific Scenario

A hospital dietitian needs to design a daily meal plan for patients that meets nutritional requirements at minimum cost. Two food types are available:

- **Food X** (plant-based): costs **$2.50/serve**, provides 18 g protein, 220 kcal, 3 mg iron, 0.5 kg CO₂-e
- **Food Y** (chicken): costs **$4.00/serve**, provides 30 g protein, 280 kcal, 1 mg iron, 2.5 kg CO₂-e

Daily requirements per patient:
- Protein: at least 350 g
- Calories: at least 3,500 kcal
- Iron: at least 25 mg
- Carbon footprint: at most 20 kg CO₂-e per day

**Decision variables:** $x$ = serves of Food X, $y$ = serves of Food Y

---
## 🎯 Group Task & Learning Objectives

| Part | Topic | Time |
|------|-------|------|
| A | Formulate the LP and identify constraints | ~15 min |
| B | Graph the feasible region | ~20 min |
| C | Find the optimal solution using corner-point theorem | ~15 min |"""),

        code(SETUP_IMPORTS + """

# LP parameters
cost = np.array([2.5, 4.0])     # objective: minimise 2.5x + 4y

# Constraints (as functions of x for plotting y = f(x))
def protein_line(x):
    '18x + 30y = 350  →  y = (350 - 18x) / 30'
    return (350 - 18*x) / 30

def calorie_line(x):
    '220x + 280y = 3500  →  y = (3500 - 220x) / 280'
    return (3500 - 220*x) / 280

def iron_line(x):
    '3x + y = 25  →  y = 25 - 3x'
    return 25 - 3*x

def carbon_line(x):
    '0.5x + 2.5y = 20  →  y = (20 - 0.5x) / 2.5'
    return (20 - 0.5*x) / 2.5

x_vals = np.linspace(0, 20, 300)

print("Constraint summary:")
print("  Protein:  18x + 30y ≥ 350")
print("  Calories: 220x + 280y ≥ 3500")
print("  Iron:     3x + y ≥ 25")
print("  Carbon:   0.5x + 2.5y ≤ 20")
print("  x ≥ 0, y ≥ 0")"""),

        md("""\
---
## Part A: LP Formulation (~15 min)

**Objective function:**
$$\\text{Minimise } Z = 2.5x + 4y$$

**Subject to:**
$$18x + 30y \\geq 350 \\quad \\text{(protein)}$$
$$220x + 280y \\geq 3500 \\quad \\text{(calories)}$$
$$3x + y \\geq 25 \\quad \\text{(iron)}$$
$$0.5x + 2.5y \\leq 20 \\quad \\text{(carbon)}$$
$$x \\geq 0,\\; y \\geq 0$$

✏️ **A.1** For each constraint, identify which is a minimum requirement (≥) vs a maximum limit (≤). Why does this distinction matter for which side of the line is feasible?

```
ANSWERS:
...
```"""),

        code("""\
# B.1 — Plot all constraint lines
fig, ax = plt.subplots(figsize=(9, 8))

ax.plot(x_vals, protein_line(x_vals), "steelblue", lw=2, label="Protein: 18x+30y=350")
ax.plot(x_vals, calorie_line(x_vals), "firebrick", lw=2, label="Calories: 220x+280y=3500")
ax.plot(x_vals, iron_line(x_vals),    "seagreen",  lw=2, label="Iron: 3x+y=25")
ax.plot(x_vals, carbon_line(x_vals),  "purple",    lw=2, label="Carbon: 0.5x+2.5y=20")

# Shade feasible region (approximate)
y_grid = np.linspace(0, 20, 400)
xx, yy = np.meshgrid(x_vals, y_grid)
feasible = (
    (18*xx + 30*yy >= 350) &
    (220*xx + 280*yy >= 3500) &
    (3*xx + yy >= 25) &
    (0.5*xx + 2.5*yy <= 20) &
    (xx >= 0) & (yy >= 0)
)
ax.contourf(xx, yy, feasible.astype(float), levels=[0.5, 1.5], colors=["lightblue"], alpha=0.4)

ax.set_xlim(0, 18); ax.set_ylim(0, 18)
ax.set_xlabel("x (serves of Food X)"); ax.set_ylabel("y (serves of Food Y)")
ax.set_title("Hospital Diet LP: Feasible Region")
ax.legend(fontsize=9); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()"""),

        md("""\
---
## Part C: Corner-Point Theorem (~15 min)

The minimum (or maximum) of a linear objective occurs at a **corner point** (vertex) of the feasible region.

**C.1** Find the corner points by solving pairs of constraints simultaneously.

Key intersections to check:
- Protein ∩ Iron: $18x + 30y = 350$ and $3x + y = 25$
- Protein ∩ Carbon: $18x + 30y = 350$ and $0.5x + 2.5y = 20$
- Calories ∩ Carbon: $220x + 280y = 3500$ and $0.5x + 2.5y = 20$
- Iron ∩ Carbon: $3x + y = 25$ and $0.5x + 2.5y = 20$"""),

        code("""\
# C.1 — Find corner points by solving pairs of constraints
from numpy.linalg import solve as linsolve

def find_corner(A_mat, b_vec):
    'Solve 2×2 linear system A x = b.'
    try:
        sol = linsolve(np.array(A_mat, dtype=float), np.array(b_vec, dtype=float))
        return sol if all(s >= -1e-6 for s in sol) else None
    except np.linalg.LinAlgError:
        return None

# Constraint matrix rows: [coeff_x, coeff_y]
corners_raw = [
    find_corner([[18, 30], [3, 1]],      [350, 25]),      # protein ∩ iron
    find_corner([[18, 30], [0.5, 2.5]],  [350, 20]),      # protein ∩ carbon
    find_corner([[220, 280], [0.5, 2.5]],[3500, 20]),     # calories ∩ carbon
    find_corner([[3, 1], [0.5, 2.5]],    [25, 20]),       # iron ∩ carbon
    find_corner([[220, 280], [3, 1]],    [3500, 25]),     # calories ∩ iron
]

corners = [c for c in corners_raw if c is not None]

print(f"{'Corner (x,y)':25s} {'Z=2.5x+4y':>12} {'Feasible?':>12}")
print("-" * 52)
for c in corners:
    x, y = c
    Z = 2.5*x + 4*y
    # Check all constraints
    ok = (18*x + 30*y >= 349.9 and 220*x + 280*y >= 3499.9 and
          3*x + y >= 24.9 and 0.5*x + 2.5*y <= 20.1 and x >= -0.01 and y >= -0.01)
    print(f"({x:6.2f}, {y:6.2f})          Z = {Z:8.2f}     {'✓' if ok else '✗'}")"""),

        md("""\
Identify optimal corner."""),

        code("""\
# C.2 — Identify optimal corner
feasible_corners = []
for c in corners:
    x, y = c
    ok = (18*x + 30*y >= 349.9 and 220*x + 280*y >= 3499.9 and
          3*x + y >= 24.9 and 0.5*x + 2.5*y <= 20.1 and x >= -0.01 and y >= -0.01)
    if ok:
        feasible_corners.append((x, y, 2.5*x + 4*y))

if feasible_corners:
    best = min(feasible_corners, key=lambda c: c[2])
    print(f"Optimal solution: x* = {best[0]:.2f}, y* = {best[1]:.2f}")
    print(f"Minimum cost: Z* = ${best[2]:.2f} per patient per day")
else:
    print("No feasible corners found — check constraint formulation")"""),

        md("""\
Scipy LP verification."""),

        code("""\
# C.3 — Scipy LP verification
from scipy.optimize import linprog

# Minimise 2.5x + 4y
# Constraints: convert all to ≤ form (negate ≥ constraints)
c_obj = [2.5, 4.0]

A_ub = [
    [-18, -30],    # -protein ≤ -350
    [-220, -280],  # -calories ≤ -3500
    [-3, -1],      # -iron ≤ -25
    [0.5, 2.5],    # carbon ≤ 20
]
b_ub = [-350, -3500, -25, 20]

result = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None),(0,None)], method='highs')
print(f"scipy linprog result:")
print(f"  x* = {result.x[0]:.4f} serves of Food X")
print(f"  y* = {result.x[1]:.4f} serves of Food Y")
print(f"  Z* = ${result.fun:.4f} per patient per day")"""),

        md("""\
---
## 🖼️ Gallery Walk Instructions (20 minutes)

1. Each group posts their **feasible region diagram** and **corner point table** on the wall.
2. Rotate through all groups (3–4 minutes per station).
3. Use sticky notes or write on the sheet:
   - **Green:** Something correct or clear
   - **Orange:** A question or concern
   - **Red:** An error found

**What to look for:**
- Is the feasible region shaded on the correct side of each constraint?
- Are all corner points correct (solve the system and check)?
- Is the minimum at the correct vertex?

---
## ✅ Submission Exercise — Batch 4 (due Tuesday 27 October, 11:59 pm)

**Submit via LMS. Covers Weeks 10–12 (hypothesis testing, trigonometry, linear programming).**

Work individually. Show all working. Write Python code where indicated.

---
### Q1 — Hypothesis Testing (Week 10)

A water authority claims average daily water consumption in a suburb is **no more than 180 L per person**. A sample of 36 households gives $\\bar{x} = 191$ L and $s = 42$ L.

**(a)** State $H_0$ and $H_1$ for a one-tailed test.

**(b)** Calculate the $t$-statistic. Show all working.

**(c)** At $\\alpha = 0.05$ ($df = 35$, one-tailed critical value $\\approx 1.690$), state your conclusion.

**(d)** Write Python code to compute the exact $p$-value using `scipy.stats.t`.

```python
# Q1d
from scipy import stats
# YOUR CODE HERE
```

---
### Q2 — Trigonometric Modelling (Week 11)

Daylight hours in a southern Australian city vary seasonally. The longest day has 14.5 hours (December 22) and the shortest has 9.5 hours (June 21).

**(a)** Find the amplitude $A$ and midline $D$.

**(b)** The period is 365 days. Find $B = 2\\pi/365$.

**(c)** Write the function $f(t)$ where $t$ = day of year, with $f(1) = 9.5$ (January 1 is near the shortest day). Use an appropriate phase shift.

**(d)** Write Python code to: (i) plot $f(t)$ for one year; (ii) calculate the total daylight hours over the year using `numpy.trapz`.

```python
# Q2d
import numpy as np, matplotlib.pyplot as plt
%matplotlib inline
# YOUR CODE HERE
```

---
### Q3 — Linear Programming (Week 12)

A farmer grows wheat ($x$ ha) and canola ($y$ ha) on 200 ha. Constraints:
- Land: $x + y \\leq 200$
- Water: $3x + 5y \\leq 800$ (ML)
- Labour: $x + 2y \\leq 300$ (days)
- Non-negativity: $x \\geq 0$, $y \\geq 0$

Profit: wheat $\\$180$/ha, canola $\\$250$/ha. **Maximise** $Z = 180x + 250y$.

**(a)** Graph the feasible region. Label each constraint line and shade the feasible region.

**(b)** Identify all corner points (intersections of constraint boundaries within the feasible region).

**(c)** Evaluate $Z$ at each corner point. State the optimal solution.

**(d)** Write Python code using `scipy.optimize.linprog` to verify your answer. (Note: `linprog` minimises — negate the objective to maximise.)

```python
# Q3d
from scipy.optimize import linprog
# YOUR CODE HERE
```"""),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# DISPATCH
# ─────────────────────────────────────────────────────────────────────────────

BUILDERS = {
    1: [
        (week1_student, "Week_1/LabFiles/Week01_Lab_STUDENT.ipynb"),
    ],
    2: [
        (week2_student, "Week_2/LabFiles/Week02_Lab_STUDENT.ipynb"),
        (week2_lab_a,   "Week_2/LabFiles/Week02_Lab_A.ipynb"),
        (week2_lab_b,   "Week_2/LabFiles/Week02_Lab_B.ipynb"),
    ],
    3: [
        (week3_student, "Week_3/LabFiles/Week03_Lab_STUDENT.ipynb"),
        (week3_lab_a,   "Week_3/LabFiles/Week03_Lab_A.ipynb"),
        (week3_lab_b,   "Week_3/LabFiles/Week03_Lab_B.ipynb"),
    ],
    4: [
        (week4_student, "Week_4/LabFiles/Week04_Lab_STUDENT.ipynb"),
        (week4_lab_a,   "Week_4/LabFiles/Week04_Lab_A.ipynb"),
        (week4_lab_b,   "Week_4/LabFiles/Week04_Lab_B.ipynb"),
    ],
    5: [
        (week5_student, "Week_5/LabFiles/Week05_Lab_STUDENT.ipynb"),
        (week5_lab_a,   "Week_5/LabFiles/Week05_Lab_A.ipynb"),
        (week5_lab_b,   "Week_5/LabFiles/Week05_Lab_B.ipynb"),
    ],
    6: [
        (week6_student, "Week_6/LabFiles/Week06_Lab_STUDENT.ipynb"),
        (week6_lab_a,   "Week_6/LabFiles/Week06_Lab_A.ipynb"),
        (week6_lab_b,   "Week_6/LabFiles/Week06_Lab_B.ipynb"),
    ],
    7: [
        (week7_student, "Week_7/LabFiles/Week07_Lab_STUDENT.ipynb"),
        (week7_lab_a,   "Week_7/LabFiles/Week07_Lab_A.ipynb"),
        (week7_lab_b,   "Week_7/LabFiles/Week07_Lab_B.ipynb"),
    ],
    8: [
        (week8_student, "Week_8/LabFiles/Week08_Lab_STUDENT.ipynb"),
        (week8_lab_a,   "Week_8/LabFiles/Week08_Lab_A.ipynb"),
        (week8_lab_b,   "Week_8/LabFiles/Week08_Lab_B.ipynb"),
    ],
    9: [
        (week9_student, "Week_9/LabFiles/Week09_Lab_STUDENT.ipynb"),
    ],
    10: [
        (week10_student, "Week_10/LabFiles/Week10_Lab_STUDENT.ipynb"),
    ],
    11: [
        (week11_student, "Week_11/LabFiles/Week11_Lab_STUDENT.ipynb"),
    ],
    12: [
        (week12_student, "Week_12/LabFiles/Week12_Lab_STUDENT.ipynb"),
    ],
}

IMPLEMENTED = sorted(BUILDERS.keys())

def generate_week(week_num):
    if week_num not in BUILDERS:
        print(f"  Week {week_num} not yet implemented (implemented: {IMPLEMENTED})")
        return
    print(f"Generating Week {week_num}:")
    for builder_fn, rel_path in BUILDERS[week_num]:
        write_nb(builder_fn(), BASE / rel_path)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: python generate_lab_notebooks.py <week> [week ...] | all")
        sys.exit(1)

    weeks = IMPLEMENTED if args[0] == "all" else [int(a) for a in args]
    for w in weeks:
        generate_week(w)
    print("Done.")
