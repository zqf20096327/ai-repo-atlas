# Lukeli0425/Galaxy-Deconv

⭐ 63 · Jupyter Notebook · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Lukeli0425/Galaxy-Deconv) · [官网](https://lukeli0425.github.io/Galaxy_Deconv/) · 组织维护

**星系图像去卷积深度学习代码：用于弱引力透镜分析**

MNRAS Letters 论文的官方 PyTorch 实现，提出展开的 Plug-and-Play ADMM 网络（Unrolled_ADMM/ADMMNet）做星系图像去卷积，服务于弱引力透镜测量。提供训练与测试脚本（train.py/test.py/test_psf.py）、基于 GalSim 与 COSMOS 真实星系数据集的数据模拟流程、LSST 数据集上预训练模型及在自己的数据上使用的教程。作者来自清华大学与西北大学。

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

- 展开式 Plug-and-Play ADMM 去卷积网络的训练与测试脚本
- 基于 GalSim + COSMOS 数据集的星系图像模拟流水线
- 提供 LSST 数据集上的预训练模型与自有数据使用教程
- 支持 PSF 系统误差鲁棒性测试

## 适用场景

- 在自有星系图像上运行预训练模型做去卷积
- 复现论文训练与测试结果
- 生成自定义设置的模拟星系数据集并重新训练

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Galaxy Image Deconvolution for Weak Gravitational Lensing with Unrolled Plug-and-Play ADMM
> L39: python train.py --model Unrolled_ADMM --n_iters 8 --n_epochs 50 --loss MultiScale --lr 1e-4

## 星数曲线

```mermaid
xychart-beta
    title "Lukeli0425/Galaxy-Deconv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-28 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3ba7868d2c3a` · [字段定义](../../DATASET.md)*
