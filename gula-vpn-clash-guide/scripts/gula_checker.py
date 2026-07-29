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

# Domain punycode mapping
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
        """Check accessibility of 古拉.com and Punycode domain."""
        target_urls = [
            f"https://{DOMAIN_PUNYCODE}/",
            f"http://{DOMAIN_PUNYCODE}/",
        ]
        
        results = {
            "domain_raw": DOMAIN_RAW,
            "domain_punycode": DOMAIN_PUNYCODE,
            "accessible": False,
            "details": []
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        for url in target_urls:
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                    status = r.status
                    content_len = len(r.read())
                    results["accessible"] = True
                    results["details"].append({
                        "url": url,
                        "status": status,
                        "content_length": content_len,
                        "message": "Connected successfully."
                    })
                    break
            except Exception as e:
                results["details"].append({
                    "url": url,
                    "status": 0,
                    "error": str(e),
                    "message": "Connection failed."
                })

        return results

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
                # Check headers for traffic userinfo
                user_info_hdr = r.headers.get("subscription-userinfo") or r.headers.get("Subscription-Userinfo")
                if user_info_hdr:
                    # Format: upload=xxx; download=xxx; total=xxx; expire=xxx
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
                
                # Rough count of proxies in Clash YAML
                if "proxies:" in body or "Proxy:" in body:
                    result["valid"] = True
                    # Estimate proxies count
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
    print("=== Checking 古拉.com Accessibility ===")
    res = checker.check_site_accessibility()
    print(json.dumps(res, ensure_ascii=False, indent=2))
