# SamanKhamesian/Credit-Card-Fraud-Detection

⭐ 14 · Python · Apache-2.0 · 推送 2026-08-30 · [GitHub](https://github.com/SamanKhamesian/Credit-Card-Fraud-Detection) · 个人维护

**用隐马尔可夫模型检测信用卡欺诈的 Python 实现**

基于论文的信用卡欺诈检测技术的 Python 实现：将单一持卡人的消费金额序列经聚类（默认 k-means，备选 DBSCAN 及多种层次聚类）转为消费水平符号，训练只依赖正常行为的隐马尔可夫模型（Baum-Welch 重估计）；新交易映射到簇后替换观察窗口最旧符号，比较新旧序列概率的相对下降，超过可配置阈值即判定为欺诈。金额通过交互方式读入并逐条打印判定结果。要求 Python 3.7.0 及 hidden_markov、numpy、pandas、scikit_learn 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HMM 仅用正常行为训练，无需欺诈标注样本
- 金额经 k-means/DBSCAN/层次聚类转为符号序列
- 滑动观察窗口上的相对概率下降判定欺诈
- 交互式逐笔读入金额并输出判定

## 适用场景

- 研究者复现 HMM 信用卡欺诈检测论文方法
- 在不依赖欺诈标注数据的场景下检测异常消费序列
- 对比不同聚类方式对符号化序列建模的影响

## 场景标签

`网络安全` `金融量化` · 领域:学习与行业

## 证据(README 行号)

> L4: Due to a rapid advancement in the electronic commerce technology, the use of credit cards has dramatically increased
> L6: This repository is a Python implementation of that technique, working from one cardholder's history as a sequence of

## 星数曲线

```mermaid
xychart-beta
    title "SamanKhamesian/Credit-Card-Fraud-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `7840d1753bf1` · [字段定义](../../DATASET.md)*
