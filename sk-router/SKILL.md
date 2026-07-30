---
name: sk
description: 智能主分发路由 Skill (/sk)。自动读取当前对话上下文，精准分发至最适合的通关 Skill。
---

# 主分发路由器 Skill (/sk)

`sk` 是 Skill System 的总指挥与调度路由器。用户无需记忆具体的 Skill 名称，只需在命令前加 `/sk`，系统会自动调度最契合的通关 Skill。

---

## 🧭 路由逻辑架构

```mermaid
flowchart TD
    subgraph router ["路由器调度引擎"]
        A[用户输入 /sk 需求] --> B[sk 智能主路由器]
        B --> C{选择专业能力 Skill}
        C -->|API 中转站搭建与变现| D["/sk-api-relay"]
        C -->|小白国内使用Codex从零到一| E["/sk-codex-beginner"]
        C -->|小白入门通关流程指南| F["/sk-starter"]
        C -->|低价Plus采购与同店接码| G["/aiprobe-plus-buyer"]
        C -->|机场与Clash客户端安装| H["/gula-vpn-clash-guide"]
        C -->|ChatGPT全平台部署| I["/chatgpt-installer-skill"]
    end
```

---

## 核心功能规范

1. **自动识别与分发**：根据用户输入的描述，匹配相应的通关 Skill。
2. **多轮引导**：在完成某一阶段操作后，提示下一步可调用的子技能（如：搭建中转站后，引导使用 `/aiprobe-plus-buyer` 采购渠道）。

---

## 使用示例

```bash
# 智能分析中转站变现
/sk 想搭建一个大模型 API 中转站卖 key 赚钱，怎么操作？

# 系统转接至 /sk-api-relay 并输出从部署到发卡的全套路线
```
