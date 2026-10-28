# ScienciaLAB/document-qa

⭐ 37 · Python · Apache-2.0 · 推送 2026-06-07 · [GitHub](https://github.com/ScienciaLAB/document-qa) · [官网](https://lfoppiano-document-qa.hf.space/) · 组织维护

**面向科学文献的 RAG 问答应用：上传 PDF 后对全文提问**

基于 Streamlit 的科学文档问答演示应用，实现 RAG 流程：上传 PDF 后经 Grobid 抽取结构化全文，切分为可调大小的块（默认 250 token），调用 LLM 端点回答问题，公共演示的端点部署在 Modal.com（Phi-4-mini-instruct、Qwen3）。支持选择不同 embedding 与 LLM（OpenAI 与开源模型不可混用）、查询模式切换，并可对回答运行 NER 识别材料提及与物理量（依赖 grobid-quantities、grobid-superconductors 外部服务）。以 Python 库 document-qa-engine 与 Docker 镜像分发，README 标注 Work in progress。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Grobid 结构化全文抽取后做 RAG 问答
- 块大小与上下文块数可调，支持 LLM/Embeddings/问题系数三种查询模式
- 回答上的 NER：识别材料提及与物理量（grobid-quantities/superconductors）
- 提供 PyPI 库与 Docker 镜像，演示部署于 Hugging Face Space/Modal.com

## 适用场景

- 上传科学论文 PDF 并对内容提问
- 材料科学场景下从回答中提取材料与测量信息
- 复用 document-qa-engine 库搭建自己的科学文档问答服务

## 场景标签

`文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L22: Question/Answering on scientific documents using LLMs. The tool can be customized to use different types of LLM API
> L23: The streamlit application demonstrates the implementation of a RAG (Retrieval Augmented Generation) on scientific d

## 星数曲线

```mermaid
xychart-beta
    title "ScienciaLAB/document-qa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a05ecd278806` · [字段定义](../../DATASET.md)*
