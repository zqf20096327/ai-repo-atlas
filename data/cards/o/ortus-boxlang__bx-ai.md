# ortus-boxlang/bx-ai

⭐ 19 · Java · 推送 2026-10-27 · [GitHub](https://github.com/ortus-boxlang/bx-ai) · [官网](https://www.boxlang.io) · 组织维护

**BoxLang 语言的官方 AI 模块：统一 API 编排多模型、Agent 与 RAG**

Ortus Solutions 维护的 BoxLang AI 库，为运行在 JVM 上的 BoxLang 语言提供统一接口接入 16+ AI 提供商（OpenAI、Claude、Gemini、Grok、DeepSeek、Ollama 等），支持自主 Agent、RAG 管道、12 种向量数据库记忆、30+ 文档格式加载、函数调用工具、流式输出与 MCP 协议。通过 aiChat/aiAgent 等内建函数以流式链式语法调用，配置切换提供商。以 Apache 2 开源，另提供付费的 BoxLang +/++ 企业版计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 API 接入 16+ AI 提供商，配置即可切换
- 自主 Agent（记忆/工具/子 Agent）与多租户记忆、12 种向量数据库 RAG
- 提供 MCP 协议、AI Skills（Claude Agent Skills 标准）与确定性回放测试
- 运行时能力发现 API，调用不支持的能力抛出明确异常

## 适用场景

- 在 BoxLang 应用中用统一 API 调用多家模型厂商
- 构建带记忆、工具与 RAG 的多步 Agent
- 本地 Ollama 离线运行以避免 API 成本
- 部署到 AWS Lambda 或 Web 应用的服务端 AI 功能

## 场景标签

`Agent 框架` `RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L26: Welcome to the **BoxLang AI Module** 🚀 The official AI library for BoxLang that provides a unified, fluent API to o
> L32: - 🔌 **16+ AI Providers** - Single API for OpenAI, Claude, AWS Bedrock, Gemini, Grok, MiniMax, Ollama, DeepSeek, and
> L34: - 🤖 **AI Agents** - Autonomous agents with memory, tools, sub-agents, and multi-step reasoning

## 星数曲线

```mermaid
xychart-beta
    title "ortus-boxlang/bx-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7a1f10caf159` · [字段定义](../../DATASET.md)*
