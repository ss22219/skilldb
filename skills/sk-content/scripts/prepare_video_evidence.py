#!/usr/bin/env python3
"""Extract metadata, review frames, audio, and a manifest from a video."""

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


def run(command):
    return subprocess.run(command, check=True, capture_output=True, text=True)


def probe(path):
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    return json.loads(result.stdout)


def frame_times(duration, maximum):
    anchors = [0.5, 1.5, 3.0]
    if duration > 3:
        remaining = max(0, maximum - len(anchors))
        for index in range(1, remaining + 1):
            anchors.append(3 + (duration - 3) * index / (remaining + 1))
    return sorted({round(min(value, max(duration - 0.05, 0)), 3) for value in anchors if value < duration})


def loudness(path):
    result = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(path),
            "-af",
            "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
            "-f",
            "null",
            "-",
        ],
        capture_output=True,
        text=True,
    )
    matches = re.findall(r'\{\s*"input_i".*?\}', result.stderr, re.DOTALL)
    if not matches:
        return None
    try:
        data = json.loads(matches[-1])
    except json.JSONDecodeError:
        return None
    return {
        "integrated_lufs": data.get("input_i"),
        "true_peak_dbfs": data.get("input_tp"),
        "loudness_range_lu": data.get("input_lra"),
        "threshold_lufs": data.get("input_thresh"),
    }


def main():
    parser = argparse.ArgumentParser(description="准备短视频多模态评审证据")
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--max-frames", type=int, default=12)
    args = parser.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"找不到视频：{args.input}")
    for executable in ("ffmpeg", "ffprobe"):
        if not shutil.which(executable):
            raise SystemExit(f"缺少依赖：{executable}")
    if args.max_frames < 3:
        raise SystemExit("--max-frames 不能小于 3")

    args.out.mkdir(parents=True, exist_ok=True)
    frames_dir = args.out / "frames"
    frames_dir.mkdir(exist_ok=True)
    metadata = probe(args.input)
    duration = float(metadata.get("format", {}).get("duration", 0))
    streams = metadata.get("streams", [])
    video_stream = next((item for item in streams if item.get("codec_type") == "video"), None)
    audio_stream = next((item for item in streams if item.get("codec_type") == "audio"), None)
    if not video_stream or duration <= 0:
        raise SystemExit("输入文件没有可分析的视频流")

    frames = []
    for index, timestamp in enumerate(frame_times(duration, args.max_frames), start=1):
        frame_path = frames_dir / f"frame-{index:02d}-{timestamp:.3f}s.jpg"
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-ss",
                str(timestamp),
                "-i",
                str(args.input),
                "-frames:v",
                "1",
                "-q:v",
                "2",
                str(frame_path),
            ]
        )
        frames.append({"timestamp_s": timestamp, "path": str(frame_path.resolve())})

    audio_path = None
    audio_metrics = None
    if audio_stream:
        extracted_audio = args.out / "speech-16k-mono.wav"
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(args.input),
                "-vn",
                "-ac",
                "1",
                "-ar",
                "16000",
                str(extracted_audio),
            ]
        )
        audio_path = str(extracted_audio.resolve())
        audio_metrics = loudness(args.input)

    manifest = {
        "source": str(args.input.resolve()),
        "duration_s": duration,
        "video": {
            "codec": video_stream.get("codec_name"),
            "width": video_stream.get("width"),
            "height": video_stream.get("height"),
            "frame_rate": video_stream.get("avg_frame_rate"),
        },
        "audio": {
            "present": bool(audio_stream),
            "codec": audio_stream.get("codec_name") if audio_stream else None,
            "sample_rate": audio_stream.get("sample_rate") if audio_stream else None,
            "channels": audio_stream.get("channels") if audio_stream else None,
            "extracted_path": audio_path,
            "metrics": audio_metrics,
        },
        "frames": frames,
        "next_steps": [
            "对关键帧执行视觉多模态分析",
            "对音轨执行带词级时间戳的语音转录",
            "按时间码完成制作层与结果层评分",
        ],
    }
    manifest_path = args.out / "evidence-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(manifest_path.resolve())


if __name__ == "__main__":
    main()
