# ccao-data/model-res-avm

⭐ 74 · R · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/ccao-data/model-res-avm) · 组织维护

**库克县住宅房产批量评估模型：用 ML 生成估定价值**

Cook County 评估官办公室的住宅再评估模型（AVM）仓库：基于历史销售数据训练 LightGBM（Tidymodels 框架，自研 Lightsnip 扩展包集成），对全县独栋与多户住宅（不含空地与公寓）估计公允市场价值。流水线含 7 个阶段（摄取/训练/评估/评价/解释/定稿/上传导出），各阶段为独立 R 脚本，可用 DVC 串联。输出含 SHAP 解释、PIN 级报告与评估员专用指标（COD/PRD/PRB/MKI）。数据来自 CCAO Athena 数据库，输入输出存 AWS S3；上传与导出阶段需内部权限。提供 Docker 方式本地运行，AWS Batch 运行仅限 CCAO 员工。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LightGBM 梯度提升模型估计全县住宅销售价格
- 7 阶段 R 流水线，脚本可独立运行或经 DVC 串联
- SHAP 值、特征重要性与 PIN 级解释报告
- 自研 Lightsnip 包集成 LightGBM 与 Tidymodels（早停、类别特征超参）

## 适用场景

- 地方政府批量评估辖区内住宅的估定价值
- 复现库克县评估流程并审查建模决策
- 参考房产税评估 ML 管线的评价指标体系

## 场景标签

 · 领域:政府/房地产评估

## 证据(README 行号)

> L52: The repository itself contains the code for the Automated
> L56: referred to as “the model”). It uses previous sales to generate
> L104: 2. **Assess**: Use the trained model to estimate values for all

## 星数曲线

```mermaid
xychart-beta
    title "ccao-data/model-res-avm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 72 --> 75
    line [73, 74, 74]
```

2026-10-18 73 → 2026-10-28 74（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a5681ac4dc5b` · [字段定义](../../DATASET.md)*
