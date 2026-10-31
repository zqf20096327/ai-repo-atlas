# Fortyseven/ircawp

⭐ 14 · Python · 推送 2026-10-07 · [GitHub](https://github.com/Fortyseven/ircawp) · 个人维护

**接入 OpenAI 兼容后端的 Slack 聊天机器人，支持插件与图像生成**

面向小规模频道使用的自托管 Slack 机器人：通过 OpenAI 兼容 API 连接 LLM 后端（Ollama、LlamaCpp 等），按请求队列顺序回复，支持以 `+` 前缀延续会话、`!`/`^`/`@` 等前缀改变行为。内置天气、新闻、翻译、转录、YouTube 摘要等斜杠命令插件，以及由模型自主调用的 LLM 工具系统；图像生成由独立的 FastAPI media-server（OpenAI Images 兼容 API）承担。用 setup.sh 与 uv 安装，面向低端硬件、默认 CPU 推理且不流式输出，需等待完整推理结束才回复。

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

- OpenAI 兼容后端（Ollama、LlamaCpp 等）+ 请求队列处理
- 斜杠命令插件体系与 LLM 工具调用（天气/维基/计算器等）
- 独立 FastAPI media-server 承担图像生成，支持 GPU/CPU 多后端
- `+` 前缀延续全局会话并保留媒体与插件输出上下文

## 适用场景

- 在小频道里挂一个能对话、查天气、读新闻的 AI 机器人
- 通过编写插件和 LLM 工具扩展机器人能力
- 用本地 LLM 后端在低端硬件上自托管 AI 聊天服务

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L14: An easy to setup OpenAI API (Ollama, Llamacpp, etc) connected IRC bot with easily extensible plugin functionality.
> L33: - LLM tool calling system — the bot can call external functions (weather, Wikipedia, calculator, network tools) dur
> L37: - **Dedicated media-server** — image generation runs as a separate FastAPI service with an OpenAI-compatible API (`

## 星数曲线

```mermaid
xychart-beta
    title "Fortyseven/ircawp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d416c84c4c9f` · [字段定义](../../DATASET.md)*
