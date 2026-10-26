# garudust-org/garudust-agent

⭐ 30 · Rust · MIT · 推送 2026-07-27 · [GitHub](https://github.com/garudust-org/garudust-agent) · [官网](https://garudust-org.github.io/garudust-agent/) · 组织维护 · 中文 README

**自托管 Rust AI agent 运行时：持久记忆、技能自改进、多平台消息**

Rust 编写的自托管 AI agent 运行时，约 10 MB 单二进制、无运行时依赖。支持终端 TUI/一次性任务、7 个消息平台适配器（Telegram/Discord/Slack 等）、原生桌面应用与 Web 仪表盘，并暴露 REST + WebSocket API。支持 24 个 LLM 提供商切换、MCP 服务器接入、终端工具三种沙箱模式（直连/Docker/SSH）、定时任务与跨会话持久记忆，可自动沉淀可复用技能。安装提供脚本、预编译二进制与桌面安装包，或从源码 cargo 构建（Rust 1.87+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个 LLM 提供商一行配置切换，--hint 可路由到更廉价模型
- 7 个消息平台适配器同一进程运行，按平台 RBAC 与按用户会话隔离
- 终端工具三档沙箱：直连/Docker 容器/SSH 远程主机，附带硬性命令阻断
- MCP 服务器接入与社区工具/技能 Hub 安装机制

## 适用场景

- 在自己服务器上运行一个跨 Telegram/Discord/Slack 等 7 平台的 AI 助手
- 通过 SSH 沙箱让 agent 安全地管理远程主机或树莓派
- 以 headless API 形式把 agent 嵌入自己的应用并跑定时自主任务

## 场景标签

`AI 助手` `Agent 记忆` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: A self-improving AI agent runtime written in Rust — ~10 MB binary, no runtime dependencies. Chat in the terminal, r
> L120: 🌐 **Headless API** — `garudust-server` exposes `/chat`, `/stream`, and a WebSocket endpoint — embed in any app or 

## 星数曲线

```mermaid
xychart-beta
    title "garudust-org/garudust-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2cebcdec7584` · [字段定义](../../DATASET.md)*
