# multimindlab/multimind-sdk

⭐ 97 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/multimindlab/multimind-sdk) · [官网](https://www.multimind.dev) · 组织维护

**面向开发者的合规优先 AI agent 框架：统一接入多模型并内置治理**

MultiMind SDK 是一个 Python AI agent 框架，以单一异步接口接入 OpenAI、Anthropic、Gemini、Mistral、Groq、DeepSeek、OpenRouter（300+ 模型）及本地 Ollama 等模型。核心机制包括运行时 PII 检测/脱敏/审计（支持流式分块边界）、GDPR/HIPAA 策略建模与合规看板、成本预算、幻觉检测、对话中途切换模型的上下文迁移，以及可包装 LangChain/LlamaIndex/CrewAI 既有对象的合规代理（multimind serve）。另提供 RAG 管线（FAISS/Chroma 及 40+ 客户端式向量库）、带记忆与工具调用的 Agent、LoRA/QLoRA 微调（Beta）。Apache 2.0 许可，提供 Docker 镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一异步接口接入 OpenAI/Claude/Gemini/Groq/DeepSeek/OpenRouter 及本地 Ollama
- 运行时 PII guard：检测、脱敏、阻断、审计，覆盖流式分块边界
- multimind serve 合规代理：改一行 base_url 即为现有 OpenAI 兼容应用加治理
- 对话中途跨模型切换且上下文随迁；RAG 支持 FAISS/Chroma 与 40+ 向量库

## 适用场景

- 统一封装多家模型 API 并做成本预算与审计
- 为已有 LangChain/LlamaIndex/CrewAI 应用增加 PII 脱敏与合规治理
- 构建带工具调用与记忆的 AI Agent，可本地 Ollama 离线运行
- 满足 GDPR/HIPAA 合规要求的模型调用留证

## 场景标签

`Agent 框架` `RAG` `微调` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: - **One API for all models** — OpenAI, Anthropic Claude, Google Gemini, Mistral, Groq, DeepSeek, xAI, Together, Per
> L20: - **Govern the stack you already have** — don't migrate off LangChain, LlamaIndex, or CrewAI; wrap them. Run `multi
> L21: - **Governed by default** — cost budgets that stop overspending before the call, hallucination detection with sente

## 星数曲线

```mermaid
xychart-beta
    title "multimindlab/multimind-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-23 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `246990d2db25` · [字段定义](../../DATASET.md)*
