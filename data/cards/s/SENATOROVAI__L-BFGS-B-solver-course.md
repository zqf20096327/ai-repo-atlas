# SENATOROVAI/L-BFGS-B-solver-course

⭐ 16 · Jupyter Notebook · MIT · 推送 2026-03-17 · [GitHub](https://github.com/SENATOROVAI/L-BFGS-B-solver-course) · [官网](https://SenatorovAI.com) · 个人维护

**面向科研与教学的 L-BFGS/L-BFGS-B 算法课程与实现**

覆盖 L-BFGS/L-BFGS-B 拟牛顿优化算法的研究型课程仓库：从割线条件推导 BFGS 更新、证明正定性与超线性收敛，给出 two-loop recursion 与 Wolfe 线搜索的完整理论处理；同时提供纯 Python/NumPy 的求解器实现，含 L-BFGS-B 盒约束处理，并与 SciPy 及 Nocedal 等人的原 Fortran 实现做对照。基准实验包含二次函数、病态问题、逻辑回归与高维合成数据集，与梯度下降、牛顿法、共轭梯度比较。面向研究第二阶优化方法的研究者、ML 工程师与学生，要求线性代数、多元微积分与数值优化基础。README 未给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从割线条件完整推导 BFGS 更新并证明正定性与超线性收敛
- 纯 Python/NumPy 实现，含 two-loop recursion、Wolfe 线搜索与 L-BFGS-B 盒约束
- 与 SciPy 及原 Fortran L-BFGS-B 实现做参考对照
- 基准实验覆盖病态问题、逻辑回归与高维合成数据集

## 适用场景

- 系统学习 L-BFGS/L-BFGS-B 的理论与收敛性证明
- 查阅 two-loop recursion 与 Wolfe 线搜索的可运行参考实现
- 将求解器用于大规模无约束与盒约束光滑优化实验

## 场景标签

`教程课程` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: Research-oriented course and implementation of the **L-BFGS / LBFGSB quasi-Newton optimization algorithm**.
> L40: > A mathematically rigorous course on the **Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS)** algorithm, c

## 星数曲线

```mermaid
xychart-beta
    title "SENATOROVAI/L-BFGS-B-solver-course 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `78dbb7073ec4` · [字段定义](../../DATASET.md)*
