# xifanz42/nl2sql_agent

⭐ 16 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/xifanz42/nl2sql_agent) · 个人维护 · 中文 README

**自然语言查询 PostgreSQL 的轻量智能体，输出 SQL 并执行分析**

面向需要频繁查库但不熟悉 SQL 的用户：基于 SiliconFlow 驱动的 LLM，通过多轮对话将自然语言转为 SQL 查询语句，连接 PostgreSQL 执行查询并做数据分析，返回自然语言结果；核心代码文件中附有 TensorFlow 驱动 LLM 的样本代码。支持 CSV/TXT/Markdown 文档上传解析，用 Faiss 做语义检索与向量召回。提供交互式命令行界面，经 pip 安装依赖、配置 .env 数据库参数后以 Streamlit 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轮对话完善查询目标并生成 SQL、执行查询
- 基于 SiliconFlow 驱动 LLM，附 TensorFlow 驱动样本代码
- Faiss 实现语义搜索与向量召回
- 支持 CSV/TXT/Markdown 文档上传、存储与解析

## 适用场景

- 不写 SQL 直接用自然语言查询 PostgreSQL 数据
- 多轮对话逐步明确查询意图
- 上传业务文档辅助查询与数据分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: `NL2SQL_AGENT`是一个轻量级的自然语言到 SQL (NL2SQL) 智能体，旨在帮助用户通过自然语言查询 PostgreSQL 数据库。该智能体结合了文档处理、向量检索、LLM 和数据库交互，为用户提供高效、便捷的数据库
> L15: 1. **自然语言到 SQL 的转换**：用户可以通过自然语言描述来查询数据库，工具会自动生成相应的 SQL 查询语句。

## 星数曲线

```mermaid
xychart-beta
    title "xifanz42/nl2sql_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `032f8e5c7eca` · [字段定义](../../DATASET.md)*
