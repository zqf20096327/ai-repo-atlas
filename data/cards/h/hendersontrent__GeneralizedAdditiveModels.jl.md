# hendersontrent/GeneralizedAdditiveModels.jl

⭐ 39 · Julia · MIT · 推送 2026-05-11 · [GitHub](https://github.com/hendersontrent/GeneralizedAdditiveModels.jl) · 个人维护

**Julia 语言原生实现的广义可加模型（GAM）拟合库**

在 Julia 中拟合、评估与可视化广义可加模型（GAMs）的统计建模包，面向回归分析从业者和 Julia 用户。核心接口为 gam 函数，以公式字符串指定样条项（结数、多项式阶数），默认 Normal 分布与 Identity 链接，可指定 Gamma/Poisson/Bernoulli 等分布族及 Log/Logit 等链接函数，并可控制 PIRLS 优化器、迭代次数与收敛容差。公式语法与 R 的 mgcv 包相近。README 声明包处于活跃开发中，公式尚以字符串而非宏表示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- gam 函数以公式字符串拟合样条 GAM
- 支持 Normal/Poisson/Gamma/Bernoulli 分布族
- 支持 Identity/Log/Logit 链接函数
- 可直接控制 PIRLS 优化器、迭代数与容差

## 适用场景

- 在 Julia 中对回归数据做广义可加模型拟合
- 替换 R mgcv 工作流中的建模步骤
- 对计数、偏态或二分类数据做样条回归

## 场景标签

 · 领域:统计/机器学习库

## 证据(README 行号)

> L2: Fit, evaluate, and visualise generalised additive models (GAMs) in native Julia
> L13:     mod = gam("Volume ~ s(Girth, k=10, degree=3) + s(Height, k=10, degree=3)", df)

## 星数曲线

```mermaid
xychart-beta
    title "hendersontrent/GeneralizedAdditiveModels.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-31 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cbd6fd90955d` · [字段定义](../../DATASET.md)*
