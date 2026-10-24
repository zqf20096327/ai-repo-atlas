# yfzhang114/OneNet

⭐ 127 · Python · 推送 2026-05-25 · [GitHub](https://github.com/yfzhang114/OneNet) · 个人维护

**面向概念漂移的在线时间序列预测模型（NeurIPS 2023 官方实现）**

OneNet 论文的 PyTorch 官方实现，同时包含 Detect-then-Adapt（D3A）框架代码。OneNet 通过在线集成两个分别建模时间维度依赖与跨变量依赖的分支模型，并借助强化学习方法在在线凸规划框架内动态调整组合权重，以应对流数据下的概念漂移。D3A 先监测损失分布漂移、检测后再对模型进行激进适配。支持 ETT/ECL/Traffic/WTH 数据集与多种骨干及训练策略复现实验，依赖固定版本 Python/PyTorch 环境，通过 shell 脚本运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在线集成双分支模型并以强化学习动态调整组合权重
- Detect-then-Adapt 框架：先检测概念漂移再快速适配
- 支持 PatchTST/FedFormer/DLinear/Crossformer 等多种骨干与训练策略
- 支持 ETT/ECL/Traffic/WHL 等数据集基准复现

## 适用场景

- 复现 NeurIPS 2023 论文的在线时间序列预测实验
- 研究流数据概念漂移下的预测模型与适配方法
- 比较在线学习训练策略（OGD/经验回放/DER++ 等）

## 场景标签

 · 领域:机器学习/时间序列预测

## 证据(README 行号)

> L1: # (NeurIPS 2023) OneNet: Enhancing Time Series Forecasting Models under Concept Drift by Online Ensembling
> L12: Online updating of time series forecasting models aims to address the **concept drifting problem** by efficiently u

## 星数曲线

```mermaid
xychart-beta
    title "yfzhang114/OneNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 126 --> 128
    line [127, 127]
```

2026-10-18 127 → 2026-10-24 127（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `254a55c1d938` · [字段定义](../../DATASET.md)*
