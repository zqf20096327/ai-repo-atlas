# Rushik-B/Clira

⭐ 20 · TypeScript · MIT · 推送 2026-04-25 · [GitHub](https://github.com/Rushik-B/Clira) · [官网](https://tryclira.com) · 个人维护

**开源自托管 AI 行政助理：代管邮件、日历与消息，动作需人工批准**

自托管的 AI 行政代理应用，可读取、搜索、起草并规划邮件、日历、文件与连接工具上的操作，覆盖 WhatsApp、Telegram、SMS 与网页聊天多渠道。采用 Planner/style 架构，style 层不允许引入事实；回复走确定性过滤、schema 校验 LLM 门控与人工审查草稿队列，任何动作不批准不执行。通过 Docker Compose 自托管，支持 MCP 服务器连接与用户自定义技能；Gmail 以 push/pull 模式接入并做确定性预过滤。默认 AI 提供方为 Google，也可经 OpenAI 兼容端点接入 OpenRouter、LM Studio、vLLM 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多渠道代理（WhatsApp/Telegram/SMS/网页聊天），所有动作需显式批准
- Planner/style 架构，style 阶段不允许添加事实
- Gmail push/pull 摄取与确定性预过滤
- Docker Compose 自托管，支持 MCP 服务器连接与用户技能扩展

## 适用场景

- 自托管一个处理邮件和日历的 AI 助理并人工把关每步操作
- 通过 WhatsApp 或 Telegram 对话管理收件箱与日程
- 生成经人工审查后再发送的邮件回复草稿

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L35: Clira is an AI executive agent that handles your email, calendar, and messaging across WhatsApp and Telegram. It pr
> L39: - Multi-channel agent across WhatsApp, Telegram, SMS, and web chat

## 星数曲线

```mermaid
xychart-beta
    title "Rushik-B/Clira 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5f1fd61e861e` · [字段定义](../../DATASET.md)*
