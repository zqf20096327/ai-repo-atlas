# JusticeFist/alfatherapp

⭐ 21 · Kotlin · MIT · 推送 2026-11-24 · [GitHub](https://github.com/JusticeFist/alfatherapp) · 个人维护

**Hermes Agent 的原生 Android 与 Wear OS 客户端**

登录用户自建的 Hermes dashboard，把 agent 带到手机与手表上：流式 Markdown/代码/LaTeX/Mermaid 聊天、命令审批、任务看板与定时任务、Bot 分组、Pulse 主动卡片、语音听写与唤醒词、按电源键唤起的手机控制助手（涉支付/删除需确认）。需自备可访问的 Hermes 主机并安装 conduit_push 插件；发布版 APK 无推送，推送需自行编译并配 Firebase relay。提供 release APK 与 Gradle 源码构建两种方式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天支持排队、插话与中断正在运行的回合，含模型与推理选择器
- 电源键唤起助手，通过无障碍服务控制手机并内置支付/删除类确认门槛
- 端到端加密的 FCM 推送与数据共享（推送需自建 Firebase relay）
- Wear OS 语音问答、磁贴与表盘复杂功能

## 适用场景

- 在手机上与自托管的 Hermes agent 聊天并审批其命令
- 通过看板与定时任务管理 agent 的工作
- 戴手表时用语音直接向 agent 提问

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L9:  A native Android client for Hermes Agent, with a Wear OS companion.
> L23: |**Chat**|Streaming replies with Markdown, code, LaTeX, Mermaid, images and files. Model and reasoning picker; queu
> L49: - A Hermes host running the web dashboard (`hermes dashboard`, port 9119 by default) that your phone can reach


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `acf3bcbcb0fe` · [字段定义](../../DATASET.md)*
