# Week 11 Materials Evaluation Report

## SCIE1500 — Analytical Methods for Scientists
### Assessment of TemperatureSTUDENTS.ipynb Consistency with Lesson and Code Snippets

---

## Executive Summary

I reviewed the Week 11 materials package:
- `TemperatureSTUDENTS.ipynb` (existing lab notebook)
- `week11_lesson.md` (comprehensive content)
- `week11_code_snippets.json` (10 Python snippets)
- `week11_practice.json` (20 practice questions)
- `TemperatureAvCityData.csv` (temperature data for 24 cities)

**Overall Assessment:** The notebook is **partially consistent** but has **significant content gaps** relative to the lesson and exam requirements. The notebook focuses heavily on temperature modeling but **misses critical exam-aligned content** from Q31 (radian conversion, amplitude, period, frequency) and Q36 (pencil movement model).

---

## Part 1: Content Coverage Analysis

### 1.1 Lesson Topics vs. Notebook Coverage

| Lesson Topic | Exam Alignment | In Notebook? | In Code Snippets? |
|--------------|----------------|--------------|-------------------|
| Degree-radian conversion | **Q31** | ❌ **Missing** | ✅ CS02 |
| Exact trig values (sin, cos, tan) | **Q31** | ❌ **Missing** | ✅ CS03 |
| Unit circle definition | Background | ❌ Missing | ❌ Not needed |
| ASTC quadrant signs | Background | ❌ **Missing** | ✅ CS04 |
| Pythagorean identity | **Q31** | ❌ **Missing** | ✅ CS05 |
| Amplitude calculation | **Q31, Q36** | ✅ Yes | ✅ CS06, CS07 |
| Period calculation | **Q31** | ⚠️ Implicit only | ✅ CS06, CS07 |
| Frequency calculation | **Q31** | ❌ **Missing** | ✅ CS07 |
| Phase shift (C parameter) | **Q36** | ✅ Yes | ✅ CS06, CS07 |
| Vertical shift (D parameter) | **Q36** | ✅ Yes | ✅ CS06, CS07 |
| **Pencil movement model** | **Q36 (exact)** | ❌ **CRITICAL MISSING** | ✅ CS07 |
| Temperature modeling | Lab focus | ✅ Extensive | ✅ CS06, CS09 |
| **Circadian rhythm model** | Scientific context | ❌ **Missing** | ✅ CS08 |
| Parameter calculator function | Utility | ❌ Missing | ✅ CS10 |

### 1.2 Critical Gaps Summary

| Priority | Missing Content | Exam Impact |
|----------|----------------|-------------|
| 🔴 HIGH | Pencil movement model | **Q36 (exact exam question)** |
| 🔴 HIGH | Degree-radian conversion | **Q31** |
| 🔴 HIGH | Period and frequency formulas | **Q31** |
| 🟠 MEDIUM | Pythagorean identity | Q31 background |
| 🟠 MEDIUM | Circadian rhythm example | Scientific relevtic |
| 🟡 LOW | ASTC quadrant rules | Conceptual understanding |

---

## Part 2: Detailed Notebook Analysis

### 2.1 Current Structure

```
TemperatureSTUDENTS.ipynb
│
├── Introduction and objectives
├── Data loading (pd.read_csv)
├── Data exploration (shape, columns, nsmallest, nlargest)
├── Extract data for specific cities
├── Plot: Singapore, Mek'ele, Edmonton comparison
├── Plot: Northern Hemisphere cities
├── Plot: Southern Hemisphere cities
├── STUDENT EXERCISE A: Perth vs Los Angeles plot
├── Learn to fit trigonometric functions
│   ├── NIWA example explanation
│   ├── Wellington Airport parameter calculations
│   └── Wellington fitted plot (cosine and sine)
├── Fit functions to Perth and San Antonio
│   ├── Perth cosine fitting (guided)
│   └── STUDENT EXERCISE B: San Antonio sine fitting
├── STUDENT EXERCISE C: Quiz answers
└── APPENDIX: Step-by-step parameter illustration
```

### 2.2 Strengths of Current Notebook

| Strength | Description |
|----------|-------------|
| ✅ Real-world data | Uses actual city temperature data |
| ✅ Pandas practice | Reinforces data manipulation skills |
| ✅ Hemisphere comparison | Shows phase difference clearly |
| ✅ NIWA reference | Links to authoritative source |
| ✅ Parameter explanation | Clear explanation of A, B, C, D |
| ✅ Appendix visualization | Excellent step-by-step parameter demo |
| ✅ Southern Hemisphere focus | Perth, Wellington (relevant to students) |

