# AmirhosseinHonardoust/Demand-Forecasting

⭐ 32 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/AmirhosseinHonardoust/Demand-Forecasting) · 个人维护

**基于 ARIMA/SARIMA 的销量需求预测工作流（作品集演示）**

端到端时间序列预测项目：用固定种子生成含趋势与周/年季节性的合成日销量数据，对 CSV 做日频缺口填充，按 AIC 在小网格内搜索 ARIMA/SARIMA 阶数，在验证窗口上计算 RMSE/MAE/MAPE/sMAPE，输出带 95% 置信区间的多天预测，并通过滚动起点回测与季节性朴素基线对比。以可安装包形式提供 demand-forecast CLI（generate/forecast/backtest），含测试与 GitHub Actions CI。README 明确声明这是作品集与研究演示，数据为合成，不适用于真实库存或财务规划；不处理多序列、外生变量或实时监控。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固定种子生成可复现合成日销量数据并做日频缺口填充
- AIC 网格搜索 ARIMA/SARIMA 并输出 95% 置信区间
- 滚动起点回测与季节性朴素基线逐折对比
- demand-forecast CLI 与 pytest 测试、ruff/black/mypy 质量门禁

## 适用场景

- 我想展示一个可复现、带基线对比的时间序列预测作品集项目
- 我想在合成或自有日销量 CSV 上快速跑 ARIMA/SARIMA 预测与回测
- 我想学习模型选择、评估指标与残差诊断的完整流程

## 场景标签

 · 领域:时间序列预测/统计建模

## 证据(README 行号)

> L10: An end-to-end demand-forecasting workflow that turns a daily sales series into **calibrated ARIMA/SARIMA forecasts*
> L26: - select an ARIMA/SARIMA model by AIC over a small grid

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Demand-Forecasting 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `75b061e47d78` · [字段定义](../../DATASET.md)*
