#!/usr/bin/env python3
"""
Cross-Platform ChatGPT Desktop Installer Helper
Detects OS and drives installer execution for macOS (DMG) and Windows (Winget / MSIXBundle).
"""

import json
import os
import platform
import subprocess
import sys
from typing import Dict

METADATA_FILE = os.path.join(os.path.dirname(__file__), "..", "resources", "installer_metadata.json")


def load_metadata() -> Dict:
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


class ChatGPTInstaller:
    def __init__(self):
        self.os_type = platform.system().lower()  # 'windows', 'darwin', 'linux'
        self.metadata = load_metadata()

    def print_system_info(self):
        print(f"[*] Detected Operating System: {platform.system()} ({platform.release()})")

    def run_macos_installer(self, download: bool = False):
        mac_meta = self.metadata["macos"]
        dmg_url = mac_meta["official_url"]
        
        print("\n==========================================")
        print("  macOS ChatGPT 桌面版官方安装指南")
        print("==========================================")
        print(f"官方离线 DMG 下载链接:\n  {dmg_url}\n")
        print("安装步骤:")
        print("1. 点击以上链接下载 ChatGPT.dmg 文件")
        print("2. 双击打开 ChatGPT.dmg 挂载磁盘镜像")
        print("3. 将 ChatGPT.app 拖入 Applications (应用程序) 文件夹即可完成安装\n")
        print("命令行快捷挂载与安装命令:")
        print(f"  curl -O {dmg_url}")
        print("  hdiutil attach ChatGPT.dmg")
        print("  cp -R '/Volumes/ChatGPT/ChatGPT.app' /Applications/")
        print("  hdiutil detach /Volumes/ChatGPT")

    def run_windows_installer(self, msix_path: str = ""):
        win_meta = self.metadata["windows"]
        store_id = win_meta["store_product_id"]
        winget_cmd = win_meta["winget_cmd"]

        print("\n==========================================")
        print("  Windows ChatGPT 桌面版安装与解锁指南")
        print("==========================================")
        print("🛑 关键前提（解决“在你所在的地区不可用”限制）:")
        print("  1. 按键盘 Win + I 打开 Windows 设置")
        print("  2. 定位到 “时间及语言” -> “区域”")
        print("  3. 将 “国家或地区” 下拉菜单修改为 “美国” (United States)\n")

        print("方法一：使用 Winget 命令（官方推荐一键安装）:")
        print("  以管理员身份打开 PowerShell / 终端，运行以下命令:")
        print(f"  {winget_cmd}\n")

        print("方法二：离线抓包手动安装 (.msixbundle):")
        print(f"  1. 打开在线抓包网站: {win_meta['rg_adguard_url']}")
        print(f"  2. 下拉选 ProductId，搜索框输入产品 ID: {store_id}，右侧选 Retail 搜索")
        print("  3. 找到以 .msixbundle 结尾的文件（约 200MB+）并下载")
        print("  4. 在管理员 PowerShell 中运行命令进行部署:")
        print("     Add-AppxPackage -Path \"C:\\路径\\下载的文件.msixbundle\"\n")

        ps_script = os.path.join(os.path.dirname(__file__), "install_windows_chatgpt.ps1")
        if self.os_type == "windows":
            print(f"[*] 也可以自动运行内置 PowerShell 脚本:")
            print(f"  powershell -ExecutionPolicy Bypass -File \"{ps_script}\"")

    def auto_install(self):
        self.print_system_info()
        if self.os_type == "darwin":
            self.run_macos_installer()
        elif self.os_type == "windows":
            self.run_windows_installer()
        else:
            print("\n[!] Linux 当前官方未提供原生桌面客户端，建议使用 Web 端或 Linux CLI 工具。")
            print("各平台元数据摘要:")
            print(json.dumps(self.metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    installer = ChatGPTInstaller()
    installer.auto_install()
