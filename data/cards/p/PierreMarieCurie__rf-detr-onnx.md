# PierreMarieCurie/rf-detr-onnx

⭐ 103 · Python · MIT · 推送 2026-01-31 · [GitHub](https://github.com/PierreMarieCurie/rf-detr-onnx) · 个人维护

**RF-DETR 目标检测模型的 ONNX 转换与推理工具集**

加载 RF-DETR 的 ONNX 版本并执行推理，把检测结果绘制到图像上；同时提供把 PyTorch 检查点导出为 ONNX 的转换脚本，架构（Nano/Small/Medium/Base/Large）自动检测。已将 Roboflow 预训练模型（COCO 与 Objects365 上的多尺寸检测模型、COCO 实例分割模型，对应 rf-detr 1.4.1）转好并托管在 Hugging Face。依赖精简，用 uv 或 pip 安装，提供 Python API 与命令行两种推理方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 检查点自动识别架构并导出为 ONNX
- Python API 与 CLI 两种推理方式，结果绘制到图像
- Hugging Face 托管已转换的预训练检测与分割模型
- 仅推理可免装 rfdetr 依赖的精简安装选项

## 适用场景

- 在最小依赖环境下运行 RF-DETR 目标检测推理
- 把自己的 RF-DETR 微调模型导出为 ONNX 格式
- 下载现成 ONNX 预训练模型做检测或实例分割

## 场景标签

`目标检测` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L5: This repository contains code to load an ONNX version of RF-DETR and perform inference, including drawing the result
> L7: RF-DETR is a transformer-based object detection and instance segmentation architecture developed by Roboflow. For mo

## 星数曲线

```mermaid
xychart-beta
    title "PierreMarieCurie/rf-detr-onnx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-24 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `347146eda11b` · [字段定义](../../DATASET.md)*
