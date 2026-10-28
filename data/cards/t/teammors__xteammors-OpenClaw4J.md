# teammors/xteammors-OpenClaw4J

⭐ 19 · Java · MIT · 推送 2026-03-27 · [GitHub](https://github.com/teammors/xteammors-OpenClaw4J) · [官网](https://www.teammors.top) · 组织维护 · 中文 README

**Java 21 + Spring AI 构建的多平台 AI Agent 开发框架**

面向 Java 开发者的智能 Agent 开发框架，基于 Java 21、Spring Boot 3.3 与 Spring AI 构建，默认集成 DeepSeek、火山引擎豆包模型，支持流式对话与上下文理解。内置 Telegram 与 Teammors 机器人适配器实现多平台接入，通过基于文件的 SimpleVectorStore 提供轻量级 RAG，采用 Java+Python 混合技能系统，收录浏览器自动化、PDF/PPT 生成、语音转文本等 20 余项技能。运行需 JDK 21+、Maven、Redis、MySQL 与 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Spring AI，默认集成 DeepSeek 与火山引擎豆包模型，支持流式对话
- 内置 Telegram 与 Teammors 适配器的多平台接入
- SimpleVectorStore 文件向量存储实现轻量级 RAG，无需独立向量数据库
- Java+Python 混合技能系统，收录 20 余项技能（浏览器自动化、PDF/PPT 生成、Whisper 语音转文本等）

## 适用场景

- Java 开发者搭建多平台 AI 机器人/Agent 服务
- 通过本地知识库 RAG 增强回答并降低 Token 消耗
- 以标准化 Skill 接入外部工具执行查邮件、爬网页等实际任务

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L17: **OpenClaw4J** 是一个基于 Java 21 和 **Spring AI** 构建的现代智能 Agent 框架。受到 OpenClaw 项目（开源精神与经典重构）的启发，本项目的目标是为 Java 开发者提供一个灵活、
> L24: * **AI 核心驱动**：基于 **Spring AI** 框架，默认集成 **DeepSeek** 和 **火山引擎豆包** 大模型，支持流式对话与上下文理解。
> L76: 2. **能力扩展**：通过标准化的 Skill 接口，让开发者可以轻松接入各种外部工具（Tools/Plugins）。

## 星数曲线

```mermaid
xychart-beta
    title "teammors/xteammors-OpenClaw4J 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5b0cbb3753bf` · [字段定义](../../DATASET.md)*
