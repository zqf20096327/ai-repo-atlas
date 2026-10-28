# floomhq/floom

⭐ 47 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/floomhq/floom) · [官网](https://floom.dev) · 组织维护

**自托管 AI Worker 运行时：定时/触发执行带审批与日志的后台智能体**

Floom 是一个开源的 AI worker 运行时：以文件夹（worker.yml + run.py 或 SKILL.md）定义 worker，支持手动、cron 定时、webhook 和 Composio 事件触发执行。脚本类 worker 在 E2B 沙箱 microVM 中运行，agent 类通过 API 进程内的 AgentDriver 执行（仅限受信 bundle）。每次运行记录日志、输出、工具调用、审批状态，支持回放与回滚；带副作用操作可设置人工审批门。提供 Next.js UI、REST API、MCP 服务器与 CLI；技术栈为 FastAPI + SQLite，需 Python 3.11+、Node 20+、模型 provider key 与 E2B key，另有托管版 floom.dev。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- worker 以文件夹形式定义（worker.yml + run.py/SKILL.md），经 validate/push 部署
- 脚本 worker 在 E2B 沙箱 microVM 隔离运行，密钥不注入沙箱
- 人工审批门 + 工具白名单 + 运行记录（日志/回放/回滚）
- 同时暴露 UI、REST API 与 MCP 端点，可从 Claude Code/Codex/CLI 操作

## 适用场景

- 把周期性知识工作（PR 摘要、收件箱分诊、监控）交给定时运行的 agent
- 让非开发者通过 UI 运行开发者部署的 Python 脚本 worker
- 要求所有副作用操作经人工审批并留审计记录的团队自动化
- 把 Python 脚本同时发布为应用、REST API 和 MCP 工具

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L115: |**What it is**|Self-hosted runtime to create, run, and supervise background AI agents|
> L123: |**Stack**|Next.js + Tailwind UI · FastAPI + SQLite API · MCP server + CLI|
> L217: Floom is an open-source runtime for background AI workers that run from versioned worker folders with declared inp

## 星数曲线

```mermaid
xychart-beta
    title "floomhq/floom 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-28 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `932c8ac5ec49` · [字段定义](../../DATASET.md)*
