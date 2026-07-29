#!/usr/bin/env python3
"""
Multi-Agent Bridge & Sync Tool (skill-bridge)
Modeled after dbs-bridge in dbskill
"""

import argparse
import os
import shutil
import sys

HOME = os.path.expanduser("~")
DEFAULT_TARGET = os.path.join(HOME, ".agents", "skills")


def sync_skills(target_dir: str = DEFAULT_TARGET, force: bool = False):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    skills_dir = os.path.join(root_dir, "skills")

    print("==========================================")
    print("      Skill System Multi-Agent Bridge     ")
    print("==========================================")
    print(f"Source Directory: {skills_dir}")
    print(f"Target Directory: {target_dir}\n")

    os.makedirs(target_dir, exist_ok=True)

    synced = 0
    for item in sorted(os.listdir(skills_dir)):
        src = os.path.join(skills_dir, item)
        dst = os.path.join(target_dir, item)

        if os.path.isdir(src) and os.path.isfile(os.path.join(src, "SKILL.md")):
            if os.path.exists(dst):
                if force:
                    shutil.rmtree(dst)
                else:
                    print(f"  [SKIP] {item} (already exists at target)")
                    continue

            shutil.copytree(src, dst)
            print(f"  [SYNCED] {item} -> {dst}")
            synced += 1

    print(f"\n✅ Bridge Sync Complete. Synced {synced} skills to {target_dir}.")


def main():
    parser = argparse.ArgumentParser(description="Bridge Sync Tool for Multi-Agent Environment")
    parser.add_argument("--target", default=DEFAULT_TARGET, help="Target skills folder")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing skills")
    parser.add_argument("--status", action="store_true", help="Check sync status")

    args = parser.parse_args()

    if args.status:
        print(f"Bridge Target Path: {args.target}")
        print(f"Exists: {os.path.exists(args.target)}")
    else:
        sync_skills(target_dir=args.target, force=args.force)


if __name__ == "__main__":
    main()
