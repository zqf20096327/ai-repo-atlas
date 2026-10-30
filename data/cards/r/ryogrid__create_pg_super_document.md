# ryogrid/create_pg_super_document

⭐ 33 · C · NOASSERTION · 推送 2026-05-09 · [GitHub](https://github.com/ryogrid/create_pg_super_document) · [官网](https://ryogrid.github.io/create_pg_super_document/) · 个人维护

**用 AI agent 为 PostgreSQL 全部符号生成文档的工具与数据集**

面向 PostgreSQL 源码维护者与贡献者的文档生成流水线：先用 GNU GLOBAL (gtags) 构建符号定义与引用索引，导入 DuckDB 并做引用关系抽取、符号类型推断、去重等清洗，再按依赖聚类分批，由 orchestrator 调度 AI agent（如 Claude Code）经自研 MCP 工具接口获取符号上下文，生成 Markdown 文档并回写数据库。仓库同时附带已生成的多格式数据（Markdown/DuckDB/JSON/CSV）。README 声明文档由 LLM 生成、准确性不保证，需对照源码核验；依赖 Python 3 与 GNU GLOBAL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- gtags 索引→DuckDB→AI 文档生成的完整流水线脚本
- 自研 MCP 风格工具接口为 AI agent 提供符号定义、引用关系与聚类上下文
- 支持批次处理与进度记录（metadata.duckdb），中断可恢复
- 仓库附带针对指定 PostgreSQL commit 的已生成文档与多格式数据

## 适用场景

- 为 PostgreSQL 代码库批量生成符号级与组件级文档
- 查阅现成的 PostgreSQL 符号文档与引用关系数据
- 复用流水线为其他大型 C 代码树生成 AI 文档

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: **create_pg_super_document** is a project that generates documentation for all symbols in the PostgreSQL codebase, t
> L251: ## AI Documentation Generation

## 星数曲线

```mermaid
xychart-beta
    title "ryogrid/create_pg_super_document 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `db8476bab732` · [字段定义](../../DATASET.md)*
