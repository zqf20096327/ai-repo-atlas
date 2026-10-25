# samhaswon/skin_segmentation

⭐ 53 · Python · GPL-3.0 · 推送 2026-09-21 · [GitHub](https://github.com/samhaswon/skin_segmentation) · 个人维护

**皮肤分割模型与方法的实验仓库：训练多模型供推理**

个人项目仓库，记录并实现多种皮肤（实为皮肤区域）分割方法：传统 HSV/YCbCr/ICM/椭圆边界方法、MediaPipe Selfie 分割、自训练的 U²-Net/U²-NetP、DeepLabV3+MobileNetV3、BiRefNet 及 StraightU²-Net。U²-Net、DLMV、BiRefNet 提供 ONNX Runtime Session 类与 PyTorch 实现，另有分块细化推理与 C++ demo；模型权重放于 GitHub Releases。训练数据集为 1,216 张图像、约 69.6 亿标注像素。限制：眉、牙、眼等会包含在掩码中；多人合影场景表现不佳。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖传统方法与多种深度模型（U²-Net/U²-NetP/DLMV/BiRefNet/StraightU²-Net）
- 提供 ONNX Runtime 与 PyTorch 两种推理实现（Session 类）
- 支持高分辨率分块细化推理（训练中最高 50MP）
- 自建 1,216 张图像、约 69.6 亿标注像素的数据集

## 适用场景

- 为照片修图（如皮肤瑕疵修正）生成皮肤掩码
- 结合人体分割做头发分割或 ROI 提取
- 按算力预算从指标与推理时间中选择模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository details the various methods I have attempted for skin segmentation.
> L11: you can use the `Session` class in `u2net/session.py` for ONNX Runtime inference.

## 星数曲线

```mermaid
xychart-beta
    title "samhaswon/skin_segmentation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `75eed7fae6a3` · [字段定义](../../DATASET.md)*
