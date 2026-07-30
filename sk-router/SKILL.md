---
name: sk
description: 智能主分发路由 Skill (/sk)。自动读取当前对话上下文、用户业务卡点或任务意图，精准推荐或分发至最适合的子 Skill。
---

# 主分发路由器 Skill (/sk)

`sk` 是 Skill System 的总指挥与调度路由器。用户无需提前了解几十个具体 Skill 的名称，只需在命令前加 `/sk`，它会自动读取当前对话信息并匹配最适合的专业分析 Skill。

---

## 🧭 路由逻辑架构

```mermaid
flowchart TD
    A[用户输入 /sk + 任务/问题/材料] --> B[意图识别与上下文分析]
    B --> C{识别痛点类型}
    C -->|小白国内使用Codex从零到一| D[/sk-codex-beginner]
    C -->|小白入门通关流程指南| E[/sk-starter]
    C -->|购买Plus/接码需求| F[/aiprobe-plus-buyer]
    C -->|机场/VPN/Clash安装| G[/gula-vpn-clash-guide]
    C -->|ChatGPT客户端部署| H[/chatgpt-installer-skill]
    C -->|重大选择/风险评估| I[/sk-decision 决策框架]
    C -->|查找资料/知识整理| J[/sk-knowledge 知识库]
```

---

## 核心功能规范

1. **自动识别与分发**：根据用户输入的材料（如：“我是小白，想在 Windows 上安装 ChatGPT 和使用 Codex”），匹配相应通关 Skill。
2. **多轮引导**：在一轮分析产出后，提示用户下一步可调用的子技能（如：“网络代理已配置完成，接下来可以使用 `/chatgpt-installer-skill` 安装桌面客户端”）。

---

## 使用示例

```bash
# 智能分析
/sk 我是国内小白，想从零开始配置 ChatGPT 和使用 Codex 编程，怎么操作？

# 系统会自动转接至 /sk-codex-beginner 技能并输出极简通关路线
```
