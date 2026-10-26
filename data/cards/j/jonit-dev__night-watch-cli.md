# jonit-dev/night-watch-cli

⭐ 49 · TypeScript · MIT · 推送 2026-06-24 · [GitHub](https://github.com/jonit-dev/night-watch-cli) · [官网](https://www.npmjs.com/package/@jonit-dev/night-watch-cli) · 组织维护

**夜间异步执行 PRD/看板任务并自动开 PR 的 CLI 工具**

面向 AI-native 独立开发者与小型团队的异步工程执行层：将 PRD 或 GitHub issue 队列交给 Claude CLI 或 Codex，在隔离的 git worktree 中运行，产出 pull request、review 修复、QA 输出与审计结果。提供看板视图、执行时间线、cron 调度、JSON 优先的 agent 可读命令，以及通过 providerEnv 指向 Anthropic 兼容自定义端点（如 GLM-5）的能力。默认 provider 为 claude，可切换 codex；内置匿名遥测，可用命令或环境变量关闭。以 npm 全局安装为主，也支持 npx 与源码构建。

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

- 在隔离 git worktree 中运行 Claude CLI / Codex 并自动开 PR
- GitHub issue 看板队列：Draft → Ready → In Progress → Review → Done
- providerEnv 支持自定义 Anthropic 兼容端点（含 GLM-5）
- JSON 优先的 agent 可读 CLI（status/health/config --json）

## 适用场景

- 白天定义 PRD/看板任务，夜里自动产出待审 PR
- 维护、review 修复、QA 与积压任务的非同步批量执行
- 通过 cron 调度定时运行 agent 任务并跨项目查看时间线

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Night Watch is an async execution layer for well-scoped engineering work. It takes PRDs or queued board items, runs
> L87: |`claude`|`claude`|`--dangerously-skip-permissions`|`-p "/command-name"`|

## 星数曲线

```mermaid
xychart-beta
    title "jonit-dev/night-watch-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-26 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ecb9f9d8291b` · [字段定义](../../DATASET.md)*
