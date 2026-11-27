# db-lyon/ue-mcp

⭐ 520 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/db-lyon/ue-mcp) · [官网](https://ue-mcp.com/) · 个人维护

**把 Unreal 编辑器暴露为 MCP 工具的 AI 代理服务器**

UE-MCP 是面向 Unreal Engine 5 的开源 Model Context Protocol 服务器，通过 3759+ 动作（含 Epic 全部 2191 个原生工具）让 Claude、Cursor、Codex 等 AI 客户端操作编辑器，覆盖关卡、Blueprint、材质、Niagara、地形、构建等。提供两种方式：Windows 专属的 Studio 桌面聊天客户端（带逐轮检查点与操作审批），或用 npx 向导将桥接插件接入已有 AI 客户端。支持 UE 5.4–5.9，需 Node.js 20+，提供写入守卫、流程回滚与受保护资产等安全机制。

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

- 3759+ MCP 动作，封装 Epic 全部 2191 个原生编辑器工具并可组合为可回滚的流程
- Studio 桌面客户端内置 Agent，逐轮检查点、Shell 命令与文件编辑需人工批准
- 写入守卫可阻止或确认改动，源码管理的资产可受保护，失败自动回滚
- npx ue-mcp init 向导安装桥接插件并配置 AI 客户端，doctor 命令诊断连接

## 适用场景

- 用自然语言在打开的 UE 项目中搭建关卡、材质与 VFX
- 让 AI 代理在编辑器内执行构建并汇报编译错误
- 在 Claude Code / Cursor 等现有客户端中接入 Unreal 编辑器操作

## 场景标签

 · 领域:游戏开发/AI 工具链

## 证据(README 行号)

> L13: UE-MCP is a free, open-source Model Context Protocol server for Unreal Engine 5. It connects AI assistants like Cla
> L55: Model Context Protocol is an open standard that lets AI assistants call external tools. UE-MCP is the tool server t

## 星数曲线

```mermaid
xychart-beta
    title "db-lyon/ue-mcp 星数(近 22 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 441 --> 527
    line [448, 451, 455, 458, 460, 462, 448, 481, 490, 491, 495, 497, 500, 503, 505, 508, 512, 513, 514, 517, 520, 520]
```

2026-10-25 448 → 2026-11-27 520（+72）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `48276a1739f8` · [字段定义](../../DATASET.md)*
