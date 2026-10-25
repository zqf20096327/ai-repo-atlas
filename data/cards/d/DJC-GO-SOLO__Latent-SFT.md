# DJC-GO-SOLO/Latent-SFT

⭐ 61 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/DJC-GO-SOLO/Latent-SFT) · 组织维护

**教 LLM 在词表空间潜链中推理的两阶段训练框架**

论文 Latent-SFT 的官方实现，面向研究者的训练框架：将潜推理建模为词表空间的叠加链，每个潜 token 表示为词表上的概率分布。两阶段流程——Stage 1 用编码器-解码器把显式 CoT 蒸馏为 top-k 词表叠加的潜链，Stage 2 丢弃编码器，用 CE 与 KL 目标加可选 Gumbel-Softmax 扰动训练模型自主生成潜链。提供 LoRA 合并与评估脚本，默认 top-k 叠加以兼容后续 Latent-GRPO 训练，数据格式与固定 schema 强耦合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 潜 token 约束在词表嵌入空间（top-k 词法叠加）
- 两阶段训练：潜链蒸馏 + 自主潜推理（CE/KL 目标）
- 潜软标签生成、LoRA 合并与评估脚本
- 可选 Gumbel-Softmax 随机扰动增强泛化

## 适用场景

- 复现论文在 GSM8K/MATH 等任务上的潜推理训练
- 在自有 CoT 数据上训练压缩式潜推理模型
- 为后续 Latent-GRPO 强化学习阶段准备潜链模型

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L10:  Official implementation of Latent-SFT, a two-stage framework for teaching LLMs to reason in vocabulary-space laten
> L16: - **Code release**: This repository provides the training, latent soft-label generation, LoRA merging, and evaluati

## 星数曲线

```mermaid
xychart-beta
    title "DJC-GO-SOLO/Latent-SFT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7ff00929661d` · [字段定义](../../DATASET.md)*
