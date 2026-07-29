#!/usr/bin/env python3
"""
Build & Packaging Tool for SkillDB System
Modeled after dbskill build-skills.sh
"""

import json
import os
import shutil
import sys
from typing import Dict, List


def build_skills_package():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    skills_dir = os.path.join(root_dir, "skills")
    dist_dir = os.path.join(root_dir, "dist", "skills")

    print(f"[*] Building Skill System release package...")
    print(f"    Source: {skills_dir}")
    print(f"    Target: {dist_dir}")

    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)

    os.makedirs(dist_dir, exist_ok=True)

    manifest = {"skills": [], "total_count": 0}

    for item in sorted(os.listdir(skills_dir)):
        if item.startswith("beta") or item.startswith("."):
            continue

        item_path = os.path.join(skills_dir, item)
        if os.path.isdir(item_path) and os.path.isfile(os.path.join(item_path, "SKILL.md")):
            target_path = os.path.join(dist_dir, item)
            shutil.copytree(item_path, target_path)
            manifest["skills"].append(item)
            manifest["total_count"] += 1
            print(f"  + Bundled skill: {item}")

    manifest_file = os.path.join(dist_dir, "manifest.json")
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Build complete! Total skills packaged: {manifest['total_count']}")
    print(f"   Manifest created: {manifest_file}")


if __name__ == "__main__":
    build_skills_package()
