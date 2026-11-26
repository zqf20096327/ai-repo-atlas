# GetCassis/ontology-skills

⭐ 32 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/GetCassis/ontology-skills) · [官网](https://blog.getcassis.com/a-blank-beats-a-guess/) · 组织维护

**为分析 agent 构建和扩展数据仓库本体（ontology）的技能包**

提供 ontology-bootstrap 与 ontology-expansion 两个技能，供编码 agent 从 schema 导出、dbt 项目、文档、看板导出和语义层（Power BI/MetricFlow/Cube/LookML）中构建分析本体。核心机制是证据约束：优先采用用户自有文本，无法举证的列留空并归档问题，每个声明标注来源，并由判定 pass 复核。运行在四个检查点暂停，由用户做业务判断；以可审查的 Git 文件树输出。支持 npx 安装技能或克隆仓库以纯 Python 脚本手动运行，需自备编码 agent 与模型。

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

- 从 schema/dbt/文档/看板/语义层读取证据构建本体，产出可审查的文件树
- 无证据支持的列留空并归档问题，每条声明携带来源，含判定 pass 复核
- 四个检查点暂停，业务判断留给用户；可增量扩展（每次 20-30 表）
- 确定性阶段为免费脚本，LLM 仅用于证据支撑的起草阶段

## 适用场景

- 为 text-to-SQL / 分析 agent 建立带证据的数据仓库语义层
- 审计现有 dbt 项目中文档与 SQL 的矛盾
- 为已有本体按增量扩展新数据域

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Skills for building and expanding the context an analytics agent needs. Both start from
> L6: - **ontology-bootstrap** builds a first ontology from what your stack already has.
> L8: - **ontology-expansion** grows one you already maintain.

## 星数曲线

```mermaid
xychart-beta
    title "GetCassis/ontology-skills 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-26"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-11-08 31 → 2026-11-26 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `873ddae58263` · [字段定义](../../DATASET.md)*