### 2.3 Issues Identified

| Issue | Severity | Details |
|-------|----------|---------|
| Missing Q31 content | 🔴 Critical | No radian conversion, frequency examples |
| Missing Q36 content | 🔴 Critical | Pencil movement not included |
| External CSV dependency | 🟠 Important | Students need separate file |
| Exercise C mismatch | 🟠 Important | References "7 questions" but unclear which quiz |
| No exam alignment section | 🟠 Important | Students don't see connection to exam |
| San Antonio phase shift | 🟡 Minor | Northern Hemisphere (coldest = January, C = +5 for sine) |
| No learning outcomes | 🟡 Minor | Missing explicit objectives |

---

## Part 3: Code Snippets Utilization

### 3.1 Snippets Reflected in Notebook

| Snippet ID | Topic | In Notebook? | Notes |
|------------|-------|--------------|-------|
| W11-CS01 | Import libraries | ✅ Yes | Basic imports present |
| W11-CS02 | Degree-radian conversion | ❌ No | **Add this** |
| W11-CS03 | Exact trig values | ❌ No | **Add this** |
| W11-CS04 | Quadrant signs | ❌ No | Optional |
| W11-CS05 | Pythagorean identity | ❌ No | **Add this** |
| W11-CS06 | Wellington temperature | ✅ Partial | Similar but less detailed |
| W11-CS07 | Pencil movement (Q36) | ❌ No | **CRITICAL - Add this** |
| W11-CS08 | Circadian temperature | ❌ No | **Add this** |
| W11-CS09 | N vs S Hemisphere | ✅ Partial | Concept present |
| W11-CS10 | Parameter calculator | ❌ No | Optional utility |

### 3.2 Snippet Utilization Rate

- **Currently used:** ~30% (3 of 10 snippets partially reflected)
- **Recommended:** 70%+ for exam alignment

---

## Part 4: CSV Data Integration Issue

### 4.1 Current Approach (Problematic)
```python
df = pd.read_csv("TemperatureAvCityData.csv")
```
**Problem:** Requires students to have the CSV file in the same directory. This can cause FileNotFoundError issues.

### 4.2 Recommended Solutions

**Option A: Embed data as dictionary (Most Robust)**
```python
temperature_data = {
    'Country': ['United Kingdom', 'Finland', ...],
    'City': ['London', 'Helsinki', ...],
    'Jan': [5.2, -3.9, ...],
    # ... all months
}
df = pd.DataFrame(temperature_data)
```

**Option B: Create CSV from string (Moderate)**
```python
import io
csv_data = """Country,City,Jan,Feb,...
United Kingdom,London,5.2,5.3,...
..."""
df = pd.read_csv(io.StringIO(csv_data))
```

**Option C: Clear file path with error handling**
```python
import os
file_path = "TemperatureAvCityData.csv"
if not os.path.exists(file_path):
    print("ERROR: Please download TemperatureAvCityData.csv to this folder")
else:
    df = pd.read_csv(file_path)
```

**Recommendation:** Use Option A (embedded data) for reliability.

---

## Part 5: Recommended Notebook Restructure

### 5.1 Proposed New Structure

```
Week11_Trigonometry_Complete.ipynb (Revised)
│
├── PART A: Foundations for Exam Q31
│   ├── A.1 Degree-Radian Conversion (from CS02)
│   ├── A.2 Exact Trigonometric Values (from CS03)
│   ├── A.3 Pythagorean Identity (from CS05)
│   └── A.4 Amplitude, Period, Frequency Definitions
│
├── PART B: Modeling Periodic Phenomena (Exam Q36)
│   ├── B.1 The General Sinusoidal Function
│   ├── B.2 **Pencil Movement Model** (Q36 exact) ← NEW
│   ├── B.3 Circadian Body Temperature ← NEW
│   └── B.4 Parameter Fitting Procedure
│
├── PART C: Seasonal Temperature Modeling (Lab Focus)
│   ├── C.1 Load and Explore Data (with embedded CSV)
│   ├── C.2 Hemisphere Comparisons
│   ├── C.3 Wellington Airport Example (NIWA)
│   ├── C.4 STUDENT EXERCISE A: Perth vs Los Angeles
│   └── C.5 STUDENT EXERCISE B: San Antonio
│
├── PART D: Self-Assessment
│   ├── D.1 Practice Quiz Alignment
│   └── D.2 Learning Outcomes Checklist
│
└── APPENDIX: Parameter Visualization (keep current)
```

