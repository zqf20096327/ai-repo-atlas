# tonyzyl/DiffusionReconstruct

⭐ 34 · Python · Apache-2.0 · 推送 2026-03-22 · [GitHub](https://github.com/tonyzyl/DiffusionReconstruct) · 个人维护

**稀疏观测下全球物理场重建的跨注意力扩散模型代码库**

论文 "Spatially-Aware Diffusion Models with Cross-Attention for Global Field Reconstruction with Sparse Observations"（CMAME 接收）的官方代码。提出跨注意力扩散模型，用 Voronoi 剖分场作为归纳偏置，通过 FiLM 调制融合插值场与传感位置信息；对比 Guided Sampling、CFG 等条件化方法与 VT-UNet 确定性基线，测试 Darcy 流、扩散反应、浅水与可压缩 Navier-Stokes 四类 PDE 数据集。提供 requirements.txt 安装、accelerate 分布式训练脚本、Colab Demo 与 HuggingFace 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨注意力条件编码块结合 Voronoi 剖分与 FiLM 调制
- 基准对比 Guided Sampling / CFG / VT-UNet / 数值方法（nRMSE 与计算成本）
- 覆盖 Darcy 流、浅水、扩散反应、可压缩 Navier-Stokes 四类 PDE
- 集成采样协方差可增强数据同化精度

## 适用场景

- 复现论文中的稀疏观测场重建实验
- 训练/微调跨注意力扩散模型用于科学计算场重建
- 比较概率式扩散重建与确定性基线的噪声鲁棒性
- 用扩散集合协方差改进数据同化流程

## 场景标签

 · 领域:科学计算/AI for Science

## 证据(README 行号)

> L10: * We propose a cross-attention diffusion model for global field reconstruction.
> L15: * The tested PDEs include Darcy flow, diffusion-reaction, shallow water equations and compressible Navier-Stokes eq
> L5: This repository contains the code for the paper "Spatially-Aware Diffusion Models with Cross-Attention for Global Fi

## 星数曲线

```mermaid
xychart-beta
    title "tonyzyl/DiffusionReconstruct 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `da1e0f2c6876` · [字段定义](../../DATASET.md)*
