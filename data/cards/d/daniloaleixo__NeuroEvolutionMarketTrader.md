# daniloaleixo/NeuroEvolutionMarketTrader

⭐ 33 · Jupyter Notebook · 推送 2026-01-16 · [GitHub](https://github.com/daniloaleixo/NeuroEvolutionMarketTrader) · 个人维护

**用神经进化训练的外汇/股票自动交易 agent（实验项目）**

个人实验项目：以神经进化（population 256、100 代、变异与存活率等参数）训练交易 agent，输入 OHLC 及生成的 RSI、MACD 指标，另经预训练 CNN 买卖分类器输出附加参数。README 报告 v3.0141 在 EURUSD 30M 蜡烛上的回测结果（2016-2018 三年均值收益 14.17%、胜率均值 80%），并列出训练与回测明细。通过 Docker 构建 notebook 运行，计划开发 API 与前端。项目主题标签含 bovespa 股票，但正文实验均在 EURUSD 外汇数据上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 神经进化训练交易 agent（OHLC + RSI + MACD 输入）
- 预训练 CNN 买卖分类器提供附加输入参数
- 提供 2016-2018 分年度回测指标（收益/回撤/胜率/SQN 等）
- 通过 Docker 构建 notebook 运行

## 适用场景

- 研究神经进化在交易策略生成中的应用
- 复现 EURUSD 分钟级蜡烛数据上的训练与回测实验
- 参考 OHLC+技术指标+CNN 分类的特征组合方式

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: * Using neuro evolution
> L16: * Also run through a pretrained CNN buy and sell classifier to get the last set of parameters

## 星数曲线

```mermaid
xychart-beta
    title "daniloaleixo/NeuroEvolutionMarketTrader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5dce83d3a697` · [字段定义](../../DATASET.md)*
