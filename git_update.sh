#!/bin/bash

# Navigate to your project directory
cd /Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators

# Add all new or modified files to staging
git add .

# Commit changes with a timestamp
git commit -m "Auto-update $(date)"

# Push to GitHub
git push origin master