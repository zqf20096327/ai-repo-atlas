# microsoft/Agent365-devTools

⭐ 61 · C# · MIT · 推送 2026-10-21 · [GitHub](https://github.com/microsoft/Agent365-devTools) · 组织维护

**微软 Agent 365 应用的开发/部署/管理命令行工具**

微软官方提供的 .NET 命令行工具，面向 Microsoft Agent 365 应用开发者：提供 develop/develop-mcp 命令管理 MCP 工具服务器与 Dataverse 环境中的 MCP 服务器，setup 命令创建 Azure 资源、配置权限并注册 agent blueprint，publish 命令打包 manifest 供上传至 Microsoft 365 管理中心并通过 Teams 完成接入。另含日志导出、Entra ID 权限查询与资源清理。前置要求 .NET 8.0+ 与 Entra ID 应用注册（delegated 权限）。项目处于活跃开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- develop/develop-mcp 管理 MCP 工具服务器与 Dataverse 环境 MCP 服务器
- setup 创建 Azure 资源并注册 agent blueprint
- publish 打包 manifest 上传 Microsoft 365 Admin Center
- 导出脱敏诊断日志、查询 Entra ID agent 权限信息

## 适用场景

- 开发与调试 Agent 365 应用的 MCP 工具服务器
- 一键配置 Azure 资源并注册 agent blueprint
- 打包发布 agent 到 Microsoft 365 并通过 Teams 接入

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: The **Microsoft Agent 365 DevTools CLI** is a command-line interface tool designed to streamline the development, d
> L19: - **develop**: Manage MCP tool servers for agent development
> L21: - **setup**: Set up your Agent 365 environment by creating Azure resources, configuring permissions, and registerin

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Agent365-devTools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ba3031cadb1d` · [字段定义](../../DATASET.md)*
