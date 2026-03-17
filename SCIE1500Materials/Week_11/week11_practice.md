# Week 11: Practice Questions
## Trigonometric Functions and Periodic Models

**Theme:** "Modeling Cycles and Rhythms"

**Exam Alignment:** Q31, Q36

---

### Foundational Questions (1-8)

---

**Q1. [Radian Conversion — Exam Q31]**

Convert $90°$ to radians.

(A) $\frac{\pi}{4}$
(B) $\frac{\pi}{3}$
(C) $\frac{\pi}{2}$
(D) $\pi$
(E) $2\pi$

<details>
<summary>Solution</summary>

**Answer: (C)**

Using the conversion formula:

$$\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$$

$$90° \times \frac{\pi}{180} = \frac{90\pi}{180} = \frac{\pi}{2}$$

**Key relationship:** $90° = \frac{\pi}{2}$ radians (a quarter circle).

</details>

---

**Q2. [Radian Conversion]**

Convert $\frac{2\pi}{3}$ radians to degrees.

(A) 60°
(B) 90°
(C) 120°
(D) 150°
(E) 180°

<details>
<summary>Solution</summary>

**Answer: (C)**

Using the conversion formula:

$$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$$

$$\frac{2\pi}{3} \times \frac{180}{\pi} = \frac{2 \times 180}{3} = \frac{360}{3} = 120°$$

</details>

---

**Q3. [Exact Trigonometric Values]**

What is $\sin\left(\frac{\pi}{6}\right)$?

(A) 0
(B) $\frac{1}{2}$
(C) $\frac{\sqrt{2}}{2}$
(D) $\frac{\sqrt{3}}{2}$
(E) 1

<details>
<summary>Solution</summary>

**Answer: (B)**

The angle $\frac{\pi}{6}$ radians equals $30°$.

From the standard values: $\sin(30°) = \sin\left(\frac{\pi}{6}\right) = \frac{1}{2}$

**Memory aid:** For sine at 0°, 30°, 45°, 60°, 90°, the values are $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$.

</details>

---

**Q4. [Exact Trigonometric Values]**

What is $\cos\left(\frac{\pi}{3}\right)$?

(A) 0
(B) $\frac{1}{2}$
(C) $\frac{\sqrt{2}}{2}$
(D) $\frac{\sqrt{3}}{2}$
(E) 1

<details>
<summary>Solution</summary>

**Answer: (B)**

The angle $\frac{\pi}{3}$ radians equals $60°$.

From the standard values: $\cos(60°) = \cos\left(\frac{\pi}{3}\right) = \frac{1}{2}$

**Note:** $\cos(60°) = \sin(30°)$ because they are complementary angles.

</details>

---

**Q5. [Amplitude — Exam Q31]**

What is the amplitude of the function $f(x) = \frac{5}{2}\sin(2x)$?

(A) 1
(B) 2
(C) 2.5
(D) 5
(E) $\pi$

<details>
<summary>Solution</summary>

**Answer: (C)**

For a function $y = A\sin(Bx + C) + D$, the amplitude is $|A|$.

Here, $A = \frac{5}{2} = 2.5$.

**Note:** The coefficient 2 inside affects the period, not the amplitude.

</details>

---

**Q6. [Period — Exam Q31]**

What is the period of the function $x(t) = \frac{7}{2}\cos(\pi t)$?

(A) $\frac{1}{2}$ seconds
(B) 1 second
(C) 2 seconds
(D) $\pi$ seconds
(E) $2\pi$ seconds

<details>
<summary>Solution</summary>

**Answer: (C)**

For $y = A\cos(Bt)$, the period is:

$$T = \frac{2\pi}{|B|}$$

Here $B = \pi$, so:

$$T = \frac{2\pi}{\pi} = 2 \text{ seconds}$$

</details>

---

**Q7. [Frequency — Exam Q31]**

What is the frequency of the function $x(t) = \frac{7}{2}\cos(\pi t)$?

