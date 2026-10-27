# salmanashraf/android-ai-chat-sdk

⭐ 22 · Kotlin · MIT · 推送 2026-05-29 · [GitHub](https://github.com/salmanashraf/android-ai-chat-sdk) · 个人维护

**Android 多供应商 AI 聊天 SDK，含 Compose UI 与无 UI Kotlin API**

面向 Android 开发者的多供应商 AI 聊天 SDK：通过统一配置接入 OpenAI、Gemini、Claude/Anthropic、Grok/xAI，并支持自定义后端（LLMEngine 注册）。提供开箱即用的 Jetpack Compose 聊天界面，以及不带 UI 的 headless Kotlin API。消息历史由 Room 本地存储，支持运行时切换供应商、persona 系统提示与配置校验。要求 Android 7.0+/API 24+、Kotlin 2.0+；流式响应尚未发布，生产环境建议经自有后端代理而非 App 内直连供应商 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一配置面接入 OpenAI/Gemini/Claude/Grok 四家供应商
- Compose 聊天 UI 与 headless Kotlin API 两种接入方式
- Room 本地消息历史与运行时供应商切换
- 供应商配置校验（validateDefaultProvider/requireValidDefaultProvider）

## 适用场景

- 在 Android 应用中快速集成多供应商 AI 聊天功能
- 无需 UI 的场景下用 headless API 获取模型回复
- 让用户在应用内切换不同 AI 供应商与模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Multi-provider AI chat SDK for Android apps. Add a ready-made Jetpack Compose chat UI or call the same providers fro
> L5: The SDK currently supports OpenAI, Gemini, Claude/Anthropic, and Grok/xAI through one configuration surface.
> L9: The host Android app integrates the SDK either through the ready-made Compose chat UI or the headless API. Both flow

## 星数曲线

```mermaid
xychart-beta
    title "salmanashraf/android-ai-chat-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `82f1c213eeca` · [字段定义](../../DATASET.md)*
