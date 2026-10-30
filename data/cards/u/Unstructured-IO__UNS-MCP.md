# Unstructured-IO/UNS-MCP

⭐ 43 · Jupyter Notebook · 推送 2026-10-20 · [GitHub](https://github.com/Unstructured-IO/UNS-MCP) · 组织维护

**管理 Unstructured 平台连接器与工作流的 MCP 服务器（已停止维护）**

面向 Unstructured API 的 MCP 服务器实现，提供 21 个工具对平台的 source/destination 连接器与工作流进行增删改查、运行与作业管理，支持 S3/Azure/Google Drive/Pinecone/Weaviate 等连接器，凭据经 .env 配置。另集成 Firecrawl 网页抓取与 LLM 文本生成工具。可经 uvx、pip 包或源码安装，接入 Claude Desktop，支持 stdio 与 SSE 协议，附最小客户端与 MCP Inspector 调试。README 声明本服务器不再积极维护，仅作参考。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 个工具管理连接器、工作流与作业（创建/运行/取消/删除）
- 支持 S3/Azure/Google Drive/Salesforce 等源与 S3/Pinecone/Weaviate/Neo4j 等目标
- 集成 Firecrawl 网页抓取与 LLM 优化文本生成
- 支持 stdio 与 SSE 协议，可接入 Claude Desktop

## 适用场景

- 让 Claude 等 MCP 客户端直接管理 Unstructured 平台的数据源与目标连接器
- 通过对话创建并运行文档处理工作流
- 用 Firecrawl 工具抓取网站并生成面向 LLM 的文本

## 场景标签

`网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L12: An MCP server implementation for interacting with the Unstructured API. This server provides tools to list sources 
> L39: Below is a list of connectors the `UNS-MCP` server currently supports, please see the full list of source connector

## 星数曲线

```mermaid
xychart-beta
    title "Unstructured-IO/UNS-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c833eb128bbd` · [字段定义](../../DATASET.md)*
