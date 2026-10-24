# HCF-STUDIOS/openhermit

⭐ 88 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/HCF-STUDIOS/openhermit) · [官网](https://openhermit.ai) · 组织维护

**将 AI agent 集群部署为生产服务的开源平台**

开源的 agent 基础设施平台，将内部状态（会话、记忆、指令、技能、MCP、密钥、调度）集中存于 PostgreSQL，按 agent_id 隔离；外部工作区运行在按 agent 划分的沙箱中，可选自托管 Docker、E2B、Daytona 或 Tenki 后端。提供 Hono 网关、CLI 与 Web 管理 UI、Telegram/Discord/Slack 等渠道适配器、cron 调度、多用户角色，以及带预算控制和证据引用的 Deep Research 流水线。通过 npm 安装，本地模型需 64k+ 上下文，官方说明 7–8B 模型常无法通过 JSON 校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内部状态集中 PostgreSQL、按 agent_id 隔离，外部状态在可插拔沙箱后端（Docker/E2B/Daytona/Tenki）
- CLI 支持 fleet 级扇出操作（技能/MCP/指令/密钥全 fleet 下发）
- Deep Research 流水线：预算硬上限、证据引用、可暂停恢复
- 内置 Telegram/Discord/Slack 适配器与多用户角色体系

## 适用场景

- 为团队或 SaaS 客户运行多 agent 生产服务
- 通过 Telegram/Discord/Slack 等渠道向用户交付 agent
- 对 agent 集群做统一的技能、密钥与调度运维

## 场景标签

 · 领域:AI agent 基础设施

## 证据(README 行号)

> L5: Open-source platform for deploying fleets of AI agents as production services — durable state, sandboxed execution, 
> L25: - **Internal state** — sessions, memories, instructions, skills, MCP servers, schedules, secrets, users — lives in 
> L43: - 🐳 **Sandboxed execution** — per-agent sandbox: self-hosted Docker, E2B, Daytona, or Tenki. Code runs isolated fro

## 星数曲线

```mermaid
xychart-beta
    title "HCF-STUDIOS/openhermit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-24 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c5211c0be0da` · [字段定义](../../DATASET.md)*
