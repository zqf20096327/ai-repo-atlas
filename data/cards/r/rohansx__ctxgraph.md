# rohansx/ctxgraph

⭐ 37 · Rust · MIT · 推送 2026-06-23 · [GitHub](https://github.com/rohansx/ctxgraph) · [官网](https://ctxgraph.io) · 个人维护

**面向 AI agent 的本地优先类型化知识图谱引擎（Rust 单二进制）**

用 Rust 编写的单二进制知识图谱引擎，数据存于单个 SQLite 文件，面向 AI agent 与团队的上下文/记忆管理。写入路径分层升级：GLiNER ONNX 本地实体抽取→本地 LLM→云端兜底，每条写入约一次 LLM 调用；读路径 90% 查询由 SQL 确定性执行、零 LLM 调用，仅约 10% 多跳查询调用本地 Qwen3-1.5B。提供 9 实体类型/10 关系类型的固定通用 schema，用户无需自写 schema。支持 local-only/cloud-fallback/cloud-quality 三种模式，附带 CLI、Rust SDK 与含 6 个工具的 MCP server（可接入 Claude Code/Cursor/Cline）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 Rust 二进制 + 单 SQLite 文件，每条写入约 1 次 LLM 调用
- 读路径 90% 查询零 LLM 调用，由 SQL 在封闭关系类型集上确定性执行
- 分层抽取：GLiNER ONNX（CPU ~30ms）→本地 LLM→云端兜底
- 提供 MCP server（6 个工具）、CLI 与 Rust SDK

## 适用场景

- 为 AI agent 提供本地化、隐私优先的长期记忆与上下文存储
- 通过 MCP 把决策/事件记忆接入 Claude Code、Cursor、Cline
- 记录并查询团队技术决策的因果与时间线（bi-temporal 边）

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Typed knowledge graph for AI agents. Single Rust binary. Single SQLite file. One LLM call per write. Zero LLM call
> L107: |`ctxgraph-mcp` — MCP server, 6 tools|shipped|~870|
> L131: ## MCP server (Claude Code / Cursor / Cline)

## 星数曲线

```mermaid
xychart-beta
    title "rohansx/ctxgraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `90249e0fa0af` · [字段定义](../../DATASET.md)*
