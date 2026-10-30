# SAP/ai-sdk-java

⭐ 44 · Java · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/SAP/ai-sdk-java) · 组织维护

**面向 Java 应用接入 SAP AI Core 的官方 SDK**

SAP 官方的 Java SDK，用于将 SAP AI Core、Generative AI Hub 与 Orchestration Service 的能力（如聊天补全）集成到 Java 业务应用中。以 Maven 依赖形式提供，通过 OrchestrationClient 等客户端调用模型（示例使用 GPT-4o），支持模板、数据脱敏、内容过滤与 grounding。要求 JDK 17+、SAP Cloud SDK 5.6.0+ 及可用的 SAP AI Core 服务实例；模型包下的类标记为 @Beta，可能随次要版本变更。可与 Spring AI/Spring Boot/CAP Java 可选集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 Orchestration/OpenAI 客户端调用聊天补全
- 支持模板、grounding、数据脱敏、内容过滤
- 基于 SAP Cloud SDK destination 概念管理与 AI Core 的连接
- 可选集成 Spring AI（≥1.0.0）、Spring Boot（≥3.0）、CAP Java（≥3.0.0）

## 适用场景

- 在 Java 业务应用中接入 SAP Generative AI Hub 的聊天补全
- 利用 Orchestration 服务做提示模板与内容过滤
- 通过 Maven 依赖将 SDK 加入 Spring Boot 项目

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: **SAP Cloud SDK for AI** is the official Software Development Kit (SDK) for **SAP AI Core**, **SAP Generative AI Hub
> L11: This SDK enables developers to seamlessly integrate AI capabilities, such as chat completion, into their Java-based

## 星数曲线

```mermaid
xychart-beta
    title "SAP/ai-sdk-java 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-30 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `76201682c154` · [字段定义](../../DATASET.md)*