(A) 0.25 Hz
(B) 0.5 Hz
(C) 1 Hz
(D) 2 Hz
(E) $\pi$ Hz

<details>
<summary>Solution</summary>

**Answer: (B)**

Frequency is the reciprocal of period:

$$f = \frac{1}{T}$$

From the previous question, $T = 2$ seconds, so:

$$f = \frac{1}{2} = 0.5 \text{ Hz}$$

Alternatively: $f = \frac{|B|}{2\pi} = \frac{\pi}{2\pi} = 0.5$ Hz.

</details>

---

**Q8. [Quadrant Signs]**

In which quadrant is $\sin\theta > 0$ and $\cos\theta < 0$?

(A) Quadrant I
(B) Quadrant II
(C) Quadrant III
(D) Quadrant IV
(E) No such quadrant exists

<details>
<summary>Solution</summary>

**Answer: (B)**

Using the ASTC rule (All, Sin, Tan, Cos):

- Quadrant I: All positive
- Quadrant II: Only Sin positive
- Quadrant III: Only Tan positive
- Quadrant IV: Only Cos positive

In **Quadrant II**, sine is positive and cosine is negative. ✓

</details>

---

### Intermediate Questions (9-16)

---

**Q9. [Pythagorean Identity]**

If $\cos\theta = \frac{3}{5}$ and $\theta$ is in Quadrant I, what is $\sin\theta$?

(A) $\frac{2}{5}$
(B) $\frac{4}{5}$
(C) $\frac{3}{5}$
(D) $-\frac{4}{5}$
(E) $\frac{\sqrt{5}}{5}$

<details>
<summary>Solution</summary>

**Answer: (B)**

Using the Pythagorean identity $\sin^2\theta + \cos^2\theta = 1$:

$$\sin^2\theta = 1 - \cos^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}$$

$$\sin\theta = \pm\frac{4}{5}$$

Since $\theta$ is in Quadrant I, $\sin\theta > 0$, so $\sin\theta = \frac{4}{5}$.

</details>

---

**Q10. [Amplitude from Data — Circadian Context]**

A circadian body temperature oscillates between 36.5°C and 37.5°C. What is the amplitude of this oscillation?

(A) 0.5°C
(B) 1.0°C
(C) 36.5°C
(D) 37.0°C
(E) 37.5°C

<details>
<summary>Solution</summary>

**Answer: (A)**

Amplitude is half the range:

$$A = \frac{\text{max} - \text{min}}{2} = \frac{37.5 - 36.5}{2} = \frac{1.0}{2} = 0.5°C$$

**Note:** The amplitude is the displacement from the midline, not the range itself.

</details>

---

**Q11. [Vertical Shift]**

If a periodic function oscillates between -3 and 7, what is the vertical shift $D$?

(A) -3
(B) 2
(C) 3.5
(D) 5
(E) 7

<details>
<summary>Solution</summary>

**Answer: (B)**

The vertical shift $D$ is the midline:

$$D = \frac{\text{max} + \text{min}}{2} = \frac{7 + (-3)}{2} = \frac{4}{2} = 2$$

</details>

---

**Q12. [Angular Frequency]**

What is the angular frequency $B$ for a temperature cycle that repeats every 12 months?

(A) $\frac{\pi}{12}$
(B) $\frac{\pi}{6}$
(C) $\frac{\pi}{3}$
(D) $\frac{2\pi}{3}$
(E) $2\pi$

<details>
<summary>Solution</summary>

**Answer: (B)**

Angular frequency is related to period by:

$$B = \frac{2\pi}{\text{Period}}$$

For a 12-month period:

$$B = \frac{2\pi}{12} = \frac{\pi}{6} \text{ per month}$$

</details>

---

**Q13. [Phase Shift]**

For a cosine function, the minimum value occurs when the argument equals $\pi$. If the coldest month in the Southern Hemisphere is July (month 7), what should $C$ be in $T(m) = A\cos\left(\frac{\pi}{6}(m + C)\right) + D$?

(A) -7
(B) -1
(C) 0
(D) 1
(E) 7

