# AnnenkovLabs/girl-agent

⭐ 351 · TypeScript · NOASSERTION · 推送 2026-07-18 · [GitHub](https://github.com/AnnenkovLabs/girl-agent) · [官网](https://oss.girl-agent.com/) · 个人维护 · 中文 README

**Telegram AI 女友人格引擎：睡眠、日程、记忆与关系状态**

面向终端用户的 Node.js AI 虚拟女友引擎：行为由多层状态（presence 在线模式、睡眠、每日日程、五个关系计数器、九个亲密阶段、冲突系统、long-term.md 长期记忆）组装而成，而非单一 system prompt。支持 Userbot 模式，通过 MTProto 使用真实 Telegram 账号读取、打反应、输入中、删改消息；内置 Anti-AI 提示词约束输出风格；Agenda 层可主动发消息。安装提供一键脚本、npx、npm 全局、Docker 与桌面二进制（Rust 客户端）。README 声明处于 beta，许可为 source-available，禁止商业使用与付费托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多层状态驱动行为：presence/睡眠/日程/冲突/九阶段关系
- MTProto Userbot 模式：读取、打反应、输入中、删改消息
- 重要事件写入 long-term.md 并在后续对话中调用
- Agenda 层自主规划主动消息

## 适用场景

- 在 Telegram 上运行一个带作息与记忆的 AI 拟人角色
- 希望 AI 角色不即时回复、有真实在线节奏
- 需要长期记忆与关系阶段演进的虚拟伴侣

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **ИИ-девушка в Telegram, которая ведёт себя как человек.**
> L23: `girl-agent` — движок ИИ-персоны для Telegram. **Не промпт. Не GPTs. Не плагин.** Это полноценный агент со своим со

## 星数曲线

```mermaid
xychart-beta
    title "AnnenkovLabs/girl-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 349 --> 352
    line [350, 351, 351]
```

2026-10-18 350 → 2026-10-26 351（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8085c2796a57` · [字段定义](../../DATASET.md)*
