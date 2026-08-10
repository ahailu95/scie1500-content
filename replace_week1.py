import re

file_path = '/Users/00047562/Dropbox/sciquant_app/assets/SCIE1500Materials_S2Y26/src/Week_01/Week_01_Master.qmd'

with open(file_path, 'r') as f:
    content = f.read()

# The content to inject
new_head = """---
title: "Week 1: Functions and the Language of Scientific Analysis"
topic: "Understanding Functional Relationships"
jupyter: python3
format:
  html: default
  revealjs: default
---

<!-- =================================================================== -->
<!-- SLIDES (applies when profile='slides')                              -->
<!-- =================================================================== -->
::: {.content-visible when-profile="slides"}

## Unit Introduction & Overview
### Scientific Analysis

- Welcome to SCIE1500
- **Goal:** Learn to model and analyze real-world scientific scenarios
- Mathematical tools: Functions, Calculus, Probability, Statistics

---

## What is a Function?

A function is a **rule** that assigns to each input exactly one output.

- $f(x) = y$
- **Input:** Independent variable ($x$)
- **Output:** Dependent variable ($y$)

---

## Domain and Range

- **Domain:** The set of all possible input values (where the function is defined)
- **Range:** The set of all possible output values

**Example:**
For $f(x) = \sqrt{x}$, the mathematical domain is $x \ge 0$.
In contexts like measuring mass, the physical domain might be $m > 0$.

---

## Linear and Non-Linear Models

- **Linear Models:** Constant rate of change
   - e.g., $y = mx + c$
- **Non-Linear Models:** Changing rate of change
   - e.g., Exponential growth, Logistic curves, Polynomials

---

## The Analytical Pipeline

1. **Observe** a physical/biological phenomenon
2. **Formulate** a mathematical model (Function)
3. **Analyze** the properties (Domain, Range, Rate of Change)
4. **Communicate** the findings to inform decisions

:::


<!-- =================================================================== -->
<!-- STUDENT HANDBOOK (applies when profile='handbook' or 'instructor')  -->
<!-- =================================================================== -->
::: {.content-visible when-profile="handbook"}
::: {.content-visible when-profile="instructor"}

## Week 1: Functions and Their Properties

### PROBLEM BRIEF: W1
**"Global Plastic Production: Understanding Functional Relationships"**

#### SCENARIO

The United Nations Environment Programme (UNEP) is preparing a report on plastic waste in oceans. You are part of a team analyzing historical data on global plastic production.

**Data: Global plastic production (million tonnes)**

| Year | 1950 | 1970 | 1990 | 2010 | 2015 |
|------|------|------|------|------|------|
| Production | 2 | 35 | 120 | 270 | 380 |

The relationship between year and production can be modeled as a function $P(t)$ where $t$ is years since 1950.

#### YOUR TASK

**Part A: Function Basics (20 minutes)**

1. Define the function $P(t)$ using the 1950 data point as the origin:
   - $P(0) = 2$ (in 1950)
   - $P(65) = 380$ (in 2015)

2. Calculate the **average rate of change** from 1950 to 2015:
   $$\text{Average rate} = \frac{P(65) - P(0)}{65 - 0}$$
   Include units in your answer.

3. What is the **domain** of this function?
   - Mathematical domain: all valid $t$ values
   - Physical domain: realistic time range for this model

4. What is the **range** of this function based on the data?

**Part B: Interpreting Slope (15 minutes)**

5. Calculate the average rate of change between consecutive decades:
   - 1950–1970
   - 1970–1990
   - 1990–2010
   - 2010–2015 (5 years)

6. What do you notice about how the rate of production growth changes over time?

**Part C: Australian Policy Application (20 minutes)**

7. Australia's coastal population in 2010 was approximately 20 million, with 50 kg of plastic waste per person per year. If 2% of this waste is mismanaged (enters the ocean):
   - Calculate Australia's daily mismanaged plastic waste entering the ocean
   - Convert to annual waste (tonnes/year)

8. If Australia's coastal population grows at 1.5% per year, write a function $W(t)$ for annual mismanaged waste, where $t$ is years from 2010.

9. The government proposes reducing the mismanagement rate from 2% to 0.5% by 2030. Would this offset the population growth effect? Support your answer with calculations.

#### DELIVERABLES

- [ ] Completed Group Worksheet
- [ ] Python plots (if created) as appendix

#### HINTS / SCAFFOLDING

**For interpreting slope:**
- Slope = $\frac{\Delta y}{\Delta x}$ = change in output per unit change in input
- Units: (million tonnes) / (year) = million tonnes per year

**For domain analysis:**
- Mathematical domain: all $x$ values where the function is defined
- Physical domain: all $x$ values that make sense in the real-world context

**Python starter for plotting:**
```python
import matplotlib.pyplot as plt

years = [1950, 1970, 1990, 2010, 2015]
production = [2, 35, 120, 270, 380]

plt.scatter(years, production)
plt.xlabel('Year')
plt.ylabel('Production (million tonnes)')
plt.title('Global Plastic Production')
plt.show()
```

:::
:::

<!-- =================================================================== -->
<!-- INSTRUCTOR NOTES (applies when profile='instructor')                -->
<!-- =================================================================== -->
::: {.content-visible when-profile="instructor"}

## INSTRUCTOR GUIDE: Week 1 – Functions & Plastic Production

### 🎯 Teaching Priorities (Week 1)
1. **Physical vs Mathematical Domain**: Students often just write "all real numbers" for domain. Emphasize that models break down outside their physical domain (e.g., negative plastic production doesn't exist).
2. **Units on Slopes**: A rate of change is meaningless without units. Insist on "million tonnes per year" rather than just a number.
3. **Model Selection**: Guide them to observe the non-constant rate of change in Part B, which sets up the need for exponential models in Week 2.

### 👥 Lab Activities (2 Hours)
- **0:00-0:15:** Briefing. Introduce the problem structure. Explain how lab groups work and the expectation that everyone participates.
- **0:15-0:35:** Python Environment Check. Ensure everyone can open the notebook, select the kernel, and run a plot. Fix Jupyter issues now so they don't block later weeks.
- **0:35-1:40:** Group Work on Problem Brief. Circulate explicitly checking that students have correctly identified the origin (1950 -> $t=0$). 
- **1:40-2:00:** Wrap-up. Discuss Part B findings as a class. 

### 📝 Marking Guidance (Worksheets)
- **Part A (Domain/Range):** Full marks require both physical and mathematical domains correctly identified. Range should reflect the bounds of the provided data points.
- **Part B (Slope interpretation):** Look for the conclusion that the rate connects consecutive points but is changing over time. If they average all gaps into one slope, they miss the point.
- **Part C (Calculations):** Ensure the unit conversions from days -> years are correct. The final answer (reducing to 0.5%) dominates the population growth. 

### ❌ Common Errors (-Point deductions)
- **[-1] Missing Units:** The rate of change in part A/B lacks units.
- **[-1] Missing the t-shift:** Using actual years (1970) as $x$ instead of $t=20$.
- **[-2] Linear assumption:** Assuming the growth between 2010 and 2030 in Part C is strictly linear without confirming population scaling.

### 💡 Discussion Points
If a group finishes early, challenge them with: "What if the 2015 data point was an anomaly caused by a reporting error? How would you verify it?" or "If this trend continues to 2050, what mathematical shape does it resemble?"

### 👁️ Academic Integrity Watch
- **AI over-reliance:** Watch for students writing high-level Pandas code they can't explain to solve basic array plotting. "Can you tell me what `plt.scatter` is doing here?" If they can't, tell them to rewrite and add comments explaining the arguments.
- **Plagiarism:** Groups copying the exact same policy interpretations for Part C.

:::

<!-- =================================================================== -->
<!-- APP LESSON (applies when profile='app-lesson')                      -->
<!-- =================================================================== -->

::: {.content-visible when-profile="app-lesson"}
"""

# Replace everything from the top of the file down to the first app-lesson tag
parts = content.split("<!-- =================================================================== -->\n<!-- APP LESSON (applies when profile='app-lesson')                      -->\n<!-- =================================================================== -->\n\n::: {.content-visible when-profile=\"app-lesson\"}")

if len(parts) == 2:
    with open(file_path, 'w') as f:
        f.write(new_head + parts[1])
    print("Replaced head of QMD successfully!")
else:
    print("Could not split properly, len was", len(parts))