<details>
<summary>Solution</summary>

**Answer: (B)**

For the minimum of cosine, we need the argument to equal $\pi$:

$$\frac{\pi}{6}(7 + C) = \pi$$

Divide both sides by $\frac{\pi}{6}$:

$$7 + C = 6$$

$$C = -1$$

</details>

---

**Q14. [Symmetry]**

Which of the following is true about $\cos(-\theta)$?

(A) $\cos(-\theta) = -\cos\theta$
(B) $\cos(-\theta) = \cos\theta$
(C) $\cos(-\theta) = \sin\theta$
(D) $\cos(-\theta) = -\sin\theta$
(E) $\cos(-\theta) = \tan\theta$

<details>
<summary>Solution</summary>

**Answer: (B)**

Cosine is an **even function**, meaning:

$$\cos(-\theta) = \cos\theta$$

**Contrast:** Sine is an **odd function**: $\sin(-\theta) = -\sin\theta$.

</details>

---

**Q15. [Tangent Calculation]**

If $\sin\theta = \frac{5}{13}$ and $\cos\theta = \frac{12}{13}$, what is $\tan\theta$?

(A) $\frac{5}{13}$
(B) $\frac{12}{13}$
(C) $\frac{5}{12}$
(D) $\frac{12}{5}$
(E) $\frac{13}{5}$

<details>
<summary>Solution</summary>

**Answer: (C)**

Using the quotient identity:

$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\frac{5}{13}}{\frac{12}{13}} = \frac{5}{13} \times \frac{13}{12} = \frac{5}{12}$$

</details>

---

**Q16. [Period Identification — Circadian Context]**

A circadian rhythm has a period of 24 hours. Which function models this rhythm if time $t$ is in hours?

(A) $y = A\sin(24t)$
(B) $y = A\sin\left(\frac{\pi}{24}t\right)$
(C) $y = A\sin\left(\frac{\pi}{12}t\right)$
(D) $y = A\sin\left(\frac{2\pi}{24}t\right)$
(E) $y = A\sin(2\pi t)$

<details>
<summary>Solution</summary>

**Answer: (C)**

For period $T = 24$ hours:

$$B = \frac{2\pi}{T} = \frac{2\pi}{24} = \frac{\pi}{12}$$

So the function is $y = A\sin\left(\frac{\pi}{12}t\right)$.

**Note:** Option D also gives $B = \frac{\pi}{12}$, but C is the simplified form.

</details>

---

### Exam-Style Questions (17-20)

---

**Q17. [Q31 Comprehensive]**

Which of the following statements is TRUE?

(i) 90° converted to radians is equal to $\frac{1}{2}\pi$
(ii) The function $\frac{5}{2}\sin(2x)$ has an amplitude of 2.5
(iii) The period of $x(t) = \frac{7}{2}\cos(\pi t)$ is 2 seconds
(iv) The frequency of $x(t) = \frac{7}{2}\cos(\pi t)$ is 0.5 Hz

(A) Only (i) and (ii) are true
(B) Only (iii) and (iv) are true
(C) Only (i), (ii), and (iii) are true
(D) Only (ii), (iii), and (iv) are true
(E) All of the above are true

<details>
<summary>Solution</summary>

**Answer: (E)**

**(i)** $90° = \frac{\pi}{2}$ radians ✓

**(ii)** Amplitude $= |A| = \frac{5}{2} = 2.5$ ✓

**(iii)** Period $= \frac{2\pi}{\pi} = 2$ seconds ✓

**(iv)** Frequency $= \frac{1}{2} = 0.5$ Hz ✓

**All statements are true.**

</details>

---

**Q18. [Q36 Pencil Movement — Motor Behavior]**

In a motor behavior experiment, a person moves a pencil periodically between 2 cm and 12 cm, completing a round every 2 seconds. The pencil is at position $x = 2$ cm at $t = 0$. If the model is $x(t) = A\cos(B(t + C)) + D$, what are the values of $A$, $B$, $C$, and $D$?

