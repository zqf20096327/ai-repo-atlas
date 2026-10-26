# dronefreak/VisDrone-dataset-python-toolkit

⭐ 85 · Python · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/dronefreak/VisDrone-dataset-python-toolkit) · [官网](https://huggingface.co/spaces/dronefreak/visdrone-aerial-detection) · 个人维护

**VisDrone 无人机航拍目标检测工具包：33 个模型的训练评测推理**

面向 VisDrone 航拍检测数据集的 PyTorch 工具包（Python 3.8+/PyTorch 2.0+），支持 33 个模型（4 个 Torchvision：Faster R-CNN/FCOS/RetinaNet + 29 个 YOLO 系列），覆盖端到端训练、评估（P/R/F1 与可选 pycocotools mAP）、图像/视频/摄像头推理、VisDrone→COCO 标注转换与 Python API。Hugging Face 上提供各 YOLO 家族的 VisDrone 预训练权重（模型卡与基准结果）。附 203 个测试与 CI。

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

- 33 个检测模型（Torchvision + YOLOv8/v9/v10/11/26）
- 训练/评估/图像视频摄像头推理/标注转换端到端脚本
- Hugging Face 提供全部 YOLO 家族的 VisDrone 预训练权重
- Python API（VisDroneDataset、get_model）与 203 个测试

## 适用场景

- 在 VisDrone 数据集上训练并评测无人机航拍目标检测模型
- 用预训练权重对航拍图像/视频做目标检测推理
- 将 VisDrone 标注转换为 COCO 格式用于其他工具链

## 场景标签

`目标检测` `模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: PyTorch toolkit for the VisDrone aerial detection dataset. Supports 33 models (4 torchvision + 29 YOLO), end-to-end 
> L107: python scripts/inference.py \

## 星数曲线

```mermaid
xychart-beta
    title "dronefreak/VisDrone-dataset-python-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-26 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `66f37403ef08` · [字段定义](../../DATASET.md)*
