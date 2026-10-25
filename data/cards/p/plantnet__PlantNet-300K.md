# plantnet/PlantNet-300K

⭐ 269 · Python · BSD-2-Clause · 推送 2026-10-12 · [GitHub](https://github.com/plantnet/PlantNet-300K) · [官网](https://doi.org/10.5281/zenodo.5645731) · 组织维护

**植物图像数据集与基准代码：30 万张图、1081 物种**

Pl@ntNet-300K 论文（NeurIPS Datasets and Benchmarks 2021）配套仓库，提供论文基准实验代码及数据集入口：306,146 张植物图像覆盖 1081 个物种，划分为 train/val/test（243,916/31,118/31,112），具有高类别歧义与长尾分布（80% 物种仅占 11% 图像）。数据集本体托管于 Zenodo（需用 1.1 版元数据），仓库另提供元数据 JSON、论文超参数位置、预训练模型加载方式（load_model），及基于 PyTorch 的训练命令（main.py）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 306,146 张植物图像、1081 物种，长尾分布（80% 物种仅占 11% 图像）
- 提供 train/val/test 划分与三类元数据 JSON 映射文件
- 预训练模型（如 resnet18）可通过 utils.py 的 load_model 加载
- 给出复现基准的 main.py 训练命令与超参数出处

## 适用场景

- 在长尾分布的植物图像数据上训练与评测分类模型
- 复现 NeurIPS 2021 论文的基准实验
- 加载预训练权重并迁移到其他植物分类数据集

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the code used to produce the benchmark in the paper ***"Pl@ntNet-300K: a plant image datase
> L24: Pl@ntNet-300K is a plant dataset containing 306,146 plant images covering 1081 species (the classes).

## 星数曲线

```mermaid
xychart-beta
    title "plantnet/PlantNet-300K 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-25"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-22 269 → 2026-10-25 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9cbd719c3033` · [字段定义](../../DATASET.md)*
