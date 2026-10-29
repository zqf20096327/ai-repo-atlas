# mitumh3/tlg-chatbot-render

⭐ 27 · Python · MIT · 推送 2026-08-14 · [GitHub](https://github.com/mitumh3/tlg-chatbot-render) · 个人维护

**接入 OpenAI 的 Telegram 聊天机器人，可免费部署到 Render**

基于 Python（uvicorn/FastAPI 风格入口）的 Telegram 聊天机器人，通过 OpenAI API（gpt-3.5-turbo）生成对话回复。功能包括私聊与群聊（/slave 命令触发）、/bash 执行 bash 脚本、/clear 清空会话、/search 调用 DuckDuckGo 搜索并由 OpenAI 汇总。提供完整指南：注册 Telegram bot、配置 OpenAI key、本地运行与在 Render 上免费 24/7 部署。限制：Render 免费实例每 15 分钟重置，部署初期私聊可能出现自回复循环消耗额度。

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

- 通过 OpenAI API 生成对话回复（gpt-3.5-turbo）
- /search 调用 DuckDuckGo 并由 OpenAI 汇总结果
- /bash 命令在服务器上执行 bash 脚本
- 提供在 Render 免费实例上 24/7 部署的步骤

## 适用场景

- 搭建一个接入 OpenAI 的个人 Telegram 聊天机器人
- 在群聊中通过命令与 AI 机器人交互
- 零成本把 bot 部署到 Render 长期运行

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This is a project to create a Telegram chatbot that is integrated with OpenAI to enable natural language processing 
> L93: - Private chat: You can freely chat with the bot using the bot username (@your_bot_username) derived from the BotFa

## 星数曲线

```mermaid
xychart-beta
    title "mitumh3/tlg-chatbot-render 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5d02df39da4c` · [字段定义](../../DATASET.md)*
