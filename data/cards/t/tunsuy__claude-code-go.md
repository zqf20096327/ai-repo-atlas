# tunsuy/claude-code-go

⭐ 38 · Go · MIT · 推送 2026-09-23 · [GitHub](https://github.com/tunsuy/claude-code-go) · 个人维护 · 中文 README

**Go 重写的 Claude Code：终端 AI 编程助手**

用 Go 逐模块重写 Anthropic 官方 TypeScript CLI Claude Code，覆盖 TUI、34 个工具、9 层权限管道、多 agent 协调、MCP 协议、会话管理、插件管理与 OAuth/API key 认证；`mcp`/`plugin` 子命令输出与原版逐字节一致。支持多 provider：Anthropic 直连、OpenAI 兼容 API（DeepSeek/Ollama/Azure 等）、AWS Bedrock、Vertex AI。README 声明全部生产代码由 AI agents 协作完成；当前处于 gap-ledger 驱动的维护模式，v0.8.0 含 27 个用户可见 stub。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 34 个内置工具经 9 层权限管道执行
- MCP 支持（stdio+HTTP），可从 Claude Desktop 导入配置
- 多 provider：Anthropic/OpenAI 兼容/Bedrock/Vertex
- 会话恢复、上下文自动压缩、插件市场管理

## 适用场景

- 在终端里通过对话读写代码、运行工具、重构与 review
- 用本地 Ollama 或 DeepSeek 等第三方 API 驱动同一套 CLI
- 通过 MCP 接入外部工具与子 agent 并行任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  🤖 A Go reimplementation of Claude Code — AI coding assistant in your terminal
> L33: This project is a **complete Go reimplementation of Claude Code** — Anthropic's official TypeScript CLI — rewritten

## 星数曲线

```mermaid
xychart-beta
    title "tunsuy/claude-code-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `44e4f9acd7c0` · [字段定义](../../DATASET.md)*
