# open-edge-platform/geti

⭐ 1,358 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/open-edge-platform/geti) · [官网](https://docs.geti.intel.com) · 组织维护

**本地构建、训练、优化与运行计算机视觉模型的开源平台**

Intel 开源的端到端计算机视觉平台：覆盖标注、微调、INT8 量化优化与部署推理，内置 1,600+ 模型变体（检测/分类/分割），经 OpenVINO 面向 Intel CPU/GPU/NPU，也支持 CUDA 与纯 CPU。提供两条使用路径：面向 SME 的无代码应用（Windows MSIX/Docker/脚本/源码）与独立 Python 库 getitune。支持从 10-20 张图片起步的训练循环、SAM 辅助标注、数据集/模型版本管理及摄像头视频流的流水线部署与 OpenVINO bundle 导出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注-训练-优化-部署-推理全生命周期，无代码应用与 getitune Python API 双路径
- 1,600+ 模型变体（RF-DETR、YOLO 系、Mask R-CNN、timm backbones 等）
- OpenVINO 自动导出与精度感知 INT8 量化，支持 Intel XPU/CUDA/纯 CPU
- USB/IP 摄像头视频流推理流水线，可导出 OpenVINO 边缘部署 bundle

## 适用场景

- 少量图片起步训练检测/分类/分割模型并部署到边缘设备
- 在无代码界面中完成标注、训练与实时视频推理监控
- 用 getitune API 在代码工作流中训练、导出并量化模型

## 场景标签

 · 领域:计算机视觉/机器学习平台

## 证据(README 行号)

> L14: **_Geti™_** is an open-source, end-to-end platform for building and continuously improving your own computer vision
> L18: The Geti™ application is powered by **_getitune_**, its engine for model training and optimization, which is also a
> L39: Geti's training engine is also available on PyPI as `getitune`, an open-source Python library for training, optimiz

## 星数曲线

```mermaid
xychart-beta
    title "open-edge-platform/geti 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 1356 --> 1359
    line [1357, 1358]
```

2026-10-18 1,357 → 2026-10-22 1,358（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `102bcd68fcd0` · [字段定义](../../DATASET.md)*
