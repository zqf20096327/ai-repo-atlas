# 392781/scikit-ntk

⭐ 27 · Python · BSD-3-Clause · 推送 2026-07-30 · [GitHub](https://github.com/392781/scikit-ntk) · [官网](https://pypi.org/project/scikit-ntk/) · 个人维护

**scikit-learn 高斯过程可用的神经正切核（NTK）实现库**

Neural Tangent Kernel 的 scikit-learn 集成实现，源自一篇硕士论文及 arXiv 论文。提供 NeuralTangentKernel 核类，直接接入 sklearn.gaussian_process 模块，可与其他核组合，用于训练和预测高斯过程回归器与分类器。要求 Python>=3.8、scikit-learn>=1.0.1，pip 安装；源码构建需 Poetry>=1.2。用法示例位于 examples/usage.py。

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

- 实现 NTK 核并直接集成 sklearn.gaussian_process 模块
- 可与其他核组合用于高斯过程回归与分类
- 配套硕士论文与 arXiv 论文（2208.03761）

## 适用场景

- 在高斯过程回归/分类中使用神经正切核
- 复现或对比论文中的 NTK/Laplace 核实验

## 场景标签

 · 领域:机器学习/核方法

## 证据(README 行号)

> L5: **scikit-ntk** is implementation of the neural tangent kernel (NTK) for the `scikit-learn` machine learning library 
> L28: kernel_ntk = NTK(D=3, bias=0.01, bias_bounds=(1e-6, 1e6))

## 星数曲线

```mermaid
xychart-beta
    title "392781/scikit-ntk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2b6ee964ce9d` · [字段定义](../../DATASET.md)*
