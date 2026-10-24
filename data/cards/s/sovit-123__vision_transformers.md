# sovit-123/vision_transformers

⭐ 69 · Python · MIT · 推送 2025-10-29 · [GitHub](https://github.com/sovit-123/vision_transformers) · 个人维护

**给 CV 从业者的视觉 Transformer 模型库：训练与推理图像分类/检测**

提供 ViT、Swin Transformer、MobileViT 等图像分类模型与 DETR 系列目标检测模型的 PyTorch 实现，内置分类器训练脚本（支持按类文件夹组织的数据、自动验证集切分）、DETR 训练脚本，以及图像/视频推理与多目标跟踪命令；模型可加载 Torchvision/Timm/微软官方预训练权重，也可仅作为模型构建库导入自有训练流程。以 pip 包与源码两种方式安装，提供按 GPU 架构（Ampere/Ada/Blackwell）区分的依赖文件。

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

- 内置 ViT/Swin/MobileViT 分类与 DETR 检测模型实现，可加载多种预训练权重
- 分类与检测训练脚本：按类文件夹读取数据、自动验证切分
- DETR 图像/视频推理与 COCO 预训练权重多目标跟踪
- 模型可脱离训练管线单独导入（vit_b_p16_224(num_classes, pretrained)）

## 适用场景

- 用自己的数据集微调 ViT 或 Swin 分类模型
- 训练 DETR 做自定义目标检测并跑视频推理/跟踪
- 在自有训练管线中直接复用模型定义

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L9: - Image Classification
> L22: - Object Detection
> L78: model = vit.vit_b_p16_224(num_classes=1000, pretrained=True)

## 星数曲线

```mermaid
xychart-beta
    title "sovit-123/vision_transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-24 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `efa4ffeeca04` · [字段定义](../../DATASET.md)*
