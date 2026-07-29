---
name: sk-bridge
description: 跨 Agent 平台桥接 Skill (/sk-bridge)。自动化将本仓库 Skills 同步并整合至 Claude Code, Codex, WorkBuddy, Trae 等不同平台。
---

# 多 Agent 桥接 Skill (/sk-bridge)

本 Skill 用于管理与同步本 Skill System 仓库中的所有 Skill 至不同 AI Agent 环境（如 `~/.agents/skills` 或 Claude Code 插件市场）。

---

## 🛠️ 命令工具与用法

```bash
# 进入 tools/ 目录
cd tools/

# 1. 检查各 Agent 环境的同步状态
python bridge_sync.py --status

# 2. 一键同步至默认 Agent 技能目录 (~/.agents/skills)
python bridge_sync.py

# 3. 强制覆盖更新
python bridge_sync.py --force
```
