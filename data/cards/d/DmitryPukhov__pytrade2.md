# DmitryPukhov/pytrade2

⭐ 31 · Python · 推送 2026-04-25 · [GitHub](https://github.com/DmitryPukhov/pytrade2) · 个人维护

**面向开发者的加密货币 AI 交易机器人（Binance 等）**

Python 编写的加密货币自动交易机器人，通过 Keras 神经网络策略（如 KerasBidAskRegressionStrategy）预测价格走势并自动买卖，支持在最近数据上周期性重训练。对接 Binance 交易所，可先用 testnet 虚拟账户或真实账户的 API key 运行，配置以 yaml 文件完成，docker-compose 启动。附带 Jupyter notebook 用于探索交易分析，策略以 python 包组织便于扩展。README 为英文并含俄文描述。

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

- Keras 神经网络策略预测价格走势并自动交易
- 支持 Binance testnet 虚拟账户与真实账户 API key
- 分钟级周期性在最新数据上重训练模型
- 附带 Jupyter notebook 分析机器人交易

## 适用场景

- 用虚拟账户试跑 AI 交易策略
- 在 Binance 上运行神经网络自动交易
- 通过 notebook 分析和调优交易策略

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L2: **Сrypto trading AI bots.
> L8: 5. Run **docker-compose up simplekeras** and the bot will start trading. KerasBidAskRegressionStrategy predicts futu

## 星数曲线

```mermaid
xychart-beta
    title "DmitryPukhov/pytrade2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b22ab7e8df40` · [字段定义](../../DATASET.md)*
