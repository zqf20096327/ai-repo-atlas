# allannuwamanya/open-data-uganda

⭐ 14 · JavaScript · NOASSERTION · 推送 2026-09-13 · [GitHub](https://github.com/allannuwamanya/open-data-uganda) · [官网](https://opendata-ug.pages.dev) · 组织维护

**乌干达公开数据集中心：14 个领域 15,806 条机器可读数据**

乌干达数据集的开放访问中心仓库：从 UBOS、世界银行、WHO、UNESCO 等经验证的政府与机构来源采集数据，清洗后以 .csv 和 .jsonl 机器可读格式按领域（人口、地理、经济、卫生、教育、本地语言等）组织分发。提供 Python/R/cURL 直接从 GitHub raw URL 加载数据的示例、数据校验与生成脚本（validate_datasets.py、generate_datasets.py、fetch_worldbank_indicators.py），并附引用元数据（CITATION.cff），整体以 CC BY 4.0 许可。语言数据集标注可用于 NLP/翻译/NER 任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个数据集、约 15,806 条记录，覆盖 12 个领域
- 数据来源为 UBOS/UN OCHA/WFP/世界银行/WHO/UNESCO 等机构并经验证清洗
- 提供自动化校验、构建流水线与世界银行指标抓取脚本
- 数据集按 ML 任务类型标注用途（NLP/回归/聚类等）

## 适用场景

- 为乌干达低资源语言的 NLP 或 TTS 模型训练查找语言数据
- 加载乌干达人口、卫生、经济等公开数据做分析
- 通过脚本复现数据校验与构建流程

## 场景标签

 · 领域:开放数据/数据集

## 证据(README 行号)

> L9: Welcome to **Open Data Uganda**! This project serves as a central, reliable, and standardized open-access hub for Ug
> L11: All datasets are curated from verified government, multilateral, and research organizations (UBOS, UN OCHA, WFP, Wo
> L61: |Domain|Datasets|Total Records|ML-Ready|

## 星数曲线

```mermaid
xychart-beta
    title "allannuwamanya/open-data-uganda 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `29df3bf9b1da` · [字段定义](../../DATASET.md)*
