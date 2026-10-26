# decisionnode/DecisionNode

⭐ 83 · TypeScript · MIT · 推送 2026-04-15 · [GitHub](https://github.com/decisionnode/DecisionNode) · [官网](https://decisionnode.dev) · 个人维护

**跨 MCP 客户端共享的结构化决策记忆库（CLI + 本地 MCP）**

面向使用 Claude Code、Cursor、Windsurf 等 MCP 客户端的开发者的本地决策记忆存储：决策以 JSON 记录，经 gemini-embedding-001 向量化存于本地（~/.decisionnode/，vectors.json），AI 通过 MCP 的 search_decisions 按余弦相似度显式检索，不预注入系统提示。提供 CLI（decide）与 MCP 服务器（9 个工具）双接口共用同一存储，另含本地 Web UI（图/向量空间/列表三视图）、75% 相似度冲突检测、软删除（deprecate 保留向量）、全局决策、历史审计与可配置相似度阈值（默认 0.3）。仅本地运行，npm 全局安装。

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

- 决策 JSON 化并向量化，MCP 语义检索（余弦相似度排序）
- CLI 与 MCP 服务器双接口共享同一本地存储
- 本地 Web UI：相似度图、UMAP 向量空间、列表三视图，MCP 查询实时脉冲
- 冲突检测（75% 相似度）与软删除保留嵌入

## 适用场景

- 让 Claude Code/Cursor 等编码 AI 在改代码前检索项目历史决策
- 跨多个 MCP 客户端与多个项目共享团队决策记忆
- 通过可视化界面浏览与审计决策及其语义聚类

## 场景标签

`语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  CLI + Local MCP - A shared structured memory store across Claude Code, Cursor, Windsurf, Antigravity, and every MCP
> L36: 1. **A decision is made** — via `decide add` or the AI calls `add_decision` through MCP
> L44: ||CLI (`decide`)|MCP Server (`decide-mcp`)|

## 星数曲线

```mermaid
xychart-beta
    title "decisionnode/DecisionNode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-26 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8bf3ba3e97d1` · [字段定义](../../DATASET.md)*
