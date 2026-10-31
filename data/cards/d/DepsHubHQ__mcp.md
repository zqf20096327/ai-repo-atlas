# DepsHubHQ/mcp

⭐ 14 · Go · 推送 2025-11-13 · [GitHub](https://github.com/DepsHubHQ/mcp) · [官网](https://discord.gg/NuEXZwNDtN) · 组织维护

**MCP 服务器：为编辑器提供依赖更新与破坏性变更信息**

DepsHub 提供的 MCP Server，将依赖更新分析能力接入支持 MCP 协议的编辑器（VS Code、Cursor、Windsurf、Zed 等）：查找并修复破坏性变更、识别依赖升级路径、从 release notes 与 changelogs 提供上下文。开箱支持 200 万+ 包，覆盖 npm/yarn/pnpm、Go、Ruby gems、cargo 生态。提供远程实例（https://mcp.depshub.com/mcp）与本地 Docker 容器（ghcr.io/depshubhq/mcp）两种接入模式；因 Windsurf 不支持 streamable HTTP，需本地 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 查找并修复依赖破坏性变更，识别升级路径
- 从 release notes 与 changelogs 向编辑器提供上下文
- 开箱支持 200 万+ 包，覆盖 npm/Go/Ruby/cargo 生态
- 提供远程实例与预构建 Docker 容器两种运行模式

## 适用场景

- 在编辑器中通过 AI 助手分析依赖升级路径
- 快速定位依赖升级引入的破坏性变更
- 在 Windsurf/Zed 等编辑器中接入依赖更新能力

## 场景标签

 · 领域:开发工具/依赖管理

## 证据(README 行号)

> L1: DepsHub MCP Server for Effortless Dependency Updates
> L13: You can use DepsHub MCP in two modes:
> L52: Any editor that supports MCP protocol should be able to work with DepsHub.

## 星数曲线

```mermaid
xychart-beta
    title "DepsHubHQ/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `edab4c46d417` · [字段定义](../../DATASET.md)*
