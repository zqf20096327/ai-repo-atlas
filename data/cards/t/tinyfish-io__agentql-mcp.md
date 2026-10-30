# tinyfish-io/agentql-mcp

⭐ 181 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/tinyfish-io/agentql-mcp) · [官网](https://docs.agentql.com/integrations/mcp) · 组织维护

**让 MCP 客户端调用 AgentQL 提取网页结构化数据的服务器**

AgentQL 官方的 Model Context Protocol 服务器，向支持 MCP 的客户端（Claude Desktop、VS Code、Cursor、Windsurf）暴露一个 extract-web-data 工具：给定 URL 与提示词，返回网页结构化数据提取结果。使用需从 Dev Portal 获取 API key，通过 npm 全局安装或 npx 按配置文件方式接入各客户端。仓库同时提供开发构建与 MCP Inspector 调试脚本。

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

- 提供 extract-web-data 工具：按 URL + 提示词提取结构化数据
- 覆盖 Claude Desktop / VS Code / Cursor / Windsurf 的接入配置说明
- 提供 npm 全局安装、npx 一键安装与 VS Code install 按钮多种方式
- 内置 MCP Inspector 调试脚本（npm run inspector）

## 适用场景

- 在 Claude Desktop 等 MCP 客户端中让 agent 抓取网页数据
- 用自然语言指定字段，提取页面列表/表格内容
- 为团队共享 VS Code 工作区级 MCP 配置

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: This is a Model Context Protocol (MCP) server that integrates AgentQL's data extraction capabilities.
> L9: - `extract-web-data` - extract structured data from a given 'url', using 'prompt' as a description of actual data an

## 星数曲线

```mermaid
xychart-beta
    title "tinyfish-io/agentql-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 180 --> 183
    line [182, 181, 181]
```

2026-10-18 182 → 2026-10-30 181（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2243eb97eb02` · [字段定义](../../DATASET.md)*
