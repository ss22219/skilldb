#!/usr/bin/env python3
"""Calculate a mission-aware SkillDB content score."""

import argparse
import json


AXES = {
    "attention": "注意力",
    "resonance": "同频",
    "trust": "信任",
    "conversion": "成交",
    "ip": "IP 积累",
}

WEIGHTS = {
    "reach": {"attention": 0.35, "resonance": 0.25, "trust": 0.15, "conversion": 0.10, "ip": 0.15},
    "community": {"attention": 0.15, "resonance": 0.40, "trust": 0.20, "conversion": 0.05, "ip": 0.20},
    "trust": {"attention": 0.10, "resonance": 0.15, "trust": 0.45, "conversion": 0.10, "ip": 0.20},
    "conversion": {"attention": 0.10, "resonance": 0.10, "trust": 0.30, "conversion": 0.40, "ip": 0.10},
    "ip": {"attention": 0.10, "resonance": 0.20, "trust": 0.25, "conversion": 0.05, "ip": 0.40},
    "balanced": {"attention": 0.20, "resonance": 0.20, "trust": 0.20, "conversion": 0.20, "ip": 0.20},
}

MISSION_NAMES = {
    "reach": "获量",
    "community": "同频",
    "trust": "信任",
    "conversion": "成交",
    "ip": "IP",
    "balanced": "综合",
}

PASS_LINES = {
    level: 80 for level in range(1, 13)
}


def parse_args():
    parser = argparse.ArgumentParser(description="内容创作者 K12 多目标评分器")
    parser.add_argument("--mission", choices=WEIGHTS, default="balanced")
    for key, label in AXES.items():
        parser.add_argument(f"--{key}", type=float, required=True, help=f"{label}得分，0-20")
    parser.add_argument("--target-level", type=int, choices=range(1, 13))
    parser.add_argument("--audience-fail", action="store_true")
    parser.add_argument("--mission-fail", action="store_true")
    parser.add_argument("--promise-fail", action="store_true")
    parser.add_argument("--integrity-fail", action="store_true")
    return parser.parse_args()


def grade(total):
    if total >= 90:
        return "S"
    if total >= 80:
        return "A"
    if total >= 70:
        return "B"
    if total >= 60:
        return "C"
    return "D"


def main():
    args = parse_args()
    raw_scores = {}
    for key, label in AXES.items():
        value = getattr(args, key)
        if value < 0 or value > 20:
            raise SystemExit(f"{label}必须在 0-20 之间")
        raw_scores[key] = value

    weighted = sum(raw_scores[key] * WEIGHTS[args.mission][key] for key in AXES) * 5
    cap = 100
    if args.audience_fail or args.mission_fail:
        cap = min(cap, 59)
    if args.promise_fail:
        cap = min(cap, 69)
    goal_fit = min(weighted, cap)
    integrity_pass = not args.integrity_fail

    result = {
        "mission": MISSION_NAMES[args.mission],
        "goal_fit_score": round(goal_fit, 1),
        "grade": grade(goal_fit),
        "axis_scores": {AXES[key]: raw_scores[key] for key in AXES},
        "gates": {
            "audience": not args.audience_fail,
            "mission": not args.mission_fail,
            "promise": not args.promise_fail,
            "integrity": integrity_pass,
        },
    }

    if args.target_level:
        pass_line = PASS_LINES[args.target_level]
        axis_pass = all(value >= 10 for value in raw_scores.values())
        result["promotion"] = {
            "target_level": f"K{args.target_level}",
            "pass_line": pass_line,
            "score_pass": goal_fit >= pass_line,
            "axis_pass": axis_pass,
            "content_gate_pass": goal_fit >= pass_line and axis_pass and integrity_pass,
            "note": "这里只判断作品门槛；晋级还需满足本级过程证据并通过 AI 动态考试",
        }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
