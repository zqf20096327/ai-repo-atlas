# Rpita623/Detecting-Credit-Card-Fraud

⭐ 22 · R · 推送 2026-06-10 · [GitHub](https://github.com/Rpita623/Detecting-Credit-Card-Fraud) · 个人维护

**用 R 与多种机器学习算法构建信用卡欺诈分类器**

一个 R 语言数据科学项目：使用信用卡交易数据集，经过数据探索、scale() 标准化、按 0.80 比例划分训练/测试集后，依次拟合 Logistic 回归、决策树（rpart）、人工神经网络（neuralnet 包，阈值 0.5）与梯度提升（GBM）四类分类模型，并通过 ROC 曲线与 AUC 评估各模型区分欺诈与非欺诈交易的表现。README 以学习记录形式撰写，注明来源 DataFlair，未给出安装或运行命令。

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

- 依次实现 Logistic 回归、决策树、ANN、GBM 四种分类器
- scale() 对交易金额做标准化，80/20 划分训练与测试集
- 使用 ROC 曲线与 AUC 评估各模型性能

## 适用场景

- 学习 R 中多种经典机器学习算法的建模流程
- 参考信用卡欺诈二分类项目的数据处理与评估方法
- 了解 rpart、neuralnet 等 R 包的用法示例

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: The aim of this R project is to build a classifier that can detect credit card fraudulent transactions. I used a var
> L8: For carrying out the credit card fraud detection, I used the Card Transactions dataset that contains a mix of fraud 

## 星数曲线

```mermaid
xychart-beta
    title "Rpita623/Detecting-Credit-Card-Fraud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6e191cf42b68` · [字段定义](../../DATASET.md)*
