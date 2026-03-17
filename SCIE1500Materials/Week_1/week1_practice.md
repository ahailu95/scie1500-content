# Week 1: Practice Questions

## Act I: Understanding Systems — Functions and Domains

> These questions reinforce the mathematical concepts from the lesson and connect to the lab exercises using the Jambeck et al. (2015) and Global Plastics Production datasets.

---

## Question 1: Domain Identification (MCQ — Exam Style)

**Context:** When modeling environmental systems, ensuring your function is defined for all relevant inputs is critical. A model that produces undefined or imaginary values is scientifically meaningless.

**Question:** In which of the following cases is the Domain (D) for the function **not** identified correctly?

**(a)** $y = 5 - 3x$, $D = \{x : x \in \mathbb{R}\}$

**(b)** $y = \frac{(3x + 6)^{1/2}}{4} - 1$, $D = \{x : x \in \mathbb{R}\}$

**(c)** $y = \frac{3}{2 - e^{-x}}$, $D = \{x \in \mathbb{R} : x \neq -\ln(2)\}$

**(d)** $y = e^{0.2x - 1}$, $D = \{x : x \in \mathbb{R}\}$

**(e)** None of the above

---

### Solution

**Answer: (b)**

Let's check each option:

**(a)** $y = 5 - 3x$ is a linear function with no restrictions. ✓ Domain is all real numbers.

**(b)** $y = \frac{(3x + 6)^{1/2}}{4} - 1$ contains a square root. 

We need $(3x + 6) \geq 0$, which gives $x \geq -2$.

The stated domain (all real numbers) is **INCORRECT** because values like $x = -3$ make the square root undefined.

**(c)** $y = \frac{3}{2 - e^{-x}}$ is undefined when $2 - e^{-x} = 0$, i.e., $e^{-x} = 2$.

Taking natural log: $-x = \ln(2)$, so $x = -\ln(2)$.

The exclusion $x \neq -\ln(2)$ is correct. ✓

**(d)** $y = e^{0.2x - 1}$ is exponential, defined for all real $x$. ✓

**Connection to Exam:** This directly mirrors MCQ Q10 on domain identification.

---

## Question 2: Function Evaluation and Domains

**Context:** The function $f(x) = \sqrt{x - 1}$ might model a relationship where measurements are only valid above a threshold value.

**(a)** Determine the domain of $f(x) = \sqrt{x - 1}$.

**(b)** Determine the range of $f(x) = \sqrt{x - 1}$.

**(c)** Calculate $f(2)$, $f(5)$, and $f(10)$.

**(d)** Find the value of $u$ if $f(u) = 4$.

**(e)** Why is $f(0)$ undefined?

---

### Solution

**(a)** For the square root to be defined: $x - 1 \geq 0 \Rightarrow x \geq 1$

**Domain:** $D = \{x \in \mathbb{R} : x \geq 1\}$ or equivalently $[1, \infty)$

**(b)** Since $\sqrt{x-1} \geq 0$ for all valid inputs, and can grow arbitrarily large:

**Range:** $R = \{y \in \mathbb{R} : y \geq 0\}$ or equivalently $[0, \infty)$

**(c)** 
- $f(2) = \sqrt{2-1} = \sqrt{1} = 1$
- $f(5) = \sqrt{5-1} = \sqrt{4} = 2$
- $f(10) = \sqrt{10-1} = \sqrt{9} = 3$

**(d)** If $f(u) = 4$, then $\sqrt{u - 1} = 4$

Squaring both sides: $u - 1 = 16$, so $u = 17$

**(e)** $f(0) = \sqrt{0 - 1} = \sqrt{-1}$, which is not a real number. The input $x = 0$ is outside the domain.

---

## Question 3: Quadratic Functions — Sketching and Analysis

**Context:** The cleanup efficiency of a plastic removal operation (tonnes removed per day) varies over time as easily accessible debris is collected first.

Suppose the efficiency function is:

$$E(t) = -0.5t^2 + 4t + 2$$

where $t$ is days since the operation began.

**(a)** What is the y-intercept? Interpret this in context.

**(b)** Find the vertex of this parabola. What does it represent?

**(c)** Find the x-intercepts (if they exist). What do they mean?

**(d)** Sketch the function for $t \geq 0$.

**(e)** What is a sensible domain for this model, and why?

---

### Solution

**(a)** Y-intercept: Set $t = 0$: $E(0) = -0.5(0) + 4(0) + 2 = 2$

**Interpretation:** On day 0, the cleanup operation removes 2 tonnes of plastic.

**(b)** Vertex x-coordinate: $t = -\frac{b}{2a} = -\frac{4}{2(-0.5)} = -\frac{4}{-1} = 4$

Vertex y-coordinate: $E(4) = -0.5(16) + 4(4) + 2 = -8 + 16 + 2 = 10$

**Vertex:** $(4, 10)$

**Interpretation:** Maximum efficiency occurs on day 4, when 10 tonnes per day are removed.

**(c)** X-intercepts: Set $E(t) = 0$:

$$-0.5t^2 + 4t + 2 = 0$$

Multiply by $-2$: $t^2 - 8t - 4 = 0$

Using the quadratic formula:

$$t = \frac{8 \pm \sqrt{64 + 16}}{2} = \frac{8 \pm \sqrt{80}}{2} = \frac{8 \pm 8.944}{2}$$

$t = 8.472$ or $t = -0.472$

**Interpretation:** Efficiency reaches zero around day 8.5 (the negative root is physically meaningless).

