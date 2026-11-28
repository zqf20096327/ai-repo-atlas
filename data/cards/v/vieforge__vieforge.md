# vieforge/vieforge

⭐ 10 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/vieforge/vieforge) · [官网](https://vieforge.dev) · 个人维护

**给 AI 编程 Agent 降低云端 token 消耗的三层混合编排工具**

以 Python 包形式提供的 AI Agent 编排层，按三层架构分流任务：云端 Agent 负责架构与审查，本地 Python/SQLite/本地 LLM 负责检查点与批处理，隔离 GPU 子进程或限额付费 API 负责重推理。通过 MCP 配置与技能安装对接 Claude Code、Cursor 等多种 Agent/IDE，输出成本账本与节省报告。核心为 MIT 许可纯标准库实现，另有商业版企业扩展（多节点、SSO 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Code First / Local LLM / Cloud Last 三层架构与成本账本
- SQLite WAL 逐项检查点、跨项目 GPU VRAM 租约与并发锁
- 为 7 类 Agent/IDE 一键安装技能并生成 MCP 配置
- 按硬件档位（CPU-only 至 24GB+ VRAM）推荐本地模型与显存守护

## 适用场景

- 批量文档分类/JSON 抽取时把任务下沉到本地执行以降低 API 支出
- 多项目同时使用 Claude Code/Cursor 时避免 GPU 与状态冲突
- 压缩 CI/pytest 日志减少喂给云端 Agent 的 token

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L22: Turn any consumer workstation into a **checkpointed, budget-guarded, multi-project local AI worker** to cut Cloud A
> L46: |**Tier 2 (Backbone)**|Python Stdlib + SQLite WAL + Local LLM (Ollama / OpenAI-compat)|Per-item checkpoints, SHA-25


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b59234cffba1` · [字段定义](../../DATASET.md)*
