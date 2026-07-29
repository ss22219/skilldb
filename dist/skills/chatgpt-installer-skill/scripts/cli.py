#!/usr/bin/env python3
"""
CLI entry point for ChatGPT Installer Skill
"""

import argparse
from chatgpt_installer import ChatGPTInstaller


def main():
    parser = argparse.ArgumentParser(description="ChatGPT Desktop Official Cross-Platform Installer")
    parser.add_argument("--os", choices=["windows", "macos", "auto"], default="auto", help="Target OS")
    parser.add_argument("--msix-path", default="", help="Path to local .msixbundle file (Windows offline installation)")

    args = parser.parse_args()
    installer = ChatGPTInstaller()

    if args.os == "windows":
        installer.run_windows_installer(msix_path=args.msix_path)
    elif args.os == "macos":
        installer.run_macos_installer()
    else:
        installer.auto_install()


if __name__ == "__main__":
    main()
