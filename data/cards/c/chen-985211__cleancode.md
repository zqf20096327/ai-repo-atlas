# chen-985211/cleancode

⭐ 103 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/chen-985211/cleancode) · 个人维护 · 中文 README

**画布式 Agentic 开发环境：聚合多个 CLI Agent 协作开发与自动化**

面向人机协作的桌面端画布 ADE，将 Agent、终端与项目工作区置于同一画布：内置 33 种 CLI 编码 Agent（Codex、Claude Code 等）的启动配置并自动检测本机已安装工具；通过 CleanCode MCP 让 Agent 操作画布、构建工作流、创建其他 Agent；支持 Git worktree 分支工作区、基于 GitHub Issue 的开发、依赖驱动的自动化工作流与端口管理。以 macOS/Windows/Linux 安装包提供，也可用 Node.js+pnpm 从源码运行；当前为未签名 Preview 版。

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

- 支持 33 种 CLI 编码 Agent 并自动检测本机安装
- CleanCode MCP 原生工具让 Agent 操作画布、创建 Agent、分配任务
- Git worktree 分支工作区，每个分支有独立画布、终端与 Agent 会话
- 依赖驱动的自动化工作流与并行服务端口管理

## 适用场景

- 在同一画布上并行使用多个编码 Agent 完成开发任务
- 让 AI 学会并执行终端工具操作，构建可复用的自动化工作流
- 按 Git 分支并行开展多项修改，各分支绑定独立 Agent 会话

## 场景标签

`多智能体` `编码 Agent` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L31: **CleanCode is a canvas ADE (Agentic Development Environment) for human–AI collaboration.** It brings Agents, termi
> L44: - 🤝 **Native Agent Collaboration**: Use CleanCode MCP to let Agents operate the canvas, build workflows, create oth

## 星数曲线

```mermaid
xychart-beta
    title "chen-985211/cleancode 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-26", "2026-10-28"]
    y-axis "stars" 92 --> 95
    line [93, 94, 94]
```

2026-10-22 93 → 2026-10-28 94（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `47f32c58ec97` · [字段定义](../../DATASET.md)*
