# Week 8: Predator-Prey Dynamics and Systems

## Act III: Predicting Interactions — Chapter 1

> *"In nature, no species exists in isolation. The lynx pursues the hare, populations rise and fall in perpetual dance. Mathematics reveals the hidden choreography."*

---

## Theme: "Predator-Prey Dynamics and Systems of ODEs"

**Science Context:** Lynx-snowshoe hare cycles, feral cat and numbat interactions, dingo and kangaroo dynamics

**Learning Outcomes:** At the end of this week you should be able to:

1. Describe interacting species systems using coupled first-order ordinary differential equations
2. Identify equilibrium points of a two-species system and qualitatively analyse their stability
3. Construct and interpret phase portraits and trajectory diagrams in state space
4. Apply the Lotka-Volterra predator-prey model to real ecological systems
5. Draw and interpret nullclines for a two-species system
6. Discuss the biological implications of cyclic predator-prey population dynamics

---

> **📓 About "Try it in Python" boxes:** Throughout this lesson, these boxes reference specific code examples by ID — e.g. **W8-CS03** means *Week 8, Code Snippet 3*. Find the matching code under **Notes → Python Code Snippets** for this week; each entry there is labelled with its ID.

## 1. From Single Populations to Interacting Systems

### The Story So Far

In previous weeks, we modeled single populations:

| Model       | Equation                                         | Behavior                            |
| ----------- | ------------------------------------------------ | ----------------------------------- |
| Exponential | $\frac{dN}{dt} = rN$                             | Unlimited growth/decay              |
| Logistic    | $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$ | Bounded growth to carrying capacity |
| Schaefer    | $G(S) = gS\left(1 - \frac{S}{K}\right)$          | Sustainable yield framework         |

**The limitation:** These models treat populations as isolated. In reality, species interact—predators depend on prey, and prey are consumed by predators.

### This Week's Challenge

How do we model systems where **two populations influence each other**?

**Examples of predator-prey systems:**
- Canadian lynx and snowshoe hare
- Wolves and deer
- Sharks and fish
- Herbivorous and piscivorous fish
- Even humans exploiting fish stocks (fishery models)

---

## 2. State Space: The Geometry of Behavior

Before diving into the Lotka-Volterra equations, we need to understand how to visualize systems with **two changing quantities**.

### 2.1 One-Dimensional State Space

For a single population $N(t)$, the **state** at any time is just a point on a number line:

$$\text{State space: } \mathbb{R}^+ = [0, \infty)$$

A **trajectory** shows how the population moves along this line over time.

### 2.2 Two-Dimensional State Space

For two interacting populations (prey $H$ and predator $P$), the state is a point in the plane:

$$\text{State: } S = (H, P) \in \mathbb{R}^+ \times \mathbb{R}^+$$

Each point represents a specific combination of prey and predator numbers. As time passes, the system traces out a **trajectory** through this 2D space.

### 2.3 The Dog's Emotional State (An Analogy)

Consider the Lorenz-Zeeman model of a dog's emotional state, characterized by:
- **Rage** (fang exposure)
- **Fear** (ear attitude)

A dog walking calmly starts at state $(r_0, f_0) = (1, 1)$. When a child startles it, fear increases to $(1, 3)$. Cornered, rage increases to $(3, 3)$. As the child flees, the dog's state evolves.

**Key insight:** The trajectory in state space tells the story of how the system evolves!

---

## 3. The Lotka-Volterra Model

### 3.0 The Origin of the Model

The Lotka-Volterra equations have a remarkable history of **independent discovery**, each motivated by real-world problems.

**Alfred Lotka (1880–1949):** An American mathematician and physical chemist, Lotka was studying oscillating chemical reactions and biological systems. In his 1925 book *Elements of Physical Biology* he published the coupled differential equations that now bear his name, framing them as a general model for any two-species interaction.

**Vito Volterra (1860–1940):** An Italian mathematician of great distinction, Volterra arrived at the same equations in 1926 through an entirely different route — and through a personal connection. His future son-in-law, the marine biologist **Umberto D'Ancona**, had been puzzling over data from Adriatic Sea fisheries:

