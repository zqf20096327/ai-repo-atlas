# Giton22/kyllene

⭐ 210 · Kotlin · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Giton22/kyllene) · [官网](https://kyllene.app) · 个人维护

**Hermes Agent 的非官方 Android 原生聊天客户端**

Kotlin Multiplatform 编写的 Hermes Agent 移动客户端：直连用户自托管的 hermes dashboard 网关（服务器/家庭实验室/VPS/Tailnet），无独立服务器与账号。功能覆盖流式聊天（Markdown/代码/推理/工具活动）、审批与提权确认、子代理与后台进程管理、定时任务、bots 与房间、成本与 token 统计、可选端到端加密推送与语音通话。需要 Android 8.0+，通过 APK 安装；另有实验性桌面应用。独立项目，未获 Nous Research 认可。

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

- 直连自托管 hermes dashboard 网关，无账号、无中介服务器
- 审批/子代理/后台进程/检查点的手机端控制
- 可选端到端加密推送（经 ntfy），不依赖 Google 服务
- 聊天与登录信息用 Android Keystore 加密，含离线加密副本

## 适用场景

- 在手机上与自托管的 Hermes Agent 对话并跟进任务
- 通过通知远程批准 agent 的操作请求
- 在外网通过 Tailscale/加密推送查看 agent 运行状态

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **A native Android client for Hermes Agent.**
> L17: Kyllene connects to the `hermes dashboard` you already run on a server, homelab, VPS or Tailnet, the
> L18: same way Hermes Desktop's "Remote gateway" connection does. There is no Kyllene server and no account:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `615d293889e0` · [字段定义](../../DATASET.md)*
