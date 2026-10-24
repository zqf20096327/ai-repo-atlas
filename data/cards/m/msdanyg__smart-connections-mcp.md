# msdanyg/smart-connections-mcp

⭐ 59 · TypeScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/msdanyg/smart-connections-mcp) · [官网](https://cmoconfessions.com) · 个人维护

**MCP 服务器：让 Claude 语义搜索本地 Obsidian 笔记库**

面向 MCP 客户端（Claude Desktop、Claude Code 等）的 MCP 服务器，复用 Obsidian Smart Connections 插件已生成的嵌入向量，在本地对笔记和块级内容做语义搜索，查询经同一嵌入模型（transformers.js，约 25MB，本地运行）编码后按余弦相似度排序。提供 search_notes、get_similar_notes、get_connection_graph 等工具，支持多库，无云端调用。嵌入不可用时降级为关键词匹配并显式标注。要求 Node.js 20+、已安装 Smart Connections 插件且已生成嵌入（v2 针对 3.x 数据测试）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复用 Smart Connections 已有嵌入，查询用同一模型本地编码（transformers.js）
- 支持多库（SMART_VAULT_PATHS）与块级（block）语义检索
- 嵌入不可用时显式降级为关键词匹配（mode/warning 字段）
- 提供相似笔记、相似度连接图谱、笔记内容读取等 6 个工具

## 适用场景

- 在 Claude Desktop 中按语义查找自己笔记库的相关内容
- 多 Obsidian 库的统一语义检索
- 通过相似度图谱梳理笔记间的关联想法

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: **Give Claude true semantic memory of your Obsidian vault.** An MCP server that
> L29: - An MCP client (Claude Desktop, Claude Code, …)
> L55: Smart Connections stores an embedding vector for every note and block in

## 星数曲线

```mermaid
xychart-beta
    title "msdanyg/smart-connections-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-24 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `21636ac32cbe` · [字段定义](../../DATASET.md)*
