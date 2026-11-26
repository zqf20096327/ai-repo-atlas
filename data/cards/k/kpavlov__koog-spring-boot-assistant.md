# kpavlov/koog-spring-boot-assistant

⭐ 10 · Kotlin · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/kpavlov/koog-spring-boot-assistant) · [官网](https://kpavlov.github.io/koog-spring-boot-assistant/) · 个人维护

**Kotlin+Spring Boot 构建的 Koog 框架 AI 聊天助手示例**

演示 JetBrains Koog 框架构建智能代理的示例应用：以精灵主题聊天机器人形式实现多节点执行图，包含输入审核、RAG 检索（JVM 向量存储，取 top-3 文档，嵌入模型 text-embedding-3-small）、会话持久化与检查点恢复、WebSocket 实时通信，Svelte 网页界面。集成 OpenTelemetry 观测与 Promptfoo 提示词评测，用 Mokksy 做可离线运行的确定性集成测试。面向学习 Koog 框架的开发者，需 Java 17+ 与 Maven 3.9+ 本地构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Koog 多节点代理工作流：输入审核、条件路由、工具调用
- RAG：Markdown 知识库 + JVM 向量存储，取 top-3 相关文档
- OpenTelemetry 追踪/指标与 Promptfoo 提示词评测集成
- 基于 Mokksy 的确定性集成测试，可离线运行

## 适用场景

- 学习 Koog 框架的代理工作流与插件体系
- 参考 Spring Boot + Kotlin 集成 LLM 应用的工程结构
- 用 Promptfoo 对 LLM 提示词做评测优化

## 场景标签

`聊天机器人` `RAG` `模型评测` · 领域:对话与助手

## 证据(README 行号)

> L14: An AI-powered conversational assistant demonstrating
> L17: The application features an Elven-themed chatbot that combines RAG (Retrieval-Augmented Generation),
> L21: - 🤖 **AI Agent Workflow**: Multi-node execution graph with input moderation, LLM processing, and conditional routin

## 星数曲线

```mermaid
xychart-beta
    title "kpavlov/koog-spring-boot-assistant 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `2d636ef2f76e` · [字段定义](../../DATASET.md)*
