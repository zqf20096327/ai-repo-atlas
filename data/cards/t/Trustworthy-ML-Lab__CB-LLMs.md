# Trustworthy-ML-Lab/CB-LLMs

⭐ 35 · Python · 推送 2026-02-05 · [GitHub](https://github.com/Trustworthy-ML-Lab/CB-LLMs) · [官网](https://lilywenglab.github.io/CB-LLMs/) · 组织维护

**构建内在可解释 LLM 的研究框架（ICLR 2025 论文代码）**

ICLR 2025 论文 Concept Bottleneck Large Language Models 的官方代码库，提出将预训练 LLM 改造为内在可解释模型的概念瓶颈框架，分分类与文本生成两部分。分类部分含自动概念打分（ACS）、概念瓶颈层训练、最终预测器训练与基线黑盒模型对比；生成部分基于 Llama3 LoRA 微调，支持概念检测、可操控性测试、困惑度评估与概念神经元干预生成。提供 Hugging Face 上的微调后 checkpoint 供跳过训练，推荐 cuda12.1/python3.10/pytorch2.2 环境，代码以脚本与 pip requirements 形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将预训练 LLM 转换为基于人类可理解概念的内在可解释模型
- 分类与文本生成两类任务均支持，含自动概念打分（ACS）与自动概念修正（ACC）
- 生成部分支持概念神经元干预，改变激活值可使输出包含指定概念
- 提供微调后 checkpoint（Hugging Face），可跳过训练过程

## 适用场景

- 研究者复现或扩展概念瓶颈可解释 LLM 方法
- 构建可解释的文本分类模型并输出基于概念的解释
- 通过干预概念神经元控制文本生成方向

## 场景标签

 · 领域:可解释AI/NLP

## 证据(README 行号)

> L6: * In this work, we proposed **Concept Bottleneck Large Language Model (CB-LLM)**, the first framework for building *
> L8:  * **CB-LLM (classification):** Transforming pre-trained LLMs into interpretable LLMs for text classification
> L9:  * **CB-LLM (generation):** Transforming pre-trained LLMs into interpretable LLMs for text generation

## 星数曲线

```mermaid
xychart-beta
    title "Trustworthy-ML-Lab/CB-LLMs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7fc0df8fd872` · [字段定义](../../DATASET.md)*
