# Jordiag/azure-devops-mcp-server

⭐ 14 · C# · MIT · 推送 2026-07-15 · [GitHub](https://github.com/Jordiag/azure-devops-mcp-server) · 个人维护

**将 Azure DevOps 操作通过 MCP 暴露给 AI 代理的 .NET 服务器**

一组 .NET 10 客户端库封装 Azure DevOps SDK/REST API，覆盖 Boards、Repos、Pipelines、Artifacts、Test Plans、Wiki、项目设置与搜索等功能域；顶层 MCP 服务器以控制台应用承载 ASP.NET Core，在 /mcp 端点经 SSE over HTTP 提供工具。AI 助手可运行时发现并以结构化函数调用调用工具。支持本地 dotnet 运行或 Docker 容器部署，配置经 appsettings.json 与 MCP_/AZURE_DEVOPS_ 环境变量读取。当前处于 pre-release 公开预览阶段，API 可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 Boards/Repos/Pipelines/Artifacts/Test Plans/Wiki/项目设置/搜索的 MCP 工具集
- 以 ASP.NET Core 承载，/mcp 端点经 SSE over HTTP 提供服务，含 /health 健康检查
- 提供 Docker 与本地 dotnet 两种部署方式
- 端到端测试验证 Semantic Kernel 代理可自动调用发布的工具

## 适用场景

- 让 AI 编程代理直接创建工作项、管理 PR、触发构建
- 通过对话式 agent 查询与操作 Azure DevOps Wiki 和测试计划
- 在容器中以统一 MCP 端点接入 Azure DevOps 自动化

## 场景标签

 · 领域:开发运维工具/AI 代理基础设施

## 证据(README 行号)

> L5: This repository contains a set of .NET libraries and a Model Context Protocol (MCP) server that expose Azure DevOps 
> L61: The `Dotnet.AzureDevOps.Mcp.Server` project brings these libraries together and exposes them as MCP tools. The serv
> L65: Integration tests exercise each client against a real Azure DevOps organization. Another test suite validates end‑t

## 星数曲线

```mermaid
xychart-beta
    title "Jordiag/azure-devops-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c543c8e146c0` · [字段定义](../../DATASET.md)*
