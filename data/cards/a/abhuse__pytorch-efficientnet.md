# abhuse/pytorch-efficientnet

⭐ 54 · Jupyter Notebook · MIT · 推送 2026-03-05 · [GitHub](https://github.com/abhuse/pytorch-efficientnet) · 个人维护

**PyTorch 版 EfficientNetV2/V1 实现并附预训练权重**

以单文件形式提供 EfficientNetV2 与 EfficientNetV1 的 PyTorch 实现，并将官方 TensorFlow 预训练权重转换为 PyTorch 格式供下载（pretrained=True 时自动初始化）。提供 tf_style_conv 参数模拟 TensorFlow 的 SAME padding，用于在 ImageNet 上评估预训练权重或做特征提取；自行训练/微调时可设为 False（仅适用于 V2）。README 列出各模型在 ImageNet 1k 上的 Top-1 精度，并附带 cifar100 训练与 ImageNet 评估 notebook。要求 Python 3.5+ 与 PyTorch 1.0+。

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

- EfficientNetV2/V1 的单文件 PyTorch 实现
- TensorFlow 预训练权重转换为 PyTorch 格式提供
- tf_style_conv 参数模拟 TensorFlow SAME padding（仅 V2）
- 列出各模型 ImageNet 1k Top-1 精度并附训练/评估 notebook

## 适用场景

- 用预训练 EfficientNet 做图像分类或特征提取
- 在自己的数据集上微调 EfficientNet 模型
- 在 ImageNet 验证集上复现模型精度

## 场景标签

 · 领域:计算机视觉/图像分类

## 证据(README 行号)

> L1: # EfficientNetV2 EfficientNetV1 in Pytorch with pretrained weights
> L7: These weigths were converted to Pytorch format and are provided in this repository.

## 星数曲线

```mermaid
xychart-beta
    title "abhuse/pytorch-efficientnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `91ef3d59a094` · [字段定义](../../DATASET.md)*
