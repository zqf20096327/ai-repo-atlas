# Sinapsis-AI/sinapsis-object-detection

⭐ 20 · Python · AGPL-3.0 · 推送 2026-04-20 · [GitHub](https://github.com/Sinapsis-AI/sinapsis-object-detection) · [官网](https://sinapsis.tech/) · 组织维护

**面向计算机视觉开发者的多模型目标检测训练与推理模板集**

Sinapsis 体系下的目标检测 mono repo，包含三个包：sinapsis-dfine（D-FINE 微调与推理）、sinapsis-rfdetr（RF-DETR 训练/推理/ONNX 导出）、sinapsis-ultralytics（Ultralytics 训练/验证/预测/导出）。以模板形式组织训练与推理流程，附 Gradio 演示 webapp，可通过 Docker compose 或 uv 运行。要求 Python 3.10+，从私有 PyPI 索引安装；D-FINE 演示默认使用 CUDA 加速。采用 AGPLv3 许可，另提供商业许可获取渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个包分别适配 D-FINE、RF-DETR、Ultralytics 模型
- 覆盖训练、微调、推理、验证与 ONNX/部署格式导出的模板
- 附 Gradio webapp 演示，支持 Docker compose 与 uv 两种运行方式

## 适用场景

- 在自定义数据上微调 D-FINE 或 RF-DETR 目标检测模型
- 用 Ultralytics 模板完成训练、验证与预测流程
- 通过 Gradio 网页应用快速体验各模型的检测效果

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L8:  Mono repo with packages for training and inference with various models for advanced object detection tasks.
> L64: This repository is organized into modular packages, each built for integration with different object detection mode

## 星数曲线

```mermaid
xychart-beta
    title "Sinapsis-AI/sinapsis-object-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9a9a7e11eaab` · [字段定义](../../DATASET.md)*
