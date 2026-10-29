# bunkerlab-net/mempalace

⭐ 63 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/bunkerlab-net/mempalace) · 组织维护

**Rust 实现的本地优先 AI 助手记忆库（MCP 记忆服务器）**

MemPalace 的 Rust 重实现：以单个约 13MB 静态二进制提供本地记忆宫殿，内嵌 SQLite（turso）存储，通过 MCP 协议（JSON-RPC 2.0 over stdio）向 AI 助手暴露 26 个工具，兼容全部 CLI 命令。用 BM25 式关键词倒排索引替代原 Python 版的 ChromaDB 嵌入式语义搜索，并在 turso 层以 WAL 模式解决并发写入丢失问题。无需 Python、无 API key；语义搜索、ChromaDB 导入、Wikipedia 实体查册为延期未实现。需从源码 cargo build 编译，或使用 GitHub Actions 预编译产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一约 13MB 静态二进制，内嵌 SQLite（turso），无 Python/API key 依赖
- MCP 服务器提供 26 个工具，JSON-RPC 2.0 over stdio
- BM25 式关键词倒排索引替代 ChromaDB 语义搜索
- WAL 模式在 turso 层解决多 MCP 客户端并发写入丢失

## 适用场景

- 为 Claude Code 等 MCP 客户端提供本地持久记忆
- 替代 Python 版 MemPalace 以获得更小体积与更好并发
- 离线本地环境运行记忆服务，不依赖外部 API

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A local-first memory palace for AI assistants. Single static binary backed by embedded SQLite (turso).
> L65: ## MCP Setup (Claude Code)
> L71: The MCP server runs as a JSON-RPC 2.0 process over stdio. All 26 tools are available immediately

## 星数曲线

```mermaid
xychart-beta
    title "bunkerlab-net/mempalace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-29 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `14a9a65b8feb` · [字段定义](../../DATASET.md)*
