# ma2za/telegram-llm-bot

⭐ 114 · Python · MIT · 推送 2026-07-01 · [GitHub](https://github.com/ma2za/telegram-llm-bot) · 个人维护

**本地优先的 Telegram AI 机器人：对话、语音转写与工具调用**

面向终端用户的 Telegram 聊天机器人，默认通过 Ollama 运行 qwen3.5:0.8b 本地模型，支持文本对话、工具调用（时间/计算器/可选 SearchApi 联网搜索）。语音消息经 faster-whisper 本地转写后进入文本流程，音频归档至 MinIO，聊天记录存 SQLite（可选 MongoDB）。提供 /health、doctor、provider-check 等诊断命令，支持 Poetry 本地运行或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认 Ollama 本地推理（qwen3.5:0.8b），另支持 Echo 与 Beam provider
- faster-whisper 本地语音转写，MinIO 归档不阻塞转写
- 工具调用含时间、计算器与可选 SearchApi 联网搜索
- 提供 smoke/doctor/provider-check/eval 诊断与就绪检查

## 适用场景

- 在 Telegram 里使用本地 LLM 进行私域对话
- 发送语音消息获得本地转写与回复
- 自托管部署并监控各依赖服务就绪状态

## 场景标签

`聊天机器人` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L5: Local-first Telegram AI bot for text, voice, tools, web search, and self-hosted storage.
> L7: The default release runs `qwen3.5:0.8b` through Ollama, keeps chat history in SQLite, transcribes voice locally with
> L13: |Chat provider|Ollama with `qwen3.5:0.8b`|

## 星数曲线

```mermaid
xychart-beta
    title "ma2za/telegram-llm-bot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 112 --> 115
    line [113, 114, 114]
```

2026-10-18 113 → 2026-10-26 114（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fda95e73b05f` · [字段定义](../../DATASET.md)*
