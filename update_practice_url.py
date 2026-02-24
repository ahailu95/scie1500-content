#!/usr/bin/env python3
"""
Update course_config.json to add remote URL for Week 1 practice questions
and bump version to 2.4.6
"""

import json
from datetime import datetime, timezone, timedelta

# Read current config
with open('course_config.json', 'r') as f:
    config = json.load(f)

# Update Week 1 exercises URL to remote GitHub raw URL
week1 = config['weeklyResources']['1']
for exercise in week1['exercises']:
    if exercise['id'] == 'w1_practice':
        # Keep asset:// for now since app doesn't support remote yet
        # But add a remoteUrl field for future use
        exercise['remoteUrl'] = 'https://raw.githubusercontent.com/ahailu95/scie1500-content/main/SCIE1500Materials/Week_1/week1_practice.json'
        print(f"✓ Added remoteUrl to {exercise['id']}")
        print(f"  Remote: {exercise['remoteUrl']}")

# Bump version to 2.4.6
old_version = config['version']
config['version'] = '2.4.6'

# Update timestamp (Perth is UTC+8)
perth_tz = timezone(timedelta(hours=8))
config['lastUpdated'] = datetime.now(perth_tz).isoformat()

# Write updated config
with open('course_config.json', 'w') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print(f"\n✓ Version updated: {old_version} → {config['version']}")
print(f"✓ Timestamp: {config['lastUpdated']}")
print(f"\n⚠️  NOTE: App code needs updates to load practice questions from remoteUrl")
print(f"   Old builds will still use bundled assets only.")
