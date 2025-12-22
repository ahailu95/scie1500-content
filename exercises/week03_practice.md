# Week 3 Practice Problems
## Linear Relationships and Graphing

### Instructions
Show all calculations. Create graphs using Python where indicated.

---

## Section A: Linear Equations (5 marks each)

### Question 1
Find the equation of the line passing through the following points:

a) (2, 5) and (6, 13)
b) (-1, 7) and (3, -1)
c) (0, 4) and (5, 4)

---

### Question 2
For the equation y = 2.5x + 3:

a) What is the slope?
b) What is the y-intercept?
c) What is the value of y when x = 4?
d) What is the value of x when y = 15.5?

---

## Section B: Data Analysis (10 marks each)

### Question 3
The following data shows the relationship between temperature and the rate of a chemical reaction:

| Temperature (°C) | Reaction Rate (mol/L/min) |
|-----------------|--------------------------|
| 10 | 0.045 |
| 20 | 0.092 |
| 30 | 0.138 |
| 40 | 0.187 |
| 50 | 0.231 |

a) Plot this data as a scatter plot (use Python)
b) Calculate the best-fit line equation
c) Calculate R²
d) Predict the reaction rate at 35°C

---

### Question 4
A student measured enzyme activity at different substrate concentrations. The data shows:

Slope = 25.3 μmol/min per mM
Intercept = 2.1 μmol/min
R² = 0.987

a) Write the equation relating activity to concentration
b) Interpret the meaning of the slope in scientific terms
c) Interpret the meaning of the intercept
d) Is this a good fit? Justify your answer.

---

## Section C: Graphing Standards (15 marks each)

### Question 5
Identify ALL the errors in the following graph description:

> "The graph is titled 'Temp vs Time'. The x-axis shows temperature from 0-100, and the y-axis shows time from 0-60. Data points are connected with lines. There are no error bars. The legend says 'data'."

List at least 5 improvements needed to make this a publication-quality figure.

---

### Question 6
Using Python, create a publication-quality figure for the following data:

Experiment: Effect of pH on enzyme activity

| pH | Activity (U/mg) | Error (±) |
|----|-----------------|-----------|
| 4.0 | 12.3 | 1.2 |
| 5.0 | 28.7 | 2.1 |
| 6.0 | 45.2 | 2.8 |
| 7.0 | 62.1 | 3.2 |
| 8.0 | 48.9 | 2.5 |
| 9.0 | 25.4 | 1.8 |

Note: This is NOT a linear relationship - just create the scatter plot with error bars and appropriate formatting.

---

### Question 7
The growth of a bacterial population was measured over time:

| Time (hours) | Population (×10⁶) |
|--------------|-------------------|
| 0 | 1.0 |
| 2 | 2.1 |
| 4 | 4.3 |
| 6 | 8.5 |
| 8 | 16.8 |

a) Plot this data
b) Does it appear linear?
c) If not linear, what type of relationship might it be?
d) Suggest a transformation that might linearize this data

---

## Answer Key

1a) y = 2x + 1
1b) y = -2x + 5
1c) y = 4 (horizontal line)

2a) Slope = 2.5
2b) y-intercept = 3
2c) y = 13
2d) x = 5

3b) Rate = 0.00465 × Temp + 0.0005 (approximately)
3c) R² ≈ 0.998
3d) Rate at 35°C ≈ 0.163 mol/L/min

5) Improvements needed:
- Independent variable on x-axis (time vs temp switched)
- Axis labels need units
- More descriptive title needed
- Should use scatter points, not connected lines
- Error bars should be included if uncertainty is known
- Legend should be descriptive
- Grid lines would help readability

7b) Not linear - appears exponential
7c) Exponential growth
7d) Plot log(population) vs time to linearize

---

*Need help? Ask the AI tutor in the SciQuant app!*
