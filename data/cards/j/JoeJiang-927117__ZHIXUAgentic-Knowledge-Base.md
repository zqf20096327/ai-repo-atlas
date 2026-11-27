# JoeJiang-927117/ZHIXUAgentic-Knowledge-Base

⭐ — · [GitHub]() · 个人维护 · 中文 README

**把杂乱文档文件夹编译成可审计本地 Markdown Wiki 的桌面知识库**

面向工程、运维、合规等团队的桌面知识库应用：导入 PDF/DOCX/XLSX/PPTX/Markdown 后，经两阶段编译生成结构化 Markdown Wiki，引用摘录回溯到原文行/页定位，未通过验证的引用被丢弃。检索采用 BM25+SQLite 向量+TF-IDF+精确 token 加权的四路 RRF 融合；AI 生成内容进入 Draft→Review→Published 审批流，删除操作进入回收站，版本历史存于 Git。单进程 SQLite+Git 部署，无需 Docker/Elasticsearch，支持 EN/中文 UI 与 RBAC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 不可变源文件库（SHA-256 追踪），AI 不改动原始文件
- 引用摘录经原文行/页定位验证，不可验证内容被丢弃
- Draft→Review→Published 审批流 + AI 删除拦截回收站 + Git 回滚
- LLLMA/LLM/VM 三层模型路由，支持云 API 与局域网/本地推理

## 适用场景

- 把服务器清单、SOP 文档、事故复盘编译成可检索知识库
- 制度与合规文档发布前强制人工审核
- 内网私有化部署，知识以本地 Markdown/SQLite/Git 存储

## 场景标签

`知识库管理` `RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L46: 2. **Two-Stage Knowledge Compilation & Excerpt Verification**: Structure-aware chunking, zero-bloat OOXML parsing, 
> L110: ### 2. RRF Hybrid Retrieval & Excerpt Verification
> L155: ZHIXU defaults to **Cloud API First** while supporting **LAN GPU** (`vLLM` / `SGLang` / `Ollama`) and **Local Olla


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6e490df1426e` · [字段定义](../../DATASET.md)*
