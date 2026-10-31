# sprklai/zenii

⭐ 24 · JavaScript · MIT · 推送 2026-09-21 · [GitHub](https://github.com/sprklai/zenii) · [官网](https://zenii.sprklai.com) · 个人维护

**本地 AI 后端：一个守护进程让桌面/CLI/脚本共享 AI 记忆与工具**

Rust 实现的本地 AI 后端守护进程，运行于 localhost:18981，向桌面应用（Tauri）、CLI、TUI、脚本和 MCP 客户端提供统一的记忆、19 个工具、多 Provider 网关、TOML/YAML DAG 工作流与 cron 调度。支持 OpenAI/Anthropic/Gemini/OpenRouter/Ollama 等 6+ 提供方，可作为 MCP server 暴露工具给 Claude Code、Cursor 等，也可消费外部 MCP server。PAR 运行时可将 GitHub 上的 Python/Node 代码注册为工具。限制：单用户守护进程，无多租户；非 OpenAI 兼容服务器；移动端未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个守护进程向桌面/CLI/TUI/MCP 客户端统一提供记忆、工具与 Provider 网关
- 19 个工具注册一次即可在所有接口使用；MCP server 与 client 双向支持
- TOML/YAML DAG 工作流与 cron 调度，每次运行为完整 agent turn
- PAR 运行时按需安装依赖并隔离运行外部 Python/Node 代码作为工具

## 适用场景

- 让多个脚本、机器人和定时任务共享同一份本地 AI 记忆
- 开发工具通过单一 HTTP 或 MCP 后端接入多家模型提供方
- 在 VPS 或树莓派上自托管 AI 工作流与定时任务
- 需要桌面 UI 与可脚本化后端共用一套栈的项目

## 场景标签

`工作流自动化` `模型网关` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Run a daemon at <code>localhost:18981</code>. Your desktop app, CLI, TUI, scripts,
> L8:  and MCP clients share the same memory, tools, providers, channels, and scheduler — no sync, no duplication.

## 星数曲线

```mermaid
xychart-beta
    title "sprklai/zenii 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `551efefcfc0b` · [字段定义](../../DATASET.md)*
