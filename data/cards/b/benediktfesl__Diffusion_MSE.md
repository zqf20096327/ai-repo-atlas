# benediktfesl/Diffusion_MSE

⭐ 15 · Python · BSD-3-Clause · 推送 2026-05-14 · [GitHub](https://github.com/benediktfesl/Diffusion_MSE) · 个人维护

**扩散模型 MSE 最优性论文的仿真复现代码（DMSE 调度器）**

复现 AISTATS 2025 论文《On the Asymptotic Mean Square Error Optimality of Diffusion Models》仿真结果的科研代码库：训练与评估基于 DPM 的去噪器、评估 GMM 基线（CME/LS），支持 rand_gmm、MNIST、Fashion-MNIST、音频四类数据。需要 CUDA 11.8 与 PyTorch 2.0.1 环境，从外部链接下载预训练模型与数据。另提供独立 PyPI 包 diffusers-dmse（diffusers 兼容版调度器），但未在本仓库中直接使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练/评估 DPM 去噪器与 GMM 基线（CME/LS）的实验脚本
- 支持 MNIST、Fashion-MNIST、音频等多类数据
- 提供独立 PyPI 包 diffusers-dmse（diffusers 兼容调度器）
- 外部链接提供数据与预训练模型下载

## 适用场景

- 复现论文的仿真实验结果
- 基于 DMSE 调度器开展扩散模型去噪研究
- 对比 MSE 最优估计与基线方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Implementation to reproduce the simulation results of the paper
> L18: This repository contains the original research implementation used for the experiments in the paper.

## 星数曲线

```mermaid
xychart-beta
    title "benediktfesl/Diffusion_MSE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `6c252912abf8` · [字段定义](../../DATASET.md)*
