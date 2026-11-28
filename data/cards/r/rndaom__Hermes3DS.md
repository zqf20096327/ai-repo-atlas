# rndaom/Hermes3DS

⭐ 3 · C · MIT · 推送 2026-11-27 · [GitHub](https://github.com/rndaom/Hermes3DS) · [官网](https://github.com/rndaom/Hermes3DS/releases/latest) · 个人维护

**在 3DS 掌机上与 Hermes Agent 对话的家庭brew客户端**

由两部分组成：运行在 Nintendo 3DS 上的 homebrew 聊天应用（.3dsx/.cia），以及安装在电脑端 Hermes 网关上的 3ds-platform 插件。插件把 3DS 作为 Hermes Agent 的一个聊天平台接入，聊天回复流式显示在上屏，支持工具调用展示、命令审批/问答、多 Bot（Hermes profile）会话、文件查看、语音消息与拍照发送。3DS 与电脑通过 Wi-Fi 自动发现，配对后使用 Noise IK 端到端加密，远程可经 Tailscale Funnel 连接。需要已破解（Luma3DS）的 3DS 与运行 Hermes Agent 0.22.5+ 的电脑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3DS 上流式聊天，支持审批、会话/技能/定时任务管理与模型切换
- 按住 Y 录语音、拍照发送，电脑端 Hermes 转录与识图
- Noise IK 端到端加密与配对机制，支持 Tailscale 远程接入
- 多 profile（Bot）聊天，3DS 上可创建克隆 Bot

## 适用场景

- 在 3DS 掌机上随时与家里的 Hermes Agent 对话
- 在客厅用 3DS 审批 Agent 的命令执行请求
- 外出时通过 Tailscale 继续使用同一会话

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L11: Hermes 3DS is a homebrew app for the 3DS plus a small plugin for the Hermes gateway on your computer. Replies
> L63: The plugin makes the 3DS one more chat platform for your Hermes gateway: the same agent, with the same tools


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `25a976686953` · [字段定义](../../DATASET.md)*
