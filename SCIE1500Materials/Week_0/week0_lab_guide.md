# Week 0 Lab Guide: Python Basics

## SCIE1500 — Analytical Methods for Scientists

---

## Overview

This guide helps you navigate **Week 0** materials. The goal is to ensure everyone has a solid foundation in both mathematics and Python before the course accelerates.

**Estimated Time:** 4-5 hours total (including math review)

---

## Materials

| Resource | Type | Where to Find It |
|----------|------|------------------|
| Week 0 Lesson | Reading | App → Week 0 → Notes |
| 📚 Lesson with Code | Interactive notebook | App → Week 0 → Notes |
| Week0_Intro_Python.ipynb | Lab notebook | LMS / Week 0 LabFiles |
| Practice Questions | Self-assessment | App → Week 0 → Practice |

---

## Learning Pathway

### Before Lab (1.5-2 hours)

**Math Review:**
1. Read `week0_lesson.md` sections 1-9
2. Try Practice Questions Q1-Q6 (test your foundations)

**Key topics to review:**
- BODMAS / Order of operations
- Exponents and radicals ($x^{1/2} = \sqrt{x}$)
- Solving equations and inequalities
- Scientific notation ($6.022 \times 10^{23}$)
- Function notation ($f(x)$ means "evaluate f at x")
- Interval notation ($[a, b]$ vs $(a, b)$)

### During Lab (2 hours)

Open `Week0_Intro_Python.ipynb` and work through:

| Section | Topic | Time | Key Skills |
|---------|-------|------|------------|
| §0 | Warmup — Python as Calculator | 30 min | Basic arithmetic, arrays |
| §1-2 | Python Syntax | 20 min | Case sensitivity, comments |
| §3 | Data Types | 20 min | int, float, str, bool |
| §4 | Operators | 25 min | Arithmetic, comparison, logical |
| §5-6 | Modules | 30 min | math, numpy, linspace |
| §7 | Plotting | 30 min | matplotlib basics |

### Lab Exercises to Complete

| Exercise | Task | Shows Understanding Of |
|----------|------|------------------------|
| A | Plot leaf area vs weight | Arrays, basic plotting |
| B | Calculate expressions | BODMAS in Python |
| C | Fix syntax errors | Python syntax rules |
| D | Logical operators | Boolean logic |
| E | Operator precedence | BODMAS |
| F | Create arrays with linspace | numpy arrays |
| G | 2D arrays | Array operations |
| H-I | Plot a parabola | Function visualization |

---

## Key Connections: Math ↔ Python

| Math Concept | Python Equivalent |
|--------------|-------------------|
| $x^n$ | `x ** n` |
| $\sqrt{x}$ | `math.sqrt(x)` or `x ** 0.5` |
| $e^x$ | `math.exp(x)` |
| $\ln(x)$ | `math.log(x)` |
| $\pi$ | `math.pi` |
| $e$ | `math.e` |
| Integer division | `a // b` |
| Remainder (mod) | `a % b` |

---

## Essential Code Patterns

### Importing libraries
```python
import numpy as np
import matplotlib.pyplot as plt
import math
```

### Creating arrays
```python
# From a list
x = np.array([1, 2, 3, 4, 5])

# Evenly spaced values
x = np.linspace(0, 10, 5)  # [0, 2.5, 5, 7.5, 10]
```

### Basic plotting
```python
plt.plot(x, y, '-b')  # solid blue line
plt.title("My Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
```

---

## Troubleshooting

### "My code won't run"
- Python is **case-sensitive**: `Print` ≠ `print`
- Check all parentheses are matched
- Read the error message — it points to the problem line

### "My plot doesn't appear"
Run this at the top of your notebook:
```python
%matplotlib inline
```

### "I can't import numpy"
Re-run the import cell. In a new session, run all import cells first.

### "I don't understand function notation f(x)"
- $f(x) = x^2 + 1$ means: "whatever number goes in, square it and add 1"
- $f(3) = 3^2 + 1 = 10$
- It's **not** multiplication! $f(x) \neq f \times x$

---

## Self-Check: Ready for Week 1?

Before moving on, confirm you can:

- [ ] Evaluate expressions using BODMAS correctly
- [ ] Work with exponents: $2^3 = 8$, $8^{1/3} = 2$
- [ ] Solve linear equations: $2x + 5 = 11$
- [ ] Understand $f(x)$ notation (not multiplication!)
- [ ] Run Python code in Jupyter Notebook
- [ ] Create arrays with `np.linspace()`
- [ ] Make basic plots with `matplotlib`

---

## What's Next

In **Week 1**, you'll:
- Define your own Python functions
- Work with linear and quadratic functions
- Analyze real ocean plastic pollution data
- Connect math models to scientific problems

---

*Version 3.0 | Updated January 2026 | Compatible with Week0_Intro_Python.ipynb*
