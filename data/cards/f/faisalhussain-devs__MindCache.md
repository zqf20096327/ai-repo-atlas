# faisalhussain-devs/MindCache

⭐ 19 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/faisalhussain-devs/MindCache) · [官网](https://medium.com/@faisaliitian/building-mindcache-designing-an-agentic-memory-system-for-long-term-ai-7359e0cf6e2a?sharedUserId=faisaliitian) · 个人维护

**面向 LLM agent 的开源长期记忆引擎**

MindCache 是为 LLM agent 提供长期记忆的 Python 库：将对话转化为 User、Decision、Episodic、Knowledge 四类结构化记忆，放入动态主题树中，随对话演化进行叶子拆分、兄弟合并、Leiden 图分区与增量摘要；记录决策状态以区分当前与历史决策。检索采用向量+BM25 混合搜索与 RRF 融合。默认 SQLite 存储，支持 PostgreSQL（pgvector），内置 MCP server 可接入 Claude Desktop、Cursor 等 AI 客户端，提取记忆时需配置 Gemini API key。

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

- 四类记忆（User/Decision/Episodic/Knowledge）与动态主题树组织
- 决策生命周期跟踪（ACTIVE/SUPERSEDED/CONDITIONAL/REJECTED）
- 向量+BM25 混合检索、RRF 融合与记忆类型配额
- 内置 MCP server（mindcache-mcp），暴露 6 个记忆工具

## 适用场景

- 为跨多轮会话的 agent 维护结构化长期记忆
- 追踪用户决策变更，区分当前有效与历史决策
- 通过 MCP 将长期记忆接入 Claude Desktop、Cursor 等客户端

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **An open-source long-term memory engine for LLM agents.**
> L227: MindCache includes a built-in **MCP server** (`mindcache-mcp`) that exposes long-term memory tools to MCP-compatib

## 星数曲线

```mermaid
xychart-beta
    title "faisalhussain-devs/MindCache 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `655158a65e87` · [字段定义](../../DATASET.md)*
