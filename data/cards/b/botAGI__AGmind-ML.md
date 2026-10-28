# botAGI/AGmind-ML

⭐ 24 · Python · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/botAGI/AGmind-ML) · 个人维护

**自托管俄语 RAG 栈的本地微调模型集（切分/查询扩展/检索）**

为自托管 AGmind RAG 栈本地微调的三个俄语模型：上下文感知文档切分器（语义分块、表格与代码保持完整、可无损还原）、面向 qmd 的查询扩展模型（hyde/lex/vec 三路、为 BM25 补词形），以及 RU-first 稠密检索嵌入器（4 层、层剪枝蒸馏 + BGE-M3 难负例）。方法为教师蒸馏 + bf16 LoRA，量化为 GGUF 后经 llama.cpp Vulkan 在 AMD（Strix Halo）上推理，训练用单张 RTX 5090，许可证允许商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个模型已发布至 HuggingFace，覆盖切分、查询扩展与检索嵌入
- GGUF 量化 + llama.cpp Vulkan 在 AMD 上推理，无 CUDA 依赖
- 教师蒸馏路线：无人工标注，含严格验证门控、去重与重试
- 商用许可、完全本地部署

## 适用场景

- 搭建俄语 RAG 系统时获取文档切分与检索嵌入组件
- 在无 CUDA 的 AMD 硬件上本地运行微调模型
- 修复通用模型在俄语查询扩展中的英语幻觉问题

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **Locally fine-tuned Russian models for the self-hosted AGmind RAG stack.**
> L6: (RTX 5090), deployed on AMD Strix Halo. Three models shipped so far — a document
> L17: |**agmind-rag-splitter-ru** · 🤗|Context-aware document splitter for RAG: semantic chunks, tables and code kept whol

## 星数曲线

```mermaid
xychart-beta
    title "botAGI/AGmind-ML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `54ec8b8c29c5` · [字段定义](../../DATASET.md)*
