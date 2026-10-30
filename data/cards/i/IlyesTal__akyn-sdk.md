# IlyesTal/akyn-sdk

⭐ 23 · TypeScript · MIT · 推送 2026-01-08 · [GitHub](https://github.com/IlyesTal/akyn-sdk) · [官网](https://akyn.dev) · 组织维护

**把任意数据源变成 MCP 服务器/知识库的 TypeScript SDK**

面向开发者的 SDK：将 PDF、DOCX、TXT、Markdown、URL 等数据源索引为可检索知识库，并通过 stdio 或 HTTP 暴露为 MCP 服务器，供 Claude Desktop、Cursor 等 AI 助手直接查询。提供自动分块、可插拔 embeddings（默认 OpenAI，可自定义）、内置内存向量库并支持 Qdrant（含 Docker 本地部署与 Qdrant Cloud）。附带 CLI 可免代码索引目录，检索参数（topK/相似度阈值）在代码侧配置。要求 Node.js 18+，默认需 OpenAI API key。另有托管服务 Akyn 供选择。

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

- 将文件/URL/目录索引为 MCP 服务器，供 Claude/Cursor 查询
- 可插拔 embeddings 与向量库（内存默认，支持 Qdrant）
- CLI 与 SDK 双用法，stdio/HTTP 两种传输方式
- 检索参数（topK/threshold）在代码侧控制，不暴露给 agent

## 适用场景

- 让自己的文档被 Cursor/Claude 直接检索
- 为 AI 助手构建领域知识库
- 搭建 RAG 检索管线的数据接入层

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L12: This SDK lets you create MCP (Model Context Protocol) servers from any data source. Your docs, PDFs, websites, or a
> L160: // Stdio (for Cursor/Claude Desktop)

## 星数曲线

```mermaid
xychart-beta
    title "IlyesTal/akyn-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `08cdcac8e0bb` · [字段定义](../../DATASET.md)*
