<?xml version="1.0" encoding="UTF-8"?>
# Week 11: Code Snippets
## Trigonometric Functions and Periodic Models

**Theme:** "Modeling Cycles and Rhythms"

These code snippets support the Week 11 lesson on trigonometric functions. Copy-paste them into your Jupyter notebook to visualize concepts and verify calculations.

---

## 1. Import Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set plot style for cleaner visuals
plt.style.use('seaborn-v0_8-whitegrid')

print("Libraries loaded successfully!")
print(f"π ≈ {np.pi:.6f}")
```

---

## 2. Degree-Radian Conversion

```python
def deg_to_rad(degrees):
    """Convert degrees to radians."""
    return degrees * np.pi / 180

def rad_to_deg(radians):
    """Convert radians to degrees."""
    return radians * 180 / np.pi

# Examples
print("Conversion Examples:")
print(f"90° = {deg_to_rad(90):.4f} rad = π/2")
print(f"π/3 rad = {rad_to_deg(np.pi/3):.1f}°")
print(f"2π rad = {rad_to_deg(2*np.pi):.1f}°")

# Built-in numpy functions (alternative)
print(f"\nUsing numpy: np.deg2rad(90) = {np.deg2rad(90):.4f}")
print(f"Using numpy: np.rad2deg(np.pi/2) = {np.rad2deg(np.pi/2):.1f}°")
```

---

## 3. Exact Trigonometric Values Table

```python
# Standard angles in radians
angles_rad = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi]
angles_deg = [0, 30, 45, 60, 90, 180]

print("Exact Trigonometric Values")
print("=" * 50)
print(f"{'Degrees':>8} {'Radians':>10} {'sin θ':>10} {'cos θ':>10} {'tan θ':>10}")
print("-" * 50)

for deg, rad in zip(angles_deg, angles_rad):
    sin_val = np.sin(rad)
    cos_val = np.cos(rad)
    # Handle tan(90°) which is undefined
    if np.abs(cos_val) < 1e-10:
        tan_val = "undef"
    else:
        tan_val = f"{np.tan(rad):.4f}"
    
    print(f"{deg:>8}° {rad:>10.4f} {sin_val:>10.4f} {cos_val:>10.4f} {tan_val:>10}")
```

---

## 4. Basic Sine and Cosine Graphs

```python
# Create x values from 0 to 4π
x = np.linspace(0, 4*np.pi, 500)

# Calculate y values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(12, 5))

plt.plot(x, y_sin, 'b-', linewidth=2, label=r'$y = \sin(x)$')
plt.plot(x, y_cos, 'r--', linewidth=2, label=r'$y = \cos(x)$')

# Mark key points on x-axis
key_points = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi]
labels = ['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π']
plt.xticks(key_points, labels)

plt.axhline(y=0, color='k', linewidth=0.5)
plt.axhline(y=1, color='gray', linestyle=':', alpha=0.5)
plt.axhline(y=-1, color='gray', linestyle=':', alpha=0.5)

plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Basic Sine and Cosine Functions', fontsize=14)
plt.legend(fontsize=12)
plt.ylim(-1.5, 1.5)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Key observations:")
print("- Both have amplitude = 1 and period = 2π")
print("- Cosine leads sine by π/2 (90°)")
```

---

## 5. Effect of Parameters A, B, C, D

```python
# Create x values (representing months 0-24)
x = np.linspace(0, 24, 200)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Effect of Amplitude (A)
ax1 = axes[0, 0]
for A in [1, 2, 3]:
    y = A * np.cos(np.pi/6 * x)
    ax1.plot(x, y, linewidth=2, label=f'A = {A}')
ax1.set_title('Effect of Amplitude (A)', fontsize=12)
ax1.set_xlabel('x (months)')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=0.5)

