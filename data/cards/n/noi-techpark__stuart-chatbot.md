# noi-techpark/stuart-chatbot

⭐ 14 · Python · Apache-2.0 · 推送 2026-05-18 · [GitHub](https://github.com/noi-techpark/stuart-chatbot) · 组织维护

**可本地运行的 RAG 聊天机器人系统，供客服团队回答工单问题**

NOI Techpark 开发的 RAG 问答系统，在内部部署时读取 Open Data Hub Wiki、历史工单、仓库 README 与 GitHub issues，辅助客服解决工单。检索端使用 Postgres + pgvector 向量库与 sentence-transformers 嵌入模型，生成端连接任意 OpenAI 兼容 chat-completion 端点（可用 Ollama 本地运行或第三方服务）。不依赖 LlamaIndex/LangChain 等框架，自行实现分块与数据库访问，仅少量依赖；自定位为实验各 RAG 组件的测试平台。安装约需 15 GiB 存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- RAG 检索基于 Postgres + pgvector 与 sentence-transformers 嵌入
- 生成端只要求 OpenAI 兼容端点，支持本地 Ollama 或第三方服务
- 不依赖 LlamaIndex/LangChain，自行实现分块与数据库访问，依赖少
- 自带针对 GitHub issues、工单、wiki 的定制爬取脚本

## 适用场景

- 用自己的文档搭建可本地运行的 RAG 问答系统
- 客服团队基于内部知识库（wiki/工单/issue）辅助答疑
- 作为实验和替换 RAG 各组件的测试平台

## 场景标签

`聊天机器人` `RAG` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L21: Stuart uses **RAG** (_retrieval-augmented generation_). RAG improves the quality of responses by
> L56: At **NOI Techpark**, Stuart is installed with access to documentation related to the **Open Data Hub**.

## 星数曲线

```mermaid
xychart-beta
    title "noi-techpark/stuart-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `772c7b707066` · [字段定义](../../DATASET.md)*
