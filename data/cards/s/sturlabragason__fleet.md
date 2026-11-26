# sturlabragason/fleet

⭐ 8 · Go · MIT · 推送 2026-11-25 · [GitHub](https://github.com/sturlabragason/fleet) · [官网](https://sturlabragason.github.io/fleet/) · 个人维护

**在单个 tmux 窗口中并排运行和监督多个 AI 编码代理**

fleet 是一个 Go 编写的终端工具，在单个 tmux 窗口中并排运行多个编码代理会话（Copilot CLI、Claude Code、agy、vibe、Pi），每个代理显示一个状态磁贴，每个代理在独立的 git worktree 和分支上工作。它提供内置的“admiral”代理，使用 MCP 工具读取其他代理的状态、查看屏幕、发送提示并生成或关闭它们。功能包括任务卡片、每个代理的开销追踪、会话采用、团队/邮件群组、无模型召回以及 26 种主题。需要 tmux 3.3+ 和代理 CLI；Linux 已测试，Windows 在没有 tmux 的情况下通过 ACP 运行。

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

- 使用 fleet_* MCP 工具的 admiral 代理可以读取状态、发送提示并生成/关闭代理
- 每个代理独立的 git worktree 和分支，配合 fleet touching/fleet merge
- 每秒刷新一次的状态磁贴，按需要你的代理优先排序
- 可选的 Claude Desktop 作为第二个 admiral 的集成

## 适用场景

- 在终端中同时运行多个编码代理，不丢失哪些代理正在等待你的追踪
- 允许 overseer 代理例行地报告并提示其他代理
- 将并行代理的工作隔离在不同的 worktree 中，直到合并

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L11: fleet runs your Copilot CLI, Claude Code, agy, vibe and Pi sessions side by side, shows each one as a status tile, 
> L29: fleet is for running many coding-agent sessions at once without visiting each one to see how it is doing. Everythin


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `a0d4667cd5c9` · [字段定义](../../DATASET.md)*
