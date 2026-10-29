# OthmanAdi/loophole

⭐ 22 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/OthmanAdi/loophole) · [官网](https://othmanadi.github.io/loophole/) · 个人维护

**让 LLM/MCP 客户端控制 Ableton Live 的 MCP 服务器扩展套件**

构建在 Ableton 官方 Extensions SDK 上的 MCP 服务器与扩展套件：Loophole Bridge 在 Live 内部 Extension Host 启动并绑定 loopback HTTP 服务，供 Claude、Cursor 等 MCP 客户端通过 12 个确定性工具读取和编辑 Live Set；Loophole Kit 提供 5 个制作人工作流扩展（Session-to-Song、增益、清理、音阶、人性化）。SDK 为 v1.0.0-beta，无自动化/CC/路由 API，尚未发布 npm 包或 .ablx，需从源码构建，面向 TypeScript/Node 开发者与 Live 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 首个基于 Ableton 官方 Extensions SDK 的 MCP 服务器，单个 .ablx 安装
- 12 个确定性工具：Zod 校验输入、排队变更、结构化结果
- 5 个制作人扩展：Session-to-Song Builder、Gain Stage Doctor 等
- SDK-free 核心可在无 Live 环境下测试

## 适用场景

- 用 Claude 等 MCP 客户端直接编辑 Live Set
- 制作人通过右键菜单执行编曲、增益、清理等工作室杂务
- 开发者基于 SDK-free 核心扩展自己的 Ableton 工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L16: - **The Loophole Bridge:** an MCP server that lets an LLM (Claude, Cursor, any MCP client) read and edit your Live 
> L36: |**Bridge**|`packages/mcp` · `@othmanadi/ableton-mcp`|The SDK-free MCP library: `buildServer`, 12 deterministic too

## 星数曲线

```mermaid
xychart-beta
    title "OthmanAdi/loophole 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0e6ebe803cd8` · [字段定义](../../DATASET.md)*
