# nianticspatial/scr-priors

⭐ 22 · Shell · NOASSERTION · 推送 2025-11-10 · [GitHub](https://github.com/nianticspatial/scr-priors) · [官网](https://nianticspatial.github.io/scr-priors/) · 组织维护

**ICCV 2025 论文代码：场景坐标重建的深度先验（扩散/Laplace）**

Niantic Spatial 发布的 ICCV 2025 论文《Scene Coordinate Reconstruction Priors》配套代码：提供复现论文主要实验的 shell 脚本、3D 点云扩散先验训练代码、Laplace 深度先验拟合脚本及对应 conda 环境文件。需先检出 ACE0 代码库并安装其 ace0 环境与 DSAC* C++/Python 绑定，扩散先验另有额外依赖。支持 ScanNet、Indoor-6、7Scenes 数据集实验，提供预训练扩散先验模型，训练在单 GPU 上约半天（V100）。论文主要贡献已集成进 ACE0 主库（默认关闭）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供复现论文 Table 1-3 实验的 shell 脚本
- 3D 点云扩散先验训练与预训练模型
- Laplace 深度先验拟合脚本
- ScanNet / Indoor-6 / 7Scenes 三套数据集实验流程

## 适用场景

- 复现 ICCV 2025 论文实验结果
- 为 ACE0/ACE 重定位与重建训练深度先验
- 在 ScanNet 上重训自己的 3D 扩散先验

## 场景标签

 · 领域:计算机视觉/三维重建与重定位

## 证据(README 行号)

> L3: This repository contains code associated to the paper:
> L22: * Scripts to replicate the main results of the experiments
> L23: * Code to train a 3D point cloud diffusion prior

## 星数曲线

```mermaid
xychart-beta
    title "nianticspatial/scr-priors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c1e60e61282d` · [字段定义](../../DATASET.md)*
