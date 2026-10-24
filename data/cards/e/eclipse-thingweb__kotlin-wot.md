# eclipse-thingweb/kotlin-wot

⭐ 49 · Kotlin · NOASSERTION · 推送 2026-08-10 · [GitHub](https://github.com/eclipse-thingweb/kotlin-wot) · 组织维护

**Kotlin 实现的 W3C Web of Things 服务端/客户端框架**

面向 Kotlin 开发者的 Web of Things（WoT）框架，用于实现 WoT 服务端与客户端。基于协程架构，通过 Thing Description（JSON-LD）描述事物的属性、动作与事件，抽象 HTTP、MQTT、WebSockets、CoAP 等协议细节；支持基于注解与类内省自动生成 TD，通过 Servient 配置协议服务器动态暴露或消费事物。README 声明库仍在开发中。以 Gradle 依赖方式接入项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于注解与类内省自动生成 Thing Description（JSON-LD）
- 通过 Servient 混合配置 HTTP/MQTT 等多协议暴露与消费事物
- 协程与 Flow 处理异步与事件流
- 遵循 W3C WoT 规范，支持 Basic/OAuth2 等安全方案

## 适用场景

- 用 Kotlin 快速实现 WoT 兼容的 IoT 设备或服务端点
- 为 AI agent 或服务暴露协议无关的标准接口（TD）
- 消费并交互远端 Thing 的属性与动作

## 场景标签

 · 领域:IoT/中间件框架

## 证据(README 行号)

> L1: # kotlin-wot: A Framework for implementing Web of Things in Kotlin
> L3: **kotlin-wot** is a framework designed to enable developers to implement **Web of Things (WoT)** servers and clients

## 星数曲线

```mermaid
xychart-beta
    title "eclipse-thingweb/kotlin-wot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-24 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0bb29e6b739f` · [字段定义](../../DATASET.md)*
