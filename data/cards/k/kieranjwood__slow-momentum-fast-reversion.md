# kieranjwood/slow-momentum-fast-reversion

⭐ 278 · Python · MIT · 推送 2026-03-19 · [GitHub](https://github.com/kieranjwood/slow-momentum-fast-reversion) · [官网](https://kieranjwood.github.io/publication/slow-momentum-fast-reversion/) · 组织维护

**论文配套代码：深度学习+变点检测的动量交易策略**

Oxford 研究者论文《Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and Changepoint Detection》的官方代码实现。在 Deep Momentum Network（LSTM 架构，同时学习趋势估计与仓位 sizing）管道中插入在线变点检测模块，输出变点位置与严重度分数，用于在趋势反转时快速切换快慢策略。数据基于 Nasdaq Data Link（Quandl）的 600+ 期货连续合约，README 给出下载数据、构造特征与运行 CPD 模块的命令。README 顶部声明该工作已被 Momentum Transformer 论文扩展并建议参考其仓库。

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

- 在 LSTM 动量网络管道中插入在线变点检测（CPD）模块
- CPD 模块输出变点位置与严重度分数
- 基于 Quandl 600+ 期货连续合约数据（1990-2020 期间测试 50 个品种）
- 提供数据下载、特征构造与 CPD 运行的命令行步骤

## 适用场景

- 复现论文中的动量+变点检测交易策略实验
- 研究变点检测如何改善动量策略对市场状态切换的响应
- 作为 Deep Momentum Network 方向研究的代码基础

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: This code accompanies the the paper Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and C
> L21: > Momentum strategies are an important part of alternative investments and are at the heart of commodity trading ad

## 星数曲线

```mermaid
xychart-beta
    title "kieranjwood/slow-momentum-fast-reversion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 277 --> 279
    line [278, 278]
```

2026-10-18 278 → 2026-10-28 278（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dfd28d6dac14` · [字段定义](../../DATASET.md)*