> *"During World War I (1914–1918), large-scale commercial fishing in the Adriatic virtually ceased. When fishing resumed after the war, fishermen reported a striking increase in the proportion of predatory fish — sharks, rays, and skates — in their catches."*

D'Ancona asked Volterra: can mathematics explain this? Volterra's answer was elegant — reducing fishing (acting as a shared predator on both species) releases prey fish from human pressure; prey abundance rises; predatory fish thrive. The two-species feedback generates a new dynamic.

**Why this matters:** The same equations discovered independently, for different reasons, by people in different countries is one of the strongest signals in science that a mathematical structure is capturing something genuinely real. The Lotka-Volterra model is now a cornerstone of theoretical ecology.

---

### 3.1 Model Setup

The **Lotka-Volterra model** (circa 1920s) describes predator-prey dynamics using two coupled ordinary differential equations (ODEs).

Let:
- $H$ = prey (Herbivore) population
- $P$ = predator population

$$\boxed{\frac{dH}{dt} = \alpha H - \beta HP}$$

$$\boxed{\frac{dP}{dt} = \lambda HP - \gamma P}$$

### 3.2 Parameter Interpretation

| Parameter           | Symbol    | Meaning                                                 | Units                 |
| ------------------- | --------- | ------------------------------------------------------- | --------------------- |
| Prey birth rate     | $\alpha$  | Natural reproduction rate of prey (without predation)   | per time              |
| Predation rate      | $\beta$   | Rate at which encounters lead to prey death             | per predator per time |
| Predator efficiency | $\lambda$ | Rate at which prey consumption leads to predator births | per prey per time     |
| Predator death rate | $\gamma$  | Natural death rate of predator (without food)           | per time              |

### 3.3 Understanding Each Term

**Prey equation:** $\frac{dH}{dt} = \underbrace{\alpha H}_{\text{births}} - \underbrace{\beta HP}_{\text{deaths from predation}}$

- Without predators ($P = 0$): prey grows exponentially at rate $\alpha$
- The term $\beta HP$ represents a "mass action" effect—more encounters when both populations are large

**Predator equation:** $\frac{dP}{dt} = \underbrace{\lambda HP}_{\text{births from feeding}} - \underbrace{\gamma P}_{\text{natural deaths}}$

- Without prey ($H = 0$): predator decays exponentially at rate $\gamma$
- Predator births depend on successful hunting ($\lambda HP$)

### 3.4 Predator Efficiency

The **efficiency of predation** measures how effectively the predator converts consumed prey into new predators:

$$\boxed{\epsilon = \frac{\lambda}{\beta}}$$

**Interpretation:**
- $\beta HP$ = number of prey killed per unit time
- $\lambda HP$ = number of predators born per unit time
- $\epsilon = \frac{\lambda HP}{\beta HP} = \frac{\lambda}{\beta}$ = predators born per prey killed

**Example:** If $\lambda = 0.0005$ and $\beta = 0.005$, then:
$$\epsilon = \frac{0.0005}{0.005} = 0.1 = 10\%$$

This means for every 10 prey consumed, 1 new predator is born.

> **📓 Try it in Python**
>
> Build and simulate the Lotka-Volterra system:
> - **W8-CS01** — *Setting Up Lotka-Volterra Parameters*: Define symbols and biological parameters.
> - **W8-CS02** — *Defining the ODE System*: Write the predator-prey equations for `odeint`.
> - **W8-CS03** — *Solving the ODEs*: Integrate over time to get population trajectories.
> - **W8-CS09** — *Verifying Equilibrium Points*: Confirm fixed points algebraically and numerically.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 4. Finding Equilibrium (Fixed) Points

### 4.1 What is an Equilibrium?

An **equilibrium** or **fixed point** is a state where both populations remain constant over time:

$$\frac{dH}{dt} = 0 \quad \text{AND} \quad \frac{dP}{dt} = 0$$

