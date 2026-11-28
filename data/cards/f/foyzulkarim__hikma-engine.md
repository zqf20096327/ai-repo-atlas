# foyzulkarim/hikma-engine

⭐ 10 · TypeScript · MIT · 推送 2026-01-06 · [GitHub](https://github.com/foyzulkarim/hikma-engine) · 个人维护

**把 Git 仓库索引成知识图谱，供 AI agent 检索代码**

其 rag 命令调用 LLM 对检索结果生成代码解释；主体是面向 AI agent 的索引基础设施。

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

- AST 解析提取代码结构关系并结合向量嵌入生成可检索知识库
- embed/search/rag 统一 CLI，显式参数配置，支持 npx 免安装运行
- 多提供方嵌入与 LLM：Python 本地模型、OpenAI API、Ollama/LM Studio 兼容服务
- 每项目独立 SQLite 数据库（sqlite-vec），支持多项目并行

## 适用场景

- 为 AI agent/编码助手建立代码库语义检索后端
- 本地离线环境下对私有仓库做嵌入索引与 RAG 问答
- 在 CI/CD 脚本中自动化代码库索引与查询

## 场景标签

`知识图谱` `RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A TypeScript-based code knowledge graph indexer that transforms Git repositories into searchable knowledge stores fo
> L13: - **Unified CLI**: Single `hikma-engine` command for all operations (embed, search, rag)
> L43: Hikma Engine provides three main commands: `embed`, `search`, and `rag` with an **explicit CLI approach** that requ


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `223d62411da1` · [字段定义](../../DATASET.md)*
