# ccao-data/model-condo-avm

⭐ 15 · R · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/ccao-data/model-condo-avm) · 组织维护

**库克县公寓自动估价模型：为全部公寓生成初步评估值**

美国库克县评估官办公室的住宅公寓（class 299/399）重新评估模型仓库，包含代码、数据与文档。系统为机器学习模型（LightGBM，R/Tidyverse/Tidymodels 技术栈），利用历史销售记录为全县公寓生成估算销售价值作为初步评估值。针对公寓单元特征稀疏、不完整的限制，设计留一法、时间加权、楼栋级五年滚动平均售价特征作为预测变量，并辅以聚合地理、经济与销售时间特征。README 说明需先阅读其住宅（独栋/多户）模型仓库文档，本仓库与其基本相同仅列出差异。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LightGBM 全县范围模型，用历史销售生成公寓评估值
- 留一法、时间加权、楼栋级 5 年滚动平均售价特征
- 列出特征清单：单元/楼栋特征、ACS 人口经济特征、区位与环境特征
- 记录 2015-2025 各年度既往模型的方法与框架沿革

## 适用场景

- 政府评估机构批量生成公寓初步评估值
- 了解公寓批量估价的特征工程与数据限制
- 参考地方政府评估模型的透明化文档实践

## 场景标签

 · 领域:政府/房地产评估（数据科学）

## 证据(README 行号)

> L54: The repository itself contains the code for the Automated
> L57: advanced machine learning model (hereafter referred to as “the model”).
> L58: It uses previous sales to generate estimated sale values (assessments)

## 星数曲线

```mermaid
xychart-beta
    title "ccao-data/model-condo-avm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1c2f064dfaaa` · [字段定义](../../DATASET.md)*