### 4.2 Solving for Equilibria

**From the prey equation:**
$$\frac{dH}{dt} = \alpha H - \beta HP = H(\alpha - \beta P) = 0$$

This gives: $H = 0$ **or** $P = \frac{\alpha}{\beta}$

**From the predator equation:**
$$\frac{dP}{dt} = \lambda HP - \gamma P = P(\lambda H - \gamma) = 0$$

This gives: $P = 0$ **or** $H = \frac{\gamma}{\lambda}$

### 4.3 The Two Equilibrium Points

Combining these conditions yields exactly **two equilibrium points**:

$$\boxed{(H^*, P^*) = (0, 0) \quad \text{(Extinction)}}$$

$$\boxed{(H^*, P^*) = \left(\frac{\gamma}{\lambda}, \frac{\alpha}{\beta}\right) \quad \text{(Coexistence)}}$$

### 4.4 Example Calculation

**Given parameters:** $\alpha = 0.15$, $\beta = 0.005$, $\lambda = 0.0005$, $\gamma = 0.10$

**Extinction equilibrium:** $(H, P) = (0, 0)$

**Coexistence equilibrium:**
$$H^* = \frac{\gamma}{\lambda} = \frac{0.10}{0.0005} = 200$$

$$P^* = \frac{\alpha}{\beta} = \frac{0.15}{0.005} = 30$$

So $(H^*, P^*) = (200, 30)$ is the interior equilibrium.

**Verification:** Substitute back:
- $\frac{dH}{dt} = 0.15(200) - 0.005(200)(30) = 30 - 30 = 0$ ✓
- $\frac{dP}{dt} = 0.0005(200)(30) - 0.10(30) = 3 - 3 = 0$ ✓

---

## 5. Phase Portraits and Direction Fields

### 5.1 The Phase Portrait

A **phase portrait** shows how the system evolves from any initial state. It consists of:
1. **Fixed points** (equilibria)
2. **Trajectories** (paths the system follows from different starting points)
3. **Direction field** (arrows showing instantaneous direction of motion)

### 5.2 Constructing a Direction Field

At any point $(H, P)$, we can compute:
- $\frac{dH}{dt}$ = rate of change in prey
- $\frac{dP}{dt}$ = rate of change in predator

The **direction** of motion is the vector $\left(\frac{dH}{dt}, \frac{dP}{dt}\right)$.

The **slope** of the trajectory at that point is:
$$\frac{dP}{dH} = \frac{dP/dt}{dH/dt} = \frac{\lambda HP - \gamma P}{\alpha H - \beta HP} = \frac{P(\lambda H - \gamma)}{H(\alpha - \beta P)}$$

### 5.3 Determining Direction of Flow

To place arrows correctly on a phase diagram, determine the **signs** of $\frac{dH}{dt}$ and $\frac{dP}{dt}$:

**For prey ($H$):**
$$\frac{dH}{dt} = H(\alpha - \beta P) \begin{cases} > 0 & \text{if } P < \frac{\alpha}{\beta} \text{ (H increasing)} \\ = 0 & \text{if } P = \frac{\alpha}{\beta} \text{ (H constant)} \\ < 0 & \text{if } P > \frac{\alpha}{\beta} \text{ (H decreasing)} \end{cases}$$

**For predator ($P$):**
$$\frac{dP}{dt} = P(\lambda H - \gamma) \begin{cases} > 0 & \text{if } H > \frac{\gamma}{\lambda} \text{ (P increasing)} \\ = 0 & \text{if } H = \frac{\gamma}{\lambda} \text{ (P constant)} \\ < 0 & \text{if } H < \frac{\gamma}{\lambda} \text{ (P decreasing)} \end{cases}$$

### 5.4 The Four Quadrants

The lines $H = \frac{\gamma}{\lambda}$ (vertical) and $P = \frac{\alpha}{\beta}$ (horizontal) divide the positive quadrant into four regions:

