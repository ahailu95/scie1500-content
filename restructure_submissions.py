"""
Restructures submission exercises and presentation notes in generate_lab_notebooks.py.
Uses a line-list approach to avoid backslash/escaping issues.
"""

with open('generate_lab_notebooks.py') as f:
    lines = f.readlines()


def find_line(text, start=0):
    for i in range(start, len(lines)):
        if text in lines[i]:
            return i
    return None


def find_line_in(text, lst, start=0):
    for i in range(start, len(lst)):
        if text in lst[i]:
            return i
    return None


def ind(text, n=8):
    """Return text indented by n spaces, as a file line."""
    return ' ' * n + text + '\n'


def md_open():
    return ind('md("""\\\n'.rstrip('\n') + '\n')


def code_open():
    return ind('code("""\\\n'.rstrip('\n') + '\n')


def md_close():
    return ind('"""),')


def code_close():
    return ind('"""),')


def md_cell(content_lines):
    """Build an md() cell from a list of content strings."""
    result = [ind('md("""\\\n'.rstrip('\n') + '\n')]
    for line in content_lines:
        result.append(line + '\n' if not line.endswith('\n') else line)
    result.append(ind('"""),'))
    return result


def code_cell(content_lines):
    """Build a code() cell from a list of content strings."""
    result = [ind('code("""\\\n'.rstrip('\n') + '\n')]
    for line in content_lines:
        result.append(line + '\n' if not line.endswith('\n') else line)
    result.append(ind('"""),'))
    return result


def blank():
    return ['\n']


def ident_cell():
    return code_cell([
        '# Fill in your details before submitting',
        'student_name   = "Your full name"',
        'student_number = "Your student number (e.g. 23456789)"',
        'print(f"Submission by: {student_name}  |  Student #{student_number}")',
    ])


def answer_cell(label=''):
    suffix = f' ({label})' if label else ''
    return md_cell([
        f'**Answer{suffix}:**',
        '',
        '...write your working here...',
    ])


def answer_cell_text(label=''):
    suffix = f' ({label})' if label else ''
    return md_cell([
        f'**Answer{suffix}:**',
        '',
        '...write your answer here...',
    ])


# ── BATCH 1 (week3_student) ───────────────────────────────────────────────────

