#!/usr/bin/env python3
"""
CLI tool for AIProbe Plus Procurement & SMS Verification Channel
"""

import argparse
import json
import sys
from aiprobe_fetcher import AIProbeFetcher
from sms_verifier import SMSClient


def cmd_fetch(args):
    fetcher = AIProbeFetcher(timeout=args.timeout)
    print(f"[*] Fetching Plus products from aiprobe.top (Sort: {args.sort}, Max Price: {args.max_price or 'Any'})...")
    
    results = fetcher.fetch_plus_products(
        in_stock_only=not args.all,
        min_price=args.min_price,
        max_price=args.max_price,
        category_filter=args.category,
        sort_by=args.sort,
    )
    
    if args.json:
        print(json.dumps(results[: args.limit], ensure_ascii=False, indent=2))
        return

    print(f"\n[+] Found {len(results)} matching Plus items. Showing top {min(len(results), args.limit)}:\n")
    print(f"{'#':<3} | {'分类':<10} | {'价格(元)':<8} | {'库存':<6} | {'店铺':<14} | {'商品名称':<40} | {'购买链接'}")
    print("-" * 120)
    
    for idx, item in enumerate(results[: args.limit], 1):
        price_str = f"¥{item['price']:.2f}"
        name_str = item['name'][:38] + ".." if len(item['name']) > 40 else item['name']
        shop_str = item['shop'][:12] + ".." if len(item['shop']) > 14 else item['shop']
        print(f"{idx:<3} | {item['category_type']:<10} | {price_str:<8} | {item['stock']:<6} | {shop_str:<14} | {name_str:<40} | {item['buy_link']}")


def cmd_sms_balance(args):
    client = SMSClient(provider=args.provider, api_key=args.api_key)
    res = client.get_balance()
    print(f"[SMS Balance] {res}")


def cmd_sms_get_number(args):
    client = SMSClient(provider=args.provider, api_key=args.api_key)
    print(f"[*] Requesting number for service='{args.service}', country='{args.country}'...")
    success, act_id, phone = client.get_number(service=args.service, country=args.country)
    
    if success:
        print(f"\n[+] Successfully rented number!")
        print(f"    Activation ID: {act_id}")
        print(f"    Phone Number:  +{phone}")
        print(f"\nUse `python cli.py sms get-code --id {act_id}` to retrieve SMS code.")
    else:
        print(f"\n[-] Error: {phone}")


def cmd_sms_get_code(args):
    client = SMSClient(provider=args.provider, api_key=args.api_key)
    print(f"[*] Waiting for SMS verification code for ID '{args.id}' (Timeout: {args.wait}s)...")
    success, code = client.get_code(args.id, wait_seconds=args.wait)
    
    if success:
        print(f"\n[+] SMS OTP Code Received: {code}")
    else:
        print(f"\n[-] Failed: {code}")


def main():
    parser = argparse.ArgumentParser(description="AIProbe Plus Member Procurement & SMS Verification CLI")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    # fetch subcommand
    p_fetch = subparsers.add_parser("fetch", help="Fetch low-price Plus membership items from aiprobe.top")
    p_fetch.add_argument("--limit", type=int, default=15, help="Number of items to show (default: 15)")
    p_fetch.add_argument("--min-price", type=float, default=None, help="Minimum price filter")
    p_fetch.add_argument("--max-price", type=float, default=None, help="Maximum price filter")
    p_fetch.add_argument("--category", type=str, default=None, help="Category filter (e.g. 成品号, 代充/直充, 兑换码)")
    p_fetch.add_argument("--sort", choices=["price_asc", "price_desc", "stock_desc"], default="price_asc", help="Sort order")
    p_fetch.add_argument("--all", action="store_true", help="Include out-of-stock items")
    p_fetch.add_argument("--json", action="store_true", help="Output in raw JSON format")
    p_fetch.add_argument("--timeout", type=int, default=8, help="API timeout in seconds")

    # sms subcommand
    p_sms = subparsers.add_parser("sms", help="SMS verification channel operations")
    p_sms_sub = p_sms.add_subparsers(dest="sms_action")

    # sms balance
    p_sms_bal = p_sms_sub.add_parser("balance", help="Check SMS account balance")
    p_sms_bal.add_argument("--provider", default="sms-activate", help="SMS Provider (sms-activate / 5sim)")
    p_sms_bal.add_argument("--api-key", default=None, help="API key for SMS provider")

    # sms get-number
    p_sms_num = p_sms_sub.add_parser("get-number", help="Rent a phone number for OpenAI verification")
    p_sms_num.add_argument("--service", default="openai", help="Service code (openai / dr)")
    p_sms_num.add_argument("--country", default="0", help="Country code (e.g. 0=Russia, 12=USA, 22=India)")
    p_sms_num.add_argument("--provider", default="sms-activate", help="SMS Provider")
    p_sms_num.add_argument("--api-key", default=None, help="API key for SMS provider")

    # sms get-code
    p_sms_code = p_sms_sub.add_parser("get-code", help="Retrieve SMS OTP code for rented number")
    p_sms_code.add_argument("--id", required=True, help="Activation ID")
    p_sms_code.add_argument("--wait", type=int, default=120, help="Max wait time in seconds")
    p_sms_code.add_argument("--provider", default="sms-activate", help="SMS Provider")
    p_sms_code.add_argument("--api-key", default=None, help="API key for SMS provider")

    args = parser.parse_args()

    if args.command == "fetch":
        cmd_fetch(args)
    elif args.command == "sms":
        if args.sms_action == "balance":
            cmd_sms_balance(args)
        elif args.sms_action == "get-number":
            cmd_sms_get_number(args)
        elif args.sms_action == "get-code":
            cmd_sms_get_code(args)
        else:
            p_sms.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
