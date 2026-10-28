# chembl/chembl_multitask_model

⭐ 22 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/chembl/chembl_multitask_model) · 组织维护

**基于 ChEMBL 训练的多靶点预测神经网络模型**

在 ChEMBL 生物活性数据上训练的小型多靶点预测神经网络，用于化合物 panel 靶点预测与脱靶预测场景。模型导出为 ONNX 格式，凡能用 RDKit 生成分子指纹的语言均可加载推理；README 提供 Python、Julia 示例及 C++ REST 微服务链接，并通过 RDKit Javascript MinimalLib 与 ONNX.js 提供在线试用页面。附带数据提取与训练脚本，数据筛选按活性类型、靶点类型与 IDG 蛋白家族活性阈值过滤，多测量值取最低浓度（偏向敏感性）。

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

- ChEMBL 数据训练的多靶点神经网络，支持脱靶预测
- 模型导出 ONNX，可跨 Python/Julia/C++/JS 使用
- 提供数据提取与训练脚本，可训练激酶家族专属模型
- 提供基于 RDKit JS 与 ONNX.js 的在线试用页面

## 适用场景

- 对大批量化合物做靶点预测筛选
- 评估候选分子的潜在脱靶活性
- 用自有 ChEMBL 版本重建或训练家族专属预测模型

## 场景标签

 · 领域:化学信息学/药物发现

## 证据(README 行号)

> L3: Small and fast target prediction model trained on a panel of targets using ChEMBL data. The model can be used in off
> L8: The model is exported to the ONNX format so it can be used in any programming language able to generate fingerprints

## 星数曲线

```mermaid
xychart-beta
    title "chembl/chembl_multitask_model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `87239abc3f5a` · [字段定义](../../DATASET.md)*
