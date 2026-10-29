# Armanidrisi/chatgpt-telegram-bot-php

⭐ 18 · PHP · 推送 2026-06-29 · [GitHub](https://github.com/Armanidrisi/chatgpt-telegram-bot-php) · 个人维护

**PHP 编写的 Telegram ChatGPT 对话机器人，通过 OpenAI API 回复**

用 PHP 实现的 Telegram 机器人，调用 OpenAI API 生成回复。README 仅提供部署说明：在虚拟主机的文件管理器中编辑 index.php 填入密钥、上传文件，再通过 Telegram Bot API 的 setWebhook 接口设置 Webhook 即可运行。文档未说明支持的具体 OpenAI 模型、命令列表或依赖库，属于功能极简的个人项目。

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

- PHP 实现的 Telegram 机器人，调用 OpenAI API
- 提供虚拟主机（Shared Hosting）部署步骤
- 通过 Telegram setWebhook 接口接入消息

## 适用场景

- 在自有虚拟主机上搭建个人 ChatGPT Telegram 对话机器人

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L2: This Is A telegram Bot created using openai api coded in php
> L13: - ```https://api.telegram.org/bot<bottoken>/setWebhook?url=<You Uploaded File Url>```

## 星数曲线

```mermaid
xychart-beta
    title "Armanidrisi/chatgpt-telegram-bot-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `5b89d539dc43` · [字段定义](../../DATASET.md)*
