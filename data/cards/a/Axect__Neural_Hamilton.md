# Axect/Neural_Hamilton

⭐ 14 · Python · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Axect/Neural_Hamilton) · [官网](https://arxiv.org/abs/2410.20951) · 个人维护

**论文官方实现：用神经算子学习求解哈密顿力学方程**

"Neural Hamilton" 论文的官方代码实现：将哈密顿方程重构为算子学习问题，在不显式求解微分方程的前提下用神经网络学习哈密顿系统动力学。提供 DeepONet、VaRONet、TraONet、MambONet 四种架构，用高斯随机场与三次 B 样条生成物理合理的势函数数据，并与 Yoshida 四阶、RK4 数值方法对比，在简谐振子、双阱、Morse 等势上评测。面向科研复现者，安装需 Rust/Cargo、Python 3.8+、uv、just，用 just all 一键完成数据生成与依赖安装，CUDA 为可选 GPU 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种神经算子架构（DeepONet/VaRONet/TraONet/MambONet）
- 高斯随机场+B 样条生成物理合理势函数数据
- 与 Yoshida 4 阶、RK4 传统数值方法对比评测
- 覆盖简谐振子、双阱、Morse 及不可微势外推测试

## 适用场景

- 复现论文中的神经算子求解哈密顿方程实验
- 比较神经算子与 RK4 数值方法在长时间演化上的精度
- 基于该框架研究新的算子学习架构

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: Neural Hamilton reformulates Hamilton's equations as an operator learning problem, exploring whether artificial inte
> L13: - Multiple neural network architectures (DeepONet, TraONet, VaRONet, MambONet) for solving Hamilton's equations

## 星数曲线

```mermaid
xychart-beta
    title "Axect/Neural_Hamilton 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2fac04185610` · [字段定义](../../DATASET.md)*
