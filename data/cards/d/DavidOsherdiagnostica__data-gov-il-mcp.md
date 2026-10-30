# DavidOsherdiagnostica/data-gov-il-mcp

⭐ 110 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp) · 个人维护

**接入以色列政府开放数据的 MCP 服务器，供 MCP 客户端查询数据集**

TypeScript 实现的 Model Context Protocol 服务器，通过官方 CKAN API 向 MCP 兼容客户端（如 Claude Desktop、Claude Code、Cursor）提供 data.gov.il 的数据集、资源、标签、组织和表记录的结构化访问。内置目录快照支持希伯来语规范化、模糊匹配与多信号加权排序，含 9 个默认工具、5 个静态资源与 3 个领域提示词。支持 stdio 与 Streamable HTTP 传输，可选 API key 与 OAuth 2.1 认证、HTTP 加固配置；Elicitation 与 Sampling 功能默认关闭，客户端不支持时自动回退。

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

- 9 个默认工具 + 5 个静态资源 + 3 个领域提示词
- 内置目录快照：希伯来语规范化、trigram 模糊索引、标签共现与加权排序
- 支持 stdio 与 Streamable HTTP 传输，可选 API key / OAuth 2.1 JWT 认证
- HTTP 加固：Helmet、CORS、限流、Host/Origin 校验

## 适用场景

- 在 Claude Desktop 或 Cursor 中查询以色列政府数据集
- 通过 MCP 客户端检索 CKAN datastore 记录并按字段过滤排序
- 以 HTTP 传输远程部署开放数据查询服务

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Production-grade Model Context Protocol (MCP) server for Israeli Government Open Data from data.gov.il.
> L7: This server gives MCP-compatible clients structured access to Israeli government datasets, resources, tags, organiza

## 星数曲线

```mermaid
xychart-beta
    title "DavidOsherdiagnostica/data-gov-il-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-30 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e6775ee51e27` · [字段定义](../../DATASET.md)*
