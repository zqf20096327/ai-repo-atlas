# OasAIStudio/open-agent-sdk

⭐ 46 · TypeScript · MIT · 推送 2026-03-30 · [GitHub](https://github.com/OasAIStudio/open-agent-sdk) · [官网](https://openagentsdk.dev/) · 组织维护

**TypeScript 轻量 agent 运行时 SDK，开源替代 Claude Agent SDK**

面向 TypeScript 开发者的通用 agent 运行时 SDK，以 MIT 许可发布，定位为 Claude Agent SDK 的开源替代。提供会话（创建/恢复/fork）、工具执行循环（bash、文件、web search、MCP、任务委派）、生命周期 hooks、权限与每工具门控、多 provider 支持（Codex OAuth、OpenAI、Gemini、Anthropic），并内置 SWE-bench 与 Terminal-bench 评测 harness。通过 npx/bunx 脚手架初始化项目，monorepo 含 core SDK、文档站与示例。当前为 0.1.0-alpha 版本，API 在 1.0 前可能变动。

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

- 会话创建/恢复/fork 与存储化历史
- 工具循环：bash、文件操作、web search/fetch、MCP、任务委派
- 权限模式与 per-tool 门控、生命周期 hooks
- 仓库内含 SWE-bench 与 Terminal-bench 本地评测 harness

## 适用场景

- 构建带工具调用的长会话 agent 工作流
- 从 Claude Agent SDK 工作流迁移到开源运行时
- 对 agent 做 SWE-bench/Terminal-bench 基准评测

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: Use it when you want a lightweight open runtime with sessions, tools, hooks, subagents, and multi-provider support 
> L70: - `packages/core/`: published SDK package

## 星数曲线

```mermaid
xychart-beta
    title "OasAIStudio/open-agent-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-27 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4e5cc9927f9b` · [字段定义](../../DATASET.md)*
