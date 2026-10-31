# Skyzi000/openclaw-open-webui-channels

⭐ 57 · TypeScript · MIT · 推送 2026-04-19 · [GitHub](https://github.com/Skyzi000/openclaw-open-webui-channels) · 个人维护

**让 OpenClaw 以用户身份接入 Open WebUI 频道的插件**

OpenClaw 的连接插件：通过 REST API 与 Socket.IO 将 OpenClaw 接入 Open WebUI 的 Channels 功能，使其以专用 bot 用户身份在频道中收发消息。支持双向消息、文件上传下载、线程与回复、表情回应和输入中提示。安装可由 OpenClaw 自动克隆安装或手动 git clone 后用 openclaw plugins install 安装。限制：发送者控制（如允许列表）尚未实现，任何能访问频道的用户均可向 OpenClaw 发指令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- REST API + Socket.IO 实时双向消息
- 支持文件/媒体上传下载、线程、表情回应、输入指示
- 可通过对话让 OpenClaw 自动完成安装与配置
- 配置写入 ~/.openclaw/openclaw.json 并由 openclaw gateway restart 生效

## 适用场景

- 在 Open WebUI 频道里 @ 机器人与 OpenClaw 对话
- 让 OpenClaw 在团队频道中收发文件并参与线程讨论
- 为自托管 Open WebUI 增加一个 agent 成员

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: A plugin that connects OpenClaw to Open WebUI Channels. Enables OpenClaw to act as a user within Open WebUI and enga
> L42: openclaw plugins install ./openclaw-open-webui-channels

## 星数曲线

```mermaid
xychart-beta
    title "Skyzi000/openclaw-open-webui-channels 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-31 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `feca982fd577` · [字段定义](../../DATASET.md)*
