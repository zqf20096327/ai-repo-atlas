# sovit-123/fasterrcnn-pytorch-training-pipeline

⭐ 275 · Jupyter Notebook · MIT · 推送 2025-10-29 · [GitHub](https://github.com/sovit-123/fasterrcnn-pytorch-training-pipeline) · 个人维护

**在自定义数据集上训练与推理 PyTorch Faster R-CNN 的流水线**

基于 PyTorch/Torchvision 的目标检测训练流水线：在自有数据集（Pascal VOC XML 或 YOLO 文本标注）上训练 Faster R-CNN 模型，可选择 Torchvision 预训练模型（COCO）或替换 Torchvision 分类骨干（ConvNext、MobileNetV3、EfficientNet、DINOv3 等），也可自定义骨干。提供单机/多卡分布式训练、图像与视频推理、ONNX 视频推理、SAHI 切片推理、Deep SORT 实时跟踪及 mAP 评估脚本。Mini Darknet 骨干加 Mini 检测头在 RTX 3080 上报告超过 150 FPS。以源码仓库形式提供，需按 GPU 型号选择 requirements 安装，Windows 需先装 Visual Studio C++ Build Tools。

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

- 支持 Pascal VOC XML 与 YOLO 文本两种标注格式训练
- 多种骨干可选（ResNet50、ConvNext、MobileNetV3、EfficientNet、DINOv3 等）
- 集成 SAHI 切片推理与 Deep SORT 实时跟踪
- 提供图像/视频推理、评估与多卡分布式训练脚本

## 适用场景

- 在自有数据集上训练 Faster R-CNN 目标检测模型
- 用 COCO 预训练模型直接对图像或视频做检测与跟踪
- 替换骨干网络做检测精度与速度的实验对比

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L5: Train PyTorch FasterRCNN models easily on any custom dataset. Choose between official PyTorch models trained on COCO
> L7: ***You can run a Faster RCNN model with Mini Darknet backbone and Mini Detection Head at more than 150 FPS on an RTX

## 星数曲线

```mermaid
xychart-beta
    title "sovit-123/fasterrcnn-pytorch-training-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 274 --> 276
    line [275, 275]
```

2026-10-18 275 → 2026-10-25 275（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9a24f25b76b6` · [字段定义](../../DATASET.md)*