**(d)** Sketch should show:
- Y-intercept at $(0, 2)$
- Maximum at $(4, 10)$
- X-intercept near $(8.5, 0)$
- Parabola opening downward ($a < 0$)

**(e)** Sensible domain: $D = \{t \in \mathbb{R} : 0 \leq t \leq 8.472\}$

**Reasoning:** 
- $t \geq 0$ because time can't be negative
- $t \leq 8.472$ because efficiency can't be negative (you can't "un-remove" plastic)

---

## Question 4: Vertical Line Test and Function Identification

**Context:** The math lecture (Example 1.2) shows various curves and asks whether they represent functions.

For each relationship below, determine whether it defines $y$ as a function of $x$:

**(a)** $y^2 + 2x^2 = 1$

**(b)** $f(x) = x^2 + 4x + 3$

**(c)** $g(x) = \frac{1}{x}$

**(d)** $x^2 + y^2 = 1$ (circle)

---

### Solution

**(a)** $y^2 + 2x^2 = 1$ — **NOT a function**

Solving for $y$: $y^2 = 1 - 2x^2$, so $y = \pm\sqrt{1 - 2x^2}$

For $x = 0$: $y = \pm 1$ (two values)

**(b)** $f(x) = x^2 + 4x + 3$ — **IS a function**

This is a quadratic; each $x$ produces exactly one $y$.

**(c)** $g(x) = \frac{1}{x}$ — **IS a function** (for $x \neq 0$)

Each non-zero $x$ gives exactly one $y$.

**(d)** $x^2 + y^2 = 1$ — **NOT a function**

For $x = 0$: $y = \pm 1$. A vertical line at $x = 0$ intersects the circle twice.

---

## Question 5: Applied Data Analysis — Jambeck Dataset

**Context:** The Jambeck et al. (2015) data includes coastal population, waste generation rate, and mismanaged plastic waste for 20 countries. You work with this data in the lab.

The top 5 countries by mismanaged plastic waste (MMT/year) are:

| Rank | Country | Coastal Pop. (millions) | Waste Rate (kg/person/day) | Mismanaged Plastic (MMT/year) |
|------|---------|------------------------|---------------------------|------------------------------|
| 1 | China | 262.9 | 1.10 | 8.82 |
| 2 | Indonesia | 187.2 | 0.52 | 3.22 |
| 3 | Philippines | 83.4 | 0.50 | 1.88 |
| 4 | Vietnam | 55.9 | 0.79 | 1.83 |
| 5 | Sri Lanka | 14.6 | 5.10 | 1.59 |

**(a)** China has the largest coastal population and the most mismanaged plastic waste. Is the relationship between coastal population and mismanaged waste strictly linear across these 5 countries? How can you tell?

**(b)** Sri Lanka has the smallest coastal population but the highest waste generation rate. Calculate the total daily waste generated by Sri Lanka's coastal population (in million kg/day).

**(c)** If we define a function $W(P) = k \cdot P$ where $P$ is coastal population (millions) and $W$ is mismanaged plastic waste (MMT/year), what value of $k$ would fit China's data exactly?

**(d)** Using your value of $k$ from part (c), predict Indonesia's mismanaged plastic waste. How does this compare to the actual value? What does this suggest about the model?

---

### Solution

**(a)** **Not strictly linear.** 

If it were linear, the ratio of mismanaged waste to coastal population would be constant. Let's check:
- China: $8.82 / 262.9 = 0.0335$
- Indonesia: $3.22 / 187.2 = 0.0172$
- Philippines: $1.88 / 83.4 = 0.0225$

The ratios vary significantly, so population alone doesn't determine waste through a simple linear relationship. Other factors (waste generation rate, % mismanaged, % plastic) matter.

**(b)** Total daily waste for Sri Lanka:

$$\text{Daily waste} = \text{Population} \times \text{Rate} = 14.6 \times 5.10 = 74.46 \text{ million kg/day}$$

Or equivalently, $74,460$ tonnes/day.

**(c)** For China: $W = k \cdot P$ implies $8.82 = k \cdot 262.9$

$$k = \frac{8.82}{262.9} = 0.0335 \text{ MMT/year per million people}$$

**(d)** Predicted for Indonesia: $W = 0.0335 \times 187.2 = 6.27$ MMT/year

Actual value: $3.22$ MMT/year

**Discrepancy:** The simple linear model over-predicts by nearly 2× because Indonesia has a lower waste generation rate and different waste management characteristics than China. This suggests **a single-variable linear model is inadequate**—we need more sophisticated functions.

---

## Summary: What You Should Be Able To Do

After completing these exercises, you should be able to:

1. ✓ Identify whether a relationship defines a function (vertical line test)
2. ✓ Determine domains from mathematical constraints (square roots, fractions)
3. ✓ Determine domains from physical/scientific constraints
4. ✓ Sketch quadratic functions and find key features (vertex, intercepts)
5. ✓ Evaluate functions at given inputs and solve for inputs given outputs
6. ✓ Connect mathematical concepts to real pollution and ecological data

---

## Lab Connection

In the lab notebook (PlasticPollution.ipynb), you will:

1. Load the `global-plastics-production.csv` data using pandas
2. Create derived variables (time trend, scaled production in MMT)
3. Plot global plastic production over time
4. Work with the Jambeck data to calculate statistics
5. Practice selecting data rows based on conditions

The mathematical foundations from this lesson—understanding functions, domains, and quadratic behavior—will help you interpret what the data reveal about the accelerating plastic pollution crisis.

---

*Next: Week 2 — Logarithmic and Logistic Functions*
