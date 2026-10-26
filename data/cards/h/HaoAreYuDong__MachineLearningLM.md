# HaoAreYuDong/MachineLearningLM

⭐ 60 · Python · MIT · 推送 2025-12-12 · [GitHub](https://github.com/HaoAreYuDong/MachineLearningLM) · [官网](https://huggingface.co/MachineLearningLM) · 组织维护

**在表格 ML 任务上扩展 many-shot 上下文学习的 LLM 与评测框架**

配套 arXiv 2509.06806 论文的模型与代码仓库：提供在 Hugging Face 发布的 MachineLearningLM 模型、开源的预训练数据集（Warmup 与 Full，分片托管），以及一整套 LLM 机器学习任务评测框架——覆盖数据预处理、prompt 生成、模型推理与多指标评测，支持传统 ML 与深度学习两类模型、单/多进程与端到端流水线，可本地加载模型或经 OpenAI SDK 调用云端模型。另含基于 TabICL 代码的先验数据生成脚本与基于 LLaMA-Factory 的训练流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评测框架覆盖数据预处理→prompt 生成→推理→评测→报告的完整流水线
- 支持本地模型与 openai:: 前缀的云端模型调用两种推理方式
- 基于 TabICL 代码生成先验数据，特征值归一化到 0–999
- 训练基于 LLaMA-Factory 框架

## 适用场景

- 复现论文中表格任务上 many-shot 上下文学习实验
- 评测 LLM 与传统 ML 模型在机器学习任务上的表现
- 生成结构因果模型先验数据用于继续预训练

## 场景标签

`模型评测` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L1: # MachineLearningLLM: Scaling Many-shot In-context Learning via Continued Pretraining
> L21: A comprehensive framework for evaluating Large Language Models on machine learning tasks, supporting both tradition
> L25: This framework provides end-to-end evaluation capabilities for LLMs on machine learning tasks, featuring automated 

## 星数曲线

```mermaid
xychart-beta
    title "HaoAreYuDong/MachineLearningLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-26 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `057bf239f07a` · [字段定义](../../DATASET.md)*
