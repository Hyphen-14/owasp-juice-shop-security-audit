#!/usr/bin/env python3
"""
OWASP Juice Shop AppSec Portfolio - Progress Tracker Automation
Calculates completion percentage across challenge tiers and updates scorecard tables.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
CHALLENGES_DIR = DOCS_DIR / "challenges"

TIER_TOTALS = {
    1: 15,
    2: 18,
    3: 23,
    4: 22,
    5: 16,
    6: 8
}

TOTAL_CHALLENGES = sum(TIER_TOTALS.values())

def count_completed_challenges():
    completed_per_tier = {i: 0 for i in range(1, 7)}
    all_completed = []

    for tier_num in range(1, 7):
        tier_dir = CHALLENGES_DIR / f"tier-{tier_num}"
        if not tier_dir.exists():
            continue
        
        # Any .md file other than index.md is treated as a completed writeup
        for file in tier_dir.glob("*.md"):
            if file.name.lower() != "index.md":
                completed_per_tier[tier_num] += 1
                all_completed.append((tier_num, file.name))

    total_completed = sum(completed_per_tier.values())
    return completed_per_tier, total_completed, all_completed

def main():
    completed_per_tier, total_completed, all_completed = count_completed_challenges()
    overall_percentage = (total_completed / TOTAL_CHALLENGES) * 100

    print("==================================================")
    print(" [🛡️] OWASP Juice Shop Portfolio Progress Tracker")
    print("==================================================")
    print(f"Total Completed: {total_completed} / {TOTAL_CHALLENGES} ({overall_percentage:.1f}%)")
    print("--------------------------------------------------")
    for tier in range(1, 7):
        count = completed_per_tier[tier]
        total = TIER_TOTALS[tier]
        pct = (count / total) * 100
        print(f" Tier {tier} (★ x {tier}): {count:2d} / {total:2d} ({pct:5.1f}%)")
    print("==================================================")

if __name__ == "__main__":
    main()

