# Docat0209/qlib-tw-trader

⭐ 11 · Python · MIT · 推送 2026-03-15 · [GitHub](https://github.com/Docat0209/qlib-tw-trader) · 个人维护 · 中文 README

**面向台湾股市的端到端量化交易研究平台**

覆盖台股量化研究全流程：从 TWSE OpenAPI、FinMind、yfinance 多源同步行情数据，计算约 300 个 alpha 因子，训练 DoubleEnsemble 与 LightGBM 模型，以 156 周 Walk-Forward 框架做样本外回测，并生成每日 top-100 股票的预测信号。提供 FastAPI 后端与 React 仪表盘（9 个页面）实时监控。设计上强调前视偏差防范：T 日交易仅用 T-1 收盘前可得特征，训练/验证集间设 7 天 embargo。数据覆盖受免费接口限流约束。

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

- 约 300 个因子库：Alpha158、台股法人资金流、交叉项与增强因子
- DoubleEnsemble（ICDM 2020）迭代集成模型与 Optuna 贝叶斯超参搜索
- 156 周 Walk-Forward 回测，含 IC Decay、分位价差与 9 种策略变体对比
- React 仪表盘 9 页面，WebSocket 实时更新

## 适用场景

- 对台股做因子挖掘与机器学习选股研究
- 用 Walk-Forward 框架做严格的样本外策略回测
- 每日生成股票排名信号并跟踪预测历史
- 通过仪表盘监控数据同步、训练质量与回测结果

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L18: qlib-tw-trader is a full-stack quantitative trading research platform built for Taiwan's stock market. It automates
> L24: 5. **Generate daily signals** ranking Taiwan's top-100 stocks by predicted 2-day return
> L22: 3. **Train ML models** using DoubleEnsemble (ICDM 2020) -- an iterative ensemble that automatically selects useful 

## 星数曲线

```mermaid
xychart-beta
    title "Docat0209/qlib-tw-trader 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-18", "2026-11-27"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-10-26 10 → 2026-11-27 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `2516c1a4f464` · [字段定义](../../DATASET.md)*
