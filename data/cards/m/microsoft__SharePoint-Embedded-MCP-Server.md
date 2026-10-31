# microsoft/SharePoint-Embedded-MCP-Server

⭐ 14 · TypeScript · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/microsoft/SharePoint-Embedded-MCP-Server) · 组织维护

**微软官方的 SharePoint Embedded MCP 服务器：让 AI 客户端管理 SPE 资源**

Microsoft 维护的 Model Context Protocol 服务器，以 stdio 方式经 npx 启动，供 VS Code Copilot、Claude Desktop、Cursor 等 MCP 兼容客户端通过自然语言管理 SharePoint Embedded 资源。提供 40 个工具，覆盖容器类型/容器创建与注册、Azure 计费设置、项目脚手架生成与 azd 部署、文件内容操作及文档检索（经 Microsoft Learn MCP）。默认 Bootstrap 模式复用 Azure CLI 登录态，需 Node.js 22/24/26。标注为 Preview 软件，资源配置可能产生 Azure 费用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 40 个工具覆盖预配、计费、脚手架、部署与内容操作
- 默认 Bootstrap 模式无需预先注册应用，复用 Azure CLI 会话
- 提供 --read-only 与 --tools 工具集限制等安全控制
- 文档工具代理公共 Microsoft Learn MCP 检索官方文档

## 适用场景

- 在 AI 编程客户端中用自然语言预配 SharePoint Embedded 容器
- 从参考架构脚手架一键生成并部署应用到 Azure
- 对容器内文件执行上传、搜索与共享管理

## 场景标签

 · 领域:云资源管理/开发工具

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for SharePoint Embedded. Lets any MCP-compatible AI client (VS Code Copilot, C
> L9: **One-click install** — add the `@microsoft/spe-mcp` server to your MCP client (stdio, launched via `npx -y @microso
> L23: The server exposes **40 tools**, plus an MCP **Prompt** (`provision_spe_app`) and **Resources** (reference architec

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/SharePoint-Embedded-MCP-Server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ec533e197dfa` · [字段定义](../../DATASET.md)*
