# aliseyfi75/COSCI-GAN

⭐ 39 · Jupyter Notebook · MIT · 推送 2025-11-18 · [GitHub](https://github.com/aliseyfi75/COSCI-GAN) · 个人维护

**NeurIPS 2022 论文 COSCI-GAN 官方代码：生成多元时间序列合成数据**

NeurIPS 2022 论文《Generating multivariate time series with COmmon Source CoordInated GAN》的官方代码库，实现 COSCI-GAN 框架用于合成多元时间序列数据。支持合成正弦、EEG（UCI 数据集）与股票（Yahoo Finance）数据，生成器与判别器可选 MLP 或 LSTM 结构，也可替换为 Transformer 等任意网络。通过 run.py 命令行运行，参数涵盖训练轮数、批大小、学习率、中央判别器类型、gamma 多样性/相关性权衡系数等。作者为 Ali Seyfi、Jean-Francois Rajotte、Raymond T. Ng。

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

- COSCI-GAN 框架的多变量时间序列合成数据生成实现
- 支持合成正弦、EEG、股票三类数据集
- 生成器/判别器可选 MLP 或 LSTM，架构可替换为 Transformer 等任意网络
- 命令行参数含中央判别器、gamma 多样性/相关性权衡等论文机制

## 适用场景

- 复现论文中的多元时间序列合成实验
- 生成 EEG 或股票数据的合成数据用于研究
- 修改生成器/判别器架构做时间序列 GAN 实验研究

## 场景标签

 · 领域:生成模型/时间序列

## 证据(README 行号)

> L1: # Codebase for "Generating multivariate time series with COmmon Source CoordInated GAN (COSCI-GAN)"
> L15: This directory contains implementations of COSCI-GAN framework for synthetic multivariate time series data generati

## 星数曲线

```mermaid
xychart-beta
    title "aliseyfi75/COSCI-GAN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1314f841f281` · [字段定义](../../DATASET.md)*
