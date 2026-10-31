# tarcisiopgs/lisa

⭐ 14 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/tarcisiopgs/lisa) · 个人维护

**连接 issue 跟踪器与 AI 编码 agent 的自动开发编排工具**

Lisa 提供两种模式：Autonomous 将 issue 跟踪器接入 AI 编码 agent，把目标分解为 issue、逐个实现、推送并开 PR、监控 CI 与 review 后更新看板；Workspace 在终端 UI 中管理多项目 git worktree，交互式运行 agent，后台 daemon 保持任务运行。支持 7 种 issue 跟踪器与 10 种 AI agent（Claude Code、Gemini CLI、Codex 等），含 LLM 验收标准核验、模型降级链与并发多仓执行。以 npm 全局安装的 CLI 提供。

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

- 7 种 issue 跟踪器（Linear/GitHub/GitLab/Jira 等）+ 10 种 AI agent 接入
- 计划→实现→PR→CI/Review 监控的全流程自动化循环
- Spec Compliance：LLM 按 issue 验收清单核验 git diff 并输出结构化判定
- Workspace 模式：git worktree 管理 + 后台 daemon 保持 agent 运行

## 适用场景

- 把待办 issue 自动交给 AI agent 实现并开 PR
- 在终端里对多个仓库并行运行 AI 编码 agent
- 自动监控 PR 的 CI 失败与 reviewer 反馈并触发修复

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: - **Autonomous** connects your issue tracker to an AI coding agent and delivers pull requests on its own. Describe 
> L50: - **10 AI agents** — Claude Code, Gemini CLI, GitHub Copilot CLI, Cursor Agent, Aider, Goose, OpenCode, Codex, Kilo
> L73: |Provider|Key|Provider|Key|

## 星数曲线

```mermaid
xychart-beta
    title "tarcisiopgs/lisa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `62bd7527635a` · [字段定义](../../DATASET.md)*