# 2. Effect of Angular Frequency (B)
ax2 = axes[0, 1]
for B_label, B in [('π/12 (24-mo)', np.pi/12), ('π/6 (12-mo)', np.pi/6), ('π/3 (6-mo)', np.pi/3)]:
    y = np.cos(B * x)
    ax2.plot(x, y, linewidth=2, label=f'B = {B_label}')
ax2.set_title('Effect of Angular Frequency (B)', fontsize=12)
ax2.set_xlabel('x (months)')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Effect of Phase Shift (C)
ax3 = axes[1, 0]
for C in [0, -2, 2]:
    y = np.cos(np.pi/6 * (x + C))
    direction = 'right' if C < 0 else 'left' if C > 0 else 'none'
    ax3.plot(x, y, linewidth=2, label=f'C = {C} (shift {direction})')
ax3.set_title('Effect of Phase Shift (C)', fontsize=12)
ax3.set_xlabel('x (months)')
ax3.set_ylabel('y')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 4. Effect of Vertical Shift (D)
ax4 = axes[1, 1]
for D in [0, 5, 10]:
    y = np.cos(np.pi/6 * x) + D
    ax4.plot(x, y, linewidth=2, label=f'D = {D}')
ax4.set_title('Effect of Vertical Shift (D)', fontsize=12)
ax4.set_xlabel('x (months)')
ax4.set_ylabel('y')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.suptitle(r'$y = A\cos(B(x + C)) + D$: Effect of Each Parameter', fontsize=14, y=1.02)
plt.tight_layout()
plt.show()
```

---

## 6. Temperature Model Fitting (Wellington Airport)

```python
# Wellington Airport temperature data (°C)
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Wellington_temps = np.array([17.8, 17.9, 16.6, 14.4, 12.0, 10.2, 
                              9.5, 9.9, 11.3, 12.9, 14.5, 16.4])

# Step 1: Calculate parameters
T_max = np.max(Wellington_temps)
T_min = np.min(Wellington_temps)

A = (T_max - T_min) / 2  # Amplitude
D = (T_max + T_min) / 2  # Vertical shift
B = 2 * np.pi / 12       # Angular frequency (12-month period)
C = -1                   # Phase shift (coldest month = July = 7)

print("Fitted Parameters:")
print(f"  Amplitude (A) = {A:.1f}°C")
print(f"  Angular frequency (B) = 2π/12 = {B:.4f} rad/month")
print(f"  Phase shift (C) = {C}")
print(f"  Vertical shift (D) = {D:.1f}°C")

# Step 2: Generate model predictions
months_fine = np.linspace(1, 12, 100)
T_model = A * np.cos(B * (months_fine + C)) + D

# Step 3: Plot data and model
plt.figure(figsize=(12, 6))
plt.plot(months, Wellington_temps, 'ko', markersize=10, label='Observed data')
plt.plot(months_fine, T_model, 'b-', linewidth=2, 
         label=f'Model: $T = {A:.1f}\\cos(\\frac{{\\pi}}{{6}}(m - 1)) + {D:.1f}$')

# Add reference lines
plt.axhline(y=D, color='gray', linestyle='--', alpha=0.5, label=f'Midline (D = {D:.1f}°C)')

plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.title('Wellington Airport: Temperature Model Fitting', fontsize=14)
plt.xticks(months, month_labels)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(8, 20)
plt.tight_layout()
plt.show()
```

---

## 7. Pencil Movement Model (Exam Q36)

```python
# Q36 Setup: Pencil moves between 2cm and 12cm, period = 2 seconds
# At t=0, position x = 2cm (minimum)

# Calculate parameters
x_max = 12  # cm
x_min = 2   # cm
T = 2       # seconds (period)

A = (x_max - x_min) / 2  # Amplitude = 5
D = (x_max + x_min) / 2  # Vertical shift = 7
B = 2 * np.pi / T        # Angular frequency = π
C = 1                    # Phase shift (minimum at t=0)

