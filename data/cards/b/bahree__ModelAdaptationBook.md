# bahree/ModelAdaptationBook

⭐ 17 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/bahree/ModelAdaptationBook) · 个人维护

**《LLM Customization and Fine-Tuning》一书配套代码：开源权重 LLM 端到端适配**

Manning 出版社图书《LLM Customization and Fine-Tuning: Adaptation, Distillation, and Alignment》的配套仓库，包含按章节组织的可运行代码、数据与示例。内容覆盖提示词/RAG、LoRA/QLoRA、全参数 SFT、蒸馏与 DPO 对齐，以及生产运维（漂移检测、回滚、安全监控），全书以 Qwen3-4B-Instruct 为贯穿示例模型，在单卡 GPU 上复现书中数据。数据集由 Stack Exchange IT 问答与 Databricks Dolly 混合构成，用脚本自行构建并附来源署名。面向 ML/AI 工程师、数据科学家与 MLOps 工程师，需具备 Python 与命令行基础。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖提示词→LoRA/QLoRA→全量 SFT→蒸馏→DPO 的完整适配技术谱系
- 全书以 Qwen3-4B 单模型贯穿，LoRA 微调可在 12GB 单卡 10 分钟内完成（第2章）
- 训练后的各章模型发布到 Hugging Face 仓库，无 GPU 也可运行推理与评估
- 数据集自行构建（Stack Exchange IT 问答 + Dolly 混合），来源署名、可审计

## 适用场景

- 跟随书中章节动手实践 LLM 微调、蒸馏与对齐技术
- 在自有 GPU 上用可复现代码比较不同适配方案的成本与效果
- 搭建企业领域助手的训练数据管线与生产监控（漂移检测/回滚）

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: Welcome to the code repository for **LLM Customization and Fine-Tuning: Adaptation, Distillation, and Alignment** (
> L13: This repository contains all the runnable code, data, and examples from the book, organized by chapter.
> L26: This book is a practitioner's playbook for adapting large language models to specific use cases in a production set

## 星数曲线

```mermaid
xychart-beta
    title "bahree/ModelAdaptationBook 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-26", "2026-10-31"]
    y-axis "stars" 13 --> 18
    line [14, 15, 16, 17, 17]
```

2026-10-18 14 → 2026-10-31 17（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `10a432171d00` · [字段定义](../../DATASET.md)*
