# technion-cs-nlp/BiologicalTokenizers

⭐ 24 · Python · MIT · 推送 2025-12-31 · [GitHub](https://github.com/technion-cs-nlp/BiologicalTokenizers) · [官网](https://academic.oup.com/bioinformatics/article/40/4/btae196/7645044) · 组织维护

**研究生物序列分词算法对 Transformer 效果影响的代码与数据**

论文配套仓库：研究 BPE、WordPiece、Unigram 等分词算法替代单字符分词对生物序列（蛋白质/DNA）Transformer 模型的影响，覆盖 8 个生物学任务（蛋白质功能与稳定性预测、核苷酸序列比对、蛋白质家族分类等）。提供训练脚本 train_tokenizer_bert.py，支持配置分词类型、词表大小、BERT 层数等参数，含 7 个数据集的训练/验证/测试数据，以及在 BFD 蛋白质数据集（超 4000 亿氨基酸）上预训练的分词器。代码以 CC-BY 4.0 提供，发表于 Bioinformatics 2024。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 BPE/WordPiece/Unigram/WORDS/PAIRS 五种分词算法的训练评估脚本
- 含论文 8 个数据集中 7 个的训练/验证/测试数据
- 提供在 BFD 蛋白质数据集上训练的分词器，按训练样本数/类型/词表大小组织
- 支持配置 BERT 层数、注意力头数、隐藏维度、任务类型等参数

## 适用场景

- 复现论文中生物序列分词对 Transformer 效果的实验
- 为蛋白质/DNA 任务训练基于 BERT 的分类或回归模型
- 获取 BFD 大规模蛋白质预训练分词器用于下游任务

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Deep-learning models are transforming biological research, including many bioinformatics and comparative genomics al
> L20: You can use the provided script `train_tokenizer_bert.py` to perform the training and evaluation.

## 星数曲线

```mermaid
xychart-beta
    title "technion-cs-nlp/BiologicalTokenizers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5c78dfeaf011` · [字段定义](../../DATASET.md)*
