# martenlienen/torchode

⭐ 290 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/martenlienen/torchode) · [官网](https://torchode.readthedocs.io) · 个人维护

**为 PyTorch 提供的批量并行 ODE 求解器库**

torchode 是一组单步 ODE 求解器（如 dopri5、tsit5），兼容 PyTorch 的 JIT 编译器，并支持在一个批次内按样本难度各自步长并行求解，避免不同刚性模型的性能陷阱，保证预测与批次组成无关。面向使用 PyTorch 做神经常微分方程建模的研究者与开发者，以 Python 库形式从 PyPI 提供，另有论文可引用。

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

- 提供 dopri5、tsit5 等单步 ODE 求解器
- 兼容 PyTorch JIT 编译器
- 批次内按样本自适应步长并行求解

## 适用场景

- 在 PyTorch 中求解神经常微分方程（Neural ODE）
- 批次内样本刚性差异大时保持求解性能
- 需要与批次组成无关的确定性预测结果

## 场景标签

 · 领域:科学计算/深度学习库

## 证据(README 行号)

> L5: torchode is a suite of single-step ODE solvers such as `dopri5` or `tsit5` that are
> L6: compatible with PyTorch's JIT compiler and parallelized across a batch. JIT compilation

## 星数曲线

```mermaid
xychart-beta
    title "martenlienen/torchode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 289 --> 291
    line [290, 290]
```

2026-10-18 290 → 2026-10-31 290（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4e6ab1b3d1a7` · [字段定义](../../DATASET.md)*
