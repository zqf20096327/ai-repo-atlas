# innat/medic-ai

⭐ 29 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/innat/medic-ai) · [官网](https://medicai.readthedocs.io/) · 个人维护

**Keras 3 医学 2D/3D 影像分析工具库：分类、分割与预处理**

基于 Keras 的医学图像分析库，兼容 tensorflow、torch、jax 三种后端。提供 75+ 分类模型、11+ 分割模型（UNet 系列、SwinUNETR、SegFormer 等）与 20+ 2D/3D 预处理增强变换，支持单/多 GPU 与 TPU-VM 训练推理、GradCAM、滑动窗口 3D 推理。变换以 keras.ops 实现，支持批量、图像-标签同步处理与 CPU/GPU 执行。面向医学影像研究者与开发者，项目受 MONAI 与 NiftyNet 启发，要求自选安装后端运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后端无关：兼容 tensorflow/torch/jax
- 75+ 分类与 11+ 分割模型，覆盖 2D/3D 输入
- 20+ 预处理增强变换，支持批量与图像-标签同步
- 支持单/多 GPU 与 TPU-VM 训练推理，含滑动窗口 3D 推理

## 适用场景

- 医学影像 2D/3D 分类与分割模型训练
- 构建后端无关的医学影像预处理增强管线
- 大体积 3D 医学数据的 GradCAM 可视化与滑动窗口推理

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: **Medic-AI** is a Keras based library designed for medical 2D and 3D image analysis using machine learning technique
> L10: - **User-Friendly API:** High-level interface for `75+` classification models, `11+` segmentation models, and `20+`

## 星数曲线

```mermaid
xychart-beta
    title "innat/medic-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f560925303ef` · [字段定义](../../DATASET.md)*
