# MikeGT4/agent-tree

⭐ 24 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/MikeGT4/agent-tree) · [官网](https://www.digitalroots.de/en/leistungen/software/agent-tree/) · 个人维护

**Claude Code 终端侧栏：以实时树视图管理各终端中的 agents**

为 Claude Code 提供的终端侧边面板插件，将一个会话的 agents 显示为实时树结构。可停止或纠正运行中的 sub-agents、为其和主会话切换模型与 effort、开关 advisor、查看用量限额。标签页覆盖完整报告、文件、日志、成本与终端。可选功能：把简单任务交给本地模型（Ollama、LM Studio）以节省 token。通过 claude plugin install 安装，需 Claude Code 2.1.292+，每日检查一次插件更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨会话实时树状展示 agents，可停止/纠正 sub-agents
- 报告、文件、日志、成本、终端多标签页视图
- 可将简单任务转交本地模型（Ollama、LM Studio）以节省 token
- 按 agent 统计 token 与成本，支持查看限额

## 适用场景

- 同时运行多个 Claude Code 终端时统一监控各 agents 状态
- 按 agent 查看 token 消耗与成本
- 把简单任务交给本地模型以节省 Claude 额度

## 场景标签

`编码 Agent` `多智能体` `LLM 可观测性` `推理引擎` · 领域:Agent 开发

## 证据(README 行号)

> L5: A side pane for Claude Code that shows a session's agents as a live tree.
> L11: Optional: Claude Code hands simple tasks to your local model (Ollama, LM Studio) and saves tokens.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `58d12c7c58ab` · [字段定义](../../DATASET.md)*
