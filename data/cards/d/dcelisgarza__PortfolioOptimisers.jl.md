# dcelisgarza/PortfolioOptimisers.jl

⭐ 25 · Julia · MIT · 推送 2026-10-26 · [GitHub](https://github.com/dcelisgarza/PortfolioOptimisers.jl) · [官网](https://dcelisgarza.github.io/PortfolioOptimisers.jl/stable/) · 个人维护

**Julia 投资组合优化库：50+风险度量与多种组合构造算法**

面向量化金融开发者与研究者的 Julia 组合优化库。以可组合的不可变估计器构成：先验（含四种 Black-Litterman 变体与熵池化）、超过 50 种风险度量（CVaR/EVaR/RLVaR/回撤/OWA 等）、协方差估计与去噪，优化器覆盖均值-风险、风险预算、层次风险平价、HERC、嵌套聚类优化等。基于 JuMP 构建数学规划问题，可对接任意 JuMP 支持的求解器（如 Clarabel、HiGHS），库本身不附带求解器；支持 walk-forward 与组合交叉验证及超参数搜索。为 Julia 注册包，经 Pkg 安装。README 声明内容不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+ 种风险度量（CVaR、EVaR、RLVaR、回撤、OWA 等）
- 层次风险平价、HERC、嵌套聚类优化、风险预算等优化器
- 四种 Black-Litterman 变体与熵池化观点融入
- 基于 JuMP，可使用任意 JuMP 支持的求解器

## 适用场景

- 在 Julia 中构建最小方差或均值-风险投资组合
- 用 Black-Litterman 或熵池化融入主观观点
- 对组合做 walk-forward 与组合交叉验证并调参
- 将最优权重经混合整数规划转为整股分配

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L20: - The optimisers include mean-risk, risk budgeting and relaxed risk budgeting, near-optimal centering, hierarchical
> L21: - The library has over 50 risk measures. Among them are variance, semi-moments, mean absolute deviation, VaR, CVaR,
> L70: We compute the returns with `prices_to_returns`. `PortfolioOptimisers.jl` builds its optimisation problems with `Ju

## 星数曲线

```mermaid
xychart-beta
    title "dcelisgarza/PortfolioOptimisers.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `613fea808316` · [字段定义](../../DATASET.md)*
