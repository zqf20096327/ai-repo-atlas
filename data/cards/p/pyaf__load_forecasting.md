# pyaf/load_forecasting

⭐ 648 · Jupyter Notebook · MIT · 推送 2026-03-25 · [GitHub](https://github.com/pyaf/load_forecasting) · 组织维护

**德里短期电力负荷预测本科项目：ARIMA/RNN/LSTM 等多模型对比**

本科生课程项目，使用印度德里 State Load Despatch Center 的负荷数据与 wunderground 天气数据，实现 9 种时间序列算法（FFNN、SMA、WMA、SES、Holt-Winters、ARIMA、RNN、LSTM、GRU），以 Jupyter notebook 形式存放于 models 目录。附带脚本完成数据抓取、ARIMA 超参数网格搜索与每日 00:30 IST 定时预测调度，并含一个用于展示各算法性能对比的 Django 网页服务器（README 标注现已弃用）。

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

- 实现 9 种时间序列预测算法（ARIMA/RNN/LSTM/GRU/平滑法等）
- 每日 00:30 IST 定时运行的预测调度脚本
- 从 SLDC 德里网站与 wunderground 抓取负荷与天气数据
- Django 网页服务器展示并对比各算法性能（已弃用）

## 适用场景

- 学习对比多种时间序列预测算法在电力负荷数据上的实现
- 参考电力负荷数据抓取与定时预测的工程脚本

## 场景标签

 · 领域:能源/时间序列预测

## 证据(README 行号)

> L3: Under graduate project on short term electric load forecasting. Data was taken from State Load Despatch Center, Delh
> L16: * Long Short Term Memory cells LSTM.ipynb

## 星数曲线

```mermaid
xychart-beta
    title "pyaf/load_forecasting 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 647 --> 649
    line [648, 648]
```

2026-10-18 648 → 2026-10-25 648（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `dc134929a455` · [字段定义](../../DATASET.md)*
