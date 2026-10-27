# deep-div/multimodel-rag

⭐ 32 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/deep-div/multimodel-rag) · 个人维护

**多模态 RAG 项目：从 PDF 检索并生成图文回答**

基于 LangChain 与 LlamaIndex 双框架实现的多模态检索增强生成项目：摄取 PDF 文档，提取文本与图像内容，通过检索生成包含文本和图片的回答。LangChain 用于文档处理与 PDF 摄取，LlamaIndex 使用 CLIP 嵌入连接文本与视觉内容。提供 main.ipynb 端到端流程 notebook 及 tutorials/ 下两套独立实现（含 Mistral 生成模型示例），支持多种嵌入、检索与生成策略。README 未给出安装命令与依赖清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄取 PDF 并处理文本与视觉内容
- 生成包含源文档相关文本与图片的回答
- LangChain 与 LlamaIndex 双实现，CLIP 嵌入连接图文
- 支持多种嵌入、检索与生成策略

## 适用场景

- 对图文混排 PDF 做基于内容的问答
- 学习或比较多模态 RAG 的两种框架实现
- 作为多模态检索管线的起点进行扩展

## 场景标签

`RAG` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L3: This project implements a **Multimodal Retrieval-Augmented Generation (RAG)** system that ingests PDF documents and 
> L16: * Supports **multimodal querying** using Retrieval-Augmented Generation.

## 星数曲线

```mermaid
xychart-beta
    title "deep-div/multimodel-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f4a403db3459` · [字段定义](../../DATASET.md)*
