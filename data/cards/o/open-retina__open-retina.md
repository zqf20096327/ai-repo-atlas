# open-retina/open-retina

⭐ 25 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/open-retina/open-retina) · [官网](https://open-retina.org) · 组织维护

**开源视网膜神经网络模型库：跨数据集与物种建模**

计算神经科学领域的视网膜神经网络模型仓库，包含预训练模型（如 hoefling_2024），支持下载模型并运行前向推理以预测视网膜对刺激的响应；支持通过 notebook、CLI 配置训练自定义模型，并允许接入新数据集。代码改编自 sinzlab/neuralpredictors，训练基于 PyTorch Lightning 与 Hydra 配置，模型可托管于 Hugging Face 供远程加载。提供 pip 安装与源码开发两种方式，有 DOI 与配套预印本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供可下载的预训练视网膜模型并支持 CPU 前向推理
- 支持 notebook 与 CLI 配置两种训练方式及新数据集接入
- 基于 PyTorch Lightning 与 Hydra 的训练配置体系

## 适用场景

- 下载预训练模型预测视网膜对视觉刺激的响应
- 在自己的数据集上训练视网膜响应模型
- 作为计算神经科学研究的可复现模型基础设施

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L12: Open-source repository containing neural network models of the retina.
> L13: The models in this repository are inspired by and contain adapted code of sinzlab/neuralpredictors. Accompanying pr

## 星数曲线

```mermaid
xychart-beta
    title "open-retina/open-retina 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d3bfbb9a3b46` · [字段定义](../../DATASET.md)*
