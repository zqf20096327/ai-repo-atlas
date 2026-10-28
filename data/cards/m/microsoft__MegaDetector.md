# microsoft/MegaDetector

⭐ 56 · Python · MIT · 推送 2026-06-25 · [GitHub](https://github.com/microsoft/MegaDetector) · [官网](https://microsoft.github.io/MegaDetector/) · 组织维护

**检测红外相机图像中动物/人/车辆的开源模型**

Microsoft AI for Good Lab 开源的相机陷阱图像检测模型 MegaDetector V6，对图像中的动物、人、车辆输出边界框与置信度，用于过滤空帧以加速野生动物研究审阅。提供 9 个变体（YOLOv9/YOLOv10/RT-DETR 架构，参数量 2.3M–76M，MIT/Apache-2.0/AGPL-3.0 多种许可）。它是检测器而非物种分类器，物种识别需配合下游分类器组成两阶段流水线。使用方式包括 PytorchWildlife Python API、megadetector CLI、SPARROW Studio/AddaxAI 图形应用及 Hugging Face 网页演示。限制：对极小/远处动物、伪装物种识别置信度较低，不适用于水下、航拍与声学监测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测动物/人/车辆三类目标，输出边界框与 0-1 置信度
- 9 个模型变体覆盖 2.3M–76M 参数量，最小变体可在 CPU 运行
- 提供 Python API、CLI、图形界面（SPARROW Studio/AddaxAI）与 Hugging Face 演示
- 支持在自有数据集上微调（megadetector train/validate）

## 适用场景

- 批量过滤红外相机照片中的空帧，减少人工审阅量
- 两阶段流水线：检测动物后接物种分类器做物种识别
- 区分图像中的人类与车辆活动，用于保护地巡护分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **MegaDetector is an open-source AI model from the Microsoft AI for Good Lab that detects animals, people, and vehic
> L5: MegaDetector is one project in the microsoft/Biodiversity ecosystem and is invoked through the PyTorch-Wildlife fram

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/MegaDetector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-28 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `41a90395f098` · [字段定义](../../DATASET.md)*
