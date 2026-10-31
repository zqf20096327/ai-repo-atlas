# AlvaroCavalcante/hand-face-detector

⭐ 18 · Python · 推送 2026-01-15 · [GitHub](https://github.com/AlvaroCavalcante/hand-face-detector) · 个人维护

**手语场景的手部与面部检测数据集、预训练模型及代码**

ESANN 论文配套仓库：提供基于 AUTSL 数据集构建的大规模手部与面部检测数据集（47.7 万帧、约 26 GB，PASCAL VOC 与 YOLO 标签格式），以及用 TensorFlow Object Detection API 训练的多种检测模型（SSD、EfficientDet、YoloV7、Faster R-CNN、CenterNet 等），附推理脚本、TFRecord 生成、训练与导出流程。数据集按 Chalearn 指南划分训练/验证/测试集且说话人不跨集。开发者需 Python 3.8 环境自行安装依赖，重训练需另装 TF OD API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 477,480 帧、954,960 个手部标注的大规模检测数据集
- 多种检测架构的预训练模型（SavedModel 格式）与基准结果表
- 提供推理脚本（默认摄像头流，输出 output.avi）与训练/评估/导出命令
- 数据按说话人划分，无跨集泄露

## 适用场景

- 我在做手语识别研究，需要手部/面部检测的预训练模型
- 我需要大规模手语视频的检测标注数据集来训练自己的模型
- 我想复现论文中的检测基准或在其上训练新模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Large-Scale Dataset and Benchmarking for Hand and Face Detection Focused on Sign Language
> L3: Detecting the hands and the face is an important task for sign language, as these channels contain the majority of t

## 星数曲线

```mermaid
xychart-beta
    title "AlvaroCavalcante/hand-face-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `e1b82e16cbed` · [字段定义](../../DATASET.md)*
