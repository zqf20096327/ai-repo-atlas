# gchochla/LLM-multilabel-differently

⭐ 19 · Python · 推送 2026-02-28 · [GitHub](https://github.com/gchochla/LLM-multilabel-differently) · [官网](https://arxiv.org/abs/2505.17510) · 组织维护

**EMNLP 2025 论文官方实现：研究 LLM 多标签分类行为**

论文 "LLMs do Multi-Label Classification Differently"（EMNLP 2025 Main）的官方代码库。研究自回归 LLM 在主观任务多标签分类中的行为：分析每步生成的输出分布，发现模型在每步倾向于抑制除一个标签外的其他标签；随模型规模增大，token 分布熵降低但标签内部排序改善；SFT 与强化学习会放大该现象。提出多标签场景的分布对齐任务及零样本与监督方法。提供 bash 脚本在 GoEmotions、MFRC 数据集上运行实验，支持 HuggingFace 模型与可选 vllm 加速，需要 Python 3.10 与 OpenAI key（GPT 实验时）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 分析 LLM 逐步生成输出分布的多标签分类研究代码
- 提出分布对齐任务：对齐 LLM 标签分布与标注者经验分布
- 提供零样本与监督两类对齐方法
- 支持 GoEmotions、MFRC 数据集与 HuggingFace 模型，vllm 加速选项（未测试）

## 适用场景

- 复现论文中的多标签分类行为分析与图表
- 研究主观任务上 LLM 标签分布与人类标注分布的对齐
- 在自定义 HuggingFace 模型上运行多标签实验管线

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repo contains the official implementation of Large Language Models do Multi-Label Classification Differently, t
> L9: > Multi-label classification is prevalent in real-world settings, but the behavior of Large Language Models (LLMs) i

## 星数曲线

```mermaid
xychart-beta
    title "gchochla/LLM-multilabel-differently 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c525de527874` · [字段定义](../../DATASET.md)*
