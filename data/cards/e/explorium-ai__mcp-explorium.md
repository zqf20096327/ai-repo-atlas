# explorium-ai/mcp-explorium

⭐ 22 · Dockerfile · MIT · 推送 2026-03-03 · [GitHub](https://github.com/explorium-ai/mcp-explorium) · [官网](https://www.explorium.ai) · 组织维护

**连接 Explorium B2B 商业数据 MCP 服务器的配置与接入仓库**

提供 Explorium 商业数据 MCP 服务器的连接配置与自托管文件：通过远程 URL（Streamable HTTP/SSE）或本地 STDIO 方式，让 Claude Desktop、Cursor、Windsurf、VS Code、Zed、Cline、JetBrains 等 MCP 客户端访问公司搜索与富化、联系人发现、商业事件追踪、潜客发现等工具。仓库内 server/index.js 仅为占位文件，实际 MCP 服务由 Explorium 远程托管；Docker 自托管部署需 API key，远程连接则无需。

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

- 提供公司搜索/富化、联系人发现与富化、商业事件与潜客事件等数据工具
- 覆盖 Claude Desktop、Cursor、Windsurf、VS Code、Zed、Cline、JetBrains 等多种 MCP 客户端安装配置
- 支持远程 Streamable HTTP/SSE 与本地 STDIO 连接，远程连接无需 API key
- 附 Docker 自托管配置，需 API_ACCESS_TOKEN

## 适用场景

- 在 AI 编程助手中直接查询目标公司的联系人信息做外联
- 研究合作方公司的技术栈、融资历史与增长信号
- 销售与商务团队通过对话发现和富化潜客名单

## 场景标签

 · 领域:B2B 商业数据/AI 集成

## 证据(README 行号)

> L14: This repository contains the configuration and setup files for connecting to Explorium's Model Context Protocol (MC
> L318: **Important Note**: The `server/index.js` file in this repository is just a placeholder and does not contain the a

## 星数曲线

```mermaid
xychart-beta
    title "explorium-ai/mcp-explorium 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `62e32651076b` · [字段定义](../../DATASET.md)*
