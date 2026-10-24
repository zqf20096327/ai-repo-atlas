# vitalops/datatune

⭐ 152 · Python · MIT · 推送 2026-07-25 · [GitHub](https://github.com/vitalops/datatune) · [官网](https://github.com/vitalops/datatune) · 组织维护

**让 LLM/Agent 对超大规模数据做行级语义变换的 Python 库**

Datatune 是一个 Python 数据变换库，面向需要用 LLM 对大量数据逐行应用语义操作的开发者与科研用户。它基于 Dask 与 Ibis（支持 DuckDB、PostgreSQL、BigQuery 等数据源），提供 Map、Filter 等行级原语，使 LLM 访问不受上下文窗口限制的数据量；并提供 Agent 模式，由 LLM 自动选择、链式组合变换步骤，必要时生成并执行 Python 代码。支持 OpenAI 等多种 LLM，通过 pip 安装。框架与评估见其同行评审论文（DATA 2026）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Dask/Ibis 支持超上下文窗口规模的数据变换
- 行级语义原语（Map、Filter 等）由 LLM 逐行应用
- Agent 模式自动编排多步变换并生成执行 Python 代码
- 支持 OpenAI 等多种 LLM 与多种数据后端

## 适用场景

- 对大规模表格数据做需要语义理解的逐行清洗与变换
- 让 Agent 从单条自然语言提示自动编排数据变换流程
- 在 DuckDB/PostgreSQL/BigQuery 等数据源上执行 LLM 驱动的处理

## 场景标签

 · 领域:数据工程/LLM 应用

## 证据(README 行号)

> L9: Scalable Data Transformations with row-level intelligence.
> L11: Datatune is not just another Text to SQL tool. With datatune, LLMs and Agents can have full access to infinite amou

## 星数曲线

```mermaid
xychart-beta
    title "vitalops/datatune 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 150 --> 153
    line [151, 152, 152]
```

2026-10-18 151 → 2026-10-24 152（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8434976f035f` · [字段定义](../../DATASET.md)*
