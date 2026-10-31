# techwithanirudh/discord-ai-bot

⭐ 16 · TypeScript · MIT · 推送 2026-05-02 · [GitHub](https://github.com/techwithanirudh/discord-ai-bot) · 个人维护

**拟人化 AI Discord 聊天机器人，基于 Vercel AI SDK 与 Bun**

用 TypeScript 与 Bun 构建的 Discord 机器人，通过 Vercel AI SDK 生成拟人化对话回复，README 称其表现几乎与真人不可区分。技术栈包含 Exa AI（搜索）、Mem0（记忆）、discord.js 等。面向想在 Discord 服务器部署 AI 对话机器人的开发者：需先创建 Discord Bot，配置 .env 环境变量，用 Bun 安装依赖并启动开发服务器。以源码形式提供，AGPL-v3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Vercel AI SDK 生成拟人化对话
- 集成 Mem0 提供记忆、Exa AI 提供搜索
- 使用 Bun 运行时与 discord.js 构建

## 适用场景

- 在 Discord 服务器部署一个能自然对话的 AI 成员
- 为社区提供拟人化的自动回复体验

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12: A human-like bot that is almost indistinguishable from a real person.
> L18: - [Vercel AI SDK][ai-sdk]

## 星数曲线

```mermaid
xychart-beta
    title "techwithanirudh/discord-ai-bot 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [16, 15, 16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `daf41f1fb573` · [字段定义](../../DATASET.md)*