BATCH1 = (
    blank() +
    md_cell([
        '---',
        '---',
        '## ✅ Submission Exercise — Batch 1',
        '',
        '**Due: Monday 11 August, 11:59 pm — submit on LMS**',
        '**Covers: Weeks 1–3 (functions, exponential models, logistic growth)**',
        '',
        'Submit individually. Show full mathematical working for all calculations.',
        'Upload your **completed notebook (.ipynb)** to the LMS — do not submit screenshots.',
    ]) +
    blank() +
    ident_cell() +
    blank() +
    md_cell([
        '---',
        '### Q1 — Functions and Rates of Change (Week 1)',
        '',
        'Southern bluefin tuna population data:',
        '',
        '| Year | $t$ (yrs since 2000) | $P(t)$ (thousand fish) |',
        '|------|---------------------|------------------------|',
        '| 2000 | 0  | 90 |',
        '| 2005 | 5  | 82 |',
        '| 2010 | 10 | 71 |',
        '| 2015 | 15 | 65 |',
        '| 2020 | 20 | 61 |',
        '',
        '**(a)** Calculate the average rate of change of $P$ over each of the four 5-year intervals. Show working.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell(['**(b)** Is the decline rate constant? Describe the pattern and what it implies about the shape of $P(t)$.']) +
    blank() +
    answer_cell_text('b') +
    blank() +
    md_cell(['**(c)** Plot $P(t)$ from $t = 0$ to $t = 20$. Does a linear model fit this data well? Explain.']) +
    blank() +
    code_cell([
        '# Q1c — your code here',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        '%matplotlib inline',
        '',
    ]) +
    blank() +
    md_cell([
        '**Answer (c) — written interpretation:**',
        '',
        '...write your answer here...',
    ]) +
    blank() +
    md_cell([
        '---',
        '### Q2 — Exponential Decay (Week 2)',
        '',
        r'A marine toxin degrades as $C(t) = 250\\,e^{-0.08t}$ μg/L ($t$ in days).',
        '',
        '**(a)** Find the half-life algebraically. Show working using logarithms.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell(['**(b)** The safe-swimming threshold is 5 μg/L. Find the crossing day algebraically, then verify in Python.']) +
    blank() +
    md_cell([
        '**Answer (b) — algebraic working:**',
        '',
        '...write your working here...',
    ]) +
    blank() +
    code_cell([
        '# Q2b — Python verification',
        'import numpy as np',
        '',
        'def C(t):',
        '    return 250 * np.exp(-0.08 * t)',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell([r'**(c)** Plot $C(t)$ from $t = 0$ to $t = 60$. Mark the threshold as a horizontal dashed line and the crossing day as a vertical marker.']) +
    blank() +
    code_cell(['# Q2c — your code here', '']) +
    blank() +
    md_cell([
        '---',
        '### Q3 — Logistic Fishery (Week 3)',
        '',
        r'A Carpentaria prawn fishery: $G(S) = 0.5S(1 - S/2000)$.',
        '',
        r'**(a)** Find the MSY and the stock level at which it occurs. Show the algebraic derivation.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell([r'**(b)** Current stock is 1400 t, harvest is 200 t/yr. Is this sustainable? Justify by computing $G(1400)$.']) +
    blank() +
    answer_cell_text('b') +
    blank() +
    md_cell([r'**(c)** Find both equilibrium stock levels for $H = 200$ t/yr using the quadratic formula. Identify which is stable and which is unstable.']) +
    blank() +
    answer_cell('c') +
    blank() +
    md_cell(['**(d)** [Written] The manager reduces harvest to 150 t/yr while stock is 1400 t. What happens to the stock over time? Justify from the model.']) +
    blank() +
    answer_cell_text('d') +
    [ind('])')]
)

# ── BATCH 2 (week6_student) ───────────────────────────────────────────────────

BATCH2 = (
    blank() +
    md_cell([
        '---',
        '## ✅ Submission Exercise — Batch 2 (due Tuesday 8 September, 11:59 pm)',
        '',
        '**Submit via LMS. Covers Weeks 4–6 (limits, differentiation, integration).**',
        '',
        'Work individually. Show all working. Write Python code where indicated.',
        'Upload your **completed notebook (.ipynb)** to the LMS — do not submit screenshots.',
    ]) +
    blank() +
    ident_cell() +
    blank() +
    md_cell([
        '---',
        '### Q1 — Limits and Continuity (Week 4)',
        '',
        'A population model uses:',
        '',
        r'$$P(t) = \\frac{1000t}{t + 5}$$',
        '',
        r'**(a)** Evaluate $\\lim_{t \\to \\infty} P(t)$. Show your working algebraically (divide numerator and denominator by $t$).',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell([r'**(b)** Is $P(t)$ continuous for all $t \\geq 0$? Justify briefly.']) +
    blank() +
    answer_cell_text('b') +
    blank() +
    md_cell([r'**(c)** Verify your limit numerically by evaluating $P(t)$ at $t = 100, 1000, 10000$.']) +
    blank() +
    code_cell([
        '# Q1c — numerical limit verification',
        'import numpy as np',
        '',
        'def P(t):',
        '    return 1000*t / (t + 5)',
        '',
        '# Evaluate at large t values — your code here',
        '',
    ]) +
    blank() +
    md_cell([
        '---',
        '### Q2 — Differentiation and Optimisation (Week 5)',
        '',
        "A timber company's profit (thousands of dollars) as a function of harvest age $a$ (years) is:",
        '',
        r'$$\\pi(a) = 80a - 2a^2 - 150 \\quad \\text{for } 5 \\leq a \\leq 30$$',
        '',
        r"**(a)** Find $\\pi'(a)$ using the power rule. Show each step.",
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell([r'**(b)** Find the harvest age $a^*$ that maximises profit. Use the second derivative to confirm it is a maximum.']) +
    blank() +
    answer_cell('b') +
    blank() +
    md_cell([r'**(c)** Evaluate $\\pi(a^*)$ and the boundary values $\\pi(5)$ and $\\pi(30)$ in Python.']) +
    blank() +
    code_cell([
        '# Q2c — profit at critical point and boundaries',
        'import numpy as np',
        '',
        'def pi_a(a):',
        '    return 80*a - 2*a**2 - 150',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell([r"**(d)** Interpret: what does $\\pi'(a^*) = 0$ mean in harvesting terms?"]) +
    blank() +
    answer_cell_text('d') +
    blank() +
    md_cell([
        '---',
        '### Q3 — Integration and Accumulation (Week 6)',
        '',
        r'A bushfire recovery site sequesters carbon at rate $R(t) = 8e^{-0.04t}$ tonnes CO₂/ha/yr.',
        '',
        r'**(a)** Find the antiderivative $F(t)$ with $F(0) = 0$. Show the rule you used.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell([r'**(b)** Calculate the total carbon captured per hectare over 30 years. Give an exact expression and a decimal approximation.']) +
    blank() +
    answer_cell('b') +
    blank() +
    md_cell([r'**(c)** Plot $R(t)$ for $t \\in [0, 30]$, shade the area under the curve, and annotate with the integral value from (b).']) +
    blank() +
    code_cell([
        '# Q3c — plot and shade',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        '%matplotlib inline',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell([r'**(d)** Carbon credits sell at \$30/tonne and the site covers 250 ha. Calculate total project revenue over 30 years.']) +
    blank() +
    answer_cell('d') +
    [ind('])')]
)

# ── BATCH 3 (week9_student) ───────────────────────────────────────────────────

BATCH3 = (
    blank() +
    md_cell([
        '---',
        '## ✅ Submission Exercise — Batch 3 (due Tuesday 29 September, 11:59 pm)',
        '',
        '**Submit via LMS. Covers Weeks 7–9 (definite integrals, ODEs, probability).**',
        '',
        'Work individually. Show all working. Write Python code where indicated.',
        'Upload your **completed notebook (.ipynb)** to the LMS — do not submit screenshots.',
    ]) +
    blank() +
    ident_cell() +
    blank() +
    md_cell([
        '---',
        '### Q1 — Consumer and Producer Surplus (Week 7)',
        '',
        'A freshwater prawn market in the Ord River region has:',
        '- Demand: $Q_d = 400 - 2P$ (kg/week)',
        '- Supply: $Q_s = -60 + 3P$ (kg/week)',
        '',
        r'**(a)** Find the equilibrium price $P^*$ and quantity $Q^*$ algebraically.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell(['**(b)** Derive the inverse demand and inverse supply functions.']) +
    blank() +
    answer_cell('b') +
    blank() +
    md_cell(['**(c)** Calculate CS and PS using the triangle formulas. Show all working.']) +
    blank() +
    answer_cell('c') +
    blank() +
    md_cell(['**(d)** Verify CS and PS using numerical integration (`numpy.trapz`).']) +
    blank() +
    code_cell([
        '# Q1d — verify with integration',
        'import numpy as np',
        '',
        'def demand_P(Q):',
        '    # inverse demand: P as a function of Q — your code here',
        '    pass',
        '',
        'def supply_P(Q):',
        '    # inverse supply: P as a function of Q — your code here',
        '    pass',
        '',
        '# Your integration code here',
        '',
    ]) +
    blank() +
    md_cell([
        '---',
        '### Q2 — Predator-Prey Dynamics (Week 8)',
        '',
        'A quoll-rat system in the Pilbara:',
        '',
        r'$$\\frac{dR}{dt} = 0.6R - 0.003RQ, \\qquad \\frac{dQ}{dt} = -0.2Q + 0.001RQ$$',
        '',
        'where $R$ = rat population, $Q$ = quoll population.',
        '',
        r'**(a)** Find the coexistence equilibrium $(R^*, Q^*)$. Show your algebra.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell(['**(b)** Identify the rat nullcline and quoll nullcline. What does each represent biologically?']) +
    blank() +
    answer_cell_text('b') +
    blank() +
    md_cell([r"**(c)** Simulate the system for 30 years starting from $R_0 = 500$, $Q_0 = 80$ using Euler's method (dt = 0.01). Plot both populations over time."]) +
    blank() +
    code_cell([
        '# Q2c — Euler method simulation',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        '%matplotlib inline',
        '',
        '# Parameters',
        'r_R = 0.6; a = 0.003; d_Q = 0.2; b = 0.001',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell(['**(d)** Do the populations oscillate or converge? Is the equilibrium reached?']) +
    blank() +
    answer_cell_text('d') +
    blank() +
    md_cell([
        '---',
        "### Q3 — Bayes' Theorem (Week 9)",
        '',
        'A breast cancer screening test has sensitivity 90% and specificity 92%. Background prevalence in the 50–60 age group is 1.5%.',
        '',
        r'**(a)** Calculate $P(T^+)$ — the probability a randomly selected person tests positive.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell(["**(b)** Calculate the PPV using Bayes' theorem. Show each step."]) +
    blank() +
    answer_cell('b') +
    blank() +
    md_cell(['**(c)** Plot PPV vs prevalence for prevalence ranging from 0.1% to 20%. Annotate the 1.5% prevalence point.']) +
    blank() +
    code_cell([
        '# Q3c — PPV vs prevalence',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        '%matplotlib inline',
        '',
        'sensitivity = 0.90',
        'specificity = 0.92',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell(['**(d)** At what prevalence would PPV reach 50%? Solve algebraically or numerically.']) +
    blank() +
    answer_cell('d') +
    [ind('])')]
)

# ── BATCH 4 (week12_student) ──────────────────────────────────────────────────

BATCH4 = (
    blank() +
    md_cell([
        '---',
        '## ✅ Submission Exercise — Batch 4 (due Tuesday 27 October, 11:59 pm)',
        '',
        '**Submit via LMS. Covers Weeks 10–12 (hypothesis testing, trigonometry, linear programming).**',
        '',
        'Work individually. Show all working. Write Python code where indicated.',
        'Upload your **completed notebook (.ipynb)** to the LMS — do not submit screenshots.',
    ]) +
    blank() +
    ident_cell() +
    blank() +
    md_cell([
        '---',
        '### Q1 — Hypothesis Testing (Week 10)',
        '',
        r'A water authority claims average daily water consumption in a suburb is **no more than 180 L per person**. A sample of 36 households gives $\\bar{x} = 191$ L and $s = 42$ L.',
        '',
        r'**(a)** State $H_0$ and $H_1$ for a one-tailed test.',
    ]) +
    blank() +
    answer_cell_text('a') +
    blank() +
    md_cell(['**(b)** Calculate the $t$-statistic. Show all working.']) +
    blank() +
    answer_cell('b') +
    blank() +
    md_cell([r'**(c)** At $\\alpha = 0.05$ ($df = 35$, one-tailed critical value $\\approx 1.690$), state your conclusion.']) +
    blank() +
    md_cell([
        '**Answer (c):**',
        '',
        '...write your conclusion here...',
    ]) +
    blank() +
    md_cell(['**(d)** Compute the exact $p$-value using `scipy.stats.t`.']) +
    blank() +
    code_cell([
        '# Q1d — exact p-value',
        'from scipy import stats',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell([
        '---',
        '### Q2 — Trigonometric Modelling (Week 11)',
        '',
        'Daylight hours in a southern Australian city vary seasonally. The longest day has 14.5 hours (December 22) and the shortest has 9.5 hours (June 21).',
        '',
        '**(a)** Find the amplitude $A$ and midline $D$.',
    ]) +
    blank() +
    answer_cell('a') +
    blank() +
    md_cell([r'**(b)** The period is 365 days. Find $B = 2\\pi/365$.']) +
    blank() +
    answer_cell_text('b') +
    blank() +
    md_cell([r'**(c)** Write the function $f(t)$ where $t$ = day of year, with $f(1) \\approx 9.5$ (January 1 is near the shortest day). Use an appropriate phase shift.']) +
    blank() +
    md_cell([
        '**Answer (c):**',
        '',
        '...write your function here...',
    ]) +
    blank() +
    md_cell(['**(d)** Plot $f(t)$ for one year and calculate the total daylight hours over the year using `numpy.trapz`.']) +
    blank() +
    code_cell([
        '# Q2d — plot and integrate',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        '%matplotlib inline',
        '',
        '# Your code here',
        '',
    ]) +
    blank() +
    md_cell([
        '---',
        '### Q3 — Linear Programming (Week 12)',
        '',
        'A farmer grows wheat ($x$ ha) and canola ($y$ ha) on 200 ha. Constraints:',
        r'- Land: $x + y \\leq 200$',
        r'- Water: $3x + 5y \\leq 800$ (ML)',
        r'- Labour: $x + 2y \\leq 300$ (days)',
        r'- Non-negativity: $x \\geq 0$, $y \\geq 0$',
        '',
        r'Profit: wheat \$180/ha, canola \$250/ha. **Maximise** $Z = 180x + 250y$.',
        '',
        '**(a)** Graph the feasible region. Label each constraint line and shade the feasible region.',
    ]) +
    blank() +
    md_cell([
        '**Answer (a):** *(sketch or description)*',
        '',
        '...write your description or attach a sketch here...',
    ]) +
    blank() +
    md_cell(['**(b)** Identify all corner points (intersections of constraint boundaries within the feasible region).']) +
    blank() +
    md_cell([
        '**Answer (b):**',
        '',
        '...list corner points and show working here...',
    ]) +
    blank() +
    md_cell(['**(c)** Evaluate $Z$ at each corner point. State the optimal solution.']) +
    blank() +
    md_cell([
        '**Answer (c):**',
        '',
        '...write your working and conclusion here...',
    ]) +
    blank() +
    md_cell(['**(d)** Verify your answer using `scipy.optimize.linprog`. (Note: `linprog` minimises — negate the objective to maximise.)']) +
    blank() +
    code_cell([
        '# Q3d — linprog verification',
        'from scipy.optimize import linprog',
        '',
        '# Your code here',
        '',
    ]) +
    [ind('])')]
)

# ── Apply all batch replacements ──────────────────────────────────────────────

def replace_batch(all_lines, marker, new_content):
    header_idx = find_line_in(marker, all_lines)
    # Walk backwards from the section header to find the md("""\ opener line
    md_start = header_idx - 1
    while md_start >= 0 and 'md("""' not in all_lines[md_start]:
        md_start -= 1
    end_idx = find_line_in('    ])', all_lines, md_start) + 1
    return all_lines[:md_start] + new_content + all_lines[end_idx:]


current = list(lines)
current = replace_batch(current, 'Submission Exercise — Batch 1', BATCH1)
print('✓ Batch 1 replaced')

current = replace_batch(current, 'Submission Exercise — Batch 2', BATCH2)
print('✓ Batch 2 replaced')

current = replace_batch(current, 'Submission Exercise — Batch 3', BATCH3)
print('✓ Batch 3 replaced')

current = replace_batch(current, 'Submission Exercise — Batch 4', BATCH4)
print('✓ Batch 4 replaced')

# ── Add presentation upload note ──────────────────────────────────────────────
SUBMIT_NOTE = '> **What to submit:** upload your completed presentation slides (PDF or PowerPoint) to the LMS after your presentation.\n'

result = []
for line in current:
    result.append(line)
    # After "Do not show raw code" lines, insert if not already present
    stripped = line.strip()
    if ('Do not show raw code' in line and '"""),' in line and 'What to submit' not in line):
        # Insert before the closing """),
        new_line = line.replace('"""),', '')
        result[-1] = new_line.rstrip() + '\n'
        result.append(SUBMIT_NOTE)
        result.append('"""),\n')
    elif ('should cover:' in line and '."""),' in line and 'What to submit' not in line):
        # Preamble ending with ."""),
        new_line = line.replace('."""),', '')
        result[-1] = new_line.rstrip() + '\n'
        result.append(SUBMIT_NOTE)
        result.append('"""),\n')

n_pres = sum(1 for l in result if 'What to submit' in l)
print(f'✓ Presentation upload note added to {n_pres} A/B notebooks')

with open('generate_lab_notebooks.py', 'w') as f:
    f.writelines(result)

print('\nDone.')
