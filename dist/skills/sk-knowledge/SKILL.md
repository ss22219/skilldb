---
name: sk-knowledge
description: 本地与网络知识库检索管理 Skill (/sk-knowledge)。管理原子知识库 (atoms.jsonl)、索引本地文件夹并建立 RAG 搜索。
---

# 知识库 Skill (/sk-knowledge)

本 Skill 用于对本地文档、代码库、推文笔记与数据向量建立索引、持续收录与快捷调用。

---

## 🛠️ 核心功能

1. **原子库检索**：直接检索 `知识库/原子库/atoms.jsonl` 中的方法论卡片。
2. **本地文件夹挂载**：将用户指定的本地 Markdown/PDF/TXT 文件夹转化为即时索引的知识库。
3. **跨对话存储与恢复**：通过交互命令保存和恢复分析进度。

---

## 使用示例

```bash
/sk-knowledge 帮我把这个文件夹变成知识库，以后我想直接从里面查找资料。
```
