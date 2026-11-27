# JoeJiang-927117/zhixu

⭐ 8 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/JoeJiang-927117/zhixu) · [官网](https://joejiang-927117.github.io/zhixu/) · 个人维护 · 中文 README

**把杂乱文档编译成可审计本地 Markdown Wiki 的企业知识库**

桌面端/单 Node 进程知识库应用：导入 PDF、DOCX、XLSX、PPTX、Markdown 与图片后，经两阶段编译生成结构化 Markdown Wiki，配合 Git 历史与知识图谱，并提供带引用行/页定位校验的问答。检索采用 BM25+向量+TF-IDF+精确词四信号 RRF 融合，索引与向量存于本地 SQLite。内置审核工作流（Draft→Review→Published）、AI 删除拦截与回滚、服务端 RBAC，附带 MCP stdio 服务器供外部客户端检索。运行无需 Docker/Elasticsearch。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段知识编译+摘录回源校验，丢弃无法定位的引用
- LLLM/LLM/VM 三层模型路由，支持 Ollama 本地模型
- 内置 MCP stdio 服务器，暴露 zhixu_search/zhixu_ask 等工具
- 数据以纯 Markdown+SQLite+Git 形式本地存储

## 适用场景

- 把工程与运维的 SOP、台账、复盘文档汇编成可检索 Wiki
- 制度合规场景下对 AI 产出做人工审核后再发布
- 内网部署下用 Ollama 本地模型做私有知识问答
- 通过 MCP 让 Claude Code/Cursor 检索本地知识库

## 场景标签

`知识库管理` `知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5:  Drop a messy folder of PDFs, Word, Excel, PPT &amp; Markdown. Get an auditable local Markdown Wiki + Git history + 
> L51: 2. **Two-Stage Knowledge Compilation & Excerpt Verification**: Structure-aware chunking, zero-bloat OOXML parsing, 
> L53: 4. **Open Data Sovereignty & Bilingual Experience**: Knowledge lives as plain Markdown, indexes and persistent vect


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `10031f3d1caa` · [字段定义](../../DATASET.md)*
