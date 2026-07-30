#!/usr/bin/env python3
"""
CLI helper for API Relay Monetization Skill (/sk-api-relay)
"""

def main():
    print("==================================================")
    print("  物理真实开源大模型 API 中转站搭建助手 (/sk-api-relay)")
    print("==================================================")
    print("\n【1. 物理真实开源项目与分工】")
    print("  • Sub2API (sub2api/sub2api): 订阅号池转 API 平台，处理 Session/RefreshToken 轮询与协议转换")
    print("  • New-API (calciumion/new-api): 企业级大模型聚合网关，负责多节点聚合与 CDK 计费")
    print("\n【2. 海外 VPS 选型对比避坑 (为什么不选 AWS/GCP/Azure?)】")
    print("  • 传统 VPS (RackNerd / Cloudcone / Vultr): 预付费固定账单 ($10-$20/年)，流量耗尽即停，零天价扣费风险")
    print("  • 公有云巨头 (AWS / GCP / Azure): 按量+出网流量费极贵 ($0.10/GB)，绑卡遭攻击易透支破产，且 IP 易遭 403 风控")
    print("\n【3. AI 驱动部署与 CDK 发卡】")
    print("  • AI 驱动部署: 提示 AI Agent 自动安装 Docker, Caddy SSL 证书并部署 Sub2API 容器")
    print("  • 联动发卡: 联动小铺 / 发卡网卖 CDK 兑换码 ➔ 用户后台兑换额度")
    print("  • 成本定价: 总成本 = VPS月费 + 域名 + Plus账号采购 + 住宅IP代理费")

if __name__ == "__main__":
    main()
