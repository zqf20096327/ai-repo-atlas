# nirmato/nirmato-ollama

⭐ 43 · Kotlin · Apache-2.0 · 推送 2026-01-25 · [GitHub](https://github.com/nirmato/nirmato-ollama) · 个人维护

**Kotlin Multiplatform 的 Ollama 客户端 SDK**

面向 Kotlin 开发者的 Ollama API 客户端库，按 Ollama OpenAPI 规范提供接口覆盖，包括聊天、流式响应、嵌入生成与模型管理（创建/拉取/推送/列出）。基于 Kotlin Multiplatform，可运行于 Kotlin 支持的各平台；使用 Kotlin Coroutines 实现异步调用，提供类型安全的 DSL 构建请求，内置流式处理。要求 Kotlin 1.8+、JVM 11+，通过 Gradle 或 Maven 依赖安装，HTTP 层基于 ktor（示例搭配 CIO engine）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 Ollama OpenAPI 提供聊天、流式、嵌入与模型管理接口
- Kotlin Multiplatform，运行于 Kotlin 支持的各平台
- 基于 Kotlin Coroutines 的异步调用与内置流式支持
- 提供类型安全 DSL，经 Gradle/Maven 分发 klib

## 适用场景

- 在 Kotlin 多平台应用中调用本地 Ollama 服务
- 构建需要聊天/嵌入能力的 Kotlin 后端或桌面应用
- 以类型安全方式管理 Ollama 模型（拉取、推送、创建）

## 场景标签

 · 领域:LLM 基础设施/客户端库

## 证据(README 行号)

> L7: An Ollama client SDK that allows you to easily interact with the Ollama API.
> L18: - **Kotlin Multiplatform:** Write once, run on any platform that Kotlin supports.

## 星数曲线

```mermaid
xychart-beta
    title "nirmato/nirmato-ollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fe8d9300ecf7` · [字段定义](../../DATASET.md)*
