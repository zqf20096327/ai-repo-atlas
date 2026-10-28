# agentralabs/agentic-memory

⭐ 30 · Rust · MIT · 推送 2026-10-02 · [GitHub](https://github.com/agentralabs/agentic-memory) · [官网](https://crates.io/crates/agentic-memory) · 组织维护

**给 AI agent 的持久认知图记忆：单文件存储事实/决策/推理链**

面向 AI agent 的长期记忆系统：将事实、决策、推理链、修正与技能存储为可导航的认知图，落盘为单一 .amem 二进制文件。Rust 核心 + Python SDK + CLI + MCP server，提供 16 种查询类型（遍历、因果影响、信念修正、推理缺口检测、类比推理、漂移检测等）与 13 个 MCP 工具。修正以 supersession 链保留历史而非覆盖；V3 加入 append-only、BLAKE3 完整性链的分层存储，并自动同步到 Claude Code、Cursor、Windsurf、Cody 等客户端。跨 LLM 提供商使用同一记忆文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 .amem 文件存储认知图，16 种查询类型，BLAKE3 完整性链
- 修正采用 supersession 链保留可审计历史
- 13 个 MCP 工具覆盖捕获/检索/搜索/统计
- 自动同步 Claude Code、Cursor、Windsurf、Cody 多客户端

## 适用场景

- 让 AI 编程助手跨会话保留决策与架构讨论记忆
- 审计 agent 的推理链与修正历史
- 在多个 LLM 客户端间携带同一份持久记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L30: **AgenticMemory** stores your agent's knowledge as a navigable graph in a single binary file. Not "search your old 
> L118: AgenticMemory V3 exposes **13 MCP tools** for AI agents:

## 星数曲线

```mermaid
xychart-beta
    title "agentralabs/agentic-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `10253306a9aa` · [字段定义](../../DATASET.md)*
