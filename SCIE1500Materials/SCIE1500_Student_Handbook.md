# SCIE1500 Lab Handbook
## Analytical Methods for Scientists
**Semester 1, 2026**

---

---

# SCIE1500 Lab Handbook

## Analytical Methods for Scientists

### "From Problem to Presentation"

**Semester 1, 2026**

---

# Welcome to the SCIE1500 Labs

This handbook contains everything you need for your weekly lab sessions. Labs are where you apply the mathematical concepts from lectures to real scientific problems—and learn to communicate your findings to others.

**What makes these labs different:**
- You'll work in**groups of 5–7 students**
- You'll tackle**realistic scientific scenarios**, not just abstract exercises
- You'll**present your work**to your peers (twice during semester)
- You can use**AI tools**to help with coding—but you must understand and explain what the code does
- The focus is on**formulating problems**and**interpreting results**, not just getting the right number

> 

*"The analytical scientist doesn't just calculate—they formulate questions, choose appropriate methods, and communicate insights that inform decisions."*

---

# Table of Contents

- [Lab Structure and Expectations
- [Assessment Overview
- [Group Presentations
- [Problem Briefs: Weeks 1–12
- [Group Worksheets
- [Presentation Rubric
- [Tips for Success

---

# 1. Lab Structure and Expectations

## 1.1 Weekly Timeline (2 Hours)
********************

| Time | Activity | What You'll Do |
| --- | --- | --- |
| 0:00–0:15 | Briefing | Demonstrator introduces this week's problem |
| 0:15–0:35 | Presentations | 2 groups present last week's work (Weeks 3–9) |
| 0:35–0:45 | Q&A | Class discusses presentations; demonstrator feedback |
| 0:45–1:40 | Group Work | Your team tackles the current week's Problem Brief |
| 1:40–2:00 | Wrap-up | Share progress; preview next week |

## 1.2 What to Bring

- Laptop with Python environment (Jupyter/Colab)
- Access to the course app for AI tutoring
- This handbook (digital or printed)
- Calculator
- Notebook for scratch work

## 1.3 Group Formation

- Groups are assigned in**Week 1**and remain fixed for the semester
- Each lab section has**7 groups**of 5–7 students
- You'll work with the same group each week
- If a group member is absent, the remaining members continue

## 1.4 AI Tool Policy

**You may use AI tools (Claude, LLama/Hosted Service, etc.) to:**
- Debug code syntax errors
- Explain error messages
- Generate plotting code after you specify what to plot
- Check your solutions after attempting independently

**You must:**
- Document any AI use in your worksheet (Section 6)
- Be able to explain any code in your submission
- Do the mathematical formulation yourself first

**Red flags that suggest over-reliance:**
- You can't why your model is appropriate for the problem
- You can't explain what your code does line-by-line
- You pasted the entire problem into an AI without attempting it first
- Your approach doesn't match what was covered in lectures

---

# 2. Assessment Overview

## 2.1 Lab Component Breakdown (20% of Unit)
********************

| Component | Weight | Details |
| --- | --- | --- |
| Lab Engagement | 5% | Attendance + active participation |
| Group Presentations | 8% | 2 presentations × 4% each |
| Weekly Worksheets | 7% | Best 10 of 12 counted |
| Total | 20% |

## 2.2 Engagement Marks

Engagement is assessed by demonstrators based on:
- Attendance (you must be present in lab)
- Active participation in group work
- Contributing to lab discussions
- Helping teammates understand concepts

Simply being physically present while others do the work does not constitute engagement.

**Note:**For group presentations and worksheets, your individual mark is further adjusted by**peer review**(see Section 2.4).
## 2.3 Worksheet Submission

- Every week you are required to upload/submit a worksheet
- Upload the worksheet via LMS before the deadline (due dates Outline)

## 2.4 Peer Review and Individual Marking

### 2.4.1 How Individual Marks Are Calculated

While worksheets and presentations are completed as a**group**, your**individual mark**is adjusted based on your contribution as assessed by your peers.

**The Formula:**
```python
Individual Mark = Group Mark × (Your Contribution Score ÷ 100)

```

### 2.4.2 Peer Review Process

After each major group assessment (presentations and selected worksheets), each group member will:
- Rate**themselves**on their contribution (0–100%)
- Rate**each teammate**on their contribution (0–100%)

Your final contribution score is the**average of all peer ratings**you receive (including your self-rating).
### 2.4.3 Worked Example

**Scenario:**Your group receives**70%**for a presentation. Peer reviews show:
- Alice's contribution score:**100%**(full engagement)
- Carlos's contribution score:**90%**(mostly engaged)
- Bob's contribution score:**60%**(minimal participation)

**Individual Marks:**
- Alice: 70 × (100 ÷ 100) =**70%**
- Carlos: 70 × (90 ÷ 100) =**63%**
- Bob: 70 × (60 ÷ 100) =**42%**

### 2.4.4 What Counts as Good Contribution?

Peer reviews should consider:
- **Attendance**at group meetings
- **Quality of ideas**contributed
- **Task completion**(did they do their assigned work?)
- **Collaboration**(helping teammates, being responsive)
- **Communication**(clear, timely, constructive)

### 2.4.5 Consequences of Poor Participation

If your contribution score falls below**70%**:
- You may be required to meet with the lab instructor
- Repeated low scores may mean you meet with the unit coordinator, and
- In extreme cases, you may be removed from your group and required to complete alternative assessment

**Important:**Consistent non-participation is grounds for failing the unit, even if your group performs well.
### 2.4.6 Peer Review Guidelines

**When rating teammates:**
- Be honest and fair
- Provide specific examples if someone receives <80%
- Don't collude to give everyone 100%—demonstrators can identify this
- Focus on contribution, not personality or friendships

**If you have concerns:**
- Speak with your demonstrator early (don't wait until assessment)
- Document issues with timestamps and specifics
- Give teammates a chance to improve before harsh ratings

## 2.5 Presentation Schedule

Each group presents**exactly twice**during Weeks 3–9 on a presentation topic from the previous week.

| Week | Presenting Groups | Presentation Topic |
| --- | --- | --- |
| 3 | 1, 2 | Week 2: Exponential models |
| 4 | 3, 4 | Week 3: Logistic/Schaefer |
| 5 | 5, 6 | Week 4: Derivatives |
| 6 | 7, 1 | Week 5: Optimization |
| 7 | 2, 3 | Week 6: Integration |
| 8 | 4, 5 | Week 7: Definite integrals & surplus |
| 9 | 6, 7 | Week 8: Lotka-Volterra |

**Weeks 10–12**use alternative formats (Mock Exam, Peer Review, Gallery Walk) where all groups participate equally.

---

# 3. Group Presentations

## 3.1 Presentation Format

- **Duration:**10 minutes (strict)
- **Presenters:**Entire group (divide speaking roles)
- **Audience:**Your lab section (~35–45 students)
- **Topic:**The previous week's Problem Brief

## 3.2 Recommended Structure
****************

| Section | Time | Content |
| --- | --- | --- |
| The Problem | 2 min | What real-world question were you answering? Why does it matter? |
| The Approach | 3 min | What mathematical model/method did you use? Why was it appropriate? |
| Key Results | 3 min | What did you find? Show at least one visualization. |
| Implications | 2 min | What should decision-makers take away? |

## 3.3 Presentation Tips

**Do:**
- Practice timing—10 minutes is shorter than you think
- Show graphs and equations, not raw code
- Explain the "so what?"—why do these numbers matter?
- Use visual aids (graphs, diagrams, key equations on slides)
- Rehearse transitions between speakers
- Anticipate questions your audience might ask

**Don't:**
- Read directly from slides
- Show detailed Python code
- Go over time (you'll be cut off)
- Let one person do all the talking
- Assume the audience remembers all problem details

## 3.4 Common Mistakes to Avoid

| Mistake | Why It's Bad | Better Approach |
| --- | --- | --- |
| Showing code instead of results | Audience can't follow; wastes time | Show the graph/output, explain what it means |
| No clear "so what?" | Problem seems pointless | Always connect to real-world decision |
| Uneven participation | Some members don't demonstrate learning | Divide roles explicitly; everyone speaks |
| Mathematical errors unchecked | Loses credibility | Double-check calculations; verify with Python |

---

---

## Week 1: Functions and Their Properties

### PROBLEM BRIEF: W1

**"Global Plastic Production: Understanding Functional Relationships"**

---

#### SCENARIO

The United Nations Environment Programme (UNEP) is preparing a report on plastic waste in oceans. You are part of a team analyzing historical data on global plastic production.

**Data: Global plastic production (million tonnes)**

| Year | 1950 | 1970 | 1990 | 2010 | 2015 |
| --- | --- | --- | --- | --- | --- |
| Production | 2 | 35 | 120 | 270 | 380 |

The relationship between year and production can be modeled as a function $P(t)$P(t)where $t$tis years since 1950.

---

#### YOUR TASK
Part A: Function Identification (20 minutes)
- 

Plot the global plastic production data (Year vs Production). Which function family best describes the shape — linear, quadratic, or exponential? Justify your choice.
- 

Linear model from 1990–2015:
- Calculate the slope (rate of change in million tonnes/year).
- Write the linear function $P(t)$P(t)where $t$t= years since 1990.
- What does the slope*mean*in real-world terms?

- 

Quadratic model $P(t) = at^2 + bt + c$P(t)=at2+bt+cthrough the points (1990, 120), (2010, 270), (2015, 380):
- Set up the system of three equations (you do not need to solve it fully).
- What would a positive coefficient $a$aindicate about the rate of growth?

Part B: Domain & Range Analysis (15 minutes)
- 

For your linear model from Q2:
- State the mathematical domain.
- State a sensible physical domain — and explain why they differ.
- State the range over your physical domain.

- 

The Reisser depth model estimates plastic concentration using:$C_i = \frac{C_s}{1 - e^{-d \cdot w_b \cdot A_0^{-1}}}$Ci​=1−e−d⋅wb​⋅A0−1​Cs​​

where $C_s > 0$Cs​>0, $d > 0$d>0, $w_b > 0$wb​>0, $A_0 > 0$A0​>0.
- As $d \to 0$d→0(very shallow sampling), what happens to $C_i$Ci​?
- As $d \to \infty$d→∞(very deep sampling), what does $C_i$Ci​approach?

Part C: Australian Policy Application (20 minutes)
- 

Calculate Australia's mismanaged plastic waste (coastal population 19.6 million, waste rate 0.028 kg/person/day, mismanagement rate 2%):
- Daily waste entering waterways (tonnes/day).
- Annual waste (tonnes/year). Show your unit conversion clearly.

- 

Write a function $W(t)$W(t)for annual mismanaged waste (tonnes/year), where $t$t= years from 2010, assuming the coastal population grows at 1.5% per year and all other rates remain constant.
- 

The government proposes cutting the mismanagement rate from 2% to 0.5% by 2030. Would this fully offset the population growth effect? Support your answer with calculations and a clear written conclusion.

#### DELIVERABLES

- Completed Special Worksheet (Type B — Week 1 format, provided by instructor)
- Python plots as appendix (if created)

#### HINTS / SCAFFOLDING

**For Q1 — choosing a function family:**Plot first; then check the decade-by-decade rates computed in Q2 across earlier weeks. Accelerating rates rule out linear; roughly constant*ratio*per period suggests exponential.

**For Q2 — linear slope from 1990–2015:**$\text{Slope} = \frac{\Delta P}{\Delta t} = \frac{380 - 120}{2015 - 1990} = \frac{260}{25} = 10.4 \ \text{MT/year}$Slope=ΔtΔP​=2015−1990380−120​=25260​=10.4MT/year

**For Q3 — quadratic system:**Set $t = 0$t=0at 1990; the three points become $(0,\ 120)$(0,120), $(20,\ 270)$(20,270), $(25,\ 380)$(25,380), giving $c = 120$c=120immediately.

**For Q5 — Reisser model limits:**
- As $d \to 0$d→0: exponent $\to 0$→0, denominator $\to 0$→0, so $C_i \to \infty$Ci​→∞.
- As $d \to \infty$d→∞: exponent $\to -\infty$→−∞, so $e^{\ldots} \to 0$e…→0and $C_i \to C_s$Ci​→Cs​.

**Python starter for Q1:**
```python
[import matplotlib.pyplot as plt
[years = [1950, 1970, 1990, 2010, 2015]
[production = [2, 35, 120, 270, 380]
[plt.scatter(years, production)
[plt.xlabel('Year')
[plt.ylabel('Production (million tonnes)')
[plt.title('Global Plastic Production')
[plt.show()

```

---

---

---

# Week 2: Exponential and Logarithmic Functions

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W2

**"Doubling Times: From Plastic to Pandemics"**

---

#### SCENARIO

Your team has been asked to prepare educational materials comparing exponential growth across different domains. The goal is to help policymakers understand why "percentage growth rates" can be deceptive and why early intervention matters.

**Context 1: Plastic Production**

Global plastic production has grown at approximately 8.4% per year since 1950. In 1950, production was 2 million tonnes.

**Context 2: Bacterial Growth**

A laboratory culture of*E. coli*doubles every 20 minutes under optimal conditions. A sample starts with 1,000 cells.

**Context 3: Radioactive Decay**

Carbon-14 has a half-life of 5,730 years. A fossil sample initially contained 100 units of C-14.

---

#### YOUR TASK

**Part A: Modeling Growth and Decay (25 minutes)**
- 

**Plastic production:**Write an exponential model $P(t) = P_0 e^{kt}$P(t)=P0​ektwhere $t$tis years since 1950.
- Given: 8.4% annual growth rate
- Find the value of $k$k(hint: $e^k = 1.084$ek=1.084)
- Predict production in 2025

- 

**Bacterial growth:**Write a model $N(t) = N_0 \cdot 2^{t/T}$N(t)=N0​⋅2t/Twhere $T$Tis the doubling time in minutes.
- How many bacteria after 2 hours?
- Convert to the form $N(t) = N_0 e^{kt}$N(t)=N0​ektand find $k$k

- 

**Radioactive decay:**Write a model $A(t) = A_0 e^{-\lambda t}$A(t)=A0​e−λtwhere $t$tis years.
- Find $\lambda$λusing the half-life
- What fraction remains after 11,460 years (two half-lives)?

**Part B: Doubling Time Analysis (15 minutes)**
- 

The**Rule of 70**states: Doubling time ≈ 70 / (percentage growth rate)
- Verify this rule for plastic production (8.4% growth)
- Derive the exact formula: $T_{double} = \frac{\ln 2}{k}$Tdouble​=kln2​
- How accurate is the Rule of 70?

- 

If plastic production continues at 8.4% annual growth:
- When will production reach 1 billion tonnes?
- When will it reach 10 billion tonnes?
- What does this suggest about the feasibility of "business as usual"?

**Part C: Logarithmic Solving (15 minutes)**
- 

A population of invasive carp in a lake follows $P(t) = 50 e^{0.15t}$P(t)=50e0.15t, where $t$tis months.
- How long until the population reaches 500?
- How long until it reaches 5,000?
- If eradication becomes impossible above 1,000 fish, how much time does the management authority have?

- 

Carbon dating: A fossil has 25% of its original C-14 remaining. How old is it?

---

#### DELIVERABLES

- Completed Group Worksheet
- **Groups 1 & 2:**Prepare 10-minute presentation for Week 3

---

#### PRESENTATION GUIDANCE (Groups 1 & 2)

Your presentation should address:
- **The Problem**(2 min): What real-world question were you answering?
- **The Approach**(3 min): What mathematical model did you use and why?
- **Key Results**(3 min): What did you find? Show at least one visualization.
- **Implications**(2 min): What should decision-makers take away?

**Presentation tips:**
- Don't show raw code—show graphs and equations
- Speak to the "so what?" — why do these numbers matter?
- Practice timing; 10 minutes is shorter than you think

---

#### HINTS / SCAFFOLDING

**Converting between forms:**
- $P(t) = P_0 \cdot b^t$P(t)=P0​⋅btand $P(t) = P_0 e^{kt}$P(t)=P0​ektare equivalent when $k = \ln(b)$k=ln(b)
- Example: $2^t = e^{t \ln 2}$2t=etln2

**Logarithm rules for solving:**
- If $e^{kt} = C$ekt=C, then $kt = \ln(C)$kt=ln(C), so $t = \frac{\ln(C)}{k}$t=kln(C)​

**Python for visualization:**
```python
t = np.linspace(0, 100, 200)
P = 2 * np.exp(0.0807 * t)  # k = ln(1.084) ≈ 0.0807

plt.semilogy(t + 1950, P)  # Log scale on y-axis
plt.xlabel('Year')
plt.ylabel('Production (million tonnes, log scale)')
plt.title('Projected Plastic Production')
plt.show()

```

---

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W2A (for Group 1 presentation in Week 3)

**"Bacterial Growth: The Hospital Infection Challenge"**

---

### SCENARIO

You are a consultant for Royal Perth Hospital's infection control team. A strain of antibiotic-resistant*Staphylococcus aureus*(MRSA) has been detected on a surgical instrument.

Laboratory tests show that under ideal conditions, this bacterial strain doubles every**25 minutes**. The initial contamination is estimated at**800 bacterial cells**.

**Hospital policy:**If bacterial count exceeds**1 million cells**, the entire surgical suite must be shut down for deep sterilization (cost: $50,000 and 48-hour delay).

---

### YOUR TASK

**Part A: Modeling Bacterial Growth (20 minutes)**
- 

Write an exponential model $N(t) = N_0 \cdot 2^{t/T}$N(t)=N0​⋅2t/Twhere $T$Tis the doubling time.
- $N_0 = 800$N0​=800cells
- $T = 25$T=25minutes
- Calculate the population after 2 hours

- 

Convert your model to the form $N(t) = N_0 e^{kt}$N(t)=N0​ekt
- Find the growth rate constant $k$k(hint: $e^k = 2^{1/25}$ek=21/25)
- Verify both models give the same answer for $t = 120$t=120minutes

- 

**Critical question:**How much time does the hospital have before the bacterial count reaches 1 million?
- Solve $800 \cdot 2^{t/25} = 1,000,000$800⋅2t/25=1,000,000
- Express your answer in hours and minutes

**Part B: Temperature Effects (15 minutes)**
- Refrigeration slows bacterial growth. At 4°C, the doubling time increases to**180 minutes**.
- What is the new growth rate constant $k_{cold}$kcold​?
- How long would it take to reach 1 million cells at 4°C?
- What does this tell you about the importance of refrigeration?

**Part C: Sterilization Decision (10 minutes)**
- 

The hospital has two options:
- **Option 1:**Immediate sterilization (cost: $50,000, 48-hour delay)
- **Option 2:**Refrigerate and monitor for 12 hours, then re-test

Using your calculations, write a 3-4 sentence recommendation to the hospital administrator.

**Part D: Rule of 70 Verification (10 minutes)**
- The "Rule of 70" states that doubling time ≈ 70/(percentage growth rate)
- For a 25-minute doubling time, what percentage growth rate per minute does this imply?
- Calculate the exact growth rate: $r = (e^k - 1) \times 100\%$r=(ek−1)×100%where $k = \ln(2)/25$k=ln(2)/25
- How close is the Rule of 70?

---

### DELIVERABLES

- Completed Group Worksheet with all calculations
- Python plot showing $N(t)$N(t)vs time with critical threshold marked
- **Group 1 ONLY:**Prepare 10-minute presentation for Week 3

---

### PYTHON HINTS

```python
import numpy as np
import matplotlib.pyplot as plt

# Time array (0 to 300 minutes)
t = np.linspace(0, 300, 500)

# Model parameters
N0 = 800
T_double = 25
k = np.log(2) / T_double

# Population function
N = N0 * np.exp(k * t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, N, linewidth=2, label='Bacterial Growth')
plt.axhline(y=1e6, color='r', linestyle='--', label='Critical Threshold')
plt.xlabel('Time (minutes)')
plt.ylabel('Bacterial Count')
plt.yscale('log')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('MRSA Growth in Hospital Environment')
plt.show()

```

---

## PROBLEM BRIEF: W2B (for Group 2 presentation in Week 3)

**"Radioactive Waste: The Fukushima Legacy"**

---

### SCENARIO

You are advising the Japanese government on long-term storage of radioactive waste from the Fukushima disaster. One isotope of concern is**Caesium-137**, which has a half-life of**30.17 years**.

A storage container holds waste with an initial activity of**500 TBq**(terabecquerels).

**Regulatory standard:**The container can be declassified as "low-level waste" when activity drops below**10 TBq**, allowing for cheaper storage options.

---

### YOUR TASK

**Part A: Modeling Radioactive Decay (20 minutes)**
- 

Write an exponential decay model $A(t) = A_0 \cdot (0.5)^{t/T_{1/2}}$A(t)=A0​⋅(0.5)t/T1/2​where $T_{1/2}$T1/2​is the half-life.
- $A_0 = 500$A0​=500TBq
- $T_{1/2} = 30.17$T1/2​=30.17years
- Calculate the activity after 50 years

- 

Convert your model to the form $A(t) = A_0 e^{-\lambda t}$A(t)=A0​e−λt
- Find the decay constant $\lambda$λ(hint: $e^{-\lambda} = 0.5^{1/30.17}$e−λ=0.51/30.17)
- Verify both models give the same answer for $t = 50$t=50years

- 

**Critical question:**How long until the waste can be reclassified as low-level (≤10 TBq)?
- Solve $500 \cdot (0.5)^{t/30.17} = 10$500⋅(0.5)t/30.17=10
- Express your answer in years

**Part B: Multiple Isotopes (15 minutes)**
- The waste also contains**Strontium-90**with half-life**28.8 years**and initial activity**200 TBq**.
- Which isotope decays faster? How can you tell from the half-lives?
- After how many years will both isotopes have the same activity?
- Solve: $500(0.5)^{t/30.17} = 200(0.5)^{t/28.8}$500(0.5)t/30.17=200(0.5)t/28.8

**Part C: Storage Cost Analysis (10 minutes)**
- High-level storage costs ¥50 million per year. Low-level storage costs ¥5 million per year.
- Calculate total storage cost over 150 years
- How much money is saved by waiting until reclassification?
- Write a 3-4 sentence cost-benefit summary for policymakers

**Part D: Carbon Dating Connection (10 minutes)**
- **Carbon-14**has a half-life of 5,730 years and is used for dating ancient artifacts.
- A fossil has 12.5% of its original C-14 remaining. How old is it?
- Hint: 12.5% = (0.5)³, so it has gone through 3 half-lives
- Verify using logarithms: solve $0.125 = (0.5)^{t/5730}$0.125=(0.5)t/5730

---

### DELIVERABLES

- Completed Group Worksheet with all calculations
- Python plot showing decay curves for both Cs-137 and Sr-90
- **Group 2 ONLY:**Prepare 10-minute presentation for Week 3

---

### PYTHON HINTS

```python
import numpy as np
import matplotlib.pyplot as plt

# Time array (0 to 200 years)
t = np.linspace(0, 200, 500)

# Cs-137 parameters
A0_cs = 500
T_half_cs = 30.17
lambda_cs = np.log(2) / T_half_cs
A_cs = A0_cs * np.exp(-lambda_cs * t)

# Sr-90 parameters
A0_sr = 200
T_half_sr = 28.8
lambda_sr = np.log(2) / T_half_sr
A_sr = A0_sr * np.exp(-lambda_sr * t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, A_cs, linewidth=2, label='Caesium-137')
plt.plot(t, A_sr, linewidth=2, label='Strontium-90')
plt.axhline(y=10, color='g', linestyle='--', label='Low-level threshold')
plt.xlabel('Time (years)')
plt.ylabel('Activity (TBq)')
plt.yscale('log')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Radioactive Decay: Fukushima Waste')
plt.show()

```

---

---

# Week 3: Logistic Functions and Bounded Growth

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W3

**"The Fishery Manager's Dilemma"**

---

#### SCENARIO

You are a scientific advisor to the Western Australian Fisheries Authority. The authority manages a sardine fishery that has shown signs of overfishing in recent years.

Marine biologists have developed a**Schaefer model**for the sardine population:$G(S) = g \cdot S \cdot \left(1 - \frac{S}{K}\right) $G(S)=g⋅S⋅(1−KS​)

where:
- $G(S)$G(S)= annual population growth (tonnes/year)
- $S$S= current stock level (tonnes)
- $g = 0.4$g=0.4= intrinsic growth rate (per year)
- $K = 1500$K=1500= carrying capacity (tonnes)

**Current situation:**
- Stock level: $S = 1200$S=1200tonnes
- Industry harvest: $H = 120$H=120tonnes/year

The Fisheries Authority wants to know:**Is this harvest sustainable?**

---

#### YOUR TASK

**Part A: Understanding the Schaefer Model (20 minutes)**
- 

Calculate the growth rate $G(S)$G(S)at three stock levels:
- $S = 400$S=400tonnes (heavily depleted)
- $S = 750$S=750tonnes (half of carrying capacity)
- $S = 1200$S=1200tonnes (current level)

- 

Show that growth is maximized when $S = K/2 = 750$S=K/2=750tonnes:
- Expand the Schaefer equation: $G(S) = gS - \frac{g}{K}S^2$G(S)=gS−Kg​S2
- This is a quadratic with vertex at $S = \frac{K}{2}$S=2K​
- Calculate the**Maximum Sustainable Yield (MSY)**

- 

Plot $G(S)$G(S)vs. $S$Sfor $S$Sranging from 0 to 1500 tonnes.

**Part B: Sustainability Analysis (20 minutes)**
- 

A harvest is**sustainable**if the population can grow enough to replace what's removed:$G(S) \geq H $G(S)≥H

At the current stock level ($S = 1200$S=1200tonnes):
- Calculate $G(1200)$G(1200)
- Is the current harvest of 120 tonnes/year sustainable?

- 

Find the**equilibrium stock levels**where $G(S) = H$G(S)=H:
- Set up: $0.4S(1 - S/1500) = 120$0.4S(1−S/1500)=120
- Expand: $0.4S - 0.0002667S^2 = 120$0.4S−0.0002667S2=120
- Rearrange to standard form: $0.0002667S^2 - 0.4S + 120 = 0$0.0002667S2−0.4S+120=0
- Solve using the quadratic formula
- There should be two solutions—what do they represent?

- 

The**lower equilibrium**is unstable (if stock drops below it, population collapses). The**upper equilibrium**is stable (population returns to it if perturbed).
- Which equilibrium is safer for the fishery?
- Is the current stock ($S = 1200$S=1200) above or below the safe equilibrium?

**Part C: Policy Recommendation (15 minutes)**
- 

The fishing industry wants to increase harvest to 140 tonnes/year due to high demand.
- Find the new equilibrium stock levels for $H = 140$H=140
- What is the minimum stock level needed to sustain this harvest?
- Compare to the $H = 120$H=120scenario—is the risk acceptable?

- 

Write a**brief recommendation**(4–5 sentences) to the Fisheries Authority:
- Is the current 120 tonne/year harvest sustainable?
- Should the 140 tonne/year increase be approved?
- What harvest level would you recommend for long-term sustainability?

---

#### DELIVERABLES

- Completed Group Worksheet
- Python plot showing $G(S)$G(S)curve with harvest levels marked
- **Groups 3 & 4:**Prepare 10-minute presentation for Week 4

---

#### PRESENTATION GUIDANCE (Groups 3 & 4)

Focus on:
- How the Schaefer model captures bounded growth
- The concept of Maximum Sustainable Yield
- Why there are two equilibrium points and what they mean
- Your policy recommendation and reasoning

---

#### HINTS / SCAFFOLDING

**Quadratic formula:**$S = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $S=2a−b±b2−4ac​​

For the equation $0.0002667S^2 - 0.4S + 120 = 0$0.0002667S2−0.4S+120=0:
- $a = 0.0002667$a=0.0002667
- $b = -0.4$b=−0.4
- $c = 120$c=120

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

S = np.linspace(0, 1500, 500)
G = 0.4 * S * (1 - S/1500)

plt.figure(figsize=(10, 6))
plt.plot(S, G, linewidth=2, label='Growth G(S)')
plt.axhline(y=120, color='r', linestyle='--', label='Harvest = 120 tonnes/year')
plt.axhline(y=140, color='orange', linestyle='--', label='Proposed = 140 tonnes/year')
plt.xlabel('Stock Level (tonnes)')
plt.ylabel('Growth Rate (tonnes/year)')
plt.title('Sardine Fishery: Schaefer Model')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W3A (for Group 3 presentation in Week 4)

**"Abalone Fishery: Sustainable Harvest in Western Australia"**

---

### SCENARIO

The WA Department of Fisheries manages a commercial abalone (*Haliotis roei*) fishery along the south coast. Population surveys and growth studies have led to the following Schaefer model:$G(S) = 0.35 \cdot S \cdot \left(1 - \frac{S}{1200}\right) $G(S)=0.35⋅S⋅(1−1200S​)

where:
- $G(S)$G(S)= annual population growth (tonnes/year)
- $S$S= current stock level (tonnes)
- Intrinsic growth rate $g = 0.35$g=0.35
- Carrying capacity $K = 1200$K=1200tonnes

**Current situation:**Stock level is $S = 950$S=950tonnes. Industry wants to harvest**100 tonnes/year**.

---

### YOUR TASK

**Part A: Understanding the Schaefer Model (15 minutes)**
- 

Calculate growth $G(S)$G(S)at three stock levels:
- $S = 300$S=300tonnes (low stock)
- $S = 600$S=600tonnes (mid stock)
- $S = 900$S=900tonnes (high stock)
- Which stock level has the highest growth rate?

- 

Show that growth is maximized at $S = K/2 = 600$S=K/2=600tonnes
- Expand $G(S) = 0.35S(1 - S/1200)$G(S)=0.35S(1−S/1200)to standard form
- Find the vertex of this parabola
- What is the maximum sustainable yield (MSY)?

**Part B: Sustainability Analysis (20 minutes)**
- 

A harvest is**sustainable**if $G(S) \geq H$G(S)≥H(growth ≥ harvest).
- At current stock $S = 950$S=950tonnes, what is $G(950)$G(950)?
- Is the proposed harvest of 100 tonnes/year sustainable?

- 

Find the**two equilibrium points**where $G(S) = 100$G(S)=100:
- Solve: $0.35S(1 - S/1200) = 100$0.35S(1−S/1200)=100
- Hint: This is a quadratic equation. Use the quadratic formula.
- Interpret: what do these two equilibrium points represent?

- 

The lower equilibrium is**unstable**(population collapses if stock drops below it). The upper equilibrium is**stable**(population recovers to it).
- Which equilibrium is safer for long-term sustainability?

**Part C: Policy Recommendation (15 minutes)**
- 

The industry proposes increasing harvest to**120 tonnes/year**due to high market prices.
- Find the new equilibrium points for $H = 120$H=120
- What is the minimum safe stock level?
- Compare to the $H = 100$H=100scenario

- 

Write a 4-5 sentence recommendation to the Fisheries Minister addressing:
- Whether the 120 tonne harvest is sustainable
- The risk to the fishery
- An alternative harvest level you would recommend

**Part D: Python Visualization (10 minutes)**
- Create a graph showing:
- The growth curve $G(S)$G(S)vs stock $S$S
- Horizontal lines at $H = 100$H=100and $H = 120$H=120
- Mark the equilibrium points
- Shade the "safe zone" for stock levels

---

### DELIVERABLES

- Completed Group Worksheet
- Python plot of growth function with harvest levels
- **Group 3 ONLY:**Prepare 10-minute presentation for Week 4

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

S = np.linspace(0, 1200, 500)
G = 0.35 * S * (1 - S/1200)

plt.figure(figsize=(10, 6))
plt.plot(S, G, linewidth=2, label='Growth G(S)', color='blue')
plt.axhline(y=100, color='orange', linestyle='--', label='H = 100 tonnes/year')
plt.axhline(y=120, color='red', linestyle='--', label='H = 120 tonnes/year')
plt.xlabel('Stock Level S (tonnes)')
plt.ylabel('Growth Rate G(S) (tonnes/year)')
plt.title('Abalone Fishery: Schaefer Growth Model')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 1200)
plt.ylim(0, 120)

# Mark MSY point
S_msy = 600
G_msy = 0.35 * S_msy * (1 - S_msy/1200)
plt.plot(S_msy, G_msy, 'go', markersize=10, label=f'MSY = {G_msy:.1f} tonnes/year')

plt.legend()
plt.show()

```

---

## PROBLEM BRIEF: W3B (for Group 4 presentation in Week 4)

**"Rock Lobster Recovery: From Overfishing to Sustainability"**

---

### SCENARIO

Western Australia's rock lobster (*Panulirus cygnus*) fishery was severely overfished in the 1990s. After implementing catch limits, the fishery is recovering. Marine biologists have developed this Schaefer model:$G(S) = 0.42 \cdot S \cdot \left(1 - \frac{S}{800}\right) $G(S)=0.42⋅S⋅(1−800S​)

where:
- $G(S)$G(S)= annual population growth (tonnes/year)
- $S$S= current stock level (tonnes)
- Intrinsic growth rate $g = 0.42$g=0.42(higher than abalone due to faster maturation)
- Carrying capacity $K = 800$K=800tonnes

**Current situation:**After recovery efforts, stock is now $S = 350$S=350tonnes. The fishing industry wants permission to harvest**70 tonnes/year**.

---

### YOUR TASK

**Part A: Schaefer Model Analysis (15 minutes)**
- 

Calculate growth $G(S)$G(S)at three stock levels:
- $S = 200$S=200tonnes (recovering from collapse)
- $S = 400$S=400tonnes (near optimal)
- $S = 700$S=700tonnes (near carrying capacity)
- At which stock does growth peak?

- 

Prove that maximum growth occurs at $S^* = K/2 = 400$S∗=K/2=400tonnes
- Write $G(S) = 0.42S - 0.000525S^2$G(S)=0.42S−0.000525S2in standard form
- Complete the square or use vertex formula
- Calculate the maximum sustainable yield (MSY)

**Part B: Harvest Sustainability (20 minutes)**
- 

At the current stock level $S = 350$S=350tonnes:
- Calculate the natural growth rate $G(350)$G(350)
- Is the proposed 70 tonnes/year harvest sustainable?
- What fraction of growth would be harvested?

- 

Find all stock levels where harvest equals growth: $G(S) = 70$G(S)=70
- Set up: $0.42S(1 - S/800) = 70$0.42S(1−S/800)=70
- Multiply out: $0.42S - 0.000525S^2 = 70$0.42S−0.000525S2=70
- Rearrange: $0.000525S^2 - 0.42S + 70 = 0$0.000525S2−0.42S+70=0
- Solve using quadratic formula
- Interpret: why are there two solutions?

- 

**Stability analysis:**
- The lower equilibrium represents a "danger zone"
- The upper equilibrium is the target sustainable level
- Which equilibrium is closer to current stock?

**Part C: Climate Change Impact (15 minutes)**
- 

Ocean warming is expected to reduce carrying capacity to $K = 720$K=720tonnes by 2040.
- What is the new MSY under warming scenario?
- New model: $G(S) = 0.42S(1 - S/720)$G(S)=0.42S(1−S/720)
- Can the fishery still sustain 70 tonnes/year harvest?

- 

Write a brief (4-5 sentence) climate adaptation strategy for the fishery addressing:
- Short-term harvest levels while stock rebuilds
- Long-term harvest levels accounting for warming
- Monitoring requirements

**Part D: Comparative Analysis (10 minutes)**
- Compare rock lobster to abalone (from Problem W3A):
- Which has faster intrinsic growth ($g$g)?
- Which has higher carrying capacity ($K$K)?
- Which can sustain a higher harvest rate relative to stock?
- What biological factors might explain these differences?

---

### DELIVERABLES

- Completed Group Worksheet
- Python plot comparing current vs. warming scenarios
- **Group 4 ONLY:**Prepare 10-minute presentation for Week 4

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

# Stock range
S = np.linspace(0, 800, 500)

# Current climate scenario
G_current = 0.42 * S * (1 - S/800)

# Warming scenario (K = 720)
G_warming = 0.42 * S * (1 - S/720)

plt.figure(figsize=(10, 6))
plt.plot(S, G_current, linewidth=2, label='Current (K=800)', color='blue')
plt.plot(S, G_warming, linewidth=2, label='Warming (K=720)', color='red', linestyle='--')
plt.axhline(y=70, color='green', linestyle=':', label='Proposed harvest = 70 t/year')

plt.xlabel('Stock Level S (tonnes)')
plt.ylabel('Growth Rate G(S) (tonnes/year)')
plt.title('Rock Lobster: Climate Change Impact on Sustainability')
plt.legend()
plt.grid(True, alpha=0.3)

# Mark current stock
plt.axvline(x=350, color='gray', linestyle='--', alpha=0.5, label='Current stock')

plt.legend()
plt.show()

```

---

---

# Week 4: Derivatives and Rates of Change

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W4

**"Optimizing Chemical Reactions in Pharmaceutical Manufacturing"**

---

#### SCENARIO

A pharmaceutical company is optimizing the production of a critical antibiotic. The yield of the drug depends on reaction temperature. Chemical engineers have developed an empirical model:$Y(T) = -0.05T^2 + 8T - 200 $Y(T)=−0.05T2+8T−200

where:
- $Y(T)$Y(T)= yield (grams of product per batch)
- $T$T= reaction temperature (°C)
- Valid range: $50°C \leq T \leq 110°C$50°C≤T≤110°C

The company wants to maximize yield while staying within safe operating temperatures.

---

#### YOUR TASK

**Part A: Understanding Rates of Change (20 minutes)**
- 

Calculate the yield at three temperatures:
- $T = 60°C$T=60°C
- $T = 80°C$T=80°C
- $T = 100°C$T=100°C

Which temperature gives the highest yield?
- 

Find the**derivative**$Y'(T) = \frac{dY}{dT}$Y′(T)=dTdY​:
- Use the power rule: $(x^n)' = nx^{n-1}$(xn)′=nxn−1
- Interpret: What does $Y'(T)$Y′(T)represent? Include units!

- 

Calculate $Y'(70)$Y′(70)and $Y'(90)$Y′(90):
- What does the sign tell you about whether yield is increasing or decreasing?
- Express each as a rate per degree Celsius

**Part B: Finding the Optimal Temperature (20 minutes)**
- 

Find the**critical point**by solving $Y'(T) = 0$Y′(T)=0:
- Set your derivative equal to zero
- Solve for $T$T
- This is the candidate for maximum yield

- 

Verify this is a maximum using the**second derivative test**:
- Calculate $Y''(T)$Y′′(T)
- Evaluate $Y''(T_{critical})$Y′′(Tcritical​)
- If $Y''<0$Y′′<0: maximum ✓
- If $Y'' > 0$Y′′>0: minimum ✗

- 

Is the optimal temperature within the safe range $[50, 110]°C$[50,110]°C?
- If YES: use it
- If NO: check the boundary values

**Part C: Practical Constraints (15 minutes)**
- 

The reaction vessel can only maintain temperature within ±3°C of the setpoint.
- If the optimal temperature is $T_{opt}$Topt​, the actual temperature varies in $[T_{opt} - 3, T_{opt} + 3]$[Topt​−3,Topt​+3]
- Calculate the yield at both extremes
- What's the range of possible yields?

- 

A competing process uses $T = 70°C$T=70°Cand claims "good enough" yields.
- How much yield is lost compared to the optimum?
- Express as a percentage

**Part D: Cost-Benefit Analysis (5 minutes)**
- Higher temperatures require more energy. Energy cost is $\$0.50$$0.50per degree above 50°C per batch.
- Calculate the energy cost at the optimal temperature
- If the drug sells for $\$5$$5per gram, calculate net profit per batch at optimal temperature
- Compare to net profit at $T = 70°C$T=70°C

---

#### DELIVERABLES

- Completed Group Worksheet showing derivative calculations
- Graph of $Y(T)$Y(T)with the critical point marked
- **Groups 5 & 6:**Prepare 10-minute presentation for Week 5

---

#### PRESENTATION GUIDANCE (Groups 5 & 6)

Focus on:
- The concept of derivative as rate of change
- How optimization works (critical points, second derivative test)
- The difference between mathematical optimum and practical optimum (constraints)
- Your recommendation for the pharmaceutical company

---

#### HINTS / SCAFFOLDING

**Power rule:**
- $(x^n)' = nx^{n-1}$(xn)′=nxn−1
- $(c \cdot f(x))' = c \cdot f'(x)$(c⋅f(x))′=c⋅f′(x)where $c$cis a constant
- $(f(x) + g(x))' = f'(x) + g'(x)$(f(x)+g(x))′=f′(x)+g′(x)

**For $Y(T) = -0.05T^2 + 8T - 200$Y(T)=−0.05T2+8T−200:**
- $Y'(T) = -0.1T + 8$Y′(T)=−0.1T+8
- $Y''(T) = -0.1$Y′′(T)=−0.1

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(50, 110, 500)
Y = -0.05 * T**2 + 8 * T - 200

# Derivative
dY_dT = -0.1 * T + 8

# Critical point
T_crit = 80  # From Y'(T) = 0
Y_crit = -0.05 * T_crit**2 + 8 * T_crit - 200

plt.figure(figsize=(10, 6))
plt.plot(T, Y, linewidth=2, label='Yield Y(T)')
plt.plot(T_crit, Y_crit, 'ro', markersize=10, label=f'Optimum: T={T_crit}°C, Y={Y_crit:.1f}g')
plt.axvline(x=50, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=110, color='gray', linestyle='--', alpha=0.5)
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield (grams/batch)')
plt.title('Drug Yield vs Reaction Temperature')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W4A (for Group 5 presentation in Week 5)

**"Pesticide Degradation: Optimizing Spray Timing"**

---

### SCENARIO

You are consulting for a wheat farm in the Wheatbelt. The farm uses a systemic pesticide that degrades over time after application. The concentration of active ingredient follows:$C(t) = 120 e^{-0.15t} $C(t)=120e−0.15t

where:
- $C(t)$C(t)= concentration (mg/L) in plant tissue
- $t$t= days after application
- Initial concentration: $C(0) = 120$C(0)=120mg/L

**Agronomic constraints:**
- Minimum effective concentration:**30 mg/L**(below this, pest control fails)
- Maximum safe concentration:**150 mg/L**(above this, phytotoxicity occurs)
- Target pests (aphids) are most vulnerable 5-10 days after wheat head emergence

---

### YOUR TASK

**Part A: Understanding the Rate of Change (20 minutes)**
- 

Calculate concentration at $t = 0, 5, 10, 15, 20$t=0,5,10,15,20days
- Create a table of values
- How quickly is concentration dropping in the first week vs. third week?

- 

Find the**instantaneous rate of change**$C'(t)$C′(t)using the derivative:
- Use rule: $(e^{kt})' = k \cdot e^{kt}$(ekt)′=k⋅ekt
- Simplify: $C'(t) = \frac{dC}{dt}$C′(t)=dtdC​
- Evaluate $C'(5)$C′(5)and interpret (include units!)

- 

At what rate is the pesticide concentration decreasing on day 10?
- Calculate $C'(10)$C′(10)
- Express as a percentage of $C(10)$C(10): $\frac{C'(10)}{C(10)} \times 100\%$C(10)C′(10)​×100%

**Part B: Effective Protection Window (20 minutes)**
- 

Determine when concentration first drops below the effective threshold:
- Solve: $120e^{-0.15t} = 30$120e−0.15t=30
- Take natural log of both sides
- $t_{end} = ?$tend​=?days

- 

How long is the "protection window" (concentration ≥ 30 mg/L)?
- Protection duration = $t_{end} - 0$tend​−0
- Express in days and hours

- 

If the farm wants to extend protection to 20 days, what initial concentration is needed?
- Solve: $C_0 e^{-0.15 \times 20} = 30$C0​e−0.15×20=30
- Would this exceed the phytotoxicity limit of 150 mg/L?

**Part C: Re-Application Strategy (15 minutes)**
- 

The farmer wants continuous protection over a 30-day period (grain filling stage).
- Strategy: re-apply when concentration drops to 40 mg/L
- How many days between applications?
- How many total applications needed for 30-day coverage?

- 

Calculate total pesticide used over 30 days:
- Each application: 120 mg/L × 500L/ha = 60,000 mg/ha = 60 g/ha
- Number of applications × 60 g/ha = total usage

**Part D: Half-Life Concept (10 minutes)**
- 

The**half-life**is the time for concentration to halve.
- Starting from 120 mg/L, when does it reach 60 mg/L?
- Solve: $120e^{-0.15t} = 60$120e−0.15t=60
- Verify using the formula: $t_{1/2} = \frac{\ln(2)}{k}$t1/2​=kln(2)​where $k = 0.15$k=0.15

- 

After two half-lives, what fraction of the original concentration remains?
- Calculate using the half-life
- Verify using the exponential formula

---

### DELIVERABLES

- Completed Group Worksheet with derivative calculations
- Graph showing $C(t)$C(t)with protection window shaded
- **Group 5 ONLY:**Prepare 10-minute presentation for Week 5

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 30, 500)
C = 120 * np.exp(-0.15 * t)

# Derivative
dC_dt = -0.15 * 120 * np.exp(-0.15 * t)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top: Concentration
ax1.plot(t, C, linewidth=2, label='Concentration C(t)')
ax1.axhline(y=30, color='r', linestyle='--', label='Minimum effective (30 mg/L)')
ax1.axhline(y=150, color='orange', linestyle='--', label='Phytotoxicity limit (150 mg/L)')
ax1.fill_between(t, 30, 150, alpha=0.2, color='green', label='Safe + effective zone')
ax1.set_xlabel('Days after application')
ax1.set_ylabel('Concentration (mg/L)')
ax1.set_title('Pesticide Degradation')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Bottom: Rate of change
ax2.plot(t, dC_dt, linewidth=2, color='purple', label="C'(t) = dC/dt")
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.set_xlabel('Days after application')
ax2.set_ylabel('Rate of change (mg/L/day)')
ax2.set_title('Rate of Pesticide Degradation')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

## PROBLEM BRIEF: W4B (for Group 6 presentation in Week 5)

**"Drug Pharmacokinetics: Dosing for Diabetes Management"**

---

### SCENARIO

You are a pharmacologist designing a dosing protocol for metformin, a diabetes medication. After oral administration, blood concentration follows:$C(t) = 85(e^{-0.12t} - e^{-0.45t}) $C(t)=85(e−0.12t−e−0.45t)

where:
- $C(t)$C(t)= blood concentration (μg/mL)
- $t$t= hours after ingestion
- The double exponential accounts for absorption (fast) and elimination (slow)

**Therapeutic constraints:**
- Minimum effective concentration:**15 μg/mL**(below this, poor glucose control)
- Maximum safe concentration:**100 μg/mL**(above this, risk of lactic acidosis)
- Patients must maintain therapeutic levels for 12-hour intervals between doses

---

### YOUR TASK

**Part A: Concentration Profile Analysis (20 minutes)**
- 

Calculate concentration at $t = 0, 1, 2, 4, 8, 12$t=0,1,2,4,8,12hours
- When does peak concentration occur? (look for the maximum in your table)
- What is the peak value?

- 

Find the**exact time**of peak concentration using calculus:
- Take the derivative: $C'(t) = 85[-0.12e^{-0.12t} - (-0.45)e^{-0.45t}]$C′(t)=85[−0.12e−0.12t−(−0.45)e−0.45t]
- Set $C'(t) = 0$C′(t)=0and solve for $t$t
- Hint: $-0.12e^{-0.12t} + 0.45e^{-0.45t} = 0$−0.12e−0.12t+0.45e−0.45t=0
- Rearrange: $0.45e^{-0.45t} = 0.12e^{-0.12t}$0.45e−0.45t=0.12e−0.12t
- Divide both sides by $e^{-0.45t}$e−0.45t: $0.45 = 0.12e^{0.33t}$0.45=0.12e0.33t
- Solve for $t$t

- 

Verify that the peak is safe:
- Calculate $C(t_{peak})$C(tpeak​)
- Is it below 100 μg/mL?

**Part B: Therapeutic Window (20 minutes)**
- 

Determine when concentration drops below therapeutic threshold:
- Solve numerically or graphically: $85(e^{-0.12t} - e^{-0.45t}) = 15$85(e−0.12t−e−0.45t)=15
- Use Python to find the intersection point
- How many hours of therapeutic coverage per dose?

- 

Can patients safely use a 12-hour dosing interval?
- Compare therapeutic duration to 12 hours
- If not sufficient, what minimum concentration will they have at 12 hours?

- 

To achieve 12-hour coverage with $C(12) = 15$C(12)=15μg/mL, what dose multiplier is needed?
- New model: $C(t) = D \cdot (e^{-0.12t} - e^{-0.45t})$C(t)=D⋅(e−0.12t−e−0.45t)where $D$Dis the dose factor
- Solve: $D(e^{-0.12 \times 12} - e^{-0.45 \times 12}) = 15$D(e−0.12×12−e−0.45×12)=15
- Does this keep peak concentration safe?

**Part C: Multiple Dosing Strategy (15 minutes)**
- 

If a second dose is taken at $t = 12$t=12hours:
- Residual from first dose: $C_1(12) = 85(e^{-0.12 \times 12} - e^{-0.45 \times 12})$C1​(12)=85(e−0.12×12−e−0.45×12)
- New dose contribution: $C_2(t) = 85(e^{-0.12(t-12)} - e^{-0.45(t-12)})$C2​(t)=85(e−0.12(t−12)−e−0.45(t−12))for $t \geq 12$t≥12
- Total concentration at $t = 12^+$t=12+: $C_{total}(12) = C_1(12) + 85$Ctotal​(12)=C1​(12)+85
- Will this cause unsafe accumulation?

- 

**Steady state:**After many doses, concentration oscillates between a minimum and maximum.
- Estimate the steady-state maximum
- Is it safe?

**Part D: Rate of Elimination (10 minutes)**
- 

Calculate the rate of change of concentration:
- $C'(t) = 85[-0.12e^{-0.12t} + 0.45e^{-0.45t}]$C′(t)=85[−0.12e−0.12t+0.45e−0.45t]
- Evaluate at $t = 2$t=2hours (around peak)
- Evaluate at $t = 10$t=10hours (late elimination phase)
- Which elimination rate is faster? Why does this make sense physiologically?

- 

The two exponential terms represent:
- $e^{-0.45t}$e−0.45t: rapid absorption and distribution
- $e^{-0.12t}$e−0.12t: slower elimination
- At what time does elimination become the dominant process?

---

### DELIVERABLES

- Completed Group Worksheet with derivative work
- Graph showing concentration profile with therapeutic window
- **Group 6 ONLY:**Prepare 10-minute presentation for Week 5

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

t = np.linspace(0, 24, 500)
C = 85 * (np.exp(-0.12*t) - np.exp(-0.45*t))

# Derivative
dC_dt = 85 * (-0.12*np.exp(-0.12*t) + 0.45*np.exp(-0.45*t))

# Find peak time
def derivative(t):
    return 85 * (-0.12*np.exp(-0.12*t) + 0.45*np.exp(-0.45*t))

t_peak = fsolve(derivative, 2)[0]
C_peak = 85 * (np.exp(-0.12*t_peak) - np.exp(-0.45*t_peak))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top: Concentration
ax1.plot(t, C, linewidth=2, label='Blood Concentration C(t)')
ax1.axhline(y=15, color='r', linestyle='--', label='Minimum therapeutic (15 μg/mL)')
ax1.axhline(y=100, color='orange', linestyle='--', label='Maximum safe (100 μg/mL)')
ax1.plot(t_peak, C_peak, 'go', markersize=10, label=f'Peak at t={t_peak:.2f}h, C={C_peak:.1f} μg/mL')
ax1.fill_between(t, 15, 100, alpha=0.2, color='green', label='Therapeutic window')
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Concentration (μg/mL)')
ax1.set_title('Metformin Pharmacokinetics')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Bottom: Rate of change
ax2.plot(t, dC_dt, linewidth=2, color='purple', label="C'(t) = dC/dt")
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.axvline(x=t_peak, color='g', linestyle=':', alpha=0.5, label=f'Peak at t={t_peak:.2f}h')
ax2.set_xlabel('Time (hours)')
ax2.set_ylabel('Rate of change (μg/mL/hour)')
ax2.set_title('Rate of Concentration Change')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

---

# Week 5: Optimization

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W5

**"Designing an Optimal Wildlife Corridor"**

---

#### SCENARIO

The Department of Biodiversity is designing a wildlife corridor to connect two nature reserves. The corridor must be rectangular, with a total perimeter fence of 2000 meters available.

Ecologists have determined that the corridor's effectiveness for wildlife movement depends on its area (larger is better) but also its shape. Very narrow corridors create "edge effects" that reduce habitat quality.

**The Challenge:**Design a corridor that:
- Uses exactly 2000 m of fencing (perimeter constraint)
- Maximizes usable area
- Meets minimum width requirement of 200 m (prevents edge effects)

---

#### YOUR TASK

**Part A: Setting Up the Optimization (15 minutes)**
- 

Let $x$x= width of corridor (meters) and $y$y= length (meters).
- 

Write the**constraint equation**for perimeter:$2x + 2y = 2000 $2x+2y=2000
- 

Solve the constraint for $y$yin terms of $x$x:$y = ? $y=?
- 

Write the**objective function**for area:$A(x) = x \cdot y $A(x)=x⋅y

Substitute your expression for $y$yto get $A$Aas a function of $x$xonly.
- 

What is the domain of $x$x?
- Mathematical: $x > 0$x>0(width must be positive)
- Physical: $x \geq 200$x≥200(minimum width) and $x \leq ?$x≤?(ensure $y > 0$y>0)

**Part B: Finding the Optimal Dimensions (25 minutes)**
- 

Take the derivative: $A'(x) = ?$A′(x)=?
- 

Find the critical point by solving $A'(x) = 0$A′(x)=0
- 

Verify this is a maximum:
- Calculate $A''(x)$A′′(x)
- Evaluate $A''(x_{critical})$A′′(xcritical​)
- Since $A''<0$A′′<0, this is a maximum ✓

- 

Is the critical point within the feasible range $[200, ?]$[200,?]?
- If YES: this is the optimal width
- If NO: the optimum is at a boundary

- 

Compare the area at:
- The critical point (if feasible)
- The minimum width boundary ($x = 200$x=200)
- The maximum width boundary (where $y = 200$y=200, by symmetry)

Which gives the largest area?

**Part C: Sensitivity Analysis (15 minutes)**
- 

Budget constraints may reduce available fencing to 1800 m.
- Repeat the optimization with perimeter = 1800 m
- How much area is lost compared to the 2000 m scenario?

- 

If the minimum width increases to 250 m (stricter ecological requirements):
- Does this change the optimal design for 2000 m of fencing?
- Calculate the new optimal area

**Part D: Recommendation (5 minutes)**
- Write a brief (3-4 sentence) recommendation to the Department:
- Optimal corridor dimensions
- Expected habitat area
- Trade-offs between budget (fencing length) and ecological requirements (minimum width)

---

#### DELIVERABLES

- Completed Group Worksheet with optimization work
- Graph of $A(x)$A(x)showing the critical point and constraints
- **Groups 7 & 1:**Prepare 10-minute presentation for Week 6

---

#### PRESENTATION GUIDANCE (Groups 7 & 1)

Focus on:
- How to handle constraints in optimization problems
- The method: constraint substitution → single-variable optimization
- Checking feasibility of mathematical solutions against physical constraints
- Real-world trade-offs in your recommendation

---

#### HINTS / SCAFFOLDING

**General strategy for constrained optimization:**
- Write constraint equation
- Solve for one variable in terms of the other
- Substitute into objective function → single-variable function
- Take derivative and find critical points
- Check feasibility and boundary values

**For this problem:**
- Constraint: $2x + 2y = 2000$2x+2y=2000→ $y = 1000 - x$y=1000−x
- Objective: $A(x) = x(1000 - x) = 1000x - x^2$A(x)=x(1000−x)=1000x−x2
- Derivative: $A'(x) = 1000 - 2x$A′(x)=1000−2x
- Critical point: $1000 - 2x = 0$1000−2x=0→ $x = 500$x=500

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(200, 800, 500)
A = x * (1000 - x)  # Area function

# Critical point
x_crit = 500
A_crit = x_crit * (1000 - x_crit)

plt.figure(figsize=(10, 6))
plt.plot(x, A, linewidth=2, label='Area A(x)')
plt.plot(x_crit, A_crit, 'ro', markersize=10, label=f'Optimum: x={x_crit}m, A={A_crit:,}m²')
plt.axvline(x=200, color='orange', linestyle='--', alpha=0.5, label='Min width = 200m')
plt.xlabel('Width x (meters)')
plt.ylabel('Area (m²)')
plt.title('Wildlife Corridor: Area vs Width')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W5A (for Group 7 presentation in Week 6 & Group 1 second presentation)

**"Solar Farm Economics: Optimal Panel Configuration"**

---

### SCENARIO

A renewable energy company is designing a 50-hectare solar farm near Geraldton. The farm will use rectangular arrays of solar panels. Due to shading effects and maintenance access requirements, there are engineering constraints on the configuration.

**Economic model:**Annual revenue (in thousands of dollars) is modeled as:$R(x) = -2x^2 + 180x - 1600 $R(x)=−2x2+180x−1600

where $x$xis the average spacing between panel rows (in meters). This accounts for:
- More spacing → less shading → higher efficiency per panel
- More spacing → fewer total panels → lower total output
- Optimal balance exists between these competing factors

**Constraints:**
- Minimum spacing: $x \geq 8$m (maintenance access)
- Maximum spacing: $x \leq 60$m (land area limit)
- Panels must generate positive revenue

---

### YOUR TASK

**Part A: Critical Point Analysis (25 minutes)**
- 

Find the derivative $R'(x)$R′(x):
- Use power rule on each term
- Interpret: $R'(x)$R′(x)represents the**rate of change**of revenue with respect to spacing

- 

Find the critical point by solving $R'(x) = 0$R′(x)=0:
- Set your derivative equal to zero
- Solve for $x$x
- This gives the**candidate**for optimal spacing

- 

Verify this is a maximum using the**second derivative test**:
- Calculate $R''(x)$R′′(x)
- Evaluate $R''(x_{critical})$R′′(xcritical​)
- If $R''<0$R′′<0→ local maximum ✓
- If $R'' > 0$R′′>0→ local minimum ✗

- 

Calculate the maximum revenue:
- Substitute $x_{optimal}$xoptimal​into $R(x)$R(x)
- Express in dollars per year

**Part B: Constraint Boundaries (20 minutes)**
- 

The critical point must lie within the feasible region $[8, 60]$[8,60]. Check:
- Is $8 \leq x_{optimal} \leq 60$8≤xoptimal​≤60?
- If YES: proceed to step 6
- If NO: the optimum is at a boundary

- 

Compare revenue at three points:
- $R(x_{optimal})$R(xoptimal​)[if within constraints]
- $R(8)$R(8)[minimum spacing boundary]
- $R(60)$R(60)[maximum spacing boundary]
- Which configuration yields highest revenue?

- 

Find the**break-even points**where revenue = 0:
- Solve: $-2x^2 + 180x - 1600 = 0$−2x2+180x−1600=0
- Use quadratic formula: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$x=2a−b±b2−4ac​​
- Interpret: below the lower break-even point, the farm loses money

**Part C: Sensitivity Analysis (15 minutes)**
- 

Climate change projections suggest reduced solar irradiance will decrease revenue by 15%.
- New model: $R_{climate}(x) = 0.85 \times R(x) = -1.7x^2 + 153x - 1360$Rclimate​(x)=0.85×R(x)=−1.7x2+153x−1360
- Find the new optimal spacing
- How much does optimal revenue decrease?

- 

To compensate for revenue loss, the company can install higher-efficiency panels (20% boost):
- New model: $R_{upgrade}(x) = 1.20 \times R(x) = -2.4x^2 + 216x - 1920$Rupgrade​(x)=1.20×R(x)=−2.4x2+216x−1920
- Find the new optimal spacing and revenue
- Compare to the baseline scenario

**Part D: Economic Interpretation (5 minutes)**
- Write a brief (4-5 sentence) recommendation to the company's CEO covering:
- Optimal panel spacing
- Expected annual revenue
- Sensitivity to climate change
- Whether high-efficiency panel upgrade is justified

---

### DELIVERABLES

- Completed Group Worksheet showing all derivative work
- Graph of $R(x)$R(x)with critical point and boundaries marked
- **Group 7 in Week 6 OR Group 1 (second presentation) in Week 6:**Prepare 10-minute presentation

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(5, 65, 500)
R = -2*x**2 + 180*x - 1600

# Derivative
dR_dx = -4*x + 180

# Critical point
x_crit = -180 / (-4)  # From dR/dx = 0
R_crit = -2*x_crit**2 + 180*x_crit - 1600

# Boundaries
R_min = -2*8**2 + 180*8 - 1600
R_max = -2*60**2 + 180*60 - 1600

plt.figure(figsize=(10, 6))
plt.plot(x, R, linewidth=2, label='Revenue R(x)')
plt.plot(x_crit, R_crit, 'ro', markersize=10, label=f'Optimal: x={x_crit:.1f}m, R=${R_crit:.0f}k')
plt.axvline(x=8, color='orange', linestyle='--', alpha=0.5, label='Min spacing (8m)')
plt.axvline(x=60, color='orange', linestyle='--', alpha=0.5, label='Max spacing (60m)')
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.xlabel('Panel Spacing x (meters)')
plt.ylabel('Annual Revenue (thousands $)')
plt.title('Solar Farm Revenue Optimization')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(-500, 2500)
plt.show()

```

---

## PROBLEM BRIEF: W5B (for Group 1 second presentation in Week 6)

**"Aquaculture Profit: Optimal Stocking Density for Barramundi"**

---

### SCENARIO

A barramundi aquaculture farm in Exmouth is optimizing its fish stocking density. The profit model accounts for:
- Higher density → more fish → higher total yield
- Higher density → competition for oxygen/food → higher mortality → lower individual fish weight

**Profit function:**$P(d) = -0.5d^2 + 55d - 800 $P(d)=−0.5d2+55d−800

where:
- $P(d)$P(d)= annual profit (thousands of dollars)
- $d$d= stocking density (fish per 100 m³)

**Constraints:**
- Minimum density: $d \geq 10$d≥10(economic viability)
- Maximum density: $d \geq 80$d≥80(animal welfare regulations)

---

### YOUR TASK

**Part A: Optimization Using Calculus (25 minutes)**
- 

Find the profit-maximizing stocking density:
- Calculate $P'(d) = \frac{dP}{dd}$P′(d)=dddP​
- Solve $P'(d) = 0$P′(d)=0for $d$d
- This gives the critical point

- 

Confirm this is a maximum:
- Calculate second derivative $P''(d)$P′′(d)
- Since $P''(d) = -1<0$P′′(d)=−1<0everywhere, the function is concave down
- Therefore the critical point is a global maximum ✓

- 

Calculate maximum profit:
- Substitute $d_{optimal}$doptimal​into $P(d)$P(d)
- Express in dollars per year

- 

Check feasibility:
- Is $10 \leq d_{optimal} \leq 80$10≤doptimal​≤80?
- If NO: the constrained optimum is at a boundary

**Part B: Constrained Optimization (20 minutes)**
- 

Compare profit at critical point vs. boundaries:
- $P(d_{optimal})$P(doptimal​)[if within $[10, 80]$[10,80]]
- $P(10)$P(10)[minimum density]
- $P(80)$P(80)[maximum density]
- Which is the true optimum given constraints?

- 

Find the break-even density levels:
- Solve: $-0.5d^2 + 55d - 800 = 0$−0.5d2+55d−800=0
- Multiply by -2: $d^2 - 110d + 1600 = 0$d2−110d+1600=0
- Use quadratic formula
- Interpret: farm loses money outside this range

- 

Calculate the**marginal profit**at current operating density $d = 40$d=40:
- $P'(40) = ?$P′(40)=?dollars per fish (per 100 m³)
- If $P'(40) > 0$P′(40)>0: increasing density increases profit
- If $P'(40)<0$P′(40)<0: decreasing density increases profit
- What does this suggest?

**Part C: Comparative Scenarios (15 minutes)**
- 

A disease outbreak reduces survival rates, decreasing the profit function to:$P_{disease}(d) = -0.5d^2 + 55d - 1200 $Pdisease​(d)=−0.5d2+55d−1200
- Find the new optimal density
- How much does profit decrease at the optimum?
- Does the farm still break even?

- 

Installing aeration systems improves oxygen levels, changing the model to:$P_{aeration}(d) = -0.4d^2 + 60d - 900 $Paeration​(d)=−0.4d2+60d−900
- Find the new optimal density (note: less steep quadratic → flatter profit curve)
- Calculate maximum profit
- Is the aeration investment worthwhile?

**Part D: Management Recommendation (5 minutes)**
- Write a brief (4-5 sentence) advisory memo to the farm manager:
- Recommended stocking density
- Expected annual profit
- Risk mitigation strategies (disease, aeration)
- Monitoring parameters

---

### DELIVERABLES

- Completed Group Worksheet with optimization calculations
- Graph showing profit function and critical point
- **Group 1 (second presentation) in Week 6:**Prepare 10-minute presentation

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(5, 90, 500)
P = -0.5*d**2 + 55*d - 800

# Derivative
dP_dd = -d + 55

# Critical point
d_crit = 55 / 1  # From dP/dd = 0
P_crit = -0.5*d_crit**2 + 55*d_crit - 800

# Disease scenario
P_disease = -0.5*d**2 + 55*d - 1200

# Aeration scenario
P_aeration = -0.4*d**2 + 60*d - 900
d_aer_crit = 60 / 0.8
P_aer_crit = -0.4*d_aer_crit**2 + 60*d_aer_crit - 900

plt.figure(figsize=(10, 6))
plt.plot(d, P, linewidth=2, label='Baseline P(d)', color='blue')
plt.plot(d, P_disease, linewidth=2, linestyle='--', label='Disease scenario', color='red')
plt.plot(d, P_aeration, linewidth=2, linestyle=':', label='Aeration upgrade', color='green')

plt.plot(d_crit, P_crit, 'bo', markersize=10, label=f'Baseline opt: d={d_crit:.0f}, P=${P_crit:.0f}k')
plt.plot(d_aer_crit, P_aer_crit, 'go', markersize=10, label=f'Aeration opt: d={d_aer_crit:.0f}')

plt.axvline(x=10, color='orange', linestyle='--', alpha=0.5)
plt.axvline(x=80, color='orange', linestyle='--', alpha=0.5)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

plt.xlabel('Stocking Density d (fish per 100 m³)')
plt.ylabel('Annual Profit (thousands $)')
plt.title('Barramundi Aquaculture: Stocking Density Optimization')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

```

---

---

# Week 6: Integration (Antiderivatives)

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W6

**"Carbon Sequestration: From Rates to Totals"**

---

#### SCENARIO

The Australian government is evaluating carbon offset projects. Your team has been asked to analyze a reforestation project in the Pilbara region.

Forest ecologists have modeled the rate of carbon sequestration (absorption) for the proposed forest:$R(t) = 12e^{-0.05t} $R(t)=12e−0.05t

where $R(t)$R(t)is the sequestration rate in tonnes of CO₂ per hectare per year, and $t$tis years since planting.

**Key observation:**This rate*decreases*over time because young trees absorb carbon faster than mature trees.

**Project parameters:**
- Project area: 500 hectares
- Project lifetime: 40 years
- Carbon credit price: $25 per tonne of CO₂

The government wants to know:**How much total carbon will this project sequester, and what is it worth?**

---

#### YOUR TASK

**Part A: Understanding Rates vs. Totals (15 minutes)**
- 

Calculate the sequestration rate at $t = 0$t=0, $t = 10$t=10, and $t = 30$t=30years. What trend do you observe?
- 

If the rate were*constant*at $R(0) = 12$R(0)=12tonnes/ha/year, how much carbon would be sequestered in 40 years per hectare? Why will the actual total be less?
- 

Explain in words why we need integration (not just multiplication) to find the total carbon sequestered.

**Part B: Antiderivatives (20 minutes)**
- 

Find the indefinite integral (antiderivative):$\int 12e^{-0.05t}\,dt $∫12e−0.05tdt

Remember: $\int e^{kt}\,dt = \frac{1}{k}e^{kt} + C$∫ektdt=k1​ekt+C
- 

Verify your answer by differentiating. Does the derivative equal the original integrand?
- 

Find the specific antiderivative $F(t)$F(t)such that $F(0) = 0$F(0)=0. (This represents cumulative carbon sequestered since planting.)

**Part C: Project Valuation (20 minutes)**
- 

Using your antiderivative, calculate the total carbon sequestered per hectare over 40 years:$\text{Total} = F(40) - F(0) $Total=F(40)−F(0)
- 

Calculate total carbon sequestered across the entire 500-hectare project.
- 

Calculate the total value of carbon credits generated over 40 years.
- 

The government requires projects to deliver at least 100,000 tonnes of CO₂ sequestration to qualify for the offset program. Does this project qualify?

**Part D: Extension – Comparison (if time permits)**
- 

An alternative project proposes planting a different species with sequestration rate:$R_2(t) = 8(1 - e^{-0.1t}) $R2​(t)=8(1−e−0.1t)

This rate*increases*over time (trees take longer to establish but eventually sequester more).

Without full calculation, predict: Which project sequesters more carbon over 40 years? Justify your reasoning.

---

#### DELIVERABLES

- Completed Group Worksheet
- **Groups 2 & 3:**Prepare 10-minute presentation for Week 7

---

#### PRESENTATION GUIDANCE (Groups 2 & 3)

**Focus:**Why integration is the right tool for "rate to total" problems

Structure suggestion:
- The problem: We have a rate, we need a total
- Why multiplication fails (rate isn't constant)
- The antiderivative: reversing differentiation
- The answer and its policy implications

---

#### HINTS / SCAFFOLDING

**Exponential integration rule:**$\int e^{kt}\,dt = \frac{1}{k}e^{kt} + C $∫ektdt=k1​ekt+C

For $\int 12e^{-0.05t}\,dt$∫12e−0.05tdt:
- Factor out the constant 12
- Apply the rule with $k = -0.05$k=−0.05
- Result: $12 \times \frac{1}{-0.05}e^{-0.05t} + C = -240e^{-0.05t} + C$12×−0.051​e−0.05t+C=−240e−0.05t+C

**To find specific antiderivative with $F(0) = 0$F(0)=0:**
- Set $F(0) = -240e^0 + C = -240 + C = 0$F(0)=−240e0+C=−240+C=0
- Solve for $C$C

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 50, 500)
R = 12 * np.exp(-0.05 * t)

# Cumulative (antiderivative with F(0)=0)
F = 240 * (1 - np.exp(-0.05 * t))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Rate
ax1.plot(t, R, linewidth=2, color='green')
ax1.set_xlabel('Years since planting')
ax1.set_ylabel('Sequestration rate (tonnes/ha/year)')
ax1.set_title('Carbon Sequestration Rate')
ax1.grid(True, alpha=0.3)

# Cumulative
ax2.plot(t, F, linewidth=2, color='blue')
ax2.set_xlabel('Years since planting')
ax2.set_ylabel('Cumulative carbon (tonnes/ha)')
ax2.set_title('Total Carbon Sequestered')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W6A (for Group 2 presentation in Week 7)

**"Soil Carbon Sequestration: Regenerative Agriculture"**

---

### SCENARIO

A wheat farm in the Wheatbelt is transitioning to regenerative agriculture practices (no-till farming, cover crops, diverse rotations). Soil scientists have measured the rate of carbon accumulation in the topsoil:$R(t) = 15e^{-0.08t} $R(t)=15e−0.08t

where:
- $R(t)$R(t)= carbon sequestration rate (tonnes C per hectare per year)
- $t$t= years since transition began

**Key insight:**Rate decreases over time because:
- Initially, bare/degraded soil absorbs carbon rapidly
- As soil health improves, sequestration slows
- Eventually approaches a new equilibrium

**Farm details:**
- Total area: 800 hectares
- Transition started in 2020
- Carbon market price: $28 per tonne CO₂-equivalent (note: 1 tonne C = 3.67 tonnes CO₂)

---

### YOUR TASK

**Part A: Rate vs. Cumulative Carbon (20 minutes)**
- 

Calculate the sequestration rate at $t = 0, 5, 10, 20$t=0,5,10,20years
- What trend do you observe?
- Why does the rate decrease?

- 

If the rate were constant at $R(0) = 15$R(0)=15tonnes/ha/year:
- How much carbon would accumulate in 25 years per hectare?
- Why will the actual total be less?

- 

Explain in words why we need**integration**(not just multiplication) to find total carbon sequestered.

**Part B: Finding the Antiderivative (20 minutes)**
- 

Find the indefinite integral:$\int 15e^{-0.08t}\,dt $∫15e−0.08tdt
- Remember: $\int e^{kt}\,dt = \frac{1}{k}e^{kt} + C$∫ektdt=k1​ekt+C
- Apply the rule with $k = -0.08$k=−0.08

- 

Verify your answer by differentiating:
- Does $\frac{d}{dt}[F(t)] = R(t)$dtd​[F(t)]=R(t)?

- 

Find the specific antiderivative $C(t)$C(t)where $C(0) = 0$C(0)=0:
- This represents**cumulative carbon**sequestered since $t=0$t=0
- Substitute $t=0$t=0and solve for the constant

**Part C: Carbon Credit Calculation (20 minutes)**
- 

Calculate total carbon sequestered per hectare over 25 years:$\text{Total} = C(25) - C(0) $Total=C(25)−C(0)
- 

Calculate total carbon across the entire 800-hectare farm.
- 

Convert to CO₂-equivalent:
- Multiply by 3.67 (molecular weight ratio)
- This is the tradeable carbon credit quantity

- 

Calculate total carbon credit revenue over 25 years:
- (Total CO₂-e tonnes) × ($28 per tonne)
- This is additional income from carbon farming

**Part D: Economic Comparison (5 minutes)**
- Traditional farming on this land yields $400/ha/year profit.
- Over 25 years: $400 × 800 × 25 = $8,000,000$8,000,000
- Compare to carbon credit revenue
- What fraction of traditional income do carbon credits represent?

---

### DELIVERABLES

- Completed Group Worksheet showing integration work
- Graph of $R(t)$R(t)and $C(t)$C(t)on separate subplots
- **Group 2 presentation in Week 7**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 30, 500)
R = 15 * np.exp(-0.08 * t)

# Cumulative carbon (antiderivative with C(0)=0)
C = -15/0.08 * np.exp(-0.08 * t) - (-15/0.08 * np.exp(0))
# Simplify: C = 187.5 * (1 - exp(-0.08t))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top: Rate
ax1.plot(t, R, linewidth=2, color='green', label='Sequestration rate R(t)')
ax1.set_xlabel('Years since transition')
ax1.set_ylabel('Rate (tonnes C/ha/year)')
ax1.set_title('Carbon Sequestration Rate')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Bottom: Cumulative
C_actual = 187.5 * (1 - np.exp(-0.08*t))
ax2.plot(t, C_actual, linewidth=2, color='blue', label='Cumulative carbon C(t)')
ax2.axhline(y=187.5, color='gray', linestyle='--', label='Asymptotic maximum')
ax2.set_xlabel('Years since transition')
ax2.set_ylabel('Cumulative carbon (tonnes C/ha)')
ax2.set_title('Total Carbon Sequestered')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

## PROBLEM BRIEF: W6B (for Group 3 second presentation in Week 7)

**"Groundwater Recharge: Managed Aquifer Recharge"**

---

### SCENARIO

The Water Corporation is implementing a managed aquifer recharge (MAR) scheme in the Perth Basin. During winter, excess stormwater is infiltrated into a confined aquifer. Engineers have modeled the infiltration rate:$I(t) = 20e^{-0.12t} $I(t)=20e−0.12t

where:
- $I(t)$I(t)= infiltration rate (megalitres per day)
- $t$t= days since infiltration began

**Why does rate decrease?**
- Initially, hydraulic gradient is steep → fast infiltration
- As aquifer fills, gradient flattens → slower infiltration
- Eventually reaches equilibrium

**Project parameters:**
- Winter infiltration period: 120 days (May–August)
- Aquifer storage target: 1,500 ML
- Water value: $1.50 per kilolitre (= $1,500 per ML)

---

### YOUR TASK

**Part A: Understanding Rate vs. Volume (20 minutes)**
- 

Calculate infiltration rate at $t = 0, 30, 60, 90, 120$t=0,30,60,90,120days
- Create a table
- Describe the trend

- 

If the rate were constant at $I(0) = 20$I(0)=20ML/day:
- How much water would infiltrate in 120 days?
- Why will actual total be less?

- 

Explain why integration is needed to find total volume infiltrated.

**Part B: Antiderivative Calculation (20 minutes)**
- 

Find the indefinite integral:$\int 20e^{-0.12t}\,dt $∫20e−0.12tdt
- Use: $\int e^{kt}\,dt = \frac{1}{k}e^{kt} + C$∫ektdt=k1​ekt+C
- Simplify your answer

- 

Verify by differentiating:
- Check that $\frac{d}{dt}[V(t)] = I(t)$dtd​[V(t)]=I(t)

- 

Find the specific function $V(t)$V(t)where $V(0) = 0$V(0)=0:
- This represents**cumulative volume**infiltrated
- Solve for the integration constant

**Part C: Water Storage Analysis (20 minutes)**
- 

Calculate total volume infiltrated over 120-day winter period:$V(120) = ? $V(120)=?
- Express in megalitres

- 

Does the project meet its target of 1,500 ML?
- Compare $V(120)$V(120)to target
- If not, how many additional days would be needed?

- 

Calculate the economic value of recharged water:
- Volume × $1,500 per ML
- This is the benefit of the MAR scheme

- 

Calculate average infiltration rate over the 120 days:$\bar{I} = \frac{V(120) - V(0)}{120 - 0} $Iˉ=120−0V(120)−V(0)​
- Compare to initial rate $I(0)$I(0)
- Express as a percentage

**Part D: Seasonal Extension (5 minutes)**
- To reach the 1,500 ML target, the Water Corporation considers extending the season.
- Solve: $V(t) = 1500$V(t)=1500for $t$t
- How many extra days beyond 120 are needed?
- Is this feasible given rainfall patterns?

---

### DELIVERABLES

- Completed Group Worksheet with integration calculations
- Graph of $I(t)$I(t)and $V(t)$V(t)vs time
- **Group 3 (second presentation) in Week 7**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 150, 500)
I = 20 * np.exp(-0.12 * t)

# Cumulative volume (antiderivative with V(0)=0)
# V(t) = -20/0.12 * exp(-0.12t) + C
# V(0) = 0 => C = 20/0.12
V = (20/0.12) * (1 - np.exp(-0.12*t))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top: Infiltration rate
ax1.plot(t, I, linewidth=2, color='blue', label='Infiltration rate I(t)')
ax1.set_xlabel('Days since start')
ax1.set_ylabel('Rate (ML/day)')
ax1.set_title('Managed Aquifer Recharge: Infiltration Rate')
ax1.axvline(x=120, color='orange', linestyle='--', label='End of winter (120 days)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Bottom: Cumulative volume
ax2.plot(t, V, linewidth=2, color='green', label='Cumulative volume V(t)')
ax2.axhline(y=1500, color='r', linestyle='--', label='Target (1500 ML)')
ax2.axvline(x=120, color='orange', linestyle='--', alpha=0.5)
ax2.set_xlabel('Days since start')
ax2.set_ylabel('Volume (ML)')
ax2.set_title('Total Water Infiltrated')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

---

# Week 7: Definite Integrals and Economic Surplus

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W7

**"Market Welfare: Who Benefits from Trade?"**

---

#### SCENARIO

The Western Australian grain market is being analyzed for a policy review. Economists have estimated the following supply and demand functions for wheat:

**Demand function:**$Q_d = 500 - 4P$Qd​=500−4P(quantity in thousands of tonnes, price in $/tonne)

**Supply function:**$Q_s = -100 + 2P$Qs​=−100+2P

The government is considering a price support policy and needs to understand how the market currently distributes benefits between consumers and producers.

**Key concepts:**
- **Consumer Surplus (CS):**The benefit consumers receive from paying less than their maximum willingness to pay
- **Producer Surplus (PS):**The benefit producers receive from selling at a price higher than their minimum acceptable price
- **Total Welfare:**CS + PS

---

#### YOUR TASK

**Part A: Market Equilibrium (15 minutes)**
- 

Find the equilibrium price $P^*$P∗by setting $Q_d = Q_s$Qd​=Qs​.
- 

Find the equilibrium quantity $Q^*$Q∗.
- 

Find the**maximum willingness to pay**(price at which $Q_d = 0$Qd​=0).
- 

Find the**minimum acceptable price**(price at which $Q_s = 0$Qs​=0).

**Part B: Setting Up the Surplus Integrals (20 minutes)**

To calculate surplus, we need the**inverse**demand and supply functions (price as a function of quantity):
- 

Rearrange $Q_d = 500 - 4P$Qd​=500−4Pto get $P = D(Q)$P=D(Q)(inverse demand).
- 

Rearrange $Q_s = -100 + 2P$Qs​=−100+2Pto get $P = S(Q)$P=S(Q)(inverse supply).
- 

**Consumer Surplus formula:**$CS = \int_0^{Q^*} D(Q)\,dQ - P^* \cdot Q^* $CS=∫0Q∗​D(Q)dQ−P∗⋅Q∗

Explain in words what each term represents. Why do we subtract $P^* \cdot Q^*$P∗⋅Q∗?
- 

**Producer Surplus formula:**$PS = P^* \cdot Q^* - \int_0^{Q^*} S(Q)\,dQ $PS=P∗⋅Q∗−∫0Q∗​S(Q)dQ

Explain in words what each term represents.

**Part C: Calculating Surplus (20 minutes)**
- 

Calculate Consumer Surplus using the integral formula. Show all steps.
- 

Calculate Producer Surplus using the integral formula. Show all steps.
- 

Calculate Total Welfare = CS + PS.
- 

**Shortcut verification:**For linear demand and supply, the surplus areas are triangles:
- $CS = \frac{1}{2} \times Q^* \times (P_{max} - P^*)$CS=21​×Q∗×(Pmax​−P∗)
- $PS = \frac{1}{2} \times Q^* \times (P^* - P_{min})$PS=21​×Q∗×(P∗−Pmin​)

Verify your integral calculations match these triangle formulas.

**Part D: Policy Analysis (if time permits)**
- The government proposes a price floor of $120/tonne (above equilibrium).
- At $P = 120$P=120, what quantity do consumers demand?
- At $P = 120$P=120, what quantity do producers supply?
- What problem does this create?

---

#### DELIVERABLES

- Completed Group Worksheet
- **Groups 4 & 5:**Prepare 10-minute presentation for Week 8

---

#### PRESENTATION GUIDANCE (Groups 4 & 5)

**Focus:**How integration quantifies economic welfare

Suggested visuals:
- Supply and demand curves with equilibrium marked
- Shaded areas showing CS and PS
- Comparison: integral method vs. geometry

---

#### HINTS / SCAFFOLDING

**Integration reminder:**$\int (ax + b)\,dx = \frac{a}{2}x^2 + bx + C $∫(ax+b)dx=2a​x2+bx+C

**Definite integral:**$\int_a^b f(x)\,dx = F(b) - F(a) $∫ab​f(x)dx=F(b)−F(a)

where $F(x)$F(x)is an antiderivative of $f(x)$f(x).

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

Q = np.linspace(0, 500, 500)

# Inverse functions
P_demand = (500 - Q) / 4
P_supply = (Q + 100) / 2

# Equilibrium
Q_star = 100  # From Qd = Qs
P_star = 100

plt.figure(figsize=(10, 8))
plt.plot(Q, P_demand, linewidth=2, label='Demand', color='blue')
plt.plot(Q, P_supply, linewidth=2, label='Supply', color='red')
plt.plot(Q_star, P_star, 'go', markersize=12, label=f'Equilibrium (Q={Q_star}, P={P_star})')

# Consumer surplus area
Q_cs = np.linspace(0, Q_star, 100)
P_cs = (500 - Q_cs) / 4
plt.fill_between(Q_cs, P_star, P_cs, alpha=0.3, color='blue', label='Consumer Surplus')

# Producer surplus area
Q_ps = np.linspace(0, Q_star, 100)
P_ps = (Q_ps + 100) / 2
plt.fill_between(Q_ps, P_ps, P_star, alpha=0.3, color='red', label='Producer Surplus')

plt.xlabel('Quantity (thousands of tonnes)')
plt.ylabel('Price ($/tonne)')
plt.title('Wheat Market: Consumer and Producer Surplus')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W7A (for Group 4 second presentation in Week 8)

**"Wine Market Analysis: Assessing Regional Wine Policy"**

---

### SCENARIO

The Margaret River Wine Association is evaluating the impact of a proposed minimum price policy. Economic consultants have estimated supply and demand for premium wine (measured in thousands of bottles per year):

**Demand:**$Q_d = 800 - 5P$Qd​=800−5P(quantity demanded, price in $/bottle)
**Supply:**$Q_s = -200 + 3P$Qs​=−200+3P(quantity supplied)

The Association wants to understand who benefits under current free-market conditions before implementing price controls.

---

### YOUR TASK

**Part A: Market Equilibrium (15 minutes)**
- 

Find equilibrium price $P^*$P∗by setting $Q_d = Q_s$Qd​=Qs​
- 

Find equilibrium quantity $Q^*$Q∗
- 

Calculate:
- Maximum willingness to pay (price where $Q_d = 0$Qd​=0)
- Minimum acceptable price for producers (price where $Q_s = 0$Qs​=0)

**Part B: Inverse Functions for Integration (15 minutes)**
- 

Rearrange demand to get inverse demand: $P = D(Q)$P=D(Q)
- From $Q = 800 - 5P$Q=800−5P, solve for $P$P

- 

Rearrange supply to get inverse supply: $P = S(Q)$P=S(Q)
- From $Q = -200 + 3P$Q=−200+3P, solve for $P$P

- 

Verify your inverse functions:
- Substitute $Q^*$Q∗into $D(Q)$D(Q)— do you get $P^*$P∗?
- Substitute $Q^*$Q∗into $S(Q)$S(Q)— do you get $P^*$P∗?

**Part C: Calculating Surplus (25 minutes)**
- 

**Consumer Surplus**formula:$CS = \int_0^{Q^*} D(Q)\,dQ - P^* \cdot Q^* $CS=∫0Q∗​D(Q)dQ−P∗⋅Q∗

Explain: What does each term represent?
- The integral $\int_0^{Q^*} D(Q)\,dQ$∫0Q∗​D(Q)dQ= ?
- The rectangle $P^* \cdot Q^*$P∗⋅Q∗= ?
- The difference = ?

- 

Calculate Consumer Surplus:
- Evaluate the definite integral
- Subtract $P^* Q^*$P∗Q∗
- Express in dollars

- 

**Producer Surplus**formula:$PS = P^* \cdot Q^* - \int_0^{Q^*} S(Q)\,dQ $PS=P∗⋅Q∗−∫0Q∗​S(Q)dQ

Calculate Producer Surplus using integration.
- 

**Verification using geometry:**
- CS = $\frac{1}{2} \times Q^* \times (P_{max} - P^*)$21​×Q∗×(Pmax​−P∗)
- PS = $\frac{1}{2} \times Q^* \times (P^* - P_{min})$21​×Q∗×(P∗−Pmin​)
- Do your integration answers match?

- 

Calculate Total Welfare = CS + PS
- Who benefits more, consumers or producers?
- Express CS and PS as percentages of total welfare

**Part D: Policy Impact (5 minutes)**
- The Association proposes a minimum price of $P_{floor} = 140$Pfloor​=140(above equilibrium).
- At this price, how much do consumers demand? $Q_d(140) = ?$Qd​(140)=?
- At this price, how much do producers supply? $Q_s(140) = ?$Qs​(140)=?
- What problem arises?

---

### DELIVERABLES

- Worksheet with all integration steps
- Graph showing supply, demand, and shaded surplus areas
- **Group 4 (second presentation) in Week 8**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

# Quantity range
Q = np.linspace(0, 800, 500)

# Inverse demand and supply
P_demand = (800 - Q) / 5
P_supply = (Q + 200) / 3

# Equilibrium
Q_star = 500  # Solve Qd = Qs
P_star = 60   # Substitute back

# Plot
plt.figure(figsize=(10, 8))
plt.plot(Q, P_demand, linewidth=2, label='Demand P=D(Q)', color='blue')
plt.plot(Q, P_supply, linewidth=2, label='Supply P=S(Q)', color='red')

# Equilibrium point
plt.plot(Q_star, P_star, 'go', markersize=12, label=f'Equilibrium (Q*={Q_star}, P*=${P_star})')

# Consumer surplus (area above P*, below demand)
Q_cs = np.linspace(0, Q_star, 200)
P_cs = (800 - Q_cs) / 5
plt.fill_between(Q_cs, P_star, P_cs, alpha=0.3, color='blue', label='Consumer Surplus')

# Producer surplus (area below P*, above supply)
Q_ps = np.linspace(0, Q_star, 200)
P_ps = (Q_ps + 200) / 3
plt.fill_between(Q_ps, P_ps, P_star, alpha=0.3, color='red', label='Producer Surplus')

plt.xlabel('Quantity (thousands of bottles)')
plt.ylabel('Price ($/bottle)')
plt.title('Margaret River Wine Market: Consumer and Producer Surplus')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 800)
plt.ylim(0, 200)
plt.show()

```

---

## PROBLEM BRIEF: W7B (for Group 5 second presentation in Week 8)

**"Avocado Market: Export vs. Domestic Trade-offs"**

---

### SCENARIO

Australian avocado growers are debating whether to support expanded export access to Asia. Economists have modeled the domestic market:

**Demand (domestic):**$Q_d = 600 - 4P$Qd​=600−4P(quantity in tonnes per week, price in $/kg)
**Supply (domestic):**$Q_s = -120 + 2P$Qs​=−120+2P

Opening export markets would effectively increase demand, shifting the curve outward. Growers benefit from higher prices, but consumers face higher costs.

---

### YOUR TASK

**Part A: Current Domestic Equilibrium (15 minutes)**
- 

Solve for equilibrium price $P^*$P∗and quantity $Q^*$Q∗
- 

Find:
- Maximum consumer willingness to pay
- Minimum producer acceptable price

- 

Sketch a rough supply-demand diagram

**Part B: Surplus Under Current Policy (25 minutes)**
- 

Find inverse demand and supply functions:
- $P = D(Q)$P=D(Q)from $Q_d = 600 - 4P$Qd​=600−4P
- $P = S(Q)$P=S(Q)from $Q_s = -120 + 2P$Qs​=−120+2P

- 

Calculate**Consumer Surplus**:$CS = \int_0^{Q^*} D(Q)\,dQ - P^* Q^* $CS=∫0Q∗​D(Q)dQ−P∗Q∗
- Evaluate the integral $\int D(Q)\,dQ$∫D(Q)dQ
- Apply limits [0, $Q^*$Q∗]
- Subtract $P^* Q^*$P∗Q∗

- 

Calculate**Producer Surplus**:$PS = P^* Q^* - \int_0^{Q^*} S(Q)\,dQ $PS=P∗Q∗−∫0Q∗​S(Q)dQ
- 

Verify using triangle formulas:
- CS = $\frac{1}{2} Q^* (P_{max} - P^*)$21​Q∗(Pmax​−P∗)
- PS = $\frac{1}{2} Q^* (P^* - P_{min})$21​Q∗(P∗−Pmin​)

- 

Calculate Total Welfare and the ratio CS/PS

**Part C: Export Scenario (15 minutes)**
- 

With export access, demand shifts to $Q_d^{new} = 720 - 4P$Qdnew​=720−4P:
- Find new equilibrium price $P^{new}$Pnewand quantity $Q^{new}$Qnew
- How much has price increased?

- 

Calculate new Consumer Surplus and Producer Surplus:
- Use the same integration approach
- Compare to the baseline scenario

- 

Who wins and loses from export expansion?
- Change in CS = ?
- Change in PS = ?
- Change in Total Welfare = ?

**Part D: Equity Consideration (5 minutes)**
- 

Export policy creates:
- Losers: domestic consumers (pay higher prices)
- Winners: producers (receive higher prices)

Write a brief (3-4 sentence) policy recommendation considering:
- Economic efficiency (total welfare)
- Equity (distribution between groups)
- Whether compensation mechanisms could address distributional concerns

---

### DELIVERABLES

- Worksheet showing integration for both scenarios
- Comparative graph: domestic-only vs. export market
- **Group 5 (second presentation) in Week 8**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

Q = np.linspace(0, 600, 500)

# Domestic-only scenario
P_demand_dom = (600 - Q) / 4
P_supply = (Q + 120) / 2

# Export scenario
P_demand_export = (720 - Q) / 4

# Equilibria
Q_dom = 240  # Solve Qd = Qs
P_dom = 90

Q_export = 260  # Solve Qd_new = Qs
P_export = 115

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Left: Domestic-only
ax1.plot(Q, P_demand_dom, linewidth=2, label='Demand (domestic)', color='blue')
ax1.plot(Q, P_supply, linewidth=2, label='Supply', color='red')
ax1.plot(Q_dom, P_dom, 'go', markersize=10, label=f'Equilibrium (Q={Q_dom}, P=${P_dom})')

Q_range = np.linspace(0, Q_dom, 200)
P_d = (600 - Q_range) / 4
P_s = (Q_range + 120) / 2
ax1.fill_between(Q_range, P_dom, P_d, alpha=0.3, color='blue', label='CS')
ax1.fill_between(Q_range, P_s, P_dom, alpha=0.3, color='red', label='PS')

ax1.set_xlabel('Quantity (tonnes/week)')
ax1.set_ylabel('Price ($/kg)')
ax1.set_title('Domestic Market Only')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Right: Export scenario
ax2.plot(Q, P_demand_export, linewidth=2, label='Demand (with exports)', color='darkblue')
ax2.plot(Q, P_supply, linewidth=2, label='Supply', color='red')
ax2.plot(Q_export, P_export, 'mo', markersize=10, label=f'New Eq (Q={Q_export}, P=${P_export})')

Q_range2 = np.linspace(0, Q_export, 200)
P_d2 = (720 - Q_range2) / 4
P_s2 = (Q_range2 + 120) / 2
ax2.fill_between(Q_range2, P_export, P_d2, alpha=0.3, color='blue', label='CS (reduced)')
ax2.fill_between(Q_range2, P_s2, P_export, alpha=0.3, color='red', label='PS (increased)')

ax2.set_xlabel('Quantity (tonnes/week)')
ax2.set_ylabel('Price ($/kg)')
ax2.set_title('With Export Access')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

```

---

---

# Week 8: Lotka-Volterra and Predator-Prey Dynamics

---

## 📝**ALL GROUPS: Lab Activity**

**During this week's lab, ALL groups work on the following problem:**
### PROBLEM BRIEF: W8

**"Feral Cat Management: Protecting Native Wildlife"**

---

#### SCENARIO

The Western Shield program aims to protect endangered numbats from feral cats. Ecologists have developed a predator-prey model:$\begin{aligned} \frac{dN}{dt} &= 0.4N - 0.002NC \\ \frac{dC}{dt} &= -0.3C + 0.001NC \end{aligned}$dtdN​dtdC​​=0.4N−0.002NC=−0.3C+0.001NC​

where:
- $N$N= numbat population
- $C$C= feral cat population
- $t$t= time (years)

**Model interpretation:**
- Numbats grow at 40% per year without cats
- Each cat-numbat interaction reduces numbat growth
- Cats decline at 30% per year without prey
- Predation increases cat population

---

#### YOUR TASK

**Part A: Equilibrium Analysis (25 minutes)**
- 

Find the**trivial equilibrium**(both species extinct):
- Set $N = 0, C = 0$N=0,C=0

- 

Find the**coexistence equilibrium**:
- Set $\frac{dN}{dt} = 0$dtdN​=0: $N(0.4 - 0.002C) = 0$N(0.4−0.002C)=0
- Either $N = 0$N=0or $C = ?$C=?

- Set $\frac{dC}{dt} = 0$dtdC​=0: $C(-0.3 + 0.001N) = 0$C(−0.3+0.001N)=0
- Either $C = 0$C=0or $N = ?$N=?

- **Coexistence:**$(N^*, C^*) = (?, ?)$(N∗,C∗)=(?,?)

- 

Interpret: What does this equilibrium mean for wildlife management?

**Part B: Phase Plane Analysis (20 minutes)**
- 

**Nullclines**(curves where population growth = 0):
- Numbat nullcline: $\frac{dN}{dt} = 0$dtdN​=0→ $N = 0$N=0or $C = ?$C=?
- Cat nullcline: $\frac{dC}{dt} = 0$dtdC​=0→ $C = 0$C=0or $N = ?$N=?

- 

The phase plane is divided into four regions:

| Region | Condition | $\frac{dN}{dt}$ | d | t | d | N | ​ | $\frac{dC}{dt}$ | d | t | d | C | ​ | Movement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | $N | < | N^*, C | < | C^*$ | N | < | N | ∗ | , | C | < | C | ∗ | ? | ? | ? |
| II | $N > N^*, C | < | C^*$ | N | > | N | ∗ | , | C | < | C | ∗ | ? | ? | ? |
| III | $N > N^*, C > C^*$ | N | > | N | ∗ | , | C | > | C | ∗ | ? | ? | ? |
| IV | $N | < | N^*, C > C^*$ | N | < | N | ∗ | , | C | > | C | ∗ | ? | ? | ? |

Fill in the table.
- 

Sketch the phase portrait showing how populations move in each region.

**Part C: Management Interventions (15 minutes)**
- 

**Cat culling:**Remove 50 cats per year
- Modified equation: $\frac{dC}{dt} = -0.3C + 0.001NC - 50$dtdC​=−0.3C+0.001NC−50
- Find the new equilibrium
- How does numbat population change?

- 

**Numbat translocation:**Add 20 numbats per year
- Modified equation: $\frac{dN}{dt} = 0.4N - 0.002NC + 20$dtdN​=0.4N−0.002NC+20
- Find the new equilibrium
- Compare effectiveness to cat culling

- 

Which intervention better supports numbat conservation? Why?

---

#### DELIVERABLES

- Completed Group Worksheet with equilibrium analysis
- Phase plane diagram with nullclines and direction arrows
- **Groups 6 & 7:**Prepare 10-minute presentation for Week 9

---

#### PRESENTATION GUIDANCE (Groups 6 & 7)

Focus on:
- The Lotka-Volterra model structure
- Equilibrium concepts (trivial vs. coexistence)
- Phase plane analysis and population dynamics
- Management implications

---

#### HINTS / SCAFFOLDING

**To find equilibria, factor equations:**
- $N(0.4 - 0.002C) = 0$N(0.4−0.002C)=0means $N = 0$N=0OR $0.4 - 0.002C = 0$0.4−0.002C=0
- Solve the second equation for $C$C

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

# Equilibrium
N_star = 300
C_star = 200

# Nullclines
N_range = np.linspace(0, 600, 100)
C_range = np.linspace(0, 400, 100)

plt.figure(figsize=(10, 8))
plt.axhline(y=C_star, color='blue', linewidth=2, linestyle='--', label=f'Numbat nullcline (C={C_star})')
plt.axvline(x=N_star, color='red', linewidth=2, linestyle='--', label=f'Cat nullcline (N={N_star})')
plt.plot(N_star, C_star, 'go', markersize=15, label=f'Equilibrium ({N_star}, {C_star})')

# Direction field
N_grid = np.linspace(50, 550, 15)
C_grid = np.linspace(50, 350, 12)
N_mesh, C_mesh = np.meshgrid(N_grid, C_grid)

dN_dt = 0.4 * N_mesh - 0.002 * N_mesh * C_mesh
dC_dt = -0.3 * C_mesh + 0.001 * N_mesh * C_mesh

# Normalize arrows
magnitude = np.sqrt(dN_dt**2 + dC_dt**2)
dN_norm = dN_dt / (magnitude + 1e-10)
dC_norm = dC_dt / (magnitude + 1e-10)

plt.quiver(N_mesh, C_mesh, dN_norm, dC_norm, alpha=0.5)

plt.xlabel('Numbat Population (N)')
plt.ylabel('Feral Cat Population (C)')
plt.title('Predator-Prey Phase Plane')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 600)
plt.ylim(0, 400)
plt.show()

```

---

---

## 🎤**PRESENTATION PROBLEMS: For Groups Presenting Next Week**

**The following problems are for the two groups presenting next week. Work on your assigned variation during this week's lab to prepare your presentation.**
## PROBLEM BRIEF: W8A (for Group 6 second presentation in Week 9)

**"Feral Cat Control: Protecting Native Numbats"**

---

### SCENARIO

The Western Shield program aims to protect the endangered numbat (*Myrmecobius fasciatus*) from introduced predators, primarily feral cats. Ecologists have developed a simple predator-prey model:$\begin{aligned} \frac{dN}{dt} &= 0.4N - 0.002NC \\ \frac{dC}{dt} &= -0.3C + 0.001NC \end{aligned}$dtdN​dtdC​​=0.4N−0.002NC=−0.3C+0.001NC​

where:
- $N$N= numbat population (number of individuals)
- $C$C= feral cat population (number of individuals)
- $t$t= time in years

**Model interpretation:**
- Numbats grow at 40% per year without cats
- Each cat-numbat interaction reduces numbat growth
- Cats decline at 30% per year without prey
- Each cat-numbat interaction increases cat population (predation success)

---

### YOUR TASK

**Part A: Equilibrium Analysis (25 minutes)**
- 

Find the**trivial equilibrium**(extinction):
- Set $N = 0, C = 0$N=0,C=0
- Is this a stable outcome?

- 

Find the**coexistence equilibrium**:
- Set both $\frac{dN}{dt} = 0$dtdN​=0and $\frac{dC}{dt} = 0$dtdC​=0
- From $\frac{dN}{dt} = 0$dtdN​=0: $N(0.4 - 0.002C) = 0$N(0.4−0.002C)=0
- Either $N = 0$N=0(trivial) or $C = 200$C=200

- From $\frac{dC}{dt} = 0$dtdC​=0: $C(-0.3 + 0.001N) = 0$C(−0.3+0.001N)=0
- Either $C = 0$C=0or $N = 300$N=300

- **Coexistence equilibrium:**$(N^*, C^*) = (300, 200)$(N∗,C∗)=(300,200)

- 

Interpret the equilibrium:
- 300 numbats and 200 cats can coexist indefinitely
- If populations deviate, do they return to equilibrium or oscillate?

**Part B: Phase Plane Analysis (20 minutes)**
- 

**Nullclines**(curves where growth rate = 0):
- Numbat nullcline: where $\frac{dN}{dt} = 0$dtdN​=0
- Either $N = 0$N=0or $C = 200$C=200(horizontal line in phase plane)

- Cat nullcline: where $\frac{dC}{dt} = 0$dtdC​=0
- Either $C = 0$C=0or $N = 300$N=300(vertical line in phase plane)

- 

Divide the phase plane into four regions based on nullclines:

| Region | $N$ | N | vs. 300 | $C$ | C | vs. 200 | $\frac{dN}{dt}$ | d | t | d | N | ​ | $\frac{dC}{dt}$ | d | t | d | C | ​ | Movement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | $N | < | 300$ | N | < | 300 | $C | < | 200$ | C | < | 200 | + | − | $N$ | N | increases, $C$ | C | decreases |
| II | $N > 300$ | N | > | 300 | $C | < | 200$ | C | < | 200 | + | + | Both increase |
| III | $N > 300$ | N | > | 300 | $C > 200$ | C | > | 200 | − | + | $N$ | N | decreases, $C$ | C | increases |
| IV | $N | < | 300$ | N | < | 300 | $C > 200$ | C | > | 200 | − | − | Both decrease |

- 

Sketch arrows showing population movement in each region

**Part C: Management Interventions (15 minutes)**
- 

**Cat culling program:**Reduce cat population by 50 cats/year
- Modified equation: $\frac{dC}{dt} = -0.3C + 0.001NC - 50$dtdC​=−0.3C+0.001NC−50
- New cat nullcline: $-0.3C + 0.001NC - 50 = 0$−0.3C+0.001NC−50=0
- Solve for new equilibrium: $C(-0.3 + 0.001N) = 50$C(−0.3+0.001N)=50
- If $C = 200$C=200: $200(-0.3 + 0.001N) = 50$200(−0.3+0.001N)=50
- Solve for $N$N: new numbat equilibrium

- 

**Numbat translocation:**Add 20 numbats/year
- Modified equation: $\frac{dN}{dt} = 0.4N - 0.002NC + 20$dtdN​=0.4N−0.002NC+20
- Find new equilibrium

- 

Which intervention is more effective for numbat conservation?

---

### DELIVERABLES

- Completed worksheet with equilibrium calculations
- Phase plane diagram with nullclines and arrows
- **Group 6 (second presentation) in Week 9**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt

# Nullclines
N_range = np.linspace(0, 600, 100)
C_range = np.linspace(0, 400, 100)

# Cat nullcline: C=0 or N=300
C_nullcline_N = 300 * np.ones_like(C_range)

# Numbat nullcline: N=0 or C=200
N_nullcline_C = 200 * np.ones_like(N_range)

# Phase plane
plt.figure(figsize=(10, 8))
plt.axhline(y=200, color='blue', linewidth=2, linestyle='--', label='Numbat nullcline (C=200)')
plt.axvline(x=300, color='red', linewidth=2, linestyle='--', label='Cat nullcline (N=300)')
plt.plot(300, 200, 'go', markersize=15, label='Equilibrium (N*=300, C*=200)')

# Direction field (quiver plot)
N_grid = np.linspace(50, 550, 15)
C_grid = np.linspace(50, 350, 12)
N_mesh, C_mesh = np.meshgrid(N_grid, C_grid)

dN_dt = 0.4 * N_mesh - 0.002 * N_mesh * C_mesh
dC_dt = -0.3 * C_mesh + 0.001 * N_mesh * C_mesh

# Normalize for visualization
magnitude = np.sqrt(dN_dt**2 + dC_dt**2)
dN_dt_norm = dN_dt / (magnitude + 1e-10)
dC_dt_norm = dC_dt / (magnitude + 1e-10)

plt.quiver(N_mesh, C_mesh, dN_dt_norm, dC_dt_norm, alpha=0.5)

plt.xlabel('Numbat Population (N)')
plt.ylabel('Feral Cat Population (C)')
plt.title('Predator-Prey Phase Plane: Numbats vs. Feral Cats')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 600)
plt.ylim(0, 400)
plt.show()

```

---

## PROBLEM BRIEF: W8B (for Group 7 second presentation in Week 9)

**"Dingo Conservation: Managing Kangaroo Populations"**

---

### SCENARIO

In arid Australia, dingoes (*Canis dingo*) are apex predators that regulate kangaroo populations. Removal of dingoes often leads to kangaroo overabundance and rangeland degradation. Ecologists model this system:$\begin{aligned} \frac{dK}{dt} &= 0.5K - 0.0015KD \\ \frac{dD}{dt} &= -0.25D + 0.0008KD \end{aligned}$dtdK​dtdD​​=0.5K−0.0015KD=−0.25D+0.0008KD​

where:
- $K$K= kangaroo population (number of individuals)
- $D$D= dingo population (number of individuals)
- $t$t= time in years

**Model features:**
- Kangaroos grow at 50% per year without predation (high reproductive rate)
- Dingoes decline at 25% per year without prey
- Predation interactions affect both populations

---

### YOUR TASK

**Part A: Finding Equilibria (25 minutes)**
- 

Trivial equilibrium:
- $(K, D) = (0, 0)$(K,D)=(0,0)— both species extinct
- Is this realistic for arid Australia?

- 

Coexistence equilibrium:
- Set $\frac{dK}{dt} = 0$dtdK​=0: $K(0.5 - 0.0015D) = 0$K(0.5−0.0015D)=0
- Either $K = 0$K=0or $D = 333.33$D=333.33(round to 333)

- Set $\frac{dD}{dt} = 0$dtdD​=0: $D(-0.25 + 0.0008K) = 0$D(−0.25+0.0008K)=0
- Either $D = 0$D=0or $K = 312.5$K=312.5(round to 313)

- **Equilibrium:**$(K^*, D^*) = (313, 333)$(K∗,D∗)=(313,333)

- 

Stability consideration:
- Are populations close to equilibrium stable?
- Or do they cycle (oscillate)?
- In this model, small perturbations cause oscillations

**Part B: Nullclines and Phase Portrait (20 minutes)**
- 

Nullclines:
- Kangaroo nullcline: $K = 0$K=0or $D = 333$D=333
- Dingo nullcline: $D = 0$D=0or $K = 313$K=313

- 

Create a phase plane table:

| Region | $K$ | K | vs. 313 | $D$ | D | vs. 333 | $\frac{dK}{dt}$ | d | t | d | K | ​ | $\frac{dD}{dt}$ | d | t | d | D | ​ | Trajectory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | $K | < | 313$ | K | < | 313 | $D | < | 333$ | D | < | 333 | + | − | K increases, D decreases |
| II | $K > 313$ | K | > | 313 | $D | < | 333$ | D | < | 333 | + | + | Both increase |
| III | $K > 313$ | K | > | 313 | $D > 333$ | D | > | 333 | − | + | K decreases, D increases |
| IV | $K | < | 313$ | K | < | 313 | $D > 333$ | D | > | 333 | − | − | Both decrease |

- 

Sketch the cyclic behavior:
- Trajectories spiral around the equilibrium
- High kangaroos → dingoes increase → kangaroos decline → dingoes decline → cycle repeats

**Part C: Management Scenarios (15 minutes)**
- 

**Dingo culling:**Pastoralists remove 40 dingoes/year to protect livestock
- New equation: $\frac{dD}{dt} = -0.25D + 0.0008KD - 40$dtdD​=−0.25D+0.0008KD−40
- Find new equilibrium: $-0.25D + 0.0008KD - 40 = 0$−0.25D+0.0008KD−40=0
- If $D = 333$D=333: $-0.25(333) + 0.0008K(333) - 40 = 0$−0.25(333)+0.0008K(333)−40=0
- Solve for new $K$Kequilibrium

- 

**Effect of culling:**
- How much does kangaroo equilibrium increase?
- What are the consequences for rangeland health?

- 

**Alternative: Dingo protection**
- No culling: equilibrium remains at $(313, 333)$(313,333)
- Lower kangaroo numbers reduce grazing pressure
- Write a brief (3-4 sentence) recommendation on dingo management for sustainable rangeland use

---

### DELIVERABLES

- Completed worksheet with equilibria and nullclines
- Phase portrait showing cyclic trajectories
- **Group 7 (second presentation) in Week 9**

---

### PYTHON TEMPLATE

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the system
def predator_prey(state, t):
    K, D = state
    dK_dt = 0.5 * K - 0.0015 * K * D
    dD_dt = -0.25 * D + 0.0008 * K * D
    return [dK_dt, dD_dt]

# Equilibrium
K_star, D_star = 313, 333

# Phase plane
K_range = np.linspace(50, 600, 15)
D_range = np.linspace(50, 600, 15)
K_mesh, D_mesh = np.meshgrid(K_range, D_range)

dK_dt = 0.5 * K_mesh - 0.0015 * K_mesh * D_mesh
dD_dt = -0.25 * D_mesh + 0.0008 * K_mesh * D_mesh

# Normalize
magnitude = np.sqrt(dK_dt**2 + dD_dt**2)
dK_norm = dK_dt / (magnitude + 1e-10)
dD_norm = dD_dt / (magnitude + 1e-10)

plt.figure(figsize=(10, 8))

# Nullclines
plt.axhline(y=333, color='blue', linewidth=2, linestyle='--', label='Kangaroo nullcline (D=333)')
plt.axvline(x=313, color='red', linewidth=2, linestyle='--', label='Dingo nullcline (K=313)')
plt.plot(K_star, D_star, 'go', markersize=15, label=f'Equilibrium ({K_star}, {D_star})')

# Vector field
plt.quiver(K_mesh, D_mesh, dK_norm, dD_norm, alpha=0.5)

# Add a trajectory
t = np.linspace(0, 50, 1000)
initial_state = [350, 250]
trajectory = odeint(predator_prey, initial_state, t)
plt.plot(trajectory[:, 0], trajectory[:, 1], 'purple', linewidth=1.5, label='Sample trajectory')

plt.xlabel('Kangaroo Population (K)')
plt.ylabel('Dingo Population (D)')
plt.title('Predator-Prey Dynamics: Kangaroos and Dingoes')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 650)
plt.ylim(0, 650)
plt.show()

```

---

---

## Week 9: Probability and Bayes' Theorem

### PROBLEM BRIEF: W9

**"COVID-19 Testing: Understanding False Positives"**

---

#### SCENARIO

Western Australia is managing a COVID-19 outbreak. Health authorities are using rapid antigen tests (RATs) for community screening. Understanding test accuracy is critical for policy decisions.

**Test characteristics:**
- **Sensitivity:**85% (if you have COVID, test is positive 85% of the time)
- **Specificity:**95% (if you don't have COVID, test is negative 95% of the time)

**Population prevalence:**2% of the tested population actually has COVID.

A person tests**positive**. What's the probability they actually have COVID?

---

#### YOUR TASK

**Part A: Understanding Conditional Probability (15 minutes)**
- 

Define the events:
- $D$D= person has COVID
- $T^+$T+= test is positive

- 

Write out the given probabilities:
- $P(T^+ | D)$P(T+∣D)= sensitivity = ?
- $P(T^- | D^c)$P(T−∣Dc)= specificity = ?
- $P(D)$P(D)= prevalence = ?

- 

Calculate the complementary probabilities:
- $P(T^- | D)$P(T−∣D)= false negative rate = ?
- $P(T^+ | D^c)$P(T+∣Dc)= false positive rate = ?
- $P(D^c)$P(Dc)= probability of not having COVID = ?

**Part B: Applying Bayes' Theorem (25 minutes)**
- 

We want to find $P(D | T^+)$P(D∣T+): the probability of having COVID given a positive test.

**Bayes' Theorem:**$P(D | T^+) = \frac{P(T^+ | D) \cdot P(D)}{P(T^+)} $P(D∣T+)=P(T+)P(T+∣D)⋅P(D)​
- 

Calculate the**total probability**of testing positive:$P(T^+) = P(T^+ | D) \cdot P(D) + P(T^+ | D^c) \cdot P(D^c) $P(T+)=P(T+∣D)⋅P(D)+P(T+∣Dc)⋅P(Dc)

Substitute the values and calculate.
- 

Now calculate $P(D | T^+)$P(D∣T+)using Bayes' theorem.
- 

**Interpret:**If someone tests positive, what's the chance they actually have COVID? Is it higher or lower than you expected?

**Part C: Sensitivity Analysis (15 minutes)**
- 

How does prevalence affect the positive predictive value?
- Recalculate $P(D | T^+)$P(D∣T+)if prevalence increases to 10%
- Recalculate if prevalence is only 0.5%
- What pattern do you observe?

- 

Create a table:

| Prevalence $P(D)$ | P | ( | D | ) | $P(D | T^+)$ | P | ( | D | ∣ | T | + | ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.5% | ? |
| 2% | ? |
| 5% | ? |
| 10% | ? |
| 20% | ? |

**Part D: Policy Implications (5 minutes)**
- 

The government is deciding between two testing strategies:
- **Strategy A:**Test everyone (current 2% prevalence)
- **Strategy B:**Only test people with symptoms (estimated 15% prevalence among symptomatic)

Which strategy gives more reliable positive results? Why?
- 

Write a brief (3-4 sentence) recommendation about when rapid tests are most useful and when they should be confirmed with PCR tests.

---

#### DELIVERABLES

- Completed Group Worksheet with Bayes' theorem calculations
- Graph showing $P(D | T^+)$P(D∣T+)vs. prevalence

---

#### HINTS / SCAFFOLDING

**Bayes' Theorem intuition:**
- Prior probability: $P(D)$P(D)= what we know before the test
- Likelihood: $P(T^+ | D)$P(T+∣D)= how good the test is
- Posterior probability: $P(D | T^+)$P(D∣T+)= what we know after the test

**Tree diagram approach:**
```python
Population (1000 people)
├─ Have COVID: 20 (2%)
│  ├─ Test positive: 17 (85% of 20)
│  └─ Test negative: 3
└─ No COVID: 980 (98%)
   ├─ Test positive: 49 (5% of 980)
   └─ Test negative: 931

Total positive tests: 17 + 49 = 66
Actually have COVID among positives: 17
P(D|T+) = 17/66 ≈ 0.26 = 26%

```

**Python template:**
```python
import numpy as np
import matplotlib.pyplot as plt

# Sensitivity and specificity (fixed)
sensitivity = 0.85
specificity = 0.95
false_positive_rate = 1 - specificity

# Range of prevalence values
prevalence = np.linspace(0.001, 0.3, 100)

# Calculate P(D|T+) for each prevalence
PPV = (sensitivity * prevalence) / (sensitivity * prevalence + false_positive_rate * (1 - prevalence))

plt.figure(figsize=(10, 6))
plt.plot(prevalence * 100, PPV * 100, linewidth=2)
plt.xlabel('Prevalence (%)')
plt.ylabel('Positive Predictive Value (%)')
plt.title('How Prevalence Affects Test Reliability')
plt.grid(True, alpha=0.3)
plt.axhline(y=50, color='r', linestyle='--', alpha=0.5, label='50% threshold')
plt.legend()
plt.show()

```

---

---

## Week 10: Hypothesis Testing (Mock Exam Workshop)

### ACTIVITY: W10

**Mock Exam: Part II Practice**

---

#### FORMAT

This week replaces the standard Problem Brief with a**Mock Exam Workshop**. You'll practice Part II exam-style questions under timed conditions.

**Structure:**
- 0:00–0:15: Demonstrator reviews exam format and expectations
- 0:15–1:30: Groups work on mock exam questions (75 minutes)
- 1:30–2:00: Groups whiteboard solutions; class discussion

---

#### MOCK EXAM QUESTIONS

Work through these four questions. They represent the style and difficulty of the actual exam Part II.

**Question 1: Hypothesis Testing (12 marks)**

A pharmaceutical company claims their new painkiller reduces headache duration by at least 30% compared to standard treatment. A clinical trial with 50 patients shows:
- Mean reduction: 28%
- Standard deviation: 8%

a) State the null and alternative hypotheses (2 marks)

b) Calculate the test statistic (4 marks)

c) At significance level $\alpha = 0.05$α=0.05, should the company's claim be rejected? (4 marks)

d) What does your conclusion mean for patients? (2 marks)

---

**Question 2: Optimization in Context (12 marks)**

A dairy farm produces milk at a cost of $C(x) = 2x^2 - 80x + 1200$C(x)=2x2−80x+1200dollars, where $x$xis thousands of liters produced per week. Milk sells for $1.20 per liter.

a) Write the profit function $P(x)$P(x)(3 marks)

b) Find the production level that maximizes profit (5 marks)

c) What is the maximum weekly profit? (2 marks)

d) If fuel costs increase and the cost function becomes $C(x) = 2x^2 - 80x + 1500$C(x)=2x2−80x+1500, how does optimal production change? (2 marks)

---

**Question 3: Integration Application (12 marks)**

A solar panel's power output (in watts) varies throughout the day according to:$P(t) = 500\sin\left(\frac{\pi t}{12}\right) $P(t)=500sin(12πt​)

where $t$tis hours after sunrise (0 ≤ t ≤ 12).

a) What is the peak power output and when does it occur? (3 marks)

b) Calculate the total energy produced during the day (energy = integral of power):$E = \int_0^{12} P(t)\,dt $E=∫012​P(t)dt

(6 marks)

c) Express your answer in kilowatt-hours (kWh) (1 kWh = 1000 watt-hours) (2 marks)

d) At $0.30 per kWh, what is the daily revenue from this panel? (1 mark)

---

**Question 4: Differential Equations (12 marks)**

A water tank drains according to the differential equation:$\frac{dV}{dt} = -0.5\sqrt{V} $dtdV​=−0.5V​

where $V$Vis volume (liters) and $t$tis time (minutes). Initially, $V(0) = 100$V(0)=100liters.

a) Separate variables and integrate to find $V(t)$V(t)(6 marks)

b) How long until the tank is half empty? (3 marks)

c) How long until the tank is completely empty? (2 marks)

d) Sketch $V(t)$V(t)vs. $t$t(1 mark)

---

#### DELIVERABLES

- Special Worksheet (Type B — Week 10 format, provided by instructor): group solutions to all four questions
- Whiteboard presentation of one assigned question

---

#### DEMONSTRATOR NOTES

- Assign each group one question to present on the whiteboard
- Circulate during work time; provide hints but don't solve
- During presentations, focus on:
- Problem formulation (did they set it up correctly?)
- Method selection (right technique for the question?)
- Calculation accuracy
- Interpretation of results

---

---

## Week 11: Trigonometry (Peer Review Exchange)

### ACTIVITY: W11

**Peer Problem Creation and Review**

---

#### FORMAT

This week, groups create their own trigonometry problems for each other, then solve the problems they receive.

**Structure:**
- 0:00–0:15: Demonstrator reviews trigonometric functions and problem requirements
- 0:15–0:45: Groups create a problem (30 minutes)
- 0:45–0:50: Problems are exchanged (Group 1 ↔ Group 4, Group 2 ↔ Group 5, etc.)
- 0:50–1:40: Groups solve the received problem (50 minutes)
- 1:40–2:00: Present solutions; creators verify correctness

---

#### PROBLEM CREATION GUIDELINES

**Your group must create a problem involving a periodic phenomenon modeled by:**$f(t) = A\cos(B(t + C)) + D $f(t)=Acos(B(t+C))+D

or$f(t) = A\sin(B(t + C)) + D $f(t)=Asin(B(t+C))+D

**Required elements:**
- **Real-world context**(temperature, tides, daylight hours, seasonal sales, heart rate, etc.)
- **Four parameters determinable from data:**
- $A$A= amplitude
- $B$B= frequency (related to period $P = 2\pi/B$P=2π/B)
- $C$C= phase shift
- $D$D= vertical shift (midline)

- **At least two questions:**
- One asking for a value at a specific time
- One asking when the function reaches a specific value

- **Include enough data for the receiving group to determine all parameters**

**Example:**

*"The average daily temperature in Perth varies seasonally. The maximum average temperature of 32°C occurs on January 15 (day 15), and the minimum of 18°C occurs on July 15 (day 196). Model temperature as a function of day of the year."*

Questions: a) Find $A$A, $B$B, $C$C, and $D$Db) What is the predicted temperature on April 10 (day 100)? c) On what days of the year is the temperature 25°C?

---

#### ASSESSMENT

This week counts as a**double worksheet**:
- **Part 1 (50%):**Quality of the problem you create (12.5 marks)
- **Part 2 (50%):**Solving the problem you receive (12.5 marks)

**Problem creation rubric:**

| Criterion | Excellent (5) | Good (3-4) | Developing (1-2) |
| --- | --- | --- | --- |
| Context | Engaging, realistic | Reasonable | Weak/implausible |
| Mathematical soundness | All parameters determinable; no ambiguity | Minor issues | Unsolvable as written |
| Difficulty | Comparable to examples | Slightly off | Way too easy/hard |
| Questions | Clear, test understanding | Formulaic | Vague or only computational |

---

#### DELIVERABLES

- Problem created by your group (submitted separately)
- Solution to the problem you received
- Solution key for your created problem (for demonstrator)

---

---

## Week 12: Linear Programming (Gallery Walk Capstone)

### PROBLEM BRIEF: W12

**"Sustainable Campus Dining: Optimizing the Guild Menu"**

---

#### SCENARIO

The UWA Student Guild is redesigning its food court menu to meet sustainability and nutrition goals. They want to offer a weekly meal plan that balances cost, nutrition, and environmental impact.

**Two main meal types:**
- **Plant-based meals**(e.g., lentil curry, veggie stir-fry)
- **Chicken-based meals**(e.g., grilled chicken, chicken sandwich)

**Nutritional and environmental data per serving:**

| Nutrient/Impact | Plant-based | Chicken | Weekly Target |
| --- | --- | --- | --- |
| Protein (g) | 18 | 30 | ≥ 350 g |
| Calories (kcal) | 220 | 280 | ≥ 3500 kcal |
| Iron (mg) | 3 | 1 | ≥ 25 mg |
| Carbon footprint (kg CO₂) | 0.5 | 2.5 | ≤ 20 kg |

**Costs:**
- Plant-based: $2.50 per serving
- Chicken: $4.00 per serving

**Goal:**Minimize cost while meeting all nutritional targets and staying within the carbon budget.

---

#### YOUR TASK

**Part A: Problem Formulation (15 minutes)**
- 

Define decision variables:
- Let $x$x= number of plant-based serves per week
- Let $y$y= number of chicken serves per week

- 

Write the**objective function**(what are we minimizing?):$\text{Minimize } Z = 2.5x + 4y $MinimizeZ=2.5x+4y
- 

Write the**constraint inequalities:**
- Protein constraint: $18x + 30y \geq 350$18x+30y≥350
- Calories constraint: $220x + 280y \geq 3500$220x+280y≥3500
- Iron constraint: $3x + y \geq 25$3x+y≥25
- Carbon constraint: $0.5x + 2.5y \leq 20$0.5x+2.5y≤20
- Non-negativity: $x \geq 0, y \geq 0$x≥0,y≥0

**Part B: Graphical Solution (25 minutes)**
- 

Convert each constraint to an equation and find the boundary line:
- Protein: $18x + 30y = 350$18x+30y=350
- When $x = 0$x=0: $y = ?$y=?
- When $y = 0$y=0: $x = ?$x=?

- Repeat for other constraints

- 

Graph all constraints on the same axes. Shade the**feasible region**(the set of points satisfying ALL constraints).
- 

Identify all**corner points**(vertices) of the feasible region by solving pairs of boundary equations simultaneously.
- 

**Corner Point Theorem:**The optimal solution occurs at a vertex. Evaluate $Z$Zat each corner point:

| Corner Point $(x, y)$ | ( | x | , | y | ) | Cost $Z = 2.5x + 4y$ | Z | = | 2.5 | x | + | 4 | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |
|  |
|  |

- 

Which corner point gives the minimum cost? This is your optimal solution.

**Part C: Interpretation and Sensitivity (15 minutes)**
- 

State the optimal menu:
- Number of plant-based serves: ...
- Number of chicken serves: ...
- Weekly cost per student: ...
- Check: Does this satisfy all constraints?

- 

**Sensitivity analysis:**The sustainability committee wants to tighten the carbon constraint to 15 kg CO₂.
- How does this change the feasible region?
- Find the new optimal solution.
- How much does cost increase?

- 

Write a brief recommendation for the Guild (3–4 sentences).

---

#### DELIVERABLES

- Completed Group Worksheet with graph
- Prepared "station" explanation for Gallery Walk

---

#### GALLERY WALK FORMAT

| Time | Activity |
| --- | --- |
| 0:00–0:15 | Demonstrator reviews LP formulation |
| 0:15–1:00 | Groups work on Problem Brief |
| 1:00–1:10 | Groups set up "stations" (poster/whiteboard with solution) |
| 1:10–1:50 | Gallery Walk: groups rotate every 8 minutes, explaining solutions |
| 1:50–2:00 | Debrief: Compare approaches |

**Gallery Walk rules:**
- 2 group members stay at station to present
- Other members visit other stations
- Visitors ask questions, compare approaches
- After each rotation, presenters and visitors swap

---

#### HINTS / SCAFFOLDING

**Graphing tips:**
- For $\geq$≥constraints, shade AWAY from origin
- For $\leq$≤constraints, shade TOWARD origin
- Feasible region = intersection of all shaded regions

**Finding intersections:**To find where protein and carbon constraints intersect:
- Protein: $18x + 30y = 350$18x+30y=350
- Carbon: $0.5x + 2.5y = 20$0.5x+2.5y=20

Solve simultaneously (substitution or elimination).

**Quick check:**A feasible solution must satisfy ALL constraints. Always verify your corner points.

**Python for graphing (optional):**
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 50, 100)

# Constraint boundaries (solve for y)
y_protein = (350 - 18*x) / 30
y_calories = (3500 - 220*x) / 280
y_iron = (25 - 3*x) / 1
y_carbon = (20 - 0.5*x) / 2.5

plt.plot(x, y_protein, label='Protein')
plt.plot(x, y_calories, label='Calories')
plt.plot(x, y_iron, label='Iron')
plt.plot(x, y_carbon, label='Carbon')
plt.xlim(0, 50)
plt.ylim(0, 25)
plt.xlabel('Plant-based serves (x)')
plt.ylabel('Chicken serves (y)')
plt.legend()
plt.show()

```

---

---

# 5. Group Worksheets

Each week you complete one group worksheet and submit it via LMS before the due date shown in the Unit Outline.

**There are two worksheet types depending on the week. Your instructor will provide (possibly modified) versions of these worksheets for you to fill out.**

---

## Type A — Standard Group Worksheet (Weeks 2–9)

Used in the eight core lab weeks. Structured in six sections with a peer contribution review appended.************************

| Section | Weight | What you do |
| --- | --- | --- |
| 1 — Problem Formulation | 20% | Describe the real-world problem; identify variables, parameters, and appropriate model |
| 2 — Mathematical Setup | 20% | Write key equations/functions; show initial calculations or setup |
| 3 — Solution / Implementation | 30% | Step-by-step working; Python code attached as appendix if used |
| 4 — Results | 15% | Key findings; graphs/visualisations (paste or attach) |
| 5 — Interpretation | 10% | What do results mean for decision-makers? Limitations and assumptions? |
| 6 — AI Tool Usage Declaration | 5% | Declare and describe any AI tool use; attach screenshots/transcripts |

An**Appendix**(Python code, extra graphs, AI transcripts, extended calculations) may be attached.

**Grading:**The worksheet receives a**group mark**. Your**individual mark**is then adjusted by your**peer-reviewed contribution score**— see Section 2.4. The peer contribution form (Section 7 of the worksheet) is completed individually and submitted alongside the group worksheet.

---

## Type B — Special Structured Worksheets (Weeks 1, 10, 11, 12)

These weeks use purpose-built worksheets that replace the standard six-section format. Each is tailored to the week's activity and has its own internal structure, timing guides, and answer spaces.****************

| Week | Activity type | Worksheet structure |
| --- | --- | --- |
| Week 1 | Function identification & Australian policy application | Parts A (function identification), B (domain & range), C (policy calculations) + Reflection & AI Declaration |
| Week 10 | Mock exam workshop (hypothesis testing) | Parts A (expected value warm-up), B (setting up the test), C (computing p-value), D (interpretation) + Whiteboard notes |
| Week 11 | Peer problem creation & exchange | Part 1 (solve the given problem), Part 2 (create a problem for another group), Part 3 (solve the problem received) |
| Week 12 | Linear programming gallery walk capstone | Parts A (problem formulation), B (graphical solution), C (interpretation & sensitivity) + Gallery walk station preparation |

**Note:**Type B worksheets include a**Reflection & AI Usage Declaration**section but*do not*include the peer contribution review form — peer review applies to Type A weeks only.

---

*Instructor note: Instructors will provide (possibly modified) versions of both worksheet types on LMS each week. Check the relevant week tab and the LMS announcement for the specific file to download.*

---

# 6. Presentation Rubric

Your group presentation will be graded out of 20 marks (scaled to 4% of your unit grade).

**Important:**This rubric determines your**group mark**. Your**individual mark**will be calculated by multiplying the group mark by your**peer-reviewed contribution score**(see Section 2.4).

*Example: If your group receives 16/20 (80%) and your contribution score is 90%, your individual mark is 80 × 0.90 = 72%.*********************

| Criterion | Excellent (5) | Good (3-4) | Developing (1-2) | Poor (0) |
| --- | --- | --- | --- | --- |
| Problem Context (5 marks) | Clear explanation of real-world problem; audience understands why it matters | Problem explained but lacks context or motivation | Problem stated but unclear why it's important | No clear problem statement |
| Mathematical Approach (5 marks) | Correct model/method selected; clear justification for choice; formula presented clearly | Correct approach with minor errors; justification present but weak | Approach has errors or is poorly justified | Wrong method or no mathematical content |
| Results & Visualization (5 marks) | Results clearly presented with effective graphs/equations; calculations correct | Results mostly correct; visualization adequate | Results unclear or visualization ineffective | Major errors or no results shown |
| Interpretation & Implications (3 marks) | Clear connection to real-world decision; discusses limitations and trade-offs | Some interpretation but lacks depth | Minimal interpretation; just states numbers | No interpretation of results |
| Delivery & Timing (2 marks) | All members participate; well-practiced; within 10-minute limit | Most members participate; slightly over/under time | Uneven participation; timing issues | One person dominates; major timing problems |

**Total: ____ / 20 marks**

---

# 7. Tips for Success

## 7.1 During Lab Sessions

**Do:**
- Arrive on time with materials ready
- Contribute actively to your group
- Ask questions when you're stuck
- Try the mathematical formulation before coding
- Verify your answers make sense in context

**Don't:**
- Let one person do all the work
- Copy from other groups without understanding
- Rely entirely on AI tools
- Skip the interpretation step
- Leave before the wrap-up

## 7.2 For Presentations

**Do:**
- Divide roles fairly (everyone speaks)
- Practice timing beforehand
- Focus on the "so what?"
- Use visuals effectively
- Anticipate questions

**Don't:**
- Show raw Python code
- Read slides word-for-word
- Go over the 10-minute limit
- Assume the audience remembers details
- Present without rehearsing

## 7.3 Problem-Solving Strategy

- **Read carefully**– What is the question really asking?
- **Identify knowns and unknowns**– What information do you have?
- **Choose a method**– What technique from lectures applies?
- **Set up mathematically**– Write equations before coding
- **Solve/compute**– Do the math (by hand or Python)
- **Check reasonableness**– Does your answer make sense?
- **Interpret**– What does this mean in the real world?

## 7.4 Common Pitfalls

| Pitfall | How to Avoid |
| --- | --- |
| Starting with code before understanding the problem | Always formulate mathematically first |
| Not checking units | Track units through every calculation |
| Ignoring domain/range restrictions | Ask: "What values make sense here?" |
| Over-relying on AI | Use AI to check/debug, not to think for you |
| Skipping the "so what?" | Always connect math back to the scenario |

## 7.5 Using AI Responsibly

**Good AI use:**
- "Why is my Python giving a syntax error on line 12?"
- "How do I plot two functions on the same axes in matplotlib?"
- "Check my derivative: is $\frac{d}{dx}[x^2 e^x] = 2xe^x + x^2e^x$dxd​[x2ex]=2xex+x2ex?"

**Bad AI use:**
- [Pasting entire Problem Brief] "Solve this for me"
- Using AI-generated code you don't understand
- Not documenting AI usage in your worksheet

## 7.6 Study Habits

**Weekly:**
- Review lecture notes before lab
- Complete the Problem Brief during lab time
- Review the presentation if you're in the audience
- Attempt practice problems from the textbook

**Before Exams:**
- Rework all Problem Briefs from scratch
- Practice Part II exam questions under timed conditions
- Focus on interpretation, not just calculation
- Review presentation feedback for common errors

## 7.7 Getting Help

**During labs:**
- Ask your demonstrator
- Discuss with your group
- Use the AI tutor in the course app

**Outside labs:**
- Unit Coordinator office hours
- STUDYSmarter drop-in sessions
- Discussion board on LMS
- Peer study groups

---

# Quick Reference: Semester Schedule

| Week | Topic | Lab Activity | Presenting Groups |
| --- | --- | --- | --- |
| 0 | Mathematical Foundations | Python basics, Schaefer model | – |
| 1 | Functions | Plastic production analysis | – |
| 2 | Exponential & Logarithmic | Growth and decay models | – |
| 3 | Logistic & Schaefer | Fishery management | 1, 2 |
| 4 | Limits & Derivatives | Chemical optimization | 3, 4 |
| 5 | Optimization | Wildlife corridor design | 5, 6 |
| 6 | Integration | Carbon sequestration | 7, 1 |
| 7 | Definite Integrals & Surplus | Market welfare analysis | 2, 3 |
| 8 | Lotka-Volterra | Predator-prey dynamics | 4, 5 |
| 9 | Probability & Bayes | COVID testing | 6, 7 |
| 10 | Hypothesis Testing | Mock Exam Workshop | All (no presentations) |
| 11 | Trigonometry | Peer Review Exchange | All (no presentations) |
| 12 | Linear Programming | Gallery Walk | All (no presentations) |

---

---

*Good luck with your labs! Remember: the goal isn't just to get the right answer—it's to learn how analytical scientists think, formulate, and communicate.*

---

**Document Version:**2.0 (Combined with Variations)**Last Updated:**Semester 1, 2026

---

*End of Lab Handbook*