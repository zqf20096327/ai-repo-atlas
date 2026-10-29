# RandyChen1985/openclaw-buddy

⭐ 70 · TypeScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/RandyChen1985/openclaw-buddy) · [官网](https://github.com/RandyChen1985/openclaw-buddy) · 个人维护 · 中文 README

**OpenClaw AI Agent 的 Web 管理台：可视化管理、在线聊天与自愈守护**

基于 Go + Gin + React 的 OpenClaw 网关管理面板，面向非技术用户提供 Bot/模型/插件/渠道的可视化配置，替代 CLI 操作。Chat V3 将聊天、Workspace 文件编辑、Skills 技能与远程终端（PTY）整合在同一界面，支持流式输出与 iframe 纯净嵌入（?embed=true）。独立进程运行，网关崩溃时可远程重启、回滚，心跳探针触发多阶段自愈，事件经 SQLite 持久化。提供 RESTful API 与 WebSocket 日志流，从源码构建部署，需 Go 1.22+ 与 Node.js 18+ 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天、Workspace 文件、Skills、Console 终端同屏的 Chat V3 工作台
- Bot/模型/插件/渠道（微信/飞书/Telegram/QQ Bot）可视化管理，微信扫码流式捕获二维码
- 独立守护进程：心跳探针、多阶段自愈、自动回滚与备份快照
- RESTful API、WebSocket 日志流与 iframe 嵌入（token/bot/user 参数）

## 适用场景

- 不会 CLI 也能在浏览器里管理 OpenClaw 的机器人、模型和渠道
- 边聊天边改文件、调技能、开终端的一体化操作
- 网关异常时远程重启与自动回滚恢复
- 把聊天窗口嵌入到自己的业务系统或监控大屏

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12: **OpenClaw Buddy** 是专为 **OpenClaw（小龙虾 AI Agent）** 打造的 **零门槛 Web 管理台与对话伴侣**。
> L34: - **🛡️ 独立守护**：Buddy 独立进程运行；即使 OpenClaw 网关崩溃，仍可远程重启、回滚并救回系统。
> L84:        [ OpenClaw Buddy Server ] (Go + Gin + React)

## 星数曲线

```mermaid
xychart-beta
    title "RandyChen1985/openclaw-buddy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-29 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3804c0d9fcbf` · [字段定义](../../DATASET.md)*
