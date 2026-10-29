# guitaripod/Swollama

⭐ 17 · Swift · NOASSERTION · 推送 2026-07-20 · [GitHub](https://github.com/guitaripod/Swollama) · [官网](https://guitaripod.github.io/Swollama/) · 个人维护

**Swift 开发者访问 Ollama API 的类型安全 SDK 与 CLI**

面向 Swift 平台的 Ollama 客户端库：以协议导向、async/await 与 AsyncSequence 流式接口覆盖 Ollama 全部 API 端点（generate、chat、embeddings、模型管理、blobs、ps、version），支持思考模型与 reasoning-effort 分级、JSON Schema 结构化输出、工具调用与多模态图像输入，另提供带 Web 搜索能力的自主 agent 封装。通过 API key Bearer 头访问认证部署与云端。零外部依赖，跨 macOS/iOS/tvOS/watchOS/visionOS/Linux，并附带 swollama 命令行工具执行聊天、生成与模型管理。要求本机或远程已安装并运行 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Ollama 全部 API 端点，原生 async/await 与流式接口
- 支持思考模型、JSON Schema 结构化输出与工具调用
- Swift actors 线程安全、零外部依赖、跨 6 个平台
- 附带 swollama CLI：聊天、生成、模型管理与自主 agent

## 适用场景

- 在 Swift/iOS 应用中接入本地或远程 Ollama 模型
- 用结构化输出和工具调用构建 Swift agent
- 命令行快速与 Ollama 模型交互或管理模型

## 场景标签

 · 领域:LLM 客户端库/开发工具

## 证据(README 行号)

> L8: A comprehensive, protocol-oriented Swift client for the Ollama API. This package provides a type-safe way to interac
> L12: - Full native Ollama API coverage — generate, chat, embeddings (`/api/embed` + legacy `/api/embeddings`), model man

## 星数曲线

```mermaid
xychart-beta
    title "guitaripod/Swollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `36a38d167c57` · [字段定义](../../DATASET.md)*
