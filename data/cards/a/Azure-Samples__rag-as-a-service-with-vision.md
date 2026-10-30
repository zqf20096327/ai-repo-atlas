# Azure-Samples/rag-as-a-service-with-vision

⭐ 37 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/Azure-Samples/rag-as-a-service-with-vision) · 组织维护

**Azure 上的图文 RAG 应用框架：处理 MHTML 文档检索增强生成**

基于 Python 的检索增强生成（RAG）应用框架，利用 Azure AI Services、Azure AI Search 与 Azure OpenAI Service，从 MHTML 文档中同时利用文本与图像内容回答用户查询。包含摄取流（MHTML 入库 Azure AI Search）、富集流（多模态 LLM 分类图像并生成图像描述，结果缓存）、推理时结合富集数据的视觉 RAG 管道，以及含 ROUGE recall 与 LLM-as-a-judge 的评估起步代码。定位为实验起点而非成品，附 devcontainer 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 摄取流将 MHTML 文件入库 Azure AI Search 并附带富集管道
- 多模态 LLM 为图像分类并生成描述，富集结果缓存加速
- 推理时检索图像并纳入富集管道的 RAG with Vision 管道
- 含 ROUGE recall 与 LLM-as-a-judge 的评估起步代码

## 适用场景

- 在自有 MHTML 文档集合上搭建图文问答系统
- 实验调整 RAG 管道配置并用评估代码衡量效果
- 为含图像的文档数据集构建检索增强生成方案

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: This repository provides an application framework for a Python-based retrieval-augmented generation (RAG) pipeline t
> L8: - **Ingestion flow**: Ingests MHTML files into Azure AI Search using a newly developed enrichment pipeline.
> L10: - **RAG with vision pipeline** : Utilizes enrichment data to search for images and incorporates the enrichment pipe

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/rag-as-a-service-with-vision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3094d9412c57` · [字段定义](../../DATASET.md)*
