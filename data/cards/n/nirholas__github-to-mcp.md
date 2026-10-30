# nirholas/github-to-mcp

⭐ 34 · TypeScript · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/nirholas/github-to-mcp) · [官网](https://nirholas.github.io/github-to-mcp/) · 个人维护

**将 GitHub 仓库自动生成为 MCP 服务器的代码生成工具**

输入一个 GitHub 仓库 URL，该工具分析仓库类型（API SDK、CLI 工具、库等），从 OpenAPI/Swagger、GraphQL schema、gRPC/Protobuf、AsyncAPI 规范、源码函数与 README 示例中提取工具，生成完整可运行的 MCP 服务器代码（TypeScript/Python/Go 输出）及 Claude Desktop、Cursor 等客户端配置文件。面向需要让 AI 助手编程化访问代码仓库的开发者。提供 Web 界面（Vercel 部署）、npx 一行命令与 TypeScript 编程 API 三种使用方式；支持多语言输入仓库，可选配置 GitHub Token（无 token 限速 60 次/小时）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 OpenAPI/GraphQL/gRPC/AsyncAPI 规范与源码自动提取 MCP 工具
- 生成完整可运行的 TypeScript/Python/Go MCP 服务器及客户端配置
- 每个生成的服务器附带 read_file/list_files/search_code 等通用仓库探索工具
- 提供 Web 界面、npx CLI 与编程 API 三种使用方式

## 适用场景

- 把公司的 API SDK 仓库转成 MCP 服务器接入 Claude Desktop 或 Cursor
- 让 AI 编程助手直接读取、搜索和调用某个 GitHub 仓库的功能
- 自动化批量为多个仓库生成 MCP 服务器

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L24: GitHub to MCP bridges the gap between code repositories and AI assistants. Instead of manually describing APIs or c
> L41: This project generates MCP servers from GitHub repositories, automatically creating tools based on the repository's
> L100: - Configuration files for Claude Desktop, Cursor, and other clients

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/github-to-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-30 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c3c49b7bbb42` · [字段定义](../../DATASET.md)*
