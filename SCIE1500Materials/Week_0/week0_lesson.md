# Week 0: Mathematical Foundations & Python Basics

## SCIE1500 — Analytical Methods for Scientists
### The Scientist's Toolkit: Preparing for Quantitative Analysis

---

## Welcome

Before we dive into the mathematical models that scientists use to understand the world—from ocean pollution to fish populations to climate systems—we need to ensure everyone has a solid foundation in the essential mathematical tools.

This week is a **diagnostic review**. If you find the material straightforward, excellent—you're ready for the challenges ahead. If you find gaps in your knowledge, now is the time to address them before the pace increases.

**By the end of this week, you should be comfortable with:**
- The number systems scientists use
- Order of operations (BODMAS)
- Exponents and radicals
- Algebraic manipulation
- Solving equations and inequalities
- Scientific notation and unit conversions
- Function notation (what $f(x)$ actually means)
- Interval notation for domains and ranges
- Basic Python for calculations and plotting

---

## 1. Real Numbers and Number Sets

Scientists work with different types of numbers, and understanding their relationships helps avoid errors.

### The Number Set Hierarchy

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

| Symbol | Name | Description | Examples |
|--------|------|-------------|----------|
| $\mathbb{N}$ | Natural numbers | Counting numbers | 1, 2, 3, 4, ... |
| $\mathbb{Z}$ | Integers | Whole numbers (positive, negative, zero) | ..., -2, -1, 0, 1, 2, ... |
| $\mathbb{Q}$ | Rational numbers | Fractions of integers | $\frac{1}{2}$, $-\frac{3}{4}$, 0.75, $2.\overline{3}$ |
| $\mathbb{R}$ | Real numbers | All points on the number line | $\pi$, $\sqrt{2}$, $e$, -4.7 |

**Key insight:** Every natural number is an integer, every integer is rational, and every rational number is real. But not every real number is rational—numbers like $\pi$ and $\sqrt{2}$ are **irrational** (cannot be expressed as a fraction).

### Set Notation

Scientists often need to describe collections of numbers:

| Notation | Meaning | Example |
|----------|---------|---------|
| $\{1, 2, 3\}$ | A set containing exactly these elements | $\{1, 2, 3\}$ |
| $\{x : x > 0\}$ | "The set of all x such that x is greater than 0" | All positive numbers |
| $\{x \in \mathbb{Z} : x > 0\}$ | "All integers x such that x is greater than 0" | $\{1, 2, 3, 4, ...\}$ |
| $\emptyset$ or $\{\}$ | The empty set | No elements |

---

## 2. Order of Operations (BODMAS/PEMDAS)

When an expression contains multiple operations, the order matters.

### BODMAS Rule

| Letter | Operation | Priority |
|--------|-----------|----------|
| **B** | Brackets (parentheses) | Highest |
| **O** | Orders (exponents, roots) | ↓ |
| **D** | Division | ↓ |
| **M** | Multiplication | ↓ |
| **A** | Addition | ↓ |
| **S** | Subtraction | Lowest |

**Note:** Division and Multiplication have equal priority (evaluate left to right). Same for Addition and Subtraction.

### Examples

**Example 1:** $3 + 4 \times 2$

- Multiplication first: $4 \times 2 = 8$
- Then addition: $3 + 8 = 11$
- **Answer:** 11 (not 14)

**Example 2:** $(3 + 4) \times 2$

- Brackets first: $3 + 4 = 7$
- Then multiplication: $7 \times 2 = 14$
- **Answer:** 14

**Example 3:** $2^3 + 4 \times 5 - 10 \div 2$

- Exponent: $2^3 = 8$
- Multiplication: $4 \times 5 = 20$
- Division: $10 \div 2 = 5$
- Left to right: $8 + 20 - 5 = 23$
- **Answer:** 23

### Python Follows BODMAS

```python
# Python respects order of operations
print(3 + 4 * 2)      # Output: 11
print((3 + 4) * 2)    # Output: 14
print(2**3 + 4*5 - 10/2)  # Output: 23.0
```

---

## 3. Exponents and Radicals

Exponents (powers) and radicals (roots) appear throughout scientific models.

### Exponent Rules

