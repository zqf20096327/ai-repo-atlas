# lespaceman/athena-flow-cli

⭐ 23 · TypeScript · MIT · 推送 2026-06-06 · [GitHub](https://github.com/lespaceman/athena-flow-cli) · [官网](htttps://athenaflow.in) · 个人维护

**面向 Claude Code 与 Codex 的 agent 工作流运行时 CLI**

为 AI 编码 agent 提供确定性编排层的 CLI 工具：在用户与底层 harness（Claude Code、OpenAI Codex）之间加入声明式、可版本化的工作流层，封装提示模板、多会话循环、插件与隔离策略。功能包括实时终端观测流、SQLite 会话持久化与恢复、工作流市场（安装/搜索/升级社区工作流）、以及面向 CI 的无头执行模式 drisp exec（JSONL 输出、结构化退出码、权限钩子默认失败）。要求 Node.js 20+ 且 PATH 上有至少一个 harness。

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

- 声明式可分享的工作流单元与社区市场
- SQLite 会话持久化，支持中断后恢复
- drisp exec 无头模式：JSONL 事件、结构化退出码、安全默认权限策略
- harness 无关：同一工作流/会话模型跨 Claude Code 与 Codex

## 适用场景

- 让团队的 agent 提示词与执行流程可复用、可版本化
- 在 CI 流水线中无头运行 agent 任务（PR 风险摘要、发布说明生成）
- 实时观测 agent 的每次工具调用与权限决策

## 场景标签

`工作流自动化` `提示工程` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: Athenaflow is a **workflow runtime** for Claude Code and OpenAI Codex. It adds structured workflows, real-time obse
> L47: **Harness-agnostic** -- same workflows, same UI, same session model across Claude Code and Codex.

## 星数曲线

```mermaid
xychart-beta
    title "lespaceman/athena-flow-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e4dd675cc78e` · [字段定义](../../DATASET.md)*
