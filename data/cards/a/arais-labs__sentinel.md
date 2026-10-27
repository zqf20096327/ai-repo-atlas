# arais-labs/sentinel

⭐ 23 · Python · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/arais-labs/sentinel) · 组织维护

**把聊天、桌面、终端与 agent 工具聚合到一个桌面应用的 AI 工作区**

面向个人用户的桌面 AI 工作区：在 Mac 上运行 Linux 工作区或经 SSH 连接远程机器，集成聊天、实时桌面查看、tmux 终端、文件管理、浏览器自动化与 agent 工具。支持流式响应、子 agent 委派、持久记忆、定时任务与事件触发，通过 Telegram 远程操控。可接入 Anthropic、OpenAI 或 Gemini；模块动作设有允许/审批/拒绝权限体系与紧急停止。macOS Apple Silicon 提供安装脚本与 DMG，源码含 Electron 桌面壳与独立 TUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Linux 工作区（本地 Apple Containerization 或 SSH 远程）与 agent 共享桌面、终端与文件
- 模块权限体系：允许/审批/拒绝，会话级审批与紧急停止
- 持久记忆、定时任务与事件驱动触发，Telegram 远程会话切换与转向
- 多实例部署，实例间独立数据库与 provider 配置，共享机器

## 适用场景

- 在一个桌面应用里跟进并介入 AI agent 的执行过程
- 让 agent 在隔离的 Linux 工作区里操作终端、文件与浏览器
- 通过 Telegram 远程指挥和延续正在进行的 agent 会话

## 场景标签

`AI 助手` `浏览器自动化` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: Sentinel brings chat, a live desktop, terminals, files, browser automation, and
> L25: |Agents|Stream responses, steer ongoing work, delegate to sub-agents, and resume conversations.|
> L31: Connect Anthropic, OpenAI, or Gemini in Settings using the supported API-key or

## 星数曲线

```mermaid
xychart-beta
    title "arais-labs/sentinel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a8a731d73418` · [字段定义](../../DATASET.md)*
