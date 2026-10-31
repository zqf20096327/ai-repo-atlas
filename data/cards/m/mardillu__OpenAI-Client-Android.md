# mardillu/OpenAI-Client-Android

⭐ 25 · Kotlin · MIT · 推送 2025-11-21 · [GitHub](https://github.com/mardillu/OpenAI-Client-Android) · 个人维护

**Android 平台的 OpenAI API 轻量 Kotlin 客户端库**

面向 Android 开发者的非官方 OpenAI API 客户端库，以 Kotlin 编写，通过 JitPack 以 Gradle 依赖方式集成。使用时先以 API key 创建 OpenAiConfig 与 OpenApiClient 实例，再通过 Coroutines 发起请求。支持 Chat Completions（GPT-4/GPT-3.5、Function Calling、JSON Mode）、图像、Embeddings、Moderations、Audio 转录翻译、Assistants、Files、Fine-tuning 等端点。README 明确声明与 OpenAI 无隶属关系，MIT 许可；Roadmap 中列有 Streaming for Chat Completions、Batch API 等尚未实现的功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Kotlin + Coroutines 的 OpenAI API 调用封装
- 支持 Chat Completions、图像、Embeddings、Audio、Assistants 等多类端点
- 通过 JitPack 以 Gradle 依赖集成

## 适用场景

- 在 Android 应用中调用 OpenAI 的对话、图像、语音等 API
- 为 Android 项目提供轻量的 OpenAI 接入层

## 场景标签

 · 领域:移动开发/LLM 接入

## 证据(README 行号)

> L2: A lightweight OpenAI API client for Android. This tool is specifically designed for Android developers to interact w
> L30: 1. Create an instance of `OpenAiConfig` and `OpenApiClient`:

## 星数曲线

```mermaid
xychart-beta
    title "mardillu/OpenAI-Client-Android 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e78478a22c7d` · [字段定义](../../DATASET.md)*
