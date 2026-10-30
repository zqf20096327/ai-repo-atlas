# cbtw-apac/qdrant-loader

⭐ 57 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/cbtw-apac/qdrant-loader) · [官网](https://qdrant-loader.net) · 组织维护

**向 Qdrant 摄入多源数据并经 MCP 提供语义搜索的工具集**

包含三个 pip 包的 monorepo：数据摄取引擎从 Git、Confluence、JIRA、本地文件等来源收集内容，经 MarkItDown 转换 PDF/Office/图片等格式，分块向量化后写入 Qdrant；核心库提供 OpenAI、Azure OpenAI、Ollama 等统一 LLM 抽象与配置管理；MCP 服务器遵循 MCP 2025-06-18 协议，支持 stdio 与 HTTP 双传输，向 Cursor、Windsurf、Claude Desktop 等 AI 开发工具提供语义搜索、跨文档相似度与知识图谱能力。面向搭建可搜索知识库的开发者与企业内容整合场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Git/Confluence/JIRA/本地文件等多源连接器与增量更新
- 基于 MarkItDown 的 PDF/Office/图片/音频等文件转换与智能分块
- MCP 服务器支持 stdio+HTTP 双传输、SSE 流式搜索与跨文档知识图谱
- LLM 提供商抽象：OpenAI、Azure OpenAI、Ollama 与自定义端点统一配置

## 适用场景

- 把 Confluence/JIRA/Git 文档整合成可检索的知识库
- 在 Cursor/Windsurf/Claude Desktop 中通过 MCP 查询项目知识
- 企业多项目内容统一向量化与语义搜索

## 场景标签

`语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L16: QDrant Loader is a data ingestion and retrieval system that collects content from multiple sources, processes and v
> L62: Model Context Protocol server providing search capabilities to AI development tools.

## 星数曲线

```mermaid
xychart-beta
    title "cbtw-apac/qdrant-loader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-30 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `78e6d2f06431` · [字段定义](../../DATASET.md)*
