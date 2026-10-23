# langchain-ai/data-enrichment

⭐ 258 · Jupyter Notebook · MIT · 推送 2026-10-22 · [GitHub](https://github.com/langchain-ai/data-enrichment) · 组织维护

**LangGraph Studio 数据富化 agent 模板：web 研究生成结构化数据**

由 LangChain 团队提供的 LangGraph 模板，用于构建"数据富化 agent"：输入研究主题与用户自定义的 extraction_schema，agent 自动进行 web 搜索（默认 Tavily）、读取网页提取关键信息、按指定 schema 组织为结构化结果并校验完整性。默认模型为 anthropic/claude-3-5-sonnet-20240620，可切换 OpenAI 等兼容模型；通过 LangGraph Studio 运行，也可经 LangGraph API 交互并部署到 LangGraph Cloud。面向希望快速搭建此类 agent 的开发者，可在 graph.py、tools.py、prompts.py 中扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入主题 + 自定义 JSON schema，产出结构化研究结果
- 流程：web 搜索 → 网页读取提取 → 按 schema 组织 → 完整性校验
- 默认 Anthropic Claude 模型，支持 provider/model-name 方式切换
- 可在 LangGraph Studio 中热重载调试，支持 LangSmith 追踪

## 适用场景

- 从开放式 web 研究生成结构化数据填充数据库或表格
- 快速搭建可自定义 schema 与模型的数据富化 agent
- 作为 LangGraph 学习与二次开发的起点模板

## 场景标签

`Agent 框架` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L6: Producing structured results (e.g., to populate a database or spreadsheet) from open-ended research (e.g., web resea
> L12: The enrichment agent defined in `src/enrichment_agent/graph.py` performs the following steps:
> L17: 4. Organizes the findings into the requested structured format

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/data-enrichment 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 257 --> 259
    line [258, 258]
```

2026-10-18 258 → 2026-10-23 258（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f7fd47e3b166` · [字段定义](../../DATASET.md)*
