# neoswarm/neosh

⭐ 30 · Rust · MIT · 推送 2026-10-17 · [GitHub](https://github.com/neoswarm/neosh) · [官网](https://neoswarm.dev) · 组织维护

**面向高级用户的终端 AI agent 编排工作区（TUI）**

Rust 编写的终端工作区，用于运行与控制多个编码 agent 会话：单一工作区进程、多终端可挂接/脱离而不中断任务；支持 claude-cli 登录、anthropic/openai 兼容/google 四种模型驱动；每个会话内置 git worktree 分支；提供 neosh agent 脚本接口供 shell/CI/其他编码 agent 驱动并行会话；TypeScript 插件体系，内置功能均构建于同一公开 API；支持多机配对远程控制。安装提供 curl 脚本、Homebrew、npm、cargo 及源码方式。

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

- 工作区进程 + 多终端挂接，会话在终端关闭后继续运行
- claude-cli / anthropic / openai 兼容 / google 四种模型驱动，无需 API key 即可起步
- 每个会话自动创建 git worktree 分支
- TypeScript 插件体系，内置功能均基于同一公开 API，可被替换

## 适用场景

- 在终端中同时运行并切换多个编码 agent 会话
- 用脚本或 CI 批量驱动 agent 会话并等待结果
- 为编码 agent（Claude Code/Codex 等）安装技能以驱动本工具
- 跨多台配对电脑远程操控 agent

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L22: Run coding agents the way you run Neovim. One workspace, any model, and a public API that every
> L64: `neosh agent` is the workspace without a screen — the same API a plugin uses, over the same socket
> L65: a terminal attaches to. A shell loop, a CI job or a coding agent can run ten conversations at once

## 星数曲线

```mermaid
xychart-beta
    title "neoswarm/neosh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6466d3378f92` · [字段定义](../../DATASET.md)*
