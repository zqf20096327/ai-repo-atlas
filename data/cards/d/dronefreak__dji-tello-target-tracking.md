# dronefreak/dji-tello-target-tracking

⭐ 56 · Python · Apache-2.0 · 推送 2025-11-11 · [GitHub](https://github.com/dronefreak/dji-tello-target-tracking) · 个人维护

**DJI Tello 无人机的 YOLOv8 实时目标检测与自主跟随系统**

基于 PyTorch 与 YOLOv8 的无人机目标检测与跟踪项目：用深度学习模型替代旧版 HSV 颜色跟踪，支持 80+ 类物体检测、质心多目标跟踪与轨迹预测，并通过自动调参 PID 控制无人机平滑跟随目标。面向拥有 DJI Tello 的开发者和爱好者，提供无硬件的摄像头 demo 与 mock 无人机模式；支持手动/自主切换、电量监控与紧急停止。可选 yolov8n/s/m/l/x 五档模型，GPU 加速为可选。

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

- YOLOv8 检测（80+ 类物体）与质心多目标跟踪
- PID 控制的自主跟随，支持手动接管与紧急停止
- 无硬件测试路径：摄像头 demo 与 mock 无人机模式
- 165+ 单元测试，覆盖率 >85%

## 适用场景

- 让 Tello 无人机自主跟随人员或物体飞行
- 在无无人机硬件时用摄像头验证检测与跟踪效果
- 作为目标检测与飞行控制的 Python 实现参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: Real-time object detection and autonomous tracking for DJI Tello drones using PyTorch and YOLOv8. This modernized ve
> L11: - 🎯 **Modern Object Detection**: YOLOv8-powered detection (person, ball, car, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "dronefreak/dji-tello-target-tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-26 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `30d53556c6cb` · [字段定义](../../DATASET.md)*
