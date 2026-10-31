# Wuyxin/DISC

⭐ 46 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/Wuyxin/DISC) · [官网](https://arxiv.org/abs/2305.00650) · 组织维护

**ICML 2023 论文官方代码：训练中自动发现并消除图像分类的伪相关**

DISC 是 ICML 2023 论文 Discover and Cure 的 PyTorch 官方实现：在图像分类训练过程中，利用 Stable Diffusion 生成的概念库，按概念敏感度逐迭代发现导致伪相关的概念，并将其合成图像混入训练集以平衡数据、更新模型参数，同时输出各属性对伪相关的贡献解释。支持 MetaShift、Waterbirds、FMoW、ISIC 四个数据集，提供预生成概念库下载与自定义概念库生成脚本，以及 ERM/DISC 训练命令。限制：面向科研复现，无打包发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 概念敏感度驱动的伪相关概念自动发现与移除
- 概念库由 Stable Diffusion v1-4 生成，可下载预生成版本或自定义
- 逐迭代将概念图像混入训练集形成平衡数据
- 提供 MetaShift/Waterbirds/FMoW/ISIC 四个数据集的下载与训练脚本

## 适用场景

- 复现论文中的伪相关缓解实验
- 研究图像分类模型的泛化与可解释性
- 用自定义概念库分析自己数据集中的伪相关属性

## 场景标签

 · 领域:机器学习研究/图像分类

## 证据(README 行号)

> L19: DISC is an algorithm on image classification tasks which adaptively discovers and removes spurious correlations dur
> L33: - In each iteration, discover spurious concepts by computing concept sensitivity.

## 星数曲线

```mermaid
xychart-beta
    title "Wuyxin/DISC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4f3f12e5a8bd` · [字段定义](../../DATASET.md)*
