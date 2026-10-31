# Cyr-Ch/Diffusion-101

⭐ 14 · Jupyter Notebook · MIT · 推送 2025-11-17 · [GitHub](https://github.com/Cyr-Ch/Diffusion-101) · 个人维护

**扩散模型从零构建与训练的入门教程仓库**

面向初学者的扩散模型教学仓库：用分步 Markdown 指南与 Jupyter 交互笔记本讲解扩散模型数学原理、U-Net 架构实现、ε-prediction 训练与采样生成，附带基于 PyTorch 的完整实现，支持 DDIM、Heun、DPM-Solver（Karras sigmas）三种采样算法。数据集自动下载 CIFAR-10，提供 small/medium/large/custom 四档模型配置，训练既可在笔记本中完成也可通过 scripts/train.py 配置脚本运行。要求 Python 3.8+，建议 GPU，小模型可用 CPU。

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

- 从零实现扩散模型：U-Net 骨干与 ε-prediction 训练
- 三种采样算法：DDIM、Heun、DPM-Solver（Karras sigmas）
- 4 个交互式 Jupyter 笔记本，自动下载并预处理 CIFAR-10
- small/medium/large/custom 四档模型配置与可配置训练脚本

## 适用场景

- 系统学习扩散模型的原理与实现
- 在 MNIST/CIFAR-10 上亲手训练扩散模型
- 对比实验不同采样算法的生成效果

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L23: - Implementing a diffusion model from scratch with U-Net architecture
> L25: - Generating images with multiple sampling algorithms (DDIM, Heun, DPM-Solver with Karras sigmas)

## 星数曲线

```mermaid
xychart-beta
    title "Cyr-Ch/Diffusion-101 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `44d4e1177931` · [字段定义](../../DATASET.md)*
