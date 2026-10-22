# AmpyFin/ampyfin

⭐ 427 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/AmpyFin/ampyfin) · 组织维护

**面向 NASDAQ-100 的集成学习量化交易系统：训练、回测到实盘**

Python 实现的算法交易框架：用 yfinance 获取历史数据，内置均值回归、动量、套利等策略，通过排名集成学习按绩效动态调整各策略权重，经训练/测试/推送流程后将模型存入 MongoDB 并由交易模块执行 Alpaca 券商订单（默认模拟盘）。数据与日志存于 MongoDB，本地另建 SQLite。面向希望研究机器学习交易系统的开发者与交易者，需自行配置 MongoDB、TA-Lib 及 Alpaca、Weights & Biases API key。

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

- 排名集成学习按绩效动态加权各交易策略
- 训练/测试/推送三模式与两阶段实盘建议流程
- 对接 Alpaca 券商执行，默认模拟盘可切换实盘
- MongoDB 存储数据与模型，支持 100+ TA-Lib 指标

## 适用场景

- 训练与回测量化交易策略后接入 Alpaca 实盘
- 研究集成学习在金融市场的加权决策方法
- 基于现有策略框架开发自定义交易算法

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: AmpyFin is an advanced AI-powered trading system designed to trade within the NASDAQ-100. It leverages machine lear
> L52: AmpyFin uses a ranked ensemble learning system that dynamically evaluates each strategy's performance and adjusts t

## 星数曲线

```mermaid
xychart-beta
    title "AmpyFin/ampyfin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 426 --> 428
    line [427, 427]
```

2026-10-18 427 → 2026-10-22 427（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `c75793c900f4` · [字段定义](../../DATASET.md)*
