# Saumya-Gupta-26/struct-uncertainty

⭐ 55 · C++ · 推送 2026-05-05 · [GitHub](https://github.com/Saumya-Gupta-26/struct-uncertainty) · 个人维护

**NeurIPS 2023 论文官方代码：图像分割的拓扑感知不确定性量化**

论文《Topology-Aware Uncertainty for Image Segmentation》（NeurIPS 2023）的官方实现：基于离散莫尔斯理论（DMT）从分割结果生成 Morse Skeleton 及临界点与流形，用于曲线结构分割的拓扑感知不确定性量化。提供训练与推理脚本（train.py/infer.py），示例基于 DRIVE 视网膜血管数据集，当前代码仅支持 2D 图像，需替换数据集配置后使用。附带 jupyter notebook 演示与可视化，另有官方 3D 版本与 3D Slicer 插件两个相关仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于离散莫尔斯理论生成 Morse Skeleton 与临界点/流形
- 提供 train.py / infer.py 训练与推理脚本
- 附带 DMT 用法演示 notebook 与可视化

## 适用场景

- 复现论文的拓扑感知不确定性量化方法
- 在自己的 2D 曲线结构分割数据集上计算结构级不确定性
- 基于 DMT 骨架开展分割质量分析研究

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2: This repository contains the implementation for our work "Topology-Aware Uncertainty for Image Segmentation", accept
> L4: The `dmt-uncertainty.ipynb` file contains simple code on how to use discrete Morse theory (DMT) to generate the Mors

## 星数曲线

```mermaid
xychart-beta
    title "Saumya-Gupta-26/struct-uncertainty 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-31 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b1b2ff8005a6` · [字段定义](../../DATASET.md)*
