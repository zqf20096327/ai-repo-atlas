# Cyclenerd/google-cloud-litellm-proxy

⭐ 65 · Dockerfile · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/Cyclenerd/google-cloud-litellm-proxy) · 个人维护

**在 Google Cloud 上部署 LiteLLM 代理的指南（OpenAI 格式访问 Vertex AI 模型）**

提供在 Google Cloud Vertex AI 上部署 LiteLLM 代理服务器的分步操作说明：通过 Cloud Shell 使用 gcloud 命令启用 API、创建服务账号、构建 Docker 镜像并部署到 Cloud Run，使 Anthropic Claude、Google Gemini、Meta Llama 3、Mistral Large 等模型可通过 OpenAI API 格式访问，并自动生成 sk- 前缀的 API key。可选步骤包括部署 Lobe Chat 前端。要求 Google Cloud 项目开启计费；区域默认 us-central1，其他区域可能导致部分服务不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- gcloud 命令一键式流程：API 启用、服务账号、Artifact Registry、Cloud Build 构建、Cloud Run 部署
- 以 OpenAI API 格式代理 Vertex AI 上的 Claude/Gemini/Llama 3/Mistral 模型
- 生成随机字符串作为 OpenAI API key
- 可选部署 Lobe Chat 前端并接入代理

## 适用场景

- 让使用 OpenAI API 格式的客户端接入 Google Cloud Vertex AI 模型
- 在自己的 Google Cloud 项目内快速搭建统一的 LLM 代理端点
- 配合 Lobe Chat 等 ChatGPT 风格前端使用 Vertex AI 模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repository provides instructions to deploy a LiteLLM proxy server that allows you to interact with various Larg
> L205: gcloud run deploy "litellm-proxy" \

## 星数曲线

```mermaid
xychart-beta
    title "Cyclenerd/google-cloud-litellm-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-26 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ba6a6023aacb` · [字段定义](../../DATASET.md)*
