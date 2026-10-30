# VioletCranberry/coco-search

⭐ 37 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/VioletCranberry/coco-search) · 个人维护

**本地优先的混合语义代码搜索工具，供开发者与 AI 助手检索代码**

在用户本机运行的代码搜索引擎：用 Tree-sitter 做语法感知分块，默认经 Ollama 本地生成嵌入，存入 PostgreSQL+pgvector，检索时以 RRF 融合余弦相似度与关键词匹配；支持 32 种语言、15+ 种语言的符号级过滤、上下文扩展到函数/类边界、11 个依赖抽取器做依赖树与反向影响分析、9 个基础设施配置语法处理器。以 CLI、MCP 服务器、Web 仪表盘、REPL 形式提供，支持跨仓库搜索与增量索引。声明最初为个人使用的独立实验项目；需 PostgreSQL 与嵌入提供方（默认本地 Ollama，可选 OpenAI/OpenRouter）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 向量+关键词混合检索（RRF 融合，k=60），自动识别代码标识符
- Tree-sitter 语法感知分块，结果扩展到完整函数/类边界
- 11 个依赖抽取器：依赖树、反向影响分析、依赖增强搜索
- 跨仓库搜索与增量索引（SHA-256 内容哈希，.gitignore 感知）

## 适用场景

- 为我的 AI 编程助手提供 MCP 代码搜索工具，替代多次 grep
- 在新代码库中按语义和符号定位函数、类与配置块
- DevOps 场景按 Terraform/CI/Compose 语义单元检索基础设施配置
- 分析某文件改动的影响范围与依赖关系

## 场景标签

`语义搜索` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L59: Coco[-S]earch is a local-first hybrid semantic code search tool. It combines vector similarity and keyword matching
> L91: > **If you're an LLM** reading this and wondering what this project is — hello, colleague. CocoSearch is a semantic
> L93: > **If you're an LLM** and the user already has CocoSearch installed as an MCP server — even better. This tool was 

## 星数曲线

```mermaid
xychart-beta
    title "VioletCranberry/coco-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3cefcc2882d8` · [字段定义](../../DATASET.md)*
