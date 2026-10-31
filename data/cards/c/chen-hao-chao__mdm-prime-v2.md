# chen-hao-chao/mdm-prime-v2

⭐ 30 · Python · 推送 2026-10-06 · [GitHub](https://github.com/chen-hao-chao/mdm-prime-v2) · [官网](https://chen-hao-chao.github.io/mdm-prime-v2/) · 组织维护

**EMNLP 2026 论文的扩散语言模型扩展性实验代码实现**

发布论文《MDM-Prime-v2: Binary Encoding and Index Shuffling Enable Scaling of Diffusion Language Models》的实验代码仓库，研究二进制编码与索引混排对扩散语言模型规模化的影响。包含两套实验：基于 Megatron 的规模分析（allenai/c4 数据集）与基于 lit_gpt 的更大规模预训练（SlimPajama-627B，1.1B 模型）。提供 Docker 环境、Hugging Face 预训练权重、Weights & Biases 训练日志与 Gradio 本地演示。注意作者曾发布勘误，指出旧版 NLL 评测存在缺陷。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Megatron 规模分析与 lit_gpt 大规模预训练两套实验代码
- Docker 镜像与 Hugging Face 预训练权重
- 提供 Weights & Biases 训练日志以复现实验
- 含 Gradio 本地推理演示（docker 启动，端口 3000）

## 适用场景

- 复现论文中的规模分析与预训练实验
- 在 SlimPajama 上预训练 1.1B 扩散语言模型
- 用预训练权重做推理与下游应用实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L16: This repository contains the code implementation of the experiments presented in the paper *MDM-Prime-v2: Binary En
> L21: - :microscope: **Code for all experiments** in our paper:
> L33: ### Larger-scale Pretraining

## 星数曲线

```mermaid
xychart-beta
    title "chen-hao-chao/mdm-prime-v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9c7fbc1d79a9` · [字段定义](../../DATASET.md)*
