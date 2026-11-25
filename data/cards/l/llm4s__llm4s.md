# llm4s/llm4s

⭐ 279 · Scala · MIT · 推送 2026-11-24 · [GitHub](https://github.com/llm4s/llm4s) · 组织维护

**Scala 开发者的 LLM 应用构建框架**

面向 JVM/Scala 平台的 LLM 应用框架，提供多供应商客户端、单/多 Agent 与工具调用、RAG 与向量存储、记忆、guardrails、追踪与指标、workspace 隔离、MCP 支持及图像语音 API。自 0.5.0 起拆分为独立模块，供应商通过 SPI 注册，核心库不含供应商客户端。当前为 pre-1.0 阶段（v0.6.0），仅支持 Scala 3.7.x 与 JDK 21，API 仍在稳定化中，Scala 2.13 调用为非支持配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 API 后接 18 个聊天供应商，含本地 Ollama 与 JVM 内运行的 Jlama
- Agent 框架、MCP、RAG、guardrails、观测能力按模块拆分，核心依赖面小
- 提供无需 API key 的 cookbook 示例（脚本客户端替代模型）
- 附带 doctor CLI 检查 JDK、供应商配置、模块与 key 是否齐全

## 适用场景

- 在 Scala/JVM 企业系统中构建 LLM 应用
- 开发单/多 Agent 工具调用工作流
- 搭建带 RAGAS 评估的检索增强流程
- 在本地 Ollama 环境下运行示例与开发调试

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L53: LLM4S provides a simple, robust, and scalable framework for building LLM applications in Scala. While most LLM work
> L61: The framework already provides multi-provider clients, agents and tool calling, RAG and vector stores, memory, guar

## 星数曲线

```mermaid
xychart-beta
    title "llm4s/llm4s 星数(近 11 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-18", "2026-11-20", "2026-11-25"]
    y-axis "stars" 272 --> 281
    line [273, 274, 278, 277, 276, 273, 278, 279, 280, 279, 279]
```

2026-10-25 273 → 2026-11-25 279（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `7f55be71fa2a` · [字段定义](../../DATASET.md)*
