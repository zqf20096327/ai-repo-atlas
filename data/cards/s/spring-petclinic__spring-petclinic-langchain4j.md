# spring-petclinic/spring-petclinic-langchain4j

⭐ 26 · Java · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/spring-petclinic/spring-petclinic-langchain4j) · 组织维护

**Spring PetClinic 示例：演示在 Java 应用中集成 LangChain4j 聊天机器人**

经典 Spring PetClinic 示例应用的分支，加入由 LangChain4j 驱动的聊天机器人，面向希望了解如何在 Java/Spring Boot 应用中集成 AI/LLM 能力的开发者。演示机制包括：LLM 供应商抽象层（OpenAI/Azure OpenAI/Ollama 可切换，经 Maven profiles 配置）、多用户对话记忆、@AiService 声明式接口、流式输出、工具调用、结构化输出，以及基于宠物诊所数据的 RAG（内存向量库 + 兽医数据启动时摄取）。需 Java 17+ 构建，默认 H2 内存数据库，可选 MySQL/PostgreSQL。限制：Ollama 为部分支持，llama3.1 模型下不完全可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Azure OpenAI/Ollama 经 Maven profiles 切换 LLM 供应商
- RAG：InMemoryEmbeddingStore + 启动时兽医数据摄取 + LLM 驱动的查询路由
- 演示 @AiService、@Tool 工具调用、TokenStream 流式输出、多用户对话记忆
- 默认 H2 内存库，另提供 MySQL/PostgreSQL 配置与 docker-compose

## 适用场景

- 学习如何在 Spring Boot 应用中用 LangChain4j 接入 LLM
- 参考对话记忆、工具调用与 RAG 的 Java 实现写法
- 作为集成 AI 助手的业务应用示例运行体验

## 场景标签

`聊天机器人` `RAG` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L7: A chatbot using **Generative AI** has been added to the famous Spring Petclinic application.
> L11: This sample demonstrates how to **easily integrate AI/LLM capabilities into a Java application using LangChain4j**.
> L13: * A unified **abstraction layer** designed to decouple your code from specific implementations like LLM or embeddin

## 星数曲线

```mermaid
xychart-beta
    title "spring-petclinic/spring-petclinic-langchain4j 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26]
```

2026-10-18 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8c0f7f30d3d0` · [字段定义](../../DATASET.md)*
