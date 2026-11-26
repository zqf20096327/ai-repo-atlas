# Blandskron/KronDocs

⭐ 12 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Blandskron/KronDocs) · [官网](https://blandskron.github.io/KronDocs/) · 组织维护

**基于 RAG 的智能文档管理与问答平台，供团队查阅文档并引用来源**

开源文档管理与查询应用：上传并组织 PDF/DOCX/TXT/MD/OCR 文档，使用本地 CPU 计算 E5 embeddings，PostgreSQL 16 + pgvector 存储，混合检索（向量+全文+RRF 融合）并给出带可验证来源引用的回答。前端 React/TypeScript，后端 Django 身份管理与十一个微服务，Docker Compose 一键部署。支持 Groq 云端或 Ollama 本地 LLM 切换、Google Drive 导入、PDF 导出、多租户 RBAC 与安全审计日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索：pgvector HNSW + 全文搜索 + Reciprocal Rank Fusion，回答带 [Fuente N] 来源引用
- 支持 Groq 云端与 Ollama 本地（CPU 目录 qwen2.5:3b/gemma2:2b/llama3.2:3b），界面内切换无需改代码
- 多步 AI Agent 与 Code Mode，运行于 Deno --deny-all 沙箱并含人工审批
- 多租户管理、15 项细粒度权限、不可变安全审计日志

## 适用场景

- 搭建内部知识库，向文档提问并获得带引用的回答
- 从 Google Drive 或 Obsidian/Logseq 集合批量导入文档
- 在无外网、不向第三方发送文档的本地模式下运行 LLM 问答
- 按租户与权限隔离管理企业文档的审阅与签署流程

## 场景标签

`RAG` `文档问答` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: Aplicación de código abierto para la gestión y consulta documental, desarrollada por Blandskron. Permite cargar y or
> L29: |`01:01 – 01:22`|**4. Chat documental RAG híbrido con citas**|`/`|Fusión `pgvector` HNSW + FTS con Reciprocal Rank 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9e01b0953c97` · [字段定义](../../DATASET.md)*
