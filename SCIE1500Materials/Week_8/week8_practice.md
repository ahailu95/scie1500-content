# Week 8 Practice Questions: Predator-Prey Dynamics and Systems

**Theme:** When Populations Interact

**Exam Alignment:** Q34

---

## Learning Objectives

This week's practice addresses common student challenges:
- Direction of arrows on phase diagrams
- Computing predator efficiency
- Verifying equilibrium points
- Understanding oscillatory behavior

---

## Foundational Questions (8)

### Q1. Model Interpretation

In the Lotka-Volterra model $\frac{dH}{dt} = \alpha H - \beta HP$, what does the term $\beta HP$ represent?

**Options:**
- (A) The birth rate of prey
- (B) The death rate of predators
- (C) The rate at which prey are killed by predators
- (D) The natural death rate of prey
- (E) The carrying capacity effect

---

### Q2. Special Case — No Predators

In the Lotka-Volterra model, if there are no predators ($P = 0$), what happens to the prey population?

**Options:**
- (A) It decreases exponentially
- (B) It grows exponentially
- (C) It remains constant
- (D) It grows logistically to a carrying capacity
- (E) It oscillates

---

### Q3. Special Case — No Prey

In the Lotka-Volterra model, if there is no prey ($H = 0$), what happens to the predator population?

**Options:**
- (A) It grows exponentially
- (B) It remains constant
- (C) It decays exponentially
- (D) It grows logistically
- (E) It oscillates periodically

---

### Q4. Equilibrium Concept

What condition defines an equilibrium point in a dynamical system?

**Options:**
- (A) The populations are at their maximum values
- (B) Both rates of change equal zero
- (C) The prey equals the predator population
- (D) The system is oscillating
- (E) The efficiency equals 100%

---

### Q5. Equilibrium Calculation — Prey

For the Lotka-Volterra model with $\alpha = 0.2$, $\beta = 0.005$, $\gamma = 0.6$, $\lambda = 0.001$, what is the prey population at the non-trivial (coexistence) equilibrium?

**Options:**
- (A) $H^* = 40$
- (B) $H^* = 200$
- (C) $H^* = 400$
- (D) $H^* = 600$
- (E) $H^* = 1000$

---

### Q6. Equilibrium Calculation — Predator

For the Lotka-Volterra model with $\alpha = 0.2$, $\beta = 0.005$, $\gamma = 0.6$, $\lambda = 0.001$, what is the predator population at the coexistence equilibrium?

**Options:**
- (A) $P^* = 20$
- (B) $P^* = 30$
- (C) $P^* = 40$
- (D) $P^* = 50$
- (E) $P^* = 60$

---

### Q7. Efficiency Definition

The predator efficiency in the Lotka-Volterra model is defined as:

**Options:**
- (A) $\frac{\alpha}{\gamma}$
- (B) $\frac{\beta}{\lambda}$
- (C) $\frac{\lambda}{\beta}$
- (D) $\frac{\gamma}{\alpha}$
- (E) $\frac{\alpha \lambda}{\beta \gamma}$

---

### Q8. Efficiency Calculation

If $\lambda = 0.0005$ and $\beta = 0.005$, what is the predator efficiency?

**Options:**
- (A) 1%
- (B) 5%
- (C) 10%
- (D) 50%
- (E) 100%

---

## Intermediate Questions (8)

### Q9. Equilibrium Verification

Consider the Lotka-Volterra model with $\alpha = 0.15$, $\beta = 0.005$, $\lambda = 0.0005$, $\gamma = 0.10$. Is $(H, P) = (200, 30)$ an equilibrium point?

**Options:**
- (A) Yes, both derivatives equal zero at this point
- (B) No, $\frac{dH}{dt} \neq 0$ at this point
- (C) No, $\frac{dP}{dt} \neq 0$ at this point
- (D) No, neither derivative equals zero
- (E) Cannot determine without solving the ODEs

---

### Q10. Direction Field — Northeast

At a point where $H > \frac{\gamma}{\lambda}$ and $P < \frac{\alpha}{\beta}$, which direction does the system move?

**Options:**
- (A) Northeast (H increasing, P increasing)
- (B) Northwest (H decreasing, P increasing)
- (C) Southwest (H decreasing, P decreasing)
- (D) Southeast (H increasing, P decreasing)
- (E) The system stays stationary

---

### Q11. Direction Field — Southwest

At a point where $H < \frac{\gamma}{\lambda}$ and $P > \frac{\alpha}{\beta}$, which direction does the system move?

**Options:**
- (A) Northeast (H increasing, P increasing)
- (B) Northwest (H decreasing, P increasing)
- (C) Southwest (H decreasing, P decreasing)
- (D) Southeast (H increasing, P decreasing)
- (E) The system oscillates in place

