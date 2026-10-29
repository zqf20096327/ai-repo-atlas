# Asem-D/arcgis-portal-mcp

⭐ 23 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/Asem-D/arcgis-portal-mcp) · 个人维护

**让 AI 助手用自然语言操作 ArcGIS Portal/Online 的 MCP 服务器**

面向 ArcGIS Enterprise Portal 与 ArcGIS Online 的 Model Context Protocol 服务器，提供 81 个工具，使 Claude Desktop、Cursor、VS Code Copilot 等 MCP 客户端能搜索、检查、编辑、发布内容并执行门户管理：图层查询与要素增删、GP 工具执行、地图图片导出、用户/组/定时任务/Webhook 管理、内容治理（失效引用扫描、陈旧内容清理）等。通过原生 REST API 调用实现，不依赖 arcgis Python SDK；支持 token/用户名密码/client_credentials/OAuth2 多种认证与 2FA、自签名证书场景，并提供只读模式、工具白名单、审计日志等安全机制。以 pip 安装，经 .env 文件自动连接。项目独立于 Esri。

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

- 81 个工具覆盖搜索、要素编辑、发布服务、GP 执行与门户管理
- 原生 REST API 调用，不依赖 arcgis Python SDK
- 只读模式、工具白名单、作用域白名单与审计日志等安全机制
- 支持 Claude Desktop / Cursor / VS Code Copilot / Windsurf 等 MCP 客户端

## 适用场景

- 在 AI 编程助手中用自然语言查询和编辑 ArcGIS 托管要素图层
- 扫描门户中的失效服务引用与陈旧内容做治理清理
- 批量转移内容所有权与用户离职处理
- 通过 AI 客户端发布数据文件为托管要素服务

## 场景标签

 · 领域:GIS/AI 工具接入

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server that gives AI assistants direct access to your ArcGIS content. Search, inspect
> L7: Works with Claude Desktop, Cursor, VS Code Copilot, and any MCP-compatible client.

## 星数曲线

```mermaid
xychart-beta
    title "Asem-D/arcgis-portal-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fc296644c202` · [字段定义](../../DATASET.md)*
