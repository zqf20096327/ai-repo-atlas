# kieranjwood/trading-momentum-transformer

⭐ 642 · Python · MIT · 推送 2026-03-19 · [GitHub](https://github.com/kieranjwood/trading-momentum-transformer) · [官网](https://kieranjwood.github.io/publication/momentum-transformer/) · 组织维护

**动量交易 Transformer 论文官方代码：深度学习输出仓位信号**

随两篇论文发布的量化交易研究代码：Momentum Transformer（基于注意力机制的 Deep Momentum Network，直接输出仓位大小，以 Sharpe 比率等风险调整指标为训练目标）与 Slow Momentum with Fast Reversion（在 DMN 管线中插入在线变点检测模块）。使用流程为：注册 Nasdaq Data Link 账户下载 600+ 期货连续合约的 Quandl 数据，用 python -m 命令生成特征、运行变点检测并执行实验。架构复用 Temporal Fusion Transformer 组件，需从源码以 Python 模块方式运行。

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

- Momentum Transformer：注意力架构直接输出仓位，按 Sharpe 比率优化
- 在线变点检测（CPD）模块，支持多时间尺度回看窗口
- 使用 Nasdaq Data Link 免费 Quandl 期货数据集（600+ 连续合约）
- 复用 Temporal Fusion Transformer 组件，提供注意力模式可解释性

## 适用场景

- 复现论文中的动量/均值回归交易策略实验
- 在期货数据上运行 DMN 与变点检测组合实验
- 研究注意力机制在金融时间序列交易信号生成中的应用

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: This code accompanies the paper Trading with the Momentum Transformer: An Intelligent and Interpretable Architectur
> L29: > Deep learning architectures, specifically Deep Momentum Networks (DMNs) , have been found to be an effective appr

## 星数曲线

```mermaid
xychart-beta
    title "kieranjwood/trading-momentum-transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 640 --> 643
    line [641, 642]
```

2026-10-18 641 → 2026-10-24 642（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `912a940e8577` · [字段定义](../../DATASET.md)*
