# cake-lab/HybridDepth

⭐ 175 · Jupyter Notebook · GPL-3.0 · 推送 2026-02-17 · [GitHub](https://github.com/cake-lab/HybridDepth) · 组织维护

**基于焦面堆栈图像的度量深度估计模型（WACV 2025）**

HybridDepth 的官方实现：输入相机拍摄的焦面堆栈（focal stack）图像，结合深度对焦（DFF）分支与单图先验精炼层，输出度量深度图。提供 4 个预训练模型（NYU Depth V2 / DDFF 数据集，5 或 10 帧焦面堆栈），支持 TorchHub 一行加载与本地 conda 安装两种方式；本地推理需下载权重并用 checkpoint 加载到 CUDA，另提供 config.yaml 驱动的评测与训练流程（训练需安装 CUDA 合成包）。限制：prepare_input_image 目前仅支持 .jpg 输入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 焦面堆栈 + 单图先验的深度融合模型，官方实现
- TorchHub 直接加载 4 个预训练模型
- 提供 NYU V2 / DDFF12 / ARKitScenes 三个数据集的评测配置
- 支持训练（含 CUDA 图像合成包）与推理流程

## 适用场景

- 用焦面堆栈图像生成度量深度图
- 在 NYU V2 / DDFF12 / ARKitScenes 上复现论文评测
- 基于预训练权重微调自己的深度估计模型

## 场景标签

 · 领域:计算机视觉/深度估计

## 证据(README 行号)

> L13: This work presents HybridDepth. HybridDepth is a practical depth estimation solution based on focal stack images ca
> L36: * `HybridDepth_NYU5`: Pre-trained on the NYU Depth V2 dataset using a 5-focal stack input, with both the DFF branch

## 星数曲线

```mermaid
xychart-beta
    title "cake-lab/HybridDepth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 174 --> 176
    line [175, 175]
```

2026-10-18 175 → 2026-10-29 175（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8c90974917c4` · [字段定义](../../DATASET.md)*
