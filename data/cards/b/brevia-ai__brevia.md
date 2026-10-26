# brevia-ai/brevia

⭐ 32 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/brevia-ai/brevia) · [官网](http://docs.brevia.app) · 组织维护

**面向开发者的 RAG 与信息抽取应用构建框架及 API**

基于 LangChain 与 FastAPI 的可扩展 API 和框架，用于构建 RAG 问答与信息抽取（如摘要、自定义分析、后台异步任务）应用，以 PostgreSQL + pgvector 扩展作为向量数据库。提供 Docker Compose 快速启动（含 API、官方 Web 管理界面、PgAdmin）、cookiecutter 项目模板、CLI 导入文档与导入/导出集合、基于 Bearer Token 的 API 访问控制，以及 LangSmith 监控接入。需 Python 3.10+、Poetry 与 PostgreSQL 14+。

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

- 提供完整 RAG API 与可自定义的信息抽取 API
- 以 PostgreSQL+pgvector 为向量数据库，Docker Compose 一键启动全栈
- 可配置 LangChain 支持的任意 LLM，含 Ollama 本地模型集成示例
- CLI 支持文档导入与集合导入/导出，内置访问令牌鉴权

## 适用场景

- 快速搭建基于自有文档的 RAG 问答服务
- 对文档执行摘要等信息抽取并接入异步后台任务
- 通过 Web 管理界面创建知识库集合并用对话测试

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: Brevia is an extensible API and framework for building Retrieval Augmented Generation (RAG) and Information Extract
> L19: * The popular LangChain framework, which you can use to create custom AI tools and logic

## 星数曲线

```mermaid
xychart-beta
    title "brevia-ai/brevia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `2c805dfdeb22` · [字段定义](../../DATASET.md)*
