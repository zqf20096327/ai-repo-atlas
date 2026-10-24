# AntonotnaWang/NaviAirway

⭐ 68 · Jupyter Notebook · MIT · 推送 2026-08-12 · [GitHub](https://github.com/AntonotnaWang/NaviAirway) · 个人维护

**胸部 CT 气管树分割管线：细支气管敏感损失与迭代训练**

面向医学图像分析研究者的深度学习气管分割流水线，基于 PyTorch。核心机制包括细支气管敏感损失函数与受人眼视觉启发的迭代训练策略（通过生成 dataset info 的 pkl 文件实现低代与高代气道的交替训练），可与不同 backbone 模型组合。支持 EXACT09 与 LIDC-IDRI 两个公开数据集，流程为 Jupyter Notebook 预处理、裁剪、训练脚本与推理 notebook。另提出 Branch Detected 与 Tree-length Detected 两个评估指标，可生成用于导航支气管镜的气道路线图。

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

- 细支气管敏感损失函数与迭代训练策略
- 可与不同 backbone 模型组合
- 提出 Branch Detected / Tree-length Detected 两个新评估指标
- 支持 EXACT09 与 LIDC-IDRI 数据集的完整预处理-训练-推理流程

## 适用场景

- 对胸部 CT 做气管树分割并检测更细的细支气管
- 生成导航支气管镜用的气道路线图
- 分割生物医学图像中细长管状结构
- 复现论文方法或在新 CT 数据上训练模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: > **NaviAirway: a Bronchiole-sensitive Deep Learning-based Airway Segmentation Pipeline**, ***Preliminary version pr
> L5: Airway segmentation is essential for chest CT image analysis. However, it remains a challenging task because of the 

## 星数曲线

```mermaid
xychart-beta
    title "AntonotnaWang/NaviAirway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-24 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8c7a6c166fd5` · [字段定义](../../DATASET.md)*