| Region | H relative to $\frac{\gamma}{\lambda}$ | P relative to $\frac{\alpha}{\beta}$ | dH/dt | dP/dt | Direction |
| ------ | -------------------------------------- | ------------------------------------ | ----- | ----- | --------- |
| I      | $H > \frac{\gamma}{\lambda}$           | $P < \frac{\alpha}{\beta}$           | +     | +     | ↗ (NE)    |
| II     | $H > \frac{\gamma}{\lambda}$           | $P > \frac{\alpha}{\beta}$           | −     | +     | ↖ (NW)    |
| III    | $H < \frac{\gamma}{\lambda}$           | $P > \frac{\alpha}{\beta}$           | −     | −     | ↙ (SW)    |
| IV     | $H < \frac{\gamma}{\lambda}$           | $P < \frac{\alpha}{\beta}$           | +     | −     | ↘ (SE)    |

This creates a **counterclockwise** flow around the interior equilibrium!

### 5.5 Reading a Phase Portrait

For the basic Lotka-Volterra model:
- Trajectories form **closed orbits** around the coexistence equilibrium
- The system exhibits **sustained periodic oscillations**
- Different initial conditions lead to different orbit sizes
- The populations never settle down—they oscillate forever

![Lotka-Volterra Phase Portrait](images/lotka_volterra_phase.svg "Phase portrait showing closed orbits around the equilibrium point, with direction field indicating counterclockwise flow")

### 5.6 Nullclines: Named Curves in the Phase Plane

A **nullcline** (from Latin *nullus* = zero) is a curve along which **one derivative equals zero** — a useful tool for finding equilibria and sketching direction fields without computing exact trajectories.

**H-nullcline (prey nullcline):** The set of all points where $\frac{dH}{dt} = 0$

$$H(\alpha - \beta P) = 0 \implies H = 0 \text{ (trivial) or } P = \frac{\alpha}{\beta} \text{ (non-trivial)}$$

The non-trivial H-nullcline is the **horizontal line** $P = \dfrac{\alpha}{\beta}$.

Along this line, prey are neither increasing nor decreasing — only the predator is changing. Trajectories cross the H-nullcline **vertically** (moving straight up or down).

**P-nullcline (predator nullcline):** The set of all points where $\frac{dP}{dt} = 0$

$$P(\lambda H - \gamma) = 0 \implies P = 0 \text{ (trivial) or } H = \frac{\gamma}{\lambda} \text{ (non-trivial)}$$

The non-trivial P-nullcline is the **vertical line** $H = \dfrac{\gamma}{\lambda}$.

Along this line, the predator population is momentarily stationary. Trajectories cross the P-nullcline **horizontally** (moving straight left or right).

**Key insight:** The intersection of the two non-trivial nullclines is the coexistence equilibrium:

$$P = \frac{\alpha}{\beta} \text{ and } H = \frac{\gamma}{\lambda} \quad \Longrightarrow \quad (H^*, P^*) = \left(\frac{\gamma}{\lambda},\, \frac{\alpha}{\beta}\right)$$

Nullclines are powerful because they pinpoint equilibria geometrically and partition the phase plane into the four quadrants of Section 5.4 — each quadrant bounded by a nullcline pair.

> **📓 Try it in Python**
>
> Visualize the dynamics in phase space and time:
> - **W8-CS04** — *Plotting Time Series*: Show how prey and predator populations oscillate over time.
> - **W8-CS05** — *Creating a Phase Portrait (Basic)*: Plot trajectories in the $H$-$P$ plane.
> - **W8-CS06** — *Adding Arrows to Phase Portrait*: Indicate direction of flow on trajectories.
> - **W8-CS07** — *Building a Vector Field*: Sample $(\dot H, \dot P)$ across the phase plane.
> - **W8-CS08** — *Complete Phase Portrait*: Combine vector field with multiple trajectories.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 6. Qualitative Behavior: Time Series

### 6.1 From Phase Portrait to Time Series

The phase portrait shows the path in $(H, P)$ space. A **time series** shows how each population changes over time $t$.

