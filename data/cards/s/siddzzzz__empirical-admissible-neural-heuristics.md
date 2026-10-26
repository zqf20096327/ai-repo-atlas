# siddzzzz/empirical-admissible-neural-heuristics

⭐ 25 · Python · 推送 2026-07-30 · [GitHub](https://github.com/siddzzzz/empirical-admissible-neural-heuristics) · 个人维护

**学习可采纳神经启发式以引导最优 A* 搜索的研究框架**

面向组合谜题（2x2 魔方、8 数码、Lights Out）的强化学习与启发式搜索框架，包含两个工作区：一是校准可采纳神经启发式框架，通过欠估计 Bellman 算子、非对称 Pinball 损失与事后校准偏移三层机制学习满足可采纳性（h(s)≤h*(s)）的启发式，维持 A* 路径最优保证；二是基于课程强化学习与宏动作层级的 H-DAVI 基线。提供预训练权重、训练/评测脚本与 Streamlit 交互面板，从源码运行。

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

- 三层防御（Bellman 算子+非对称损失+校准偏移）学习经验可采纳启发式
- 8 数码与 2x2 魔方上校准后可采纳率 100%、路径最优差距 0.0%
- BFS 全状态空间穷举验证（Lights Out 512 态）
- Streamlit 交互面板含 3D 可旋转魔方可视化

## 适用场景

- 研究如何在保持 A* 最优性下用神经启发式减少节点扩展
- 对比 MSE 网络与校准启发式的可采纳率与求解率
- 作为 bounded-suboptimal 方法（Weighted A*/DeepCubeA）之外的最优性替代实验基线

## 场景标签

`强化学习` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L19: Standard value network estimators trained via Mean Squared Error (MSE) regularly yield overestimations, violating t
> L100: Evaluate solve rates, average node expansions, A* node reopenings, optimality gaps, and empirical admissibility ra
> L145: * **Comparisons to Bounded-Suboptimal Baselines (Weighted A* & DeepCubeA):** Deep neural heuristic frameworks like

## 星数曲线

```mermaid
xychart-beta
    title "siddzzzz/empirical-admissible-neural-heuristics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `657b9739a22e` · [字段定义](../../DATASET.md)*
