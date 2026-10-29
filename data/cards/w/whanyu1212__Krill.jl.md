# whanyu1212/Krill.jl

⭐ 29 · Julia · MIT · 推送 2026-03-30 · [GitHub](https://github.com/whanyu1212/Krill.jl) · [官网](https://whanyu1212.github.io/Krill.jl/) · 个人维护

**Julia 编写的 AI agent 运行时，把 LLM 接入 Telegram/Discord**

用纯 Julia 实现的轻量 agent 运行时，受 nanobot 与 OpenClaw 启发：通过单个 krill.toml 配置把 LLM（目前仅 OpenAI 与 Gemini）连接到 Telegram/Discord，提供本地工具（文件、shell、GitHub CLI、Google Workspace）、持久记忆、Cron 调度、子代理、MCP 工具服务器接入，并可委托 Claude Code 或 Codex CLI 做编码任务。支持从 ClawHub 公共注册表（3,200+ 技能）安装技能，并带隔离校验管线与提示级二次限制。项目自述为 WIP，API 可能变化；Anthropic、Ollama 与本地模型为规划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单文件 krill.toml 配置驱动的 agent 运行时（Telegram/Discord 双通道）
- MCP 工具服务器接入（stdio/HTTP，Julia 自定义实现）
- ClawHub 技能注册表接入，带 quarantine→validation→verified 管线与提示级安全限制
- 可委托 Claude Code / Codex CLI 作为编码子代理

## 适用场景

- 把 LLM 接到 Telegram 或 Discord 聊天里做带工具的助手
- 搭建带定时任务、记忆与子代理的个人 agent
- 在 Julia 技术栈内运行与 OpenClaw 类似的 agent 工作流

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A Julia-native, channel-agnostic AI agent runtime
> L24: Connect an LLM to Telegram or Discord with tools, memory, scheduling, and coding agents — all from a single `krill.
> L42: |🔌|**MCP**|Connect external tool servers via stdio or HTTP|

## 星数曲线

```mermaid
xychart-beta
    title "whanyu1212/Krill.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `89efcd6bdadc` · [字段定义](../../DATASET.md)*
