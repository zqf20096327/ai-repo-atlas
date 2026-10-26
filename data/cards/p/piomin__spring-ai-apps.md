# piomin/spring-ai-apps

⭐ 37 · Java · 推送 2026-10-24 · [GitHub](https://github.com/piomin/spring-ai-apps) · [官网](https://piotrminkowski.com) · 个人维护

**演示 Spring AI 框架集成的 Spring Boot 示例应用集**

一组基于 Spring Boot 的示例工程，演示如何通过 Spring AI 框架在 Java 应用中接入 AI 能力。包含 MCP（Model Context Protocol）客户端与服务端示例，展示 @Tools 与 Prompts 的暴露与外部 MCP 服务器的连接方式。运行方式为 Maven 的 spring-boot:run 命令，连接模型前需导出 SPRING_AI_OPENAI_API_KEY 环境变量。README 配有配套教程文章链接、CircleCI 持续集成与 SonarCloud 代码质量检查徽章。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 客户端与服务端示例，暴露 @Tools 与 Prompts
- 演示连接外部 MCP 服务器的客户端实现
- 通过环境变量 SPRING_AI_OPENAI_API_KEY 接入模型

## 适用场景

- 学习 Spring AI 框架的 MCP 集成方式
- 参考 Spring Boot 应用接入 AI 模型的工程结构
- 配合配套文章做 Spring AI 入门实践

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: This project demonstrates the integration of AI capabilities within a Spring Boot application, utilizing the Spring
> L33: 1. Getting started with the Spring AI **MCP** concept. Implement a client-side and a server-side application that e

## 星数曲线

```mermaid
xychart-beta
    title "piomin/spring-ai-apps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3b4a12fd2cd7` · [字段定义](../../DATASET.md)*
