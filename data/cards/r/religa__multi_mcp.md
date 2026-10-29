# religa/multi_mcp

⭐ 37 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/religa/multi_mcp) · 个人维护

**面向 Claude Code 的多模型编排 MCP 服务器，做代码审查与分析**

基于 Model Context Protocol 的 MCP 服务器，供 Claude Code CLI 与 OpenCode 连接使用，编排多个 AI 模型（OpenAI GPT、Anthropic Claude、Google Gemini、OpenRouter）执行代码审查、OWASP Top 10 安全检查、多模型对比与多智能体辩论（debate）共识流程。支持 API 模型与 CLI 模型（Gemini CLI、Codex CLI、Claude CLI）混合使用，通过 Python asyncio 并行执行，并可用 YAML 配置自定义模型与短别名。需 Python 3.11+ 与至少一个提供商 API key；附带实验性独立 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 并行编排多模型执行代码审查与安全分析（OWASP Top 10）
- chat/compare/debate 多智能体共识工作流与会话线程保持上下文
- API 模型与 CLI 模型（Gemini CLI/Codex CLI/Claude CLI）可混合使用
- YAML 配置自定义模型与短别名（mini/sonnet/gemini 等），支持用户覆盖

## 适用场景

- 在 Claude Code 开发流程中用多个模型并行做代码审查
- 让多个模型就架构决策独立回答并互相批评以形成共识
- 用短别名快速切换不同提供商的模型进行分析

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L10: A **multi-model AI orchestration MCP server** for **automated code review** and **LLM-powered analysis**. Multi-MCP
> L27: Multi-MCP acts as an **MCP server** that Claude Code or OpenCode connects to, providing AI-powered code analysis to

## 星数曲线

```mermaid
xychart-beta
    title "religa/multi_mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-29 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6d50dbd8894d` · [字段定义](../../DATASET.md)*
