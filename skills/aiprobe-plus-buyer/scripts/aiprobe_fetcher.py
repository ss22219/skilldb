#!/usr/bin/env python3
"""
AIProbe Plus Product Fetcher
Fetch and filter ChatGPT Plus membership products from https://aiprobe.top/
"""

import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Union

BASE_URL = "https://aiprobe.top"
WEB_PASS_URL = f"{BASE_URL}/api/web_pass"
QUICK_DATA_URL = f"{BASE_URL}/api/data_quick?q=plus"
INITIAL_DATA_URL = f"{BASE_URL}/data.initial.json"

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "X-AIPROBE-Client": "web",
    "Referer": f"{BASE_URL}/",
}

# Exclusion rules as per aiprobe.top website logic
EXCLUSION_PATTERN = re.compile(
    r"(?:不是|非|不含|可升级|可开|媲美)plus|99%?开plus|开plus|提链|提炼|扫码|二维码|提取|助手|free|免费|普号|普通号|icloud",
    re.IGNORECASE,
)


class AIProbeFetcher:
    """Fetcher class for querying low-price Plus products from aiprobe.top"""

    def __init__(self, timeout: int = 8):
        self.timeout = timeout
        self.pass_token: str = "public"
        self._ctx = ssl.create_default_context()
        self._ctx.check_hostname = False
        self._ctx.verify_mode = ssl.CERT_NONE

    def _get_web_pass(self) -> str:
        """Fetch the web pass token required for API requests."""
        try:
            req = urllib.request.Request(
                f"{WEB_PASS_URL}?_={int(time.time()*1000)}",
                headers=DEFAULT_HEADERS,
            )
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                res = json.loads(r.read().decode("utf-8"))
                if res.get("token"):
                    self.pass_token = str(res["token"])
        except Exception:
            self.pass_token = "public"
        return self.pass_token

    def _is_valid_plus_item(self, item: Dict) -> bool:
        """Check if an item is a genuine ChatGPT Plus product."""
        name = str(item.get("name") or "")
        category = str(item.get("category") or "")
        combined = f"{name} {category}"
        
        compact = re.sub(r"[\s\"'“”‘’「」『』【】()[\]{}<>《》|｜·•,，。:：;；!！?？_—–-]+", "", combined.lower())
        
        if EXCLUSION_PATTERN.search(compact):
            return False
            
        if "plus" not in compact and "gpt-4" not in compact and "gpt4" not in compact:
            return False
            
        return True

    def _categorize_product(self, item: Dict) -> str:
        """Categorize item into:成品号, 代充/直充, 兑换码, 团队/Pro"""
        name = (item.get("name") or "").lower()
        cat = (item.get("category") or "").lower()
        combined = f"{name} {cat}"

        if any(k in combined for k in ["代充", "直充", "充值", "官方充"]):
            return "代充/直充"
        elif any(k in combined for k in ["兑换码", "礼品卡", "cdk", "激活码", "卡密"]):
            return "兑换码/卡密"
        elif any(k in combined for k in ["team", "团队", "pro", "商业版"]):
            return "团队/Pro号"
        elif any(k in combined for k in ["成品", "独享", "共享", "首登", "账号", "月卡"]):
            return "成品号"
        else:
            return "其他Plus商品"

    def fetch_plus_products(
        self,
        in_stock_only: bool = True,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        category_filter: Optional[str] = None,
        sort_by: str = "price_asc",
    ) -> List[Dict]:
        """
        Fetch ChatGPT Plus products.
        sort_by: 'price_asc', 'price_desc', 'stock_desc'
        """
        token = self._get_web_pass()
        headers = dict(DEFAULT_HEADERS)
        headers["X-AIPROBE-Pass"] = token

        raw_items = []

        # Attempt 1: Quick data endpoint
        try:
            req = urllib.request.Request(QUICK_DATA_URL, headers=headers)
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                res = json.loads(r.read().decode("utf-8"))
                raw_items = res.get("items") or []
        except Exception:
            raw_items = []

        # Fallback Attempt 2: Initial data endpoint
        if not raw_items:
            try:
                req = urllib.request.Request(INITIAL_DATA_URL, headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as r:
                    res = json.loads(r.read().decode("utf-8"))
                    raw_items = res.get("items") or []
            except Exception as e:
                raise RuntimeError(f"Failed to fetch data from AIProbe: {e}")

        # Process and filter items
        filtered = []
        for item in raw_items:
            if not self._is_valid_plus_item(item):
                continue

            price = float(item.get("price", 0))
            stock = item.get("stock", 0)
            
            # Stock check
            is_in_stock = stock != 0 and stock != "0" and str(stock).lower() != "out of stock"
            if in_stock_only and not is_in_stock:
                continue

            # Price check
            if min_price is not None and price < min_price:
                continue
            if max_price is not None and price > max_price:
                continue

            cat_type = self._categorize_product(item)
            if category_filter and category_filter not in cat_type and cat_type not in category_filter:
                continue

            cleaned_item = {
                "id": item.get("id"),
                "name": item.get("name"),
                "price": price,
                "stock": stock if is_in_stock else 0,
                "in_stock": is_in_stock,
                "category_type": cat_type,
                "shop": item.get("shop", "未知店铺"),
                "shop_link": item.get("shop_link", ""),
                "buy_link": item.get("link", ""),
                "source_site": item.get("source_site", ""),
                "last_seen": item.get("last_seen_at", ""),
            }
            filtered.append(cleaned_item)

        # Sorting
        if sort_by == "price_asc":
            filtered.sort(key=lambda x: x["price"])
        elif sort_by == "price_desc":
            filtered.sort(key=lambda x: x["price"], reverse=True)
        elif sort_by == "stock_desc":
            filtered.sort(key=lambda x: (int(x["stock"]) if str(x["stock"]).isdigit() else 0), reverse=True)

        return filtered


if __name__ == "__main__":
    fetcher = AIProbeFetcher()
    results = fetcher.fetch_plus_products(in_stock_only=True)
    print(f"Fetched {len(results)} valid in-stock Plus items from AIProbe.")
    for item in results[:5]:
        print(f"[{item['category_type']}] ¥{item['price']} | 库存:{item['stock']} | {item['shop']} - {item['name'][:40]}")
        print(f"   Buy: {item['buy_link']}")
