# trflorian/virtual-hand-clone

⭐ 21 · GDScript · MIT · 推送 2026-05-16 · [GitHub](https://github.com/trflorian/virtual-hand-clone) · [官网](https://medium.com/@flip.flo.dev/real-time-hand-tracking-in-godot-creating-virtual-3d-clones-of-my-hands-ecbfb73c2fcf) · 个人维护

**用单个摄像头追踪手部并在 Godot 中生成 3D 手部克隆**

通过 Python + MediaPipe + OpenCV 从单个摄像头检测并追踪手部关键点坐标，坐标经 UDP 发送至 Godot 4.6 游戏引擎，在 3D 场景中可视化虚拟手部克隆。运行方式：在 python 目录用 uv run hand_detection.py 启动检测窗口，同时在 Godot 中打开 godot 目录项目运行。项目提供教程与演示动画，MIT 许可。

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

- MediaPipe + OpenCV 单摄像头手部关键点检测
- 检测坐标经 UDP 发送至 Godot 进行 3D 可视化
- uv 一键安装依赖并运行检测脚本

## 适用场景

- 在 Godot 游戏或原型中用自己的手实时操控 3D 虚拟手
- 学习手部追踪与引擎间 UDP 通信的实现方式

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: In this project I created a digital 3D clone of my hands with a single webcam.
> L10: To track the hands, I use mediapipe with OpenCV and Python.
> L11: The identified hand landmark coordinates are then packaged and sent via UDP to Godot, where the virtual hands are t

## 星数曲线

```mermaid
xychart-beta
    title "trflorian/virtual-hand-clone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `49a6eabfe42f` · [字段定义](../../DATASET.md)*
