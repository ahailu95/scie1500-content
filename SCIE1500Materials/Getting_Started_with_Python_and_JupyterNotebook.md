# Getting Started with Python and Jupyter Notebook

**SCIE1500 — Analytical Methods for Scientists**

*Atakelty Hailu, University of Western Australia*

---

## 1. Introduction

This unit uses **Python**, a general-purpose programming language widely adopted in science, engineering, and data analysis. Unlike specialised statistical software, Python combines readability with powerful libraries for numerical computation (`numpy`), data manipulation (`pandas`), symbolic mathematics (`sympy`), and visualisation (`matplotlib`). These libraries extend Python's base capabilities much the way add-on packages extend R.

You will write and run Python code inside **Jupyter Notebook**, an interactive environment that lets you weave documentation (text, equations, images), code, and results into a single document — a `.ipynb` file. Jupyter Notebook is to Python roughly what RStudio is to R: a user-friendly front end that reduces frustration and increases productivity.

### 1.1 Two Ways to Run Jupyter Notebook

You have two options, and both work identically for this unit:

| | **Miniconda / Anaconda (Local)** | **Google Colab (Cloud)** |
|---|---|---|
| **What it is** | A Python distribution installed on your computer. **Miniconda** is a lightweight version (~200 MB) that includes Python, conda, and pip. **Anaconda** is the full distribution (~3 GB) with hundreds of extra packages you probably won't need. | A free, browser-based Jupyter environment hosted by Google |
| **Pros** | Works offline; full control over packages; faster for large files | Zero installation; works on any device with a browser; easy sharing via Google Drive |
| **Cons** | Miniconda: ~200 MB + packages you install; Anaconda: ~3 GB disk space | Needs internet; sessions timeout after inactivity |
| **Best for** | Regular use on your own laptop | Quick access, Chromebooks, or when you cannot install software |

**Recommendation:** We recommend **Miniconda** — it is lightweight, fast to install, and includes everything you need to run Jupyter and install the packages used in this unit. Use Google Colab as a backup or for working on shared devices. Full Anaconda also works but is much larger and includes many packages you will not use.

### 1.2 Installing Miniconda (Recommended)

1. Go to [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/)
2. Download the installer for your operating system (Windows, macOS, or Linux)
3. Run the installer, accepting the default options
4. Open a terminal (or **Anaconda Prompt** on Windows) and install Jupyter:
   ```
   conda install jupyter numpy matplotlib pandas
   ```
5. Launch Jupyter Notebook by typing:
   ```
   jupyter notebook
   ```

> **Already have Anaconda?** That works too — Anaconda already includes Jupyter and all the packages above. Launch it from Anaconda Navigator or the terminal.

With either Miniconda or Anaconda, you get `conda` — a package manager that makes installing additional packages easy (e.g. `conda install sympy`).

### 1.3 Using Google Colab