---

### Q12. Phase Portrait Behavior

In the basic Lotka-Volterra model (without carrying capacity), trajectories around the coexistence equilibrium are:

**Options:**
- (A) Straight lines approaching the equilibrium
- (B) Spirals converging to the equilibrium
- (C) Spirals diverging from the equilibrium
- (D) Closed orbits (cycles) around the equilibrium
- (E) Random paths with no pattern

---

### Q13. Carrying Capacity Effect

When carrying capacity $K$ is added to the Lotka-Volterra model (prey equation becomes $\frac{dH}{dt} = \alpha H(1 - H/K) - \beta HP$), what changes about the system behavior?

**Options:**
- (A) Oscillations become larger over time
- (B) Oscillations dampen and the system approaches equilibrium
- (C) The system no longer has an equilibrium
- (D) The predator always goes extinct
- (E) The behavior is unchanged

---

### Q14. Carrying Capacity Equilibria

With carrying capacity $K$, the modified Lotka-Volterra model has how many equilibrium points (in the biologically meaningful region $H \geq 0$, $P \geq 0$)?

**Options:**
- (A) One
- (B) Two
- (C) Three
- (D) Four
- (E) Infinitely many

---

### Q15. Arrow Placement on Phase Diagrams

On a phase diagram, an arrow at point $(H, P)$ should point in a direction with slope equal to:

**Options:**
- (A) $\frac{dH}{dt}$
- (B) $\frac{dP}{dt}$
- (C) $\frac{dH}{dt} \cdot \frac{dP}{dt}$
- (D) $\frac{dP/dt}{dH/dt}$
- (E) $\frac{dH/dt}{dP/dt}$

---

### Q16. Ecological Interpretation

In the predator-prey cycle, why do predator population peaks typically lag behind prey population peaks?

**Options:**
- (A) Predators migrate more slowly than prey
- (B) Predator birth rate depends on current prey abundance
- (C) Prey have a longer gestation period
- (D) Predators are more resistant to environmental changes
- (E) Both populations are controlled by the same external factor

---

## Exam-Style Questions (4)

### Q17. Complete Analysis (Q34 Style) — 12 marks

Consider the Lotka-Volterra model:

$$\frac{dH}{dt} = \alpha H - \beta HP$$
$$\frac{dP}{dt} = \lambda HP - \gamma P$$

with parameters $\alpha = 0.15$, $\beta = 0.005$, $\lambda = 0.0005$, $\gamma = 0.10$.

**(a)** Show that $(H, P) = (0, 0)$ is an equilibrium point.

**(b)** Find the coexistence equilibrium $(H^*, P^*)$.

**(c)** Calculate the predator efficiency.

**(d)** Describe the behavior of the system when starting from a non-equilibrium point.

---

### Q18. True/False Analysis (Q34 Style) — 8 marks

For the model in Q17, determine which of the following statements is **NOT** true:

**(a)** $H = 0$, $P = 0$ is a fixed point for this system.

**(b)** $H = 200$, $P = 30$ is a fixed point for this system.

**(c)** The efficiency of predation is 10%.

**(d)** The efficiency of predation is 0.05%.

**(e)** If the initial point is not a fixed point, the populations oscillate with constant amplitudes forever.

---

### Q19. Carrying Capacity Modification — 12 marks

Consider the modified Lotka-Volterra model with carrying capacity:

$$\frac{dH}{dt} = \alpha H\left(1 - \frac{H}{K}\right) - \beta HP$$
$$\frac{dP}{dt} = \lambda HP - \gamma P$$

with $\alpha = 0.2$, $\beta = 0.005$, $\gamma = 0.6$, $\lambda = 0.001$, and $K = 1500$.

**(a)** Find all equilibrium points.

**(b)** Calculate the predator population at the coexistence equilibrium.

**(c)** Compare this to the basic model (without K). How does carrying capacity affect the equilibrium predator population?

---

### Q20. Direction Field Analysis — 12 marks

For the basic Lotka-Volterra model with coexistence equilibrium at $(H^*, P^*) = (600, 40)$:

**(a)** Divide the phase plane into four regions using the nullclines. What are the equations of these nullclines?

**(b)** In which region(s) is the prey population increasing?

**(c)** In which region(s) is the predator population decreasing?

**(d)** Describe the overall flow pattern and explain why closed orbits form.

---

## Answer Key

### Multiple Choice

| Q | Answer | Q | Answer |
|---|--------|---|--------|
| 1 | C | 9 | A |
| 2 | B | 10 | A |
| 3 | C | 11 | C |
| 4 | B | 12 | D |
| 5 | D | 13 | B |
| 6 | C | 14 | C |
| 7 | C | 15 | D |
| 8 | C | 16 | B |

