# romainkp/stremr

⭐ 41 · R · MIT · 推送 2026-02-17 · [GitHub](https://github.com/romainkp/stremr) · 组织维护

**纵向数据因果推断 R 包：估计静态/动态/随机干预下的反事实结局**

R 语言统计分析包，面向带时变混杂与信息性右删失的纵向数据，估计静态、动态或随机干预下的期望反事实结局（连续或二分类生存结局）。提供 IPW、G-formula、TMLE 系列及无限维 TMLE 等估计器，可对删失、暴露与监测机制分别拟合倾向得分模型，默认逻辑回归，也可经 sl3/gridisl 使用 xgboost、h2o 等机器学习算法并通过 Super Learning 做模型集成选择。输入要求长格式数据并遵循固定列序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IPW/KM-MSM/GCOMP/TMLE/CVTMLE/iTMLE 等多类估计器
- 支持时变混杂与信息性右删失的调整
- 经 sl3 与 gridisl 支持机器学习算法与 Super Learner 集成选择
- 倾向得分模型可按时间或自定义逻辑表达式分层拟合

## 适用场景

- 估计治疗干预下的反事实生存曲线与风险差
- 处理纵向数据中的时变混杂与右删失偏倚
- 用 Super Learner 对结局与暴露模型做数据自适应拟合

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: > Analysis of longitudinal data, with continuous or time-to-event
> L85: - Alternatively, model fitting can be performed via any machine

## 星数曲线

```mermaid
xychart-beta
    title "romainkp/stremr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dc596705ff20` · [字段定义](../../DATASET.md)*
