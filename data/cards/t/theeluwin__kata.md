# theeluwin/kata

⭐ 20 · Python · 推送 2026-03-30 · [GitHub](https://github.com/theeluwin/kata) · 个人维护

**个人机器学习算法手写实现练习仓库，含任务与评测**

theeluwin 的个人 code kata 仓库：以“亲手实现经典机器学习算法”为目标，覆盖 HMM、朴素贝叶斯、协同过滤、线性回归、词嵌入（GloVe/Word2Vec）等 hard-coded 实现，并配 POS 标注、Titanic、MovieLens、Iris、MNIST 等任务及 baseline 对比。每个算法须在实际任务上训练并评测，附 test.py 单元测试与 benchmark 性能对比模式。深度学习部分计划使用 Keras/TensorFlow，另有论文复现 TODO 未完成。作者自述部分原则后期未坚持，Python 2/3 混杂。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- hard-coded 实现 HMM/朴素贝叶斯/协同过滤/线性回归等经典算法
- 每个算法绑定实际任务并实现评测与 baseline 对比
- test.py 支持单元测试与 benchmark 性能对比两种运行方式
- GloVe 与 Word2Vec 已完成 hard-coded 实现

## 适用场景

- 参考经典机器学习算法的从零实现方式
- 对照 hard-coded 实现与 sklearn/TensorFlow baseline 的性能差异
- 了解算法在具体任务（标注/分类/推荐/回归）上的评测流程

## 场景标签

 · 领域:机器学习/算法实现

## 证据(README 行号)

> L9: 주로 머신러닝 관련 알고리즘과 방법론을 구현하며, 딥러닝의 경우는 기본적인 부분 빼고는 Keras나 Tensorflow를 사용 할 예정.
> L38: 충분히 범용적으로 쓰일 수 있도록 코딩해둔 모듈들:

## 星数曲线

```mermaid
xychart-beta
    title "theeluwin/kata 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d80b1c1c3ca9` · [字段定义](../../DATASET.md)*
