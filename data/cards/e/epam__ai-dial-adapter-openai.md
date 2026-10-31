# epam/ai-dial-adapter-openai

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/epam/ai-dial-adapter-openai) · [官网](https://dialx.ai) · 组织维护

**将 Azure OpenAI 等上游模型接入 AI DIAL 统一协议的适配器**

AI DIAL 生态的 LLM 适配器之一：把 Azure OpenAI、OpenAI Platform、Amazon Bedrock、Azure AI Foundry 等上游服务的 Chat Completions、Responses、Embeddings、图像与视频生成（DALL·E 3/GPT-Image-1/Sora 1/Sora 2）、TTS 与 STT 等 API 转换为 DIAL Core 的统一协议，以独立容器运行。通过 DIAL Core 配置映射模型部署 ID，支持 overrideName 解耦 DIAL 与上游模型名。Claude 模型由 aidial-adapter-anthropic 包处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Azure OpenAI Chat Completions/Responses/Embeddings 等多种上游 API 并转换为 DIAL 统一协议
- 覆盖图像（DALL·E 3/GPT-Image-1）与视频生成（Sora 1/Sora 2）及 TTS/STT 音频模型
- 支持 OpenAI Platform 与 Amazon Bedrock（Mantle/Runtime）两种上游端点
- 通过 overrideName 配置解耦 DIAL 模型 ID 与上游部署名

## 适用场景

- 在 AI DIAL 平台中接入 Azure OpenAI 部署的模型
- 通过 DIAL 统一协议调用 Sora 文生视频/图生视频与 TTS/STT
- 将同一 Azure OpenAI 端点以不同配置暴露为多个 DIAL 部署

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: LLM Adapters unify the APIs of respective LLMs to align with the Unified Protocol of DIAL Core. Each Adapter operat
> L17: The project implements AI DIAL API for language models from Azure OpenAI.

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-adapter-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `138916e856c6` · [字段定义](../../DATASET.md)*
