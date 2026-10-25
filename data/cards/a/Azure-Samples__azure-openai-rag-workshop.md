# Azure-Samples/azure-openai-rag-workshop

⭐ 153 · Bicep · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Azure-Samples/azure-openai-rag-workshop) · [官网](https://aka.ms/ws/openai-rag) · 组织维护

**Azure OpenAI RAG 工作坊示例：Node.js 搭建文档问答聊天应用**

微软 Azure Samples 出品的教学示例与配套工作坊：用 Fastify 构建 Node.js 服务，通过 OpenAI SDK 与 LangChain.js 实现 RAG 聊天机器人，基于文档语料回答问题；架构为 Azure Static Web Apps + Container Apps 托管，Azure AI Search 作为向量数据库。提供 azd 一键部署、GitHub Codespaces 与 Dev Containers 开发环境；另存在 Node.js+Qdrant、Java/Quarkus+Qdrant 等其他版本。面向想在 Azure 上学习构建 RAG 应用的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Fastify + OpenAI SDK + LangChain.js 的 RAG 聊天服务与前端网站
- Azure Static Web Apps / Container Apps / AI Search 的完整参考架构
- azd up 命令一键部署到 Azure，azd down 清理资源
- 提供 Codespaces 与 Dev Containers 两种在线/本地开发环境

## 适用场景

- 学习在 Azure 上构建 RAG 文档问答应用的完整流程
- 将该示例作为起点二次开发更复杂的 AI 应用
- 对比不同技术栈版本（Azure AI Search / Qdrant、Node / Java）的 RAG 实现

## 场景标签

`RAG` `文档问答` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L14: This sample shows how to build an AI chat experience with Retrieval-Augmented Generation (RAG) using LangChain.js a
> L17: > 👉 **Follow the full-length workshop** to learn how we built this sample and how you can run and deploy it.

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-openai-rag-workshop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 151 --> 154
    line [152, 153, 153]
```

2026-10-18 152 → 2026-10-25 153（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `cf612d856eaa` · [字段定义](../../DATASET.md)*