| Rule | Formula | Example |
|------|---------|---------|
| Product rule | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7 = 128$ |
| Quotient rule | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{5^6}{5^2} = 5^4 = 625$ |
| Power rule | $(a^m)^n = a^{mn}$ | $(3^2)^4 = 3^8 = 6561$ |
| Zero exponent | $a^0 = 1$ (for $a \neq 0$) | $7^0 = 1$ |
| Negative exponent | $a^{-n} = \frac{1}{a^n}$ | $2^{-3} = \frac{1}{8}$ |
| Fractional exponent | $a^{1/n} = \sqrt[n]{a}$ | $8^{1/3} = \sqrt[3]{8} = 2$ |
| General fractional | $a^{m/n} = \sqrt[n]{a^m}$ | $4^{3/2} = \sqrt{4^3} = 8$ |

### Radical Rules

| Rule | Formula | Example |
|------|---------|---------|
| Product | $\sqrt{ab} = \sqrt{a} \cdot \sqrt{b}$ | $\sqrt{12} = \sqrt{4 \cdot 3} = 2\sqrt{3}$ |
| Quotient | $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ | $\sqrt{\frac{9}{16}} = \frac{3}{4}$ |
| Power | $\sqrt{a^2} = |a|$ | $\sqrt{(-3)^2} = 3$ |

### Python Syntax for Exponents

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

## 4. Algebraic and Rational Expressions

### Algebraic Expressions

An algebraic expression combines numbers, variables, and operations.

**Simplifying by combining like terms:**

$$3x^2 + 5x - 2x^2 + 7 - 3x = (3-2)x^2 + (5-3)x + 7 = x^2 + 2x + 7$$

**Expanding brackets:**

$$(a + b)(c + d) = ac + ad + bc + bd$$

**Example:** $(2x + 3)(x - 4) = 2x^2 - 8x + 3x - 12 = 2x^2 - 5x - 12$

### Factoring Common Patterns

| Pattern | Formula |
|---------|---------|
| Difference of squares | $a^2 - b^2 = (a+b)(a-b)$ |
| Perfect square | $a^2 + 2ab + b^2 = (a+b)^2$ |
| Perfect square | $a^2 - 2ab + b^2 = (a-b)^2$ |

**Example:** Factor $x^2 - 9$
- Recognize: $x^2 - 9 = x^2 - 3^2$
- Apply difference of squares: $(x+3)(x-3)$

### Rational Expressions

A rational expression is a fraction with polynomials in the numerator and/or denominator.

**Simplifying:** Factor and cancel common terms.

$$\frac{x^2 - 4}{x + 2} = \frac{(x+2)(x-2)}{x+2} = x - 2 \quad \text{(for } x \neq -2\text{)}$$

**Important:** Always note restrictions! The original expression is undefined at $x = -2$.

---

## 5. Equations

An equation states that two expressions are equal. Solving means finding the value(s) that make it true.

### Linear Equations

Form: $ax + b = c$

**Strategy:** Isolate the variable.

**Example:** Solve $3x + 7 = 22$
1. Subtract 7: $3x = 15$
2. Divide by 3: $x = 5$

### Quadratic Equations

Form: $ax^2 + bx + c = 0$

**Methods:**
1. **Factoring** (when possible)
2. **Quadratic formula:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

**Example:** Solve $x^2 - 5x + 6 = 0$
- Factor: $(x-2)(x-3) = 0$
- Solutions: $x = 2$ or $x = 3$

**Example:** Solve $2x^2 + 3x - 5 = 0$
- Use quadratic formula with $a=2$, $b=3$, $c=-5$
- $x = \frac{-3 \pm \sqrt{9 + 40}}{4} = \frac{-3 \pm 7}{4}$
- Solutions: $x = 1$ or $x = -2.5$

### The Discriminant

The expression $b^2 - 4ac$ (under the square root) determines the nature of solutions:

| Discriminant | Meaning |
|--------------|---------|
| $b^2 - 4ac > 0$ | Two distinct real solutions |
| $b^2 - 4ac = 0$ | One repeated real solution |
| $b^2 - 4ac < 0$ | No real solutions (complex only) |

---

## 6. Inequalities

Inequalities compare expressions using $<$, $>$, $\leq$, $\geq$.

### Solving Linear Inequalities

**Rules:**
- Add/subtract the same quantity to both sides: inequality preserved
- Multiply/divide by a **positive** number: inequality preserved
- Multiply/divide by a **negative** number: **inequality reverses**

**Example:** Solve $-2x + 5 > 11$
1. Subtract 5: $-2x > 6$
2. Divide by $-2$ (reverse inequality!): $x < -3$

**Solution:** $x < -3$ or $(-\infty, -3)$

