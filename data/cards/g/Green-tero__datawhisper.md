# Green-tero/datawhisper

⭐ 6 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Green-tero/datawhisper) · 个人维护

**本地优先的数据问答与 SQL PR 审计工具：自然语言查数据并审变更**

以 CLI 和 GitHub Action 形式运行的本地表格数据分析引擎：用户对数据集提问，工具做意图分类与 schema 剪枝后生成 SQL，经语义防火墙、AST 沙箱与 EXPLAIN 成本闸执行，并自动修复自身错误、在输出前清洗 PII；另可对触及 SQL/迁移/数据文件的 PR 报告 schema 漂移、PII 列、执行计划回退与迁移静态审计。无需 LLM API key 也可用本地模板合成只读 SQL 离线运行；当前版本 1.4.3，从仓库安装，未发布到 PyPI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流水线：意图剪枝→SQL 生成→三重护栏执行→结果清洗合成
- 语义防火墙+AST 沙箱+EXPLAIN 成本闸三重语句防护
- 支持 SQLite/DuckDB/PostgreSQL/Parquet/JSONL 数据源，全部只读打开
- 离线模式 DW_LLM_PROVIDER=local 无需网络与 API key

## 适用场景

- 用自然语言向本地数据库提问并获得清洗后的结果
- 在 CI 中对触及数据文件的 PR 做 schema 漂移与 PII 审计
- 在无网络环境用模板合成 SQL 分析本地数据集

## 场景标签

`数据分析` `代码审查` · 领域:效率与自动化

## 证据(README 行号)

> L3: DataWhisper answers questions about your data and reviews database changes in pull requests.
> L22: **1. A local analysis tool.** Ask a question about a dataset. DataWhisper classifies intent and prunes a large sche
> L24: **2. A pull-request reviewer.** On a PR that touches SQL, migrations or data files, the bot reports column-level sc

## 星数曲线

```mermaid
xychart-beta
    title "Green-tero/datawhisper 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-11-08", "2026-11-25"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-23 5 → 2026-11-25 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `b90eaf3b1046` · [字段定义](../../DATASET.md)*
