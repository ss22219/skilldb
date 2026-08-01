#!/usr/bin/env python3
"""Score the craft layer of a short-form video."""

import argparse
import json


DIMENSIONS = {
    "script": "文案与信息",
    "visual": "视觉表达",
    "audio": "音频质量",
    "performance": "声音与镜头表现",
    "integration": "音画协同",
}


def parse_args():
    parser = argparse.ArgumentParser(description="短视频多模态制作层评分器")
    for key, label in DIMENSIONS.items():
        parser.add_argument(f"--{key}", type=float, required=True, help=f"{label}，0-20")
    parser.add_argument("--audio-unintelligible", action="store_true")
    parser.add_argument("--visual-unusable", action="store_true")
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
    scores = {}
    for key, label in DIMENSIONS.items():
        value = getattr(args, key)
        if value < 0 or value > 20:
            raise SystemExit(f"{label}必须在 0-20 之间")
        scores[label] = value

    raw_total = sum(scores.values())
    cap = 100
    if args.audio_unintelligible or args.visual_unusable:
        cap = 59
    total = min(raw_total, cap)
    result = {
        "craft_score": total,
        "craft_grade": grade(total),
        "scores": scores,
        "gates": {
            "audio_intelligible": not args.audio_unintelligible,
            "visual_usable": not args.visual_unusable,
        },
        "note": "制作层分数不能替代注意力、同频、信任、成交与 IP 的结果层评分",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
