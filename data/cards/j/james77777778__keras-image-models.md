# james77777778/keras-image-models

⭐ 48 · Python · Apache-2.0 · 推送 2026-01-01 · [GitHub](https://github.com/james77777778/keras-image-models) · 个人维护

**Keras 3 图像模型库：预训练视觉模型与迁移学习 API**

KIMM（kimm）是用 Keras 3 编写的图像模型集合，包含层、块与模型，绝大部分模型附带 ImageNet 预训练权重，权重多移植自 timm。提供模型枚举、特征提取、重参数化技术支持，以及导出 .tflite 与 .onnx 的 API。附有图像分类、cats vs. dogs 微调、Grad-CAM 等 Colab 示例。代码以 Apache 2.0 许可，许可声明要求参照 timm。安装方式为 pip。

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

- 模型动物园：绝大多数模型附带 ImageNet 预训练权重
- 支持导出 .tflite 与 .onnx
- 集成特征提取能力（feature_keys 指定）
- 支持重参数化技术（ReparameterizableConv2D）

## 适用场景

- 在 Keras 3 中做图像分类的迁移学习与微调
- 导出模型到 TFLite/ONNX 用于部署
- 从预训练骨干网络提取特征

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L23: **K**eras **Im**age **M**odels (`kimm`) is a collection of image models, blocks and layers written in Keras 3. The 
> L27: - 🚀 A model zoo where almost all models come with **pre-trained weights on ImageNet**.

## 星数曲线

```mermaid
xychart-beta
    title "james77777778/keras-image-models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-28 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f1b3ff2e048c` · [字段定义](../../DATASET.md)*
