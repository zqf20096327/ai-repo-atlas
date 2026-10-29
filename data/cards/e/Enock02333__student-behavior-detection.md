# Enock02333/student-behavior-detection

⭐ 22 · Python · 推送 2026-04-17 · [GitHub](https://github.com/Enock02333/student-behavior-detection) · 个人维护

**用 YOLO 检测课堂学生行为的计算机视觉项目**

基于 YOLOv8n 等轻量级目标检测模型的课堂行为检测项目：识别读书、写字、举手、回答问题等 11 类行为，输出带边界框的检测结果，并生成混淆矩阵与 Precision-Recall 曲线等评估指标。面向教育者与计算机视觉开发者，用于课堂活动监测与教学策略分析。训练与推理通过单个 Python 脚本完成，数据集来自 Roboflow 公开数据集，需手动下载放入 data/ 目录；训练默认参数为 100 epochs、batch 8、imgsz 416。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别 11 类课堂行为（读书/写字/举手/回答问题等）
- 使用 YOLOv8n 等轻量级预训练模型
- 生成混淆矩阵与 Precision-Recall 曲线等评估输出
- 支持对新图像做推理并输出带边界框的结果图

## 适用场景

- 我想自动检测课堂中学生举手、读书、写字等行为
- 分析学生课堂参与度和活动水平
- 训练并评估 YOLOv8 课堂行为检测模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: A computer vision project aimed at detecting and classifying student behaviors in classroom settings using YOLO-base
> L31: - **YOLO-based Models:** Uses lightweight pre-trained YOLO models like YOLOv8n for fast and efficient detection.

## 星数曲线

```mermaid
xychart-beta
    title "Enock02333/student-behavior-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4bf390f6a678` · [字段定义](../../DATASET.md)*
