# AIGNE-io/aigne-hub

⭐ 183 · TypeScript · NOASSERTION · 推送 2026-05-13 · [GitHub](https://github.com/AIGNE-io/aigne-hub) · [官网](https://hub.aigne.io) · 组织维护 · 中文 README

**AIGNE 生态的统一 AI 网关：多 LLM 接入与 API key 管理**

基于 Blocklet 与 AIGNE 框架构建的统一 AI 网关，面向使用 AIGNE 框架、AIGNE Studio 与 AIGNE CLI 的开发者和团队。支持接入 OpenAI、Anthropic、Amazon Bedrock、Gemini、DeepSeek、Ollama、OpenRouter 等 8+ 家模型服务商，提供加密 API key 存储、用量统计与成本分析、信用计费与 Payment Kit 支付集成、OAuth 与审计日志。通过 Blocklet Store 部署，也可作为 npm 包在代码中调用。采用 Elastic License 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8+ AI 服务商统一接入，含 Ollama 本地模型部署
- 加密 API key 存储与细粒度访问控制
- 信用计费系统与 Payment Kit 支付集成，可对外提供服务
- 提供 Chat Completions、图像生成、Embeddings 与 RESTful API

## 适用场景

- 团队自托管统一管理多家 LLM 的 API key 与用量成本
- 作为面向客户的 AI 服务运营并按信用计费
- AIGNE 框架应用通过统一网关调用多种模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: AIGNE Hub is a unified AI gateway that manages connections to multiple LLM and AIGC providers, eliminating the comp
> L22: - **🔌 Multi-Provider Management**: Connect to 8+ AI providers through one interface

## 星数曲线

```mermaid
xychart-beta
    title "AIGNE-io/aigne-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 182 --> 184
    line [183, 183]
```

2026-10-18 183 → 2026-10-26 183（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3eb1e3e0e8f2` · [字段定义](../../DATASET.md)*
