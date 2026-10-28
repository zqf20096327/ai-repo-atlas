# Hallupa/AutomatedTrading

⭐ 22 · C# · GPL-3.0 · 推送 2026-04-14 · [GitHub](https://github.com/Hallupa/AutomatedTrading) · 个人维护

**C# 编写的加密货币/外汇交易机器人设计与回测工具**

用 C#（Visual Studio 2019）编写的桌面应用，用于设计加密货币与价差交易的交易策略，并以 1 小时及以上 K 线回测：可从 FXCM 下载 K 线数据、在多市场多年代价数据上快速运行策略、在图表上查看交易与权益曲线并输出期望值、回撤等统计。当前仅支持对 FXCM 实盘运行。计划中的机器学习支持可基于图表上标注的兴趣点用 TensorFlow 神经网络学习。项目自述为高度实验性的进行中作品，作者目前主要供自用，无安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 策略编辑器设计交易策略，针对 1 小时及以上 K 线回测
- 多市场快速回测：33 个市场 10 年数据 35 秒生成 10.5 万笔交易
- 从 FXCM 下载 K 线数据并可将策略对 FXCM 实盘运行
- 基于 TensorFlow 神经网络的机器学习支持（实验性）

## 适用场景

- 设计并回测加密货币或外汇交易策略
- 在图表上查看模拟交易与权益曲线
- 将回测通过的策略接入 FXCM 实盘运行

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L45: Set points of interest on the chart which will then feed into the TensorFlow machine learning, which will use a neu
> L17: 9. Add machine learning support

## 星数曲线

```mermaid
xychart-beta
    title "Hallupa/AutomatedTrading 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `52cddbfcb8b1` · [字段定义](../../DATASET.md)*
