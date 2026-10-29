# fundamental-research-labs/langdag

⭐ 33 · Go · MIT · 推送 2026-09-30 · [GitHub](https://github.com/fundamental-research-labs/langdag) · [官网](https://langdag.com) · 个人维护

**把 LLM 对话持久化为 DAG 的 Go 工具与 API 服务**

以纯 Go 编写的 LLM 对话管理工作具：将每轮对话存储为有向无环图（SQLite + WAL），支持从任意节点分支延续对话、节点别名、SSE 流式输出、指数退避重试与 tool_use/tool_result 流程。提供多供应商模型路由（Anthropic/OpenAI/Gemini/Grok/OpenRouter/Ollama/Azure/Vertex/Bedrock 等），基于权威模型目录解析部署与用量/成本元数据。形态包括 Go 库、单二进制 CLI、REST API 服务端及 Python/Go/TypeScript SDK，并附从 LangGraph 迁移对话的指引。

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

- 对话以 DAG 持久化，可从任意节点分支探索替代路径
- 多供应商路由：Anthropic/OpenAI/Gemini/Grok/OpenRouter/Ollama/Azure/Vertex AI/Bedrock
- 单一静态二进制，宣称约 1ms 开销，零运行时依赖
- 提供 CLI、REST API 服务与 Python/Go/TypeScript 三种 SDK

## 适用场景

- 构建需要持久化对话树与分支回溯的 AI agent 应用
- 在多个模型供应商/部署间做路由与降级重试
- 自托管一个可追溯完整历史的 LLM 对话服务

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L22: LangDAG is a **high-performance Go tool** that persists LLM conversations as directed acyclic graphs. Branch from a
> L50: LangDAG is available as an importable Go package for building AI agent applications with persistent conversation st
> L179: LangDAG can run as a REST API server:

## 星数曲线

```mermaid
xychart-beta
    title "fundamental-research-labs/langdag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ff5205fd88b9` · [字段定义](../../DATASET.md)*
