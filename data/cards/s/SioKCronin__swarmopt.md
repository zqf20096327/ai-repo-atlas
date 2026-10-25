# SioKCronin/swarmopt

⭐ 37 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/SioKCronin/swarmopt) · 个人维护

**Python 群体智能优化算法库：PSO 变体求解成本函数优化**

以 Python 实现的群体优化算法库：提供全局最优/局部最优/统一/模拟退火/协同 PSO 及马群优化等 7 种单目标算法与多目标 PSO，附带 Sphere、Rosenbrock、ZDT/DTLZ 等基准函数。支持 8 种惯性权重策略与 11 种速度钳制变体，可传 seed 实现可复现运行（不触碰全局随机状态）。面向需要参数/结构优化的开发与科研用户，提供基准评测驱动脚本与测试套件；DMSPSO 算法正在重做，0.3 版不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 种单目标群智能算法 + 多目标 PSO
- 8 种惯性权重策略与 11 种速度钳制变体
- seed 参数实现确定性可复现，不污染全局随机状态
- 内置单目标/多目标基准函数与分层基准评测脚本

## 适用场景

- 为神经网络层数与权重做优化
- 求解通信网络路由等组合优化问题
- 用标准基准函数比较不同 PSO 变体性能

## 场景标签

 · 领域:优化算法/机器学习

## 证据(README 行号)

> L5: SwarmOpt is a library of swarm optimization algorithms implemented in Python.
> L66: * Global Best PSO - Kennedy & Eberhart 1995

## 星数曲线

```mermaid
xychart-beta
    title "SioKCronin/swarmopt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b678ed9d63e9` · [字段定义](../../DATASET.md)*
