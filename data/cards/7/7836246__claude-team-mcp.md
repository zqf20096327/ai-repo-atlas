# 7836246/claude-team-mcp

⭐ 49 · TypeScript · MIT · 推送 2026-04-14 · [GitHub](https://github.com/7836246/claude-team-mcp) · [官网](https://www.npmjs.com/package/claude-team) · 个人维护 · 中文 README

**多模型协作 MCP 服务器：让 IDE 编排 GPT/Claude/Gemini 组成 AI 开发团队**

Node.js/TypeScript 实现的 MCP Server，供 Claude Code、Windsurf、Cursor 等 IDE 接入：由 Tech Lead 角色分析任务并自动创建专家（frontend/backend/qa 及自定义），将任务分配给最多 10 个 worker 模型（openai/anthropic/gemini 提供方，默认 gpt-4o），支持模型分层（fast/balanced/powerful）。提供 5 个预置工作流（代码生成/修 bug/重构/评审/文档）、仪表盘与成本估算、协作历史、项目文件读取等工具。通过 npm 全局安装或 npx 直接使用，配置经环境变量完成，支持代理 API 自定义 Base URL。

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

- Tech Lead 分析任务并自动创建/分配专家，最多 10 个 worker 模型
- 5 个预置工作流：代码生成、修 bug、重构、评审、文档
- 仪表盘、成本估算、任务计划预览与使用统计
- 自定义专家（名称/系统提示/模型层级）经环境变量配置

## 适用场景

- 在 IDE 中用多个模型协作完成代码生成、修 bug 与重构
- 按任务复杂度分配不同层级的模型并估算成本
- 查看和检索历史协作记录

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Multi-Agent MCP Server for AI-Powered Development Teams**
> L48: |**Claude Code**|`~/.claude/config.json`|
> L149: |`CLAUDE_TEAM_MAIN_PROVIDER`|❌|Provider: `openai` / `anthropic` / `gemini`|

## 星数曲线

```mermaid
xychart-beta
    title "7836246/claude-team-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-30 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dfc9308dbb87` · [字段定义](../../DATASET.md)*
