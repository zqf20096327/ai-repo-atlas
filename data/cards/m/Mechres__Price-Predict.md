# Mechres/Price-Predict

⭐ 14 · Python · 推送 2026-03-13 · [GitHub](https://github.com/Mechres/Price-Predict) · 个人维护

**加密货币与股票价格预测工具：多种回归模型实验**

使用 Python 编写的价格预测与预测实验工具包，通过 Main.py 与 GUI.py 选择模型和起止日期，基于 Yahoo Finance 历史数据训练模型。可用模型包括 LSTM、CatBoost、Prophet、XGBoost、LightGBM 与随机森林；LSTM 结合技术指标（SMA/EMA/RSI）与时间特征，CatBoost 通过网格搜索调参。作者声明这是业余实验项目，产出的模型不适用于真实加密货币交易，不应作为投资决策依据。依赖通过 pip 安装并给出固定版本号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 种模型可选：LSTM、CatBoost、Prophet、XGBoost、LightGBM、随机森林
- 数据来自 Yahoo Finance，LSTM 结合 SMA/EMA/RSI 技术指标
- 提供 GUI 与保存/加载功能，依赖给出固定版本号

## 适用场景

- 学习对比不同回归模型在金融时间序列上的表现
- 在 GUI 中选择模型与日期区间做价格预测实验
- 了解技术指标特征工程与网格搜索调参的实现方式

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L4: Main.py & GUI.py files let's you select model, start & end date, available models are: Lstm, Catboost, Prophet, XGBo
> L29: Long Short-Term Memory (LSTM). It leverages historical price data from Yahoo Finance and incorporates technical ind

## 星数曲线

```mermaid
xychart-beta
    title "Mechres/Price-Predict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a0f6639b70bf` · [字段定义](../../DATASET.md)*
