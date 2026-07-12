<style>
.katex, .katex-display, .katex-display * { color: #1d4ed8 !important; }
.katex .boxed, .katex .fbox, .katex .colorbox { border-color: #1d4ed8 !important; }
</style>

**Analytical Methods for Scientists · Semester 2, 2026**

This guide is designed to help you study **effectively**, not to memorise. It does not include practice questions from the paper, because the exam rewards *understanding*, not recall. If you can confidently tick every Learning Outcome below, you are ready.

---

## Part 1 — Exam Blueprint (what the paper looks like)

| Section      | Marks   | Format                                         | What it tests                                               |
| :----------- | :------ | :--------------------------------------------- | :---------------------------------------------------------- |
| **Part I**   | **72**  | 36 multiple-choice × 2 marks                   | Recognition and single-step skills across **all 12 weeks** |
| **Part II**  | **14**  | 7 multiple-choice × 2 marks                    | Python as a mathematical tool (conceptual — no computer needed) |
| **Part III** | **24**  | Answer **2 of 4** long-answer × 12 marks each  | Setting up, solving, and **interpreting** larger problems   |
| **Total**    | **110** | 2 hours (≈ 1.5 min/MCQ, ≈ 20 min/long-answer) |                                                             |

> **Part III — important change from previous semesters.** You are required to answer only **2 of the 4** long-answer questions. This is a deliberate change: choose the two questions you feel most confident on. Read all four before you start, then commit — do not try to hedge by writing half an answer to three questions.

### How Part I is distributed

MCQs cover **all 12 weeks**, with a mix of single-topic and integrative questions that ask you to connect ideas across weeks. The coverage is broad rather than concentrated on any single week.

> **Implication:** No week is safe to skip. A week you ignore leaves real marks on the table.

> **Time pressure:** 2 hours is tight. A practical allocation: ~54 min for the 36 Part I MCQs (≈1.5 min each), ~14 min for the 7 Part II MCQs (≈2 min each), and ~40 min for 2 long-answer questions (≈20 min each), leaving ~12 min to review flagged questions. Do not get stuck on any single MCQ — flag it and move on.

### What Part II looks like

Part II has 7 multiple-choice questions that test your ability to **read and reason about Python code** — not write it. You will see short code snippets using `numpy`, `scipy`, and `matplotlib` and be asked what the code computes, which function performs a given mathematical task, or how to interpret the output. No computer is needed.

Useful things to be familiar with:
- `sp.Symbol('x')` — declares a symbolic variable
- `sp.diff(f, x)` — exact symbolic derivative
- `sp.integrate(f, (x, a, b))` — exact definite integral
- `sp.solve(expr, x)` — finds values of `x` where `expr = 0`
- `expr.subs(x, val)` — evaluates a symbolic expression at a specific value
- `plt.fill_between(x, y1, y2)` — shaded area between two curves
- `scipy.stats.binom.cdf(k, n, p)` — $P(X \le k)$ for $X \sim \text{Bin}(n,p)$; tail $P(X \ge k) = 1 - \text{cdf}(k-1, n, p)$

### What Part III looks like

Four extended problems are provided — you answer **any two**. Each is broken into 3–5 lettered parts and is **integrative** — you'll need to combine skills from several weeks. Read all four questions before you start, choose the two you feel most prepared for, and commit fully to each. Typical moves the marker is looking for:

1. **Set up** — define variables, write the model, state the units
2. **Solve** — carry out the calculus / algebra / LP steps
3. **Verify** — check a second-order condition, check a constraint, substitute back
4. **Interpret** — say what the number *means* in the scientific context

Partial marks are available for correct setup even if the algebra slips. Write down your reasoning.

### Materials allowed in the exam

As announced, you may bring:

- **Two double-sided A4 sheets of notes** (hand-written or typed — your choice)
- A **UWA-approved scientific calculator**
- Pens, pencils, eraser, ruler

### What to put on your two A4 sheets

You have four sides of A4 — use them well. This is your highest-leverage preparation task. Here is a prioritised list of what most students find useful to write down. You do **not** need all of it; pick what you are least confident recalling under pressure.

**Sheet 1 — Calculus (Weeks 4–7)**

- Standard derivatives: $\dfrac{d}{dx}[x^n],\ \dfrac{d}{dx}[e^{ax}],\ \dfrac{d}{dx}[\ln x],\ \dfrac{d}{dx}[\sin(kt)],\ \dfrac{d}{dx}[\cos(kt)]$
- Product rule: $(uv)' = u'v + uv'$
- Quotient rule: $(u/v)' = (u'v - uv')/v^2$
- Chain rule: $\dfrac{d}{dx}[f(g(x))] = f'(g(x))\,g'(x)$
- Standard antiderivatives (each with $+C$): $\int x^n\,dx = \dfrac{x^{n+1}}{n+1}$ (for $n \neq -1$), $\int \dfrac{1}{x}\,dx = \ln|x|$, $\int e^{ax}\,dx = \dfrac{1}{a}e^{ax}$
- Second-derivative test ($f'' > 0$ min, $f'' < 0$ max), **write this down** — easy to confuse under stress
- Fundamental Theorem of Calculus (both forms)
- Geometric series: $S_n = a\,\dfrac{r^n - 1}{r - 1}$

**Sheet 2 — Models, Probability & Algebra (Weeks 1–3, 8–12)**

- Logistic model $\dfrac{dP}{dt} = rP\!\left(1 - \dfrac{P}{K}\right)$, solution form $P(t) = \dfrac{K}{1 + A e^{-rt}}$ where $A = (K - P_0)/P_0$
- Schaefer model: growth $G(S) = gS(1 - S/K)$; MSY $= gK/4$ at $S = K/2$
- Lotka–Volterra equilibrium: $(N^*, P^*) = (\gamma/\delta,\ \alpha/\beta)$
- Doubling time: $t_d = \ln 2 / r$; half-life: $t_{1/2} = \ln 2 / |r|$ (with $r < 0$)
- Probability axioms, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- Conditional probability and Bayes' formula (the diagnostic-testing version is worth rewriting in your own words)
- Binomial PMF: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$, $E[X] = np$, $\mathrm{Var}(X) = np(1-p)$
- Trig: $\sin^2\theta + \cos^2\theta = 1$; exact values at $0, \pi/6, \pi/4, \pi/3, \pi/2$; sinusoidal parameters $A, B, C, D$ in $A\cos(B(t+C)) + D$; $T = 2\pi/B$
- Market equilibrium: $Q^d = Q^s$
- Consumer surplus $= \int_0^{Q^*}(P^d(Q) - P^*)\,dQ$; Producer surplus $= \int_0^{Q^*}(P^* - P^s(Q))\,dQ$
- Quadratic formula (you *will* need it)

**Python quick-reference (Part II — no computer needed, but useful to have)**

The Part II questions ask you to read short code snippets and reason about what they do. The table below covers the SymPy and matplotlib patterns used in the course.

| Python call | What it computes |
| :---------- | :--------------- |
| `x = sp.Symbol('x')` | Declare a symbolic variable |
| `sp.diff(f, x)` | Exact derivative $df/dx$ (symbolic) |
| `sp.diff(f, x, 2)` | Second derivative $d^2f/dx^2$ |
| `sp.integrate(f, x)` | Indefinite integral $\int f\,dx$ (symbolic, $+C$ omitted) |
| `sp.integrate(f, (x, a, b))` | Definite integral $\int_a^b f\,dx$ (exact value) |
| `sp.solve(expr, x)` | Solve $\text{expr} = 0$ for $x$; returns list of solutions |
| `expr.subs(x, val)` | Substitute $x = \text{val}$ into a symbolic expression |
| `plt.fill_between(x, y1, y2)` | Shaded region between two curves on a plot |
| `binom.cdf(k, n, p)` | $P(X \le k)$ for $X \sim \text{Bin}(n,p)$ |
| `1 - binom.cdf(k-1, n, p)` | $P(X \ge k)$ (upper tail probability) |

**Typical SymPy workflow for optimisation:**
```python
import sympy as sp
x = sp.Symbol('x')
f = ...                        # define the function
fp = sp.diff(f, x)             # first derivative
x_star = sp.solve(fp, x)[0]   # stationary point (solve f'=0)
fpp = sp.diff(f, x, 2)        # second derivative for SOC check
opt_val = f.subs(x, x_star)   # function value at optimum
```


**What is usually *not* worth writing**

- Fully worked examples — you won't have time to copy them during the exam
- Content for a week you haven't studied — formulas you don't understand won't help
- Long prose explanations — use symbols and short captions

**Tip:** prepare your sheets *as you study*, not at the end. Every time you look up a formula while working practice problems, copy it onto your sheet. By the end of revision your sheet is effectively your study log.

---

## Part 2 — Learning Outcomes by Week

For each week below, ask yourself: *Can I do this from scratch, without notes, in about 2 minutes?* Mark each one ✅ / ⚠️ / ❌. Spend your revision time on the ⚠️ and ❌ items.

### Week 1 — Functions and the Language of Scientific Analysis
- [ ] State the **domain** and **range** of common functions (linear, quadratic, rational, root, exponential, logarithm)
- [ ] Identify which values of $x$ make a function undefined (division by zero, square root of negative, log of zero/negative)
- [ ] Form the **composite** $(f \circ g)(x)$ correctly (inner function first)
- [ ] Find the **vertex**, **intercepts**, and **range** of a quadratic function
- [ ] Recognise when a relation is *not* a function (vertical line test)

### Week 2 — Exponential and Logarithmic Functions
- [ ] Sketch $y = A e^{kt}$ and recognise growth (k > 0) vs decay (k < 0)
- [ ] Use the laws of logarithms to simplify $\ln(ab)$, $\ln(a/b)$, $\ln(a^n)$
- [ ] Convert between the continuous form $P(t) = P_0 e^{rt}$ and the doubling-time / half-life form
- [ ] Compute the continuous growth rate from a doubling time (and vice versa)
- [ ] Solve exponential equations by taking logarithms of both sides

### Week 3 — Bounded Growth (Logistic and Schaefer)
- [ ] Recognise the **logistic** model $dP/dt = rP(1 - P/K)$ and identify $r$, $K$
- [ ] State the **equilibria** of the logistic model and classify them (stable / unstable)
- [ ] Recognise the **Schaefer** model $G(S) = gS(1 - S/K)$ and interpret $g$, $K$
- [ ] Explain why growth slows as the population approaches carrying capacity
- [ ] **Invert a function** — both a simple linear function, and a logistic solution $P(t)$ to solve for the **time** $t$ at which a given population level is reached
- [ ] Identify the **vertical and horizontal asymptotes** of a rational or shifted-rational function (e.g., $f(x) = \tfrac{3}{x-2} + 5$)

### Week 4 — Limits, Continuity and the Derivative
- [ ] Evaluate a limit numerically (from a table) and symbolically
- [ ] State what "continuous at a point" means
- [ ] Differentiate a polynomial term-by-term
- [ ] Differentiate $e^x$, $\ln x$, $x^n$, and a sum of these
- [ ] Find the **tangent line** to $y = f(x)$ at a given point (value + slope)

### Week 5 — Differentiation Rules and Optimisation
- [ ] Apply the **product rule** correctly
- [ ] Apply the **quotient rule** correctly
- [ ] Apply the **chain rule** (outside · inside)
- [ ] Locate **stationary points** by solving $f'(x) = 0$
- [ ] Classify stationary points using the **second derivative test** ($f''>0$ min, $f''<0$ max)
- [ ] Set up an **optimisation** word problem: identify the objective, the decision variable, and any constraint
- [ ] Interpret the optimum in context (e.g., "the maximum profit occurs at $t^*$ days and equals …")

### Week 6 — Introduction to Integration
- [ ] Compute the **indefinite integral** of a polynomial (don't forget $+C$)
- [ ] Integrate $e^{ax}$, $1/x$, $x^n$ (for $n \neq -1$)
- [ ] Use an **initial condition** to determine $C$ and state the particular antiderivative
- [ ] Recognise integration as the reverse of differentiation

### Week 7 — Definite Integrals, Area, and Sequences
- [ ] Evaluate a definite integral $\int_a^b f(x)\,dx$ and interpret it as a **net area**
- [ ] Compute **consumer surplus** and **producer surplus** from supply/demand curves
- [ ] State and use the **Fundamental Theorem of Calculus** in both forms
- [ ] Use the **geometric series** formula $S_n = a\,(r^n - 1)/(r - 1)$ for finite sums
- [ ] Recognise when a "total over $n$ periods" problem is a geometric series

### Week 8 — Predator–Prey (Lotka–Volterra) Dynamics
- [ ] Write the Lotka–Volterra system $dN/dt = \alpha N - \beta N P$, $dP/dt = \delta N P - \gamma P$
- [ ] Identify the parameters $\alpha, \beta, \gamma, \delta$ biologically (prey growth, predation, predator death, conversion efficiency)
- [ ] Find the non-trivial **equilibrium** $(N^*, P^*) = (\gamma/\delta,\ \alpha/\beta)$
- [ ] Perform **comparative statics**: if $\alpha$ increases, what happens to $N^*$ and $P^*$?
- [ ] Explain why prey and predator populations oscillate

### Week 9 — Probability and Combinatorics
- [ ] Apply $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- [ ] Apply $P(A \cap B) = P(A)P(B)$ for **independent** events
- [ ] Use **conditional probability** $P(A|B) = P(A \cap B) / P(B)$
- [ ] Apply **Bayes' theorem** to diagnostic-testing problems (sensitivity, specificity, prevalence → PPV / NPV)
- [ ] Use binomial coefficients $\binom{n}{k}$ for counting outcomes
- [ ] Recognise when events are mutually exclusive vs independent (they are *not* the same)

### Week 10 — Random Variables and Hypothesis Testing
- [ ] Compute the **expected value** $E[X] = \sum x\,P(X=x)$
- [ ] Compute the **variance** and **standard deviation** of a discrete random variable
- [ ] Recognise the **binomial** distribution and use $X \sim \text{Bin}(n, p)$
- [ ] Compute tail probabilities such as $P(X \ge k)$ for a binomial variable
- [ ] State a null and alternative hypothesis correctly
- [ ] Given a **$p$-value** and a significance level $\alpha$, state the correct conclusion and what it means in context

### Week 11 — Trigonometry and Sinusoidal Models
- [ ] Know the exact values of $\sin$, $\cos$, $\tan$ at $0, \pi/6, \pi/4, \pi/3, \pi/2$
- [ ] Differentiate $\sin(kt)$ and $\cos(kt)$ using the chain rule
- [ ] Identify the **amplitude**, **period**, **phase shift**, and **vertical shift** of $x(t) = A\cos(B(t+C)) + D$
- [ ] Compute **period** $T = 2\pi/B$ and **frequency** $f = 1/T$
- [ ] Build a sinusoidal model from a verbal description (max, min, period, starting value)

### Week 12 — Simultaneous Equations and Linear Programming
- [ ] Solve a 2×2 linear system (substitution or elimination)
- [ ] Find a **market equilibrium** by setting supply equal to demand
- [ ] Formulate a linear-programming problem: objective, decision variables, constraints, non-negativity
- [ ] Sketch the **feasible region** and label all vertices
- [ ] Apply the **corner-point theorem** to find the optimum
- [ ] Identify which constraints are **binding** at the optimum
- [ ] Perform a simple **sensitivity analysis** when one coefficient changes

---

## Part 3 — Integrative skills (across weeks)

These are the hinge ideas that appear in the long-answer section. If you only have one day left, focus here.

1. **Rate → total**: given $dy/dt$, integrate and apply an initial condition to recover $y(t)$
2. **Optimisation with calculus**: set up $\pi(t)$, take $d\pi/dt = 0$, check $d^2\pi/dt^2 < 0$
3. **LP graphical method**: formulate → sketch → enumerate corners → evaluate objective → verify binding constraints → sensitivity
4. **Bounded-growth dynamics**: set $dS/dt = 0$ to find equilibria, interpret what happens if $S$ starts below or above $S_{\text{MSY}}$
5. **Interpret when asked**: where a question explicitly asks you to *explain* or *interpret*, a short plain-English sentence about what the number means scientifically will earn the marks. Don't pad answers with interpretation when none is requested — follow what the question asks.

---

## Part 4 — Common traps markers see

These cost students marks every year:

- ❌ Forgetting $+C$ on an indefinite integral
- ❌ Writing $dy/dx$ when the problem asks for $dP/dt$ (use the right variable)
- ❌ Dropping the chain rule on $\sin(4\pi t)$ — the derivative is $4\pi \cos(4\pi t)$, not $\cos(4\pi t)$
- ❌ LP sketch without labelled axes, boundary lines, or vertex coordinates
- ❌ Stating a stationary point is a maximum without checking the second-order condition
- ❌ Confusing "mutually exclusive" with "independent" in probability
- ❌ Stopping at the numerical answer and not writing the **interpretation sentence**
- ❌ Rounding too early — keep 4+ significant figures until the final line
- ❌ Missing units on the final answer (kg, \$/day, tonnes/year, etc.)

---

## Part 5 — A recommended 3-pass study protocol

**Pass 1 — Concepts (1 day).** Go through the checklist above. Mark ✅ / ⚠️ / ❌ honestly.

**Pass 2 — Skills (2–3 days).** For each ⚠️ item, redo one problem from the **Student Lab Handbook worksheet** for that week *without looking at the solution first*. For each ❌ item, re-read the weekly lesson and re-watch the concept video before attempting anything.

**Pass 3 — Integration (1 day).** Under timed conditions: redo the Week 10 mock exam questions; redo one lab worksheet each from Weeks 5, 7, 8, and 12 (these are among the most integrative weeks); attempt any Part II Python MCQs in the sample exam; and attempt any practice questions in the app that you previously struggled with. For Part III practice, time yourself: allow 20 minutes per question and practise the full set-up → solve → verify → interpret workflow.

---

## Part 6 — Resources you already have

- **SciQuant Assistant app** — Weekly lessons, practice questions, and the Tools tab (calculator, equation solver, graphing tool, periodic table, flashcards).
  > ⚠️ **Important — update your app.** The lessons and practice questions have been revised to reflect the full Semester 2 content. Please **download and install the latest version** from the usual distribution link before you start your revision in earnest — the bundled lessons should match the refreshed set.
- **Student Lab Handbook (worksheets)** — All weekly problem briefs in one document
- **Formula Sheet** — In the Course Overview of the app
- **Week 10 Mock Exam** — Treat it as a full dress rehearsal

---

## Part 7 — Before you walk in

- Bring your student card, a **UWA-approved scientific calculator** (get it approved *before* exam day and check the battery), two pens, a pencil, and a ruler
- Arrive early
- Read the whole paper first. Note which long-answer question you're most confident on and do it first.
- Budget your time
- On MCQs — if you're stuck, eliminate the options that are obviously wrong and narrow your choice down to the remaining ones. There is no penalty for guessing.
- Show working on long-answer questions *even if* you're not confident of the final answer. Setup marks are real.

Good luck. You have done the work this semester — this exam gives you a chance to show what you now understand.

---

# Appendix — Exemplar Part II Problems (with full solutions)

These five problems are written in the **style, scope and difficulty** of Part II of the paper. They are **not** from the exam. They are designed to let you practise the full workflow:

> **set up → solve → verify → interpret**

For each problem, sit down with blank paper, set a **15-minute timer**, and work from setup to interpretation without notes or peeking — this mirrors the pace you will need on the day (12 min per Part II question, plus a small buffer for practice). If you genuinely stall before the timer ends, glance at the *hint* only; save the full solution for the post-attempt review. Do not read ahead.

---

## Exemplar Problem 1 — Optimisation (Weeks 5, 6)

**Context: optimal nitrogen rate for wheat.**

A grower manages $N = 40$ hectares of wheat and must choose the nitrogen fertiliser application rate $x$ (kg N per hectare, $x \ge 0$) that **maximises profit**. Over the relevant range, the per-hectare marginal yield response to nitrogen (in kg of extra grain per kg of N applied) is
$$\frac{dY}{dx} = 30 - 0.5\,x,$$
so the first kilogram of nitrogen gives a large yield boost and each further kilogram gives progressively less. Assume the additional yield at zero N is $Y(0) = 0$. Nitrogen costs \$2.00 per kg applied, and the extra wheat sells for \$0.40 per kg.

**(a)** [3 marks] Write the per-hectare additional-yield function $Y(x)$.

**(b)** [3 marks] Derive an expression for the total **profit** $\pi(x)$ from the 40 ha (extra revenue minus nitrogen cost).

**(c)** [3 marks] Find the nitrogen rate $x^*$ that maximises $\pi(x)$ and verify it is a maximum using the second-order condition.

**(d)** [3 marks] Compute $Y(x^*)$, the total extra revenue, the total nitrogen cost, and the maximum profit.

*Hint: $\pi(x) = 40 \times [0.40\,Y(x) - 2\,x]$. Take $d\pi/dx = 0$.*

### Solution

**Part (a) — Additional-yield function.**

Integrate the marginal response and apply $Y(0) = 0$:
$$Y(x) = \int (30 - 0.5\,x)\,dx = 30\,x - 0.25\,x^2 + C, \qquad Y(0) = 0 \;\Rightarrow\; C = 0.$$
$$\boxed{\,Y(x) = 30\,x - 0.25\,x^2 \quad (\text{kg/ha})\,}$$

**Part (b) — Total profit function.**

Per-hectare profit is extra revenue minus nitrogen cost per hectare:
$$\pi_{\text{ha}}(x) = 0.40\,Y(x) - 2\,x = 0.40(30x - 0.25x^2) - 2x = 10\,x - 0.1\,x^2.$$
Total profit over the 40 ha:
$$\boxed{\,\pi(x) = 40\,(10x - 0.1x^2) = 400\,x - 4\,x^2 \quad (\text{dollars})\,}$$

**Part (c) — Optimum nitrogen rate.**

Stationary point:
$$\pi'(x) = 400 - 8\,x = 0 \;\Longrightarrow\; x^* = 50 \text{ kg N/ha}.$$
Second-order check:
$$\pi''(x) = -8 < 0 \;\Rightarrow\; x^* = 50 \text{ is a maximum.} \;\checkmark$$

**Part (d) — Numerical values at the optimum.**

| Quantity            | Calculation                   | Value                |
| :------------------ | :---------------------------- | :------------------- |
| Extra yield per ha  | $Y(50) = 30(50) - 0.25(50)^2$ | $875$ kg/ha          |
| Total extra revenue | $40 \times 0.40 \times 875$   | $\$14{,}000$         |
| Total nitrogen cost | $40 \times 2 \times 50$       | $\$4{,}000$          |
| **Maximum profit**  | $\$14{,}000 - \$4{,}000$      | $\boxed{\$10{,}000}$ |

*Interpretation: Applying 50 kg N/ha maximises profit. Beyond that rate, the marginal yield response $dY/dx$ has fallen below the cost per kilogram of nitrogen, so each extra kg of N loses money.*

---

## Exemplar Problem 2 — Linear Programming (Week 12)

**Context: aquaculture feed blend.**

An aquaculture manager mixes two feed ingredients, Pellet A and Pellet B, in quantities $x$ and $y$ kg per tank per day. Nutrient contents, minimum daily requirements and prices are summarised below.

| Nutrient (per kg of pellet) | Pellet A | Pellet B | Minimum per tank/day |
| :-------------------------- | :------- | :------- | :------------------- |
| Protein (g)                 | 2        | 3        | 12                   |
| Lipid (g)                   | 3        | 1        | 9                    |
| Calcium (g)                 | 1        | 2        | 6                    |
| **Cost (\$/kg)**            | 4        | 3        | —                    |

In addition, a **regulatory requirement** specifies that each tank must receive **at least 1 kg of Pellet A per day** (it carries a medicated additive). The manager wants to **minimise daily cost** $C = 4x + 3y$ subject to all nutrient and regulatory constraints (and $x, y \ge 0$).

**(a)** [2 marks] Write the complete LP formulation.

**(b)** [4 marks] Sketch the feasible region, labelling all boundary lines and the corner points of the feasible region.

**(c)** [3 marks] Apply the corner-point theorem to find the minimum-cost feed mix. State $(x^*, y^*)$ and the minimum cost.

**(d)** [2 marks] Which constraints are **binding** at the optimum, and which are slack?

**(e)** [1 mark] **Sensitivity.** If the cost of Pellet B rises from \$3 to \$5 per kg (all else unchanged), recompute the minimum-cost mix.

*Hint: write each constraint as an equality, find the pairwise intersections, and test only the corners that satisfy **all four** inequality constraints simultaneously.*

### Solution

**Part (a) — LP formulation.**

$$\begin{aligned}
\min_{x,y}\quad & C = 4x + 3y \\
\text{s.t.}\quad & 2x + 3y \ge 12 && (\text{protein}) \\
& 3x + y \ge 9 && (\text{lipid}) \\
& x + 2y \ge 6 && (\text{calcium}) \\
& x \ge 1 && (\text{regulatory}) \\
& x,\ y \ge 0.
\end{aligned}$$

**Part (b) — Feasible region and corner points.**

Boundary lines:

- **Protein** $2x + 3y = 12$: passes through $(0, 4)$ and $(6, 0)$
- **Lipid** $3x + y = 9$: passes through $(0, 9)$ and $(3, 0)$
- **Calcium** $x + 2y = 6$: passes through $(0, 3)$ and $(6, 0)$
- **Regulatory** $x = 1$: vertical line

Check each candidate intersection against *all four* inequality constraints:

| Intersection      | Coordinates     | Feasible?                              |
| :---------------- | :-------------- | :------------------------------------- |
| Protein ∩ Lipid   | $(15/7,\ 18/7)$ | ✓  $P_1$                               |
| Lipid ∩ $x = 1$   | $(1,\ 6)$       | ✓  $P_2$                               |
| Protein ∩ Calcium | $(6,\ 0)$       | ✓  $P_3$                               |
| Protein ∩ $x = 1$ | $(1,\ 10/3)$    | ✗ (lipid: $3 + 10/3 \approx 6.33 < 9$) |
| Lipid ∩ Calcium   | $(12/5,\ 9/5)$  | ✗ (protein: $10.2 < 12$)               |
| Calcium ∩ $x = 1$ | $(1,\ 5/2)$     | ✗ (lipid: $3 + 2.5 = 5.5 < 9$)         |

The feasible region is bounded below by the three binding-capable constraints (protein, lipid, calcium) and on the left by the regulatory line $x = 1$. Three corners are feasible: $P_1 \approx (2.14,\ 2.57),\ P_2 = (1,\ 6),\ P_3 = (6,\ 0)$.

<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-55 -20 380 310" width="480" height="390" font-family="sans-serif" font-size="11">
  <!-- Axes -->
  <line x1="0" y1="280" x2="310" y2="280" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="0" y1="280" x2="0" y2="0"  stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <defs>
    <marker id="arr" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
  <!-- Axis labels -->
  <text x="315" y="284" font-size="12" fill="#333">x</text>
  <text x="-5" y="-8"  font-size="12" fill="#333" text-anchor="middle">y</text>
  <!-- Tick marks and numbers (scale: 35px per unit) -->
  <g stroke="#333" stroke-width="1">
    <line x1="35"  y1="276" x2="35"  y2="284"/><text x="35"  y="294" text-anchor="middle">1</text>
    <line x1="70"  y1="276" x2="70"  y2="284"/><text x="70"  y="294" text-anchor="middle">2</text>
    <line x1="105" y1="276" x2="105" y2="284"/><text x="105" y="294" text-anchor="middle">3</text>
    <line x1="140" y1="276" x2="140" y2="284"/><text x="140" y="294" text-anchor="middle">4</text>
    <line x1="175" y1="276" x2="175" y2="284"/><text x="175" y="294" text-anchor="middle">5</text>
    <line x1="210" y1="276" x2="210" y2="284"/><text x="210" y="294" text-anchor="middle">6</text>
    <line x1="-4" y1="245" x2="4" y2="245"/><text x="-8" y="249" text-anchor="end">1</text>
    <line x1="-4" y1="210" x2="4" y2="210"/><text x="-8" y="214" text-anchor="end">2</text>
    <line x1="-4" y1="175" x2="4" y2="175"/><text x="-8" y="179" text-anchor="end">3</text>
    <line x1="-4" y1="140" x2="4" y2="140"/><text x="-8" y="144" text-anchor="end">4</text>
    <line x1="-4" y1="105" x2="4" y2="105"/><text x="-8" y="109" text-anchor="end">5</text>
    <line x1="-4" y1="70"  x2="4" y2="70" /><text x="-8" y="74"  text-anchor="end">6</text>
    <line x1="-4" y1="35"  x2="4" y2="35" /><text x="-8" y="39"  text-anchor="end">7</text>
  </g>
  <!-- Feasible region: vertices P1=(15/7,18/7)≈(2.14,2.57), P2=(1,6), P3=(6,0) -->
  <!-- In SVG coords (y flipped): x_svg=35x, y_svg=280-35y -->
  <!-- P1=(74.9,190.0), P2=(35,70), P3=(210,280) -->
  <polygon points="74.9,190.0 35,70 35,0 280,0 280,280 210,280" fill="#b0c4de" fill-opacity="0.45" stroke="none"/>
  <!-- Constraint lines -->
  <!-- Protein: 2x+3y=12 → y=(12-2x)/3; at x=0,y=4; at x=6,y=0 -->
  <line x1="0" y1="140" x2="210" y2="280" stroke="#1e50aa" stroke-width="2"/>
  <text x="80" y="230" fill="#1e50aa" font-size="10">protein 2x+3y=12</text>
  <!-- Lipid: 3x+y=9 → y=9-3x; at x=0,y=9; at x=3,y=0 -->
  <line x1="0" y1="-35" x2="105" y2="280" stroke="#c86420" stroke-width="2"/>
  <text x="30" y="95" fill="#c86420" font-size="10">lipid 3x+y=9</text>
  <!-- Calcium: x+2y=6 → y=(6-x)/2; at x=0,y=3; at x=6,y=0 -->
  <line x1="0" y1="175" x2="210" y2="280" stroke="#1e9657" stroke-width="2"/>
  <text x="120" y="255" fill="#1e9657" font-size="10">calcium x+2y=6</text>
  <!-- Regulatory: x=1 -->
  <line x1="35" y1="0" x2="35" y2="280" stroke="#a020a0" stroke-width="2"/>
  <text x="37" y="20" fill="#a020a0" font-size="10">x=1</text>
  <!-- Isocost C*=4x+3y=114/7≈16.29: y=(16.29-4x)/3; at x=0,y=5.43→y_svg=89.9; at x=4.07,y=0 -->
  <line x1="0" y1="89.9" x2="142.5" y2="280" stroke="#111" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="100" y="148" fill="#111" font-size="10">C*≈$16.29</text>
  <!-- Corner dots -->
  <circle cx="74.9"  cy="190.0" r="5" fill="#e02020"/>
  <circle cx="35"    cy="70"    r="4" fill="#555"/>
  <circle cx="210"   cy="280"   r="4" fill="#555"/>
  <!-- Labels -->
  <text x="80" y="192" fill="#e02020" font-weight="bold" font-size="11">P₁≈(2.14, 2.57) ★</text>
  <text x="38" y="65"  fill="#333" font-size="11">P₂=(1, 6)</text>
  <text x="213" y="275" fill="#333" font-size="11">P₃=(6, 0)</text>
  <text x="170" y="120" fill="#7a8a9a" font-size="11">feasible</text>
  <!-- Axis titles -->
  <text x="155" y="308" text-anchor="middle" font-size="12">x (Pellet A, kg/day)</text>
  <text x="-42" y="140" text-anchor="middle" font-size="12" transform="rotate(-90,-42,140)">y (Pellet B, kg/day)</text>
</svg>
<figcaption>Feasible region (shaded) and minimum-cost corner P₁ ≈ (2.14, 2.57) for Exemplar 2.</figcaption>
</figure>

**Part (c) — Corner-point theorem.**

| Corner | $x$    | $y$    | $C = 4x + 3y$                         |
| :----- | :----- | :----- | :------------------------------------ |
| $P_1$  | $15/7$ | $18/7$ | $60/7 + 54/7 = 114/7 \approx \$16.29$ |
| $P_2$  | $1$    | $6$    | $4 + 18 = \$22.00$                    |
| $P_3$  | $6$    | $0$    | $24 + 0 = \$24.00$                    |

$$\boxed{\,(x^*, y^*) = (15/7,\ 18/7) \approx (2.14,\ 2.57)\ \text{kg/tank/day}; \quad C^* \approx \$16.29\,}$$

**Part (d) — Binding and slack constraints at $P_1$.**

- Protein: $2(15/7) + 3(18/7) = 84/7 = 12$ — **binding**
- Lipid: $3(15/7) + 18/7 = 63/7 = 9$ — **binding**
- Calcium: $15/7 + 36/7 = 51/7 \approx 7.29 > 6$ — slack by $9/7$
- Regulatory: $x = 15/7 \approx 2.14 > 1$ — slack by $8/7$

**Part (e) — Sensitivity to Pellet B price.**

New objective $C' = 4x + 5y$. Re-evaluate the three feasible corners (the feasible region is unchanged):

| Corner | $C' = 4x + 5y$                        |
| :----- | :------------------------------------ |
| $P_1$  | $60/7 + 90/7 = 150/7 \approx \$21.43$ |
| $P_2$  | $4 + 30 = \$34.00$                    |
| $P_3$  | $24 + 0 = \$24.00$                    |

**Optimum remains at $P_1$**, new cost $\approx \$21.43$.

*Interpretation: Even a ~67% rise in Pellet B's price does not shift the optimum. The rule from the corner-point theorem is: the optimum changes only when the isocost line $4x + c_B\,y = C$ becomes flatter (or steeper) than one of the two constraints binding at the current optimum. At $P_1$ the binding constraints are protein ($2x + 3y = 12$, slope $-2/3$) and lipid ($3x + y = 9$, slope $-3$). The isocost slope is $-4/c_B$. The optimum stays at $P_1$ as long as $-3 \le -4/c_B \le -2/3$, i.e.\ $4/3 \le c_B \le 6$. For $c_B > 6$ the optimum jumps to $P_3 = (6,\,0)$ (drop Pellet B altogether); for $c_B < 4/3$ it jumps to $P_2 = (1,\,6)$ (use only the regulatory minimum of Pellet A). Since \$5 lies inside $[4/3,\,6]$, the mix is unchanged; the cost simply rises from \$16.29 to \$21.43.*

---

## Exemplar Problem 3 — Bounded Growth Dynamics (Weeks 3, 7)

**Context: commercial kangaroo harvest on a rangeland station.**

A red kangaroo population of size $S$ (animals) on a large pastoral property grows logistically, and is harvested each year by a licensed commercial operator:
$$\frac{dS}{dt} = r\,S\!\left(1 - \frac{S}{K}\right) - H,$$
where $r = 0.4$ per year is the intrinsic growth rate, $K = 500$ animals is the rangeland's carrying capacity, and $H$ is the annual cull quota (animals removed per year) set by the wildlife agency.

**(a)** [3 marks] Find the **maximum sustainable yield** (MSY) — the largest constant harvest the population can support at equilibrium ($dS/dt = 0$) — and the population $S_{\mathrm{MSY}}$ at which it is achieved. Show that $\mathrm{MSY} = rK/4$ and $S_{\mathrm{MSY}} = K/2$.

**(b)** [3 marks] The current population is $S_0 = 400$. If the agency sets $H$ equal to the MSY from part (a), compute $dS/dt$ at $S = 400$. Does the population grow or shrink, and toward what long-run level?

**(c)** [3 marks] Suppose instead the agency wants to *hold* the population at $S = 400$ (to keep a viable breeding stock while avoiding overgrazing at $K$). What annual cull $H$ just achieves that?

**(d)** [3 marks] Each harvested animal yields a carcass sold for \$300. Compute the annual revenue of the industry when the quota is set at MSY. In one sentence, explain why setting $H$ **above** MSY would eventually collapse the population.

*Hint: MSY is the maximum of $G(S) = r S\,(1 - S/K)$, which occurs at $S = K/2$.*

### Solution

**Part (a) — Maximum sustainable yield.**

At equilibrium $dS/dt = 0 \;\Rightarrow\; H = G(S) \equiv r\,S\,(1 - S/K)$. Maximise $G$:
$$G'(S) = r - \tfrac{2rS}{K} = 0 \;\Longrightarrow\; S_{\mathrm{MSY}} = \tfrac{K}{2} = 250\ \text{animals}.$$
Second derivative $G''(S) = -2r/K < 0$ confirms a maximum. Therefore
$$\boxed{\,\mathrm{MSY} = G(K/2) = \tfrac{rK}{4} = \tfrac{0.4 \times 500}{4} = 50\ \text{animals/year}\,}$$

**Part (b) — Dynamics at $S_0 = 400$, $H = 50$.**

$$\frac{dS}{dt}\bigg|_{S=400} = 0.4(400)\!\left(1 - \tfrac{400}{500}\right) - 50 = 160 \times 0.2 - 50 = 32 - 50 = -18\ \text{animals/year}.$$
**The population is shrinking by 18 animals/year.** Because $H = 50$ equals MSY, the harvest line $H = 50$ is *tangent* to the recruitment curve $G(S) = rS(1 - S/K)$ at $S = S_{\mathrm{MSY}} = 250$. Setting $G(S) = 50$ gives $S^2 - 500S + 62{,}500 = 0$, a perfect square with the single (double) root $S = 250$. So there is only **one** equilibrium under this policy. Since $G(S) < 50$ for every $S \ne 250$, we have $dS/dt < 0$ for all $S > 250$ (and for all $S < 250$ as well): from $S_0 = 400$ the population declines monotonically and asymptotically approaches $S = 250$ from above. This equilibrium is only **semi-stable** (tangent): any perturbation below $250$ would send the population crashing to extinction, so operating at MSY carries no safety margin.

**Part (c) — Quota needed to hold $S = 400$.**

$$H = G(400) = 0.4(400)\!\left(1 - \tfrac{400}{500}\right) = 160 \times 0.2 = 32\ \text{animals/year}.$$
This is **less than** MSY ($32 < 50$), as expected: populations above $S_{\mathrm{MSY}}$ have lower recruitment and so support smaller sustainable harvests.

**Part (d) — Annual revenue at MSY.**

$$\text{Annual revenue} = 50 \times \$300 = \boxed{\$15{,}000\ \text{per year}}.$$

<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-60 -20 430 300" width="520" height="340" font-family="sans-serif" font-size="11">
  <!-- Axes: x=S in [0,500], y=G in [0,55]; scale: x×0.56, y×4 -->
  <!-- x_svg = 56*S/50 = 1.12*S (but let's use 500px wide for S=0..500, so 0.9px/unit) -->
  <!-- Use: x_svg = S*0.68, y_svg = 240 - G*4.4 -->
  <defs>
    <marker id="ar2" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
  <line x1="0" y1="240" x2="360" y2="240" stroke="#333" stroke-width="1.5" marker-end="url(#ar2)"/>
  <line x1="0" y1="240" x2="0"   y2="0"   stroke="#333" stroke-width="1.5" marker-end="url(#ar2)"/>
  <text x="364" y="244" font-size="12" fill="#333">S</text>
  <text x="-4"  y="-8"  font-size="12" fill="#333" text-anchor="end">G</text>
  <!-- Tick marks: S = 100,200,250,300,400,500 -->
  <g stroke="#333" stroke-width="1" font-size="10">
    <line x1="68"  y1="236" x2="68"  y2="244"/><text x="68"  y="254" text-anchor="middle">100</text>
    <line x1="136" y1="236" x2="136" y2="244"/><text x="136" y="254" text-anchor="middle">200</text>
    <line x1="170" y1="236" x2="170" y2="244"/><text x="170" y="254" text-anchor="middle">250</text>
    <line x1="204" y1="236" x2="204" y2="244"/><text x="204" y="254" text-anchor="middle">300</text>
    <line x1="272" y1="236" x2="272" y2="244"/><text x="272" y="254" text-anchor="middle">400</text>
    <line x1="340" y1="236" x2="340" y2="244"/><text x="340" y="254" text-anchor="middle">500</text>
    <!-- y ticks: G=10,20,30,40,50 → y_svg=240-44*n -->
    <line x1="-4" y1="196" x2="4" y2="196"/><text x="-7" y="200" text-anchor="end">10</text>
    <line x1="-4" y1="152" x2="4" y2="152"/><text x="-7" y="156" text-anchor="end">20</text>
    <line x1="-4" y1="108" x2="4" y2="108"/><text x="-7" y="112" text-anchor="end">30</text>
    <line x1="-4" y1="64"  x2="4" y2="64" /><text x="-7" y="68"  text-anchor="end">40</text>
    <line x1="-4" y1="20"  x2="4" y2="20" /><text x="-7" y="24"  text-anchor="end">50</text>
  </g>
  <!-- Parabola G(S)=0.4S(1-S/500); at S=s: G=0.4s(1-s/500)
       x_svg=0.68*S, y_svg=240-4.4*G = 240 - 4.4*0.4*S*(1-S/500)
       Points: S=0→(0,240), S=100→(68,193.6), S=200→(136,170.4), S=250→(170,162),
               S=300→(204,170.4), S=400→(272,193.6), S=500→(340,240) -->
  <polyline points="0,240 34,199.7 68,172.0 102,156.9 136,154.4 170,164.4 204,187.1 238,222.3 272,240 306,240 340,240"
    fill="none" stroke="#1e50aa" stroke-width="2.5"/>
  <!-- smoother curve via more points -->
  <polyline points="0,240 17,206.8 34,177.2 51,151.1 68,128.5 85,109.5 102,94.0 119,82.0 136,73.5 153,68.6 170,67.2 187,69.3 204,74.9 221,84.1 238,96.7 255,112.8 272,132.5 289,155.6 306,182.3 323,212.4 340,240"
    fill="none" stroke="#1e50aa" stroke-width="2.5"/>
  <!-- H=50 line (MSY) -->
  <line x1="0" y1="20" x2="340" y2="20" stroke="#c86420" stroke-width="2" stroke-dasharray="8,4"/>
  <text x="345" y="24" fill="#c86420" font-size="10">H=MSY=50</text>
  <!-- MSY tangent point: S=250, G=50 → (170,20) -->
  <circle cx="170" cy="20" r="5" fill="#e02020"/>
  <line x1="170" y1="20" x2="170" y2="240" stroke="#777" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="174" y="14" fill="#e02020" font-size="10">S_MSY=250</text>
  <!-- S0=400 marker -->
  <circle cx="272" cy="240" r="5" fill="#1e9657"/>
  <text x="264" y="232" fill="#1e9657" font-size="10">S₀=400</text>
  <!-- G(400)=32 point: y_svg=240-4.4*32=99.2 -->
  <circle cx="272" cy="99.2" r="4" fill="#1e9657"/>
  <line x1="272" y1="99.2" x2="272" y2="240" stroke="#aaa" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="276" y="95" fill="#1e9657" font-size="10">G(400)=32</text>
  <!-- Axis labels -->
  <text x="170" y="275" text-anchor="middle" font-size="12">Stock size S (animals)</text>
  <text x="-50" y="120" text-anchor="middle" font-size="12" transform="rotate(-90,-50,120)">Recruitment G(S)</text>
  <!-- Curve label -->
  <text x="10" y="85" fill="#1e50aa" font-size="10">G(S)=0.4S(1−S/500)</text>
</svg>
<figcaption>Schaefer recruitment curve G(S) = 0.4S(1−S/500) with MSY = 50 at S_MSY = 250 (red dot). The orange dashed line shows the harvest quota H = 50, tangent to G(S) at S_MSY. Starting from S₀ = 400 the population declines toward S_MSY.</figcaption>
</figure>

*Interpretation: Setting $H > \mathrm{MSY}$ initially gives higher returns, but the population falls; once $S$ drops below $S_{\mathrm{MSY}} = 250$, the now-reduced recruitment can no longer keep up with the same cull and the population collapses — together with the industry that depends on it.*

---

## Exemplar Problem 4 — Rate → Total with Initial Condition (Weeks 6, 7)

**Context: drug clearance.**

After an intravenous dose, the plasma concentration $c(t)$ (mg/L) of a drug changes at rate
$$\frac{dc}{dt} = -0.5 + 0.06\,t - 0.003\,t^2 \quad (\text{mg/L per hour}),\qquad t \ge 0.$$
A measurement at $t = 2$ hours gives $c(2) = 7.80$ mg/L.

**(a)** [3 marks] Find the general antiderivative $c(t)$, including the integration constant $C$.

**(b)** [3 marks] Use $c(2) = 7.80$ to determine $C$ and state the particular solution.

**(c)** [2 marks] Compute $c(0)$ and $c(10)$.

**(d)** [2 marks] Interpret biologically what the **sign** of $dc/dt$ at $t = 0$ and at $t = 10$ says about how the plasma concentration is changing.

**(e)** [2 marks] Sketch $c(t)$ on $0 \le t \le 20$ hours, indicating the measurement at $t = 2$ and any interior minimum.

*Hint: integrate $dc/dt$ term-by-term to get $c(t) = -0.5\,t + 0.03\,t^2 - 0.001\,t^3 + C$, then use the measurement at $t = 2$ to pin down $C$.*

### Solution

**Part (a) — General antiderivative.**

$$c(t) = \int \left(-0.5 + 0.06\,t - 0.003\,t^2\right) dt = -0.5\,t + 0.03\,t^2 - 0.001\,t^3 + C.$$

**Part (b) — Particular solution.**

At $t = 2$: $c(2) = -1 + 0.12 - 0.008 + C = -0.888 + C = 7.80 \;\Rightarrow\; C = 8.688$.

$$\boxed{\,c(t) = -0.5\,t + 0.03\,t^2 - 0.001\,t^3 + 8.688 \quad (\text{mg/L})\,}$$

**Part (c) — Values at $t = 0$ and $t = 10$.**

| $t$ (h) | Calculation          | $c(t)$ (mg/L) |
| :------ | :------------------- | :------------ |
| $0$     | $0 + 0 - 0 + 8.688$  | $8.688$       |
| $10$    | $-5 + 3 - 1 + 8.688$ | $5.688$       |

**Part (d) — Interpretation of the rate's sign.**

| $t$ (h) | $dc/dt$ (mg/L per h)      | Biological meaning                                           |
| :------ | :------------------------ | :----------------------------------------------------------- |
| $0$     | $-0.5 + 0 - 0 = -0.5$     | Concentration **falling rapidly** immediately after dose.    |
| $10$    | $-0.5 + 0.6 - 0.3 = -0.2$ | Still **falling**, but more slowly — clearance is weakening. |

**Part (e) — Sketch guidance.**

Does an interior minimum exist? Solve $dc/dt = 0$:
$$-0.003\,t^2 + 0.06\,t - 0.5 = 0 \;\Longleftrightarrow\; t^2 - 20\,t + \tfrac{500}{3} = 0.$$
Discriminant $= 400 - 4 \times \tfrac{500}{3} = 400 - 666.\overline{6} < 0 \;\Rightarrow\;$ **no real root**.

Therefore $dc/dt < 0$ for all $t \ge 0$: $c(t)$ is **monotonically decreasing** on $[0, 20]$. The minimum on this interval is at $t = 20$:
$$c(20) = -10 + 12 - 8 + 8.688 = 2.688\ \text{mg/L}.$$

Sketch: curve starts at $c(0) = 8.688$, passes through $(2,\ 7.80)$, and decreases smoothly to $(20,\ 2.688)$.

<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-55 -20 390 300" width="480" height="340" font-family="sans-serif" font-size="11">
  <defs>
    <marker id="ar3" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
  <!-- Axes: t in [0,20], c in [0,9]; scale: x=16*t, y=250-26*c -->
  <line x1="0" y1="250" x2="345" y2="250" stroke="#333" stroke-width="1.5" marker-end="url(#ar3)"/>
  <line x1="0" y1="250" x2="0"   y2="0"   stroke="#333" stroke-width="1.5" marker-end="url(#ar3)"/>
  <text x="348" y="254" font-size="12" fill="#333">t</text>
  <text x="-4"  y="-8"  font-size="12" fill="#333" text-anchor="end">c</text>
  <!-- Ticks: t=0..20 step 2; c=0..9 step 1 -->
  <g stroke="#333" stroke-width="1" font-size="10">
    <line x1="32"  y1="246" x2="32"  y2="254"/><text x="32"  y="263" text-anchor="middle">2</text>
    <line x1="64"  y1="246" x2="64"  y2="254"/><text x="64"  y="263" text-anchor="middle">4</text>
    <line x1="96"  y1="246" x2="96"  y2="254"/><text x="96"  y="263" text-anchor="middle">6</text>
    <line x1="128" y1="246" x2="128" y2="254"/><text x="128" y="263" text-anchor="middle">8</text>
    <line x1="160" y1="246" x2="160" y2="254"/><text x="160" y="263" text-anchor="middle">10</text>
    <line x1="192" y1="246" x2="192" y2="254"/><text x="192" y="263" text-anchor="middle">12</text>
    <line x1="224" y1="246" x2="224" y2="254"/><text x="224" y="263" text-anchor="middle">14</text>
    <line x1="256" y1="246" x2="256" y2="254"/><text x="256" y="263" text-anchor="middle">16</text>
    <line x1="288" y1="246" x2="288" y2="254"/><text x="288" y="263" text-anchor="middle">18</text>
    <line x1="320" y1="246" x2="320" y2="254"/><text x="320" y="263" text-anchor="middle">20</text>
    <line x1="-4" y1="224" x2="4" y2="224"/><text x="-7" y="228" text-anchor="end">1</text>
    <line x1="-4" y1="198" x2="4" y2="198"/><text x="-7" y="202" text-anchor="end">2</text>
    <line x1="-4" y1="172" x2="4" y2="172"/><text x="-7" y="176" text-anchor="end">3</text>
    <line x1="-4" y1="146" x2="4" y2="146"/><text x="-7" y="150" text-anchor="end">4</text>
    <line x1="-4" y1="120" x2="4" y2="120"/><text x="-7" y="124" text-anchor="end">5</text>
    <line x1="-4" y1="94"  x2="4" y2="94" /><text x="-7" y="98"  text-anchor="end">6</text>
    <line x1="-4" y1="68"  x2="4" y2="68" /><text x="-7" y="72"  text-anchor="end">7</text>
    <line x1="-4" y1="42"  x2="4" y2="42" /><text x="-7" y="46"  text-anchor="end">8</text>
    <line x1="-4" y1="16"  x2="4" y2="16" /><text x="-7" y="20"  text-anchor="end">9</text>
  </g>
  <!-- c(t)=-0.5t+0.03t²-0.001t³+8.688; x_svg=16t, y_svg=250-26*c(t)
       t=0: c=8.688 → y=24.1;  t=2: c=7.800 → y=47.2;  t=5: c=6.688 → y=75.6;
       t=10: c=5.188 → y=114.1; t=15: c=3.813 → y=150.9; t=20: c=2.688 → y=180.1 -->
  <polyline points="0,24.1 16,38.1 32,47.2 48,53.8 64,59.0 80,63.5 96,68.1 112,73.3 128,79.7 144,87.6 160,97.4 176,109.4 192,123.7 208,140.5 224,159.8 240,181.5 256,205.8 272,225.5 288,241.2 304,252.3 320,259.1"
    fill="none" stroke="#1e50aa" stroke-width="2.5"/>
  <!-- Key points -->
  <circle cx="0"   cy="24.1"  r="5" fill="#e02020"/>
  <text x="6"   y="22"  fill="#e02020" font-size="10">c(0)=8.688</text>
  <circle cx="32"  cy="47.2"  r="4" fill="#c86420"/>
  <text x="37"  y="44"  fill="#c86420" font-size="10">(2, 7.80)</text>
  <circle cx="320" cy="180.1" r="5" fill="#1e9657"/>
  <text x="298" y="170" fill="#1e9657" font-size="10">c(20)=2.688</text>
  <!-- Axis labels -->
  <text x="160" y="280" text-anchor="middle" font-size="12">t (hours)</text>
  <text x="-48" y="125" text-anchor="middle" font-size="12" transform="rotate(-90,-48,125)">c(t) (mg/L)</text>
  <text x="80" y="155" fill="#1e50aa" font-size="10">c(t)=−0.5t+0.03t²−0.001t³+8.688</text>
</svg>
<figcaption>Drug clearance c(t) = −0.5t + 0.03t² − 0.001t³ + 8.688 on [0, 20] h. The function is monotonically decreasing (no interior minimum) from c(0) = 8.688 to c(20) = 2.688 mg/L.</figcaption>
</figure>

*Learning point: always check whether the stationary point of $dc/dt$ actually lies in your domain. When the derivative is a quadratic function, a negative discriminant means the rate never changes sign and the function is monotonic.*

---

## Exemplar Problem 5 — Inflow–Outflow Dynamics and Long-Run Equilibrium (Weeks 6, 7)

**Context: lake nutrient dilution.**

A small lake of constant volume $V = 2{,}000{,}000$ L receives fertiliser run-off carrying nutrient at a steady rate of $5{,}000$ mg per hour. The lake is well-mixed (the concentration is uniform everywhere) and drains to a river; drainage removes nutrient at a rate proportional to the current concentration, with proportionality constant $0.05$ per hour. Let $C(t)$ denote the nutrient concentration in the lake (mg/L) at time $t$ (hours). The lake is initially clean: $C(0) = 0$.

**(a)** [3 marks] Starting from a mass balance on the nutrient in the lake (rate in minus rate out), show that the concentration satisfies
$$\frac{dC}{dt} = 0.0025 - 0.05\,C.$$

**(b)** [2 marks] Find the long-run concentration $C_{\mathrm{eq}}$ that the lake approaches as $t \to \infty$.

**(c)** [4 marks] Solve the differential equation in part (a) by separation of variables, using the initial condition $C(0) = 0$, and write $C(t)$ explicitly (no integrals or derivatives remaining).

**(d)** [3 marks] Compute the time $t_{90}$ at which the concentration reaches $90\%$ of the long-run value.

*Hint: for part (a), apply a mass balance on the nutrient ($\text{rate in} - \text{rate out}$) and divide by $V$. For part (b), set $dC/dt = 0$. For part (c), factor the right-hand side as $0.05\,(C_{\mathrm{eq}} - C)$ before separating variables — this makes the integral a single clean logarithm.*

### Solution

**Part (a) — Mass balance.**

Let $M(t)$ (mg) be the total mass of nutrient in the lake. The volume $V$ is constant and the lake is well-mixed, so $C(t) = M(t)/V$ and $dM/dt = V\,dC/dt$. The mass balance is:
$$\frac{dM}{dt} = (\text{rate in}) - (\text{rate out}) = 5000 - 0.05\,M.$$
Dividing by $V = 2 \times 10^6$:
$$\frac{dC}{dt} = \frac{5000}{2 \times 10^6} - 0.05\,\frac{M}{V} = 0.0025 - 0.05\,C.$$
$$\boxed{\,\frac{dC}{dt} = 0.0025 - 0.05\,C \quad (\text{mg/L per hour})\,}$$

**Part (b) — Long-run equilibrium concentration.**

At equilibrium, $dC/dt = 0$:
$$0 = 0.0025 - 0.05\,C_{\mathrm{eq}} \;\Longrightarrow\; \boxed{\,C_{\mathrm{eq}} = \frac{0.0025}{0.05} = 0.05\ \text{mg/L}\,}$$

**Part (c) — Explicit solution by separation of variables.**

In principle we can just separate the ODE directly:
$$\frac{dC}{0.0025 - 0.05\,C} = dt,$$
integrate both sides, and solve for $C$. That works fine. But the algebra is much cleaner — and the *meaning* of the answer much more transparent — if we first factor out the coefficient of $C$. Because $0.0025 = 0.05 \times C_{\mathrm{eq}}$ (from part (b)), we can rewrite the right-hand side as
$$\frac{dC}{dt} = 0.05\,(C_{\mathrm{eq}} - C).$$
This step is **not strictly necessary**, but it has two payoffs:

1. the integral becomes a single clean logarithm of $C_{\mathrm{eq}} - C$, and
2. it reveals the pattern at the heart of every "approach-to-equilibrium" problem: *the rate of change is proportional to the gap from equilibrium*.

Recognise that pattern once, and you can reuse it for cooling, drug infusion, pollutant dilution, and lake nutrients alike.

Separate:
$$\frac{dC}{C_{\mathrm{eq}} - C} = 0.05\,dt.$$
Integrate both sides:
$$-\ln|C_{\mathrm{eq}} - C| = 0.05\,t + A \;\Longrightarrow\; C_{\mathrm{eq}} - C = B\,e^{-0.05\,t},$$
where $B$ is a constant to be fixed by the initial condition. Apply $C(0) = 0$: $C_{\mathrm{eq}} - 0 = B \Rightarrow B = C_{\mathrm{eq}} = 0.05$. Therefore
$$\boxed{\,C(t) = C_{\mathrm{eq}}\,(1 - e^{-0.05\,t}) = 0.05\,(1 - e^{-0.05\,t}) \quad (\text{mg/L})\,}$$

**Part (d) — Time to 90% of the long-run value.**

Set $C(t_{90}) = 0.9\,C_{\mathrm{eq}} = 0.045$:
$$0.05\,(1 - e^{-0.05\,t_{90}}) = 0.045 \;\Longrightarrow\; 1 - e^{-0.05\,t_{90}} = 0.9 \;\Longrightarrow\; e^{-0.05\,t_{90}} = 0.1.$$
Take natural logs:
$$-0.05\,t_{90} = \ln(0.1) = -\ln 10 \;\Longrightarrow\; t_{90} = \frac{\ln 10}{0.05} \approx \frac{2.3026}{0.05} \approx \boxed{46.05\ \text{hours}}.$$

*Interpretation: The lake approaches $C_{\mathrm{eq}} = 0.05$ mg/L exponentially, and reaches 90% of this long-run level after about $46$ hours. The mathematical structure here — separation of variables on a linear first-order ODE, giving an exponential approach to a steady state — is the same as the draining-tank problem on the **Week 10 Mock Exam**. Revisit that paper: you should find the same setup and very similar algebra, even though the physical context is completely different.*

<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-60 -20 450 300" width="540" height="340" font-family="sans-serif" font-size="11">
  <defs>
    <marker id="ar4" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
  <!-- Axes: t in [0,120], C in [0,0.055]; scale: x_svg=3.0*t, y_svg=240-4000*C -->
  <line x1="0" y1="240" x2="385" y2="240" stroke="#333" stroke-width="1.5" marker-end="url(#ar4)"/>
  <line x1="0" y1="240" x2="0"   y2="0"   stroke="#333" stroke-width="1.5" marker-end="url(#ar4)"/>
  <text x="388" y="244" font-size="12" fill="#333">t</text>
  <text x="-4"  y="-8"  font-size="12" fill="#333" text-anchor="end">C</text>
  <!-- Ticks -->
  <g stroke="#333" stroke-width="1" font-size="10">
    <line x1="60"  y1="236" x2="60"  y2="244"/><text x="60"  y="254" text-anchor="middle">20</text>
    <line x1="120" y1="236" x2="120" y2="244"/><text x="120" y="254" text-anchor="middle">40</text>
    <line x1="138" y1="236" x2="138" y2="244"/><text x="138" y="258" text-anchor="middle" fill="#c86420">46</text>
    <line x1="180" y1="236" x2="180" y2="244"/><text x="180" y="254" text-anchor="middle">60</text>
    <line x1="240" y1="236" x2="240" y2="244"/><text x="240" y="254" text-anchor="middle">80</text>
    <line x1="300" y1="236" x2="300" y2="244"/><text x="300" y="254" text-anchor="middle">100</text>
    <line x1="360" y1="236" x2="360" y2="244"/><text x="360" y="254" text-anchor="middle">120</text>
    <!-- C ticks: 0.01→y=200, 0.02→160, 0.03→120, 0.04→80, 0.05→40 -->
    <line x1="-4" y1="200" x2="4" y2="200"/><text x="-7" y="204" text-anchor="end">0.01</text>
    <line x1="-4" y1="160" x2="4" y2="160"/><text x="-7" y="164" text-anchor="end">0.02</text>
    <line x1="-4" y1="120" x2="4" y2="120"/><text x="-7" y="124" text-anchor="end">0.03</text>
    <line x1="-4" y1="80"  x2="4" y2="80" /><text x="-7" y="84"  text-anchor="end">0.04</text>
    <line x1="-4" y1="40"  x2="4" y2="40" /><text x="-7" y="44"  text-anchor="end">0.05</text>
  </g>
  <!-- Curve C(t)=0.05*(1-exp(-0.05*t)); y_svg=240-4000*0.05*(1-exp(-0.05*t))=240-200*(1-e^{-0.05t})
       t=0:y=240; t=20:y=240-200*(1-e^{-1})=240-126.4=113.6; t=40:y=240-200*(1-e^{-2})=240-172.9=67.1
       t=60:y=240-200*(1-e^{-3})=240-190=50; t=80:y=240-200*(1-e^{-4})=240-196.3=43.7
       t=100:y=240-200*(1-e^{-5})=240-198.7=41.3; t=120:y=240-200*(1-e^{-6})=240-199.5=40.5 -->
  <polyline points="0,240 15,210.1 30,185.3 45,165.0 60,148.5 75,135.2 90,124.6 105,116.3 120,110.0 138,103.0 150,98.8 165,94.8 180,91.7 195,89.2 210,87.3 225,85.8 240,84.6 255,83.7 270,83.0 285,82.5 300,82.1 315,81.8 330,81.5 345,81.3 360,81.2"
    fill="none" stroke="#1e50aa" stroke-width="2.5"/>
  <!-- Equilibrium C_eq=0.05 → y=40 -->
  <line x1="0" y1="40" x2="370" y2="40" stroke="#c86420" stroke-width="1.8" stroke-dasharray="8,4"/>
  <text x="374" y="44" fill="#c86420" font-size="10">C_eq=0.05</text>
  <!-- 90% mark: t90≈46.05, C=0.045 → y_svg=240-200*0.9=240-180=60 -->
  <circle cx="138" cy="60" r="5" fill="#e02020"/>
  <line x1="138" y1="60"  x2="138" y2="240" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="0"   y1="60"  x2="138" y2="60"  stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="141" y="57" fill="#e02020" font-size="10">t₉₀≈46 h, C=0.045</text>
  <!-- Origin dot -->
  <circle cx="0" cy="240" r="4" fill="#333"/>
  <!-- Axis labels -->
  <text x="185" y="278" text-anchor="middle" font-size="12">t (hours)</text>
  <text x="-52" y="120" text-anchor="middle" font-size="12" transform="rotate(-90,-52,120)">C(t) (mg/L)</text>
  <text x="70" y="155" fill="#1e50aa" font-size="10">C(t)=0.05(1−e^{−0.05t})</text>
</svg>
<figcaption>Lake nutrient concentration C(t) = 0.05(1 − e<sup>−0.05t</sup>) approaching equilibrium C<sub>eq</sub> = 0.05 mg/L. The red dot marks t₉₀ ≈ 46 hours, when C reaches 90% of the long-run value.</figcaption>
</figure>
