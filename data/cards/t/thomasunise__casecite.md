# thomasunise/casecite

⭐ 138 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/thomasunise/casecite) · [官网](https://thomasunise.com/casecite) · 个人维护

**自托管法律 RAG 研究与文档分析平台，面向律所**

开源、自托管的法律研究平台：上传律所文档后提供九个工具，包括混合检索（向量+全文关键词、秩融合）的文档问答与内联引用、深度研究、合同审查与批量表格审阅、工作流编排、基于多文档的起草、CourtListener 案例视图与法官分析。文档与索引存储在用户自有服务器；AI 功能按 BYOK 将问题与相关文本发送至用户配置的提供商（OpenAI/Anthropic/Gemini），也可将 OPENAI_BASE_URL 与 EMBEDDING_BASE_URL 指向自托管 OpenAI 兼容服务器以留存全部文本。通过 Docker Compose 部署，内置 Postgres、Redis 与 HTTPS 代理；每个 AI 输出附带需人工核验的提示，明确不替代律师判断与引证核查服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 九个工具共享同一文档库：研究、合同审查、批量表格审阅、工作流、起草、法官分析等
- 回答内联引用来源并逐条与所引段落核对；深度研究引用均对原文核验
- BYOK 密钥体系：每用户密钥 AES-256-GCM 加密存储，支持自托管 OpenAI 兼容端点
- Docker Compose 一键部署，捆绑 Postgres/Redis/HTTPS 代理；提供 Word 加载项

## 适用场景

- 律所在自有基础设施上做文档问答与判例研究
- 批量合同审阅并导出 Excel/CSV/JSON 结果
- 把合同审查与起草流程固化为可审批、可恢复的后台工作流
- 通过 Word 加载项在文档内分析、改写与插入带脚注的研究答案

## 场景标签

`文档问答` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: CaseCite is an **open-source, self-hosted** legal research platform. Upload your firm's documents, ask questions, an
> L15: |**Research** (`/research`)|Chat over your firm's documents — hybrid retrieval (vector search and a full-corpus key


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e67c942a295e` · [字段定义](../../DATASET.md)*
