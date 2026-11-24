# NVIDIA/auto-ontology

⭐ 14,666 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/NVIDIA/auto-ontology) · 组织维护

**为 LLM/agent 工作流自动构建企业本体语义层的 Python 框架**

NVIDIA 开源的 Python 框架，从企业元数据自动生成本体（概念、映射、关系、指标、血缘、认证六要素），供 agent 通过 MCP、CLI、API 检索业务上下文并生成可核验的 text-to-SQL 答案。流程分两阶段：先从数据库摄取并语义编译生成本体草稿，再由推理模型以 retrieve/run_sql/submit 工具循环回答问题，每个答案附 SQL 与步骤，并先检查可答性。技术栈为 Next.js 前端、FastAPI+LangChain 后端、Postgres+pgvector，通过 Docker Compose 部署，需 NVIDIA API key。README 称在 BEAVER 与 BIRD-Interact 基准上排名第一。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从企业元数据自动生成本体，含概念、映射、关系、指标、血缘与认证六类元素
- 通过 MCP、CLI、API 向任意 agent harness 暴露语义上下文
- 答案附 SQL 与推导步骤，回答前检查可答性并请求澄清
- 兼容 Apache Ossie 语义模型交换标准，支持 YAML 导入导出

## 适用场景

- 为 text-to-SQL 分析 agent 提供受治理的业务语义层
- 跨多个定义冲突的数据源统一指标口径
- 专家认证前用真实问题测试自动生成的本体草稿

## 场景标签

`数据分析` `知识图谱` · 领域:效率与自动化

## 证据(README 行号)

> L6: Agents can retrieve documents and query databases, but reliability gates agentic analytics: a revenue metric answere
> L15: - **Expose:** serve context to any agent harness through MCP, CLI, and API.
> L213: |Backend|FastAPI (Python 3.12+), LangChain|Text-to-SQL agent, catalog, ontology APIs|3001|

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/auto-ontology 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 0 --> 15769
    line [35, 43, 57, 63, 102, 120, 178, 306, 508, 595, 653, 673, 691, 102, 10212, 11798, 12204, 12523, 12799, 13002, 13310, 13620, 13795, 13949, 14050, 14169, 14339, 14339]
```

2026-10-21 35 → 2026-11-24 14,339（+14,304）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `0f286505ed29` · [字段定义](../../DATASET.md)*
