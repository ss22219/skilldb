#!/usr/bin/env python3
"""
CLI helper for API Relay Monetization Skill (/sk-api-relay)
"""

def main():
    print("==================================================")
    print("  大模型 API 中转站搭建与商业变现助手 (/sk-api-relay)")
    print("==================================================")
    print("\n【1. 核心开源组件与架构演进】")
    print("  • 核心组件: sub2api / Shop2API (号池管理与转接) + cli-proxy-api")
    print("  • 新手架构: 单个 sub2api 节点挂载 Plus 账号池")
    print("  • 进阶架构: 多个 sub2api/cli-proxy-api 节点 ➔ New-API 统一路由网关")
    print("\n【2. 海外服务器与 AI 辅助部署】")
    print("  • 服务器购买: 推荐海外免备案 VPS (RackNerd / Cloudcone / Vultr，轻量 1核1-2G)")
    print("  • AI 驱动部署: 提示 AI Agent 自动安装 Docker, Caddy SSL 证书并部署 sub2api")
    print("\n【3. CDK 发卡与收单模式】")
    print("  • 推荐模式: 联动小铺 / 发卡网售卖 CDK 兑换码 ➔ 用户后台直接兑换额度")
    print("\n【4. 运维成本评估与科学定价】")
    print("  • 成本公式: 总成本 = VPS月费 + 域名 + Plus账号采购 + 住宅IP代理费")
    print("  • 售卖定价: 根据预估月度总成本推算保本单价，设置 10% 薄利或高毛利倍率")

if __name__ == "__main__":
    main()
