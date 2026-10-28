# TheLeprechaun25/NCOLib

⭐ 19 · Python · MIT · 推送 2025-11-14 · [GitHub](https://github.com/TheLeprechaun25/NCOLib) · 个人维护

**用图神经网络近似求解组合优化问题的 Python 库**

面向业界与科研人员的神经组合优化（NCO）库：通过定义问题类（状态、目标值、动作），使用图神经网络（GCN、Graph Transformer 等架构）训练模型来近似求解组合优化问题。支持神经构造式（从零自回归构造解）与神经改进式（局部修改改进现有解）两类框架，强化学习算法目前支持 Policy Gradient（构造与改进均可用），Actor Critic 与 PPO 在路线图中，监督学习部分开发中。提供训练、推理与实验功能及示例脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 GCN、Graph Transformer 等 GNN 架构，按节点/边特征与动作类型选择
- 神经构造式与神经改进式两类求解框架
- Policy Gradient 强化学习训练（POMO 数据增强、MARCO 记忆机制等已完成）
- 通过自定义问题类接入用户自己的优化问题

## 适用场景

- 研究神经组合优化方法在 TSP 等问题上的应用
- 用深度学习近似求解业务中的组合优化问题
- 实验不同 GNN 架构、数据集与超参数对比求解效果

## 场景标签

 · 领域:运筹学/深度学习

## 证据(README 行号)

> L6: The Neural Combinatorial Optimization Library (NCOLib) is an accessible software library designed to simplify the ap
> L41: We use Graph Neural Networks (GNNs) to solve combinatorial optimization problems. Different GNN architectures can b

## 星数曲线

```mermaid
xychart-beta
    title "TheLeprechaun25/NCOLib 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [20, 19, 19]
```

2026-10-18 20 → 2026-10-28 19（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5357ef28a156` · [字段定义](../../DATASET.md)*
