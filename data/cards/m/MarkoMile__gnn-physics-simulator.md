# MarkoMile/gnn-physics-simulator

⭐ 15 · Jupyter Notebook · MIT · 推送 2026-03-02 · [GitHub](https://github.com/MarkoMile/gnn-physics-simulator) · 个人维护

**用 GNN 学习流体粒子动力学的 PyTorch Geometric 实现（课程项目）**

复现 Sanchez-Gonzalez et al. (2020) 的 Learning to Simulate 架构：以 Encode-Process-Decode 与 InteractionNetwork 消息传递，从粒子局部交互预测加速度，模拟流体。流程为先在 DeepMind WaterDrop 数据集预训练，再在自研 WCSPH（弱可压缩光滑粒子流体力学）数值模拟器生成的数据集上微调；WCSPH 模拟器采用 Symplectic Euler 积分并经 Numba JIT 优化。作为诺维萨德大学数值算法课程作业开发，提供配置化训练/微调脚本、数据生成脚本与 Kaggle notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Encode-Process-Decode + InteractionNetwork 的 GNN 流体模拟复现
- 自研 WCSPH 数值模拟器（边界粒子、Symplectic Euler、Numba JIT）
- 支持 WaterDrop 预训练与自生成 WCSPH 数据集微调
- 提供 Kaggle-ready 训练与微调 notebook

## 适用场景

- 复现论文的图网络物理模拟方法
- 对比数值积分器与深度学习消息传递方法
- 生成 WCSPH 流体数据集用于 GNN 训练

## 场景标签

 · 领域:科学计算/物理仿真

## 证据(README 行号)

> L5: A PyTorch Geometric implementation of Learning to Simulate Complex Physics with Graph Networks (Sanchez-Gonzalez et 
> L25: 4. **GNN Architecture:** An Encode-Process-Decode approach using `InteractionNetwork` message passing blocks, trans

## 星数曲线

```mermaid
xychart-beta
    title "MarkoMile/gnn-physics-simulator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3f847475cea7` · [字段定义](../../DATASET.md)*
