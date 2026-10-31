# dyneth02/YOLOv11-People-Enter-Exit-Detector

⭐ 15 · Python · MIT · 推送 2026-01-08 · [GitHub](https://github.com/dyneth02/YOLOv11-People-Enter-Exit-Detector) · 个人维护

**基于 YOLOv11 与 OpenCV 的双向人流计数与占用分析系统**

使用 YOLOv11（Ultralytics）进行行人检测与跟踪的 Python 应用：在出入口附近定义两个多边形 ROI，通过跟踪边界框底部中心点在 area1/area2 之间的移动顺序判定进入/离开事件，用字典状态管理防止重复计数，实时计算当前在场人数，并用 OpenCV VideoWriter 导出带计数器与边界叠加的视频。安装方式为 git clone 源码加 pip 安装 ultralytics、opencv-python、cvzone、numpy 依赖。检测区域坐标需在 main.py 中手工配置。

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

- 双多边形 ROI 逻辑区分进入与离开方向
- YOLOv11 persist=True 多目标跟踪维持唯一 ID，防止重复计数
- 实时计算在场人数（Entered - Exited）
- 自动导出带计数器、轨迹 ID 与检测边界叠加的视频

## 适用场景

- 零售门店统计客流量进出人数
- 室内空间实时在场人数监控
- 生成带可视化标注的人流分析视频报告

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: An advanced Computer Vision system that performs real-time detection, tracking, and bidirectional counting of indivi
> L17: - **Core Engine:** YOLO11 (Ultralytics) for object detection.

## 星数曲线

```mermaid
xychart-beta
    title "dyneth02/YOLOv11-People-Enter-Exit-Detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ba5dd0e722fc` · [字段定义](../../DATASET.md)*
