# andrebrener/crypto_predictor

⭐ 42 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/andrebrener/crypto_predictor) · 个人维护

**用机器学习预测加密货币价格并给出建议的 Python 应用**

2017–2018 年构建的 Python 应用：抓取 CoinMarketCap 数据，用 scikit-learn 模型预测加密货币价格并生成买卖建议，通过邮件发送结果；价格以 BTC 计价以规避 BTC 波动。README 声明项目已归档：抓取脚本针对 2018 年站点布局已失效，Gmail 旧认证方式亦被 Google 于 2022 年停用，现需迁移到 CoinGecko API 与新邮件认证才能运行。安装方式为 git clone 后 pip install -r requirements.txt。

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

- scikit-learn 模型预测加密货币价格并生成建议
- 自动执行数据抓取、预测与邮件发送流程
- 价格以 BTC 计价以规避 BTC 波动

## 适用场景

- 参考一个端到端的价格预测与建议生成流水线实现
- 学习加密货币量化分析中的特征与建模做法（历史参考）

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: Crypto Predictor is an application that generates financial recommendations for cryptocurrencies using Machine Learn
> L3: > **Status (2026): archival.** This project was built in 2017–2018. The ML pipeline and technical-analysis features 

## 星数曲线

```mermaid
xychart-beta
    title "andrebrener/crypto_predictor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3d502ee07ef` · [字段定义](../../DATASET.md)*
