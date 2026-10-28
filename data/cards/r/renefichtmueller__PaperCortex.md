# renefichtmueller/PaperCortex

⭐ 31 · TypeScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/renefichtmueller/PaperCortex) · 个人维护

**给 Paperless-ngx 文档库加本地 AI：语义搜索、收据提取与 DATEV 导出**

面向使用 Paperless-ngx 管理票据、合同等扫描件的用户与德国自由职业者/企业：轮询 Paperless-ngx API，用本地 Ollama 模型生成向量嵌入存入 SQLite 向量库，提供跨语言语义搜索、LLM 自动分类打标、收据结构化数据提取、银行流水模糊匹配，以及生成可导入 DATEV 的 EXTF 文件或 CSV 的导出功能。全部能力以 MCP Server（五个工具）暴露给 Claude Code 等 agent，附带德英双语 Web 设置界面。运行需 Docker、Paperless-ngx 实例与 Ollama，文档内容不出本机网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于本地 Ollama 嵌入模型（nomic-embed-text 等）的跨语言语义搜索，SQLite 向量库存储
- 收据提取（供应商/金额/税率/明细）+ 银行 CSV 交易模糊匹配与置信度评分
- 生成 DATEV EXTF 格式文件（SKR03/SKR04 映射、按财年拆分），异常收据跳过并报告原因
- 以 MCP Server 形式暴露五个工具，兼容 Claude Code 等 MCP agent

## 适用场景

- 在票据档案中按含义而非关键词跨语言查找文档
- 自动给新到文档分类打标，无需手工规则
- 把收据数据一键导出为 DATEV/CSV 交给税务顾问或会计软件
- 让 Claude Code 等 AI agent 通过 MCP 直接查询我的文档库

## 场景标签

`语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L29: - **Extract structured data from receipts** — vendor, date, amount, tax rate, line items
> L150: PaperCortex translates natural language into document queries, retrieves relevant documents via semantic search, a
> L197: 6. **Query interface** — the MCP Server exposes search, classify, extract, query, and export tools

## 星数曲线

```mermaid
xychart-beta
    title "renefichtmueller/PaperCortex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `25ee3e0765c2` · [字段定义](../../DATASET.md)*
