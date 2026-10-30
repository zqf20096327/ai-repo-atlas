# MMUZAMMUL/GOIS

⭐ 21 · Python · NOASSERTION · 推送 2026-03-03 · [GitHub](https://github.com/MMUZAMMUL/GOIS) · 个人维护 · 中文 README

**微小目标检测增强框架：动态自适应切片推理**

Guided Object Inference Slicing（GOIS）研究代码，发表于 Neurocomputing。核心机制为两阶段分层切片：按目标密度动态调整粗到细切片尺寸、重叠率与 NMS 阈值，以提升微小目标检测并减少边界伪影与误检，可作用于微调与非微调模型（YOLO11/v10/v9/v8/v6/v5、RT-DETR-L、YOLOv8s-Worldv2）。以源码仓库提供，含 ground truth 生成、全图推理、GOIS 推理与评测脚本，另在 Gradio、Hugging Face、Colab 提供在线测试。兼容 VisDrone、UAV 监控等数据集。许可为 MIT 但声明仅限学习与教育用途，再分发或商用需作者书面同意。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段分层切片：按目标密度动态调整切片尺寸/重叠率/NMS
- 支持微调与非微调模型（YOLO 系列、RT-DETR-L、YOLOv8s-Worldv2）
- 提供推理、评测、结果对比与上采样评测的完整脚本流程
- Gradio/Hugging Face/Colab 在线测试（图像、视频、实时摄像头）

## 适用场景

- 无人机/监控影像中提升微小目标检测召回
- 对比 GOIS 切片与全图推理（FI-Det）及 SAHI/ASAHI 静态切片
- 调整切片尺寸、重叠率、NMS 参数做检测精度与速度权衡实验

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4: ## 🚀 Enhancing Tiny Object Detection Using Guided Object Inference Slicing (GOIS): An Efficient Dynamic Adaptive Fra
> L63: GOIS incorporates a **two-stage hierarchical slicing** strategy, dynamically adjusting **coarse-to-fine slicing** a

## 星数曲线

```mermaid
xychart-beta
    title "MMUZAMMUL/GOIS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7d177ac1e7ef` · [字段定义](../../DATASET.md)*
