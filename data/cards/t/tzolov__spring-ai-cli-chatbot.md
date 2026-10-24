# tzolov/spring-ai-cli-chatbot

⭐ 69 · Java · 推送 2026-01-03 · [GitHub](https://github.com/tzolov/spring-ai-cli-chatbot) · [官网](https://docs.spring.io/spring-ai/reference/index.html) · 个人维护

**Spring AI 构建的 CLI 聊天机器人示例：演示 RAG 与对话记忆**

基于 Spring Boot 与 Spring AI 的命令行聊天机器人示例应用，以 Hurricane Milton 维基 PDF 为领域知识演示 RAG 与对话记忆能力。默认接入 Anthropic Claude 模型（可切换 OpenAI、Ollama），使用 Transformers (ONNX) 生成嵌入，Chroma 作为向量库并通过 Docker Compose 本地启动；PDF 经 PagePdfDocumentReader 读取、TokenTextSplitter 切分后写入向量库，QuestionAnswerAdvisor 提供检索问答，MessageWindowChatMemory 维护最多 500 条对话历史。需 Java 21，通过 Maven 构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 实现：PDF 读取切分入向量库 + QuestionAnswerAdvisor 检索问答
- MessageChatMemoryAdvisor 对话记忆（最多 500 条消息窗口）
- 默认 Anthropic Claude，pom.xml 提供 OpenAI/Ollama 备选依赖
- Chroma 向量库经 Docker Compose 本地自动启动

## 适用场景

- 学习如何在 Spring AI 中搭建 RAG 聊天机器人
- 参考 Spring AI 的模型切换、嵌入与向量库配置方式
- 了解对话记忆与检索参数的可配置实现

## 场景标签

`聊天机器人` `RAG` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L3: This Spring Boot, CLI, application demonstrates how to create an AI-powered chatbot with domain-specific knowledge (
> L25: By default, this project uses Anthropic's Spring Boot starter (`spring-ai-starter-model-anthropic`) with the Claude
> L98: 1. **RAG Implementation**: The application uses a vector store to implement RAG, allowing the chatbot to retrieve r

## 星数曲线

```mermaid
xychart-beta
    title "tzolov/spring-ai-cli-chatbot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-24 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `77b6f813cd33` · [字段定义](../../DATASET.md)*
