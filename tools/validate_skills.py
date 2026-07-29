#!/usr/bin/env python3
"""
Skill Specification & Frontmatter Validator (Linter)
Modeled after dbskill validation system
"""

import os
import re
import sys
import yaml
from typing import Dict, List, Tuple


def validate_skill_folder(skill_path: str) -> Tuple[bool, List[str]]:
    errors = []
    skill_name = os.path.basename(skill_path)
    skill_md = os.path.join(skill_path, "SKILL.md")

    if not os.path.isfile(skill_md):
        errors.append(f"Missing SKILL.md in {skill_name}")
        return False, errors

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse YAML frontmatter
    if not content.startswith("---"):
        errors.append(f"{skill_name}/SKILL.md does not start with YAML frontmatter '---'")
        return False, errors

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_name}/SKILL.md invalid YAML frontmatter format")
        return False, errors

    yaml_str = parts[1]
    try:
        data = yaml.safe_load(yaml_str)
        if not isinstance(data, dict):
            errors.append(f"{skill_name}/SKILL.md frontmatter is not a dictionary")
        else:
            if "name" not in data:
                errors.append(f"{skill_name}/SKILL.md frontmatter missing 'name'")
            if "description" not in data:
                errors.append(f"{skill_name}/SKILL.md frontmatter missing 'description'")
    except Exception as e:
        errors.append(f"{skill_name}/SKILL.md YAML parse error: {e}")

    return len(errors) == 0, errors


def main():
    root_dir = os.path.join(os.path.dirname(__file__), "..")
    skills_dir = os.path.join(root_dir, "skills")

    if not os.path.isdir(skills_dir):
        print(f"[!] Skills directory not found: {skills_dir}")
        sys.exit(1)

    print("==========================================")
    print("      Skill System Linter & Validator      ")
    print("==========================================")

    total = 0
    passed = 0
    all_errors = []

    for item in sorted(os.listdir(skills_dir)):
        item_path = os.path.join(skills_dir, item)
        if os.path.isdir(item_path):
            total += 1
            ok, errors = validate_skill_folder(item_path)
            if ok:
                passed += 1
                print(f"  ✅ [PASS] {item}")
            else:
                print(f"  ❌ [FAIL] {item}")
                for err in errors:
                    print(f"      - {err}")
                    all_errors.append(err)

    print(f"\nResult: {passed}/{total} skills passed validation.")
    if all_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
