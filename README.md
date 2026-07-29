# SkillDB System — 面向开发者与业务创作者的开源 AI Skills 工具箱

[简体中文](README.md) | [English](README.md)

> 模仿 [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) 构建的高可扩展、模块化 AI Skill 操作系统与知识库引擎。
> 把真实业务、开发部署、内容策划与行动卡点交给 Agent，获得清晰判决与可以立刻执行的下一步。

支持 Agent 平台：**Antigravity / Claude Code / Codex / WorkBuddy / Trae / 豆包** 等所有支持 Skill 规范的 Agent。

---

## 🌟 核心理念与工作流

你不需要事先掌握复杂的套路，也不需要记忆繁多的技能命令。只需输入 `/sk` 加你的需求，路由器会自动识别上下文并调度最契合的专业 Skill。

```mermaid
flowchart TD
    A[用户输入 /sk 需求] --> B[sk 智能主路由器]
    B --> C{选择专业能力 Skill}
    C -->|商业/产品/定价卡点| D[/sk-diagnosis 商业诊断]
    C -->|爆款选题/Hook/文案| E[/sk-content 内容策划]
    C -->|标杆/竞品模式拆解| F[/sk-benchmark 竞品拆解]
    C -->|重大选择/下行风险| G[/sk-decision 决策框架]
    C -->|RAG知识检索| H[/sk-knowledge 知识库]
    C -->|低价Plus采购与接码| I[/aiprobe-plus-buyer]
    C -->|机场与Clash客户端安装| J[/gula-vpn-clash-guide]
    C -->|ChatGPT全平台部署| K[/chatgpt-installer-skill]
```

---

## ⚡️ 快速开始

在 Agent 终端或聊天框中直接使用：

### 1. 智能路由唤醒 (`/sk`)
```text
/sk 我做面向宝妈的收纳咨询，客户总觉得贵，我该怎么调整？
```

### 2. 显式调用具体技能
```text
/sk-diagnosis    我做少儿编程课，已经有 40 个付费学员，但续费率很低。我该调整什么？
/sk-content      我想讲“普通人别急着做个人 IP”，这个选题怎样做成高完播率脚本？
/sk-benchmark    我想研究企业服务内容账号，应该找哪些对标？
/sk-decision     我想离职出来做全职 AI 顾问，如何评估下行风险？
/sk-knowledge    帮我把这个文件夹变成知识库，以后直接搜索。
/aiprobe-plus-buyer      抓取当前最低价的 ChatGPT Plus 会员并准备接码。
/gula-vpn-clash-guide    指引如何订阅古拉.com 并安装 Windows/macOS Clash 客户端。
/chatgpt-installer-skill  突破 Windows 区域限制一键安装官方 ChatGPT 桌面版。
```

---

## 🧩 技能全目录

| 技能指令 | 技能名称 | 目录路径 | 说明 |
| :--- | :--- | :--- | :--- |
| **`/sk`** | **主路由器** | [skills/sk-router](skills/sk-router) | **总调度引擎，自动识别上下文并分发最适合的技能** |
| `/sk-diagnosis` | 商业诊断 | [skills/sk-diagnosis](skills/sk-diagnosis) | 深度诊断产品、PMF 客群匹配、定价与续费瓶颈 |
| `/sk-content` | 内容策划 | [skills/sk-content](skills/sk-content) | 爆款前 3 秒 Hook、情绪共鸣与转化文案脚本 |
| `/sk-benchmark` | 竞品拆解 | [skills/sk-benchmark](skills/sk-benchmark) | 拆解标杆账号选题池、视觉符号与变现路径 |
| `/sk-decision` | 战略决策 | [skills/sk-decision](skills/sk-decision) | 基于 MVP 第一原理与下行风险评估重大商业选择 |
| `/sk-knowledge` | 知识库 | [skills/sk-knowledge](skills/sk-knowledge) | 结构化原子库 (atoms.jsonl) 检索与本地挂载 |
| `/sk-bridge` | 多Agent桥接 | [skills/sk-bridge](skills/sk-bridge) | 自动将 Skills 同步至各种 Agent 技能目录 |
| `/aiprobe-plus-buyer` | Plus会员与接码采购 | [skills/aiprobe-plus-buyer](skills/aiprobe-plus-buyer) | 自动抓取 aiprobe.top 低价商品并对接 SMS 接码 |
| `/gula-vpn-clash-guide` | 机场与Clash指南 | [skills/gula-vpn-clash-guide](skills/gula-vpn-clash-guide) | 引导订阅古拉.com 及全平台安装 Clash 客户端 |
| `/chatgpt-installer-skill` | ChatGPT全平台部署 | [skills/chatgpt-installer-skill](skills/chatgpt-installer-skill) | 突破区域限制安装 Windows 桌面版及 macOS DMG |

---

## 🧠 结构化知识库系统 (`知识库/`)

本系统内嵌了结构化知识原子库，用于 RAG 检索与底层推理：
- **原子库 (`知识库/原子库/atoms.jsonl`)**: JSONL 格式的模块化知识点，方便导入 Qdrant / Ollama 向量库。
- **说明文档 (`知识库/README.md`)**: 介绍知识库架构与向量检索使用方法。

---

## 🛠️ 构建与维护工具链 (`tools/`)

开发或新增 Skill 后，使用项目内置工具链进行校验与自动化打包：

```bash
cd tools/

# 1. 运行 Linter 检查所有 Skill 的规范与 YAML 前置定义
python validate_skills.py

# 2. 打包生成发布目录 dist/skills/
python build_skills.py

# 3. 桥接同步至系统全局 Agent 目录 (~/.agents/skills)
python bridge_sync.py
```

---

## 📂 项目结构

```
skilldb/
├── skills/                     # 核心 Skill 库 (各技能包含 SKILL.md 与脚本)
│   ├── sk-router/              # 智能分发路由器
│   ├── sk-diagnosis/           # 商业诊断技能
│   ├── sk-content/             # 内容策划技能
│   ├── sk-benchmark/           # 竞品拆解技能
│   ├── sk-decision/            # 战略决策技能
│   ├── sk-knowledge/           # 知识库管理技能
│   ├── sk-bridge/              # 跨 Agent 桥接技能
│   ├── aiprobe-plus-buyer/     # 低价 Plus 会员与接码技能
│   ├── gula-vpn-clash-guide/   # 机场与 Clash 全指南技能
│   └── chatgpt-installer-skill/# ChatGPT 全平台安装技能
├── 知识库/                     # 结构化知识原子库与方法论
│   ├── 原子库/                 # atoms.jsonl 知识原子数据
│   └── README.md
├── docs/                       # 新手入门与全目录文档
│   └── 新手入门.md
├── tools/                      # 构建、校验与同步工具链
│   ├── validate_skills.py      # SKILL.md 规范校验器
│   ├── build_skills.py         # 自动打包构建脚本
│   └── bridge_sync.py          # 跨 Agent 同步桥接工具
├── .claude-plugin/             # Claude Code 插件市场配置
│   └── marketplace.json
├── VERSION                     # 版本号
├── LICENSE                     # CC BY-NC 4.0 许可证
└── README.md                   # 仓库主说明文档
```

---

## 📄 许可证

本项目采用 [CC BY-NC 4.0](LICENSE) 许可证。个人使用、学习研究与非商业项目均可自由免费使用。
