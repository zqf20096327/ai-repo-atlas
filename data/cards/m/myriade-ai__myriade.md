# myriade-ai/myriade

⭐ 62 · Shell · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/myriade-ai/myriade) · [官网](https://www.myriade.ai) · 组织维护

**面向企业数据仓库的 AI 分析师：自然语言查询与数据治理**

连接既有数据仓库（含 dbt 集成），从 schema、元数据、关系与查询历史构建上下文层，不要求预先具备语义层或完整文档。提供自然语言分析能力：生成并解释 SQL、文档化表/列/指标、检测数据质量与异常，并将回答锚定在源表、血缘与校验上，供数据团队审查和控制 AI 生成的分析。安装方式为一键安装脚本，要求 Ubuntu 20.04+/Debian 11+，通过浏览器访问服务端 8080 端口，另提供 SSL 安装脚本与安装指南（含 Docker 快速开始）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从仓库与现有数据栈（含 dbt）构建上下文层，无需语义层前置
- 生成并解释 SQL，自动文档化表、列与指标
- 数据质量与异常检测
- 回答基于源表、血缘与校验锚定，支持团队审查 AI 分析

## 适用场景

- 用自然语言对数据仓库做分析并审查生成的 SQL
- 为文档不全、指标不一致的数仓补建上下文与文档
- 检测数据质量问题与异常
- 数据团队对 AI 生成的分析进行治理与控制

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Myriade connects to an existing data warehouse, builds the missing context layer, and provides a reliable AI analy
> L13: - generates and explains SQL
> L16: - grounds answers in source tables, lineage, and checks

## 星数曲线

```mermaid
xychart-beta
    title "myriade-ai/myriade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ebabb461650e` · [字段定义](../../DATASET.md)*
