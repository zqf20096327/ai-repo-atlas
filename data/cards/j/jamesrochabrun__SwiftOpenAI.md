# jamesrochabrun/SwiftOpenAI

⭐ 665 · Swift · MIT · 推送 2026-10-05 · [GitHub](https://github.com/jamesrochabrun/SwiftOpenAI) · 个人维护

**Swift 开发者调用 OpenAI API 的开源 SDK 包**

面向 Apple 平台（iOS 15+/macOS 13+/watchOS 9+）与 Linux 的 Swift Package，封装 OpenAI 全部公开 API 端点：聊天补全与流式输出、音频转录/翻译/语音生成、Realtime 双向语音会话（VAD、全双工音频、function/MCP 工具）、结构化输出与 function calling。另支持 Azure、AIProxy 等提供方，Linux 端使用 AsyncHTTPClient 并可配合 Vapor。通过 Swift Package Manager 安装，需自备 API key；Realtime 功能依赖 AVFoundation，不支持 Linux。

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

- 覆盖 OpenAI 全部公开端点，含 Realtime 双向语音 API
- 支持 Azure、AIProxy 等多种 OpenAI 兼容提供方及自定义 URL
- Realtime 会话支持 VAD、全双工音频、function 与 MCP 工具、会话中途更新
- iOS/macOS/watchOS/Linux 多平台支持，Linux 使用 AsyncHTTPClient

## 适用场景

- 在 iOS/macOS 应用中接入 OpenAI 聊天、语音与 Realtime API
- 通过 AIProxy 后端保护客户端应用中的 API key
- 在 Linux 服务端（Vapor）调用 OpenAI 兼容接口

## 场景标签

 · 领域:LLM API 客户端库

## 证据(README 行号)

> L15: An open-source Swift package designed for effortless interaction with OpenAI's public API.
> L23: `SwiftOpenAI` is an open-source Swift package that streamlines interactions with **all** OpenAI's API endpoints, no
> L74: SwiftOpenAI supports both Apple platforms and Linux.

## 星数曲线

```mermaid
xychart-beta
    title "jamesrochabrun/SwiftOpenAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 664 --> 666
    line [665, 665]
```

2026-10-18 665 → 2026-10-26 665（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `560a99bd6607` · [字段定义](../../DATASET.md)*
