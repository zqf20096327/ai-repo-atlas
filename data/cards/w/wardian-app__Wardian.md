# wardian-app/Wardian

⭐ 10 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/wardian-app/Wardian) · [官网](https://wardian.org) · 组织维护

**本地桌面端多 CLI Agent 编排与可视化管理工作台**

基于 Tauri/Rust 的桌面应用，把用户已使用的 CLI agent（Antigravity、Claude Code、Codex、OpenCode、Pi）统一纳入持久化身份、PTY 实时终端、作用域技能、自动化运行与队列证据的本地管理界面。工作台支持多窗格布局，可将可用的提示词、角色类、技能沉淀为可复用工件；提供 wardian CLI 供脚本与 agent 以文本方式控制应用。面向需要在本地跨工作区运行与协调多个 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一编排六个 provider CLI，适配同一 agent 生命周期、遥测与自动化模型
- 每个 agent 拥有持久化身份、作用域技能与完成历史，而非一次性终端会话
- Rust 引擎运行本地自动化模板，保留运行状态与节点输出证据
- 内置 wardian CLI，供 agent 和脚本以文本方式发现身份、协调与控制

## 适用场景

- 在一个桌面应用里生成、监督和交接多个 CLI agent 的工作
- 把重复执行的指令沉淀为提示词、角色模板和自动化流程
- 用 Git worktree 为 agent 分配隔离分支并审查其产出

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L24: Use it to spawn specialized agents, monitor their progress, hand work between them, collect completed output, and a
> L95: Wardian supports six provider CLIs today and adapts each runtime into the same agent lifecycle, telemetry, skill, a


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `e734bc8f2c13` · [字段定义](../../DATASET.md)*
