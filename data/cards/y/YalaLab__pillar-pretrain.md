# YalaLab/pillar-pretrain

⭐ 42 · Python · NOASSERTION · 推送 2026-01-13 · [GitHub](https://github.com/YalaLab/pillar-pretrain) · 组织维护

**放射学基础模型 Pillar-0 的预训练代码**

YalaLab 发布的 Pillar-0 放射学视觉-语言基础模型预训练代码仓库。覆盖依赖管理（uv）、CT 视觉特征缓存生成、基于 Qwen3-Embedding-8B 的文本嵌入缓存构建，以及通过脚本启动的 Merlin 腹部 CT 数据集单节点训练流程；也支持从 HuggingFace 数据集仓库下载预生成缓存。面向复现或开展放射学基础模型预训练的研究者；训练需依赖外部数据清单（Merlin ABD-CT）与 rad-vision-engine 仓库配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pillar-0 放射学视觉-语言基础模型的预训练流程
- 提供 CT 视觉缓存与 Qwen3-Embedding-8B 文本嵌入缓存的生成脚本
- 支持下载预生成缓存并配置 YAML 路径后直接训练

## 适用场景

- 复现 Pillar-0 放射学基础模型的预训练
- 在 Merlin 腹部 CT 数据集上训练视觉-语言模型
- 研究生成缓存驱动的放射学多模态训练流程

## 场景标签

`多模态` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository contains the pretraining code for the Pillar-0 model.
> L39: bash train_unimodal_pillar0_merlin_abd_ct_1node.sh
> L47:   title   = {Pillar-0: A New Frontier for Radiology Foundation Models},

## 星数曲线

```mermaid
xychart-beta
    title "YalaLab/pillar-pretrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b949dd9b7c66` · [字段定义](../../DATASET.md)*
