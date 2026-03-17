# Student Guide: Submitting Your Assignment Using SciQuant and GitHub

**SCIE1500 — Analytical Methods for Scientists, Semester 1 2026**

---

> **About this guide:** This guide explains what is happening when you submit your assignment through the SciQuant app. It describes what the app is doing *for* you automatically, what GitHub is, and why the workflow is set up this way. Understanding these concepts will help you avoid common mistakes and feel confident about your submission.

---

## Part 1: The Big Picture — What Is GitHub and Why Are We Using It?

### GitHub is like Google Drive, but for code and documents — with superpowers

You probably already use Google Drive or OneDrive to store files. GitHub does a similar job, but with one very powerful difference: **it remembers the entire history of every change you ever make**. It never truly deletes anything. Every time you save ("commit") your work, GitHub takes a timestamped snapshot and stores it forever.

This matters for assignments because:

- **Your instructor can see exactly when you did your work** — not just the final file, but every saving point along the way.
- **If you accidentally delete something, it can always be recovered.**
- **Your work is safe even if your laptop breaks.** The files live on GitHub's servers.
- **Instructors can leave feedback comments** directly on your work, and you can see them in the app.

### Your Personal Repository — Your Assignment Folder

For this assignment, GitHub has automatically created a personal **repository** (almost always shortened to "repo") just for you. Think of it as a folder on GitHub that belongs to you.

Your repo name looks like: **`SCIE1500-A1-S1-2026-yourusername`**

Nobody else can write to your repo — only you and your instructors. Your instructors can read it (to mark your work) and leave comments, but they cannot change your answers.

---

## Part 2: Three Concepts You Need to Understand

Before walking through the steps, let's explain three concepts that confuse almost everyone the first time. These are: **Branches**, **Commits**, and **Pull Requests**.

---

### Concept 1: Branches — "My Working Draft"

Imagine you are writing an essay. You save it as `Essay_Final.docx`. Then you keep editing, so now you have `Essay_Final_v2.docx`, `Essay_FINAL_actually_final.docx` and so on. This is a mess.

GitHub solves this with **branches**. A branch is a named, parallel version of your files.

Your repo has one permanent branch called **`main`**. Think of `main` as your "official submitted copy" — the one your instructor marks.

When you start working, GitHub (or SciQuant, automatically) creates a second branch — your **working draft**. This is where your edits live while you are still working. It doesn't affect `main` at all.

```
main ──────────────────────────────────────────────► (your submitted work, visible to markers)
         ↑ created from here
         └── work branch ─── edit ─── edit ─── edit ─── (your draft, only you see this)
```

**In SciQuant's words:** when you open your assignment in the app, it is automatically working on a branch called something like `week01-work`. You never have to create this yourself — SciQuant handles it.

**On the GitHub website:** you can see branches by clicking the branch selector dropdown near the top-left of your repo page (it usually shows "main" by default). If you have started working, you should see a second branch listed.

---

### Concept 2: Commits — "A Timestamped Snapshot with a Note"

On your laptop, you press **Ctrl+S** or **Cmd+S** to save a file. This overwrites the previous version. There is no history.

A **commit** is different. When you commit in GitHub:

- A complete snapshot of your files is saved **permanently** alongside a message you write (e.g., *"Added answer to question 3"*).
- Every commit has a unique ID (a long code like `a3f9c2d`).
- The history of all commits is always visible.

**Important:** In everyday English, "commit" means to dedicate yourself to something. In GitHub, it means the same thing — you are committing to a version of your work. You're saying: *"This is a checkpoint I want to preserve."*

**In SciQuant:** When you tap the **"Commit"** button after writing your answer, the app saves your work to GitHub with a message like *"Week 3 worksheet — yourusername"*. You will see a green confirmation. Your work is now safely stored on GitHub.

**On the GitHub website:** Under the **"Commits"** tab of your repo (or the clock icon), you can see every commit ever made — who made it, when, and what changed.

> **Key distinction:** SciQuant's "Commit" button is NOT the same as Cmd+S. Pressing Cmd+S inside a text editor just saves to your local device memory temporarily. Tapping "Commit" in SciQuant sends it permanently to GitHub. Always **Commit** when you finish a session or want to checkpoint your progress.

---

### Concept 3: Pull Requests — "I am ready for you to review my work"

Once you are happy with your work on your draft branch, you need to tell your instructor: *"Please look at my branch and make it the official version."*

This is called a **Pull Request** (often abbreviated PR). The name is confusing for beginners — you are not pulling anything. Think of it as: *"I am requesting that my draft work be pulled into the main official copy."*

A Pull Request:
- Shows the instructor exactly what changed (line by line)
- Is the official record of your submission
- Has a timestamp (so instructors know when you submitted)
- Is where instructors leave marking comments

**In SciQuant:** After committing, a banner appears offering to **"Create PR"**. Tapping this creates the Pull Request automatically. You can also tap "View on GitHub" to see it in your browser.

