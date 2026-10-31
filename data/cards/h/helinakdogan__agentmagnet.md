# helinakdogan/agentmagnet

⭐ 14 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/helinakdogan/agentmagnet) · [官网](https://www.agentmagnet.app) · 个人维护

**跨 Claude/Cursor/Codex 共享项目记忆的本地 MCP 记忆层**

面向使用多个 AI 编码助手的开发者：在工作过程中自动学习项目的决策、约定、失败尝试与偏好，形成一份共享记忆，供 Claude、Cursor、Codex 等客户端读取，避免每次会话重复解释项目背景。通过 pip 安装，agent-magnet init 命令可自动检测并配置 Claude Code、Claude Desktop 和 Cursor；其他 MCP 客户端可手动配置。默认本地运行，无需 Redis 或 API key。团队共享记忆功能需从 agentmagnet.app 购买付费 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动学习无需手动 remember，支持遗忘与标记完成
- 一份记忆跨 Claude、Cursor、Codex 共享
- agent-magnet init 自动检测配置 Claude Code/Claude Desktop/Cursor
- 默认本地运行，无需 Redis 与 key；支持任意 MCP 客户端手动配置

## 适用场景

- 在多个 AI 编码助手间保持同一份项目记忆
- 免去每次新会话重新解释项目背景
- 团队成员共享决策与约定作为上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: - Shares one memory across Claude, Cursor, and Codex
> L32: Claude, Cursor, Codex — same memory, local by default. `agent-magnet init` detects and configures Claude Code, Clau
> L38:   "mcpServers": {

## 星数曲线

```mermaid
xychart-beta
    title "helinakdogan/agentmagnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5b1d35ed0e4e` · [字段定义](../../DATASET.md)*
