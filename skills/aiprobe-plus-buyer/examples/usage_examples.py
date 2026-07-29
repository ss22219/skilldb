#!/usr/bin/env python3
"""
Usage Examples for AIProbe Plus Buyer & SMS Channel Skill
"""

import sys
import os

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))

from aiprobe_fetcher import AIProbeFetcher
from sms_verifier import SMSClient

def example_fetch_cheapest_plus():
    print("=== Example 1: Fetch Top 3 Cheapest In-Stock ChatGPT Plus Items ===")
    fetcher = AIProbeFetcher()
    items = fetcher.fetch_plus_products(in_stock_only=True, sort_by="price_asc")
    
    print(f"Total matching in-stock items: {len(items)}")
    for item in items[:3]:
        print(f"• [{item['category_type']}] ¥{item['price']} | 店铺: {item['shop']} | 库存: {item['stock']}")
        print(f"  商品名称: {item['name']}")
        print(f"  直达链接: {item['buy_link']}\n")

def example_sms_verification_flow():
    print("=== Example 2: SMS Verification OTP Channel Flow ===")
    # Set your SMS provider API Key in environment or parameter
    api_key = os.getenv("SMS_API_KEY", "DEMO_API_KEY")
    client = SMSClient(provider="sms-activate", api_key=api_key)
    
    balance = client.get_balance()
    print(f"SMS Account Balance Check: {balance}")
    
    # Note: Rented numbers cost real balance
    # success, act_id, phone = client.get_number(service="openai", country="0")
    # if success:
    #     print(f"Got number: +{phone} (ID: {act_id})")
    #     ok, code = client.get_code(act_id, wait_seconds=60)
    #     print(f"Received OTP: {code}")

if __name__ == "__main__":
    example_fetch_cheapest_plus()
    example_sms_verification_flow()
