# senjinthedragon/SillyTavern-Discord-Connector

⭐ 19 · JavaScript · AGPL-3.0 · 推送 2026-05-30 · [GitHub](https://github.com/senjinthedragon/SillyTavern-Discord-Connector) · 个人维护

**将 SillyTavern 角色接入 Discord 实时角色扮演的桥接扩展**

SillyTavern 的第三方扩展加桥接服务器：把 Discord 频道消息转发到 SillyTavern 的 AI 管线，由当前活跃角色生成回复并流式返回 Discord，支持图片与表情发送。提供斜杠命令控制角色、聊天、persona 等，回复支持 13 种语言。设计为私人服务器或小群共享同一角色与故事的场景，不适合每人独立聊天历史的大群。需自行搭建 Discord bot 与 Node.js v18+，配置允许用户 ID 列表防止公开触发生成；另有付费的 Telegram/Signal 插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Discord 消息经桥接服务器路由至 SillyTavern 生成角色回复，流式更新
- 完整斜杠命令集：切换角色、新聊天、persona、图像生成等
- 回复支持 13 种语言，每用户可用 /setlang 设置偏好
- 超过 Discord 上传限制的图片自动缩放后发送

## 适用场景

- 在自己的 Discord 服务器上与 SillyTavern 角色实时聊天
- 邀请少量好友围绕同一角色进行群组角色扮演
- 在手机上通过 Discord 应用继续 SillyTavern 对话

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: Bridge your SillyTavern character to Discord for real-time roleplay. Messages sent in a Discord channel are routed t
> L132: The extension runs inside SillyTavern's browser environment and connects to the bridge server. When a Discord mess

## 星数曲线

```mermaid
xychart-beta
    title "senjinthedragon/SillyTavern-Discord-Connector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f0b43bc155f3` · [字段定义](../../DATASET.md)*
