# F4biian/HalluRAG

⭐ 14 · Python · 推送 2026-05-04 · [GitHub](https://github.com/F4biian/HalluRAG) · 组织维护

**RAG 封闭域句子级幻觉检测数据集与分类方法实现**

论文 HalluRAG（arXiv:2412.17056）的官方代码库：提供从 Wikipedia 抓取、生成问答对、构造 RAG 提示并从 LLaMA 2 7B/13B Chat 与 Mistral 7B Instruct 提取上下文化嵌入向量与中间激活值、由 GPT-4o 标注句级幻觉的完整数据构建流程；再以 MLP 在这些内部状态上训练幻觉分类器。数据集（2.65 GB 压缩）与研究数据（6.55 GB）单独提供下载。README 首行声明推荐改用新数据集 RAGognize。构建数据需 OpenAI API key 与 GPU（实验用 NVIDIA RTX A6000），且需对 transformers 库做手动修改。

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

- 基于 LLM 内部状态（嵌入向量与中间激活值）的句级幻觉检测
- 数据构建流水线：Wikipedia 抓取→问答对生成→RAG 提示→内部状态提取→GPT-4o 标注
- 提供 MLP 分类器训练与分析脚本（含 Cohen's Kappa 等指标）
- 最终数据集 2.65 GB，全部研究数据 6.55 GB，单独下载

## 适用场景

- 研究 RAG 系统中封闭域幻觉的内部状态检测方法
- 复现论文实验或在其数据集上训练幻觉分类器
- 构建类似的幻觉检测数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: # The HalluRAG Dataset: Detecting Closed-Domain Hallucinations in RAG Applications Using an LLM's Internal States
> L5: Welcome to the official repository for **HalluRAG**, a dataset for detecting sentence-level hallucinations in Retrie
> L7: RAG-based systems combine external retrieval mechanisms with generative models to produce information-rich responses

## 星数曲线

```mermaid
xychart-beta
    title "F4biian/HalluRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `8699a8bdb048` · [字段定义](../../DATASET.md)*
