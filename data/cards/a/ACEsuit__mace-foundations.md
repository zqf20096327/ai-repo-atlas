# ACEsuit/mace-foundations

⭐ 316 · Shell · MIT · 推送 2026-08-26 · [GitHub](https://github.com/ACEsuit/mace-foundations) · [官网](https://mace-docs.readthedocs.io/en/latest/guide/foundation_models.html) · 组织维护

**材料化学预训练机器学习势模型集合：覆盖 89 种元素**

发布 MACE 系列原子间机器学习势基础模型（MACE-MP、MACE-MPA、MACE-OMAT、MACE-MATPES、MACE-OMOL、MACE-MH 等），参数化覆盖 89 种化学元素，训练数据来自 MPTrj、OMAT、MATPES、OMol25 等 DFT 数据集，面向材料、分子与表面体系的分子动力学模拟。使用需另行安装 MACE 代码，模型另在 Hugging Face 提供；仓库同时附训练脚本、MPtrj 训练数据与论文补充材料。各模型分别标注 MIT 或 ASL 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多个系列基础模型，覆盖 89 种化学元素
- 提供训练脚本与 MPtrj 训练数据
- 模型同步发布于 Hugging Face
- 注明各模型许可（MIT/ASL）与所需 MACE 版本

## 适用场景

- 材料与分子体系的机器学习势分子动力学模拟
- 在自有数据上对基础模型做微调
- 复现论文结果与查看示例轨迹

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains the MACE pre-trained foundation models for materials chemistry, parameterised for 89 chemic
> L13: |Model Name|Elements Covered|Training Dataset|Level of Theory|Target System|Model Size|GitHub Release|Notes|License
> L30: This release includes models with improved stability during MD simulations, using core repulsion, a new repulsion r

## 星数曲线

```mermaid
xychart-beta
    title "ACEsuit/mace-foundations 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 314 --> 317
    line [315, 316, 316]
```

2026-10-18 315 → 2026-10-23 316（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2672c74c3d8e` · [字段定义](../../DATASET.md)*
