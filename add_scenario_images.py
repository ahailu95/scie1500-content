"""
Insert scenario images into generate_lab_notebooks.py.
Each image goes as a new line immediately after the blank line that follows
the ## ... Scenario/Scientific Scenario heading line.

Pattern inserted:
    (blank line after heading)
    ![alt text](../images/filename.svg)
    (blank line)
    ... existing scenario text ...
"""

INSERTIONS = [
    # (search_text_in_md_cell, image_filename, alt_text)
    (
        "## 🌊 Scientific Scenario: Global Plastic Production",
        "W1_plastic_production.svg",
        "Global plastic production data with rate of change trends",
    ),
    (
        "## 🌍 Scientific Scenario\n\nYour team is preparing educational materials comparing",
        "W2_doubling_times.svg",
        "Comparing exponential growth and decay across three domains",
    ),
    (
        "## 📋 Scenario\n\nYou are a consultant for **Royal Perth Hospital",
        "W2A_bacterial_hospital.svg",
        "MRSA bacterial growth curve approaching shutdown threshold",
    ),
    (
        "## 📋 Scenario\n\nYou are advising the **Japanese government",
        "W2B_radioactive_fukushima.svg",
        "Radioactive decay curves for Cs-137 and Sr-90",
    ),
    (
        "## 🌍 Scientific Scenario\n\nYou are a scientific advisor to the **Western Australian Fisheries",
        "W3_fishery_schaefer.svg",
        "Schaefer growth curve with harvest lines and MSY point",
    ),
    (
        "## 📋 Scenario\n\nThe WA Department of Fisheries manages a commercial abalone",
        "W3A_abalone.svg",
        "Abalone growth parabola with current and proposed harvest levels",
    ),
    (
        "## 📋 Scenario\n\nWA's rock lobster",
        "W3B_rock_lobster.svg",
        "Rock lobster growth under current vs warming conditions",
    ),
    (
        "## 🌍 Scientific Scenario\n\nA pharmaceutical company is optimizing production",
        "W4_chemical_reaction.svg",
        "Chemical yield curve showing optimal temperature and derivative",
    ),
    (
        "## 📋 Scenario\n\nA wheat farm in the Wheatbelt uses a pesticide",
        "W4A_pesticide.svg",
        "Pesticide concentration decay with effective zone and vulnerability window",
    ),
    (
        "## 📋 Scenario\n\nA pharmacologist is designing a dosing protocol",
        "W4B_pharmacokinetics.svg",
        "Drug concentration profile with therapeutic window and dosing",
    ),
    (
        "## 🌍 Scientific Scenario\n\nThe Department of Biodiversity is designing",
        "W5_wildlife_corridor.svg",
        "Wildlife corridor layout and area optimisation curve",
    ),
    (
        "## 📋 Scenario\n\nA renewable energy company designs a 50-ha solar farm",
        "W5A_solar_farm.svg",
        "Solar farm revenue optimisation curve",
    ),
    (
        "## 📋 Scenario\n\nA barramundi farm in Exmouth",
        "W5B_aquaculture.svg",
        "Aquaculture profit as a function of stocking density",
    ),
    (
        "## 📋 Scientific Scenario\n\nA reforestation project in the Wheatbelt",
        "W6_carbon_sequestration.svg",
        "Carbon sequestration rate and cumulative capture over time",
    ),
    (
        "## 📋 Scenario\n\nA soil carbon project converts 800 ha",
        "W6A_soil_carbon.svg",
        "Soil carbon accumulation rate and cumulative storage",
    ),
    (
        "## 📋 Scenario\n\nA managed aquifer recharge",
        "W6B_groundwater.svg",
        "Groundwater infiltration rate and cumulative volume vs target",
    ),
    (
        "## 📋 Scientific Scenario\n\nThe Australian domestic wheat market",
        "W7_market_welfare.svg",
        "Supply and demand diagram with consumer and producer surplus",
    ),
    (
        "## 📋 Scenario\n\nThe Australian domestic wine market",
        "W7A_wine_market.svg",
        "Wine market equilibrium with price floor intervention",
    ),
    (
        "## 📋 Scenario\n\nThe Australian avocado market",
        "W7B_avocado_market.svg",
        "Avocado market comparison: domestic only vs with exports",
    ),
    (
        "## 📋 Scientific Scenario\n\nFeral cats threaten numbats",
        "W8_predator_prey.svg",
        "Lotka-Volterra phase plane and population oscillations",
    ),
    (
        "## 📋 Scenario\n\nSame Lotka-Volterra model as the main lab",
        "W8A_cat_control.svg",
        "Detailed phase portrait with directional field and trajectory",
    ),
    (
        "## 📋 Scenario\n\nIn the Kimberley, dingoes prey on kangaroos",
        "W8B_dingo_kangaroo.svg",
        "Dingo-kangaroo dynamics: natural balance vs culling scenario",
    ),
    (
        "## 📋 Scientific Scenario\n\nDuring a COVID-19 wave",
        "W9_bayes_testing.svg",
        "Diagnostic testing: population grid and PPV vs prevalence curve",
    ),
    (
        "## 📋 Scientific Scenario\n\nA hospital dietitian needs to design",
        "W12_linear_programming.svg",
        "Linear programming feasible region with constraint lines",
    ),
]

with open('generate_lab_notebooks.py') as f:
    content = f.read()

inserted = 0
for search_text, image_file, alt_text in INSERTIONS:
    # The search_text is the heading + "\n\n" + start of next line
    # We want to insert the image between the heading's blank line and the text
    # i.e., replace "heading\n\ntext" with "heading\n\n![alt](../images/file.svg)\n\ntext"

    # Find the heading line only (up to first \n\n)
    heading_end = search_text.find('\n\n')
    if heading_end == -1:
        heading = search_text
        after = ''
    else:
        heading = search_text[:heading_end]
        after = search_text[heading_end + 2:]  # skip the \n\n

    img_line = f"![{alt_text}](../images/{image_file})"

    # Pattern: heading + \n\n + (possibly some text that starts with after)
    old = f"{heading}\n\n{after}"
    new = f"{heading}\n\n{img_line}\n\n{after}"

    if old in content:
        content = content.replace(old, new, 1)
        inserted += 1
        print(f"  ✓ Inserted {image_file}")
    else:
        print(f"  ✗ NOT FOUND: {heading[:60]!r}...")

print(f"\nTotal insertions: {inserted}/{len(INSERTIONS)}")

with open('generate_lab_notebooks.py', 'w') as f:
    f.write(content)

print("Done.")
