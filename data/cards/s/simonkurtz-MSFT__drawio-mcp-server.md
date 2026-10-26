# simonkurtz-MSFT/drawio-mcp-server

⭐ 82 · TypeScript · MIT · 推送 2026-05-15 · [GitHub](https://github.com/simonkurtz-MSFT/drawio-mcp-server) · 个人维护

**供 AI 客户端生成 Draw.io 图表的 MCP 服务器**

基于 Model Context Protocol 的图表生成服务器：直接生成 Draw.io XML，无需浏览器扩展或 Draw.io 实例。内置 700+ 官方 Azure 架构图标（约 20 类）与基础流程图形状，提供模糊搜索、批量增删改单元格、图层/页面/分组管理等约 25 个工具，支持 stdio 与 HTTP 两种传输。面向 Claude Desktop、VS Code、Codex、Zed、oterm 等 MCP 客户端用户，要求 Deno v2.3+，提供 Docker Hub 预构建镜像（distroless，约 20MB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接生成 Draw.io XML，无需浏览器扩展或 Draw.io 实例
- 700+ Azure 架构图标，约 20 类，支持模糊搜索
- 提供形状发现/图表修改/图层/页面/分组管理等工具集，支持批量操作与 dry_run 校验
- 支持 stdio 与 streamable HTTP 双传输，提供 Docker 预构建镜像

## 适用场景

- 让 Claude/VS Code 等 MCP 客户端通过对话生成 Azure 架构图与流程图
- 程序化批量构建和修改 Draw.io 图表 XML
- 在本地或容器中运行图表生成服务供多个客户端接入

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server 
> L54: Configure your MCP client (Claude Desktop, VS Code, Codex, etc.) to use the server:
> L295: ## Tools

## 星数曲线

```mermaid
xychart-beta
    title "simonkurtz-MSFT/drawio-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-26 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `606f08d25733` · [字段定义](../../DATASET.md)*
