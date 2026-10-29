# shreyaskamathkm/FTNet

⭐ 20 · Python · NOASSERTION · 推送 2026-04-03 · [GitHub](https://github.com/shreyaskamathkm/FTNet) · 个人维护

**FTNet 热成像语义分割网络的 PyTorch 官方实现**

论文 "FTNet: Feature Transverse Network for Thermal Semantic Segmentation" 的官方 PyTorch 实现，基于 Pytorch Lightning 构建，内置 DistributedDataParallel/DataParallel 支持。提供 ResNeXt50/101 的预训练权重、SODA/SCUT-Seg/MFN 三个热成像数据集的训练与测试脚本，以及测试阶段生成的语义图。限制：边缘生成步骤依赖 MATLAB。面向复现论文结果或在此基础上训练自有模型的研究与开发人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 ResNeXt50/101 模型权重与各数据集语义图预测结果
- 基于 Pytorch Lightning，内置 DDP/DataParallel 支持
- 覆盖 SODA、MFN、SCUT-Seg 三个热成像数据集的完整训练测试流程
- 数据集目录结构整理与边缘生成脚本（边缘生成需 MATLAB）

## 适用场景

- 复现 FTNet 论文在热成像分割数据集上的结果
- 在热成像语义分割任务上用预训练权重做测试
- 以最小改动接入新模型进行训练

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L9: This repository is an official PyTorch implementation of the paper **" FTNet: Feature Transverse Network for Thermal
> L12: We provide scripts for the models from our paper. You can train your own model from scratch, or use pretrained mode

## 星数曲线

```mermaid
xychart-beta
    title "shreyaskamathkm/FTNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8809d5b6102a` · [字段定义](../../DATASET.md)*
