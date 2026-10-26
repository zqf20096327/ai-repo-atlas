# ismailperim/briefd

⭐ 31 · Go · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/ismailperim/briefd) · 个人维护

**给 AI 编程团队的自托管上下文编译器，经 MCP 供给编码智能体**

briefd 以 git 仓库中的 Markdown 为知识源，索引为 SQLite（FTS5 BM25 + multilingual-e5-small 纯 Go 嵌入，倒数排序融合），通过 MCP/REST 向编码智能体提供按 token 预算编译去重的上下文包；agents 不直接写索引，propose_update 只开分支/PR 由人合并。面向多项目同领域的团队，替代每轮全量注入 CLAUDE.md。提供单二进制、stdio/HTTP MCP、Docker 镜像与仪表盘；首次运行需下载约 470 MB 嵌入模型，也支持 BM25-only 模式。README 给出基准：样本库上较全量 CLAUDE.md 省 86% token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- compile_bundle 返回不超预算的去重上下文包，含来源行与缓存
- SQLite FTS5 + multilingual-e5-small 纯 Go 嵌入的混合检索，无 Postgres/向量库/CGO
- propose_update 只开分支/PR，索引仅在人工合并后变化
- 支持 Obsidian vault 的 wikilink 解析与链接图，列出孤儿/断链与知识缺口

## 适用场景

- 团队把术语、规范、架构决策放进 git 仓库，按需供给编码智能体
- 削减每轮会话中重复注入 CLAUDE.md/AGENTS.md 的 token 消耗
- 多项目同领域团队让所有 agent 应用同一套规则并跟踪规则过时

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L6:  A self-hosted context compiler for AI coding teams: git-backed knowledge, served to coding agents
> L74: How briefd works. Ingest: knowledge repo → chunker → SQLite → embeddings in pure Go. Serve: coding agent → MCP/REST
> L79: - **Hybrid retrieval, no external services.** SQLite FTS5 (BM25) + multilingual embeddings

## 星数曲线

```mermaid
xychart-beta
    title "ismailperim/briefd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `697a8a829551` · [字段定义](../../DATASET.md)*
