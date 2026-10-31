# yjhmelody/nanobot-rs

⭐ 16 · Rust · MIT · 推送 2026-07-08 · [GitHub](https://github.com/yjhmelody/nanobot-rs) · 个人维护 · 中文 README

**Rust 实现的本地极简 AI Agent 运行时，供学习研究**

用 Rust 编写的本地 Agent 运行时，定位为最小化的 openclaw 式实现，作者声明当前主要用于学习与研究，不建议直接用于生产。支持 CLI 单轮与交互式对话、Gateway 模式与渠道分发；原生接入 Anthropic Messages 与 OpenAI-compatible provider（responses 与 chat_completions），provider 含 anthropic、openai、custom 及自定义键；渠道含 CLI、Telegram、Feishu/Lark（Discord 暂未实现）。工具能力覆盖文件、Shell、Web、消息、子代理、Cron、MCP、ACP 等，并提供本地会话持久化、记忆、心跳与定时任务。通过 cargo 运行，环境需 Rust 1.95。

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

- 原生 Anthropic Messages 与 OpenAI-compatible provider（responses 与 chat_completions）
- CLI/Telegram/Feishu 渠道接入与 Gateway 调度模式
- 文件、Shell、Web、MCP、ACP、子代理、Cron 等工具能力
- 本地会话持久化、记忆、心跳与定时任务

## 适用场景

- 在本地快速搭建可扩展的 AI Agent
- 通过 Telegram/Feishu/CLI 进行多轮对话与工具调用
- 用统一配置切换 OpenAI-compatible 与 Anthropic-compatible 网关

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: `nanobot` 是一个 Rust 实现的本地 Agent 运行时，提供：
> L11: - Gateway 模式与渠道分发

## 星数曲线

```mermaid
xychart-beta
    title "yjhmelody/nanobot-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `edd13ff3eb51` · [字段定义](../../DATASET.md)*
