# OpenHands/OpenHands

⭐ 94,075 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/OpenHands/OpenHands) · [官网](https://openhands.dev) · 组织维护

**自托管的编码 agent 控制中心：运行与自动化 agent 任务**

Agent Canvas 是一个自托管的开发者控制中心，用于启动编码 agent 对话与自动化日常工作流（如生成报告发布到 Slack、将 GitHub issue 拆解为任务）。默认本地运行，可连接多个 agent 后端（本机、Docker、VM、云）；开箱支持 OpenHands agent，也兼容 Claude Code、Codex、Gemini CLI、Pi、OpenCode 等符合 ACP 协议的第三方 agent。后端由 Agent Server（REST API）提供，架构分散在多个仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 63,461 位贡献者
- 涨星:近 1 天 **+101**(自 20261016 起算)
- 安装:npm 包 `@openhands/agent-canvas` 月下载 17,530

## 能力要点

- 兼容 ACP 协议，可接入 OpenHands、Claude Code、Codex、Gemini CLI 等多个 agent
- 支持本地、Docker、VM、云等多种后端运行环境并可切换
- 支持定时或 webhook 触发的自动化工作流，集成 Slack、GitHub、Notion 等
- 提供 npm 全局安装与 Docker 镜像两种运行方式

## 适用场景

- 自托管一个持续运行的编码 agent 工作台
- 把 GitHub issue 自动拆解成任务或定时生成报告推送 Slack
- 在同一界面切换本地、Docker、云端的多个 agent 后端
- 团队共享一个 Agent Server 做代码审查和依赖更新

## 场景标签

`编码 Agent` `工作流自动化` `代码审查` · 领域:效率与自动化

## 证据(README 行号)

> L4:  The self-hosted developer control center for coding agents and automations.
> L186: Agent Canvas is powered by the OpenHands Agent Server, a REST API for running multiple agents on a single machine.
> L205: |`OpenHands/OpenHands`|Agent Canvas frontend, user-facing control center, backend selection, and local-stack orche

## 星数曲线

```mermaid
xychart-beta
    title "OpenHands/OpenHands 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 91210 --> 94335
    line [91470, 91581, 91658, 91730, 91806, 91915, 92009, 92108, 92204, 92273, 92348, 92426, 91730, 92961, 93144, 93247, 93341, 93421, 93467, 93523, 93606, 93665, 93759, 93846, 93922, 93962, 94075, 94075]
```

2026-10-22 91,470 → 2026-11-24 94,075（+2,605）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `82c2f8d3f35f` · [字段定义](../../DATASET.md)*
