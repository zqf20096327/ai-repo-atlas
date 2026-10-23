# Azure-Samples/aisearch-openai-rag-audio

⭐ 563 · Python · MIT · 推送 2025-11-19 · [GitHub](https://github.com/Azure-Samples/aisearch-openai-rag-audio) · [官网](https://azure.microsoft.com/products/search) · 组织维护

**语音 RAG 应用示例：GPT-4o Realtime 语音问答结合 Azure AI Search**

Azure-Samples 维护的 VoiceRAG 模式示例应用：浏览器采集语音输入，Python 后端通过 RTMiddleTier 调用 Azure OpenAI gpt-4o-realtime-preview 实时音频 API，并以 Azure AI Search 检索知识库文档送入模型生成带引用的回答，回答以音频形式播放。面向希望在语音界面应用中实现 RAG 的开发者。提供基础设施即代码与 Dockerfile，可经 azd up 一键部署到 Azure Container Apps，也可本地运行（需配置 Azure 服务）；需已配置 Azure AI Search 与 Azure OpenAI，且部署资源会产生费用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器语音输入经 GPT-4o Realtime API 处理并以音频返回回答
- Azure AI Search 检索知识库文档并展示引用来源
- 提供基础设施即代码与 Dockerfile，azd up 一键部署到 Azure Container Apps
- 支持 GitHub Codespaces、VS Code Dev Containers 与本地环境三种运行方式

## 适用场景

- 构建语音交互的知识库问答应用
- 学习实时语音 API 与 RAG 结合的参考实现
- 基于 Azure 服务快速部署一个语音问答演示

## 场景标签

`语音 Agent` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L6: This repo contains an example of how to implement RAG support in applications that use voice as their user interface
> L12: * **Voice interface**: The app uses the browser's microphone to capture voice input, and sends it to the backend wh
> L13: * **RAG (Retrieval Augmented Generation)**: The app uses the Azure AI Search service to answer questions about a kn

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/aisearch-openai-rag-audio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 561 --> 564
    line [562, 563, 563]
```

2026-10-18 562 → 2026-10-23 563（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `e6e34713af70` · [字段定义](../../DATASET.md)*
