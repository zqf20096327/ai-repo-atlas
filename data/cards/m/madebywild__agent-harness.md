# madebywild/agent-harness

⭐ 16 · TypeScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/madebywild/agent-harness) · [官网](https://www.npmjs.com/package/@madebywild/agent-harness-framework) · 组织维护

**统一管理多家 AI agent CLI 配置的 TypeScript CLI 工具**

Agent Harness 是一个 TypeScript CLI 工具与库，将 AI agent 配置（可组合 prompt 片段、技能、MCP server 配置、子 agent 与钩子）收敛到 `.harness/` 单一来源，运行 `npx harness apply` 后生成 OpenAI Codex、Anthropic Claude Code、GitHub Copilot 与 Cursor 各自的原生配置文件。采用 shadcn/ui 模式：可从共享 git registry 以完整源码形式拉取实体，可检查、修改与版本化。支持 monorepo 按包放置产物、watch 模式、schema 版本管理与旧配置一键导入（U-Haul）。限制：旧版单 prompt 实体无自动迁移。

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

- 单一来源同时生成 Codex/Claude/Copilot/Cursor 四家原生配置
- git registry 共享实体，以完整源码形式拉取并可修改提交
- U-Haul 一步导入既有 CLAUDE.md/AGENTS.md/.mcp.json 等旧配置
- monorepo 下按实体 target 将产物放置到对应包目录

## 适用场景

- 团队在多个 agent CLI 间保持技能、prompt 与 MCP 配置同步
- 把团队沉淀的 prompt 与技能通过共享 git registry 分发到各项目
- 把已有的各家 provider 配置文件迁移为单一来源管理

## 场景标签

 · 领域:开发工具/AI agent 配置管理

## 证据(README 行号)

> L12: Agent Harness is a TypeScript CLI tool and library that manages AI agent configurations (composable prompt sections
> L36: - Multi-provider support with simultaneous output generation for Codex, Claude, Copilot, and Cursor

## 星数曲线

```mermaid
xychart-beta
    title "madebywild/agent-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5d14d13d3f99` · [字段定义](../../DATASET.md)*