### Compound Inequalities

**Example:** Solve $-3 \leq 2x + 1 < 7$
1. Subtract 1 from all parts: $-4 \leq 2x < 6$
2. Divide by 2: $-2 \leq x < 3$

**Solution:** $-2 \leq x < 3$ or $[-2, 3)$

---

## 7. Scientific Notation and Unit Conversions

### Scientific Notation

Large and small numbers are written as: $a \times 10^n$ where $1 \leq |a| < 10$

| Number | Scientific Notation |
|--------|-------------------|
| 4,500,000 | $4.5 \times 10^6$ |
| 0.00032 | $3.2 \times 10^{-4}$ |
| 381,000,000 (tonnes) | $3.81 \times 10^8$ tonnes |

**Operations:**
- Multiply: $(2 \times 10^3)(3 \times 10^4) = 6 \times 10^7$
- Divide: $\frac{8 \times 10^5}{2 \times 10^2} = 4 \times 10^3$

### Unit Conversions

Scientists constantly convert between units.

**Example:** Convert 381,000,000 metric tonnes to million metric tonnes (MMT)

$$381,000,000 \text{ MT} = \frac{381,000,000}{1,000,000} \text{ MMT} = 381 \text{ MMT}$$

**Example:** Convert 5.1 kg/person/day to grams/person/day

$$5.1 \text{ kg/person/day} \times \frac{1000 \text{ g}}{1 \text{ kg}} = 5100 \text{ g/person/day}$$

### Python for Scientific Notation

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

## 8. Function Notation: What $f(x)$ Actually Means

This is crucial preparation for Week 1 and beyond.

### The Meaning of $f(x)$

When we write $f(x) = 2x + 3$, we're defining a **rule** called $f$ that takes an input $x$ and produces an output.

**$f(x)$ does NOT mean "$f$ times $x$"!**

It means "the function $f$ evaluated at the value $x$."

### Evaluating Functions

If $f(x) = 2x + 3$:
- $f(5) = 2(5) + 3 = 13$ (input 5, output 13)
- $f(-2) = 2(-2) + 3 = -1$ (input -2, output -1)
- $f(a) = 2a + 3$ (input $a$, output $2a + 3$)
- $f(x+1) = 2(x+1) + 3 = 2x + 5$ (input $x+1$, output $2x+5$)

### Multiple Functions

We can have several functions with different names:
- $f(x) = x^2$
- $g(x) = 3x - 1$
- $h(t) = 5t + 2$ (using $t$ as the variable)

Then:
- $f(3) = 9$
- $g(3) = 8$
- $h(3) = 17$

### Python Functions Mirror Mathematical Functions

```python
# Define a function
def f(x):
    return 2*x + 3

# Evaluate it
print(f(5))     # 13
print(f(-2))    # -1
print(f(0))     # 3
```

This direct parallel between mathematical notation and Python code is why learning Python helps reinforce mathematical understanding.

---

## 9. Interval Notation

In Week 1, you'll describe **domains** (valid inputs) and **ranges** (possible outputs) of functions. Interval notation is the standard way to do this.

### Types of Intervals

| Interval | Notation | Meaning | Number Line |
|----------|----------|---------|-------------|
| Closed | $[a, b]$ | $a \leq x \leq b$ | ●────● |
| Open | $(a, b)$ | $a < x < b$ | ○────○ |
| Half-open (left) | $(a, b]$ | $a < x \leq b$ | ○────● |
| Half-open (right) | $[a, b)$ | $a \leq x < b$ | ●────○ |
| Infinite | $[a, \infty)$ | $x \geq a$ | ●────→ |
| Infinite | $(-\infty, b)$ | $x < b$ | ←────○ |
| All reals | $(-\infty, \infty)$ | All $x \in \mathbb{R}$ | ←────→ |

