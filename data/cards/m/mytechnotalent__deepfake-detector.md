# mytechnotalent/deepfake-detector

⭐ 36 · Python · Apache-2.0 · 推送 2025-11-26 · [GitHub](https://github.com/mytechnotalent/deepfake-detector) · 个人维护

**用 CNN 分类图像真伪的深度伪造检测模型与训练/推理代码**

基于 TensorFlow/Keras 的卷积神经网络二分类模型，将图像判为 REAL 或 FAKE。提供从 Kaggle（OpenForensics）数据集下载与预处理、模型构建训练、评估、保存的完整流程，以及 Flask 推理脚本。README 详细列出各层（输入 128x128x3、Rescaling、Conv2D、BatchNormalization 等）的公式与 Loss/Accuracy/Precision/Recall 指标定义，并给出 macOS/Ubuntu/Windows 三平台的 Python 3.11 虚拟环境搭建步骤。数据集作者 Trung-Nghia Le，模型作者 Kevin Thomas，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorFlow/Keras 构建的 CNN 二分类模型，输出图像 REAL/FAKE 判定
- 包含数据下载、训练、评估、模型保存的完整流程
- 提供 Flask 推理脚本（inference.py）
- macOS/Ubuntu/Windows 三平台 Python 3.11 环境搭建说明

## 适用场景

- 训练并评估自己的深度伪造图像检测模型
- 对图像做真伪判定并部署为 Web 推理服务
- 学习 CNN 各层与二分类评估指标的计算方式

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: Deepfake Detector is an AI/ML model designed to detect AI-generated or manipulated images.
> L9: This notebook uses a convolutional neural network (CNN) model to detect deepfake images. The model is built using Te

## 星数曲线

```mermaid
xychart-beta
    title "mytechnotalent/deepfake-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd1a7b23b1b7` · [字段定义](../../DATASET.md)*
