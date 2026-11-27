# agelenler/gen-ai-java-spring

⭐ 19 · Java · NOASSERTION · 推送 2026-11-06 · [GitHub](https://github.com/agelenler/gen-ai-java-spring) · [官网](https://www.udemy.com/course/complete-genai-with-java-spring-ai-llms-rag-ai-agents/?referralCode=EAF28E814432B8BB9A98) · 个人维护

**Udemy 课程配套代码库：用 Java/Spring AI 实现 LLM、RAG 与多 Agent**

Udemy 课程《Complete GenAI with Java & Spring AI》的配套源码仓库，用 Java 和 Spring Boot 演示生成式 AI 功能。包含一个主 Spring Boot 应用与一个被主应用调用的 posture-service 应用，涉及 AI agents、chat memory、RAG、MCP、multi-agent 与 observability 等主题。仓库提供 Docker Compose 启动可观测性栈（Prometheus/Grafana/Loki/Jaeger/Tempo）及带 pgvector 的本地 Postgres；应用需 Java 25 与 IntelliJ 或 Maven 运行，并通过环境变量配置 API 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主应用与 posture-service 两个 Spring Boot 应用的完整源码
- Docker Compose 一键启动 Prometheus/Grafana/Loki/Jaeger/Tempo 可观测性栈
- 本地 Postgres + pgvector 作为向量库，端口 5433 初始化
- 通过环境变量接入 OpenAI、Hugging Face、Cohere 等 API 密钥

## 适用场景

- 跟随 Udemy 课程学习 Java 生态下的 GenAI 开发
- 在 Spring Boot 项目中参考 RAG、chat memory、多 Agent 的实现方式
- 复用其可观测性 Docker 配置监控 LLM 应用

## 场景标签

`教程课程` `RAG` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Code repository for "Complete GenAI with Java & Spring AI: LLMs, RAG, AI Agents" Udemy course,
> L4: demonstrating Gen AI features with Java and Spring Boot.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `118640ea174b` · [字段定义](../../DATASET.md)*
