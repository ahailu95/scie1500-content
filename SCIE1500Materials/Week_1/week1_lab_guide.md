<?xml version="1.0" encoding="UTF-8"?>
# Week 1 Lab Guide: Functions and Ocean Pollution

## SCIE1500 — Analytical Methods for Scientists

---

## Overview

This guide helps you navigate **Week 1** materials efficiently. The main lab activity uses a single integrated notebook that covers both mathematical functions and real-world data analysis.

**Estimated Time:** 5-6 hours total (including preparation)

---

## Materials

| Resource | Type | Where to Find It |
|----------|------|------------------|
| Week 1 Lesson | Reading | App → Week 1 → Notes |
| 📚 Lesson with Code | Interactive notebook | App → Week 1 → Notes |
| Week1_Functions_Complete.ipynb | Lab notebook | LMS / Week 1 LabFiles |
| Practice Questions | Self-assessment | App → Week 1 → Practice |
| global-plastics-production.csv | Data file | Week 1 LabFiles |
| Jambeck2015Table1.csv | Data file | Week 1 LabFiles |

---

## Learning Pathway

### Before Lab (2 hours)

1. **Read the lesson** (`week1_lesson.md`)
   - Focus on: function definitions, domain/range, linear and quadratic functions
   - Key concept: What makes something a function? (vertical line test)

2. **Try Practice Questions Q1-Q4**
   - These test the math concepts you'll implement in Python
   - Use the AI tutor for hints if stuck

3. **Optionally:** Work through the "📚 Lesson with Code" notebook for interactive examples

### During Lab (90 minutes)

Open `Week1_Functions_Complete.ipynb` and work through:

| Part | Topic | Time | Assessment |
|------|-------|------|------------|
| A | The Plastic Pollution Crisis | 10 min | — |
| B | Python Functions Fundamentals | 20 min | **Exercise A** ✓ |
| C | Domains of Functions | 20 min | **Exercise B** ✓ |
| D | Linear Functions | 20 min | **Exercise C** ✓ |
| E | Quadratic Functions | 20 min | **Exercise D** ✓ |

**Checkpoint:** Show Exercise A to your demonstrator before proceeding.

### After Lab (60-90 minutes)

Complete the remaining sections at home:

| Part | Topic | Time |
|------|-------|------|
| F | Real Data with Pandas | 30 min |
| G | Jambeck Country Analysis | 30 min |

---

## Key Exam Connections

| Notebook Part | Exam Question | What to Focus On |
|---------------|---------------|------------------|
| Part C | MCQ Q10 | Identifying valid domains |
| Part E | MCQ Q22 | Quadratic vertex formula: $x = -\frac{b}{2a}$ |

---

## What to Submit

**During lab:**
- Show **Exercise A** (triangle function) to your demonstrator

**Upload to LMS:**
- Screenshot of **Exercise B** (domain function)
- Screenshot of **Exercise C** (linear plotting)
- Screenshot of **Exercise D** (quadratic analysis)

---

## Troubleshooting

### "My function doesn't work"
Check these common issues:
```python
# Wrong: Missing return statement
def my_function(x):
    result = x * 2
    
# Correct: Include return
def my_function(x):
    result = x * 2
    return result
```

### "I can't load the CSV file"
Make sure the data file is in the same folder as your notebook:
```python
# Check your current directory
import os
print(os.getcwd())
print(os.listdir())  # See what files are there
```

### "My plot doesn't show"
Make sure you ran the Setup cell at the top (it includes `%matplotlib inline`).

### "Domain question is confusing"
Remember the key restrictions:
- **Square roots:** Expression inside must be ≥ 0
- **Fractions:** Denominator cannot equal 0
- **Logarithms:** Argument must be > 0

---

## Concept Quick Reference

| Math Concept | Python Implementation |
|--------------|----------------------|
| $f(x) = mx + c$ | `def linear(x, m, c): return m*x + c` |
| $f(x) = ax^2 + bx + c$ | `def quadratic(x, a, b, c): return a*x**2 + b*x + c` |
| Vertex x-coordinate | `x_vertex = -b / (2*a)` |
| Domain check | `if x >= 0:` (example) |

---

## What's Next

In **Week 2**, you'll explore:
- **Piecewise functions** — different rules for different regions
- **Fisheries economics** — using linear models for sustainable fishing
- **Data transformations** — preparing real data for analysis

---

*Version 3.0 | Updated January 2026 | Compatible with Week1_Functions_Complete.ipynb*
