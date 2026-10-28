# yranjan06/WEBGhosting-MCP

⭐ 33 · Go · MIT · 推送 2026-04-08 · [GitHub](https://github.com/yranjan06/WEBGhosting-MCP) · 个人维护

**给 AI agent 的隐身浏览器 MCP 服务器，含 34 个工具**

用 Go 实现的 MCP 服务器，封装 Playwright 提供浏览器自动化：34 个工具覆盖导航、点击输入、数据抽取、截图、多标签页、记忆与任务编排，内置 22 个反指纹脚本用于绕过站点机器人检测。LLM 用于复杂抽取与提示重构，通过环境变量接入任意 OpenAI 兼容提供商（默认 gpt-4o，支持 Groq、Ollama、NVIDIA NIM 等）。附带 Sarvam 语音助手包装脚本，可用语音下达浏览指令。使用方式为加入 IDE 的 MCP 配置，供 Cursor、Copilot、Claude Code 等调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 34 个 MCP 工具：导航/交互/抽取/截图/多标签页/记忆/编排
- 22 个反指纹脚本构成的隐身引擎
- 三层执行模型：regex 处理简单任务，LLM 仅用于复杂任务
- 任意 OpenAI 兼容 LLM 均可接入，含语音控制包装

## 适用场景

- 让 Cursor/Claude Code 等 agent 通过 MCP 操控真实浏览器
- 需要绕过机器人检测的网页数据抽取
- 用语音命令驱动浏览器并抽取结构化结果

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L13: The way I layered the architecture was very intentional, especially with the Go-based MCP server wrapping Playwrigh
> L32: Every capability is exposed as a standard MCP tool. Any compatible AI agent can call these directly.
> L45: **As an MCP server for AI agents:** add it to your IDE's MCP config and any agent (Cursor, Copilot, Claude Code) ca

## 星数曲线

```mermaid
xychart-beta
    title "yranjan06/WEBGhosting-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dcf6094b2e9c` · [字段定义](../../DATASET.md)*
