# SilvioBaratto/stockpy

⭐ 20 · Python · MIT · 推送 2026-05-17 · [GitHub](https://github.com/SilvioBaratto/stockpy) · [官网](https://pypi.org/project/stockpy-learn/) · 个人维护

**基于 PyTorch/Pyro 的深度学习回归与分类 Python 库**

面向数据分析与机器学习开发者的 Python 库，最初为股票市场数据预测设计，现支持通用数据集的回归与分类任务。基于 PyTorch 与 Pyro 实现 8 类算法（贝叶斯神经网络、LSTM、BiLSTM、GRU、BiGRU、MLP、NNHMM、DMM），每种算法均提供回归与分类实现。可读取 CSV、pandas dataframe、numpy 数组与 torch 张量作为输入，并附带命令行数据下载器（data.py）用于下载和更新标普 500 股票数据。通过 pip（包名 stockpy-learn）或源码安装。

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

- 8 类算法各含回归与分类实现（BNN/LSTM/GRU/MLP/NNHMM/DMM 等）
- 支持 CSV/pandas/numpy/torch 多种输入格式
- 附带标普 500 股票数据下载与更新的命令行工具

## 适用场景

- 对股票市场数据做回归预测或分类
- 用贝叶斯神经网络等概率模型做通用回归分类任务
- 批量下载并更新标普 500 成分股历史数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L10: **stockpy** is a versatile Python Machine Learning library initially designed for stock market data analysis and pr
> L12: - Bayesian Neural Networks (BNN)

## 星数曲线

```mermaid
xychart-beta
    title "SilvioBaratto/stockpy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bd98b0c2835f` · [字段定义](../../DATASET.md)*
