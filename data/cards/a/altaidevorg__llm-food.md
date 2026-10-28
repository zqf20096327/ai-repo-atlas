# altaidevorg/llm-food

⭐ 26 · Python · 推送 2026-03-09 · [GitHub](https://github.com/altaidevorg/llm-food) · [官网](https://altai.dev/open-source/llm-food/) · 组织维护

**文档转 Markdown 微服务：为 LLM 流水线准备干净文本**

基于 FastAPI 的 Python 包，提供将 PDF、DOC/DOCX、RTF、PPTX、HTML/网页转为 Markdown 的微服务：单文件同步转换（/convert）、URL 转换与异步批处理（/batch），批处理 PDF 走 Gemini Batch API（页面转 PNG 存入 GCS），其他格式由服务器后台任务逐个处理；任务状态用本地 DuckDB 跟踪。附带异步 Python 客户端与 CLI。面向搭建 RAG 或微调数据管线的开发者；批处理依赖 GCS 存储桶与 Google Cloud 配置，同步 PDF 转换可选 pymupdf4llm/pypdf 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件/URL 同步转换与异步批量处理两类端点
- 批量 PDF 经 Gemini Batch API 处理（页面图片存 GCS，payload.jsonl 提交）
- DuckDB 跟踪批任务进度与逐文件状态
- Docker 化部署、Bearer Token 可选鉴权、async Python 客户端与 CLI

## 适用场景

- RAG/微调管线前批量把 PDF 转 Markdown
- 把网页或办公文档统一清洗为 LLM 可用文本
- 以服务方式向团队提供文档转换 API

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13: `llm-food` is a Python package that provides a FastAPI-based microservice (the **server**) for converting various i
> L21: * Asynchronous batch processing of multiple uploaded files (`/batch`), with PDFs leveraging Google's Gemini Batch A

## 星数曲线

```mermaid
xychart-beta
    title "altaidevorg/llm-food 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `58f4a66b2bb8` · [字段定义](../../DATASET.md)*
