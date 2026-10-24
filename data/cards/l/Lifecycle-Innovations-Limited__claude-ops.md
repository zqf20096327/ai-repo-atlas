# Lifecycle-Innovations-Limited/claude-ops

⭐ 545 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Lifecycle-Innovations-Limited/claude-ops) · [官网](https://github.com/Lifecycle-Innovations-Limited/claude-ops/wiki) · 组织维护

**把 Claude Code 变成企业运营操作系统的插件（68 技能/多 agent）**

以 Claude Code 插件形式交付的运营层：68 个技能覆盖晨报仪表盘、统一收件箱、自主 PR 合并、全 AWS 基础设施监控、收入（Stripe/RevenueCat）、电商（Shopify）、营销（Klaviyo/Meta/GA4）与语音（Twilio/Bland/ElevenLabs）等 22 项服务集成；通过 launchd 后台守护进程预热数据，技能用 shell 块在模型上下文加载前采集数据。提供 Claude Code marketplace 一键安装，也可经 installer 以 npm 脚本镜像到 Codex/Grok/Cursor 等多个 CLI。多处机制（launchd、Phone.app、Continuity）面向 macOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 68 个技能 + 专家 agent 路由，覆盖工程、业务、自动化与维护
- 22 项服务集成，多数提供 MCP OAuth 与 CLI 双通道
- launchd 后台守护进程预热数据，晨报从冷启动约 30s 降至 3s 内
- 跨 CLI 安装器可把技能镜像到 Codex/Grok/Cursor 等多个 CLI

## 适用场景

- 在 Claude Code 里一站式查看基础设施、CI、收入与 PR 状态
- 让自主 agent 处理收件箱、PR 合并与构建失败自动修复
- 统一管理跨 WhatsApp/Email/Slack/Telegram 的消息

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Business Operating System for Claude Code**
> L24: Turn Claude Code into a complete business operating system — infrastructure health, CI/CD status, unified inbox, op
> L77: git clone https://github.com/Lifecycle-Innovations-Limited/claude-ops.git

## 星数曲线

```mermaid
xychart-beta
    title "Lifecycle-Innovations-Limited/claude-ops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 545 --> 548
    line [546, 547, 547]
```

2026-10-18 546 → 2026-10-24 547（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6a50998b0588` · [字段定义](../../DATASET.md)*
