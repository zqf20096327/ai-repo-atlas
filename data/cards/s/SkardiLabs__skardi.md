# SkardiLabs/skardi

⭐ 108 · Rust · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/SkardiLabs/skardi) · [官网](https://skardi.ai) · 组织维护

**面向 AI agent 的自进化上下文框架：记录查询意图并固化为工具**

Rust 编写的上下文服务框架：通过一个 DataFusion 进程将 Postgres、Parquet/S3、MongoDB、Lance 等数据源统一为联邦 SQL 查询入口；agent 每次查询通过 ai_context 声明 purpose/session，写入 SQLite（或 Postgres）审计账本；反复出现的查询被提升为参数化 pipeline（YAML），同一 pipeline 以 shell、REST 与 MCP（本地 stdio 与远程 HTTP）多种绑定暴露，供 Claude Code、Cursor 等 agent 宿主调用。附带 auto-context/retrieval/graph-source/graph-rag 四个技能，支持本地混合检索与多种 embedding 后端（含 gguf/llama.cpp）。提供安装脚本、预编译 CLI、Docker 镜像与源码构建；自声明 Beta，API 可能变动；账本含原始 SQL 字面量，交给托管 LLM 分析需自行权衡。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 联邦 SQL：一条语句跨所有注册数据源查询
- ai_context 意图账本：记录每次查询的 purpose/session/task
- 递归查询提升为 pipeline，同一绑定暴露为 shell/REST/MCP
- 四个 Agent Skills（auto-context/retrieval/graph-source/graph-rag），混合检索（向量+FTS+RRF）

## 适用场景

- 让 agent 用统一 SQL 入口查询我分散在多个库和对象存储里的数据
- 从查询账本发现反复出现的意图并固化为可复用工具
- 把文件夹或已有数据存储变为带治理的检索上下文供 agent 使用

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L30: guessed wrong. Skardi inverts that. The agent gets one general way in, and the
> L80: **4 — The agent has a new tool.** One definition, every binding — shell, REST,
> L136: **One line** installs the CLI, then offers to set up the Claude Code, Codex

## 星数曲线

```mermaid
xychart-beta
    title "SkardiLabs/skardi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 105 --> 109
    line [106, 108, 108]
```

2026-10-18 106 → 2026-10-28 108（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0415588edc67` · [字段定义](../../DATASET.md)*
