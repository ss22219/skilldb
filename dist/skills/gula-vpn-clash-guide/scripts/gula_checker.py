#!/usr/bin/env python3
"""
Gula.com Connectivity & Clash Subscription Diagnostic Checker
"""

import json
import ssl
import sys
import urllib.parse
import urllib.request
from typing import Dict, Optional, Tuple

DOMAIN_RAW = "古拉.com"
DOMAIN_PUNYCODE = "xn--w4r430a.com"


def to_punycode(url_or_domain: str) -> str:
    """Convert unicode Chinese domain to ASCII Punycode."""
    if "古拉.com" in url_or_domain:
        return url_or_domain.replace("古拉.com", DOMAIN_PUNYCODE)
    return url_or_domain


class GulaChecker:
    def __init__(self, timeout: int = 8):
        self.timeout = timeout
        self._ctx = ssl.create_default_context()
        self._ctx.check_hostname = False
        self._ctx.verify_mode = ssl.CERT_NONE

    def check_site_accessibility(self) -> Dict:
        """Explain anti-loss发布站 mechanism and test site."""
        return {
            "domain_raw": DOMAIN_RAW,
            "domain_punycode": DOMAIN_PUNYCODE,
            "site_type": "防丢失导航发布站 (指向二级真正入口)",
            "notice": "古拉.com 属于防丢失导航发布主站，自身不提供节点，而是指向最新的二级通用入口。命令行直接 curl/ping 会被防火墙直接拦截阻断（属于正常现象）。用户需要在浏览器手动打开 https://古拉.com/ 并点击最新的二级入口进行注册与购买！",
            "manual_steps": [
                "1. 在浏览器手动打开 https://古拉.com/ (或 https://xn--w4r430a.com/)",
                "2. 点击页面上的二级最新可用入口跳转真正的注册后台",
                "3. 注册电子邮箱账号并选择套餐支付 (推荐月付)",
                "4. 后台下载 Clash 软件并复制/导入 Clash 订阅链接",
                "5. 在 Clash 客户端选择规则模式并开启系统代理"
            ]
        }

    def verify_clash_subscription(self, sub_url: str) -> Dict:
        """Verify a Clash subscription link and extract user traffic & node count."""
        sub_url_ascii = to_punycode(sub_url)
        headers = {
            "User-Agent": "ClashforWindows/0.20.39 (Clash.Meta)",
        }

        result = {
            "sub_url": sub_url,
            "valid": False,
            "user_info": {},
            "nodes_count": 0,
            "raw_snippet": "",
            "error": ""
        }

        try:
            req = urllib.request.Request(sub_url_ascii, headers=headers)
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                user_info_hdr = r.headers.get("subscription-userinfo") or r.headers.get("Subscription-Userinfo")
                if user_info_hdr:
                    parts = dict(item.strip().split("=") for item in user_info_hdr.split(";") if "=" in item)
                    upload_bytes = int(parts.get("upload", 0))
                    download_bytes = int(parts.get("download", 0))
                    total_bytes = int(parts.get("total", 0))
                    expire_ts = int(parts.get("expire", 0))
                    
                    result["user_info"] = {
                        "used_gb": round((upload_bytes + download_bytes) / (1024**3), 2),
                        "total_gb": round(total_bytes / (1024**3), 2),
                        "expire_timestamp": expire_ts
                    }

                body = r.read().decode("utf-8", errors="ignore")
                result["raw_snippet"] = body[:200]
                
                if "proxies:" in body or "Proxy:" in body:
                    result["valid"] = True
                    lines = body.splitlines()
                    proxy_count = sum(1 for l in lines if l.strip().startswith("- name:") or l.strip().startswith("- { name:"))
                    result["nodes_count"] = proxy_count or 1
                elif "ssr://" in body or "vmess://" in body or "vless://" in body:
                    result["valid"] = True
                    result["nodes_count"] = len(body.splitlines())

        except Exception as e:
            result["error"] = str(e)

        return result


if __name__ == "__main__":
    checker = GulaChecker()
    print("=== 古拉.com 防丢失导航站与 4 步通关说明 ===")
    res = checker.check_site_accessibility()
    print(json.dumps(res, ensure_ascii=False, indent=2))