For basic Lotka-Volterra:
- Both populations oscillate periodically
- Prey peaks **lead** predator peaks (prey increase → more food → predator increase → more predation → prey decrease → less food → predator decrease → cycle repeats)
- The phase lag is approximately 1/4 of the period

![Predator-Prey Time Series](images/predator_prey_timeseries.svg "Time series showing oscillating prey and predator populations with characteristic phase lag")

### 6.2 The Hudson Bay Data

Historical fur trading data from Hudson's Bay Company shows approximately 10-year cycles for Canadian lynx and snowshoe hare—remarkably consistent with Lotka-Volterra predictions!

**Quantitative picture:** Analysis of records from 1845–1935 reveals:
- Snowshoe hare populations oscillate between roughly **2,000 and 150,000 individuals per 100 km²** — a 75-fold amplitude
- Canadian lynx populations oscillate between roughly **500 and 8,000 individuals per 100 km²** — a 16-fold amplitude
- The cycle period is approximately **9–11 years**
- Lynx peaks follow hare peaks by approximately **1–2 years**, consistent with the model's prediction of a quarter-cycle phase lag

These numbers show just how dramatic predator-prey cycling can be in real ecosystems — population sizes changing by orders of magnitude in just a few years.

However, real data also shows:
- Irregular cycle lengths
- Varying amplitudes
- Spatial synchronization effects

These complexities arise from factors the basic model ignores.

---

## 7. Limitations and Extensions

### 7.1 Assumptions of Basic Lotka-Volterra

The model makes several simplifying assumptions:

1. **Exponential prey growth** without predators (unrealistic—ignores carrying capacity)
2. **Unlimited predator appetite** (no satiation)
3. **Only two species** (ignores food web complexity)
4. **No age structure** (all individuals are equivalent)
5. **No migration** (closed system)
6. **Deterministic** (no random events like disease, fire)
7. **Homogeneous space** (no spatial structure)

### 7.2 Extension: Adding Carrying Capacity

We can make prey growth logistic instead of exponential:

$$\frac{dH}{dt} = \alpha H \left(1 - \frac{H}{K}\right) - \beta HP$$

$$\frac{dP}{dt} = \lambda HP - \gamma P$$

### 7.3 New Equilibria with Carrying Capacity

Setting both derivatives to zero:

**Three equilibrium points:**

1. **Both extinct:** $(H, P) = (0, 0)$

2. **Predator extinct, prey at capacity:** $(H, P) = (K, 0)$

3. **Coexistence (interior):**
$$H^* = \frac{\gamma}{\lambda}$$
$$P^* = \frac{\alpha}{\beta}\left(1 - \frac{\gamma}{\lambda K}\right) = \frac{\alpha}{\beta}\left(1 - \frac{H^*}{K}\right)$$

### 7.4 Changed Behavior

With carrying capacity:
- Orbits are no longer closed—they **spiral inward**
- The system converges to the interior equilibrium
- Oscillations are **damped** rather than sustained
- The coexistence point becomes an **attractor**

**Example:** With $\alpha = 0.2$, $\beta = 0.005$, $\lambda = 0.001$, $\gamma = 0.6$, $K = 1500$:

$$H^* = \frac{0.6}{0.001} = 600$$

$$P^* = \frac{0.2}{0.005}\left(1 - \frac{600}{1500}\right) = 40 \times 0.6 = 24$$

---

### 7.5 Australian Application: Feral Cats and Small Marsupials

Australia provides some of the most dramatic and ecologically urgent predator-prey dynamics in the world. Feral cats (*Felis catus*), introduced with European settlement, are estimated to kill **1.4–1.5 billion native animals per year** (Woinarski et al. 2017), making them a leading cause of mammal extinction on the continent.

A simplified Lotka-Volterra model for feral cats ($P$, predator) preying on small marsupials such as the bilby or numbat ($H$, prey) might use illustrative parameters:

