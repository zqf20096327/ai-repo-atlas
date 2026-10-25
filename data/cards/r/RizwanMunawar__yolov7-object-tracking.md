# RizwanMunawar/yolov7-object-tracking

⭐ 653 · Python · AGPL-3.0 · 推送 2026-09-11 · [GitHub](https://github.com/RizwanMunawar/yolov7-object-tracking) · 个人维护

**基于 YOLOv7 与 SORT 的目标检测与追踪脚本工具**

用 PyTorch、OpenCV 与 SORT 实现 YOLOv7 目标检测与多目标追踪的命令行工具：支持视频文件、摄像头、外接摄像头与 IP 摄像流作为输入，可按类别过滤检测、为每条轨迹分配颜色、保存轨迹中心点/ID/边界框坐标到 txt，并已加入 Ultralytics YOLOv8 权重支持（YOLOv9 及之后版本为计划中）。预训练权重可自动下载，输出保存在 runs/detect 目录。以源码仓库形式提供，含 Colab/Kaggle/SageMaker 运行入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持视频/摄像头/IP 摄像流输入的检测与追踪
- 已支持 Ultralytics YOLOv8 权重（--weights yolov8n.pt）
- 可保存轨迹 ID、中心点与边界框坐标，按类别过滤检测
- 预训练 yolov7 权重可自动下载

## 适用场景

- 对监控或视频流做带 ID 的多目标追踪
- 只检测或只追踪特定类别（如行人）
- 导出轨迹坐标数据用于后续分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: ## YOLOv7 Object Tracking 🚀
> L71:       python detect_and_track.py --weights yolov7.pt
> L119: |`--device`|`str`|`''`|CUDA device (e.g., `0` or `0,1,2,3`) or `cpu`.|

## 星数曲线

```mermaid
xychart-beta
    title "RizwanMunawar/yolov7-object-tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 652 --> 654
    line [653, 653]
```

2026-10-18 653 → 2026-10-25 653（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `1bca571cc03e` · [字段定义](../../DATASET.md)*
