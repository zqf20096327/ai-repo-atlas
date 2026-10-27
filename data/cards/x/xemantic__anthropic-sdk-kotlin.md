# xemantic/anthropic-sdk-kotlin

⭐ 66 · Kotlin · Apache-2.0 · 推送 2026-07-14 · [GitHub](https://github.com/xemantic/anthropic-sdk-kotlin) · 个人维护

**面向 Kotlin 多平台的非官方 Anthropic SDK**

用 Kotlin Multiplatform 编写的 Anthropic API 客户端库，可在 Android、JVM、JavaScript、macOS、iOS、WebAssembly 等环境调用 Claude 模型。基于 ktor HttpClient，支持响应流式读取、HTTP 客户端自定义（网关、代理、超时）与用量成本计算；工具定义可从 Kotlin 类自动提取 JSON schema 发送给 API，无需手写样板代码。通过 Gradle 依赖引入，API 仍处于早期阶段可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Kotlin 多平台：同一 SDK 覆盖 Android/JVM/JS/macOS/iOS/WebAssembly
- 工具的 JSON schema 从类定义自动提取
- 基于 ktor 的 HTTP 客户端自定义（网关/代理/超时/自定义头）
- MessageResponse 携带 Usage 并提供成本累计计算

## 适用场景

- 在 Android 或 Kotlin 多平台应用中接入 Claude API
- 用 Kotlin 编写带工具调用的 AI agent
- 通过自建网关或代理路由 Anthropic API 请求

## 场景标签

 · 领域:LLM 基础设施/开发库

## 证据(README 行号)

> L3: Unofficial Kotlin multiplatform variant of the
> L37: This library is a Kotlin multiplatform
> L38: one, therefore your AI agents developed with it can be seamlessly used in Android, JVM, JavaScript, macOS, iOS, Web

## 星数曲线

```mermaid
xychart-beta
    title "xemantic/anthropic-sdk-kotlin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-27 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8183d22bcfde` · [字段定义](../../DATASET.md)*