| Parameter            | Symbol    | Value     | Meaning                    |
| -------------------- | --------- | --------- | -------------------------- |
| Marsupial birth rate | $\alpha$  | 0.50 /yr  | Natural reproduction       |
| Predation rate       | $\beta$   | 0.020 /yr | Per cat per prey           |
| Predator efficiency  | $\lambda$ | 0.002 /yr | Cat births per prey killed |
| Cat death rate       | $\gamma$  | 0.30 /yr  | Natural cat mortality      |

**Coexistence equilibrium:**
$$H^* = \frac{\gamma}{\lambda} = \frac{0.30}{0.002} = 150 \text{ marsupials per km}^2$$

$$P^* = \frac{\alpha}{\beta} = \frac{0.50}{0.020} = 25 \text{ cats per km}^2$$

**Predator efficiency:** $\epsilon = \dfrac{\lambda}{\beta} = \dfrac{0.002}{0.020} = 10\%$

**Effect of culling:** A cat-control programme that increases the effective cat death rate from $\gamma = 0.30$ to $\gamma = 0.45$ (via baiting or trapping) raises the equilibrium prey population:

$$H^*_\text{new} = \frac{0.45}{0.002} = 225 \text{ marsupials per km}^2$$

This is the key management insight from the model: **reducing predator survival allows prey equilibrium to rise.**

**Why the basic model is insufficient here:** In practice, introduced cat–marsupial interactions rarely produce the sustained oscillations the model predicts. Instead, many marsupial species have been driven to extinction, for three reasons the model ignores:
1. Cats are **generalist predators** — they switch to abundant alternative prey (rabbits, mice) when target marsupial populations fall, preventing the "predator crash" that would allow prey to recover.
2. Small marsupials have **low carrying capacities** — small population sizes mean stochastic events (drought, disease) can push them below viable thresholds.
3. Australian marsupials have **no evolutionary history** with cats — they lack antipredator behaviours that co-evolved prey exhibit.

This case illustrates a profound lesson: understanding when and why a model's predictions fail is as scientifically important as applying it when it succeeds.

> **📓 Try it in Python**
>
> Extend the model with realistic constraints:
> - **W8-CS10** — *Modified Model with Carrying Capacity*: Add a logistic term and observe how equilibria shift.
>
> Find these under **Notes → Python Code Snippets** for this week.

---

## 8. Connection to Scientific Method

### 8.1 Model as Hypothesis

The Lotka-Volterra model is a **mathematical hypothesis** about how predator-prey systems work:

1. **Observation:** Lynx and hare populations oscillate
2. **Hypothesis:** Oscillations arise from predator-prey feedback
3. **Model:** Lotka-Volterra equations
4. **Prediction:** Periodic cycles with specific phase relationships
5. **Test:** Compare with Hudson Bay data

### 8.2 Model Refinement

When basic predictions don't match data perfectly, we:
- Add carrying capacity (damped oscillations)
- Include stochastic effects (irregular amplitudes)
- Consider spatial structure (traveling waves)

This is the iterative cycle of scientific modeling!

---

## 9. Summary: Key Formulas

| Concept                  | Formula                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Prey equation            | $\frac{dH}{dt} = \alpha H - \beta HP$                                                                          |
| Predator equation        | $\frac{dP}{dt} = \lambda HP - \gamma P$                                                                        |
| Predator efficiency      | $\epsilon = \frac{\lambda}{\beta}$                                                                             |
| Extinction equilibrium   | $(H^*, P^*) = (0, 0)$                                                                                          |
| Coexistence equilibrium  | $(H^*, P^*) = \left(\frac{\gamma}{\lambda}, \frac{\alpha}{\beta}\right)$                                       |
| Prey increasing when     | $P < \frac{\alpha}{\beta}$                                                                                     |
| Predator increasing when | $H > \frac{\gamma}{\lambda}$                                                                                   |
| With carrying capacity K | Interior: $\left(\frac{\gamma}{\lambda}, \frac{\alpha}{\beta}\left(1 - \frac{\gamma}{\lambda K}\right)\right)$ |

---
