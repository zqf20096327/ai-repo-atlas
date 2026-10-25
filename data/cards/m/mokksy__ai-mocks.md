# mokksy/ai-mocks

⭐ 53 · Kotlin · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/mokksy/ai-mocks) · [官网](http://mokksy.dev/) · 个人维护

**Kotlin 本地模拟 LLM API 的 mock 服务器工具包，供集成测试**

基于 Mokksy（受 WireMock 启发的 Kotlin/Ktor mock HTTP 服务器）构建的 LLM mock 服务器集合，支持响应流式与 SSE。提供五个专用模块分别模拟 OpenAI、Anthropic、VertexAI Gemini、Ollama 与 A2A 协议服务，各模块的 Chat Completions、Streaming 能力齐全，Embeddings/Moderation 因服务而异。面向 Kotlin/Java 开发者，用于本地构建、测试 LLM 客户端的集成测试场景；构建需 JDK 与 Gradle。

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

- 五个专用 mock 模块：OpenAI/Anthropic/Gemini/Ollama/A2A
- 支持真实响应流式与 SSE
- A2A 模块覆盖完整协议（11 个端点）
- 基于 Mokksy，Kotlin/Java API 可用

## 适用场景

- 在本地模拟 OpenAI/Anthropic 等服务做 LLM 客户端集成测试
- 验证流式与 SSE 场景下的客户端行为
- 不依赖真实 API 与密钥的确定性测试环境搭建

## 场景标签

 · 领域:LLM 开发工具/测试基础设施

## 证据(README 行号)

> L18: _AI-Mocks_ are mock LLM (Large Language Model) servers built on Mokksy, a mock server inspired by WireMock, with su
> L31: **AI-Mocks** is a set of specialized mock server implementations (e.g., mocking OpenAI API) built using Mokksy.
> L33: It supports mocking following AI services:

## 星数曲线

```mermaid
xychart-beta
    title "mokksy/ai-mocks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b2638d76fc3a` · [字段定义](../../DATASET.md)*
