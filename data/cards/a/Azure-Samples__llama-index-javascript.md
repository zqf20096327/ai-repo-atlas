# Azure-Samples/llama-index-javascript

⭐ 76 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Azure-Samples/llama-index-javascript) · 组织维护

**Azure 上快速上手 LlamaIndex.TS 的 RAG 聊天示例模板**

Azure 官方示例模板：一个全栈 Next.js 应用，使用 LlamaIndex.TS 摄取 PDF、文本、CSV、Markdown、Word、HTML 文件，接入 Azure OpenAI（gpt-35-turbo 与嵌入模型），以聊天界面回答关于自有数据的问题。面向想在 Azure Container Apps 上搭建 RAG 应用的开发者，作为更复杂应用的起点。支持 GitHub Codespaces、VS Code Dev Containers 与本地三种启动路径，通过 azd 命令完成资源供给与部署；模型版本 1106 并非所有 Azure 区域可用，README 推荐 swedencentral 区域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LlamaIndex.TS 摄取 PDF/文本/CSV/Markdown/Word/HTML 文件
- Azure OpenAI gpt-35-turbo 与嵌入模型驱动聊天问答
- azd up 数条命令内部署到 Azure Container Apps
- 提供 Codespaces、Dev Containers 与本地三种启动方式

## 适用场景

- 我在 Azure 上快速搭一个能问答自有数据的 RAG 聊天应用
- 我需要一个 LlamaIndex.TS + Azure OpenAI 的 Next.js 起始模板
- 我想学习如何将 LlamaIndex 应用部署到 Azure Container Apps

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L8: This sample shows how to quickly get started with LlamaIndex for TypeScript on Azure. The application is hosted on A
> L35: - A full-stack Next.js application that is hosted on Azure Container Apps in just a few commands. This app uses Lla
> L37: - The app uses Azure OpenAI to answer questions about the data you provide. The app is set up to use the `gpt-35-tu

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/llama-index-javascript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-31 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `07e2ec639cfd` · [字段定义](../../DATASET.md)*
