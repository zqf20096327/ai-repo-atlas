# MLI-lab/ProPicker

⭐ 14 · Jupyter Notebook · 推送 2026-03-30 · [GitHub](https://github.com/MLI-lab/ProPicker) · 组织维护

**冷冻电子断层扫描图中基于提示的颗粒挑选与微调工具**

ProPicker 的论文实现，面向 cryo-ET 颗粒挑选：提供基于提示的挑选、针对特定颗粒的微调，以及从零训练的代码。使用 TomoTwin 模型作为提示编码器，需下载预训练 ProPicker 检查点与 TomoTwin 检查点并设置环境变量。通过 Conda 环境加 pip 安装，提供 Jupyter notebook 教程入口与实验性 GUI/CLI 交互探索；训练数据体积较大。仓库含修改自 DeepETPicker、DeePiCt、TomoTwin 的代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于提示（prompt-based）的颗粒挑选与针对特定颗粒的微调
- 提供从零训练代码与训练数据下载脚本
- Jupyter notebook 教程入口与实验性 GUI/CLI

## 适用场景

- 在 cryo-ET 断层图中挑选颗粒颗粒
- 针对目标颗粒类型做数据高效的微调
- 复现论文中的定性行为与性能趋势

## 场景标签

`目标检测` `微调` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L2: This repo contains an implementation of ProPicker as described in our paper.
> L3: The repo covers prompt-based picking and particle-specific fine-tuning. We also provide code to train ProPicker from

## 星数曲线

```mermaid
xychart-beta
    title "MLI-lab/ProPicker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5e6f5c83775b` · [字段定义](../../DATASET.md)*
