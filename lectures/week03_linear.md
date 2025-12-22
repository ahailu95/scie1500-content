# Week 3: Linear Relationships and Graphing

## SCIE1500 - Analytical Methods for Scientists
### Semester 1, 2026

---

## Learning Objectives

By the end of this week, you will be able to:
1. Identify linear relationships in data
2. Create publication-quality graphs
3. Calculate slope and intercept
4. Interpret linear equations in scientific contexts

---

## 1. The Linear Equation

A linear relationship has the form:

$$y = mx + c$$

Where:
- **m** = slope (gradient) = rise/run = Δy/Δx
- **c** = y-intercept (value of y when x = 0)

---

## 2. Calculating Slope

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

### Interpreting Slope
- **Positive slope**: y increases as x increases
- **Negative slope**: y decreases as x increases
- **Zero slope**: y doesn't change (horizontal line)
- **Undefined slope**: vertical line

---

## 3. Scientific Graphing Rules

### Essential Elements
1. **Title**: Descriptive, includes variables
2. **Axis labels**: Variable name AND units
3. **Scale**: Appropriate range, clear intervals
4. **Data points**: Clearly visible markers
5. **Best-fit line**: If appropriate
6. **Error bars**: When uncertainty is known

### Example Axis Label
✅ "Temperature (°C)"
❌ "Temp"

---

## 4. Creating Graphs in Python

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
time = np.array([0, 1, 2, 3, 4, 5])
distance = np.array([0, 2.1, 3.9, 6.2, 7.8, 10.1])

# Create plot
plt.figure(figsize=(8, 6))
plt.scatter(time, distance, color='blue', label='Data')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Distance vs Time for Falling Object')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 5. Best-Fit Lines

The **least squares method** finds the line that minimizes the sum of squared residuals.

```python
from scipy import stats

# Calculate best-fit line
slope, intercept, r_value, p_value, std_err = stats.linregress(time, distance)

print(f"Slope: {slope:.2f} m/s")
print(f"Intercept: {intercept:.2f} m")
print(f"R-squared: {r_value**2:.4f}")
```

---

## 6. R-squared (R²)

**R²** tells us how well the line fits the data:
- R² = 1.00: Perfect fit
- R² > 0.90: Excellent fit
- R² > 0.70: Good fit
- R² < 0.50: Poor fit

---

## Discipline Examples

### Biology: Enzyme Kinetics
Plot reaction rate vs substrate concentration

### Environmental Science: Climate Trends
Plot temperature anomaly vs year

### Agricultural Science: Fertilizer Response
Plot crop yield vs fertilizer amount

---

## Key Terms

- **Slope**: Rate of change (Δy/Δx)
- **Y-intercept**: Value of y when x = 0
- **Residual**: Difference between observed and predicted
- **R-squared**: Coefficient of determination
- **Best-fit line**: Line minimizing residuals

---

## Practice Problems

1. Find the equation of the line through (2, 5) and (6, 13)
2. A plant grows 2.5 cm per week. Write the height equation.
3. Create a scatter plot from the data below and fit a line.

---

*Next week: Non-Linear Relationships and Logarithms*
