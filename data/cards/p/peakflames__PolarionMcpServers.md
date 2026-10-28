# peakflames/PolarionMcpServers

⭐ 42 · C# · MIT · 推送 2026-10-26 · [GitHub](https://github.com/peakflames/PolarionMcpServers) · 组织维护

**面向 Polarion ALM 的 MCP 服务器，供 AI 客户端读取工作项**

提供两个 MCP 服务器实现：Streamable HTTP 远程版（PolarionRemoteMcpServer，无状态，支持可选 OAuth 2.1 认证与按调用者 RBAC）与本地 stdio 控制台版（PolarionMcpServer）。暴露 15 个工具用于读取 Polarion 文档、工作项、修订历史、自定义字段并支持文本/SQL 检索，另附 REST API 与健康检查端点。通过 appsettings.json 配置一个或多个 Polarion 项目，密码可用 POLARION_PASSWORD 环境变量覆盖。主要给希望 AI 编码/对话客户端访问 Polarion 数据的开发者与企业使用；README 提示不要多副本运行（会话不共享）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个 Polarion 工作项/文档读取与检索 MCP 工具（含 opt-in 只读 SQL 查询）
- HTTP 与 stdio 两种服务器形态，Docker 部署
- 可选 OAuth 2.1 认证（RFC 9728 发现）与按调用者 RBAC
- REST API 提供 API Key 认证与 polarion:read 作用域

## 适用场景

- 让 Cline、VS Code、Claude 等 MCP 客户端读取 Polarion 需求与工作项
- 通过 AI 客户端对 Polarion 项目做文本或 SQL 检索
- 企业按用户身份控制对 Polarion 项目的 MCP 访问

## 场景标签

 · 领域:ALM/AI 工具集成

## 证据(README 行号)

> L3: This repository contains Model Context Protocol (MCP) server implementations for Polarion Application Lifecycle Mana
> L25: - **PolarionRemoteMcpServer**: Streamable HTTP MCP server for server-based installations. Stateless, with optional 

## 星数曲线

```mermaid
xychart-beta
    title "peakflames/PolarionMcpServers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `da5b9c889700` · [字段定义](../../DATASET.md)*
