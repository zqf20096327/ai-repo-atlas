# qiauil/torchfsm

⭐ 62 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/qiauil/torchfsm) · [官网](https://qiauil.github.io/torchfsm/) · 组织维护

**基于 PyTorch 的傅里叶谱方法 PDE 求解库**

TorchFSM 是用傅里叶谱方法求解偏微分方程的 PyTorch 库，面向物理驱动的深度学习与可微仿真。提供散度、梯度、对流等模块化数学算子，可组合构建自定义求解器；同一算子可直接在 1D/2D 网格上仿真。支持 GPU 加速与批量仿真（不同初始条件），全程可微，可接入残差算子、可微物理或数据集生成等机器学习流程。由慕尼黑工业大学基于物理仿真小组维护，另有 Jax 替代项目 Exponax。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 傅里叶谱方法求解 PDE 的模块化算子体系（散度/梯度/对流等）
- GPU 加速与批量仿真（参数扫描/不确定性量化/集成分析）
- 全程可微，可与机器学习工作流集成（残差算子/可微物理/数据集生成）

## 适用场景

- 用谱方法快速求解 1D-3D PDE 并做 GPU 加速仿真
- 在可微仿真中做参数扫描或不确定性量化
- 为物理驱动的深度学习生成数据集或构建残差算子

## 场景标签

 · 领域:科学计算/物理仿真

## 证据(README 行号)

> L21: `TorchFSM` is a PyTorch-based library for solving PDEs using Fourier spectral method. It is designed for physics-ba
> L57: * **Differentiable and ML-ready**: Fully differentiable by design, TorchFSM integrates naturally with machine learn
> L82: * `TorchFSM` is mainly built by Qiang Liu, Felix Koehler, and Nils Thuerey at Physics Based Simulation Group, Techn

## 星数曲线

```mermaid
xychart-beta
    title "qiauil/torchfsm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-25 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2f171026a463` · [字段定义](../../DATASET.md)*
