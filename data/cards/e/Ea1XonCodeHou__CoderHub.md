# Ea1XonCodeHou/CoderHub

⭐ 32 · Vue · 推送 2026-03-17 · [GitHub](https://github.com/Ea1XonCodeHou/CoderHub) · [官网](http://8.140.19.7/) · 个人维护 · 中文 README

**面向开发者的智能技术博客社区平台，内置 RAG 问答助手**

基于 SpringBoot+Vue3 的技术博客交流社区，包含用户端与管理端。提供博客发布、章节式教程（视频/PDF）、开发者动态、实时私信、消息通知等社区功能；AI 部分基于 LangChain4j 构建 Agent 助手，通过 Tool Calling 检索平台知识库，支持 HyDE、向量+BM25 混合召回与 RRF 融合，并集成 Tavily 联网搜索，模型对接通义千问或 OpenAI。部署依赖 JDK 17+、Node.js 20+ 与 Docker 启动中间件，需自备 API Key，以 MIT 协议开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangChain4j Agent 助手：Tool Calling 检索平台内文章与教程
- RAG 深度检索：HyDE + 向量 Top-K + MySQL BM25 双路召回，RRF 融合排序，SSE 推送进度
- 集成 Tavily 联网搜索，本地知识库优先
- Docker 容器化部署与 GitHub Actions CI/CD

## 适用场景

- 搭建技术博客社区并自带 AI 问答助手
- 在学习教程时通过 AI 助手检索平台内相关内容
- 作为 SpringBoot+LangChain4j 的全栈项目学习参考

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L14: CoderHub 是一个面向开发/学习者的智能技术博客交流社区平台。不仅提供了体系化的技术博客阅读/发布功能，和项目/教程学习模块，更整合了目前热门的 AI Agent 能力，让开发者在阅读和学习过程中，能通过智能助手实时调取平台
> L29: * **AI Agent 内核**：这是项目的核心灵魂。我们采用了最新的 **LangChain4j (0.35.0)** 框架，它不仅能对接主流大模型，更重要的是其提供的 **Tool Calling** 机制，使得 AI 能够
> L37: **1. 智能化技术助理 (Hub-AI)**

## 星数曲线

```mermaid
xychart-beta
    title "Ea1XonCodeHou/CoderHub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f3fc98cc6a39` · [字段定义](../../DATASET.md)*
