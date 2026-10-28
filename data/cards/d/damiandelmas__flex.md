# damiandelmas/flex

⭐ 19 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/damiandelmas/flex) · [官网](https://getflex.dev) · 个人维护

**面向 AI agent 的本地检索工具：把会话/仓库编译成可查询的 SQLite 知识单元**

flex 将 Claude Code/Codex 会话历史、文件夹、GitHub/Reddit/HN/arXiv 等来源编译为自描述的 SQLite「cell」，agent 通过单一 MCP 工具用 SQL、关键词和语义三种方式查询，并可回溯到源证据。默认本地运行，无需托管服务；嵌入采用本地 Nomic v1.5 模型，无需 API key。原生安装器支持 macOS/Linux（需 Bash、Python 3.12+、git、curl、file），Windows 仅有实验性 Docker 容器发行版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多来源（会话/文件系统/GitHub/Reddit/HN/arXiv）统一编译为 SQLite cell，单一 MCP 工具查询
- SQL 预过滤→关键词/语义评分→SQL 组合的三段式检索，过滤先于打分
- 本地 Nomic v1.5 嵌入模型，无需 embedding API key
- flexvec 向量算子（similar/suppress/diverse/decay 等）可在选行前调整语义检索

## 适用场景

- 把编码 agent 的历史会话变成可查询数据库，追溯文件改动与决策依据
- 把 Obsidian 库或混合代码文件夹编译为一个可结构化+语义检索的单元
- agent 通过 MCP 工具检索本地知识库并回溯到原始证据

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: flex compiles coding-agent sessions, folders, repositories, and supported data
> L18: source can support. flex runs locally by default; a hosted retrieval service is not
> L306: flex has one shape and a small set of conventions. Every source compiles into the

## 星数曲线

```mermaid
xychart-beta
    title "damiandelmas/flex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6e7d41762ebd` · [字段定义](../../DATASET.md)*
