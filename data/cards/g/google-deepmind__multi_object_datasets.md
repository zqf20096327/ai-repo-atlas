# google-deepmind/multi_object_datasets

⭐ 290 · Python · Apache-2.0 · 推送 2026-03-03 · [GitHub](https://github.com/google-deepmind/multi_object_datasets) · 组织维护

**多物体场景表示学习数据集：带真值分割掩码与生成因子**

DeepMind 发布的多物体表示学习数据集合集，含 Multi-dSprites、Objects Room、CLEVR（带掩码）、Tetrominoes、CATER（带掩码）五个数据集，每张图像或视频均附带所有物体的真值分割掩码；部分数据集（Objects Room 与 CATER 除外）还提供逐物体生成因子（位置、颜色、形状、尺度等）。附带的 segmentation_metrics 模块提供 adjusted Rand index 的 TensorFlow 实现，用于比较推断分割与真值掩码；代码在 TensorFlow r1.14 下测试。数据以 TFRecords 形式从 Google Cloud Storage 下载，总下载量从 300 MB 到 10.5 GB 不等。限科研用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个多物体数据集，均带真值分割掩码
- 部分数据集提供逐物体生成因子（位置/颜色/形状/尺度等）
- 提供 adjusted Rand index 的 TensorFlow 实现用于分割评估
- 数据以 TFRecords 提供，附 tf.data.Dataset 读取器

## 适用场景

- 训练与评测多物体场景分解方法（如 MONet、IODINE、SIMONe）
- 评估无监督物体分割结果与真值掩码的差异
- 研究生成因子驱动的表示学习

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains datasets for multi-object representation learning, used
> L17: The datasets consist of multi-object scenes. Each image or video is accompanied by

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/multi_object_datasets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 289 --> 291
    line [290, 290]
```

2026-10-18 290 → 2026-10-25 290（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `22018f9e5443` · [字段定义](../../DATASET.md)*
