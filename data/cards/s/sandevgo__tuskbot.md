# sandevgo/tuskbot

⭐ 24 · Go · MIT · 推送 2026-04-04 · [GitHub](https://github.com/sandevgo/tuskbot) · [官网](https://tuskbot.ai) · 个人维护

**自托管的 Telegram 个人 AI agent，支持 MCP 与本地 RAG**

用 Go 编写的自托管个人 AI agent，以 Telegram Bot 形式运行：支持斜杠命令快捷操作、通过 MCP server 接入工具、用 sub-agent 处理后台任务，内置 llama.cpp 提供本地 embedding（本地 RAG）。LLM 侧可接 OpenAI、Anthropic、OpenRouter、Ollama 及兼容 API。以 curl 脚本安装 tusk 二进制并注册系统服务运行，也可部署为二进制或 Docker 容器；安装前需准备 Telegram Bot Token、Owner ID 与至少一个 LLM provider。平台支持 Linux amd64/arm64 与 macOS arm64，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Telegram Bot 形式自托管运行的个人 AI agent
- 通过 MCP server 接入工具，sub-agent 处理后台任务
- 内置 llama.cpp 本地 embedding（本地 RAG）
- 支持 OpenAI/Anthropic/OpenRouter/Ollama 及兼容 API

## 适用场景

- 在 Telegram 中运行自己的 AI agent 并用斜杠命令交互
- 通过 MCP 接入各类工具扩展 agent 能力
- 搭配本地 Ollama 端点实现完全本地的 agent 部署

## 场景标签

`RAG` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: ### Personal AI Agent. MCP-First, Local RAG, Easy to Run.
> L40: - Runs as a self-hosted AI agent in Telegram
> L45: - Works with OpenAI, Anthropic, OpenRouter, Ollama, and compatible APIs

## 星数曲线

```mermaid
xychart-beta
    title "sandevgo/tuskbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c4eea1ee1482` · [字段定义](../../DATASET.md)*
