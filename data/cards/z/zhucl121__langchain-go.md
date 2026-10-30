# zhucl121/langchain-go

⭐ 18 · Go · MIT · 推送 2026-02-28 · [GitHub](https://github.com/zhucl121/langchain-go) · 个人维护 · 中文 README

**LangChain/LangGraph 的 Go 语言实现框架，用于构建 AI 应用**

用 Go 实现 LangChain 与 LangGraph 的 AI 应用开发框架：提供 7 种 Agent 类型、统一 Agent 创建接口（5 种策略）、Multi-Agent 协作（顺序/并行/层次化）、3 行代码 RAG、GraphRAG、学习型检索与三层认知记忆系统。支持 6 个 LLM 提供商（OpenAI/Anthropic/Gemini/Bedrock/Azure/Ollama）、5 个向量存储、8 个文档加载器、38 个内置工具，并实现 MCP 与 A2A 协议。含 RBAC/多租户/审计日志等企业特性与 Prometheus/OpenTelemetry 可观测性，通过 go get 安装，附 27 个示例程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种 Agent 类型与统一 Agent 创建接口（5 种策略切换）
- 3 行代码 RAG、GraphRAG（Neo4j/NebulaGraph）与学习型检索
- MCP/A2A 协议实现与 Claude Desktop 互操作
- 5 个向量存储 + 6 个 LLM 提供商接入

## 适用场景

- 用 Go 构建 ReAct/ToolCalling 等 Agent 应用
- 在 Go 服务中搭建 RAG 与多 Agent 协作系统
- 通过 MCP/A2A 协议与 Claude Desktop 等系统互操作

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L12: LangChain-Go 是 LangChain 和 LangGraph 的完整 Go 语言实现，针对 Go 生态优化，提供高性能、类型安全的 AI 应用开发体验。
> L31: - 🌐 **6个LLM提供商** - OpenAI, Anthropic, Gemini, Bedrock, Azure, Ollama

## 星数曲线

```mermaid
xychart-beta
    title "zhucl121/langchain-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e12b062b8054` · [字段定义](../../DATASET.md)*
