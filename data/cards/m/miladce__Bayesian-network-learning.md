# miladce/Bayesian-network-learning

⭐ 10 · Jupyter Notebook · 推送 2026-05-13 · [GitHub](https://github.com/miladce/Bayesian-network-learning) · 个人维护

**学习贝叶斯网络结构的 Python 实验项目**

基于 UCI Nursery 数据集演示贝叶斯网络结构学习，比较 MDL/BIC、AIC、BDeu 三种评分方法，使用 Hill Climbing 搜索学习网络结构，并将学习结果与预定义金标准网络对比，计算 TP/TN/FP/FN、Accuracy、Sensitivity、AHD、SHD 等结构指标；测试不同样本量对结构恢复的影响，AIC 评分为基于 pgmpy 的自定义实现。通过 pip 安装依赖后运行，附带渲染好的 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 比较 MDL/BIC、AIC、BDeu 三种结构学习评分方法
- 使用 Hill Climbing 搜索进行结构学习
- 以金标准网络评估，输出 Accuracy、SHD、AHD 等指标
- 基于 pgmpy 扩展自定义 AIC 评分实现

## 适用场景

- 学习贝叶斯网络结构学习算法的实现方式
- 比较不同评分函数在结构恢复上的表现
- 研究样本量对结构学习效果的影响

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: This project demonstrates Bayesian Network structure learning using the Nursery dataset from the UCI Machine Learnin
> L34: - The project uses Hill Climbing Search for Bayesian network structure learning.

## 星数曲线

```mermaid
xychart-beta
    title "miladce/Bayesian-network-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `8732f29b66bd` · [字段定义](../../DATASET.md)*
