# tanjimin/CANVAS

⭐ 16 · Python · 推送 2026-07-17 · [GitHub](https://github.com/tanjimin/CANVAS) · [官网](https://www.nature.com/articles/s41551-025-01348-1) · 组织维护

**多重成像肿瘤异质性分析：无分割表征学习流水线**

论文官方代码库（Nat. Biomed. Eng. 2025）：在多重成像数据（IMC/tiff 等）上做无分割的表征学习，用于刻画肿瘤异质性。四步流水线：预处理转 zarr 格式、训练模型、特征提取（含 UMAP 与 KMeans 聚类）、下游分析。面向计算生物学/癌症影像研究人员，需在带 GPU 的本地机器上训练与推理，另提供 Google Colab 调试演示（受运行时长与存储限制）。示例数据集托管于 zenodo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四步流水线：预处理→训练→特征提取→下游分析
- 将 IMC/tiff 等原始图像转为 zarr 格式并按通道组织
- 特征提取附带 UMAP 与 KMeans 初始聚类
- 无分割（segmentation-free）表征学习方法

## 适用场景

- 对多重免疫荧光/IMC 肿瘤图像做无分割表征学习
- 提取细胞级特征后做聚类与下游异质性分析
- 复现论文方法或在新数据集上训练 CANVAS 模型

## 场景标签

 · 领域:计算生物学/癌症影像分析

## 证据(README 行号)

> L5: Official repository for Characterization of tumor heterogeneity through segmentation-free representation learning on
> L14: 2. Train CANVAS: this step trains the CANVAS model with the zarr data and save the trained model.
> L15: 3. Extract features with trained model: this step extracts features from the trained model and save the features.

## 星数曲线

```mermaid
xychart-beta
    title "tanjimin/CANVAS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e9f91b0a96bf` · [字段定义](../../DATASET.md)*
