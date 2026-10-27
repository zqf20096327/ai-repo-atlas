# djene-mengistu/dseg_models

⭐ 25 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/djene-mengistu/dseg_models) · 个人维护

**钢材表面缺陷分割的深度学习模型实现与对比实验代码库**

论文配套代码库：实现多种深度学习图像分割方法（CNN 系与 transformer 系）用于钢材表面缺陷分割，在 NEU-Seg 与 Severstal Steel Defect Detection（SSDD）两个公开数据集上按分割精度、处理时间与计算复杂度做对比评估；并提出 transformer 编码器 + CNN（UperNet 式、含 PPM）解码器的混合网络，报告 Dice 95.22%（NEU-Seg）与 95.55%（SSDD）。README 提供数据目录结构说明与论文链接，面向工业检测方向的科研与开发者。未给出安装命令或环境依赖清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多种 CNN 与 transformer 分割方法的对比实验（精度/时间/复杂度）
- 提出 transformer 编码器 + CNN 解码头的混合网络
- 在 NEU-Seg 与 SSDD 两个公开数据集上评估
- 附带 Springer 论文全文链接与 BibTeX 引用

## 适用场景

- 复现论文中的钢材缺陷分割对比实验
- 工业检测中选型缺陷分割模型时参考性能结果
- 基于混合 transformer-CNN 架构做分割模型改进研究

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # Deep learning-based automated steel surface defect segmentation: A comparative experimental study
> L3: The use of machine vision and deep learning for intelligent industrial inspection has become increasingly important 

## 星数曲线

```mermaid
xychart-beta
    title "djene-mengistu/dseg_models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `88e0b3f3161a` · [字段定义](../../DATASET.md)*
