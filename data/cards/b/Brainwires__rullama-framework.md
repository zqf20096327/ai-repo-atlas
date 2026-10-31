# Brainwires/rullama-framework

⭐ 21 · Rust · Apache-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/Brainwires/rullama-framework) · [官网](https://brainwires.dev/) · 组织维护

**Rust AI agent 框架：多提供商、工具编排、MCP 与 RAG**

由 33 个框架 crate 与 18 个附加应用组成的工作区，供开发者构建、训练、部署与协调 AI agent。核心机制：统一 Provider trait 接入 Anthropic/OpenAI/Google/Ollama 及本地 LLM；基于 rmcp 的 MCP 客户端/服务器；5 层 agent 网络协议栈（IPC/TCP/A2A/Pub-Sub）；AST 感知代码分块的混合检索 RAG；云端微调与本地 LoRA/QLoRA/DoRA 训练。各 crate 独立发布于 crates.io，也可经 rullama 门面 crate 组合使用。README 声明为早期项目，预期破坏性变更；需要 Rust 1.91+（edition 2024）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 Provider trait 多提供商接入（含 Ollama、Bedrock、Vertex AI、本地 llama.cpp/Candle）
- MCP 客户端与服务器框架，含 HTTP+SSE、OAuth JWT 中间件
- 5 层 agent 网络协议栈与 A2A 协议（JSON-RPC/REST/gRPC）
- AST 感知分块、向量+BM25 混合检索的 RAG 与本地 LoRA/QLoRA/DoRA 训练

## 适用场景

- 在 Rust 项目中构建多提供商 AI agent 应用
- 将 agent 暴露为 MCP 工具或搭建 MCP 服务器
- 对代码库做索引与混合检索实现 RAG
- 进行云端微调或本地 LoRA/QLoRA 训练

## 场景标签

`Agent 框架` `RAG` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L11: A modular Rust framework for building AI agents with multi-provider support, tool orchestration, MCP integration, a
> L17: rullama is a workspace of 33 framework crates plus 18 extras — apps and libraries under `sdks/`, `servers/`, `integ
> L21: - **Multi-provider AI** — Anthropic, OpenAI, Google, Ollama, and local LLMs behind a unified `Provider` trait

## 星数曲线

```mermaid
xychart-beta
    title "Brainwires/rullama-framework 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5f85a851b57a` · [字段定义](../../DATASET.md)*
