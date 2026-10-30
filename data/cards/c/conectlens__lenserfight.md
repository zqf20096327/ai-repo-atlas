# conectlens/lenserfight

⭐ 18 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/conectlens/lenserfight) · [官网](https://moon.lenserfight.com) · 组织维护

**开源提示词与 AI 工作流自动化平台：提示词版本化与编排**

将 AI 指令转化为可复用资产的平台：提示词以版本化、参数化的 Lens 形式管理，通过 Tags 检索、Threads 讨论迭代，用 Lensers 与 XP 记录贡献；支持把 Lens 与工具链接成 Workflow（开发中）、配置为可调度并可接 MCP 的 Agent（未完成）、以 Battle 进行评测（实验性，目标 2026 年 10 月）。提供 Web 应用（本地 Supabase + Vite，需 Node 22 与 Docker）、lf 命令行 CLI 及面向 Claude/Cursor/Codex 的 MCP 服务器（55 个工具）。自述为 beta 阶段，Lens/Thread/Tag/Lenser/XP 五项为稳定功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Lens 版本化参数化提示词管理，Tags 检索与 Threads 讨论迭代
- lf CLI 覆盖全部 Lens/Workflow/Agent/Lenser 操作，可离线对接本地 Ollama
- 托管 MCP 服务器暴露 55 个类型化工具，可接入 Claude/Cursor/Codex
- 本地运行基于 Supabase 栈（Postgres/Auth/Storage/Realtime），源码 MIT

## 适用场景

- 把反复调试的提示词沉淀为带版本和参数的 Lens 库
- 把重复 AI 任务编排成 Workflow 或按需/定时运行的 Agent
- 从 Claude/Cursor/Codex 助手内直接创建和运行 Lens 与 Workflow

## 场景标签

`提示工程` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L32: LenserFight is an open-source **prompt management and AI workflow automation platform** for
> L43:  automation-platform building (n8n, Zapier-style pipelines), purpose-built for AI instructions
> L45: - **Configure** a Workflow and a set of Lenses into an **Agent** you can run on demand or on a

## 星数曲线

```mermaid
xychart-beta
    title "conectlens/lenserfight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `200655bedc33` · [字段定义](../../DATASET.md)*
