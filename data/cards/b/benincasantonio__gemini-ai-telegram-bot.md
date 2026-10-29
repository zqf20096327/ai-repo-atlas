# benincasantonio/gemini-ai-telegram-bot

⭐ 18 · Python · 推送 2026-05-23 · [GitHub](https://github.com/benincasantonio/gemini-ai-telegram-bot) · [官网](https://gemini-ai-telegram-bot-elfw.vercel.app) · 个人维护

**基于 Gemini 的 Telegram 聊天机器人，支持插件与多模态**

Python 编写的 Telegram 聊天机器人：通过 Google Generative AI（Gemini）生成回复，默认模型 gemini-2.5-flash，支持图像与文本多模态识别、聊天历史上下文（可配置条数上限）、天气/股票等插件扩展。后端使用 FastAPI 与 async SQLAlchemy，通过 Telegram webhook 接收消息，支持一键部署到 Vercel，或本地用 uvicorn 运行；数据库迁移使用 Alembic，兼容 PostgreSQL 与 SQLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 多模态 API，识别图像与文本
- 插件系统（DateTime/天气/股票等）
- 聊天历史上下文模式，可配置最大历史条数
- 支持 Vercel 一键部署与 webhook 安全令牌校验

## 适用场景

- 在 Telegram 中与 Gemini 模型对话
- 通过插件扩展机器人功能（天气、股票等）
- 部署到 Vercel 作为 serverless 机器人运行

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: This project is a chatbot application that uses Google's Generative AI (Gemini) to generate responses. It is built w
> L64: - [x] Implement Gemini model

## 星数曲线

```mermaid
xychart-beta
    title "benincasantonio/gemini-ai-telegram-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7a110b4662fb` · [字段定义](../../DATASET.md)*
