# leondgarse/keras_cv_attention_models

⭐ 625 · Python · MIT · 推送 2026-02-15 · [GitHub](https://github.com/leondgarse/keras_cv_attention_models) · 个人维护

**Keras/PyTorch 双后端的视觉模型实现库：识别、检测等预训练模型**

以 Keras 风格 API 复现大量视觉骨干网络（VOLO、CoAtNet、Swin、EfficientNet 系列等）及检测头（EfficientDet/YOLOX/YOLOR/YOLOV8 锚模式），支持 TensorFlow 与 PyTorch 双后端（KECAM_BACKEND 切换），加载 ImageNet/COCO 预训练权重即可输出分类或检测预测结果。附 ImageNet 训练/评估/渐进式训练脚本、ONNX 导出、FLOPs 计算与 model_surgery 等工具。限制：不兼容 keras 3.x（需 tf-keras 或 TF_USE_LEGACY_KERAS=1），COCO 训练脚本仍在测试中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 100+ 视觉模型架构实现，TensorFlow/PyTorch 双后端切换
- 预训练权重加载与模型预测（preprocess_input/decode_predictions）
- ImageNet 训练/评估/渐进式训练脚本与断点恢复
- ONNX 导出、FLOPs 计算、模型结构修改（model_surgery）工具

## 适用场景

- 用预训练模型做图像分类或目标检测推理
- 微调/迁移训练自己的识别或检测数据集
- 导出 ONNX 或对比不同骨干网络的参数量与推理速度

## 场景标签

`目标检测` `微调` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L29:     from keras_cv_attention_models import volo
> L200:  - Default parameters for `coco_train_script.py` is `EfficientDetD0` with `input_shape=(256, 256, 3), batch_size=6

## 星数曲线

```mermaid
xychart-beta
    title "leondgarse/keras_cv_attention_models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 624 --> 626
    line [625, 625]
```

2026-10-18 625 → 2026-10-30 625（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9735eac4f61f` · [字段定义](../../DATASET.md)*
