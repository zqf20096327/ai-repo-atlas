# dirmacs/ares

⭐ 18 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/dirmacs/ares) · [官网](https://dirmacs.github.io/ares/) · 个人维护

**Rust 编写的可组合 AI agent 运行时服务器与嵌入库**

基于 Cordis 框架的 Rust AI agent 运行时，可独立运行或作为库嵌入。功能包括多提供商 LLM 路由（Ollama、OpenAI、Anthropic、LlamaCpp 直载 GGUF）、类型安全工具调用、RAG（纯 Rust 向量库与多策略检索）、MCP 集成、多租户 JWT 认证与 PostgreSQL 隔离、工作流编排、配置热重载、断路器故障转移与崩溃恢复。通过 TOML/TOON 声明式配置，ares-server 二进制提供 Axum HTTP 层与 CLI。默认功能集依赖 Rust 1.98+ 与 PostgreSQL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商 LLM 路由（Ollama/OpenAI/Anthropic/LlamaCpp 直载 GGUF），按优先级自动选择与断路器故障转移
- TOML/TOON 声明式配置，500ms 内热重载，含循环引用检测
- RAG：纯 Rust HNSW 向量库 + 语义/BM25/模糊/混合检索与重排
- MCP 集成、多租户隔离、崩溃恢复检查点、3 级循环检测

## 适用场景

- 自建多 agent 服务的后端运行时，按租户隔离工具与数据
- 本地 Ollama/GGUF 模型接入并编排工作流与深度研究任务
- 将 agent 能力（Llm/Tools/Execute）作为 Rust 库嵌入现有项目

## 场景标签

`多智能体` `Agent 框架` `RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: **A.R.E.S** (Agentic Runtime Extensible Server) is a composable AI agent runtime in Rust, built on the Cordis frame
> L18: - Multi-provider LLM: Ollama, OpenAI, Anthropic Claude, LlamaCpp (direct GGUF loading)

## 星数曲线

```mermaid
xychart-beta
    title "dirmacs/ares 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `654cf8661683` · [字段定义](../../DATASET.md)*