**On the GitHub website:** Your Pull Request appears under the **"Pull requests"** tab of your repo. You can see its status: Open (not yet marked), and later Closed or Merged (marked and finalised).

---

### Concept 4: Merging — "The Instructor Accepts and Locks In Your Submission"

When your instructor has finished reviewing your Pull Request, they **merge** it. Merging means: *"I am officially accepting this work. It now becomes the permanent `main` content."*

After merging:
- Your draft branch is closed
- The `main` branch now contains your submitted answers
- The marks/feedback in the PR comments are permanently attached

**You do not need to do anything for this step** — merging is the instructor's action. You just need to have created your Pull Request before the due date.

---

## Part 3: The Full Assignment Workflow — Step by Step

Now let's walk through the entire process from start to finish.

---

### Step 1: Connect Your GitHub Account to SciQuant

*(You only do this once for the whole semester.)*

1. Open SciQuant and tap **More** (bottom right) → **Settings** → **GitHub**.
2. Tap **"Connect GitHub Account"**.
3. SciQuant shows you a short **8-character code** (like `AB12-CD34`).
4. On any browser, go to **github.com/login/device** and type in that code.
5. Log in to GitHub (or create a free account if you don't have one).
6. Approve the access request.
7. Switch back to SciQuant — it will confirm your username is connected.

**What is happening:** SciQuant uses a secure method called "Device Flow" — the app never handles your GitHub password. You authenticate directly to GitHub's website, and GitHub gives SciQuant a secure token. This is the same method used by professional developer tools.

**On the GitHub website:** After this step, go to **github.com/settings/applications** — you will see "SciQuant" listed as an authorised app.

---

### Step 2: Find Your Assignment in the Worksheets Tab

1. In SciQuant, tap the **Worksheets** tab (second from left, the pencil icon).
2. You will see a list including your assignment (labelled "Assignment 1").
3. Tap **Assignment 1**.

**What is happening:** SciQuant is looking up your personal GitHub repo (`SCIE1500-A1-S1-2026-yourusername`) and checking what branch and files exist there. It then loads the `ANSWERS.md` file for you to edit.

**On the GitHub website:** Go to **github.com/SCIE1500-2026-S1/SCIE1500-A1-S1-2026-yourusername** and you will see the same `ANSWERS.md` file.

---

### Step 3: Write Your Answers

1. SciQuant opens a text editor showing the assignment file. Questions are already formatted — you type your answers below each question.
2. The file uses **Markdown** formatting (e.g., `**bold**`, `*italic*`, headings with `#`). You can use the **"Markdown Reference"** (book icon in the top-right of the editor) for a cheat sheet.
3. For mathematical equations, use LaTeX notation: `$x^2 + y^2$` renders as a proper equation.

**What is happening:** While you type, SciQuant is holding your text locally in memory. Nothing has been sent to GitHub yet. Think of this as the equivalent of typing in a Google Doc before you close the tab.

---

### Step 4: Commit Your Work

1. When you want to save a checkpoint, tap the **"Commit"** button (top-right of the editor).
2. A confirmation appears briefly at the bottom: *"Committed successfully — commit ID: a3f9c2d"*.
3. You can continue editing after committing. Commit as many times as you like.

**What is happening (in detail):**
- SciQuant checks whether the branch `week01-work` exists in your repo. If not, it creates it automatically.
- It retrieves the current SHA (unique ID) of the `ANSWERS.md` file from GitHub.
- It sends your new file content to GitHub via the Contents API.
- GitHub stores a permanent snapshot.

**On the GitHub website:** Go to your repo → switch branch from `main` to `week01-work` (using the branch dropdown). Your updated `ANSWERS.md` is now visible. Click **"commits"** (the clock icon) to see each commit.

> **Tip:** Commit regularly — at least after completing each question. If you accidentally type over something important, you can always ask your instructor to recover an earlier version.

---

### Step 5: Create a Pull Request (Submit Your Assignment)

1. After committing, SciQuant shows a banner: **"Work saved — Create Pull Request?"** Tap **"Create PR"**.
2. Alternatively, tap the three-dots menu (⋮) in the assignment editor and choose **"Create Pull Request"**.
3. A dialog confirms: *"Pull Request created from week01-work → main"*. Tap **"View on GitHub"** to see it in your browser.

**What is happening:**
- SciQuant calls GitHub's API to create a PR from your `week01-work` branch to `main`.
- The PR title is set automatically (e.g., *"Assignment 1 — yourusername"*).
- This PR is the official record of your submission and the channel through which you receive feedback.

**On the GitHub website:**
1. Go to your repo.
2. Click the **"Pull requests"** tab.
3. You will see your open PR. Click on it to see:
   - The **"Files changed"** tab — shows exactly what you wrote (green = added lines).
   - The **"Commits"** tab — lists every commit you made.
   - The **"Conversation"** tab — where your instructor will leave comments and your marks.

> **Important:** Creating a Pull Request does NOT "lock" your submission. You can continue to push commits to `week01-work` and they will automatically appear in the PR. The instructor marks whatever is there at the due date. So create the PR early and keep updating it.

---

### Step 6: Check for Instructor Feedback

After the due date, your instructor marks your work and leaves comments in the PR.

**In SciQuant:** Open your assignment in the Worksheets tab. If there is instructor feedback, a banner appears at the top: **"Instructor Feedback"**. Tap to expand and read the comments.

**On the GitHub website:** Go to your repo → Pull requests → your PR → **Conversation** tab. Each comment is attached to a specific line in your answer file, so you can see exactly what the instructor is referring to.

---

### Step 7: Merge (Instructor Action — Nothing Required from You)

Once marking is complete, your instructor merges the PR. You will see the status change from **Open** to **Merged** in the GitHub website.

---

## Part 4: SciQuant Is Doing a Lot for You — Here's the Full List

When you tap "Commit" or "Create PR" in SciQuant, it is silently handling all of the following steps that a developer would normally do manually in a terminal:

| What SciQuant Does Automatically | The Equivalent Manual Command |
|----------------------------------|-------------------------------|
| Creates the `week01-work` branch if it doesn't exist | `git checkout -b week01-work` |
| Checks the current file SHA to avoid overwriting conflicts | `git fetch origin` |
| Uploads your file changes to GitHub | `git add ANSWERS.md && git commit -m "..."` |
| Pushes the change to GitHub | `git push origin week01-work` |
| Creates the Pull Request | Done via GitHub website or `gh pr create` |
| Shows inline instructor comments from the PR | Viewing PR reviews on GitHub website |

---

## Part 5: Common Questions and Gotchas

---

**Q: I tapped Commit but the app showed an error saying "Conflict detected". What happened?**

This means someone (or another device of yours) committed a newer version of the file to GitHub after the version SciQuant last loaded. SciQuant is protecting you from accidentally overwriting that newer version.

The dialog offers three choices:
- **Reload** — discard your local changes and load the newer version from GitHub
- **Overwrite** — keep your local version and replace the newer GitHub version
- **Cancel** — do nothing for now

If you were working on two devices, choose **Reload** on the older device. If you are sure your current edits are the right ones, choose **Overwrite**.

---

**Q: Do I need to create the PR before the due date, or just have commits?**

You need to create the PR. Commits sitting on the `week01-work` branch without a PR are not considered a submission — they are like a draft that was never handed in. Create the PR early; you can keep editing afterward.

---

**Q: What if I forget to commit and close the app?**

SciQuant only keeps your edits in memory while the app is running. If you close the app without committing, **your unsaved edits are lost**. Commit regularly.

---

**Q: Can my classmates see my assignment answers?**

No. Your repo is private to you and the instructors. Other students cannot see it.

---

**Q: The Worksheets tab shows "unknown" for my team. What do I do?**

Tap the team name and manually type your team name (or in the case of A1, leave it — the assignment repo is individual, not team-based). SciQuant will search for your personal repo automatically.

---

**Q: I want to see what my submission looks like right now. How?**

Go to your repo on the GitHub website → click the **`week01-work`** branch → click `ANSWERS.md`. You will see your file rendered nicely (Markdown is displayed as formatted text on GitHub).

---

## Summary: The Assignment Workflow at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│  1. Connect GitHub account (once only)                      │
│  2. Open Assignment in Worksheets tab                       │
│  3. Write answers in the editor                             │
│  4. Tap COMMIT  ──► snapshot saved to GitHub (assignment-    │
│                      work branch)                           │
│     (Repeat steps 3–4 as many times as you like)           │
│  5. Tap CREATE PR  ──► official submission created          │
│     (Continue editing and committing — PR updates itself)  │
│  6. Read instructor feedback in PR conversation             │
│  7. Instructor MERGES PR ──► submission finalised           │
└─────────────────────────────────────────────────────────────┘
```

---

## Appendix: Glossary

| Term | Plain English Meaning |
|------|-----------------------|
| **Repository (Repo)** | Your personal assignment folder on GitHub |
| **Branch** | A parallel version of your files (draft vs official) |
| **`main` branch** | The official version — what your instructor marks |
| **`week01-work` branch** | Your working draft — created automatically by SciQuant |
| **Commit** | A permanently saved, timestamped snapshot of your work |
| **Commit message** | A short note describing what you changed (*"Answered Q1 and Q2"*) |
| **Commit SHA** | The unique ID code for a specific commit (e.g., `a3f9c2d`) |
| **Pull Request (PR)** | A request to merge your draft into the official version — equivalent to "submit" |
| **Merge** | Accepting a PR and making the draft the new official version (done by instructor) |
| **Conflict** | Two versions of the same file have contradictory changes — must be resolved |
| **GitHub** | The cloud service that hosts your repo and manages all version history |
| **SciQuant** | The app that connects to GitHub and makes all the above happen without a terminal |

---

*Last updated: March 2026 | SCIE1500 Teaching Team*
