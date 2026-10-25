# acerbilab/pyvbmc

⭐ 136 · Python · BSD-3-Clause · 推送 2026-10-24 · [GitHub](https://github.com/acerbilab/pyvbmc) · [官网](https://acerbilab.github.io/pyvbmc/) · 组织维护

**变分贝叶斯蒙特卡洛算法的 Python 实现，用于后验与模型推断**

赫尔辛基大学 Machine and Human Intelligence Group 开源的 Python 库，实现 VBMC 算法：在有限次数（可能带噪声）的似然评估预算下，同时计算模型参数的近似后验分布与对数模型证据的近似下界（ELBO），后者用于贝叶斯模型选择。适用于黑箱对数似然、评估代价约 0.1 秒以上或带噪声、参数维度 D≤10（至多 20）的连续光滑后验场景。机制上结合变分推断与贝叶斯求积，用高斯过程迭代逼近目标后验并以高斯混合变分分布匹配；支持 Torch/JAX 模型封装、PyMC 直接适配、S-VBMC 多次运行堆叠与 ArviZ 导出。需 Python 3.10+（部分集成需 3.12+）。

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

- 有限似然评估预算下同时产出近似后验与对数模型证据下界（ELBO）
- 支持带噪声目标评估与 S-VBMC 堆叠多次运行的后验
- Torch/JAX 模型封装集成与 PyMC 直接适配（PyMCTarget）
- 后验可导出为 Torch 分布或 ArviZ DataTree

## 适用场景

- 为计算代价高的贝叶斯模型做后验推断与模型选择
- 似然只能通过模拟获得或评估带噪声时的近似推断
- 将 PyMC 中代价较高的模型交给 PyVBMC 以更少评估次数推断

## 场景标签

 · 领域:科学计算/贝叶斯统计推断

## 证据(README 行号)

> L17: PyVBMC [1] is a Python implementation of the Variational Bayesian Monte Carlo (VBMC) algorithm for posterior and mo
> L206: VBMC/PyVBMC combine two machine learning techniques in a novel way:
> L210: PyVBMC iteratively builds an approximation of the true, expensive target posterior via a Gaussian process (GP), an

## 星数曲线

```mermaid
xychart-beta
    title "acerbilab/pyvbmc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 134 --> 137
    line [135, 136, 136]
```

2026-10-18 135 → 2026-10-25 136（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `69c5b89ca4b0` · [字段定义](../../DATASET.md)*
