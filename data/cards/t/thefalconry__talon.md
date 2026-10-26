# thefalconry/talon

⭐ 74 · TypeScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/thefalconry/talon) · [官网](https://thefalconry.github.io) · 组织维护

**多平台 agentic AI 运行框架：Telegram/WhatsApp/Discord/Teams/终端/桌面运行可插拔后端 agent**

Talon 是自托管的 Node.js/TypeScript agentic AI harness，将一个 agent 引擎同时接入 Telegram、WhatsApp、Discord、Microsoft Teams、终端以及 Flutter 桌面/移动伴侣应用；后端可插拔（Claude Agent SDK、Kilo、OpenCode、Codex、Antigravity、OpenAI Agents），通过 MCP 提供工具访问。支持热加载插件、SKILL.md 技能、自编写触发器脚本，以及 Heartbeat/Dream 后台 agent 与多日 Goals 持久目标。安装需 git clone + npm install（Bun 1.3+ 或 Node 24+），也提供 Linux/macOS/Windows 独立二进制与 Homebrew。部分后端需各自 CLI 已安装并认证（如 claude、codex）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种前端 + 6 种可插拔后端，按配置切换或并行运行
- MCP 全量工具访问与热加载插件系统（npm/git/本地源）
- Heartbeat/Dream 后台 agent 与多日持久 Goals
- 独立二进制发布（Linux/macOS x64+arm64、Windows x64）附带 SHA256 校验与构建出处验证

## 适用场景

- 把同一个 agent 同时挂到 Telegram、WhatsApp、Discord 等多个聊天平台
- 自托管一个带后台定时任务和长期目标的私人 AI 助手
- 在桌面/手机伴侣应用中远程使用本地运行的 agent
- 切换不同后端（Claude SDK、Codex、Kilo 等）复用同一套前端与工具

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L13: Multi-platform agentic AI harness. Runs on **Telegram**, **WhatsApp**, **Discord**, **Microsoft Teams**, the **Term
> L20: |**Pluggable backend**|Claude Agent SDK, Kilo, OpenCode, Codex, Antigravity, OpenAI Agents — selectable per-process
> L95: **Dependency rule:** `core/` imports nothing from `frontend/` or `backend/`. Frontends and backends depend on core 

## 星数曲线

```mermaid
xychart-beta
    title "thefalconry/talon 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 73 --> 80
    line [79, 74, 74]
```

2026-10-18 79 → 2026-10-26 74（-5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3b56c8a11965` · [字段定义](../../DATASET.md)*
