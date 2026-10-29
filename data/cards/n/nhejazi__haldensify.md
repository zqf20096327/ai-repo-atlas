# nhejazi/haldensify

⭐ 19 · R · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/nhejazi/haldensify) · [官网](https://codex.nimahejazi.org/haldensify) · 个人维护

**R 包：基于 Highly Adaptive Lasso 的非参数条件密度估计**

面向因果推断研究者的 R 统计包：通过 pooled hazards 回归在变量条件支撑上恢复条件密度估计，专用于估计连续处理的广义倾向得分（generalized propensity score），并基于 HAL 条件密度估计族提供达到半参数效率界的非参数逆概率加权（IPW）估计量。仅支持与 highly adaptive lasso（内部使用 hal9001）配合使用。通过 CRAN 或 GitHub 安装，提供 predict 方法对新数据输出密度预测，附带 vignette 与 JOSS 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pooled hazards 回归恢复非参数条件密度估计
- 估计连续处理的广义倾向得分
- 基于 HAL 估计族的 IPW 因果效应估计（沿正则化路径欠平滑）
- 提供 predict 方法与 CV-risk 可视化

## 适用场景

- 因果推断中估计连续暴露的广义倾向得分
- 构建连续处理的逆概率加权估计量
- 训练 HAL 模型并对新数据输出条件密度预测

## 场景标签

 · 领域:统计学/因果推断机器学习

## 证据(README 行号)

> L27: The `haldensify` R package is designed to provide facilities for
> L38: Hejazi 2020). `haldensify` implements this conditional density

## 星数曲线

```mermaid
xychart-beta
    title "nhejazi/haldensify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bfb99f0ebc54` · [字段定义](../../DATASET.md)*
