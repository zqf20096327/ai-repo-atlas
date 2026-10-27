# inercia/mitto

⭐ 34 · Go · 推送 2026-10-26 · [GitHub](https://github.com/inercia/mitto) · 个人维护

**跨设备管理多个 AI 编程 agent 会话的 CLI/Web/macOS 界面**

面向已安装 ACP 兼容 agent（Claude Code、Copilot CLI、Auggie 等）的用户的管理与访问层：支持多 agent、多工作区并行会话，提供会话历史恢复、父子会话委派、定时循环任务、消息队列、内置 MCP Server 与消息处理器等机制。界面包括原生 macOS 应用与浏览器（含手机/平板），支持 Cloudflare/ngrok 自动隧道与远程认证。本产品本身不是 AI 编程 agent，不提供模型输出。安装途径为 Homebrew、下载二进制或 Go 源码构建（需 Go 1.24+、Bun 1.2+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 ACP agent 与多工作区并行管理（Claude Code、Copilot CLI、Auggie 等）
- 父子会话委派与 Loop 定时会话（含 webhook/cron 回调触发）
- 内置 MCP Server 支持跨会话自动化与 agent 间编排
- 自动隧道（Cloudflare/ngrok）与限流、IP 封禁、受限 runner 等安全机制

## 适用场景

- 同时运行多个 AI 编程 agent 实例并在各自工作区切换
- 离开电脑后用手机或浏览器继续与 agent 对话
- 定时触发 prompt 自动生成日报或周期性检查
- 通过 MCP Server 做跨会话与 agent 间编排

## 场景标签

 · 领域:AI 编程工具/agent 基础设施

## 证据(README 行号)

> L10: **A modern interface for your team of AI coding agents**
> L18: So you have installed some ACP compatible agents, like Claude Code, or Copilot CLI, or Auggie, or any
> L35: - **Multi-Agent Support** — Connect to Claude Code, Copilot CLI, Auggie or any ACP-compatible agent

## 星数曲线

```mermaid
xychart-beta
    title "inercia/mitto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b05d668f8404` · [字段定义](../../DATASET.md)*
