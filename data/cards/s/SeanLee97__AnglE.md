# SeanLee97/AnglE

⭐ 575 · Python · MIT · 推送 2026-03-22 · [GitHub](https://github.com/SeanLee97/AnglE) · [官网](https://arxiv.org/abs/2309.12871) · 个人维护 · 中文 README

**面向开发者的句子嵌入训练与推理库（BERT/LLM 主干）**

出自 ACL 2024 论文 AnglE: Angle-optimized Text Embeddings 的 Python 库，用于训练和推理句子嵌入。支持 BERT、LLM、双向 LLM（BiLLM）等主干，内置 AnglE/对比/CoSENT/Espresso 多种损失函数，支持单卡与多卡（accelerate/FSDP）训练、LoRA、知识蒸馏，并提供 CLI 训练器与 Python API 两种方式。可加载第三方 transformer 模型（sentence-transformers、BGE 等），训练后可转换为 sentence-transformers 格式。官方发布 UAE 系列预训练模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 BERT/LLM/双向 LLM 主干与 LoRA 训练
- 内置 AnglE、对比、CoSENT、Espresso（ICLR 2025）损失
- 单卡/多卡训练，CLI（angle-trainer + accelerate）与 Python API
- 可加载第三方模型并将训练结果转为 sentence-transformers 格式

## 适用场景

- 训练检索或语义相似度任务用的句子嵌入模型
- 用官方 UAE 系列模型做文本嵌入与相似度计算
- 将自训嵌入模型转换为 sentence-transformers 格式接入现有系统

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L22: This library is from the paper: AnglE: Angle-optimized Text Embeddings. It allows for training state-of-the-art BER
> L27: - 📐 AnglE loss (ACL24)

## 星数曲线

```mermaid
xychart-beta
    title "SeanLee97/AnglE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 574 --> 576
    line [575, 575]
```

2026-10-18 575 → 2026-10-29 575（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9b8e4712d576` · [字段定义](../../DATASET.md)*
