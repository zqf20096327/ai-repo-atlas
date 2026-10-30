# feyninc/mtcb

⭐ 15 · Python · Apache-2.0 · 推送 2026-02-07 · [GitHub](https://github.com/feyninc/mtcb) · 组织维护

**RAG 文本分块策略评测基准（9 领域，约 1.7 万问题）**

面向 RAG 系统的文本分块（chunking）标准化评测框架：在 9 个领域（经典文学、SEC 财报、GitHub README、多语言代码、金融表格、科学论文、法律合同、医疗指南、讲座转录）共约 2,910 篇文档、16,921 个问题上，度量分块与嵌入策略的检索质量；提供每数据集约 100 题的 nano 版用于快速迭代。基于 Chonkie 构建，任何继承 chonkie.BaseChunker 的分块器开箱可用，并支持自定义语料评测与 QA 数据集生成，指标含 Recall@k/Precision@k/MRR@k/NDCG@k。以 pip 包形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 领域、约 2,910 文档、16,921 问题的完整基准与约 900 题的 nano 快速版
- 兼容任何继承 chonkie.BaseChunker 的分块器
- 支持自定义语料（SimpleEvaluator）与 QA 数据集生成（DatasetGenerator）
- 提供 Recall@k / Precision@k / MRR@k / NDCG@k 检索指标

## 适用场景

- 对比不同分块策略在自己 RAG 管线中的检索效果
- 开发分块器时用 nano 基准快速迭代验证
- 从自有文档生成经验证的 QA 评测数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: _The benchmark for evaluating chunking strategies in RAG pipelines._
> L18: MTCB (Massive Text Chunking Benchmark) is a standardized evaluation framework for text chunking in RAG systems. It 

## 星数曲线

```mermaid
xychart-beta
    title "feyninc/mtcb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a613d499e108` · [字段定义](../../DATASET.md)*