print("Q36 Solution: Pencil Movement Model")
print("=" * 40)
print(f"  A (amplitude) = {A} cm")
print(f"  B (angular freq) = π rad/s")
print(f"  C (phase shift) = {C}")
print(f"  D (vertical shift) = {D} cm")
print(f"\nModel: x(t) = {int(A)}cos(π(t + {C})) + {int(D)}")

# Verify at t=0
x_at_0 = A * np.cos(B * (0 + C)) + D
print(f"\nVerification: x(0) = {A}×cos(π×{C}) + {D} = {x_at_0} cm ✓")

# Plot the model
t = np.linspace(0, 4, 200)  # 4 seconds = 2 complete cycles
x = A * np.cos(B * (t + C)) + D

plt.figure(figsize=(12, 5))
plt.plot(t, x, 'b-', linewidth=2, label=r'$x(t) = 5\cos(\pi(t+1)) + 7$')
plt.scatter([0], [2], color='red', s=100, zorder=5, label='Initial position (0, 2)')

# Mark key features
plt.axhline(y=D, color='gray', linestyle='--', alpha=0.5, label=f'Midline (D = {D} cm)')
plt.axhline(y=x_max, color='r', linestyle=':', alpha=0.3)
plt.axhline(y=x_min, color='b', linestyle=':', alpha=0.3)

plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Position (cm)', fontsize=12)
plt.title('Q36: Pencil Position During Motor Behavior Experiment', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(0, 14)
plt.tight_layout()
plt.show()
```

---

## 8. Circadian Body Temperature Model

```python
# Typical circadian body temperature pattern
# Minimum ~36.5°C at 4 AM, Maximum ~37.3°C at 6 PM

T_max = 37.3  # °C
T_min = 36.5  # °C
period = 24   # hours

# Parameters
A = (T_max - T_min) / 2  # Amplitude
D = (T_max + T_min) / 2  # Midline
B = 2 * np.pi / period   # Angular frequency
C = 8                    # Phase shift (minimum at hour 4)

print("Circadian Body Temperature Model")
print("=" * 40)
print(f"  Amplitude: {A:.2f}°C")
print(f"  Midline: {D:.2f}°C")
print(f"  Period: {period} hours")
print(f"  Minimum at: 4:00 AM")

# Generate model
hours = np.linspace(0, 48, 200)  # Two days
T = A * np.cos(B * (hours + C)) + D

plt.figure(figsize=(14, 5))
plt.plot(hours, T, 'b-', linewidth=2, label='Body Temperature Model')

# Mark sleep periods (11 PM - 7 AM)
for day in [0, 24]:
    plt.axvspan(day + 23, min(day + 31, 48), alpha=0.2, color='gray', 
                label='Sleep' if day == 0 else '')

# Mark temperature extremes
plt.axhline(y=T_min, color='blue', linestyle=':', alpha=0.5, label=f'Min = {T_min}°C')
plt.axhline(y=T_max, color='red', linestyle=':', alpha=0.5, label=f'Max = {T_max}°C')
plt.axhline(y=D, color='green', linestyle='--', alpha=0.5, label=f'Mean = {D:.2f}°C')

# Add time labels
time_labels = ['12AM', '6AM', '12PM', '6PM', '12AM', '6AM', '12PM', '6PM', '12AM']
plt.xticks(np.arange(0, 49, 6), time_labels)

plt.xlabel('Time', fontsize=12)
plt.ylabel('Body Temperature (°C)', fontsize=12)
plt.title('Circadian Rhythm of Human Body Temperature', fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(36.2, 37.6)
plt.tight_layout()
plt.show()

print("\nClinical Relevance:")
print("- Drug metabolism varies with circadian phase")
print("- Optimal medication timing (chronotherapy)")
print("- Body temperature drops during sleep")
```

---

## 9. Parameter Calculator Function

```python
def calculate_sinusoidal_params(y_max, y_min, period, extreme_position, 
                                  extreme_type='min', model_type='cos'):
    """
    Calculate parameters for y = A*trig(B(x + C)) + D
    
    Parameters:
    -----------
    y_max : float - Maximum value
    y_min : float - Minimum value  
    period : float - Length of one complete cycle
    extreme_position : float - x-value where extreme occurs
    extreme_type : str - 'min' or 'max'
    model_type : str - 'cos' or 'sin'
    
    Returns:
    --------
    dict with A, B, C, D values
    """
    # Amplitude and vertical shift
    A = (y_max - y_min) / 2
    D = (y_max + y_min) / 2
    
    # Angular frequency
    B = 2 * np.pi / period
    
    # Phase shift calculation
    if model_type == 'cos':
        if extreme_type == 'min':
            target_arg = np.pi      # cos min at π
        else:
            target_arg = 0          # cos max at 0
    else:  # sin
        if extreme_type == 'min':
            target_arg = 3 * np.pi / 2  # sin min at 3π/2
        else:
            target_arg = np.pi / 2       # sin max at π/2
    
    # Solve: B(x_extreme + C) = target_arg
    C = target_arg / B - extreme_position
    
    return {'A': A, 'B': B, 'C': C, 'D': D}

# Example: Exam Q36 (Pencil movement)
print("Example: Exam Q36 - Pencil Movement")
print("=" * 45)
params = calculate_sinusoidal_params(
    y_max=12, y_min=2, period=2, 
    extreme_position=0, extreme_type='min', model_type='cos'
)
print(f"  A = {params['A']:.1f} cm")
print(f"  B = {params['B']:.4f} = π rad/s")
print(f"  C = {params['C']:.1f}")
print(f"  D = {params['D']:.1f} cm")
```

---

## 10. ASTC Quadrant Signs Visualization

```python
# Visualize signs in each quadrant
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Draw axes
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Draw unit circle
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2)

# Quadrant labels with ASTC rule
quadrant_info = [
    (0.5, 0.5, 'Q I\nAll +\nsin+, cos+, tan+', 'green'),
    (-0.5, 0.5, 'Q II\nSin +\nsin+, cos−, tan−', 'blue'),
    (-0.5, -0.5, 'Q III\nTan +\nsin−, cos−, tan+', 'orange'),
    (0.5, -0.5, 'Q IV\nCos +\nsin−, cos+, tan−', 'red')
]

for x, y, text, color in quadrant_info:
    ax.annotate(text, (x, y), fontsize=10, ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

# Add ASTC memory aid
ax.set_title('ASTC Rule: "All Students Take Calculus"', fontsize=14)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Add angle markers
for angle, label in [(0, '0'), (np.pi/2, 'π/2'), (np.pi, 'π'), (3*np.pi/2, '3π/2')]:
    x, y = np.cos(angle), np.sin(angle)
    ax.plot(x, y, 'ko', markersize=8)
    offset = 0.15
    ax.annotate(label, (x*(1+offset), y*(1+offset)), fontsize=10, ha='center')

plt.tight_layout()
plt.show()

print("Memory Aid: ASTC")
print("  A - All positive in Quadrant I")
print("  S - Sin positive in Quadrant II")
print("  T - Tan positive in Quadrant III")
print("  C - Cos positive in Quadrant IV")
```

---

## Quick Reference: Key Python Functions

| Operation | Python Code |
|-----------|-------------|
| Sine | `np.sin(x)` |
| Cosine | `np.cos(x)` |
| Tangent | `np.tan(x)` |
| Pi constant | `np.pi` |
| Deg → Rad | `np.deg2rad(degrees)` |
| Rad → Deg | `np.rad2deg(radians)` |
| Array creation | `np.linspace(start, end, num)` |
| Maximum | `np.max(array)` |
| Minimum | `np.min(array)` |

---

*Week 11 Code Snippets — Trigonometric Functions and Periodic Models*
