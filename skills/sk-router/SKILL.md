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
    C -->|业务卡点/定价/转化低| D[/sk-diagnosis 商业诊断]
    C -->|选题/短视频/文案爆款| E[/sk-content 内容策划]
    C -->|对标账号/竞品模式| F[/sk-benchmark 竞品拆解]
    C -->|重大选择/风险评估| G[/sk-decision 决策框架]
    C -->|查找资料/知识整理| H[/sk-knowledge 知识库]
    C -->|购买Plus/接码需求| I[/aiprobe-plus-buyer]
    C -->|机场/VPN/Clash安装| J[/gula-vpn-clash-guide]
    C -->|ChatGPT客户端部署| K[/chatgpt-installer-skill]
```

---

## 核心功能规范

1. **自动识别与分发**：根据用户输入的材料（如：“我的课程定价 299，但转化率很低”），匹配 `/sk-diagnosis` 商业诊断。
2. **多轮引导**：在一轮分析产出后，提示用户下一步可调用的子技能（如：“已完成商业诊断，接下来可以使用 `/sk-content` 产出高转化文案”）。

---

## 使用示例

```bash
# 智能分析
/sk 我做面向宝妈的收纳咨询，客户总觉得贵，我该怎么调整？

# 系统会自动转接至 /sk-diagnosis 技能并输出精准诊断矩阵
```
