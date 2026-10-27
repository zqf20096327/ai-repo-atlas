# bentherien/parametricScatteringNetworks

⭐ 30 · Python · BSD-3-Clause · 推送 2025-11-10 · [GitHub](https://github.com/bentherien/parametricScatteringNetworks) · 组织维护

**CVPR'22 论文代码：可学习散射网络的小样本图像分类**

Parametric Scattering Networks（CVPR 2022 Oral）官方代码库：把 Morlet 小波散射网络的滤波器参数设为可学习（支持 tight-frame/随机初始化），可与线性层或 Wide Residual Network 组成混合架构，面向小样本图像分类。提供在 CIFAR-10（100 样本挑战）、KTH-TIPS2、COVIDx CRX-2 三个数据集上复现实验的脚本，结果自动记录到 MLflow，并含形变鲁棒性评测脚本。注意：Kymatio 更新已使仓库内实现失效，作者另提供 2024 年 4 月更新的教程 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可学习 Morlet 小波滤波器的散射网络（tight-frame/随机初始化）
- 100 样本 CIFAR-10 挑战脚本与确定性种子控制
- 覆盖 CIFAR-10/KTH-TIPS2/COVIDx CRX-2 的实验复现脚本，结果记录到 MLflow
- 散射表示对形变稳定性的经验评测脚本

## 适用场景

- 复现论文实验或在小样本图像分类任务上使用散射混合架构
- 在 100 样本 CIFAR-10 设定下对比自己的架构
- 研究可学习散射滤波器的优化过程与形变鲁棒性

## 场景标签

 · 领域:机器学习/图像分类

## 证据(README 行号)

> L3: This repository contains the code for Parameteric Scattering Networks. It also contains code to run and test new hyb
> L64: Our empirical evaluations are based on three image datasets, illustrated in the Figure below. We subsample each dat
> L135:  │ ├── models <- Contains all the pytorch NN.modules for this project.

## 星数曲线

```mermaid
xychart-beta
    title "bentherien/parametricScatteringNetworks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8eef1d5889fb` · [字段定义](../../DATASET.md)*
