# peteretelej/directory-indexer

⭐ 18 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/peteretelej/directory-indexer) · [官网](https://etelej.com/apps/directory-indexer) · 个人维护

**将本地目录索引为知识库、供 AI 助手语义检索的 MCP Server**

自托管的本地文件语义搜索服务：读取本地目录中的文本、代码、数据与配置文件，通过嵌入服务（Ollama 本地模型或 OpenAI API）生成向量并存入 Qdrant 向量数据库，再以 MCP Server 形式接入 Claude Desktop、Cursor、Cline 等 AI 助手，使其可按概念、相似内容检索本地文件。提供 npx/npm 安装与 CLI 索引命令，支持多工作区隔离、增量重索引与后台索引。需自行运行 Qdrant 与嵌入服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将本地文件向量化存入 Qdrant，通过 MCP 供 AI 助手语义检索
- 嵌入服务可选 Ollama 本地（免费）或 OpenAI API（付费）
- 支持工作区划分、仅重处理变更文件的增量重索引
- 支持文本/代码/数据/配置等文件类型，PDF、docx 尚未支持

## 适用场景

- 让 Claude Desktop/Cursor 等 AI 助手检索我的本地笔记与项目文档
- 按概念或相似内容在工作文件中查找示例与排障方案
- 将不同目录组织为工作区做分区检索

## 场景标签

`语义搜索` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L10: Self-hosted semantic search for local files. Give your AI assistant access to search, read, and work with your loca
> L88: Directory Indexer runs locally on your machine or server. It uses an embedding provider (such as Ollama) to create 
> L169: 1. **MCP server starts automatically** - When your AI assistant connects, it launches the MCP server in the backgr

## 星数曲线

```mermaid
xychart-beta
    title "peteretelej/directory-indexer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `3cfc76b003dc` · [字段定义](../../DATASET.md)*
