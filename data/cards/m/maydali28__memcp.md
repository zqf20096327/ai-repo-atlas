# maydali28/memcp

⭐ 17 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/maydali28/memcp) · [官网](https://pypi.org/project/claude-memory-mcp/) · 个人维护

**为 Claude Code 提供持久记忆的 MCP 服务器**

基于 Python 的 Model Context Protocol 服务器，为 Claude Code 提供跨会话持久记忆：实现 RLM（Recursive Language Model, arXiv:2512.24601）框架，内容存于磁盘由模型按需加载。提供 24 个 MCP 工具，覆盖记忆存储/召回/遗忘、上下文分块（6 种策略）、5 层搜索（关键词/BM25/模糊/语义/RRR 混合）、MAGMA 4 类边知识图谱、Hebbian 共召回强化、保留生命周期（Active/Archive/Purge）与多项目隔离；支持 4 个 Haiku/Sonnet 子代理并行处理。存储用 SQLite 与文件系统，核心依赖仅 2 个包。提供交互式安装器、Docker 部署与 458 个测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个 MCP 工具：记忆、上下文管理、搜索、图遍历、保留生命周期
- RLM 模式：内容存盘按需加载，减少上下文窗口 token 消耗
- 5 层搜索与 HNSW 可选向量索引，零可选依赖下可降级运行
- PreCompact 自动保存钩子与 4 个 Claude Code 子代理

## 适用场景

- 长会话中防止 /compact 后上下文丢失
- 跨会话保留决策、洞察与技术发现
- 多项目隔离地管理知识记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8:  Persistent Memory MCP Server for Claude Code
> L30: MemCP implements the **RLM framework** (Recursive Language Model, arXiv:2512.24601) — an active exploration model w
> L36:     CC[Claude Code] -->|MCP Protocol| S[MemCP Server<br/>FastMCP]

## 星数曲线

```mermaid
xychart-beta
    title "maydali28/memcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `4dd211a4ed15` · [字段定义](../../DATASET.md)*
