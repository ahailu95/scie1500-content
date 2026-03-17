<?xml version="1.0" encoding="UTF-8"?>
# Python Code Snippets - Mathematical Foundations

**Copy-ready Python code examples for Week 0**

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
```

---

## 1. BODMAS - Order of Operations

Python follows the same order of operations as mathematics

```python
# Python follows BODMAS
print(3 + 4 * 2)      # Output: 11
print((3 + 4) * 2)    # Output: 14
print(2**3 + 4*5 - 10/2)  # Output: 23.0
```

---


## 2. Exponentiation

Using ** for powers and math.sqrt() for roots

```python
import math

# Exponentiation
print(2 ** 3)           # 8 (2 to the power 3)
print(math.pow(2, 3))   # 8.0 (returns float)

# Square root
print(math.sqrt(16))    # 4.0
print(16 ** 0.5)        # 4.0 (alternative)

# Cube root
print(27 ** (1/3))      # 3.0

# Negative exponent
print(2 ** -3)          # 0.125 (= 1/8)
```

---


## 3. Scientific Notation

Working with large and small numbers

```python
# Scientific notation in Python
large = 3.81e8    # 3.81 × 10^8
small = 3.2e-4    # 3.2 × 10^-4

print(large)      # 381000000.0
print(small)      # 0.00032

# Unit conversion
tonnes = 381000000
mmt = tonnes / 1_000_000  # Using underscore for readability
print(f"{mmt} MMT")       # 381.0 MMT
```

---


## 4. Defining and Evaluating Functions

Python functions mirror mathematical functions

```python
# Define a function
def f(x):
    return 2*x + 3

# Evaluate it
print(f(5))     # 13
print(f(-2))    # -1
print(f(0))     # 3
```

---

## 5. Quadratic Function

Defining and evaluating a quadratic

```python
# Quadratic function: f(x) = 3x² - 2x + 1
def f(x):
    return 3*x**2 - 2*x + 1

# Evaluate at different points
print(f"f(2) = {f(2)}")    # f(2) = 9
print(f"f(-1) = {f(-1)}")  # f(-1) = 6
print(f"f(0) = {f(0)}")    # f(0) = 1
```

---


## 6. Import Statements

Standard imports for SCIE1500 notebooks

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
```

---


## 7. Creating Arrays with NumPy

Creating arrays manually and with linspace

```python
import numpy as np

# Create array manually
Ftemps = np.array([0, 68, 97, 112, 134])
print(Ftemps)

# Create equally spaced values
x = np.linspace(0, 10, 5)  # 5 values from 0 to 10
print(x)  # [0, 2.5, 5, 7.5, 10]

# Exclude endpoint
x2 = np.linspace(0, 10, 5, endpoint=False)
print(x2)  # [0, 2, 4, 6, 8]
```

---


## 8. Array Operations

Applying formulas to entire arrays

```python
import numpy as np

# Temperature conversion (applies to all elements)
Ftemps = np.array([0, 68, 97, 112, 134])
Ctemps = (Ftemps - 32) * (5/9)

print(np.round(Ctemps, 2))  # [-17.78, 20.0, 36.11, 44.44, 56.67]
```

---


## 9. Basic Plotting

Creating a simple line plot

```python
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.linspace(-8, 8, 33)
y = -0.4 * x**2 + 0.5 * x + 12

# Create plot
plt.plot(x, y, '-b')
plt.title("Parabola: $y = -0.4x^2 + 0.5x + 12$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()
```

---


## 10. Scatter Plot with Formatting

Plotting data points with markers

```python
import matplotlib.pyplot as plt

# Data
Ftemps = [0, 68, 97, 112, 134]
Ctemps = [-17.78, 20.0, 36.11, 44.44, 56.67]

# Plot with red dashed line and circle markers
plt.plot(Ftemps, Ctemps, '--ro')
plt.title("Temperature Conversion")
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.grid()
plt.show()
```

---


## 11. Math Module Constants and Functions

Using mathematical constants and functions

```python
import math

# Constants
print(f"π = {math.pi}")
print(f"e = {math.e}")

# Functions
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"e^1 = {math.exp(1)}")
print(f"ln(10) = {math.log(10)}")
print(f"log10(100) = {math.log10(100)}")
print(f"sin(π/2) = {math.sin(math.pi/2)}")
```

---


## 12. Comparison and Logical Operators

Boolean operations in Python

```python
x = 5
y = 3

# Comparison operators
print(x > y)    # True
print(x == y)   # False
print(x != y)   # True
print(x >= 5)   # True

# Logical operators
print((x > 3) and (y < 5))  # True
print((x > 10) or (y < 5))  # True
print(not(x == y))          # True
```

---

## 13. Floor Division and Modulus

Integer division and remainders

```python
# Regular division
print(17 / 5)   # 3.4

# Floor division (integer part)
print(17 // 5)  # 3

# Modulus (remainder)
print(17 % 5)   # 2

# Verification: 17 = 5 * 3 + 2
print(5 * (17 // 5) + (17 % 5))  # 17
```

---


## 14. 2D Arrays and Transpose

Working with tables of data

```python
import numpy as np

# Create 2D array (rows: quantity, price, expenditure)
quantity = np.array([3, 2, 5])
price = np.array([4, 6, 9])
expenditure = quantity * price

jack_data = np.array([quantity, price, expenditure])
print("Before transpose:")
print(jack_data)

# Transpose (items in rows, values in columns)
jack_data = jack_data.transpose()
print("\nAfter transpose:")
print(jack_data)
```

---

