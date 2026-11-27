# Electron-libre/cardinal

⭐ 5 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Electron-libre/cardinal) · [官网](https://github.com/Electron-libre/cardinal/blob/main/docs/tutorial.md) · 个人维护

**为多项目同步 Claude Code agent 技能、钩子与门禁的脚手架工具**

Cardinal 将一套 Claude Code 技能（issue 工作流、规范编写、发布等）、钩子、审查门禁、可选 just 配方与 CI 打包为可管理的源文件，由 cardinal 二进制通过 init/sync/update/check 命令复制进各个 git 项目并在副本漂移时报错。附带 cardinal-ui 终端面板展示 issue 队列、worktree 与会话状态，并提供 session-metrics 等评测命令读取 Claude Code 会话记录衡量 agent 表现。使用者是通过 agent 处理 issue 的开发项目；安装仅需下载预编译二进制，无需克隆仓库。

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

- init/sync/update/check 命令将托管文件同步到项目并检测副本漂移
- 门禁机制：无 diff 审查不可提交、lint 警告不结束回合、Conventional Commits 校验
- cardinal-ui 终端面板展示 issue 队列、worktree 会话状态与度量趋势
- session-metrics/rule-breaches 等评测命令基于一年期会话记录

## 适用场景

- 在多个仓库统一部署同一套 Claude Code 技能与规则
- 让 agent 安全地在项目里完成 issue 并强制代码审查门禁
- 监控并行 worktree 中多个 agent 会话的进度与发布状态

## 场景标签

`代码审查` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L5: Cardinal is one agent harness for many projects. This repository holds the Claude Code skills, hooks, checks, option
> L6: recipes and CI that a project needs to have an agent work its issues safely, plus `cardinal`, the tool that copies t


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f173b9b2e158` · [字段定义](../../DATASET.md)*