### Exam-Style

| Q | Answer |
|---|--------|
| 17 | See detailed solution |
| 18 | Statement (d) is NOT true |
| 19 | See detailed solution |
| 20 | See detailed solution |

---

## Detailed Solutions

### Q1. Model Interpretation
The term $\beta HP$ represents the **mass action** effect of predation:
- $\beta$ is the predation rate coefficient
- $H$ is the prey population
- $P$ is the predator population

The product $HP$ captures the idea that more encounters (and thus more predation events) occur when both populations are larger. This term reduces the prey population, hence it appears with a negative sign.

**Answer: C**

---

### Q2. Special Case — No Predators
When $P = 0$, the prey equation becomes:
$$\frac{dH}{dt} = \alpha H - \beta H(0) = \alpha H$$

This is **exponential growth** with solution $H(t) = H_0 e^{\alpha t}$.

**Answer: B**

---

### Q3. Special Case — No Prey
When $H = 0$, the predator equation becomes:
$$\frac{dP}{dt} = \lambda (0) P - \gamma P = -\gamma P$$

This is **exponential decay** with solution $P(t) = P_0 e^{-\gamma t}$.

**Biological interpretation:** Without food, predators starve and die off.

**Answer: C**

---

### Q4. Equilibrium Concept
An **equilibrium** is a state where the system does not change over time:
$$\frac{dH}{dt} = 0 \quad \text{AND} \quad \frac{dP}{dt} = 0$$

**Answer: B**

---

### Q5. Equilibrium Calculation — Prey
From the predator equation at equilibrium with $P \neq 0$:
$$\lambda H = \gamma \Rightarrow H^* = \frac{\gamma}{\lambda} = \frac{0.6}{0.001} = 600$$

**Answer: D**

---

### Q6. Equilibrium Calculation — Predator
From the prey equation at equilibrium with $H \neq 0$:
$$\alpha = \beta P \Rightarrow P^* = \frac{\alpha}{\beta} = \frac{0.2}{0.005} = 40$$

**Answer: C**

---

### Q7. Efficiency Definition
Predator efficiency measures predators born per prey killed:
$$\epsilon = \frac{\text{Predators born}}{\text{Prey killed}} = \frac{\lambda HP}{\beta HP} = \frac{\lambda}{\beta}$$

**Answer: C**

---

### Q8. Efficiency Calculation
$$\epsilon = \frac{\lambda}{\beta} = \frac{0.0005}{0.005} = 0.1 = 10\%$$

**Interpretation:** For every 10 prey consumed, 1 new predator is born.

**Answer: C**

---

### Q9. Equilibrium Verification
**Check prey equation:**
$$\frac{dH}{dt} = 0.15(200) - 0.005(200)(30) = 30 - 30 = 0 \checkmark$$

**Check predator equation:**
$$\frac{dP}{dt} = 0.0005(200)(30) - 0.10(30) = 3 - 3 = 0 \checkmark$$

Both derivatives are zero, so $(200, 30)$ **is** an equilibrium.

**Answer: A**

---

### Q10. Direction Field — Northeast
- Since $P < \frac{\alpha}{\beta}$: $\frac{dH}{dt} > 0$ → H increasing
- Since $H > \frac{\gamma}{\lambda}$: $\frac{dP}{dt} > 0$ → P increasing

**Combined:** System moves **Northeast** (↗)

**Answer: A**

---

### Q11. Direction Field — Southwest
- $P > \frac{\alpha}{\beta}$ → $\frac{dH}{dt} < 0$ (H decreasing)
- $H < \frac{\gamma}{\lambda}$ → $\frac{dP}{dt} < 0$ (P decreasing)

This is the "crash" phase where both populations are declining.

**Answer: C**

---

### Q12. Phase Portrait Behavior
In the basic Lotka-Volterra model, trajectories form **closed orbits** around the coexistence equilibrium:
- Perpetual periodic oscillations
- The equilibrium is a **center** (neutrally stable)

**Answer: D**

---

### Q15. Arrow Placement
The **slope** of the trajectory at any point is:
$$\text{slope} = \frac{dP}{dH} = \frac{dP/dt}{dH/dt}$$

**Answer: D**

---

### Q17. Complete Analysis — Solution

**(a) Verify $(0, 0)$:**
$$\frac{dH}{dt}\bigg|_{(0,0)} = 0.15(0) - 0.005(0)(0) = 0 \checkmark$$
$$\frac{dP}{dt}\bigg|_{(0,0)} = 0.0005(0)(0) - 0.10(0) = 0 \checkmark$$

