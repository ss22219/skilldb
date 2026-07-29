#!/usr/bin/env python3
"""
Clash Client Installation & Download Helper
"""

import json
import os
from typing import Dict, List

RESOURCES_FILE = os.path.join(os.path.dirname(__file__), "..", "resources", "clash_download_links.json")


def load_clash_resources() -> Dict:
    with open(RESOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def print_platform_guide(platform: str = "windows"):
    resources = load_clash_resources()
    plat = platform.lower()
    items = resources.get(plat) or []

    print(f"\n==========================================")
    print(f"  Clash 客户端安装指南 [{plat.upper()}]")
    print(f"==========================================")

    for item in items:
        print(f"\n📌 推荐软件: {item.get('name')}")
        if item.get('description'):
            print(f"   说明: {item.get('description')}")
        if item.get('download_url'):
            print(f"   官方发布页面: {item.get('download_url')}")
        if item.get('direct_installer'):
            print(f"   Windows 64位安装包: {item.get('direct_installer')}")
        if item.get('direct_dmg'):
            print(f"   macOS 安装包: {item.get('direct_dmg')}")
        if item.get('app_store_url'):
            print(f"   App Store 地址: {item.get('app_store_url')}")


if __name__ == "__main__":
    print_platform_guide("windows")
    print_platform_guide("macos")
