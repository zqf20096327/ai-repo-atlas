# amathislab/DeepDraw

⭐ 17 · Jupyter Notebook · MIT · 推送 2026-10-20 · [GitHub](https://github.com/amathislab/DeepDraw) · [官网](https://www.mathislab.org/deepdraw) · 组织维护

**本体感觉任务驱动建模代码：从肌梭输入训练层级网络识别动作**

eLife 2023 论文的官方代码仓库，实现任务驱动的本体感觉建模：基于运动学数据生成可扩展的肌梭数据集（PCRT 数据集），定义动作识别基准任务，训练层级深度神经网络，并对模型做 RDM、调谐曲线、tSNE、CKA 等神经科学分析。代码分为数据生成、SVM 分析、网络训练、表征分析、单单元分析五部分，各含独立说明。运行环境分两套：Docker 容器（含 OpenSim 与 TensorFlow）用于数据生成与训练，conda 环境用于分析，二者不互通。数据集与训练权重共享于 Dropbox 与 Zenodo。NN 训练需 GPU，数据集约 30GB，全量分析数据约 88GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于运动学数据生成肌梭数据集并定义动作识别基准（PCRT）
- 提供 Docker 容器（OpenSim + TensorFlow）复现训练环境
- 共享 PCRT 数据集（~30GB）与全部训练网络权重（~3.5GB）
- RDM、调谐曲线、tSNE、CKA 等模型-神经对比分析

## 适用场景

- 复现论文的本体感觉任务驱动建模结果
- 使用 PCRT 数据集与预训练权重开展模型-大脑对比分析
- 基于行为目标推导本体感觉神经调谐特性

## 场景标签

 · 领域:计算神经科学

## 证据(README 行号)

> L13: - We provide a normative approach to derive neural tuning of proprioceptive features from behaviorally-defined obje
> L15: - Hierarchical neural networks solve the recognition task from muscle spindle inputs.
> L33: 3. Classifying the PCRT Dataset using various network models. Code in `nn-training`

## 星数曲线

```mermaid
xychart-beta
    title "amathislab/DeepDraw 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-26 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fe43d5bc890f` · [字段定义](../../DATASET.md)*
