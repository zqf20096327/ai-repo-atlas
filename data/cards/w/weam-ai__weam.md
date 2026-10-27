# weam-ai/weam

⭐ 223 · TypeScript · NOASSERTION · 推送 2026-10-13 · [GitHub](https://github.com/weam-ai/weam) · [官网](https://opensource.weam.ai/) · 组织维护

**面向 20+ 人团队的自托管 AI 平台：团队聊天、提示词与 agent 集中协作**

开源的自托管团队 AI 平台，Next.js 前端 + Node.js 后端，开箱接入 OpenAI、Anthropic、Gemini、DeepSeek、OpenRouter 等主流 LLM（填 API key 即用），并支持通过 Ollama 连接本地模型（无需 API key）。以 "Brains" 智能文件夹组织聊天历史、提示词库、AI agent 与知识库文档（内置 RAG 流水线），提供多工作区、权限控制、用量分析等企业功能，另附 AI Docs、AI Recruiter、Blog Engine 等可扩展 AI 应用库。通过 Docker 安装或 git clone 源码自部署，需 4+ 核 CPU、8GB+ 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置接入 OpenAI/Anthropic/Gemini/DeepSeek/OpenRouter 等多家 LLM API
- Ollama 本地模型支持（无需 API key，含 helper 安装脚本）
- Brains 组织聊天、提示词、agent，内置文档分块/嵌入/向量检索的 RAG 流水线
- 多工作区、细粒度权限、用量分析、审计日志等企业功能

## 适用场景

- 团队集中使用多家 LLM 进行协作聊天
- 沉淀共享提示词库与按部门组织的 AI agent
- 自托管部署，数据不出自有基础设施

## 场景标签

`聊天机器人` `提示工程` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18: Modern teams need easy access to the latest AI models. Weam connects to all major LLM providers out of the box - ju
> L19: All your organization's AI interactions live in one centralized platform, organized into "Brains" (intelligent fold
> L41: - **Multi-LLM Support:** OpenAI, Anthropic, Gemini, Llama, Perplexity, DeepSeek, OpenRouter, Hugging Face, Grok, GL

## 星数曲线

```mermaid
xychart-beta
    title "weam-ai/weam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 222 --> 224
    line [223, 223]
```

2026-10-18 223 → 2026-10-27 223（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9f42344674a0` · [字段定义](../../DATASET.md)*
