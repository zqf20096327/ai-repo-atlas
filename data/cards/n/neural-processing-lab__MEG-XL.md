# neural-processing-lab/MEG-XL

⭐ 19 · Python · MIT · 推送 2026-05-13 · [GitHub](https://github.com/neural-processing-lab/MEG-XL) · [官网](https://arxiv.org/abs/2602.02494) · 组织维护

**MEG/EEG 长上下文预训练模型：数据高效地把脑信号解码为文本**

ICML 2026 论文的官方代码：在 MEG 上进行长上下文预训练学习可迁移表征，微调后实现 brain-to-text 词级解码，据 README 称在下游数据需求显著减少的情况下达到 state-of-the-art 精度。提供 HuggingFace 预训练权重下载、微调与线性探针评估脚本、多数据集（CamCAN/MOUS/LibriBrain 等）预训练配置，基于 PyTorch/Hydra。限制：微调与预训练需 1 块 80GB VRAM GPU，线性探针需 40GB。面向神经解码研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MEG 长上下文自监督预训练，产出可迁移表征
- 支持微调与线性探针两种 brain-to-text 评估路径
- 预训练权重托管于 HuggingFace，含 Hydra 配置
- 支持 Armeni/Gwilliams/LibriBrain 等多个微调数据集

## 适用场景

- 在公开 MEG 数据集上微调做脑信号词级解码实验
- 复现或扩展论文中的长上下文预训练流程
- 用线性探针评估预训练表征质量

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: **MEG-XL** is a pre-trained model for non-invasive electrophysiological brain signals (MEG/EEG) published at ICML 20
> L9: **Paper:** arXiv:2602.02494 | **Model weights:** HuggingFace

## 星数曲线

```mermaid
xychart-beta
    title "neural-processing-lab/MEG-XL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `106a78dfc298` · [字段定义](../../DATASET.md)*
