# mlr-org/mlr3measures

⭐ 13 · R · LGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/mlr-org/mlr3measures) · [官网](https://mlr3measures.mlr-org.com) · 组织维护

**R 包：为 mlr3 提供 40+ 种监督学习性能度量**

mlr3 生态的 R 包，实现 40 余种用于回归与分类任务的监督学习性能度量，并可查询度量的元信息（如最优与最差可能得分）。内部使用 checkmate 做参数检查，无其他运行时依赖。面向 mlr3 用户与 R 开发者：在 mlr3 中使用这些度量无需显式加载本包，包作者建议通过 requireNamespace() 与 :: 操作符访问以避免命名空间冲突。发布于 CRAN。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 余种回归与分类性能度量
- 可查询度量的元信息（最优/最差可能得分）
- 仅依赖 checkmate，无其他运行时依赖

## 适用场景

- 在 mlr3 中评估监督学习模型性能
- 查询性能度量的取值范围等元信息
- 作为独立 R 包在其他项目中复用度量实现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: Implements multiple performance measures for supervised learning.
> L11: Includes over 40 measures for regression and classification.

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3measures 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e46f8519305e` · [字段定义](../../DATASET.md)*
