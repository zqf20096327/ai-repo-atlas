# nguyenvanduocit/jira-mcp

⭐ 97 · Go · MIT · 推送 2026-04-18 · [GitHub](https://github.com/nguyenvanduocit/jira-mcp) · 个人维护

**Go 编写的 Jira MCP 服务器，让 AI 助手操作 Jira**

基于 Go 的 MCP 服务器，通过 20 余个工具将 Jira 操作暴露给 Claude、Cursor 等 AI 助手：问题管理、JQL 搜索、Sprint 管理、状态流转、评论、工时记录、变更历史、问题关联、版本与开发信息（分支/PR/commit）。认证使用 Atlassian API token（host/email/token 环境变量），支持 STDIO 与可选 HTTP 模式，可经 ENABLED_TOOLS 限制暴露的工具子集（如只读 15 个读工具）。另附带独立的 jira-cli 命令行二进制，无需 MCP 客户端即可在终端执行常用 Jira 操作。安装途径包括 Homebrew、go install 与 Docker。

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

- 20+ 个 MCP 工具覆盖问题/Sprint/评论/工时/开发信息等 Jira 操作
- ENABLED_TOOLS 环境变量按白名单限制暴露工具，支持只读 agent 配置
- 附带独立 jira-cli 命令行二进制，无需 MCP 客户端
- 支持 STDIO 与可选 HTTP 模式运行

## 适用场景

- 在 Claude Desktop/Cursor 中直接查询和操作 Jira 问题与 Sprint
- 为 AI agent 提供只读的 Jira 数据视图
- 在终端用 jira-cli 快速执行 Jira 操作

## 场景标签

 · 领域:开发工具/项目管理集成

## 证据(README 行号)

> L131: - This is a Go-based MCP server that connects AI assistants to Jira
> L57: Install the Jira MCP server (https://github.com/nguyenvanduocit/jira-mcp) for my Claude Desktop or Cursor IDE. Read

## 星数曲线

```mermaid
xychart-beta
    title "nguyenvanduocit/jira-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-20"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-20 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `d50d61260e4c` · [字段定义](../../DATASET.md)*
