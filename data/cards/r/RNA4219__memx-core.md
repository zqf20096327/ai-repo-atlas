# RNA4219/memx-core

⭐ 23 · Go · MIT · 推送 2026-03-10 · [GitHub](https://github.com/RNA4219/memx-core) · 个人维护

**本地优先的个人记忆/知识存储，供 LLM agent 使用**

面向本地 LLM 与 agent 的轻量记忆基盘：以 4 个 SQLite 存储（short/journal/knowledge/archive）分别管理短期记忆、时序日志、知识与归档，提供 CLI 与 HTTP API 两种使用方式，支持跨库检索、条目显示与 LLM 自动摘要。摘要功能可配置 OpenAI 或 Alibaba Cloud Model Studio 作为后端。附带 Claude Code Skills 斜杠命令（/remember、/recall 等），并有 secret 拒存与字段校验等安全机制。以 Go 源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 SQLite 存储分层管理短期记忆/日志/知识/归档
- CLI 与 HTTP API 双通道（检索、显示、摄取、摘要端点）
- 保存时自动 LLM 摘要（OpenAI / Alibaba 可配置）
- 内置 Claude Code Skills 斜杠命令集

## 适用场景

- 为本地 LLM agent 提供持久化个人记忆存储
- 通过 Claude Code 斜杠命令快速记忆与检索笔记
- 以 API 形式向 agent 提供跨库记忆检索与摘要服务

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: ローカル LLM / エージェント向けの軽量メモリ基盤です。
> L4: 4つの SQLite ストアで、保存、検索、参照、要約を行えます。
> L27: `mem out search` は `short / journal / knowledge` を横断検索します。

## 星数曲线

```mermaid
xychart-beta
    title "RNA4219/memx-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3363159c7c59` · [字段定义](../../DATASET.md)*
