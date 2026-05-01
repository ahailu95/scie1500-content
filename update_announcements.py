import json
from datetime import datetime

with open('announcements.json', 'r') as f:
    data = json.load(f)

new_announcement = {
    "id": "sciquant-update-v2.1.0",
    "title": "🚀 SciQuant App Update – Version 2.1.0 is Live!",
    "message": "The app has been updated with a **much better markdown editing facility featuring a split window with live view**, alongside a few other quality-of-life improvements to the file editor:\n\n• 💡 **Help & Guide added directly in the menu:** Tap the **⋮** menu at any time for a quick walkthrough of the editor buttons, step tracking, and how to commit and submit your work.\n• 📝 **Clarified Submission Process:** The \"How to Submit\" guide now clearly distinguishes between individual assignments and group work expectations.\n• 🛠️ **Formatting Fix:** The \"Common Formatting Mistakes\" section in the Markdown Cheat Sheet now displays correctly.\n• 🎯 **Smarter Progress Tracking:** The step tracker at the top of the editor now accurately reflects your live progress in the flow.\n\n**Action Required:** Please download and install version 2.1.0. No other action is required to keep your work synced.",
    "publishedAt": "2026-04-30T10:00:00+08:00",
    "priority": "important",
    "category": "general",
    "isPinned": True
}

data["version"] = "2.4.0"
data["lastUpdated"] = "2026-04-30T10:00:00+08:00"
data["announcements"].insert(0, new_announcement)

with open('announcements.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

