# OuyangWenyu/HydroDHM

⭐ 23 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/OuyangWenyu/HydroDHM) · 个人维护 · 中文 README

**面向资料稀缺流域的可微分水文模型：日径流预测**

基于 PyTorch 的可微分水文建模框架，包含新安江（XAJ）物理模型的命令行率定、评估与可视化工具，支持 SCE-UA/GA/scipy 多种优化算法；同时提供 LSTM 纯深度学习模型与 DPL-XAJ 物理约束混合模型，用于日径流预测。支持 CAMELS 数据集（自动下载约 15GB）与自定义数据，基于 hydromodel 与 torchhydro 构建，为论文配套代码，供水文研究者复现实验与开展混合建模。

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

- XAJ 物理模型命令行率定/评估/可视化（SCE-UA、GA、scipy 优化）
- LSTM 与 DPL-XAJ 物理约束混合深度学习模型
- CAMELS 数据集自动下载与自定义水文数据支持
- 发布级评估指标与可视化输出

## 适用场景

- 在缺资料流域做日径流预测与模型率定
- 复现论文中的可微分水文模型实验
- 对比物理模型、LSTM 与物理-ML 混合模型的预测表现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: - LSTM neural networks for streamflow prediction
> L15: - DPL-XAJ: Hybrid physics-constrained deep learning model

## 星数曲线

```mermaid
xychart-beta
    title "OuyangWenyu/HydroDHM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f48b4c47dbd6` · [字段定义](../../DATASET.md)*