**Key points:**
- Square bracket $[$ or $]$ means **included** (≤ or ≥)
- Round bracket $($ or $)$ means **excluded** (< or >)
- Infinity ($\infty$) always uses round brackets (you can't "reach" infinity)

### Examples

- "All numbers from 0 to 10, including both endpoints" → $[0, 10]$
- "All positive numbers" → $(0, \infty)$
- "All numbers less than or equal to 5" → $(-\infty, 5]$
- "All numbers except 3" → $(-\infty, 3) \cup (3, \infty)$

---

## 10. Why This Matters: Equations in Scientific Modelling

Everything you've reviewed connects to real scientific work. Here's a preview of how equations model the natural world.

### The Temperature Conversion Model

The relationship between Fahrenheit and Celsius temperatures:

$$C = \frac{5}{9}(F - 32)$$

This is a **linear equation**. Given any Fahrenheit value, we can compute the Celsius equivalent. In Python:

```python
def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)
```

### The Ocean Plastic Crisis

Scientists estimate that **4.8 to 12.7 million metric tonnes** of plastic entered the oceans in 2010 alone (Jambeck et al., 2015). To model this, they use:

- **Linear equations** to describe simple relationships
- **Quadratic equations** to model growth rates (like fish populations)
- **Exponential equations** to model accelerating growth (like plastic production)

The production of plastic has grown from 2 million tonnes in 1950 to 381 million tonnes in 2015—an increase of over 190×. This is clearly not linear growth.

### Coming Up: Bounded Growth Models

In **Week 3**, you'll encounter the **Schaefer fish growth model** — an elegant equation that uses quadratics to describe how fish populations grow when limited by their environment. Everything you've reviewed this week — BODMAS, fractions, algebraic manipulation, quadratics — prepares you to work with models like this.

---

## 11. Week 0 Lab: Python Basics (Week0_Intro_Python.ipynb)

The lab notebook this week introduces you to Python through hands-on exercises. Here's what you'll cover:

### Section 0: Warmup
- Using Python as a calculator
- Temperature conversion example
- Creating arrays with numpy
- Basic plotting with matplotlib
- **Exercise A:** Plot leaf area vs. leaf weight

### Sections 1-2: Python Fundamentals
- Jupyter Notebook environment
- Python syntax (case sensitivity, comments, whitespace)
- Variable naming conventions
- Indentation for code blocks
- **Exercises B, C:** Calculations and fixing syntax errors

### Section 3: Data Types
- Integers, floats, strings, booleans
- Lists, tuples, arrays
- Type conversion (casting)
- User input

### Section 4: Operators
- Arithmetic: `+`, `-`, `*`, `/`, `**`, `%`, `//`
- Assignment: `=`, `+=`, `-=`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- **Exercises D, E:** Operator precedence

### Section 5-6: Help and Modules
- Using `help()` function
- Importing `math` module
- Constants: `math.pi`, `math.e`
- Functions: `math.sqrt()`, `math.exp()`, `math.log()`
- Importing `numpy` for arrays
- `np.array()`, `np.linspace()`
- **Exercise F:** Creating arrays with linspace
- **Exercise G:** 2D arrays and transposition

### Section 7: Plotting
- Using matplotlib.pyplot
- Line plots, labels, titles, grids
- **Exercises H, I:** Plotting a parabola

---

## Key Formulas Summary

| Topic | Formula/Notation |
|-------|-----------------|
| Exponent product | $a^m \cdot a^n = a^{m+n}$ |
| Exponent quotient | $a^m / a^n = a^{m-n}$ |
| Negative exponent | $a^{-n} = 1/a^n$ |
| Fractional exponent | $a^{1/n} = \sqrt[n]{a}$ |
| Quadratic formula | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ |
| Closed interval | $[a,b]$ means $a \leq x \leq b$ |
| Open interval | $(a,b)$ means $a < x < b$ |
| Function notation | $f(x)$ means "f evaluated at x" |

---

## Self-Assessment Checklist

Before moving to Week 1, ensure you can:

- [ ] Identify which number set a given number belongs to
- [ ] Apply BODMAS correctly to evaluate expressions
- [ ] Use exponent and radical rules to simplify expressions
- [ ] Expand and factor algebraic expressions
- [ ] Solve linear equations
- [ ] Solve quadratic equations (by factoring and by formula)
- [ ] Solve linear inequalities (remembering to flip when dividing by negative)
- [ ] Convert between standard and scientific notation
- [ ] Evaluate a function like $f(x) = 3x^2 - 2$ at specific values
- [ ] Write intervals in correct notation (e.g., $[0, \infty)$)
- [ ] Write and run basic Python code for calculations
- [ ] Create numpy arrays and use linspace
- [ ] Make simple plots with matplotlib

If you're unsure about any of these, revisit the relevant section or ask for help before Week 1.

---

## References

- Jambeck, J.R., et al. (2015). Plastic waste inputs from land into the ocean. *Science*, 347(6223), 768-771.

---

*Next: Week 1 — Functions and the Language of Scientific Analysis*
