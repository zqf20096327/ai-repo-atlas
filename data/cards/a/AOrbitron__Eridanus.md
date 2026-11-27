# AOrbitron/Eridanus

⭐ 219 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/AOrbitron/Eridanus) · [官网](https://eridanus.netlify.app) · 个人维护 · 中文 README

**OneBot 协议多功能 QQ/多平台 bot 框架**

基于 OneBot v11 协议与事件驱动 Hub 的多端桥接 bot 框架：通过 WebUI 服务端作为 WebSocket Hub 中转，将 QQ、Telegram、WebUI 与 Android 悬浮窗应用统一接入，所有消息规范化为标准 OneBot 事件，插件单实例加载共享上下文。主题标签显示以 LLM function calling 构建功能调用机制，支持纯 Live2d 桌宠模式（不接入 QQ）。部署方式见文档，提供 Telegram 相册合并、文件原样传输、跨端 /bind 上下文绑定等能力。许可为 CC BY-NC-SA 4.0，禁止商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OneBot v11 协议多端统一桥接：QQ/Telegram/WebUI/Android 共享上下文
- 单实例多客户端：插件仅加载一次，无需多平台重复拉起 Bot
- LLM function calling 功能调用机制（主题标签）
- 支持不接入 QQ 的纯 Live2d 桌宠模式

## 适用场景

- 搭建同时服务 QQ 与 Telegram 的机器人
- 跨端会话绑定与长期记忆互通
- 作为桌宠/悬浮窗助理运行

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: _🎊 基于 OneBot 协议的多功能bot兼python开发框架 🎊_
> L33: Eridanus 采用基于 **OneBot v11 协议标准**与**事件驱动中心 Hub** 的多端统一桥接架构：无需重复启动多份 Bot 核心插件，通过 WebUI 服务端作为 WebSocket Hub 中转，实现 QQ、

## 星数曲线

```mermaid
xychart-beta
    title "AOrbitron/Eridanus 星数(近 11 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-15", "2026-11-19", "2026-11-27"]
    y-axis "stars" 207 --> 220
    line [208, 209, 210, 211, 208, 214, 215, 216, 217, 219, 219]
```

2026-10-25 208 → 2026-11-27 219（+11）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `48832cf63715` · [字段定义](../../DATASET.md)*
