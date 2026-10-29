# Lakonik/GMFlow

⭐ 199 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/Lakonik/GMFlow) · [官网](https://arxiv.org/abs/2504.05304) · 组织维护

**ICML 2025 论文 GMFlow 官方实现：高斯混合流匹配生成模型**

论文《Gaussian Mixture Flow Matching Models》的官方 PyTorch 实现，由 Stanford、Adobe Research 与 Hillbot 研究者发表。将扩散/流匹配模型的输出层扩展为预测流速的高斯混合分布，提供 GM-SDE 与 GM-ODE 求解器实现少步采样，并引入概率化 CFG 缓解过饱和。提供 Diffusers 推理 pipeline、ImageNet 256x256 训练/评测脚本与 2D 棋盘玩具模型；训练需 CUDA 与多 GPU。已并入 pi-Flow 代码库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网络输出层扩展为高斯混合分布，标准扩散/流匹配为其单分量特例
- GM-SDE 与 GM-ODE 求解器实现精确少步采样
- 概率化 CFG 缓解过饱和问题
- 提供 Diffusers 推理 pipeline 与 ImageNet 训练/评测脚本

## 适用场景

- 复现论文中的 ImageNet 256x256 图像生成实验
- 在 GMFlow 基础上开展流匹配生成模型研究
- 基于玩具模型学习高斯混合流匹配的训练机制

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L3: Official PyTorch implementation of the paper:
> L29: - **Gaussian Mixture Output**: GMFlow expands the network's output layer to predict a Gaussian mixture (GM) distrib

## 星数曲线

```mermaid
xychart-beta
    title "Lakonik/GMFlow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 197 --> 200
    line [198, 199, 199]
```

2026-10-18 198 → 2026-10-29 199（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c756fcbb4afa` · [字段定义](../../DATASET.md)*
