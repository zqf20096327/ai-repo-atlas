# azat-io/ai-config

⭐ 15 · TypeScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/azat-io/ai-config) · 个人维护

**统一管理 Claude Code 等多个 AI 编程助手配置的安装器**

面向 AI 编程助手的配置管理工具：通过单一 npx 安装器，将本仓库维护的指令、命令、技能、子代理、hooks 与 MCP 集成部署到 Claude Code、Codex、Gemini CLI、OpenCode 四种 agent 的各自目录结构中，支持项目级与全局（home）两种安装范围。内置 9 个命令、7 个技能、5 个代理及 Fetch、Sequential Thinking 两个 MCP 服务器。要求 Node.js v22+，GitHub 相关任务需 gh CLI 并先完成 gh auth login，内置 MCP 依赖需 uv。

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

- 单个 npx 安装器覆盖 4 种 AI 编程助手的配置同步
- 项目级与全局（home）两种安装范围可选
- 内置命令/技能/代理/hooks 及两个 MCP 服务器（Fetch、Sequential Thinking）
- 提供各 agent 的功能支持矩阵（指令、命令、技能、子代理、hooks、MCP）

## 适用场景

- 让多个 AI 编程助手共用同一套指令与技能配置
- 在团队项目中统一部署 AI 编程助手的配置
- 免去手工维护各 agent 不同目录结构的配置文件

## 场景标签

 · 领域:开发工具/AI 助手配置

## 证据(README 行号)

> L13: A unified configuration manager for AI coding assistants that keeps Claude Code,
> L16: Seamlessly deploy consistent instructions, commands, skills, and MCP

## 星数曲线

```mermaid
xychart-beta
    title "azat-io/ai-config 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6ef25878e928` · [字段定义](../../DATASET.md)*
