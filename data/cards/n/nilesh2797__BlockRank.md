# nilesh2797/BlockRank

⭐ 45 · Python · MIT · 推送 2025-12-12 · [GitHub](https://github.com/nilesh2797/BlockRank) · [官网](https://nilesh2797.github.io/publications/blockrank/) · 个人维护

**让 LLM 高效做上下文文档排序的稀疏注意力方法与模型**

对现有生成式 LLM（Mistral-7B 等）做三处改造以用于列表式文档排序：块结构稀疏注意力将复杂度从 O(n²) 降至 O(n)；中层 InfoNCE 对比辅助损失强化查询-文档相关信号；推理时直接从注意力图提取相关性分数，跳过自回归解码，在 BEIR 基准上报告 2-4× 推理加速。以 Python 库形式提供，含训练、评测脚本与基于 Mistral-7B 的预训练模型（HuggingFace 下载），要求 Python 3.9+。

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

- 块稀疏注意力实现 O(n) 复杂度的列表式排序
- 注意力图直接提取相关性分数，跳过自回归解码
- 现有 LLM（Qwen/Mistral/Llama）可改造为 BlockRank 模型
- 提供基于 Mistral-7B-Instruct-v0.3 的预训练模型与 BEIR 评测结果

## 适用场景

- 在 RAG 检索阶段用 LLM 做高效文档重排
- 研究稀疏注意力与注意力推理在排序任务的效果
- 在 BEIR 基准上训练和评测列表式排序模型

## 场景标签

`RAG` `语义搜索` `模型训练` · 领域:知识与检索

## 证据(README 行号)

> L11: **BlockRank** makes LLMs efficient for document ranking by using structured sparse attention and attention-based in
> L79: **1. Structured Sparse Attention**
> L88: **3. Attention-Based Inference**

## 星数曲线

```mermaid
xychart-beta
    title "nilesh2797/BlockRank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8e1a9cc0dc17` · [字段定义](../../DATASET.md)*
