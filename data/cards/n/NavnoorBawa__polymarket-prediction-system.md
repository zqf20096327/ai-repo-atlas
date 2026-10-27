# NavnoorBawa/polymarket-prediction-system

⭐ 36 · Python · 推送 2025-12-25 · [GitHub](https://github.com/NavnoorBawa/polymarket-prediction-system) · 个人维护

**面向 Polymarket 的 ML 预测系统：生成交易信号与仓位建议**

通过 Python 实现的预测市场研究系统：从 Polymarket API 拉取实时市场数据，计算 RSI、波动率、订单簿失衡、期望值等量化指标，用 XGBoost、LightGBM 与 stacking 集成模型预测市场价格，输出当前价与预测价对比、买入/卖出/持有建议、置信度与 Kelly 准则仓位大小，并自动排除已结算和低成交量市场。以源码仓库形式提供，需 Python 3.8+ 并安装 requirements.txt 依赖，README 声明仅供教育与研究用途、非财务建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XGBoost + LightGBM + stacking 集成预测模型
- 实时拉取 Polymarket API 数据并计算量化指标
- Kelly 准则仓位 sizing 与风险调整
- 输出交易信号（STRONG BUY/BUY/HOLD）与置信度

## 适用场景

- 研究预测市场的 ML 建模与信号生成方法
- 学习量化指标计算与 Kelly 仓位管理
- 对 Polymarket 市场做实验性数据分析

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: This project uses sophisticated ML algorithms including XGBoost, LightGBM, and stacking ensembles to analyze predict
> L21: - `prediction_model.py` - ML models and prediction algorithms

## 星数曲线

```mermaid
xychart-beta
    title "NavnoorBawa/polymarket-prediction-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f2ef89ce0911` · [字段定义](../../DATASET.md)*
