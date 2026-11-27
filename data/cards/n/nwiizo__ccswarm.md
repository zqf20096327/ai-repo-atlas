# nwiizo/ccswarm

⭐ 157 · Rust · MIT · 推送 2026-11-07 · [GitHub](https://github.com/nwiizo/ccswarm) · [官网](https://crates.io/crates/ccswarm) · 个人维护

**为 Claude Code/Codex 编排可复现多阶段编码工作流的 CLI**

以 Rust 编写的 AI 编码代理工作流引擎：通过 YAML 定义 plan→Sangha 法定人数评审→实现→review→fix 等阶段的流程，由 Claude Code 与 Codex CLI 执行具体工作。支持任务队列、运行记录与成本核算、多 provider 配置与降级、headless/live 两种执行模式，本地 provider 运行需 Herdr 0.9.5+ 的后台标签页承载。Sangha 的异议解决与检查点恢复尚在设计阶段；auto-commit 带敏感路径拒绝列表，undo 仅提示不改写历史。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Sangha 法定人数评审：分离评估、证据性异议、记录决策（接受谓词当前仅计数批准）
- 内置 6 种流程（default/team/team-dynamic/quick/review-fix/research），支持自定义 YAML 流程
- 多 provider 支持：claude 全功能、codex exec、copilot 对代码生成快速失败；A2A 远程端点路由
- 运行记录、时间线对比、per-stage/per-agent 成本拆解与机器可读 JSON 输出

## 适用场景

- 给编码任务套上可复用的计划-评审-实现-审查流程
- 多代理并行开发前后端并由 supervisor 审查
- 无人值守自动提交 PR，需 HITL 审批高风险动作
- 回放历史运行并比较时间线与成本

## 场景标签

`多智能体` `编码 Agent` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L8: `ccswarm` is a workflow engine for AI coding agents, with **Sangha as its product
> L11: the work; ccswarm governs how the workflow advances.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `fd1447d17f66` · [字段定义](../../DATASET.md)*
