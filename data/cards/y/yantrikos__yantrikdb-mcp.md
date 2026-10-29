# yantrikos/yantrikdb-mcp

⭐ 25 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/yantrikos/yantrikdb-mcp) · [官网](https://yantrikdb.com) · 组织维护

**给 AI agent 的持久认知记忆 MCP 服务器**

一个为 MCP 兼容客户端（Claude Code、Cursor、Windsurf 等）提供持久化、结构化、可查询跨会话记忆的 MCP 服务器，底层为 YantrikDB Rust 引擎。提供 21 个工具覆盖记忆存取（remember/recall/forget/correct）、知识图谱、矛盾检测（conflict/think）、时间衰减、程序性学习、任务与会话管理等；存储默认为本地 SQLite，也可连接 HTTP 集群或以 SSE 服务运行。内嵌 64 维 Rust embedder，可选 ONNX MiniLM（384 维）与多语言（256 维、101 语言）后端。默认 pip 安装，全部数据留在本机、无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 个 MCP 工具：记忆存取、知识图谱、矛盾检测、时间查询、程序性记忆、任务管理等
- 三种部署模式：本地 SQLite 内嵌引擎、HTTP 集群客户端、SSE 远程服务
- 三种 embedder 后端：内置 64 维 Rust、ONNX MiniLM 384 维、多语言 256 维（101 语言）
- digest-first 工作流：session(digest) 一次调用返回启动简报

## 适用场景

- 让 Claude Code / Cursor 等 MCP 客户端在跨会话间保留决策与偏好记忆
- 在多台机器间通过 HTTP 集群共享 agent 记忆
- 检测并解决 agent 存储信念之间的矛盾

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L22: |**What it is**|An MCP server that gives any MCP-compatible AI agent persistent, structured, queryable memory acros
> L3: **YantrikDB — Cognitive memory for AI agents. Persistent semantic recall, knowledge graph, contradiction detection, 

## 星数曲线

```mermaid
xychart-beta
    title "yantrikos/yantrikdb-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a2f6ee325427` · [字段定义](../../DATASET.md)*
