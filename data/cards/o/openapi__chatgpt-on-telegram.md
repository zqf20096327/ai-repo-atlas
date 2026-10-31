# openapi/chatgpt-on-telegram

⭐ 14 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/openapi/chatgpt-on-telegram) · [官网](https://console.openapi.com) · 组织维护

**把 Telegram 机器人接入 ChatGPT 对话的 Python 桥接服务**

极简 Python HTTP 服务器，通过无状态 webhook 流程把 Telegram 机器人连接到 GPT：设置时校验 Telegram token、加密存储机器人配置并注册 webhook，由单一 HTTP 服务实例处理更新。用户在网页填入 ChatGPT Prompt ID、Telegram Bot Token 与 OpenAI API Key 即可创建机器人链接。聊天上下文仅回传最近一小时消息，敏感字段用 SERVER_SECRET_KEY 静态加密。支持 ngrok 本地隧道、Docker 部署与反向代理。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无状态 webhook 流程，单 HTTP 实例处理所有机器人更新
- 机器人配置与会话状态静态加密存储于 DATA_PATH
- 上下文仅回传最近一小时消息，更早消息不发送给 OpenAI
- 提供 ngrok 本地隧道、Docker 与反向代理部署方式

## 适用场景

- 为 Telegram 机器人接入 GPT 对话能力
- 本地通过 ngrok 隧道开发调试 Telegram AI 机器人
- 以 Docker 在生产环境部署 Telegram-GPT 桥接服务

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5:  ChatGPT on Telegram
> L12: Minimal Python server that connects Telegram bots to GPT through a stateless
> L48: Open `http://127.0.0.1:8000`, fill in `ChatGPT Prompt ID`,

## 星数曲线

```mermaid
xychart-beta
    title "openapi/chatgpt-on-telegram 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f1f27320eef6` · [字段定义](../../DATASET.md)*
