# ymcui/Chinese-Mixtral

⭐ 613 · Python · Apache-2.0 · 推送 2026-04-19 · [GitHub](https://github.com/ymcui/Chinese-Mixtral) · [官网](https://arxiv.org/abs/2403.01851) · 个人维护 · 中文 README

**中文增量训练的 Mixtral MoE 开源大模型及训练脚本**

基于 Mistral.ai 的 Mixtral-8x7B-v0.1，用大规模中文无标注语料做增量训练得到 Chinese-Mixtral 基座模型，再用约 500 万条指令数据精调出 Chinese-Mixtral-Instruct 指令模型。模型实际参数量约 46.7B、推理激活约 13B，原生支持 32K 上下文（实测可达 128K），llama.cpp 量化推理最低需 16G 内存或显存。提供完整版、LoRA 版与 GGUF 量化版下载，开源预训练与指令精调脚本，并支持 transformers、llama.cpp、vLLM、text-generation-webui、LangChain 等生态部署。面向需要中文 MoE 大模型的研究者与开发者。发布有技术报告与 C-Eval/CMMLU/MMLU/LongBench 评测结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 开源中文 Mixtral 基座与 Instruct 指令模型（8x7B，激活约 13B）
- 原生 32K 上下文，实测可达 128K
- 提供预训练与指令精调脚本，用户可进一步训练微调
- 提供完整版/LoRA/GGUF 三种模型形态及量化、本地 CPU/GPU 部署教程

## 适用场景

- 本地部署中文对话或文本续写大模型
- 在中文 NLU 与长文本任务上复现或对比评测
- 基于开源脚本继续训练或微调中文 MoE 模型

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L7: 本项目基于Mistral.ai发布的Mixtral模型进行开发，该模型使用了稀疏混合专家模型（Sparse MoE）架构。本项目利用大规模中文无标注数据进行了中文增量训练，得到了**中文Mixtral**基础模型，并且进一步通过指令
> L13: - 🚀 开源中文Mixtral基础模型，该模型在Mixtral-8x7B-v0.1的基础上进行了中文增量训练
> L14: - 🚀 开源中文Mixtral-Instruct指令模型，该模型在中文Mixtral的基础上进一步进行了指令精调

## 星数曲线

```mermaid
xychart-beta
    title "ymcui/Chinese-Mixtral 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 612 --> 614
    line [613, 613]
```

2026-10-18 613 → 2026-10-31 613（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `089c161a2f4e` · [字段定义](../../DATASET.md)*
