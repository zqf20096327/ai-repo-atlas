# stefan-jansen/machine-learning-for-trading

⭐ 22,053 · Jupyter Notebook · MIT · 推送 2026-11-25 · [GitHub](https://github.com/stefan-jansen/machine-learning-for-trading) · [官网](https://ml4trading.io) · 个人维护

**面向量化交易学习者：机器学习交易教材配套代码库**

Stefan Jansen《Machine Learning for Trading》第三版的随书代码，覆盖 27 章与 9 个案例研究，围绕一条从数据获取、策略研究、回测到实盘部署的端到端工作流组织。数据层使用 Polars，每章提供可复现 Docker 环境，建模栈包含 PyTorch、LightGBM、Optuna 与 Plotly。读者按章节目录打开对应 notebook 配合书本学习；另提供 Maven 平台的课程与工作坊信息。

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

- 27 章代码，每章一个目录并附实现指南与所需数据说明
- 9 个案例研究覆盖 ETF、加密永续、日内股票、期权、外汇、期货等资产类别
- 每章提供可复现 Docker 环境，数据层迁移到 Polars
- 涵盖梯度提升、深度时序模型、因果 ML、强化学习与生成式 AI 等专题

## 适用场景

- 按章节运行 notebook 学习机器学习交易工作流
- 在 Docker 环境中复现书中案例研究的结果
- 参考从原始数据到策略部署的完整流水线实现

## 场景标签

`金融量化` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: The code for *Machine Learning for Trading, 3rd Edition* by
> L107: One directory per chapter, each opening with a guide that maps the chapter's sections onto the
> L51: The data layer moves to **Polars** for fast, expression-based manipulation, and every chapter ships in **reproducib

## 星数曲线

```mermaid
xychart-beta
    title "stefan-jansen/machine-learning-for-trading 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 21472 --> 22105
    line [21524, 21534, 21548, 21555, 21597, 21618, 21631, 21641, 21653, 21666, 21534, 21756, 21776, 21788, 21796, 21808, 21815, 21826, 21840, 21865, 21891, 21907, 21920, 21934, 21960, 22011, 22053]
```

2026-10-24 21,524 → 2026-11-26 22,053（+529）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7d1e0479084f` · [字段定义](../../DATASET.md)*
