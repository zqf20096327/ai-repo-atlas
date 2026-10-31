# osqp/osqp-r

⭐ 16 · R · Apache-2.0 · 推送 2026-02-28 · [GitHub](https://github.com/osqp/osqp-r) · [官网](https://osqp.org/) · 组织维护

**OSQP 二次规划求解器的 R 语言接口**

为 OSQP（Operator Splitting Quadratic Program）求解器提供 R 语言绑定。OSQP 是数值优化包，求解形如 minimize 0.5x'Px + q'x，受 l <= Ax <= u 约束的凸二次规划问题，其中 P 为半正定矩阵。R 用户可在 R 环境中调用该求解器处理带线性约束的 QP 问题。项目带有 R-CMD-check 与 CRAN 状态徽章，接口文档另行提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OSQP 求解器的 R 绑定
- 支持半正定目标矩阵与线性约束的 QP 求解
- 通过 CRAN 分发，带 R-CMD-check 检查

## 适用场景

- 在 R 中求解带线性约束的凸二次规划问题
- lasso 等优化任务中调用 OSQP 求解器

## 场景标签

 · 领域:数值优化/R 语言包

## 证据(README 行号)

> L7: Provides R-bindings to OSQP: the Operator
> L8: Splitting QP Solver.

## 星数曲线

```mermaid
xychart-beta
    title "osqp/osqp-r 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `9af525544c63` · [字段定义](../../DATASET.md)*
