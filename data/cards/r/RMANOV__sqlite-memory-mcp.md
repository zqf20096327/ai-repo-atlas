# RMANOV/sqlite-memory-mcp

⭐ 18 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/RMANOV/sqlite-memory-mcp) · 个人维护

**面向编码 agent 的 SQLite 跨 agent 记忆 MCP 服务器**

为 Claude Code / Codex 等编码 agent 提供本地优先的共享记忆层：单一 SQLite 文件（WAL 模式支持 10+ 并发会话），FTS5 BM25 全文检索与可选 sqlite-vec 语义检索经 RRF 融合，附带会话快照、任务管理、跨机器 bridge 同步、来源追踪与审批式的候选事实晋升机制。核心 9 个知识图谱工具与 @modelcontextprotocol/server-memory 即插即用兼容，由 FastMCP 微服务器群组扩展更多工具。限制：未发布定价，存在 OSS/premium 运行时边界（私有扩展需签名授权）。

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

- 单一 SQLite 文件 + WAL 模式，支持 10+ 并发 Claude Code 会话
- FTS5 BM25 与可选 sqlite-vec 语义检索经 Reciprocal Rank Fusion 混合排序
- 核心 9 个工具与 @modelcontextprotocol/server-memory 即插即用兼容
- 记忆变更带来源追踪，候选声明经审批门晋升为规范事实

## 适用场景

- 让 Claude 与 Codex 共享同一个带来源记录的知识图谱
- 多个编码会话并发读写同一份本地记忆库
- 跨机器同步共享实体（通过私有 git 仓库的 bridge 工具）
- 为编码 agent 附加会话快照与结构化任务管理

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L13: It is a production-quality, local-first MCP memory stack: a single SQLite file under WAL concurrency (10+ sessions)
> L48: - **Drop-in compatible core** -- All 9 tools from `@modelcontextprotocol/server-memory` work identically in `sqlite

## 星数曲线

```mermaid
xychart-beta
    title "RMANOV/sqlite-memory-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4091bd34a7c2` · [字段定义](../../DATASET.md)*
