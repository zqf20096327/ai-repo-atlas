# microsoft/devbox-mcp-server

⭐ 14 · MIT · 推送 2025-12-12 · [GitHub](https://github.com/microsoft/devbox-mcp-server) · 组织维护

**微软 Dev Box 的 MCP 服务器：让 AI agent 管理云开发机**

微软官方的 Model Context Protocol 服务器，连接 AI agent 与 Microsoft Dev Box 服务，支持自然语言操作 Dev Box 的创建、启停、删除、计划任务、定制化任务、项目与池管理等。通过 npx 安装到 VS Code、Visual Studio 等 MCP 客户端使用；需 Node.js 18+、Azure 订阅、已预配的 Dev Center 及 RBAC 权限。认证采用 DefaultAzureCredential 链（环境变量、托管标识、VS Code、Azure CLI/PowerShell、Windows SSO/WAM）。

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

- 以 scope 模式统一管理 Dev Box 生命周期（列表/创建/删除/启停/修复）
- 支持计划任务（延迟/跳过）、定制化任务与镜像构建日志查看
- 一键安装到 VS Code，npx 方式运行
- DefaultAzureCredential 多级认证链含 Windows WAM 单点登录

## 适用场景

- 在 VS Code Copilot 中用自然语言创建和管理 Dev Box
- 通过 AI agent 查看 Dev Box 状态并执行启停操作
- 在 Dev Box 上远程安装软件包或运行命令

## 场景标签

 · 领域:开发工具/云基础设施

## 证据(README 行号)

> L5: This is a Model Context Protocol (MCP) server for Microsoft Dev Box, providing seamless integration between AI agent
> L96: The Dev Box MCP provides tools for interacting with the following Microsoft Dev Box resources:

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/devbox-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `44ee2d4daf6c` · [字段定义](../../DATASET.md)*
