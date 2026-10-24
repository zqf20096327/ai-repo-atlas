# Thinklab-SJTU/EDA-AI

⭐ 327 · C · MIT · 推送 2025-11-23 · [GitHub](https://github.com/Thinklab-SJTU/EDA-AI) · 组织维护 · 中文 README

**芯片布局布线深度学习论文的官方代码实现集合**

上海交大 Thinklab 维护的 EDA+AI 论文实现仓库，收录 DeepPlace（联合布局布线）、PRNet、HubRouter（全局布线）、PreRoutGNN（时序预测）、FlexPlanner（3D 布图规划强化学习）、DSBRouter（扩散桥全局布线）与 OAREST（直角斯坦纳最小树）共七篇 NeurIPS/AAAI/ICML 论文的代码，均发表于 2021-2025 年。README 仅列论文与引用信息，未提供安装或运行说明，各实现的使用方式需进入对应子目录查看。适合芯片设计自动化方向的研究者复现与对比方法。

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

- 覆盖 7 篇顶会论文（NeurIPS/AAAI/ICML 2021-2025）的布局、布线、时序预测实现
- 方法包括强化学习、生成式网络、GNN 预训练、扩散 Schrödinger 桥
- 以 PyTorch 为实现框架（仓库主题标签）

## 适用场景

- 复现芯片布局布线与时序预测的深度学习方法
- 在论文基础上开展 EDA+AI 方向研究
- 引用与对比相关方法时查找官方实现

## 场景标签

 · 领域:芯片设计自动化（EDA）/深度学习

## 证据(README 行号)

> L1: # Implementations of
> L2: - NeurIPS 2021 paper "On Joint Learning for Solving Placement and Routing in Chip Design" (*DeepPlace*)
> L7: - ICML 2025 paper "DSBRouter: End-to-end Global Routing via Diffusion Schr¨odinger Bridge" (*DSBRouter*)

## 星数曲线

```mermaid
xychart-beta
    title "Thinklab-SJTU/EDA-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 326 --> 328
    line [327, 327]
```

2026-10-18 327 → 2026-10-24 327（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7f4a4f012ad7` · [字段定义](../../DATASET.md)*
