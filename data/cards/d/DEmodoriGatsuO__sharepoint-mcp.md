# DEmodoriGatsuO/sharepoint-mcp

⭐ 94 · Python · NOASSERTION · 推送 2026-04-14 · [GitHub](https://github.com/DEmodoriGatsuO/sharepoint-mcp) · 个人维护

**让 LLM 应用通过 MCP 访问 SharePoint 文档与列表的连接器**

基于 Model Context Protocol 的服务器，将 LLM 应用（如 Claude Desktop）经 Microsoft Graph API 接入 SharePoint 站点。暴露 15 个 MCP 工具：读取 DOCX/PDF/XLSX/CSV/TXT 文档、全文搜索、上传文件、创建/更新列表项、创建站点/页面/新闻帖等。需要 Python 3.10+、Azure AD 应用注册与 Microsoft 365 SharePoint 站点；提供配置校验与认证诊断脚本，支持 stdio/SSE/streamable-http 传输，可 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个 MCP 工具：文档读取、全文搜索、上传、列表与站点管理
- 读取并解析 DOCX/PDF/XLSX/CSV/TXT 文件内容
- 支持 stdio、SSE、streamable-http 三种传输方式
- 提供 config_checker 与 auth-diagnostic 诊断脚本

## 适用场景

- 在 Claude Desktop 中用自然语言查询 SharePoint 文档
- 让 AI 助手在 SharePoint 中创建列表、页面与上传文件
- 通过 HTTP/Docker 部署供 Copilot 类 web 客户端调用

## 场景标签

 · 领域:AI 工具集成/企业协作

## 证据(README 行号)

> L12: SharePoint MCP Server is a Model Context Protocol (MCP) server that connects LLM applications such as Claude to you
> L25: |**Transport**|stdio (local), SSE, streamable-http (web / Docker)|
> L123: The following MCP tools are exposed to the LLM:

## 星数曲线

```mermaid
xychart-beta
    title "DEmodoriGatsuO/sharepoint-mcp 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-28", "2026-10-30"]
    y-axis "stars" 90 --> 95
    line [91, 92, 93, 94, 94]
```

2026-10-18 91 → 2026-10-30 94（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `745623aadf9d` · [字段定义](../../DATASET.md)*
