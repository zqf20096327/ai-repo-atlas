# IanButterworth/YOLO.jl

⭐ — · [GitHub]() · 个人维护

**Julia 实现的 YOLO 目标检测库，加载 YOLOv2-tiny 预训练模型**

基于 Knet.jl 的 Julia 目标检测包，当前仅支持加载 YOLOv2-tiny 与 VOC-2007 预训练模型（Darknet 预训练），提供数据集测试、单图推理（含加载/缩放/填充辅助函数）、结果渲染（配合 Makie）与推理速度基准测试。支持 CUDA GPU 运行；CPU 运行时依赖系统编译器。README 标注 Example Usage 为 WIP，并指引参考 ObjectDetector.jl 与 Darknet.jl 等其他实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 加载 YOLOv2-tiny VOC-2007 预训练模型进行目标检测
- 提供图像加载/缩放/填充辅助函数与结果渲染
- 支持 CUDA GPU 或 CPU 运行，附推理速度基准

## 适用场景

- 在 Julia 中对图像运行 YOLO 目标检测推理
- 在 VOC 数据集上评估检测效果
- 用 Makie 可视化与保存检测结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Currently only supports loading YOLOv2-tiny and the VOC-2007 pretrained model (pretrained on Darknet).
> L64: predictions = YOLO.postprocess(res, settings, conf_thresh = 0.3, iou_thresh = 0.3)

## 星数曲线

```mermaid
xychart-beta
    title "IanButterworth/YOLO.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `86bd31913620` · [字段定义](../../DATASET.md)*
