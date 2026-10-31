# brandokoch/attention-is-all-you-need-paper

⭐ 253 · Jupyter Notebook · MIT · 推送 2026-08-05 · [GitHub](https://github.com/brandokoch/attention-is-all-you-need-paper) · 个人维护

**Transformer 原论文的 PyTorch 从零实现，供学习机器翻译**

对 Vaswani 等人 2017 年论文《Attention is all you need》的原始 Transformer（编码器-解码器）架构的从零实现，目标是配合论文阅读、易于理解，可在 CPU 上运行用于学习。实现 WMT14 英德翻译任务训练：训练时自动下载数据、预处理与分词，支持 BPE/WordLevel 分词器、动态 batching、梯度累积、标签平滑、BLEU 评估与 W&B 日志；提供预训练模型下载、教程 notebook 与 Streamlit 浏览器推理应用。通过 conda 环境安装，训练与推理配置集中在一个 config 文件中。

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

- 可在 CPU 与 GPU 上运行的原始 Transformer 实现
- WMT14 英德翻译训练：自动下载数据、BPE/WordLevel 分词、动态 batching
- 预训练模型下载与 Streamlit 浏览器推理应用
- W&B 集成记录训练指标，教程 notebook 讲解架构

## 适用场景

- 边读原论文边对照代码理解 Transformer 架构
- 在 CPU 上小规模跑通机器翻译训练流程
- 用自己的配置训练或微调英德翻译模型

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This is my from-scratch implementation of the original transformer architecture from the following paper: Vaswani, A
> L90: $ python train.py

## 星数曲线

```mermaid
xychart-beta
    title "brandokoch/attention-is-all-you-need-paper 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 252 --> 255
    line [254, 253, 253]
```

2026-10-18 254 → 2026-10-31 253（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3545db0b0088` · [字段定义](../../DATASET.md)*
