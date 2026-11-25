# db-lyon/ue-mcp

⭐ 517 · C++ · MIT · 推送 2026-11-23 · [GitHub](https://github.com/db-lyon/ue-mcp) · [官网](https://ue-mcp.com/) · 个人维护

**把 UE5 编辑器暴露为 MCP 工具，让 AI 客户端操作项目**

面向 Unreal Engine 5 的 Model Context Protocol 服务器，通过 3729+ 动作（含 Epic 原生 2191 个工具）让接入的 AI 客户端在打开的项目中执行关卡搭建、Blueprint、材质、Niagara、地形、构建等编辑器操作。提供两种用法：Windows 专用桌面客户端 Studio（内置 agent，按回合 checkpoint、操作需批准），或在已有 AI 客户端中经 `npx ue-mcp init` 向导接入。需 Node.js 20+，编辑器运行时才能执行更改类操作，带写保护、资产保护与回滚机制。MIT 许可，模型费用由用户自有账户承担。

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

- MCP 服务器暴露 3729+ 编辑器动作，覆盖 UE 5.4–5.9
- 可选 Studio 桌面客户端，内置 agent 与逐回合 checkpoint/审批
- 支持流程链式执行、失败回滚、多编辑器并行驱动与插件扩展
- 写保护与受控资产保护机制

## 适用场景

- 用自然语言让 AI 在 UE 项目里摆放关卡与材质
- 在 Claude Code/Cursor 等 AI 客户端中操作 Unreal 编辑器
- 让 AI 执行构建并汇报编译错误
- 把常用编辑器步骤封装成可回滚的可复用流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: UE-MCP is a free, open-source Model Context Protocol server for Unreal Engine 5. It connects AI assistants like Cla
> L55: Model Context Protocol is an open standard that lets AI assistants call external tools. UE-MCP is the tool server t
> L33: Already using Claude Code, Claude Desktop, Cursor or Codex? The server runs on Windows, macOS and Linux with UE 5.4

## 星数曲线

```mermaid
xychart-beta
    title "db-lyon/ue-mcp 星数(近 21 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-25"]
    y-axis "stars" 439 --> 524
    line [446, 448, 451, 455, 458, 460, 462, 448, 481, 490, 491, 495, 497, 500, 503, 505, 508, 512, 513, 514, 517]
```

2026-10-23 446 → 2026-11-25 517（+71）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `83a2bf31e31b` · [字段定义](../../DATASET.md)*
