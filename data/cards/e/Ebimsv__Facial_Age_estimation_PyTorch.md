# Ebimsv/Facial_Age_estimation_PyTorch

⭐ 88 · Python · MIT · 推送 2026-08-18 · [GitHub](https://github.com/Ebimsv/Facial_Age_estimation_PyTorch) · 个人维护

**基于 PyTorch 的人脸年龄估计训练与推理管线**

人脸年龄估计深度学习工程：提供 5 种骨干网络（MobileNetV3-Large、EfficientNet-B0/B3、ResNet-50、ViT-S/14 DINOv2），采用 Mean-Variance Loss（CVPR 2018）将年龄建模为 [0–100] 上的概率分布，输出 101 类分布而非单一标量。面向计算机视觉开发者与研究人员，使用 UTKFace 数据集训练（约 23,000 张图，年龄 0–116），支持 CPU 与 GPU 训练、AMP 混合精度、OmegaConf 配置覆盖、按年龄/性别/族裔的 MAE 偏差分析、TorchScript 与 ONNX 导出，以及 Gradio 演示界面。当前多数基准结果标记为 TBD，EfficientNet-B3 训练仍在进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 5 种骨干网络支持（MobileNetV3/EfficientNet/ResNet-50/ViT DINOv2）
- Mean-Variance Loss 将年龄建模为 101 类概率分布
- 按年龄组、性别、族裔分组的偏差分析（MAE 分解）
- TorchScript 与 ONNX（动态 batch）导出，及 Gradio 演示

## 适用场景

- 我在 UTKFace 数据集上训练人脸年龄估计模型并评估 MAE
- 我上传一张人脸照片，得到预测年龄及其概率分布
- 我把训练好的年龄估计模型导出为 ONNX 用于部署

## 场景标签

`人脸识别` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L5: **Production-ready deep learning pipeline for estimating age from face images.**
> L27: - 🖥️ **Gradio demo** — upload a photo → see predicted age + full probability distribution
> L22: - 📐 **Mean-Variance Loss** (CVPR 2018) — models age as a probability distribution over [0–100], outperforming plain

## 星数曲线

```mermaid
xychart-beta
    title "Ebimsv/Facial_Age_estimation_PyTorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-26 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `bbe917d2681d` · [字段定义](../../DATASET.md)*
