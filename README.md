# SkillDB System — 面向“想学习 AI 变现人群”的开源 AI Skills 通关工具箱

[简体中文](README.md) | [English](README.md)

支持 Agent 平台：**Antigravity / Claude Code / Codex / WorkBuddy / Trae / 豆包** 等所有支持 Skill 规范的 Agent。

---

## 🎯 系统核心定位：聚焦“AI 变现”全生命周期

本 Skill 系统专为**想要学习 AI 变现的人群**（独立开发者、AI 副业创作者、自媒体引流者、Solo Founder）打造，帮助用户从 **0 到 1 破除基建门槛**（网络代理、软件安装、账号采购与接码验证），顺利开启 AI 变现之路。

```mermaid
flowchart TD
    subgraph router ["路由器调度引擎"]
        A[用户输入 /sk 需求] --> B[sk 智能主路由器]
        B --> C{选择专业能力 Skill}
        C -->|小白国内使用Codex从零到一| D["/sk-codex-beginner"]
        C -->|小白入门通关流程指南| E["/sk-starter"]
        C -->|低价Plus采购与同店接码| F["/aiprobe-plus-buyer"]
        C -->|机场与Clash客户端安装| G["/gula-vpn-clash-guide"]
        C -->|ChatGPT全平台部署| H["/chatgpt-installer-skill"]
    end
```

---

## 📦 技能库安装与更新指南 (Installation & Update Guide)

### 1. 快捷一键安装 (Installation)

#### 方式 A：Git Clone 本地挂载 (推荐所有 Agent 平台)
```bash
# 1. 克隆 Skill 仓库
git clone https://github.com/ss22219/skilldb.git

# 2. 挂载或复制 skills/ 目录至 Agent 技能路径
# Antigravity 路径: ~/.gemini/antigravity/skills/
# Claude Code 路径:  ~/.claude/skills/
```

#### 方式 B：Claude Code / Codex 插件源挂载
```bash
/plugin add https://github.com/ss22219/skilldb
```

---

### 2. 保持最新更新 (Update)

当 Skill 仓库（如 Plus 排除规则或最新下载链接）发生更新时，在本地仓库目录中运行：

```bash
cd skilldb
git pull origin main

# (可选) 一键同步 Skills 至系统全局 Agent 目录
python tools/bridge_sync.py
```

---

## ⚡️ 快速开始

在 Agent 终端或聊天框中直接使用：

### 1. 智能路由唤醒 (`/sk`)
```text
/sk 我是国内小白，想从零开始配置 ChatGPT 和使用 Codex 编程，怎么操作？
```

### 2. 显式调用具体技能
```text
/sk-codex-beginner       国内小白使用 Codex 的全流程通关指南
/sk-starter              新手入门 3 步通关基础教程
/aiprobe-plus-buyer      抓取 aiprobe.top 纯净低价 Plus 账号与 Codex 1元短信接码卡密
/gula-vpn-clash-guide    访问古拉防丢失发布站与全平台 Clash 配置指导
/chatgpt-installer-skill 安装 Windows / macOS ChatGPT 桌面版客户端
```

---

## 🧩 核心技能目录 (Core Skills Catalog)

| 技能标识 (Skill ID) | 推荐指令 | 核心功能与避坑细节说明 |
| :--- | :--- | :--- |
| **`sk-router`** | `/sk` | **主分发路由器**：智能识别用户意图并自动匹配调度最优 Skill。 |
| **`sk-codex-beginner`** | `/sk-codex-beginner` | **国内小白 Codex 从零到一通关指南**：说明网络解锁、Windows 区域改美国、以及在同一卡密平台购买 Codex 1元接码服务全流程。 |
| **`sk-starter`** | `/sk-starter` | **新手 3 步通关指南**：从 0 到 1 引导网络代理配置、客户端部署与账号采购。 |
| **`aiprobe-plus-buyer`** | `/aiprobe-plus-buyer` | **ChatGPT Plus / Codex 采购与同店接码**：实时抓取 `aiprobe.top` 数据，自动过滤 `提链/提炼/扫码/free/普号/icloud`，支持直接买账号与同一店铺买接码服务。 |
| **`gula-vpn-clash-guide`**| `/gula-vpn-clash-guide` | **古拉 VPN 与 Clash 配置指南**：说明 `古拉.com` 作为**防丢失导航发布主站**的机制（需手动在浏览器点开获取二级入口），并提供 4 步完整配置指导。 |
| **`chatgpt-installer-skill`**| `/chatgpt-installer-skill` | **ChatGPT 桌面版跨平台安装**：解决 Windows 微软商店“在所在地区不可用”问题（修改区域为美国 + Winget `9NT1R1C2HH7J` / `.msixbundle` 离线包）。 |

