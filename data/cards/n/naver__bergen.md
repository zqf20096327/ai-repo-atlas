# naver/bergen

⭐ 282 · Jupyter Notebook · NOASSERTION · 推送 2026-07-14 · [GitHub](https://github.com/naver/bergen) · 组织维护

**RAG 系统评测基准库：统一评测检索与生成各组件**

面向问答场景的 RAG 系统基准评测库，管道为 retriever → reranker → LLM，支持 20+ 检索器、4 种重排器和 20+ 大模型，通过 YAML 与命令行配置实验。提供 Match、EM、LLMEval 等评测指标及 LLM 作为裁判的两两对比，支持多语言实验与 LoRA 训练配置，并附多篇数据集上的基线结果表。以 Python 脚本形式运行，许可证为 CC BY-NC-SA 4.0（禁止商用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 20+ 检索器、4 种重排器、20+ 大模型
- YAML 配置实验，含 Match/EM/LLMEval 指标与 LLM 裁判两两对比
- 支持多语言实验与 LoRA 训练
- 附 Llama-2/Mistral/Solar 等模型在多个数据集上的基线结果

## 适用场景

- 统一基准评测自建 RAG 流水线各组件的影响
- 复现论文中的 RAG 基线结果做对比
- 多语言检索问答实验评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: BERGEN (BEnchmarking Retrieval-augmented GENeration) is a library designed to benchmark RAG systems with a focus on 
> L14: - Comprehensive evaluation metrics (*Match, EM, LLMEval*, ... )

## 星数曲线

```mermaid
xychart-beta
    title "naver/bergen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 281 --> 283
    line [282, 282]
```

2026-10-18 282 → 2026-10-25 282（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `534c46beca11` · [字段定义](../../DATASET.md)*
