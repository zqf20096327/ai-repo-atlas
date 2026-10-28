# marco-hoffmann/HANNA

⭐ 20 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/marco-hoffmann/HANNA) · 组织维护

**预测多元混合物相平衡（VLE/LLE）的机器学习过量吉布斯能模型**

HANNA 是一个基于机器学习的过量吉布斯能（excess Gibbs energy）预测模型：输入各分子的 SMILES 表示与状态点（组成和温度），通过自动微分导出热力学一致的活动系数，预测汽液平衡（VLE）、液液平衡（LLE）等相平衡性质。模型在超过 80 万个二元混合物实验数据点上训练，支持任意组分数的混合物。面向化学工程与过程设计场景的用户，安装方式为克隆仓库并用 conda 环境配置（可选 CUDA 版 PyTorch），通过 demo.ipynb 测试，另提供无需安装的网页界面 MLPROP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入 SMILES 与状态点即可预测过量吉布斯能与活动系数
- 在超过 80 万个实验数据点（VLE/LLE/无限稀释活动系数/过量焓）上训练
- 通过自动微分保证热力学一致性，支持任意组分数混合物
- 提供无需安装的网页界面 MLPROP

## 适用场景

- 化工过程设计中预测多组分混合物的汽液/液液相平衡
- 由分子 SMILES 快速估算活动系数
- 不安装环境时通过网页界面试用模型

## 场景标签

 · 领域:化学工程/分子性质预测

## 证据(README 行号)

> L8: HANNA is a machine learning model for predicting the excess Gibbs energy of the liquid phase in mixtures with an arb

## 星数曲线

```mermaid
xychart-beta
    title "marco-hoffmann/HANNA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1888a00f1b2c` · [字段定义](../../DATASET.md)*
