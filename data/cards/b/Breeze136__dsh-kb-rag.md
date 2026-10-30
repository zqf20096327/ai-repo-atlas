# Breeze136/dsh-kb-rag

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Breeze136/dsh-kb-rag) · [官网](https://www.npmjs.com/package/dsh-kb-rag) · 个人维护 · 中文 README

**DSH 插件：本地文献知识库 RAG，答案定位到段落/页码/DOI**

面向 DeepSeek Harness（DSH）桌面端及其他 MCP 客户端的本地文献 RAG 插件：把 PDF、TXT/MD/DOCX 与 Zotero 库分块、嵌入并索引到一个 SQLite 文件，检索时以关键词+向量混合召回，deep 模式追加本地重排（bge-reranker），返回带章节、物理页码、DOI 与引文链的段落证据。索引、嵌入、重排全部本机运行，无 API 费用。支持按 DOI/arXiv ID 拉取文献、增量索引（SHA-256 跳过未变文件）、引文跨库解析与 10 种模板的自包含 HTML 答案页。限制：不做 OCR，扫描版 PDF 需先转换；需 DSH 桌面端 0.2+，首次搜索需下载约 1.2 GB 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 SQLite 索引 + 混合检索 + 本地重排，段落级出处（章节/页码/DOI/引文链）
- Zotero 库同步（dry_run 预览）与 DOI/arXiv 一键拉取入库
- 增量索引：按 SHA-256 跳过未变与重复文件
- 10 种模板的自包含 HTML 答案页，渲染无模型调用

## 适用场景

- 把模糊的文献记忆定位到具体段落和图表，DOI 直达原文
- 跨论文比较方法、梳理综述、追踪引文链
- 在 DSH 对话中只基于本地文献库回答（strict mode）

## 场景标签

`RAG` `科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L15: kb-rag is a local literature knowledge base for DSH (DeepSeek Harness) and other MCP clients. It indexes PDFs and Z
> L75: kb-rag runs in the DSH desktop app. Install it from the plugin panel. The command-line routes exist for maintainers

## 星数曲线

```mermaid
xychart-beta
    title "Breeze136/dsh-kb-rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `29b1d0fe1fa9` · [字段定义](../../DATASET.md)*
