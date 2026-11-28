# benjaminLedel/covey

⭐ 10 · Go · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/benjaminLedel/covey) · [官网](https://covey.work) · 个人维护

**自托管平台：像管理员工一样在企业内运行 AI agent**

面向组织（IT、安全、团队负责人等多角色集中管理）的自托管 agent 运行平台：每个 agent 拥有独立 Docker 沙箱、凭据、backlog 与组织架构位置。由控制平面（Go 单二进制 + Postgres/pgvector）与可弃式数据平面沙箱组成，通过 daemon 协议对接可替换的运行时（Claude Code、Codex、SevenCode、educa AI）。守卫规则在运行时之外集中强制执行，秘密经 broker 短期下发，全程录像并支持一键停机。Docker Compose 一键部署，或经安装脚本装二进制；首个版本发布于 2026 年 8 月，由一人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每 agent 独立沙箱、身份、凭据与 backlog，空闲不消耗计算
- 守卫规则集中强制、fail-closed，秘密经 broker 短期下发
- 运行时可换：daemon 协议 + 薄适配器对接 Claude Code/Codex 等
- 全程运行录像、按 agent/模型计费统计、组织级 kill switch

## 适用场景

- 企业内让 agent 自主处理支持队列、开发工单或 QA 走查
- 集中管理多个 AI agent 的权限、预算与审批
- 需要审计录像与紧急停机能力的 agent 部署场景

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L27: covey is a self-hosted platform for running AI agents inside a company. You create an agent, give it access to the 
> L114: Inside each sandbox a small **daemon** speaks a single protocol to the control plane, and an **adapter** starts th
> L143: 3. **Runtime-agnostic.** One daemon protocol plus thin adapters instead of framework lock-in.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `08a3b18d3349` · [字段定义](../../DATASET.md)*
