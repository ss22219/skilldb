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
    print("  • New-API (calciumion/new-api): 企业级大模型聚合网关，负责多节点聚合、多渠道重试与 CDK 计费")
    print("  • One-API (songquanpeng/one-api): 经典 LLM 分发系统")
    print("  • CLI Proxy API (router-protocol): 命令行代理转接 API 工具")
    print("  ⚠️ 避坑澄清: 彻底摒弃与 AI 无关的电商插件 (如 Shop2API)")
    print("\n【2. 架构演进路线】")
    print("  • 初级阶段: 单节点 Sub2API 挂载 1-3 个 Plus 订阅号池")
    print("  • 高级阶段: 部署多节点 Sub2API / CLI Proxy API ➔ 统一接入 New-API 聚合网关")
    print("\n【3. 海外 VPS 与 AI 驱动部署】")
    print("  • 服务器购买: 推荐海外免备案 VPS (RackNerd / Cloudcone / Vultr，轻量 1核1-2G)")
    print("  • AI 驱动部署: 提示 AI Agent 自动安装 Docker, Caddy SSL 证书并部署 Sub2API 容器")
    print("\n【4. CDK 发卡与成本评估】")
    print("  • 发卡模式: 联动小铺 / 发卡网卖 CDK 兑换码 ➔ 用户后台直接兑换额度")
    print("  • 成本评估: 总成本 = VPS月费 + 域名 + Plus账号采购 + 住宅IP代理费")
    print("  • 定价策略: 算准保本单价，选择 10% 薄利跑大流水模式或高毛利模式")

if __name__ == "__main__":
    main()