**(b) Coexistence equilibrium:**

From $\frac{dP}{dt} = P(\lambda H - \gamma) = 0$ with $P \neq 0$:
$$H^* = \frac{\gamma}{\lambda} = \frac{0.10}{0.0005} = 200$$

From $\frac{dH}{dt} = H(\alpha - \beta P) = 0$ with $H \neq 0$:
$$P^* = \frac{\alpha}{\beta} = \frac{0.15}{0.005} = 30$$

$$\boxed{(H^*, P^*) = (200, 30)}$$

**(c) Predator efficiency:**
$$\epsilon = \frac{\lambda}{\beta} = \frac{0.0005}{0.005} = 0.1 = \boxed{10\%}$$

**(d) Behavior from non-equilibrium:**

The populations will **oscillate periodically with constant amplitude**. The trajectory forms a closed orbit around the coexistence equilibrium $(200, 30)$. Prey peaks are followed by predator peaks (with a phase lag).

---

### Q18. True/False Analysis — Solution

- **(a) TRUE:** Verified above.
- **(b) TRUE:** $(200, 30) = (\gamma/\lambda, \alpha/\beta)$ is the coexistence equilibrium.
- **(c) TRUE:** $\epsilon = \lambda/\beta = 0.0005/0.005 = 10\%$
- **(d) FALSE:** ❌ The efficiency is $10\%$, NOT $0.05\%$.
- **(e) TRUE:** Basic L-V model has closed orbits.

$$\boxed{\text{Statement (d) is NOT true}}$$

---

### Q19. Carrying Capacity — Solution

**(a) Finding all equilibrium points:**

**From predator equation:** $P(\lambda H - \gamma) = 0$
- Either $P = 0$ or $H = \gamma/\lambda = 600$

**With $P = 0$:** $\alpha H(1 - H/K) = 0$ gives $H = 0$ or $H = K = 1500$

**With $H = 600$:**
$$0.2 \cdot 600 \cdot (1 - 600/1500) - 0.005 \cdot 600 \cdot P = 0$$
$$72 = 3P \Rightarrow P = 24$$

**Three equilibria:**
$$\boxed{(0, 0), \quad (1500, 0), \quad (600, 24)}$$

**(b)** Coexistence equilibrium predator population: $\boxed{P^* = 24}$

**(c) Comparison:**
- Without carrying capacity: $P^* = \alpha/\beta = 40$
- With carrying capacity: $P^* = 24$

**Effect:** Carrying capacity **reduces** the equilibrium predator population.

---

### Q20. Direction Field Analysis — Solution

**(a) Nullclines:**

**H-nullcline** (where $dH/dt = 0$):
$$H = 0 \text{ or } P = \frac{\alpha}{\beta} = 40$$

**P-nullcline** (where $dP/dt = 0$):
$$P = 0 \text{ or } H = \frac{\gamma}{\lambda} = 600$$

**(b) Prey increasing:** $\frac{dH}{dt} > 0$ when $P < 40$

**(c) Predator decreasing:** $\frac{dP}{dt} < 0$ when $H < 600$

**(d) Flow pattern:**
- **Region I** ($H > 600$, $P < 40$): ↗ Northeast
- **Region II** ($H > 600$, $P > 40$): ↖ Northwest
- **Region III** ($H < 600$, $P > 40$): ↙ Southwest
- **Region IV** ($H < 600$, $P < 40$): ↘ Southeast

The flow circulates **counterclockwise** around the equilibrium. A conserved quantity prevents trajectories from spiraling, creating **closed periodic orbits**.

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Prey equation | $\frac{dH}{dt} = \alpha H - \beta HP$ |
| Predator equation | $\frac{dP}{dt} = \lambda HP - \gamma P$ |
| Prey equilibrium | $H^* = \frac{\gamma}{\lambda}$ |
| Predator equilibrium | $P^* = \frac{\alpha}{\beta}$ |
| Predator efficiency | $\epsilon = \frac{\lambda}{\beta}$ |
| Phase plane slope | $\frac{dP}{dH} = \frac{dP/dt}{dH/dt}$ |

---

## Lab Connection

**Notebook:** `LoktaVolterraModel.ipynb`

| Lab Exercise | Practice Link |
|--------------|---------------|
| A. Predator decay without prey | W8-003 |
| B. Symbolic model setup | W8-001 |
| C. Slope calculation | W8-015 |
| D. Vector field refinement | W8-010, W8-011 |
| E. Equilibrium finding | W8-005, W8-006, W8-009 |
| F. Phase portrait with multiple trajectories | W8-012, W8-020 |
| G. Practice quiz completion | W8-017, W8-018 |

---

*Good luck on your exam!*
