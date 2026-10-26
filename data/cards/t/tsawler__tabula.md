# tsawler/tabula

⭐ 29 · Go · MIT · 推送 2026-06-29 · [GitHub](https://github.com/tsawler/tabula) · 个人维护

**Go 文本提取库：多格式文档抽取文本与 RAG 分块**

纯 Go 编写的文档文本提取库，提供链式 API，支持 PDF（1.0-1.7，含加密与损坏文件恢复）、DOCX、ODT、XLSX、PPTX、HTML、EPUB 七种格式。功能包括布局分析（标题/段落/列表/表格检测）、页眉页脚识别与排除、HTML 导航过滤、Markdown 导出，以及面向 RAG 的语义分块（大小受限、自动恢复章节标题）。可选启用 Tesseract OCR 处理扫描件（需 -tags ocr 构建及额外系统库），扫描内容可透明进入分块结果。面向在 Go 项目中做文档摄取的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 PDF/DOCX/ODT/XLSX/PPTX/HTML/EPUB 七种格式的文本与 Markdown 提取
- 面向 RAG 的语义分块：大小受限、无碎片化、自动恢复章节标题
- 可选 Tesseract OCR 处理扫描 PDF（JBIG2/JPEG2000 解码、整页栅格化）
- PDF 布局分析与加密（RC4/AES）、损坏交叉引用表恢复

## 适用场景

- 为 RAG 管道将 PDF/Office/EPUB 文档转换为分块或 Markdown 输入向量库
- 提取扫描版 PDF 的文本（启用 OCR 构建标签）
- 清洗网页内容，过滤导航、页眉、侧栏后做结构化提取

## 场景标签

 · 领域:文档处理/RAG 基础设施

## 证据(README 行号)

> L9: A Go text extraction library with a fluent API, designed for RAG (Retrieval-Augmented Generation) workflows. Support
> L18: - **RAG-Ready Chunking** - Semantic chunking with metadata: size-bounded chunks (no tiny fragments or over-max chun
> L167: |`Chunks()`|`*rag.ChunkCollection`|Semantic chunks for RAG|PDF, DOCX, ODT, XLSX, PPTX, HTML, EPUB|

## 星数曲线

```mermaid
xychart-beta
    title "tsawler/tabula 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `36b7596827ca` · [字段定义](../../DATASET.md)*