---

## 📖 新手教程关键细节摘录

### 1. 网络配置细节 (古拉防丢失主站 + 4 步法)
- **主站性质**：`https://古拉.com/` (`xn--w4r430a.com`) 为防丢失导航发布站，主站不直接提供节点，而是**指向最新二级入口**。必须由用户在浏览器手动打开点开跳转！
- **4 步配置**：手动打开获取二级入口 -> 注册邮箱并选择套餐（**强烈建议按月订阅**） -> 下载 Clash Verge Rev 软件并导入订阅 -> 切换 **规则模式 (Rule)** 并开启 **系统代理 (System Proxy)**。

### 2. Windows 客户端安装突破限制细节
- **修改系统区域**：按 **Win + I** 打开设置 -> **时间及语言** -> **区域** -> 将国家修改为 **美国 (United States)**（即时生效，解决商店搜不到或不可用）。
- **管理员 PowerShell 安装**：运行 `winget install --id=9NT1R1C2HH7J -e`。

### 3. 买号与 Codex 短信接码细节
- **过滤排除规则**：系统自动剔除 `提链`、`提炼`、`扫码`、`二维码`、`free`、`免费`、`普号`、`icloud`、`非Plus` 等干扰项。
- **同一平台同一店铺接码**：小白无需注册国外接码网站，在 `https://aiprobe.top/` 同一个店铺（如 *一梦AI*、*ai小头*、*奥特曼严选* 等）即可像买卡密一样直接购买 Codex 短信接码服务（单次约 1 元左右）。

---

## 🛠️ 构建与维护工具链 (`tools/`)

开发或新增 Skill 后，使用项目内置工具链进行校验与自动化打包：

```bash
cd tools/

# 1. 运行 Linter 检查所有 Skill 的规范与 YAML 前置定义
python validate_skills.py

# 2. 打包生成发布目录 dist/skills/
python build_skills.py
```

---

## 📂 项目结构

```
skilldb/
├── skills/                     # 核心 6 大实战 Skill 库
│   ├── sk-router/              # 智能分发路由器 (/sk)
│   ├── sk-codex-beginner/      # 国内小白 Codex 0到1通关指南 (/sk-codex-beginner)
│   ├── sk-starter/             # 新手 3 步入门指南 (/sk-starter)
│   ├── aiprobe-plus-buyer/     # 低价 Plus 会员与同店接码采购 (/aiprobe-plus-buyer)
│   ├── gula-vpn-clash-guide/   # 防丢失机场与 Clash 全平台配置 (/gula-vpn-clash-guide)
│   └── chatgpt-installer-skill/# ChatGPT 桌面版全平台部署与区域突破 (/chatgpt-installer-skill)
├── docs/                       # 新手入门与通关教程文档
│   ├── 新手入门.md
│   └── 新手教程.md
├── tools/                      # 构建与校验工具链
│   ├── validate_skills.py      # SKILL.md 规范校验器
│   └── build_skills.py         # 自动打包构建脚本
├── .claude-plugin/             # Claude Code 插件市场配置
│   └── marketplace.json
├── VERSION                     # 版本号
├── LICENSE                     # CC BY-NC 4.0 许可证
└── README.md                   # 仓库主说明文档
```

---

## 📄 许可证

本项目采用 [CC BY-NC 4.0](LICENSE) 许可证。个人使用、学习研究均可自由免费使用。
