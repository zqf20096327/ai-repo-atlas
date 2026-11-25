# apify/apify-mcp-server

⭐ 17,608 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/apify/apify-mcp-server) · [官网](https://mcp.apify.com) · 组织维护

**让 AI agent 通过 MCP 调用 Apify Store 数千抓取/自动化工具**

Apify 官方的 Model Context Protocol 服务器：通过一次连接让 agent 搜索 Apify Store、查看 Actor 的输入模式与定价、运行 Actor 并读取数据集结果，覆盖网页抓取、数据提取、浏览器自动化、SERP 监控、线索生成等任务。提供托管端点（OAuth/Bearer 认证）与本地 stdio 两种运行方式，支持按类别或名称选择性加载工具，可把单个 Actor 暴露为独立工具，并为 Actor 声明 JSON Schema 输出模式。使用需要 Apify 账户与 API token。

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

- search-actors/fetch-actor-details/call-actor/get-dataset-items 四步调用流程
- 托管服务器（OAuth/Bearer）与本地 stdio（npx @apify/actors-mcp-server）两种部署
- Actor 输出模式以 JSON Schema 形式在运行前告知 agent
- Docker MCP 目录收录，每次发布附带 .mcpb 一键安装包

## 适用场景

- 让 coding agent 抓取网页、电商或社媒数据供后续处理
- 为 RAG 流程抓取网站内容作为语料
- 通过 agent 自动化 SERP 监控与线索收集任务

## 场景标签

`浏览器自动化` `网页抓取` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L19: **The official Apify Model Context Protocol (MCP) server gives AI agents web scraping, data extraction, and browser
> L23: Your agent searches Apify Store, checks an Actor's input and pricing, runs it, and reads the structured results, so

## 星数曲线

```mermaid
xychart-beta
    title "apify/apify-mcp-server 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 12107 --> 18108
    line [12607, 12795, 12935, 13102, 13308, 13461, 13639, 13790, 13939, 14067, 14218, 12935, 15293, 15611, 15755, 15970, 16127, 16258, 16381, 16559, 16714, 16890, 17055, 17169, 17289, 17428, 17608]
```

2026-10-23 12,607 → 2026-11-25 17,608（+5,001）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `4915081634bf` · [字段定义](../../DATASET.md)*
