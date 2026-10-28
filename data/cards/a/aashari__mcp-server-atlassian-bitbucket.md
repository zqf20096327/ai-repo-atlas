# aashari/mcp-server-atlassian-bitbucket

⭐ 163 · TypeScript · 推送 2026-03-06 · [GitHub](https://github.com/aashari/mcp-server-atlassian-bitbucket) · 个人维护

**连接 AI 助手与 Bitbucket 仓库/PR 的 MCP 服务器**

Node.js/TypeScript 实现的 MCP server，使 Claude Desktop、Cursor、Cline 等 MCP 客户端通过 6 个通用工具（get/post/put/patch/delete/clone）访问任意 Bitbucket Cloud REST API 2.0 端点，覆盖工作区、仓库、分支、提交、PR、流水线等资源。默认输出 TOON 格式（自称较 JSON 减少 30-60% token），支持 JMESPath 过滤；另带镜像 MCP 工具的 CLI。限制：仅支持 Bitbucket Cloud，不支持 Server/Data Center；需 Node.js 18+ 与 Scoped API Token 或 App Password（后者将于 2026 年 6 月弃用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个通用工具可访问任意 Bitbucket Cloud API 2.0 端点
- 默认 TOON 输出格式与 JMESPath 过滤以减少 token 消耗
- 官方支持 Claude Desktop，兼容 Cursor、Continue.dev、Cline 等 MCP 客户端
- CLI 命令与 MCP 工具对应，可直接在终端调用

## 适用场景

- 让 AI 助手查看仓库、分支与提交内容
- 通过自然语言创建、评论、审批或合并 PR
- 在 AI 工作流中自动化 Bitbucket 仓库操作

## 场景标签

 · 领域:开发工具/AI 集成

## 证据(README 行号)

> L140: This MCP server provides 6 generic tools that can access any Bitbucket API endpoint:
> L110: - Claude Desktop (official support)

## 星数曲线

```mermaid
xychart-beta
    title "aashari/mcp-server-atlassian-bitbucket 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-28 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a42d232644fb` · [字段定义](../../DATASET.md)*
