# antonio-gaskin/car-sales-prediction

⭐ 10 · Jupyter Notebook · 推送 2026-08-06 · [GitHub](https://github.com/antonio-gaskin/car-sales-prediction) · 个人维护

**基于客户特征预测购车预算并推荐车型的 Flask 应用**

Flask Web 应用：根据性别、年龄、净资产、年薪、信用卡欠款等特征预测客户购车预算（因变量为 SalePrice），并按预测区间筛选展示车辆。README 展示回归模型训练过程，含相关性热力图、Epoch Loss、评估损失曲线等图表，并通过 Heroku PaaS 部署，提供在线演示地址。面向需要为客户估算购车预算并推荐车型的销售场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于人口与财务特征回归预测客户购车预算
- 按预测预算区间筛选并展示候选车辆
- 提供交互式 Web UI 与模型训练图表
- 已部署至 Heroku，提供在线访问地址

## 适用场景

- 为到店客户估算购车预算
- 按客户预算筛选展示车型
- 查看回归模型的训练与评估曲线

## 场景标签

 · 领域:机器学习应用/销售分析

## 证据(README 行号)

> L2: This software will help you predict the budget of your client given parameters like Gender, Age, Net Worth, Annual S
> L30: The Website is deployed using Platform as a service (PaaS) model. The hosted website can be seen on https://car-sal

## 星数曲线

```mermaid
xychart-beta
    title "antonio-gaskin/car-sales-prediction 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `a04425c2b64b` · [字段定义](../../DATASET.md)*
