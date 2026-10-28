# GeoBrain-Project/GeoBrain

⭐ 87 · Python · Apache-2.0 · 推送 2026-08-20 · [GitHub](https://github.com/GeoBrain-Project/GeoBrain) · [官网](https://geobrain-project.github.io/GeoBrain/) · 组织维护

**面向地下综合建模的可微分贝叶斯科学计算平台**

GeoBrain 是开源的模块化科研平台，为地下综合建模提供端到端可微分工作流：以 ForwardOperator 与可微性契约组织地质统计、岩石物理、地震、电磁、位场与油藏流动等多物理过程，用 @ 组合算子链；同一 InverseProblem 对象既可运行确定性反演优化器，也可切换为后验采样（HMC/NUTS/Langevin/SVD）做不确定性量化，并支持深度神经网络参数化与信息价值决策分析。面向科研用户，Python 3.10+、PyTorch 2.0+ 环境下源码安装，示例可在 CPU 上运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 算子契约 + 可微性声明（autograd/隐式伴随/手写 VJP，经有限差分校验）
- 同一 InverseProblem 支持确定性优化与贝叶斯后验采样（HMC/NUTS/Langevin/SVGD）
- 多物理（地质统计/地震/电磁/位场/流动）在一张计算图中可微组合
- 信息价值（EoI）决策：在测量前对测井方案逐单元估价

## 适用场景

- 做地球物理联合反演并量化不确定性
- 将深度神经网络参数化接入物理反演链
- 决定下一口井/测量布在哪里，先估价再测量
- 开发新的多物理算子并复用平台反演与采样框架

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: **GeoBrain** is an open, modular, and extensible platform for **Geo**scientific **B**ayesian **R**easoning with **A
> L14: By combining **differentiable physics**, **Bayesian inference**, and **deep learning**, GeoBrain enables end-to-end
> L30: - **Differentiable Multiphysics Modeling**: geostatistics, rock physics, seismic, electromagnetics, potential field

## 星数曲线

```mermaid
xychart-beta
    title "GeoBrain-Project/GeoBrain 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-28 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f0a30561e520` · [字段定义](../../DATASET.md)*
