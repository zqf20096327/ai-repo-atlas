# stefan-jansen/machine-learning-for-trading

⭐ 22,011 · Jupyter Notebook · MIT · 推送 2026-11-22 · [GitHub](https://github.com/stefan-jansen/machine-learning-for-trading) · [官网](https://ml4trading.io) · 个人维护

**《机器学习交易》第三版配套代码：27章+9个案例研究**

Stefan Jansen 所著 Machine Learning for Trading 第三版的配套代码仓库，含 27 章代码与九个贯穿全书的案例研究，覆盖 ETF、加密永续、日内股票、期权、外汇、期货等资产类别。代码按章节目录组织，每章目录附实现指南；数据层使用 Polars，各章以 Docker 环境提供可复现运行。内容涵盖数据基础设施、特征工程、模型开发（梯度提升、深度时间序列、因果机器学习）、回测、组合构建与实盘交易（Interactive Brokers、Alpaca、QuantConnect），并包含基于 SEC 文件的 RAG 与多智能体研究系统等生成式 AI 章节。第二版代码保留在 second-edition 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.2 天,年发版 5,17 位贡献者
- 涨星:近 1 天 **+28**(自 20261016 起算)

## 能力要点

- 27 章代码与 9 个端到端案例研究，统一同一 pipeline
- 可复现 Docker 环境，数据层迁移至 Polars
- 覆盖从数据获取、模型开发到实盘执行的完整 ML4T workflow
- 包含 RAG（SEC 文件）、Graph RAG 与多智能体研究系统等生成式 AI 内容

## 适用场景

- 按书籍章节学习机器学习交易策略的实现代码
- 在 Docker 环境中复现书中九个资产类别的案例研究
- 参考书中数据基础设施与回测流程搭建自己的策略研究 pipeline

## 场景标签

`RAG` `金融量化` `强化学习` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L5: The code for *Machine Learning for Trading, 3rd Edition* by
> L6: Stefan Jansen: 27 chapters and nine case studies, rebuilt
> L107: ## The Code, Chapter by Chapter

## 星数曲线

```mermaid
xychart-beta
    title "stefan-jansen/machine-learning-for-trading 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 21465 --> 22060
    line [21514, 21524, 21534, 21548, 21555, 21597, 21618, 21631, 21641, 21653, 21666, 21534, 21756, 21776, 21788, 21796, 21808, 21815, 21826, 21840, 21865, 21891, 21907, 21920, 21934, 21960, 22011]
```

2026-10-23 21,514 → 2026-11-25 22,011（+497）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `943787af6cc1` · [字段定义](../../DATASET.md)*
