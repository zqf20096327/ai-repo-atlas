# zzh1996/chatgpt-telegram-bot

⭐ 52 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/zzh1996/chatgpt-telegram-bot) · 个人维护

**在 Telegram 中使用多种大模型的聊天机器人**

基于 Telegram 的 ChatGPT 对话机器人：通过消息前缀触发与切换模型，默认使用 GPT-4，$$ 前缀切换 GPT-3.5-Turbo。支持流式实时输出、并发请求、长消息分段、自动重试、数据库持久化与可分叉的对话历史、消息队列、群组白名单管理、图片与文本文件输入及富文本渲染。通过分支支持 OpenAI GPT、Google Gemini、Anthropic Claude、智谱 GLM-4 等模型，另有 GPTs 式系统前缀与 Function calling 插件分支。以 docker-compose 部署，需配置 OpenAI API key 与 Telegram 凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式实时输出与消息前缀切换模型
- 数据库持久化、可回复分叉的对话历史
- 图片与文本文件多模态输入
- 分支支持 GPT/Gemini/Claude/GLM-4 及 Function calling 插件

## 适用场景

- 在 Telegram 私聊或群组中使用 GPT 等大模型对话
- 通过回复历史消息分叉延续不同对话线
- 管理员以白名单控制机器人在群组中的启用

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L18: 1. **Real-time output streaming** - Receive AI model outputs while they are being generated using the message editi
> L38: 1. You can interact with your bot by initiating a new conversation with a message that starts with `$`. For example

## 星数曲线

```mermaid
xychart-beta
    title "zzh1996/chatgpt-telegram-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `40002005d838` · [字段定义](../../DATASET.md)*
