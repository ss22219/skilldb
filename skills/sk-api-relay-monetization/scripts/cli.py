#!/usr/bin/env python3
"""
CLI helper for API Relay Monetization Skill
"""

import sys

def main():
    print("==================================================")
    print("  大模型 API 中转站搭建与商业变现助手 (/sk-api-relay)")
    print("==================================================")
    print("\n【阶段一：基础设施】")
    print("  • 核心推荐引擎: New-API (基于 Docker 一键部署)")
    print("  • Docker 命令: docker compose up -d (端口: 3000)")
    print("\n【阶段二：渠道与套利计算】")
    print("  • 成本套利: 上游采购约 0.3元/$ 额度 ➔ 零售 1.2-2.0元/$ 额度")
    print("  • 利润率: 60% - 80%")
    print("\n【阶段三：发卡与自动销售】")
    print("  • 生成额度兑换码 ➔ 上架发卡网自动充值 ➔ 生成 sk-xxx Key")
    print("\n【阶段四：风控防刷】")
    print("  • 开启单令牌 QPS 速率控制与渠道降级重试")

if __name__ == "__main__":
    main()
