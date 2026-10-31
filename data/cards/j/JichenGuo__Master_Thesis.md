# JichenGuo/Master_Thesis

⭐ 15 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/JichenGuo/Master_Thesis) · 个人维护

**硕士论文代码：改造 YOLOv3 做目标检测与距离估计**

在 keras-yolo3 实现基础上修改 YOLOv3：在每个预测层增加距离预测变量，并在原损失函数中加入距离损失项（尝试过 MAE/MSE/RMSE，作者选 MAE）。使用处理后的公开 KITTI 数据集与自建 SMART 数据集进行迁移学习再训练；评估时分别用 TP、PR 曲线、mAP 衡量检测性能，并单独评估距离估计。README 列出多个测试图片示例，但未提供安装与运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv3 每个预测层增加距离预测变量
- 损失函数加入距离损失项（MAE/MSE/RMSE 中选 MAE）
- 基于 KITTI 与 SMART 数据集的迁移学习训练
- 检测（TP/PR/mAP）与距离估计分别评估

## 适用场景

- 在图像目标检测的同时估计物体距离
- 复现或参考单目视觉距离估计的模型改造方案

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2: Topic: Modification of YOLOv3(Keras) for object distance estimation
> L6: 1.Modify the output of YOLOv3 by adding a predicted distance variable at each prediction layer.
> L9: 4.Evaluation: judge the performance of object detection (metrics of TP, PR curve, mAP) and distance estimation separ

## 星数曲线

```mermaid
xychart-beta
    title "JichenGuo/Master_Thesis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `76f6596213f5` · [字段定义](../../DATASET.md)*
