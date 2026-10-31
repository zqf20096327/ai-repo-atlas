# cyborg-garden/swarm-map

⭐ 26 · TypeScript · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/cyborg-garden/swarm-map) · [官网](https://nimbleco.ai) · 组织维护

**多租户异构 agent 运行时（Hermes/Letta）的统一管理编排平台**

面向需要在服务器上长期运行多个 AI agent 的个人与小团队的 Web 控制平面：用 Next.js 单一仪表盘同时管理两种形态的 agent 运行时——Hermes（每 agent 一个容器，部署多租户 fork cyborg-garden/hermes-agent-mt）与 Letta（共享服务器上以行存储的 memory-first agent）。提供创建向导、模型级联降级（如 Claude→Gemini→本地 Ollama）、平台接入（Telegram/Signal/Mattermost）、按 key 的预算限制、AES-256-GCM 密钥加密、审批与审计日志，并开放 REST API 供其他 agent 编排。限制：Letta 支持目前为只读+发消息，预算不覆盖经 Hermes 前端代理的 Letta 调用；面板内无按用户的角色分离。需 Node.js 18+ 与本地 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单界面同时管理 Hermes（容器型）与 Letta（共享服务器行型）两类 agent 运行时
- 模型级联降级链（含回退到本地 Ollama）+ 每 agent 预算上限
- 多租户安全：内存按上下文隔离、群组审批策略、AES-256-GCM 密钥加密、审计日志
- REST API 允许任意 AI agent（如 Claude Code、Hermes）无 GUI 编排整个 fleet

## 适用场景

- 我一个人在服务器上跑多个不同用途的 agent，想从一个面板统一部署和监控
- 小团队给每人配 Mattermost 助手，由负责人管理 API key、成本与群组接入审批
- 让 Claude Code 等外部 agent 通过 REST API 自动重启、克隆、级联调整我的 agent 集群

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Multiplayer admin and orchestrator platform for heterogeneous agent runtimes.** One dashboard for two shapes of ag
> L20: Swarm Map is the control plane. One UI to deploy, configure, and manage a fleet of agents — each with its own perso
> L22: It also gets harder when your agents aren't all the same *shape*. A Hermes agent is a container you can start, stop

## 星数曲线

```mermaid
xychart-beta
    title "cyborg-garden/swarm-map 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1a48469b9309` · [字段定义](../../DATASET.md)*
