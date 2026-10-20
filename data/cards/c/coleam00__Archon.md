# coleam00/Archon

⭐ 23,709 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/coleam00/Archon) · [官网](https://archon.diy) · 个人维护

**为 AI 编码 agent 提供可复现 YAML 工作流引擎的开发者工具**

Archon 是面向 AI 编码 agent 的工作流引擎：开发者把计划、实现、验证、代码评审、PR 创建等开发流程定义为 YAML 工作流，由引擎确定性执行，AI 仅在各步骤填充智能内容。支持确定性节点（bash 脚本、测试、git 操作）与 AI 节点组合，可在独立 git worktree 中运行，并提供 CLI、Web UI 及 Telegram/Slack/Discord/GitHub 等平台接入。安装依赖 Bun、Claude Code 与 GitHub CLI；提供 curl 安装脚本、Homebrew 与源码安装途径，附带 sdlc 工作流包与匿名遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 26,76 位贡献者
- 涨星:近 1 天 **+9**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX / WEB · 协议:MCP

## 能力要点

- 以 YAML 定义开发流程工作流，含阶段、验证门与产物
- 确定性节点与 AI 节点可混合编排
- 支持 CLI、Web UI、Slack、Telegram、Discord、GitHub 触发运行
- 内置 sdlc 工作流包（archon-ship/triage/investigate/review 等 10 个）

## 适用场景

- 让 AI agent 按固定流程修复 issue 并交付已评审的 PR
- 把团队的代码评审/验证门标准化为可提交的工作流
- 通过 Slack/Telegram 远程触发开发工作流

## 场景标签

`工作流自动化` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L13: Archon is a workflow engine for AI coding agents. Define your development processes as YAML workflows - planning, i
> L26: - **Composable** - Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation,
> L129: Release binaries ship without AI providers. The quick installers ask which of

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `0237e46383b6` · [字段定义](../../DATASET.md)*
