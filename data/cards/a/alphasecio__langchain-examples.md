# alphasecio/langchain-examples

⭐ 551 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/alphasecio/langchain-examples) · [官网](https://go.alphasec.io/langchain-examples) · 个人维护

**开发者示例应用：一个 Streamlit 应用集成四个 LangChain 工具**

单个 Streamlit 应用内集成四个 LangChain 工具：带引用来源的 Web 研究代理、文本/网页/PDF 摘要、新闻摘要聚合、基于 Postgres+pgvector 的文档问答（页级引用）。使用 OpenAI 模型，支持用户自选搜索服务商（Tavily/Exa/Firecrawl/Perplexity 等 8 个，API key 可配）。提供 Railway 一键部署模板，也可在任意带 Docker 与 Postgres 的 VPS 运行或本地 pip 运行；支持 OpenAI 兼容端点与侧边栏临时输入 key、APP_PASSWORD 保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个工具：Web 研究代理、摘要、新闻摘要、文档问答
- pgvector 向量存储，问答带页级引用
- 支持 8 个可自选的搜索服务商 API key
- 提供 Railway 部署模板与本地运行步骤

## 适用场景

- 让 AI 代理搜索网页并给出带引用的回答
- 对粘贴文本、网页或 PDF 生成不同粒度的摘要
- 把 PDF/文本/Markdown 存入向量库后提问检索

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L19: A single Streamlit app with four practical LangChain tools, using OpenAI models, your choice of web search provider
> L23: |🔎 **Web Research**|An agent that searches the web, reads pages and answers with cited sources.|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `24d9ea67735d` · [字段定义](../../DATASET.md)*
