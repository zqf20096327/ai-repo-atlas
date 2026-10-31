# kirillzhosul/ollama-telegram-ai

⭐ 18 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/kirillzhosul/ollama-telegram-ai) · 个人维护

**连接本地 Ollama 模型的 Telegram 对话机器人**

基于 aiogram 的 Telegram bot，调用本地 Ollama API 的 LLM 模型回复用户消息。功能包括多语言基础翻译（默认译为英语、可关闭）、可清空的聊天会话、通过 dislike 按钮重新生成补全；模型切换为 WIP。运行方式：安装 Ollama 与 poetry 依赖、编辑 settings.py 配置后运行 main.py。README 提供俄语帮助视频，测试环境使用 llama2 等 Ollama 模型。

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

- 通过 Telegram 对话调用本地 Ollama LLM
- 聊天会话管理与补全重新生成（dislike 按钮）
- 基础多语言翻译（可关闭）

## 适用场景

- 在 Telegram 中使用本地 Ollama 模型进行对话问答
- 搭建私人本地 LLM 聊天机器人

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L2: Contains Telegram bot that interacts with the Ollama API LLM models to answer user messages
> L14: - Install Ollama

## 星数曲线

```mermaid
xychart-beta
    title "kirillzhosul/ollama-telegram-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8ebceeae67a3` · [字段定义](../../DATASET.md)*
