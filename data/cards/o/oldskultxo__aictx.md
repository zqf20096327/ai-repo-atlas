# oldskultxo/aictx

⭐ 59 · Python · MIT · 推送 2026-06-17 · [GitHub](https://github.com/oldskultxo/aictx) · [官网](https://aictx.org) · 个人维护

**给 AI 编程 agent 的仓库级会话延续运行时，避免每次冷启动**

面向 Codex、Claude Code、GitHub Copilot 等编程 agent 的轻量仓库本地延续运行时：通过 resume/work/finalize 生命周期把当前任务、交接内容、决策、失败记录与验证证据写入 .aictx/ 目录，让后续会话从可检视的仓库状态恢复，而非依赖厂商聊天历史。兼容 agent 优先使用 MCP 工具、可回退 CLI；提供 continuity-view 报告与 doctor 诊断。声明不是 agent 框架、向量库或云端记忆服务。pip 安装，全程本地、无账号与守护进程。

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

- resume/finalize 生命周期将任务、决策、失败与验证证据写入仓库本地 .aictx/
- 支持 Codex/Claude Code/Copilot 及任意可读指令并调用 CLI 或 MCP 的通用 agent
- 生成可检视的 continuity 报告（markdown 与 mermaid 图）与 doctor 健康诊断
- 本地优先：无账号、守护进程、仪表盘或云同步

## 适用场景

- 让新会话的编程 agent 直接接着上一会话的任务与决策继续工作
- 跨不同厂商 agent 交接仓库上下文，避免上下文困在单一聊天历史
- 查看与审计 agent 留下的工作状态、失败记录与质量信号

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: AICTX is a lightweight repo-local continuity runtime for Codex, Claude Code, GitHub Copilot, and other coding agent
> L135: It is a lightweight continuity runtime that helps cooperating coding agents start from useful repository state.

## 星数曲线

```mermaid
xychart-beta
    title "oldskultxo/aictx 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 57 --> 60
    line [58, 59, 59]
```

2026-10-18 58 → 2026-10-26 59（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6479efbea4e7` · [字段定义](../../DATASET.md)*
