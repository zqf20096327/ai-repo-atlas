# sergio11/safedrive_drowsiness_detection

⭐ 18 · Jupyter Notebook · Apache-2.0 · 推送 2025-11-29 · [GitHub](https://github.com/sergio11/safedrive_drowsiness_detection) · 个人维护

**学习项目：CNN 与 YOLO 两种路线的驾驶员疲劳检测**

深度学习课程产出的教育实验项目：在 Kaggle 的 Driver Drowsiness Dataset（41,790+ 张 227x227 标注人脸图像，约 2.32 GB）上训练并比较两条路线——基于 MobileNetV2 迁移学习的 CNN 二分类（Drowsy/Non-Drowsy），以及经 Roboflow 集成的 YOLOv8 实时目标检测。README 给出方法流程（预处理、训练、以 accuracy/precision/recall/F1 评估、实时性模拟）与两种方案的对比表，并讨论 TensorFlow Lite 移动端集成。作者声明仅供学习与研究用途，未见安装命令或代码运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两条路线对比：MobileNetV2 迁移学习分类与 Roboflow 集成的 YOLOv8 实时检测
- 基于 41,790+ 张标注图像的 DDD 数据集，Drowsy/Non-Drowsy 二分类
- 提供两种方案在实时性、数据需求、硬件要求等维度的对比表
- 讨论 TensorFlow Lite 移动端部署的模型选型

## 适用场景

- 学习疲劳检测任务中分类与目标检测两类方法的差异
- 参考迁移学习与 Roboflow 数据准备流程做类似视觉实验
- 了解移动端实时检测模型的选型考量

## 场景标签

`教程课程` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L66: Driver fatigue is a major cause of road accidents worldwide 😴. Detecting **drowsy driving** in real-time is crucial
> L89: - **Classes:** `Drowsy` vs. `Non-Drowsy`.

## 星数曲线

```mermaid
xychart-beta
    title "sergio11/safedrive_drowsiness_detection 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7e4897fb6431` · [字段定义](../../DATASET.md)*
