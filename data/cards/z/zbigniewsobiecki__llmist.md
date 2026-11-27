# zbigniewsobiecki/llmist

⭐ 10 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/zbigniewsobiecki/llmist) · [官网](https://llmist.dev) · 个人维护

**面向开发者的 TypeScript 多供应商 LLM 客户端与 Agent 构建库**

以流式输出优先的 TypeScript 库，提供统一 API 接入 OpenAI、Anthropic、Gemini、HuggingFace 等供应商，并支持自定义供应商与模型。核心机制包括自研 gadgets 工具调用语法（无需原生 function calling，块解析即执行）、DAG 依赖执行、低样板 Agent API（Zod 类型推断、子 Agent 派生）、三层 Hook 系统（Observers/Interceptors/Controllers）、双向 MCP 集成、跨供应商的 Deep Research 任务接口，以及无 LLM 调用的确定性测试基础设施。npm 分发核心库、CLI 与 testing 三个包，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 gadgets 工具调用语法，块解析时即执行，支持任意可遵循指令的模型
- 双向 MCP：消费任意 MCP 服务器，也可将 gadgets 发布为 stdio MCP 服务器
- 统一 API 的多供应商接入，含缓存感知 token 统计与成本估算
- 无 API 调用的 MockBuilder/gadget 测试基础设施

## 适用场景

- 在 TypeScript 项目中构建多供应商可切换的 Agent 与子 Agent
- 通过 MCP 将自有工具暴露给 Claude Code、Cursor 等客户端使用
- 运行跨供应商的长时间深度研究任务并断点恢复
- 对 Agent 流程做无 LLM 调用的确定性测试

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10:  Streaming-first multi-provider LLM client in TypeScript with home-made tool calling
> L12:  The flexible agent and tool layer for any LLM.
> L87: First-class support for multiple LLM providers with unified API. Learn more →


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `63035bd192c2` · [字段定义](../../DATASET.md)*
