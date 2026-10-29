# stdapi-ai/stdapi.ai

⭐ 25 · Python · AGPL-3.0 · 推送 2026-09-30 · [GitHub](https://github.com/stdapi-ai/stdapi.ai) · [官网](https://stdapi.ai/?utm_source=github-readme&utm_medium=repo&utm_campaign=owned-surfaces) · 组织维护

**面向 Amazon Bedrock 的自托管 AI API 网关，兼容多种主流 API**

部署在用户自己 AWS 账户内的 LLM 网关：把 Amazon Bedrock 及 Polly、Transcribe、Comprehend 等 AWS AI 服务聚合为 OpenAI、Anthropic、Cohere 和 Ollama 兼容端点，覆盖 100+ 模型的聊天、嵌入、图像、视频、音频与内容审核。支持多区域配额与故障重试、按 API key 的多租户限额、OpenTelemetry 可观测性、内置 MCP server 与带引用的文件检索。提供免费社区版 Docker 镜像（本地开发免费），生产版经 AWS Marketplace 按 $0.10/容器小时计费，模型用量由 AWS 直接计费、零加价。面向在 AWS 上运行 AI 应用的企业开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Anthropic/Cohere/Ollama 四种兼容端点聚合 Bedrock 及 AWS AI 服务
- 多区域配额、跨区域重试与模型退役自动重定向
- 多租户 API key、按分钟限流、密钥定期轮换
- 内置 MCP server（90+ 工具）与 OpenTelemetry 可观测性

## 适用场景

- 让 Claude Code、Open WebUI、n8n 等现有工具直接接入 Amazon Bedrock
- 在企业自有 AWS 账户内统一管理多团队的模型调用与配额
- 通过标准 SDK 在 Bedrock 上运行 RAG、语音与多模态应用

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L5: **OpenAI, Anthropic, Cohere & Ollama Compatible API Gateway for Amazon Bedrock and AWS AI Services**
> L28: - **🔌 Same API, wider catalogue** — Adoption is quick: standard OpenAI, Anthropic, Cohere and Ollama SDKs connect o
> L50: docker run --rm -p 8000:8000 \

## 星数曲线

```mermaid
xychart-beta
    title "stdapi-ai/stdapi.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f6f635448535` · [字段定义](../../DATASET.md)*
