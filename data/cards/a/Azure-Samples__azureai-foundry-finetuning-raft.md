# Azure-Samples/azureai-foundry-finetuning-raft

⭐ 81 · Jupyter Notebook · MIT · 推送 2026-09-02 · [GitHub](https://github.com/Azure-Samples/azureai-foundry-finetuning-raft) · 组织维护

**开发者的 RAFT 微调教程：在 Azure AI 上生成数据集并微调部署模型**

Azure 官方示例仓库，提供一套 RAFT（Retrieval Augmented Fine-Tuning）操作流程：用 GPT-4o 或 Llama 3.1 405B 作为教师模型生成合成训练集，微调学生模型（如 GPT-4o-mini 或 Llama 3.1 8B）以提升 RAG 精度，再部署并与基线模型对比评测。基础设施通过 Azure Developer CLI（azd）自动供给，可用 Codespaces/Dev Container 运行；流程以 6 个 notebook 组织，支持 papermill 参数化命令行执行，并给出各步骤运行时长与费用估算。仅面向 Azure 平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 教师模型生成合成数据集，微调学生模型提升 RAG 能力
- azd 自动供给全部 Azure 基础设施
- 6 个 notebook 覆盖生成/微调/部署/评测全流程
- 支持 OpenAI API 与 Azure OpenAI 两种接入方式

## 适用场景

- 在 Azure 上跑通 RAFT 微调以提升 RAG 问答精度
- 用大模型蒸馏生成领域训练数据
- 对比微调模型与基线模型的 RAG 表现

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository is a recipe that will walk you through improving RAG system precision using UC Berkeley's RAFT techn
> L7: This recipe uses either OpenAI GPT-4o or Meta Llama 3.1 405B as a teacher model deployed on Azure AI to generate a s

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azureai-foundry-finetuning-raft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-28 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f5f68cde67b1` · [字段定义](../../DATASET.md)*
