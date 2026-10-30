# energnn/energnn

⭐ 32 · Python · MPL-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/energnn/energnn) · [官网](https://energnn.readthedocs.io) · 组织维护

**面向能源网络的图神经网络库，基于 JAX/Flax**

基于 JAX 与 Flax 构建的图神经网络库，面向现实能源网络与大型复杂工业基础设施。核心提供 Hyper Heterogeneous Multi Graph（H2MG）数据表示、对结构变化（停电、重构等）具备鲁棒性的 GNN 库，以及将 GNN 应用于优化、仿真等自定义场景的接口。快速上手示例展示训练 GNN 求解以图建模的线性系统（DC 潮流）。支持 PyPI 安装，提供 GPU 与可视化 extras，由 RTE、列日大学、INRIA 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hyper Heterogeneous Multi Graph（H2MG）数据表示
- 对网络结构变化（停电、重构等）鲁棒的 GNN
- 可应用于优化、仿真等自定义场景的接口

## 适用场景

- 在电网等能源网络上训练 GNN 做仿真或优化
- 将带异构元素的复杂工业基础设施建模为图并训练模型
- 求解以图建模的线性系统如 DC Power Flow

## 场景标签

 · 领域:能源系统/图机器学习

## 证据(README 行号)

> L11: A Graph Neural Network library based on JAX and Flax, specifically
> L17: - A **Graph Neural Network** (GNN) library robust to structure variations (outages, reconfigurations, etc.).

## 星数曲线

```mermaid
xychart-beta
    title "energnn/energnn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a24cb496b789` · [字段定义](../../DATASET.md)*
