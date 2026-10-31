# SnowNation101/Nyx

⭐ 14 · Python · MIT · 推送 2025-12-06 · [GitHub](https://github.com/SnowNation101/Nyx) · 组织维护

**论文实现：面向通用 RAG 的混合模态检索器 Nyx 与数据集 NyxQA**

SIGIR'26 论文的官方实现仓库，提出统一混合模态检索器 Nyx，用于通用检索增强生成（URAG）场景；配套构建大规模混合模态问答数据集 NyxQA。框架包含四阶段自动生成多模态问答对的流水线，以及先在 NyxQA 上预训练、再用 VLM 反馈做监督微调的两阶段训练方法。核心实现基于 VLM2Vec，使用 PyTorch、faiss-cpu、transformers 等依赖，通过 Conda 环境安装，模型发布于 Hugging Face Collection。

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

- 面向 URAG 场景的统一混合模态检索器
- 四阶段自动生成多模态 QA 对的流水线
- NyxQA 大规模混合模态问答数据集
- 两阶段训练：NyxQA 预训练 + VLM 反馈监督微调

## 适用场景

- 在文本与图文混合的 RAG 任务中做检索
- 复现论文实验或在其基础上训练检索模型
- 使用 NyxQA 数据集训练/评测混合模态检索

## 场景标签

`RAG` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L24: This repository contains the official implementation of our paper *"Towards Mixed-Modal Retrieval for Universal Ret
> L27: We propose **Nyx**, a unified mixed-modal retriever tailored for URAG scenarios, and construct **NyxQA**, a large-s
> L29: - A two-stage training framework combining pre-training on NyxQA and supervised fine-tuning with VLM feedback.

## 星数曲线

```mermaid
xychart-beta
    title "SnowNation101/Nyx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `50a3341890e9` · [字段定义](../../DATASET.md)*
