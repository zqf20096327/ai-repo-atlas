# yammdd/tldr-bot

⭐ 3 · Python · 推送 2026-11-24 · [GitHub](https://github.com/yammdd/tldr-bot) · [官网](https://yammdd.github.io/tldr-bot/) · 个人维护

**Discord 服务器用户：把未读消息蒸馏成带出处的摘要**

运行在 Discord 上的摘要机器人：将 5 至 1,500 条未读频道消息处理为按发言人归属的结构化摘要，附可点击跳转链接与仅私聊可见的个人相关提醒。用户在服务器内通过 BYOK 方式自备 LLM API key，支持 Google Gemini、DeepSeek、OpenAI、Anthropic Claude、OpenRouter、Groq 及自定义端点，按 token 预算在单次调用与并行 Map-Reduce 两条路径间路由。密钥以 AES-256-GCM 加密存于 SQLite。提供 Railway、Docker Compose 与本地部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5–1,500 条消息的发言人归属摘要，含经校验的跳转链接
- BYOK：7 类预设 provider 与任意 OpenAI 兼容自定义端点，/model 可切换模型
- 密钥经 AES-256-GCM 加密存储，聊天消息不落盘
- /language 支持输出语言设置（en/vi/ja/ko/zh/auto）

## 适用场景

- 为新加入群组的人快速补读大量未读讨论
- 长时间空闲后了解频道关键进展
- 以指定语言输出频道摘要

## 场景标签

 · 领域:聊天社区工具/摘要

## 证据(README 行号)

> L5:  Distill 5 to 1,500 unread Discord messages into speaker-attributed summaries with verified jump links, powered by y
> L31: 3. **Configure once:** Run `/config`, choose a provider (Google Gemini, DeepSeek, OpenAI, Anthropic Claude, OpenRou


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a3f380f1f0a4` · [字段定义](../../DATASET.md)*
