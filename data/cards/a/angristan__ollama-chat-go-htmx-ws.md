# angristan/ollama-chat-go-htmx-ws

⭐ 15 · Go · 推送 2025-11-20 · [GitHub](https://github.com/angristan/ollama-chat-go-htmx-ws) · 个人维护

**基于 Ollama 本地 LLM 的网页聊天 PoC（Go+htmx+WebSocket）**

作者自称的实验性聊天应用（PoC）：通过 Ollama Chat API（官方 Go 客户端）在本地运行 Mistral 模型提供对话；聊天历史存于内存并发送给 Ollama 以维持上下文。前端用 htmx 及其 WebSocket 扩展处理实时通信，后端用 Go text/template 渲染 HTML，Melody 处理 WebSocket，TailwindCSS 负责样式，头像来自 DiceBear。README 未给出安装或运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过官方 Go 客户端调用 Ollama Chat API，本地运行 Mistral 模型
- htmx WebSockets 扩展 + 后端 Melody 实现实时通信
- 聊天历史内存存储并回传 Ollama 维持上下文

## 适用场景

- 本地跑一个简单 LLM 聊天界面做实验
- 参考 Go+htmx+WebSocket 构建 AI 聊天应用的示例代码

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Just a little PoC of a chat app running an LLM locally on Ollama. Just an excuse to have fun with websockets, htmx a
> L7: - The Ollama Chat API
> L9:  - Running the Mistral model locally

## 星数曲线

```mermaid
xychart-beta
    title "angristan/ollama-chat-go-htmx-ws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0da44b2b80f4` · [字段定义](../../DATASET.md)*
