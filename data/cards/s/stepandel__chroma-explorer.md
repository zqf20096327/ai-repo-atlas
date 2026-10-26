# stepandel/chroma-explorer

⭐ 46 · TypeScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/stepandel/chroma-explorer) · [官网](https://www.chroma-explorer.com/) · 个人维护

**macOS 桌面应用：浏览与管理 ChromaDB 向量数据库**

基于 Electron 与 React 构建的 macOS 桌面应用，面向使用 ChromaDB 的开发者：支持多配置连接本地、远程或 Chroma Cloud 数据库；提供集合的创建/复制/删除与自定义嵌入函数配置、文档的批量增删改查、自然语言语义搜索与元数据过滤。语义搜索支持 OpenAI、Cohere、Ollama、HuggingFace Server 等 13+ 嵌入提供方，API key 在设置中配置并加密存储。开发通过 pnpm 安装依赖与构建；默认开启错误上报，可在设置中关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多配置文件连接本地/远程/Chroma Cloud 数据库
- 文档批量增删改查与元数据过滤查询
- 自然语言语义搜索，支持 13+ 嵌入提供方
- API key 加密存储于设置中

## 适用场景

- 浏览和调试 ChromaDB 中的集合与文档
- 为 RAG 应用核查向量库数据内容
- 通过语义搜索验证嵌入与检索效果

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: A desktop application for exploring and managing ChromaDB vector databases. Built with Electron and React.
> L17: - **Semantic Search** - Query documents using natural language with 13+ embedding providers
> L23: OpenAI, Cohere, Google Gemini, Ollama, HuggingFace Server, Mistral, Voyage AI, Together AI, Jina, Cloudflare Worker

## 星数曲线

```mermaid
xychart-beta
    title "stepandel/chroma-explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ee69a32a3ad6` · [字段定义](../../DATASET.md)*
