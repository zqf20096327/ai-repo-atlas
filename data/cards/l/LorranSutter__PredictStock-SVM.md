# LorranSutter/PredictStock-SVM

⭐ 30 · Python · GPL-3.0 · 推送 2026-07-01 · [GitHub](https://github.com/LorranSutter/PredictStock-SVM) · 个人维护

**基于机器学习的股票涨跌趋势预测分类模型（课程项目）**

巴西茹伊斯-迪福拉联邦大学计算工程 Capstone 项目，用 Python 实现股票趋势分类预测流水线：以 pandas-datareader 获取股票历史数据，pandas 清洗并计算金融指标；用 Extremely Randomized Trees 做特征选择（度量各指标重要性），K-Means 聚类以减少支持向量数量，Support Vector Machines 做涨跌分类，K-Fold 交叉验证做参数调优。运行时先执行 initGetData.py 按 NASDAQ 清单抓取数据，再修改 main.py 中 ticker 变量运行主程序。面向机器学习学习者与量化研究参考人群。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Extra Trees 特征选择 + K-Means 聚类 + SVM 分类的完整流水线
- K-Fold 交叉验证用于参数调优
- pandas-datareader 自动抓取股票历史数据
- 提供逐步骤的方法说明与文献引用

## 适用场景

- 我想学习机器学习方法在股票趋势预测中的组合应用
- 我想跑通一个从数据抓取到分类预测的 Python 完整示例
- 我想参考金融指标特征选择与 SVM 分类的实现方式

## 场景标签

`金融量化` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3:  Classification model for predicting stock market trending, based on machine learning techniques, such as Extremely 
> L42:  This is the main step of this pipeline, where the classified data stands for upward or downward stock oscillation.

## 星数曲线

```mermaid
xychart-beta
    title "LorranSutter/PredictStock-SVM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1c4f4f1f87ac` · [字段定义](../../DATASET.md)*
