#!/usr/bin/env python3
"""
CLI helper for Gula VPN & Clash Installation Skill
"""

import argparse
import json
import sys
from gula_checker import GulaChecker
from clash_installer import print_platform_guide, load_clash_resources


def main():
    parser = argparse.ArgumentParser(description="Gula VPN & Clash Guide CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    # check-site
    subparsers.add_parser("check-site", help="Check connectivity to 古拉.com website")

    # check-sub
    p_sub = subparsers.add_parser("check-sub", help="Validate a Clash subscription link")
    p_sub.add_argument("--url", required=True, help="Clash subscription URL")

    # client-info
    p_client = subparsers.add_parser("client", help="Show Clash download links for platform")
    p_client.add_argument("--platform", choices=["windows", "macos", "android", "ios", "all"], default="windows")

    args = parser.parse_args()

    if args.command == "check-site":
        checker = GulaChecker()
        res = checker.check_site_accessibility()
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif args.command == "check-sub":
        checker = GulaChecker()
        res = checker.verify_clash_subscription(args.url)
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif args.command == "client":
        if args.platform == "all":
            for p in ["windows", "macos", "android", "ios"]:
                print_platform_guide(p)
        else:
            print_platform_guide(args.platform)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
