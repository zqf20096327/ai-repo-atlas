# TUI-NICR/ESANet

⭐ 281 · Python · Apache-2.0 · 推送 2026-01-01 · [GitHub](https://github.com/TUI-NICR/ESANet) · 组织维护

**面向移动机器人的高效 RGB-D 室内语义分割网络**

论文 'Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis' 的官方代码，提供训练、评估、数据集/样例推理、ONNX 与 TensorRT 转换及推理耗时测量脚本。网络可在 NVIDIA Jetson AGX Xavier 上实时运行，面向移动机器人实时场景分析流程。在 NYUv2、SUNRGB-D、Cityscapes 上训练，提供 ESANet-R34-NBt1D 预训练权重下载；2025 年更新了环境（Python 3.12、PyTorch 2.9.1）。Jetson 上复现计时依赖特定 Jetpack 4.4 与 TensorRT 版本。以源码仓库形式发布，需自行准备数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供训练/评估/推理全套脚本与预训练权重（NYUv2、SUNRGB-D、Cityscapes）
- 支持导出 ONNX 与 TensorRT，附 Jetson AGX Xavier 推理计时脚本
- 2025 年更新 conda 环境（Python 3.12、PyTorch 2.9.1，移除 TensorFlow）

## 适用场景

- 在移动机器人上做实时室内 RGB-D 语义分割
- 复现论文 mIoU 结果或在新数据集上训练模型
- 将模型转为 TensorRT 并测量嵌入式设备推理耗时

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: This repository contains the code to our paper "Efficient RGB-D Semantic
> L14: Our carefully designed network architecture enables real-time semantic

## 星数曲线

```mermaid
xychart-beta
    title "TUI-NICR/ESANet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 280 --> 282
    line [281, 281]
```

2026-10-18 281 → 2026-10-31 281（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `0d910585d9b2` · [字段定义](../../DATASET.md)*
