# SapienXai/AgentOS

⭐ 141 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/SapienXai/AgentOS) · [官网](https://agentos.sapienx.app/) · 组织维护

**OpenClaw 的代理运行控制平面：集中管理 AI 数字员工团队**

AgentOS 是一个开源的操作层，构建于 OpenClaw 代理运行时之上，面向需要同时运行多个 AI 代理的人员。功能包括创建工作区与数字员工、分配即时/定时/周期性任务、查看执行记录与 token 用量、连接 Telegram/Discord/Slack 等渠道，以及通过审批与诊断机制保持人工监督。自身不替代 OpenClaw，仅读取其 Gateway 状态并转发操作；浏览器账户等功能处于 MVP 阶段，部分账户访问规则被有意阻断。提供 CLI、桌面安装包与 Railway 部署路径。

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

- 基于 Next.js/React/TypeScript 的操作界面，读取 OpenClaw Gateway 实时状态
- 支持即时、cron 定时、间隔与未来一次性任务分发
- 通过 ClawHub 提供 OpenClaw 插件，暴露 agentos status/doctor 命令
-  Railway 模板自动配置双持久卷与私有浏览器 worker 服务

## 适用场景

- 集中管理多个 OpenClaw 代理的工作区、任务与模型访问
- 定时调度代理执行周期性工作并查看运行历史
- 对敏感操作保留人工审批与诊断能力

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8:  AgentOS is an open-source operating layer for building and running teams of digital workers.
> L11:  Powered by OpenClaw as the agent runtime.
> L263: AgentOS does not replace OpenClaw. OpenClaw is the kernel; AgentOS is the human operating layer above it.

## 星数曲线

```mermaid
xychart-beta
    title "SapienXai/AgentOS 星数(近 9 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-12", "2026-11-16", "2026-11-20", "2026-11-22", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 128 --> 142
    line [129, 133, 134, 136, 137, 138, 139, 140, 141]
```

2026-10-26 129 → 2026-11-28 141（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `37db81440e93` · [字段定义](../../DATASET.md)*
