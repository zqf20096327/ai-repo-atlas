# YilmazKadir/Volt

⭐ 195 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/YilmazKadir/Volt) · [官网](https://www.vision.rwth-aachen.de/Volt) · 组织维护

**3D 场景理解的体素 Transformer 语义/实例分割模型官方实现**

ECCV 2026 论文 Volume Transformer (Volt) 的官方实现，基于 Pointcept 代码库构建，实例分割部分引入 SGIFormer 组件。模型将输入 3D 场景划分为不重叠的体素 patch，经线性 tokenizer 嵌入为 token，由全局注意力的 Transformer encoder 处理，再经一次转置卷积上采样回体素分辨率并输出语义预测。纯 PyTorch 实现，不依赖 spconv。支持 ScanNet/ScanNet200/ScanNet++/nuScenes/SemanticKITTI/Waymo/SceneFun3D 数据集的训练与预处理，提供 HuggingFace 权重下载与 Model Zoo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 体素 patch 化 + 全局注意力 Transformer encoder 的分割架构
- 纯 PyTorch 实现，不依赖 spconv
- 覆盖 6+ 数据集的语义与实例分割训练流程与预处理脚本
- 提供蒸馏训练（UNet teacher）与多数据集联合训练配置

## 适用场景

- 在 ScanNet/nuScenes/Waymo 等数据集上训练 3D 语义与实例分割模型
- 复现 ECCV 2026 论文实验结果
- 下载预训练 backbone 权重用于下游 3D 场景理解任务

## 场景标签

 · 领域:计算机视觉/3D 场景理解

## 证据(README 行号)

> L10:  This repository contains the official implementation of Volume Transformer (Volt).
> L14:  Volt partitions the input 3D scene into non-overlapping volumetric patches and embeds each patch into a token with

## 星数曲线

```mermaid
xychart-beta
    title "YilmazKadir/Volt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 191 --> 196
    line [192, 194, 195]
```

2026-10-18 192 → 2026-10-22 195（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2b27006ec614` · [字段定义](../../DATASET.md)*