(A) $A = 6, B = \pi, C = 1, D = 7$
(B) $A = 6, B = \pi, C = 1.5, D = 8$
(C) $A = 5, B = 2\pi, C = 1.5, D = 7$
(D) $A = 5, B = \pi, C = 1, D = 7$
(E) $A = 12, B = 2\pi, C = -1.5, D = 8$

<details>
<summary>Solution</summary>

**Answer: (D)**

**Step 1: Amplitude**
$$A = \frac{12 - 2}{2} = 5$$

**Step 2: Vertical shift**
$$D = \frac{12 + 2}{2} = 7$$

**Step 3: Angular frequency (Period = 2 seconds)**
$$B = \frac{2\pi}{2} = \pi$$

**Step 4: Phase shift (minimum at $t = 0$)**

Cosine has minimum when argument $= \pi$:
$$\pi(0 + C) = \pi \Rightarrow C = 1$$

**Verification:** $x(0) = 5\cos(\pi \cdot 1) + 7 = 5(-1) + 7 = 2$ ✓

</details>

---

**Q19. [Temperature Modeling]**

Wellington Airport has a maximum monthly average temperature of 17.9°C in February and a minimum of 9.5°C in July. For the cosine model $T(m) = A\cos\left(\frac{\pi}{6}(m + C)\right) + D$, what is the vertical shift $D$?

(A) 4.2°C
(B) 9.5°C
(C) 13.7°C
(D) 17.9°C
(E) 27.4°C

<details>
<summary>Solution</summary>

**Answer: (C)**

The vertical shift $D$ is the midline:

$$D = \frac{\text{max} + \text{min}}{2} = \frac{17.9 + 9.5}{2} = \frac{27.4}{2} = 13.7°C$$

</details>

---

**Q20. [Complete Model Fitting — Heart Rate]**

A patient's heart rate varies sinusoidally between 60 and 100 beats per minute over a 4-minute exercise cycle. At $t = 0$ (start of exercise), heart rate is at its minimum of 60 bpm. Which function models the heart rate $H(t)$?

(A) $H(t) = 20\cos\left(\frac{\pi}{2}t\right) + 80$
(B) $H(t) = 20\cos\left(\frac{\pi}{2}(t+1)\right) + 80$
(C) $H(t) = 40\cos\left(\frac{\pi}{2}t\right) + 60$
(D) $H(t) = 20\sin\left(\frac{\pi}{2}t\right) + 80$
(E) $H(t) = 20\cos\left(\frac{\pi}{2}(t+2)\right) + 80$

<details>
<summary>Solution</summary>

**Answer: (E)**

**Step 1: Amplitude**
$$A = \frac{100 - 60}{2} = 20$$

**Step 2: Vertical shift**
$$D = \frac{100 + 60}{2} = 80$$

**Step 3: Angular frequency (Period = 4 minutes)**
$$B = \frac{2\pi}{4} = \frac{\pi}{2}$$

**Step 4: Phase shift (minimum at $t = 0$)**

Cosine has minimum when argument $= \pi$:
$$\frac{\pi}{2}(0 + C) = \pi \Rightarrow C = 2$$

**Verification:** $H(0) = 20\cos(\pi) + 80 = -20 + 80 = 60$ ✓

</details>

---

## Quick Reference: Key Formulas

| Concept | Formula |
|---------|---------|
| Degree → Radian | $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$ |
| Radian → Degree | $\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$ |
| Pythagorean Identity | $\sin^2\theta + \cos^2\theta = 1$ |
| Tangent | $\tan\theta = \frac{\sin\theta}{\cos\theta}$ |
| Amplitude | $|A| = \frac{\max - \min}{2}$ |
| Period | $T = \frac{2\pi}{|B|}$ |
| Frequency | $f = \frac{1}{T} = \frac{|B|}{2\pi}$ |
| Vertical Shift | $D = \frac{\max + \min}{2}$ |

---

*Week 11 Practice — Trigonometric Functions and Periodic Models*
