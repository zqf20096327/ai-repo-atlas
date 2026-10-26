# WenChentao/3DeeCellTracker

⭐ 70 · Python · MIT · 推送 2025-11-13 · [GitHub](https://github.com/WenChentao/3DeeCellTracker) · 个人维护

**深度学习管道：追踪3D变形器官/运动动物中的细胞**

基于深度学习的细胞分割与追踪流程，处理3D时间序列显微图像，支持变形器官（Single 模式）与自由运动动物（Ensemble 模式）。分割可选 3D StarDist（官方优化推荐）或 3D U-Net，可选训练 FFN 用于匹配；以 Jupyter notebook 形式提供训练与追踪示例，模型与演示数据可下载。要求 NVIDIA GPU（CUDA）+ Anaconda + TensorFlow 2.x，经 pip 从 PyPI 安装，也可在 Google Colab 运行。v1.0.0 的 notebook 需使用指定版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D+T 图像中变形器官与运动动物的细胞分割与追踪
- StarDist 与 3D U-Net 两种分割网络，支持自定义数据训练
- Single 与 Ensemble 两种追踪模式，FFN 匹配可选训练
- 提供 notebook 示例、演示数据与视频教程

## 适用场景

- 追踪线虫、斑马鱼心脏等活体样本中的细胞
- 在新光学条件下训练自定义分割网络
- 3D 肿瘤球体等体外样本的细胞追踪

## 场景标签

 · 领域:生物医学图像分析

## 证据(README 行号)

> L5: Youtube
> L47: To learn how to track cells using 3DeeCellTracker, please refer to the following notebooks for examples. We recomme
> L98: We designed this pipeline for segmenting and tracking cells in 3D + T images in deforming organs. The methods have 

## 星数曲线

```mermaid
xychart-beta
    title "WenChentao/3DeeCellTracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-26 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bba68922f10c` · [字段定义](../../DATASET.md)*
