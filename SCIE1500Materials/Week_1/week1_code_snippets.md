<?xml version="1.0" encoding="UTF-8"?>
# Python Code Snippets - Functions

**Copy-ready Python code examples for Week 1**

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
```

---

## 1. Standard Imports for Week 1

Import statements for Functions.ipynb and PlasticPollution.ipynb

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
```

---


## 2. Defining a Linear Function

General linear function y = ax + b

```python
def linear_fun(a, b, x):
    y = a * x + b
    return y

# Example: y = 2x + 5
xvals = np.linspace(-4, 4, 9)
y1vals = linear_fun(a=2, b=5, x=xvals)
print(y1vals)
```

---


## 3. Defining a Quadratic Function

General quadratic function y = ax² + bx + c

```python
def quad_fun(x, a, b, c):
    y = a * (x**2) + b * x + c
    return y

# Example: y = x² - 4x + 3
xvals = np.linspace(-2, 6, 17)
yvals = quad_fun(x=xvals, a=1, b=-4, c=3)
print(yvals)
```

---


## 4. Piecewise Function with if-else

Function with different rules for different domains

```python
def h(x):
    if (x >= 0) and (x < 4):
        result = 9
    elif (x >= 4) and (x < 10):
        result = 1 + 2*x
    else:
        result = 21
    return result

# Test values
for val in [0, 2, 4, 5, 7, 10, 12]:
    print(f"h({val}) = {h(val)}")
```

---


## 5. Reisser Depth-Integration Model

Calculates the correction ratio for ocean plastic sampling

```python
def CiCsRatio_fun(d, alpha=0.4):
    """Calculate depth-integration correction ratio.
    
    Args:
        d: immersion depth in metres (must be > 0)
        alpha: parameter (default 0.4 m^-1)
    
    Returns:
        Correction ratio Ci/Cs
    """
    ratio = 1 / (1 - np.exp(-alpha * d))
    return ratio

# Calculate for different depths
d_values = np.array([0.1, 0.17, 0.3, 1.0])
for d in d_values:
    print(f"R({d}) = {CiCsRatio_fun(d):.2f}")
```

---

## 6. Plotting the Reisser Model

Visualize how correction ratio changes with depth

```python
# Create depth values (avoid d=0 where function is undefined)
d = np.linspace(0.05, 2.0, 40)

# Calculate correction ratios
cdf = pd.DataFrame()
cdf['d'] = d
cdf['CiCsRatio'] = CiCsRatio_fun(d)

# Plot
cdf.plot(x='d', y='CiCsRatio', 
         title='Correction Ratio vs Sampling Depth',
         xlabel='Depth (m)',
         ylabel='Ci/Cs Ratio',
         legend=False,
         grid=True)
plt.show()
```

---


## 7. Loading Global Plastics Data

Read and explore the production dataset

```python
# Read the CSV file from GitHub (works on Google Colab too)
url = "https://raw.githubusercontent.com/ahailu95/scie1500-content/main/SCIE1500Materials/Week_1/LabFiles/global-plastics-production.csv"
gpp = pd.read_csv(url)

# Explore the data
print(gpp.info())
print(gpp.head())
print(gpp.tail())
```

---

## 8. Creating Derived Variables

Add time trend and convert units

```python
# Create time trend (t = 1 for 1950)
gpp['t'] = gpp['Year'] - 1949

# Convert to million metric tonnes
gpp['GPP (MMT)'] = gpp['GPP (MT)'] / 1_000_000

# Check results
print(gpp[['Year', 't', 'GPP (MT)', 'GPP (MMT)']].head())
```

---

## 9. Plotting Global Plastic Production

Time series plot of production data

```python
gpp.plot(x='Year', 
         y='GPP (MMT)',
         title='Global Plastic Production (1950-2015)',
         xlabel='Year',
         ylabel='Production (Million Metric Tonnes)',
         kind='line',
         grid=True,
         color='red',
         legend=False)

plt.tight_layout()
plt.show()
```

---


## 10. Plotting Multiple Linear Functions

Compare different linear equations on one chart

```python
# Create x values
xvals = np.linspace(-4, 4, 9)

# Calculate y values for different equations
y1vals = linear_fun(a=2, b=5, x=xvals)   # y = 2x + 5
y2vals = linear_fun(a=2, b=0, x=xvals)   # y = 2x
y3vals = linear_fun(a=-3, b=4, x=xvals)  # y = -3x + 4

# Create DataFrame
df = pd.DataFrame()
df['x'] = xvals
df['y = 2x + 5'] = y1vals
df['y = 2x'] = y2vals
df['y = -3x + 4'] = y3vals

# Plot all three
df.plot(x='x', 
        y=['y = 2x + 5', 'y = 2x', 'y = -3x + 4'],
        title='Plot of Three Linear Equations',
        xlabel='x',
        ylabel='y',
        kind='line',
        grid=True,
        legend=True)
plt.show()
```

---


## 11. Plotting Quadratic Functions

Compare different quadratic equations

```python
# Create x values
xvals = np.linspace(-10, 10, 25)

# Create DataFrame
df = pd.DataFrame()
df['x'] = xvals

# Calculate y values for different quadratics
df['y1'] = quad_fun(x=xvals, a=1, b=-1, c=-2)    # Opens up
df['y2'] = quad_fun(x=xvals, a=-2, b=0, c=150)   # Opens down
df['y3'] = quad_fun(x=xvals, a=3, b=2, c=-50)    # Opens up

# Plot
df.plot(x='x', 
        y=['y1', 'y2', 'y3'],
        title='Comparison of Quadratic Functions',
        xlabel='x',
        ylabel='y',
        kind='line',
        grid=True,
        legend=True)
plt.show()
```

---


## 12. Finding Quadratic Vertex

Calculate vertex of a parabola

```python
def find_vertex(a, b, c):
    """Find vertex of quadratic y = ax² + bx + c
    
    Returns:
        (x_vertex, y_vertex)
    """
    x_v = -b / (2 * a)
    y_v = a * x_v**2 + b * x_v + c
    return (x_v, y_v)

# Example: E(t) = -0.5t² + 4t + 2
a, b, c = -0.5, 4, 2
vertex = find_vertex(a, b, c)
print(f"Vertex: ({vertex[0]}, {vertex[1]})")
```

---

## 13. Quadratic Formula

Find roots of a quadratic equation

```python
def quadratic_formula(a, b, c):
    """Solve ax² + bx + c = 0
    
    Returns:
        Tuple of roots, or message if no real roots
    """
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

# Example: -0.5t² + 4t + 2 = 0
a, b, c = -0.5, 4, 2
roots = quadratic_formula(a, b, c)
print(f"Roots: {roots}")
```

---


## 14. Evaluating a Function at Multiple Points

Function evaluation with numpy arrays

```python
def f(x):
    """f(x) = sqrt(x - 1)"""
    return np.sqrt(x - 1)

# Evaluate at specific points
test_points = np.array([1, 2, 5, 10, 17])
results = f(test_points)

# Display results
for x, y in zip(test_points, results):
    print(f"f({x}) = {y}")
```

---

