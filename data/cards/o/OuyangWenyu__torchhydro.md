# OuyangWenyu/torchhydro

⭐ 31 · Python · NOASSERTION · 推送 2026-08-18 · [GitHub](https://github.com/OuyangWenyu/torchhydro) · 个人维护

**PyTorch 流域水文建模框架：数据集、模型与训练**

基于 PyTorch 的深度学习水文建模框架，提供 LSTM 变体、Seq2Seq/Transformer、可微分物理模型（DPL-XAJ/HBV/GR4J）、图神经网络、MoE、Diffusion/FNO 等模型，通过 hydrodataset/hydrodatasource 统一解析 CAMELS 系列、Caravan 等 10+ 标准数据集与自定义数据源。支持标准监督、迁移学习、多任务学习与联邦学习四种训练模式，集成 Lightning Fabric 分布式训练与 SHAP 可解释性。需 Python 3.10+，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 LSTM、可微分物理模型、GNN、MoE、Diffusion/FNO 等模型族
- 统一数据解析器支持 10+ 标准数据集与自定义/云端数据源
- 支持迁移学习、多任务学习与联邦学习训练模式
- Lightning Fabric 分布式训练与 SHAP 模型可解释性

## 适用场景

- 在 CAMELS-US 等流域数据集上训练径流预测模型
- 跨流域做迁移学习或多任务水文建模
- 用可微分物理模型结合深度学习做水文模拟

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: A PyTorch-based deep learning framework for hydrological modeling. Supports Normal, Transfer Learning, Multi-Task Le
> L61: |Category|Models|

## 星数曲线

```mermaid
xychart-beta
    title "OuyangWenyu/torchhydro 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `22caa4aa26f4` · [字段定义](../../DATASET.md)*
