# hsilvosa/hsc-mtl-wuxia

⭐ 33 · Jupyter Notebook · 推送 2026-08-03 · [GitHub](https://github.com/hsilvosa/hsc-mtl-wuxia) · 个人维护

**武侠小说中英机器翻译的本科论文研究实现与评测框架**

西班牙拉科鲁尼亚大学本科毕业论文（TFG）的配套仓库，包含实现代码、数据集、流水线配置与评测框架。研究对比三种机器翻译范式（SMT/NMT/微调 LLM）在武侠文学中译英上的表现：含语料切分与 LaBSE 对齐流水线、NLTK IBM 模型的 SMT 基线、四个 NMT 模型微调、五个 LLM 的 QLoRA 微调，以及 BLEU/COMET 等自动指标和 LLM-as-a-Judge 定性评测。数据集与微调模型发布于 Hugging Face Hub。依赖 pip 安装，LLM 实验在 CESGA HPC 节点上以 sbatch 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端流水线：原始文本→切分→LaBSE 跨语对齐→平行语料
- SMT/NMT/LLM 三范式对比，LLM 采用 QLoRA 微调
- 量化评测（SacreBLEU/chrF2/ROUGE-L/METEOR/COMET）与 LLM-as-a-Judge 定性评测
- 数据集与微调模型公开在 Hugging Face Hub

## 适用场景

- 复现武侠/仙侠文学领域的机器翻译对比实验
- 获取已对齐的武侠中英平行语料用于训练
- 参考 QLoRA 微调大模型做领域适配的流程

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L9: This repository contains the implementation, datasets, pipeline configurations, and evaluation frameworks for the Ba
> L30: This project implements an end-to-end pipeline from raw, unaligned web/book sources to fine-tuned advanced sequence
> L170: Following the LLM-as-a-Judge paradigm, validation protocols utilize state-of-the-art closed engines (Claude 3.5 So


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `bfe69d0bc89d` · [字段定义](../../DATASET.md)*
