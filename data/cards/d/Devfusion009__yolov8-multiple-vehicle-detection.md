# Devfusion009/yolov8-multiple-vehicle-detection

⭐ 34 · Python · 推送 2026-07-10 · [GitHub](https://github.com/Devfusion009/yolov8-multiple-vehicle-detection) · 个人维护

**基于 YOLOv8 的视频车辆检测与桥梁载荷控制演示**

Python 项目：用 YOLOv8 检测并跟踪视频中的汽车、公交与卡车，叠加多目标跟踪与出入口线逻辑，按车辆类别估算重量，实时计算桥梁载荷（默认上限 20 吨），超载时在画面上显示 CLOSED 与红色闸门提示，重量下降后自动重开。附带配置常量可修改容量、重量与检测线位置；支持替换视频文件或接入摄像头/RTSP 流。阻塞仅为逻辑/视觉层面，不含硬件控制。面向想学习检测、跟踪与业务逻辑结合的开发者。

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

- YOLOv8 检测 car/bus/truck 并跨帧保持稳定 ID
- 入口/出口双线逻辑与按类别的重量估算
- 默认 20 吨容量管理，超载显示 CLOSED 与红色闸门，自动重开
- 可替换视频文件或接入摄像头/RTSP 流

## 适用场景

- 学习 YOLOv8 检测与多目标跟踪的完整流程
- 演示视频流上的桥梁载荷监控与闸门控制逻辑
- 在此基础上替换输入源做交通监控实验

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: - Vehicle detection (cars, buses, trucks) with YOLOv8
> L42: 2. Detect objects using YOLOv8.

## 星数曲线

```mermaid
xychart-beta
    title "Devfusion009/yolov8-multiple-vehicle-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d0f191bbc8ec` · [字段定义](../../DATASET.md)*
