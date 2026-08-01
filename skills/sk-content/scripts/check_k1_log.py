#!/usr/bin/env python3
"""Validate daily and course-level K1 observation practice logs."""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


REQUIRED = {
    "date",
    "url",
    "creator",
    "source",
    "like_reason",
    "mechanism",
    "mission",
    "modality",
    "deep_analysis",
}


def load_rows(path):
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise SystemExit(f"第 {line_number} 行不是有效 JSON：{error}") from error
        missing = sorted(REQUIRED - set(row))
        if missing:
            raise SystemExit(f"第 {line_number} 行缺少字段：{', '.join(missing)}")
        rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description="检查 K1 内容观察日志")
    parser.add_argument("log", type=Path)
    parser.add_argument("--daily-likes", type=int, default=20)
    parser.add_argument("--daily-deep", type=int, default=3)
    parser.add_argument("--course-days", type=int, default=20)
    args = parser.parse_args()

    if not args.log.is_file():
        raise SystemExit(f"找不到日志：{args.log}")

    rows = load_rows(args.log)
    by_date = defaultdict(list)
    for row in rows:
        by_date[str(row["date"])].append(row)

    daily = {}
    qualified_days = 0
    for date, items in sorted(by_date.items()):
        deep_count = sum(bool(item["deep_analysis"]) for item in items)
        passed = len(items) >= args.daily_likes and deep_count >= args.daily_deep
        qualified_days += int(passed)
        daily[date] = {
            "liked": len(items),
            "deep": deep_count,
            "passed": passed,
        }

    report = {
        "total_observations": len(rows),
        "deep_analyses": sum(bool(row["deep_analysis"]) for row in rows),
        "recorded_days": len(by_date),
        "qualified_days": qualified_days,
        "course_days_required": args.course_days,
        "course_process_pass": qualified_days >= args.course_days,
        "source_distribution": Counter(str(row["source"]) for row in rows),
        "mechanism_distribution": Counter(str(row["mechanism"]) for row in rows),
        "mission_distribution": Counter(str(row["mission"]) for row in rows),
        "modality_distribution": Counter(str(row["modality"]) for row in rows),
        "daily": daily,
        "note": "脚本只检查训练过程，K1 晋级仍需人工评审观察质量、规则卡和迁移能力",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
