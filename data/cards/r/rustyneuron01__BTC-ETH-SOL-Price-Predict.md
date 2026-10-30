# rustyneuron01/BTC-ETH-SOL-Price-Predict

⭐ 19 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/rustyneuron01/BTC-ETH-SOL-Price-Predict) · 个人维护

**加密资产价格概率预测系统：ensemble 路径 + CRPS 评分**

面向加密资产（BTC/ETH/SOL/XAU 及代币化股票）的集成价格预测系统：Worker 端每次请求生成 1000 条模拟价格路径（24 小时、5 分钟间隔），用 XGBoost 基于缓存特征做波动率预测；Coordinator 端用 CRPS（proper scoring rule）对预测的校准度与锐度评分，按资产加权的 10 日滚动平均生成排行榜，并按相对表现用 softmax 分配 emissions。输出为合成价格数据，供训练 AI agent 及期权定价、组合风险分析使用。技术栈为 Python 3.11，含 PostgreSQL 存储、Pyth 价格数据、Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次请求生成 1000 条模拟路径的概率预测（非点估计）
- XGBoost 基于缓存特征做波动率预测
- CRPS 评分覆盖校准度与锐度，多时间增量（5min–24h）评估
- 10 日资产加权滚动平均排行榜 + softmax emissions 分配

## 适用场景

- 为 AI agent 训练提供合成价格数据
- 期权定价与组合风险分析的价格分布输入
- 以 CRPS 客观衡量价格预测模型质量

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: This project produces **ensemble forecasts** of future asset prices (many simulated paths per request) to capture fu
> L93: |**ML / volatility**|XGBoost (volatility prediction from cached features)|

## 星数曲线

```mermaid
xychart-beta
    title "rustyneuron01/BTC-ETH-SOL-Price-Predict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `40447cd98892` · [字段定义](../../DATASET.md)*
