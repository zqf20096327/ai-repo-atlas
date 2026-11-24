# king-tri-ton/chatgpt-telegram-bot

⭐ 10 · Python · MIT · 推送 2026-05-15 · [GitHub](https://github.com/king-tri-ton/chatgpt-telegram-bot) · [官网](https://t.me/ChatGPTTlgrmBot) · 个人维护

**通过 Telegram 付费访问 GPT-5.1 的机器人**

以 Python 编写的 Telegram 机器人，用户在 Telegram 中发送消息（10–4000 字符）即可获得 GPT-5.1 生成的回复，无需注册。采用 Telegram Stars 计费（1 Star=1 次请求），新用户获 3 次免费请求，支持 1–100 次的批量购买与促销码；内置 SQLite 数据库记录用户、请求与支付，提供管理员命令查看统计、赠送请求和管理促销码。需自行配置 OpenAI API key 与 Bot token，运行 Python 3.7+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram Stars 内置计费，1 Star 兑换 1 次请求，附 3 次免费试用与促销码系统
- 管理员命令：使用统计、按 ID 赠送请求、促销码增删查
- SQLite 存储用户、请求与支付历史，回复前显示"正在输入"状态与消息长度校验

## 适用场景

- 在 Telegram 里直接向 GPT-5.1 提问，不想订阅 ChatGPT 月费
- 以按次付费方式让他人使用自己的 OpenAI API 额度
- 为自己的机器人运营收集用户与收入统计

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Телеграм-бот для доступа к GPT-5.1 через OpenAI API с монетизацией через Telegram Stars.
> L51: * **Умные ответы** — генерация сообщений с GPT-5.1.

## 星数曲线

```mermaid
xychart-beta
    title "king-tri-ton/chatgpt-telegram-bot 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-22 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `e4b538f4f366` · [字段定义](../../DATASET.md)*
