# guillermo-navas-palencia/ropwr

⭐ 14 · Python · Apache-2.0 · 推送 2026-01-23 · [GitHub](https://github.com/guillermo-navas-palencia/ropwr) · [官网](http://gnpalencia.org/ropwr/) · 个人维护

**Python 分段多项式回归库：给定分割点求最优拟合**

RoPWR 是一个 Python 库，实现多种数学规划形式化方法，在给定分割点列表下计算最优的连续/不连续分段多项式回归。支持单调性约束（如 ascending/convex/valley）、四种目标函数（l1/l2/huber/quantile）与 Lasso/Ridge 正则化，并可对预测设置上下界。底层依赖 cvxpy（支持 CLARABEL、ECOS、OSQP、SCS、HIGHS 求解器），部分形式化采用直接求解。通过 PyPI 或源码安装，依赖 cvxpy、numpy、scikit-learn、scipy。

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

- 给定分割点计算最优连续/不连续分段多项式回归
- 支持单调性约束（ascending/convex/valley 等）与预测上下界
- 四种目标函数（l1/l2/huber/quantile）与 L1/L2 正则化
- 基于 cvxpy，支持 CLARABEL/ECOS/OSQP/SCS/HIGHS 求解器

## 适用场景

- 对呈现分段趋势的数据做带形状约束的回归拟合
- 风控建模中构造带单调性约束的分段特征变换
- 需要 L1/Huber 等鲁棒目标下的分段多项式拟合

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L15: The **RoPWR** library implements several mathematical programming formulations
> L19: relies on cvxpy (CLARABEL, ECOS, OSQP, SCS and HIGHS solvers) to solve the underlying optimization

## 星数曲线

```mermaid
xychart-beta
    title "guillermo-navas-palencia/ropwr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `650fb79515cc` · [字段定义](../../DATASET.md)*
