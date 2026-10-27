# Kevin-Liu-01/Agent-Machines

⭐ 30 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Kevin-Liu-01/Agent-Machines) · [官网](https://agent-machines.dev) · 个人维护

**多 agent 运行时与沙箱的编排控制平面（SDK/CLI/仪表盘）**

为 agent harness 提供源码级构建块：通过共享适配层安装运行 Claude Code、Codex、Hermes、OpenClaw 四种 agent 运行时，并在 Daytona、E2B、Sprites、Vercel Sandbox 四种沙箱上供给、执行与销毁机器。提供直接多路复用 SDK、生命周期内核（期望状态记录与调和）、托管 SDK、CLI 与浏览器终端仪表盘，内置 161 个技能与 39 个 MCP 服务目录。自托管部署需 Clerk 与 Supabase 配置；直接 SDK 用自己的 provider 密钥即可，无需托管账户。

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

- 四种运行时适配器（Claude Code/Codex/Hermes/OpenClaw）×四种沙箱 provider 适配器
- 三层 SDK 入口：直接 mux、生命周期内核（desired state + 调和恢复）、托管客户端
- 浏览器终端仪表盘管理与重连真实 agent CLI 会话
- 内置 161 技能与 39 MCP 服务目录，支持调度（cron）与多 Worker 生命周期管理

## 适用场景

- 用一套控制平面在多个沙箱上运行不同 agent CLI 并管理生命周期
- 在自有代码中集成 runtime/compute 适配器与期望状态调和
- 通过浏览器终端远程操作与监管多个持久 agent 工作区

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L26: |Runtime adapters|Install and run Claude Code, Codex, Hermes, or OpenClaw through a shared boundary|Runtime adapter
> L27: |Compute adapters|Provision, execute, inspect, and tear down machines on Daytona, E2B, Sprites, or Vercel Sandbox|P
> L31: |Lifecycle and multiple-agent dashboard|Manage configured workspaces, launch operations, schedules, files, logs, an

## 星数曲线

```mermaid
xychart-beta
    title "Kevin-Liu-01/Agent-Machines 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5eb1d7813b38` · [字段定义](../../DATASET.md)*
