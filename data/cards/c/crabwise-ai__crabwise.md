# crabwise-ai/crabwise

⭐ 24 · Go · AGPL-3.0 · 推送 2026-04-05 · [GitHub](https://github.com/crabwise-ai/crabwise) · [官网](https://crabwise.ai) · 组织维护

**本地守护进程+CLI：监控、治理并审计本机 AI agent 活动**

面向个人开发者与 OpenClaw 用户的本地优先守护进程加 CLI，用于对 Claude Code、Codex CLI、OpenClaw 等 AI agent 做监控、审计与策略执行。通过 crabwise wrap 将 agent 流量路由到本地代理，在请求到达模型提供商前评估 YAML 策略（warn/block），并在 SQLite 中存储带哈希链的审计记录；使用本地 CA 证书检查 HTTPS 流量。控制面保留在本机，不依赖托管服务。当前为 v1，专注 Claude Code、Codex CLI 与 OpenClaw 相关工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地代理在请求到达模型提供商前执行 YAML 策略（warn/block）
- SQLite 哈希链审计记录，可本地核验完整性
- crabwise wrap 路由本地 agent，crabwise service inject 注入服务级 OpenClaw
- 提供 status/agents/watch/audit 终端命令与 Desktop/Discord 通知

## 适用场景

- 实时查看本机 AI agent 正在执行的操作
- 在危险动作或提供商调用前用本地策略拦截
- 保留可核验的 agent 活动审计历史

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L23: Crabwise is a local-first daemon plus CLI for monitoring, audit, and policy enforcement around AI agents. It watche
> L25: Built for solo developers, builders, and OpenClaw users. Current support is focused on Claude Code, Codex CLI, and 

## 星数曲线

```mermaid
xychart-beta
    title "crabwise-ai/crabwise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0d864fce81a1` · [字段定义](../../DATASET.md)*
