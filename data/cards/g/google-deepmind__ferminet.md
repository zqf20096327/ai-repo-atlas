# google-deepmind/ferminet

⭐ 855 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/google-deepmind/ferminet) · 组织维护

**用神经网络计算原子分子基态波函数的从头算电子结构代码**

FermiNet 的 JAX 实现，通过变分蒙特卡洛方法学习原子与分子的高精度基态波函数，用于从头算电子结构计算。基于 ml_collections ConfigDict 配置系统与超参数，可通过命令行或自定义训练脚本运行，支持多 GPU 并行（JAX pmap 自动检测）、激发态计算（NES-VMC 与 ensemble penalty 两种方法）、推理期观测量统计（自旋、偶极矩、密度矩阵）及周期性边界条件。README 声明这是研究级发布、仍在开发中，原始 TensorFlow 实现在 tf 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 变分蒙特卡洛学习基态波函数，含 PsiFormer 自注意力架构
- 支持 NES-VMC 与 ensemble penalty 两种激发态计算方法
- 多 GPU 并行（JAX pmap，自动检测可用 GPU）
- 推理期可统计自旋、偶极矩与密度矩阵等观测量

## 适用场景

- 计算原子和分子的基态能量与波函数
- 研究分子激发态性质
- 用神经网络方法求解多电子薛定谔方程并复现论文实验

## 场景标签

 · 领域:计算化学/量子物理

## 证据(README 行号)

> L3: FermiNet is a neural network for learning highly accurate ground state
> L6: This repository contains an implementation of the algorithm and experiments

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/ferminet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 853 --> 856
    line [854, 855, 855]
```

2026-10-18 854 → 2026-10-28 855（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6861eb6eea0e` · [字段定义](../../DATASET.md)*
