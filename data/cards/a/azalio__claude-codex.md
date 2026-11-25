# azalio/claude-codex

⭐ 10 · Python · 推送 2026-11-19 · [GitHub](https://github.com/azalio/claude-codex) · 个人维护

**让 Claude Code CLI 通过 ChatGPT 订阅使用 Codex 后端的桥接工具**

一个本地桥接代理：启动本地 proxy，将 Anthropic Messages 与流式事件翻译为 Codex Responses 协议，使已安装的 claude 二进制以 ChatGPT 登录（而非 OpenAI API key）作为后端运行。保留 Claude Code 原有终端 UI、slash 命令、skills、hooks 与 MCP 工具；支持主模型与辅助请求分别路由（辅助请求可走 Ollama）。依赖 Claude Code、uv 与已在 Codex CLI/OpenCode 配置的 ChatGPT 登录；订阅限额生效，部分 Anthropic 专有能力不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 proxy 在 Anthropic Messages 与 Codex Responses 协议间转换
- 复用 Codex CLI 或 OpenCode 的 ChatGPT 登录，无需 OpenAI API key
- 主模型与辅助请求分开路由，辅助请求可经 Ollama

## 适用场景

- 用已有 ChatGPT 订阅驱动 Claude Code 命令行工作流
- 保留现有 skills/hooks/MCP 配置的同时切换后端模型
- 将辅助请求（如 auto-mode 检查）路由到本地 Ollama 模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: skills, hooks, MCP servers, and tools. `claude-codex` connects it to the Codex
> L54: Claude Code → local claude-codex bridge → ChatGPT Codex backend
> L57: The launcher starts a local proxy, translates Anthropic Messages and streaming


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `19a1e3d1c204` · [字段定义](../../DATASET.md)*
