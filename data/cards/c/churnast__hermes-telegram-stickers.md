# churnast/hermes-telegram-stickers

⭐ 5 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/churnast/hermes-telegram-stickers) · 个人维护

**让 Hermes agent 用 Telegram 贴纸回复的插件**

面向 Nous Research 开源 Hermes Agent 的插件：为 Telegram 网关上的 bot 提供四个贴纸工具、/stickers 命令组、礼仪技能与回合提示钩子，使 agent 能按 emoji、按语义描述或按贴纸包名挑选贴纸，作为对应话题中的回复发出，并带冷却与消息间隔等拟人节奏控制。默认内置四个 Telegram 官方贴纸包，可经对话学习或配置指定贴纸包；语义挑选依赖 vision 模型为贴纸生成描述。安装要求 Hermes Agent 0.20.6 及以上并已完成 Telegram 网关配置，无需额外 Python 包。

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

- 按语义/emoji/贴纸包名挑选贴纸并作为话题内回复发送
- 四类贴纸包来源：内置默认包、配置指定、对话学习、可随时恢复默认
- 冷却秒数与最少消息间隔控制发送节奏，/stickers off 为不可被 agent 绕过的关闭开关
- 可选 vision 模型批量描述贴纸（每次默认 30 张）以支持语义匹配

## 适用场景

- 让 Telegram bot 在合适场合用贴纸回应玩笑与情绪
- 自选或让 bot 从我发送的贴纸中学习贴纸包
- 限制 bot 在某些聊天中不发贴纸

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13: Hermes Agent is an open-source AI agent from Nous Research; on Telegram it talks as your bot. Out of the box it can
> L58: **What it adds:** four tools, the `/stickers` command, a skill and a hook that adds a short sticker hint on Telegra

## 星数曲线

```mermaid
xychart-beta
    title "churnast/hermes-telegram-stickers 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-20 5 → 2026-11-22 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `87e32fe6b30c` · [字段定义](../../DATASET.md)*
