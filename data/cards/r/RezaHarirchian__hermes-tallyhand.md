# RezaHarirchian/hermes-tallyhand

⭐ 5 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/RezaHarirchian/hermes-tallyhand) · 个人维护

**把 Hermes Agent 接入 Twitch 聊天并以代码强制角色权限的插件**

Hermes Agent 的插件，将 agent 放入主播的 Twitch 聊天室，并把观众输入视为不可信数据：每个工具调用前在代码层做角色检查，房主、房管、观众各自可用不同工具；封禁、超10分钟超时等操作需房主在聊天中逐次批准（一次/会话/永久）。支持 !hermes 触发问答、OBS 场景切换与剪辑、免模型调用的聊天命令、观众笔记（!remember/!forgetme）与多语言回复。依赖 Hermes Agent 0.22.7+，仅支持 Twitch。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 角色权限在代码而非模型层面强制，工具调用前逐一检查
- 封禁类敏感操作需房主在聊天内批准，5分钟未确认不执行
- 注入防护：聊天文本作为引用数据，@file:/@url: 引用被破坏
- 支持 OBS 工具、自动剪辑、字幕化回答等可配置功能

## 适用场景

- 让 AI agent 进直播间回答观众提问且不越权执行操作
- 一句话完成切场景、打字幕、剪辑等直播操作
- 对观众可触发的命令做细粒度权限与冷却管理

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Tallyhand is a Hermes Agent plugin that puts the agent in your Twitch chat and treats that chat as untrusted input.
> L9: Anyone in a chat can type anything at the bot. Wired straight to chat, an agent follows whoever asked last, even whe
> L13: - Roles are enforced in code, not by the model: you, your moderators and your viewers get different tools, and a ch

## 星数曲线

```mermaid
xychart-beta
    title "RezaHarirchian/hermes-tallyhand 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-25"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-11 5 → 2026-11-25 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ea2655550cec` · [字段定义](../../DATASET.md)*
