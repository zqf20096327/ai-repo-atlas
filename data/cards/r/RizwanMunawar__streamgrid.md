# RizwanMunawar/streamgrid

⭐ 17 · Python · AGPL-3.0 · 推送 2026-05-20 · [GitHub](https://github.com/RizwanMunawar/streamgrid) · 个人维护

**多路视频流网格显示工具，实时运行 YOLO 目标检测**

基于 Ultralytics YOLO 的多视频流推理展示库：将多路视频流以网格布局并排显示，并在所有流上实时运行目标检测，支持 CPU 或 GPU 设备。提供 Python API 与 CLI 两种使用方式（如 streamgrid model=yolo11n.pt），通过 pip 安装。按流数自动调整分辨率与帧率（1-2 路最高 15 FPS/流，10+ 路降至 240×135、约 3 FPS/流）；基准测试基于 CPU，官方标注为 Beta，最终数据待发布。适用于监控画面浏览与多流分析看板等场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多路视频流网格布局并排显示
- 在全部流上实时运行 Ultralytics YOLO 检测
- 支持 CPU/GPU 设备，按流数自动调整分辨率与帧率
- 提供 Python API 与 CLI 两种调用方式

## 适用场景

- 把多路监控视频集中到一个网格界面并叠加目标检测
- 搭建多流实时检测的分析看板
- 用 CLI 一条命令跑起多流 YOLO 推理

## 场景标签

 · 领域:计算机视觉/视频分析

## 证据(README 行号)

> L3: Ultra-fast multi-stream video display, Run real-time object detection across multiple video feeds with real-time spe
> L5: From smart surveillance to AI-powered dashboards, StreamGrid makes it effortless to display and analyze multiple vid

## 星数曲线

```mermaid
xychart-beta
    title "RizwanMunawar/streamgrid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `90cab5bb5e63` · [字段定义](../../DATASET.md)*
