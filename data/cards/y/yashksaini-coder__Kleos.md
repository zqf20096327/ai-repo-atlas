# yashksaini-coder/Kleos

⭐ 20 · Python · 推送 2025-12-19 · [GitHub](https://github.com/yashksaini-coder/Kleos) · [官网](https://dev.to/yashksaini/kleos-cli-mindsdb-knowledge-base-supercharged-1a83) · 个人维护

**操作 MindsDB 知识库与 AI Agent 的命令行工具**

面向 MindsDB 的交互式 CLI（kleos），聚焦知识库功能与 AI Agent 集成：创建、索引、查询知识库，摄取数据，创建并查询关联知识库的 AI Agent，管理 MindsDB Jobs、数据源与 AI 模型/表。附带性能基准、压力测试与 reranking 评测脚本。提供 Docker Compose 一键启动本地 MindsDB 与 Ollama 实例，另含 Dockerfile 容器化 CLI 本身。需要 Python 3.8+ 与运行中的 MindsDB 实例；使用 Ollama 模型需本地或 Docker 实例及 nomic-embed-text、llama3 等模型，Gemini 功能需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库创建/索引/摄取/查询与 AI Agent 关联命令
- MindsDB Jobs、数据源与 AI 模型/表管理
- docker-compose.yml 一键启动本地 MindsDB 与 Ollama
- 性能基准、压力测试与 reranking 评测脚本套件

## 适用场景

- 用命令行批量创建和查询 MindsDB 知识库
- 搭建并连接本地 MindsDB+Ollama 的知识库工作流
- 对 MindsDB 知识库 reranking 做基准与压测

## 场景标签

 · 领域:LLM 基础设施/知识库工具

## 证据(README 行号)

> L7: **Kleos** provides a powerful and interactive, Command Line Interface (CLI) for interacting with MindsDB, with a spe
> L24:  * Create, index, and query Knowledge Bases (e.g., `kleos kb create ...`, `kleos kb query ...`).
> L26:  * Create and query AI Agents linked to KBs (e.g., `kleos kb create-agent ...`).

## 星数曲线

```mermaid
xychart-beta
    title "yashksaini-coder/Kleos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `94d147709bbd` · [字段定义](../../DATASET.md)*
