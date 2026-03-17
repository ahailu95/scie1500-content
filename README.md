# SCIE1500 Course Content - Semester 1, 2026

## Analytical Methods for Scientists

This directory contains the course materials for SCIE1500, used by the SciQuant Assistant app.

---

## ⛔ CRITICAL — ALWAYS PULL BEFORE EDITING `course_config.json`

> **Why this matters:** Multiple people and automated tools can update this file. Editing a stale local copy and pushing will silently overwrite live changes (e.g. videos, announcements, schedule updates added since your last pull).

### THE ONLY SAFE WORKFLOW — NO EXCEPTIONS:

```bash
# ✅ STEP 0 — ALWAYS DO THIS FIRST, EVERY SINGLE TIME:
cd ~/scie1500-content
git pull origin main          # ← NEVER SKIP THIS LINE

# ✅ STEP 1 — Edit the file IN PLACE (never copy from another location without pulling first)

# ✅ STEP 2 — Bump the version field

# ✅ STEP 3 — Review the diff, commit, push
git diff course_config.json   # ← Check nothing was accidentally removed
git add -A && git commit -m "Describe your change" && git push origin main
```

### ❌ WHAT WILL CAUSE A DISASTER:

```bash
# ❌ NEVER copy course_config.json from another folder (e.g. app assets, Dropbox)
# over this file WITHOUT doing git pull first.
# Those copies are frequently stale and WILL overwrite live changes.
```

---

## Directory Structure

```
scie1500_2026_sem1/
├── course_config.json     # Main configuration (links resources to app)
├── lectures/              # Lecture notes (Markdown)
│   ├── week01_introduction.md
│   ├── week02_units.md
│   └── week03_linear.md
├── notebooks/             # Jupyter notebooks (open in Colab)
│   ├── week01_python_intro.ipynb
│   ├── week02_units.ipynb
│   └── week03_graphing.ipynb
├── exercises/             # Practice problems
│   ├── week01_practice.md
│   ├── week02_practice.md
│   └── week03_practice.md
└── videos/                # Video resource links
    └── video_links.md
```

## How to Use

### For Students
1. Open the SciQuant Assistant app
2. Navigate to any week
3. Tap on resources to access materials
4. Notebooks open directly in Google Colab

### For Instructors
1. Edit files in this directory
2. Update `course_config.json` with new resources
3. Bump the version number
4. Commit and push to GitHub
5. App will automatically fetch updated content

## Resource Formats

### Lecture Notes
- Format: Markdown (.md)
- Can be converted to PDF for download
- Viewed directly in browser

### Notebooks
- Format: Jupyter Notebook (.ipynb)
- Opens in Google Colab via URL transformation:
  ```
  https://colab.research.google.com/github/ahailu95/sciquant_app/blob/main/scie1500_2026_sem1/notebooks/week01_python_intro.ipynb
  ```

### Exercises
- Format: Markdown (.md)
- Include practice problems with answer keys

### Videos
- External YouTube links
- Curated educational content

## Adding New Content

### Add a Lecture
1. Create `lectures/weekXX_topic.md`
2. Add entry to `course_config.json` under appropriate week:
```json
{
  "id": "wX_lecture1",
  "title": "Topic Name",
  "description": "Brief description",
  "type": "lectureNotes",
  "url": "https://raw.githubusercontent.com/ahailu95/sciquant_app/main/scie1500_2026_sem1/lectures/weekXX_topic.md",
  "source": "github"
}
```

### Add a Notebook
1. Create `notebooks/weekXX_topic.ipynb`
2. Test in Google Colab first
3. Add entry to `course_config.json`:
```json
{
  "id": "wX_nb1",
  "title": "Notebook Title",
  "description": "What students will learn",
  "runtime": "googleColab",
  "githubRepoUrl": "https://github.com/ahailu95/sciquant_app",
  "notebookPath": "scie1500_2026_sem1/notebooks/weekXX_topic.ipynb",
  "requiredPackages": ["numpy", "matplotlib"],
  "estimatedTimeMinutes": 45
}
```

## Testing

After making changes:
1. Push to GitHub
2. Wait 1-2 minutes for CDN cache to update
3. Open app and navigate to updated week
4. Tap refresh button if needed
5. Verify resources load correctly

## URL Patterns

| Resource Type | URL Pattern |
|---------------|-------------|
| Raw content | `https://raw.githubusercontent.com/ahailu95/sciquant_app/main/scie1500_2026_sem1/...` |
| Colab notebook | `https://colab.research.google.com/github/ahailu95/sciquant_app/blob/main/scie1500_2026_sem1/notebooks/...` |
| YouTube | `https://www.youtube.com/watch?v=VIDEO_ID` |
| Thumbnail | `https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg` |

## Contact

For issues with course content, contact the course coordinator.
For app issues, use the feedback option in Settings.