1. Go to [https://colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Click **New Notebook** or upload a `.ipynb` file from your computer
4. Colab comes with `numpy`, `matplotlib`, `pandas`, and `sympy` pre-installed

### 1.4 The Learning Curve

With sustained effort, Python is straightforward to learn — especially if you focus on the subset of the language we use in this unit. Start early in the semester, build your knowledge gradually, and remember: the investment pays off well beyond this course. Previous experience shows that students who feel lost in the first week become confident users by mid-semester.

---

## 2. The Jupyter Notebook Environment

When you open a Jupyter Notebook, you see an interface with **cells**. There are two main cell types:

- **Code cells:** Where you write and run Python instructions. Press `Shift+Enter` (or click **Run**) to execute. Output appears directly below the cell.
- **Markdown cells:** Where you write text, equations (using LaTeX: `$f(x) = x^2$`), and insert images. Press `Shift+Enter` to render.

A new cell is a Code cell by default. Change it to Markdown using the dropdown menu in the toolbar.

### 2.1 Setting Up a Working Directory

Organise your files sensibly. A recommended structure:

```
Documents/
  └── SCIE1500/
        ├── Week_0/
        │     └── Week0_Intro_Python.ipynb
        ├── Week_1/
        │     └── Week1_Functions_Complete.ipynb
        └── Week_2/
              └── Week2_Exponential_Logarithmic.ipynb
```

In Jupyter Notebook (Miniconda or Anaconda), navigate to your folder using the file browser that opens in your web browser when you launch the application. In Colab, upload notebooks or connect to Google Drive.

### 2.2 Quick Test

Open a notebook and type the following in a code cell, then press `Shift+Enter`:

```python
2 + 2
```

You should see `4` as the output. Congratulations — you have just run your first Python instruction.

---

## 3. Python Basics

### 3.1 Python as a Calculator

```python
2 + 2          # addition → 4
2 * 3          # multiplication → 6
9 ** 2         # exponentiation (9²) → 81
2 ** 0.5       # square root of 2 → 1.4142...
```

### 3.2 Variables and Assignment

Store values in variables using `=`:

```python
product = 2 * 3
print(product)          # → 6
```

### 3.3 Comments

Everything after `#` on a line is a comment — ignored by Python but essential for documenting your code:

```python
# This is a comment
x = 5    # This is an inline comment
```

### 3.4 Functions Use Parentheses

Python functions work like $f(x)$ in algebra — arguments go inside parentheses:

```python
print(3 ** 2)           # Correct ✓
print 3**2              # Wrong ✗ — SyntaxError
```

### 3.5 Case Sensitivity

Python is case-sensitive: `print` works, `Print` does not. Jupyter highlights recognised commands in colour — if a word you typed is not highlighted, check for typos or case errors.

### 3.6 Data Types

| Type | Example | Check with `type()` |
|------|---------|---------------------|
| Integer | `x = 5` | `int` |
| Float | `x = 5.0` | `float` |
| String | `x = "hello"` | `str` |
| Boolean | `x = True` | `bool` |
| List | `x = [1, 2, 3]` | `list` |

```python
x = 3.14
type(x)       # → float
```

### 3.7 Operators

| Category | Operators | Example |
|----------|-----------|---------|
| Arithmetic | `+  -  *  /  **  //  %` | `7 // 2 → 3` (floor division), `7 % 2 → 1` (remainder) |
| Comparison | `==  !=  >  <  >=  <=` | `5 > 3 → True` |
| Logical | `and  or  not` | `(5 > 3) and (2 < 1) → False` |
| Assignment | `=  +=  -=  *=` | `x += 1` is shorthand for `x = x + 1` |

**Precedence** follows standard mathematical rules (BODMAS/PEMDAS). When in doubt, use parentheses.

### 3.8 Indentation Defines Code Blocks

Unlike R (which uses `{}`), Python uses **indentation** to define blocks of code inside `if`, `for`, `while`, and function definitions:

```python
x = 2
if x > 0:
    print("positive")    # indented = inside the if block
else:
    print("non-positive")
```

---

## 4. Importing Modules and Key Packages

Python's strength lies in its ecosystem. Import packages using `import`:

```python
import math                       # standard math library
import numpy as np                # numerical arrays — alias 'np'
import matplotlib.pyplot as plt   # plotting — alias 'plt'
%matplotlib inline                # display plots inline in Jupyter
```

> **Note:** From Week 4 onward, you will also use `import sympy as sp` for symbolic mathematics (derivatives, integrals, equation solving). You do not need it for the first few weeks.

### 4.1 The `math` Module — Constants and Functions

```python
import math
math.pi          # → 3.141592653589793
math.e           # → 2.718281828459045 (Euler's number)
math.sqrt(2)     # → 1.4142135623730951
math.log(10)     # → 2.302585... (natural log, base e)
math.log10(10)   # → 1.0 (base-10 log)
```

### 4.2 NumPy — Arrays and Vectorised Operations

NumPy lets you work with entire arrays at once, just as you would in R:

```python
import numpy as np

# Create an array
temps_F = np.array([0, 68, 97, 112, 134])

# Vectorised conversion (applies to all elements simultaneously)
temps_C = (temps_F - 32) * (5/9)
print(np.round(temps_C, 2))    # → [-17.78  20.  36.11  44.44  56.67]
```

**Creating sequences of values:**

```python
# 50 equally spaced values from 0 to 10
x = np.linspace(0, 10, 50)

# Integers from 0 to 9
y = np.arange(0, 10)

# Integers with step size
z = np.arange(0, 20, 2)    # → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### 4.3 Matplotlib — Plotting

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2

plt.plot(x, y, 'r-', label='$y = x^2$')    # red solid line
plt.title("A Simple Parabola")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
```

### 4.4 Finding Help

```python
help(np.linspace)     # detailed documentation
np.linspace?          # quick help (Jupyter only)
dir(math)             # list everything in a module
```

---

## 5. Defining Your Own Functions

Starting from Week 0, you will define Python functions to represent scientific models. The syntax uses `def`:

```python
def fahrenheit_to_celsius(F):
    """Convert Fahrenheit to Celsius."""
    C = (F - 32) * (5/9)
    return C

# Use it
fahrenheit_to_celsius(68)    # → 20.0
```

Functions can take multiple arguments and be combined with NumPy:

```python
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

x = np.linspace(-5, 5, 100)
y = quadratic(x, -0.4, 0.5, 12)
plt.plot(x, y)
plt.show()
```

---

## 6. Working with Data — A Quick Preview

### 6.1 Lists vs Arrays

```python
# Python list (general-purpose)
names = ["Tom", "Tim", "Tiger"]

# NumPy array (numerical operations)
values = np.array([15, 22, 18, 26])
print(values.mean())    # → 20.25
print(values.std())     # → 3.9370...
```

### 6.2 Reading Data from Files (using Pandas)

```python
import pandas as pd

# Read a CSV file
df = pd.read_csv("data.csv")
df.head()            # show first 5 rows
df.describe()        # summary statistics
df.columns           # list column names
```

---

## 7. Common Mistakes and How to Avoid Them

| Mistake | Example | Fix |
|---------|---------|-----|
| Missing parentheses | `print "hello"` | `print("hello")` |
| Wrong case | `Print("hello")` | `print("hello")` |
| Wrong exponent operator | `2^3` | `2**3` (caret is XOR in Python) |
| Integer division surprise | `7/2 → 3.5` is fine in Python 3 | Use `7//2` if you want `3` |
| Indentation error | Mixing tabs and spaces | Use 4 spaces consistently |
| Forgetting to import | `np.array([1,2])` without `import numpy as np` | Add the import at the top |

---

## 8. Summary of Key Commands

| Task | Python | R Equivalent |
|------|--------|--------------|
| Print a value | `print(x)` | `print(x)` |
| Square root | `math.sqrt(x)` or `np.sqrt(x)` | `sqrt(x)` |
| Natural log | `math.log(x)` or `np.log(x)` | `log(x)` |
| Create a vector/array | `np.array([1,2,3])` | `c(1,2,3)` |
| Sequence of values | `np.linspace(0,10,50)` | `seq(0,10,length=50)` |
| Read CSV | `pd.read_csv("file.csv")` | `read.csv("file.csv")` |
| Plot | `plt.plot(x, y)` | `plot(x, y)` |
| Define a function | `def f(x): return x**2` | `f = function(x) x^2` |
| Get help | `help(func)` | `?func` or `help(func)` |
| List module contents | `dir(module)` | `ls("package:pkg")` |

---

## 9. Resources for Further Learning

**(A) W3Schools Python Tutorial:** A comprehensive, beginner-friendly tutorial covering all the basics and more. Work through the sections on variables, data types, operators, lists, and functions at [https://www.w3schools.com/python/](https://www.w3schools.com/python/).

**(B) NumPy for Beginners:** Official getting-started guide at [https://numpy.org/doc/stable/user/absolute_beginners.html](https://numpy.org/doc/stable/user/absolute_beginners.html). Covers arrays, indexing, and basic operations.

**(C) Matplotlib Tutorials:** Official tutorials at [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html). Start with "Pyplot tutorial" for the plotting style used in this unit.

**(D) SymPy Documentation:** For symbolic mathematics (derivatives, integrals, solving equations) from Week 4 onward: [https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html).

**(E) Pandas Getting Started:** For data manipulation: [https://pandas.pydata.org/docs/getting_started/index.html](https://pandas.pydata.org/docs/getting_started/index.html).

**(F) Google Colab Guide:** Introduction to using Colab notebooks: [https://colab.research.google.com/notebooks/intro.ipynb](https://colab.research.google.com/notebooks/intro.ipynb).

**(G) Miniconda Download & Documentation:** Lightweight Python installer (recommended): [https://docs.conda.io/projects/miniconda/](https://docs.conda.io/projects/miniconda/). For full Anaconda: [https://docs.anaconda.com/](https://docs.anaconda.com/).

**(H) Real Python:** High-quality tutorials on a wide range of topics: [https://realpython.com/](https://realpython.com/). Search for specific topics as you need them.

**(I) YouTube:** Search for "Python for beginners Jupyter Notebook" for video walkthroughs. Corey Schafer's Python tutorials are widely recommended.

**(J) Stack Overflow:** When you encounter an error, search for the error message at [https://stackoverflow.com/](https://stackoverflow.com/). Chances are someone has had the same problem.

The key is to **learn how to look for answers** — that skill will serve you well beyond this semester.
