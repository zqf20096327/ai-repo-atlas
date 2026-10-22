# baal-org/baal

⭐ 936 · Python · Apache-2.0 · 推送 2025-12-03 · [GitHub](https://github.com/baal-org/baal) · [官网](https://baal.readthedocs.io) · 组织维护

**给研究与工业界的贝叶斯主动学习 PyTorch 库**

Python 主动学习库，面向科研与工业场景。支持 Monte-Carlo Dropout、MCDropConnect、深度集成与半监督学习等方法估计预测不确定性；框架由 ActiveLearningDataset、Heuristics、ModelWrapper、ActiveLearningLoop 四部分组成，自动从未标注池中挑选最不确定样本进行标注。基于 PyTorch，要求 Python>=3.10，提供 pip 安装与 Docker 复现实验脚本。最初在 ElementAI 开发，现为独立维护，团队含 3 名维护者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Monte-Carlo Dropout、MCDropConnect、深度集成、半监督学习的不确定性估计
- 四组件框架：ActiveLearningDataset/Heuristics/ModelWrapper/ActiveLearningLoop
- 自动计算不确定性并从未标注池中选择最不确定样本
- 提供 Docker 复现实验与 CIFAR10 示例脚本

## 适用场景

- 训练模型时减少人工标注量，优先标注最有价值的样本
- 研究不确定性估计与主动学习方法并复现论文实验
- 在生产流水线中集成主动学习标注循环

## 场景标签

 · 领域:机器学习/数据标注

## 证据(README 行号)

> L22: Baal is an active learning library that supports both industrial applications and research usecases.
> L67: At the moment Baal supports the following methods to perform active learning.
> L99: Finally, _**ActiveLearningLoop**_ automatically computes the uncertainty and label the most

## 星数曲线

```mermaid
xychart-beta
    title "baal-org/baal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 935 --> 937
    line [936, 936]
```

2026-10-18 936 → 2026-10-22 936（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `332e76f1ed17` · [字段定义](../../DATASET.md)*
