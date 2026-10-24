# alkalescent/hyperdrive

⭐ 159 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/alkalescent/hyperdrive) · [官网](https://Algotrade.io) · 个人维护

**ML 驱动的算法交易库：数据采集、回测与下单**

Python 算法交易库，量化研究公司 Algotrade.io 在用。功能聚合来自 Polygon、Robinhood、BLS 的市场与宏观经济数据，S3 存储历史数据，基于 vectorbt 回测，用 AutoGluon 做机器学习预测，并支持在 Binance、Alpaca、Kraken 执行交易。提供 GitHub Actions 工作流自动化数据更新。建模部分代码仍闭源（Historian 类可参考）。通过 pip 安装，需 Python 3.11+，密钥经环境变量传入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 Polygon、Robinhood、BLS 市场与宏观数据
- 基于 vectorbt 的策略回测
- AutoGluon 机器学习预测
- 支持 Binance、Alpaca、Kraken 交易所下单

## 适用场景

- 采集并存储历史行情数据用于量化研究
- 回测交易策略并查看收益统计
- 将策略订单提交到加密货币交易所

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: **_hyperdrive_** is an algorithmic trading library that powers quant research firm **Algotrade.io**.
> L22: - **AI/ML**: Machine learning predictions with AutoGluon

## 星数曲线

```mermaid
xychart-beta
    title "alkalescent/hyperdrive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 158 --> 160
    line [159, 159]
```

2026-10-18 159 → 2026-10-24 159（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `987f568f2d28` · [字段定义](../../DATASET.md)*
