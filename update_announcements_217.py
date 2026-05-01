import json
from datetime import datetime

with open('announcements.json', 'r') as f:
    data = json.load(f)

# Update the previously added announcement to v2.1.7 and include the split view feature
for announcement in data.get('announcements', []):
    if announcement.get('id') == 'sciquant-update-v2.1.0':
        announcement['id'] = 'sciquant-update-v2.1.7'
        announcement['title'] = '🚀 SciQuant App Update – Version 2.1.7 is Live!'
        announcement['message'] = "The app has been updated with a **much better Markdown editing facility featuring a split window with live view**, alongside a few other quality-of-life improvements to the file editor:\n\n• 📝 **Split Window / Live View:** See your Markdown formatting update in real-time as you type, making it easier than ever to structure your work.\n• 💡 **Help & Guide added directly in the menu:** Tap the **⋮** menu at any time for a quick walkthrough of the editor buttons, step tracking, and how to commit and submit your work.\n• 📋 **Clarified Submission Process:** The \"How to Submit\" guide now clearly distinguishes between individual assignments and group work expectations.\n• 🛠️ **Formatting Fix:** The \"Common Formatting Mistakes\" section in the Markdown Cheat Sheet now displays correctly.\n• 🎯 **Smarter Progress Tracking:** The step tracker at the top of the editor now accurately reflects your live progress in the flow (e.g., *Commit* lights up once you've saved, and *Submit* lights up once a PR is open).\n\n**Action Required:** Please download and install version 2.1.7. No other action is required to keep your work synced."
        break

data['version'] = '2.4.1'
data['lastUpdated'] = '2026-04-30T10:15:00+08:00'

with open('announcements.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

