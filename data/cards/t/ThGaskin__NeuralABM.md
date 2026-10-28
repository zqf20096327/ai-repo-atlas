# ThGaskin/NeuralABM

⭐ 34 · Jupyter Notebook · 推送 2026-02-12 · [GitHub](https://github.com/ThGaskin/NeuralABM) · 个人维护

**科研用户的多智能体模型神经参数校准与混合神经建模工具集**

用神经网络将多智能体 ODE/SDE/PDE 模型校准到数据，估计方程参数（含邻接矩阵）的边缘密度。仓库按模型组织（SIR、SIRS、Kuramoto、Laser 等），每个模型含 Jupyter notebook 示例；配合 utopya 包实现并行集成训练与不确定性量化，自动保存配置、数据与绘图。代码对应多篇 PNAS/PNAS Nexus/arXiv 论文并按论文版本发布。utopya 在 Unix 系统完整支持，Windows 为开发分支；CUDA 加速需额外安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 神经网络校准 ODE/SDE/PDE 并估计参数边缘密度
- 基于 utopya 的并行集成训练不确定性量化
- 多模型示例（SIR/SIRS/Kuramoto/Laser 等）配 Jupyter notebook
- 按论文版本发布以复现出版物图表

## 适用场景

- 校准流行病学或耦合振荡器等机理模型参数
- 从时间序列推断网络邻接矩阵
- 复现论文图表并做不确定性量化实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: This project calibrates multi-agent ODEs, SDEs, and PDEs to data using a neural network, and presents general exper
> L14: We estimate marginal densities on the equation parameters, including adjacency matrices.
> L29: The repository is organised into *models*, which are defined as mechanistic equations (e.g. the SIR model)

## 星数曲线

```mermaid
xychart-beta
    title "ThGaskin/NeuralABM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0264d95a57a0` · [字段定义](../../DATASET.md)*
