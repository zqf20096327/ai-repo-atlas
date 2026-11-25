# sheng-tse/argonauts-code

⭐ 6 · Rust · Apache-2.0 · 推送 2026-11-01 · [GitHub](https://github.com/sheng-tse/argonauts-code) · 个人维护

**给开发者的多 coding agent 编排 CLI：并行协作互审**

终端应用，把用户已有的 coding agent CLI（Claude Code、Codex、agy、OpenCode）作为团队编排运行：主 agent 对话，其余 agent 在各自 git worktree 中并行规划与构建，并互相评审，合并需用户或预设规则批准。支持多种工作流（Captain/Orchestrator/Council 等），跨供应商评审、任务降级回退、实时流式视图与脚本/CI 模式。当前为 Alpha，仅支持 macOS 与 Linux，Windows 不支持；需 git 与至少一个已登录的 agent CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 Claude Code、Codex、agy、OpenCode 编排为一个团队协作
- 每个 agent 在独立 git worktree 中并行构建，合并前需检查与评审通过
- 评审默认来自与构建者不同的供应商，支持本地开源权重模型接入
- 提供安装器、Homebrew、npm、crates.io 及 deb/rpm 多种安装方式与自更新

## 适用场景

- 让多个不同模型的 coding agent 分工构建并互审代码改动
- 在脚本或 CI 中以预算限额运行 agent 团队完成任务
- 多个 agent 独立给出方案后协商一致再做开发决策

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L15: Argonauts Code is a terminal app that runs the coding agents you already use, Claude Code, Codex, agy and OpenCode,
> L105: - **The crew** is everyone else it can bring in. Workers build, reviewers read changes, and a judge settles questi

## 星数曲线

```mermaid
xychart-beta
    title "sheng-tse/argonauts-code 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-19", "2026-11-25"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-08 5 → 2026-11-25 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `175605c4656a` · [字段定义](../../DATASET.md)*