### 5.2 Key Additions Required

| Addition | Source | Exam Alignment |
|----------|--------|----------------|
| Degree-radian conversion section | CS02 + Lesson §1 | Q31 |
| Exact trig values table | CS03 + Lesson §2 | Q31 |
| Pythagorean identity examples | CS05 + Lesson §7 | Q31 |
| Period and frequency calculations | CS07 + Lesson §4 | Q31 |
| **Pencil movement model** | CS07 + Lesson §5.3 | **Q36** |
| Circadian rhythm model | CS08 + Lesson §5.1 | Scientific context |
| Embedded CSV data | Data file | Reliability |
| Exam alignment table | Practice questions | Student guidance |

---

## Part 6: Specific Corrections Needed

### 6.1 Student Exercise B: San Antonio Phase Shift

**Current instruction:** "Fit a **sine function** to San Antonio temperature data"

**Issue:** San Antonio is in the Northern Hemisphere (coldest month = January, month 1)

**For sine function with min at month 1:**
- Sine minimum occurs at argument = 3π/2
- B(1 + C) = 3π/2
- (π/6)(1 + C) = 3π/2
- 1 + C = 9
- **C = +8** (not +2 like Wellington)

**Recommendation:** Add explicit guidance for Northern Hemisphere phase shift calculation.

### 6.2 Student Exercise C: Quiz Reference

**Current text:** "Trigonometry practice quiz 1 (Week 11)" with "7 questions"

**Issue:** Our `week11_practice.json` has 20 questions, and the numbers don't match.

**Recommendation:** Either:
1. Update to reference specific question IDs from week11_practice.json
2. Or keep as-is if referencing an LMS quiz (but clarify in notebook)

### 6.3 Data File Path

**Current:** `pd.read_csv("TemperatureAvCityData.csv")`

**Recommendation:** Embed data or add error handling (see Part 4).

---

## Part 7: Summary of Required Changes

### 🔴 Critical (Must Do for Exam Alignment)

| Change | Action |
|--------|--------|
| Add Q31 foundations | Insert new Part A with radian conversion, exact values, period/frequency |
| Add Q36 pencil model | Insert pencil movement section before temperature modeling |
| Add exam alignment | Add table showing how exercises connect to Q31/Q36 |

### 🟠 Important (Should Do)

| Change | Action |
|--------|--------|
| Embed CSV data | Replace pd.read_csv with embedded dictionary |
| Add circadian rhythm | Include 24-hour body temperature example |
| Fix Exercise C | Align with actual practice questions or clarify reference |
| Add learning outcomes | List explicit outcomes at start |

### 🟡 Recommended (Consider)

| Change | Action |
|--------|--------|
| Add parameter calculator | Include CS10 utility function |
| Improve Exercise B guidance | Add explicit Northern Hemisphere phase shift notes |
| Add verification steps | Show students how to verify their fitted models |

---

## Part 8: Alignment Matrix

### Current vs. Recommended Coverage

| Exam Question | Current Coverage | Recommended Coverage |
|---------------|------------------|---------------------|
| Q31(i): 90° → radians | ❌ 0% | ✅ Add Part A.1 |
| Q31(ii): Amplitude | ✅ 80% | ✅ Keep + formalize |
| Q31(iii): Period | ⚠️ 40% | ✅ Add explicit formula |
| Q31(iv): Frequency | ❌ 0% | ✅ Add Part A.4 |
| Q36: Pencil model | ❌ 0% | ✅ Add Part B.2 |
| Q36: Phase shift | ✅ 70% | ✅ Add boundary condition method |

---

## Conclusion

The current notebook provides excellent coverage of **temperature modeling** but significantly underserves **exam preparation**. The most critical gaps are:

1. **Missing Q36 pencil movement example** — This is an exact exam question that students will face
2. **Missing Q31 foundational content** — Radian conversion, frequency calculations
3. **No explicit exam alignment** — Students don't see how lab work connects to exam

**Recommendation:** Create an enhanced notebook that:
1. Adds a new "Exam Foundations" section at the beginning
2. Includes the pencil movement model before temperature modeling
3. Embeds the CSV data for reliability
4. Adds explicit exam alignment references throughout

The code snippets (W11-CS01 through W11-CS10) provide excellent templates for the missing content.

---

*Report generated: Week 11 Materials Evaluation*
*Key finding: Notebook covers ~50% of exam-relevant content*
