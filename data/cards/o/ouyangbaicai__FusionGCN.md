# ouyangbaicai/FusionGCN

⭐ 14 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ouyangbaicai/FusionGCN) · [官网](https://www.sciencedirect.com/science/article/pii/S0957417424025326) · 组织维护 · 中文 README

**多焦点图像融合的 PyTorch 官方实现（GCN+CNN）**

论文 FusionGCN（ESWA 2025）的官方 PyTorch 代码：用超像素特征生成 GCN 与像素级特征重建 CNN 完成多焦点图像融合，面向计算资源受限设备。提供 train.py 训练与 inference.py 推理脚本，内置 Lytro、MFFW、MFI-WHU、GrayScale 四个数据集，替换数据集名称即可运行，结果输出到 ./Result 目录。代码在 MFFT (EAAI 2024) 基础上构建。依赖 python>=3.6、pytorch>=1.5.0、CUDA>=12.0。

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

- GCN 用于多焦点图像融合（作者称为首次）
- 超像素特征生成 GCN + 像素级特征重建 CNN 结构
- 提供 Lytro/MFFW/MFI-WHU/GrayScale 四个测试数据集
- 面向计算资源受限设备的轻量级设计

## 适用场景

- 我在资源受限设备上做多焦点图像融合任务
- 复现或引用 FusionGCN 论文实验结果
- 在 Lytro/MFFW/MFI-WHU 等数据集上对比融合方法

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: #### Code for paper “FusionGCN: Multi-focus image fusion using superpixel features generation GCN and pixel-level fe
> L22: - To our knowledge, this is the first time that GCN has been used to solve the problem of multi-focus image fusion.

## 星数曲线

```mermaid
xychart-beta
    title "ouyangbaicai/FusionGCN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bb1ae7987816` · [字段定义](../../DATASET.md)*
