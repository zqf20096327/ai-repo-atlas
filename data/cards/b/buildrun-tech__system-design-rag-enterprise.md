# buildrun-tech/system-design-rag-enterprise

⭐ 16 · Java · 推送 2026-10-27 · [GitHub](https://github.com/buildrun-tech/system-design-rag-enterprise) · [官网](https://tinyurl.com/434by77r) · 组织维护

**企业级 NotebookLM 简化克隆：笔记本式 RAG 对话平台（Java/AWS）**

基于 Java 21 + Spring Boot 3.x + Spring AI 构建的简化版 NotebookLM：用户创建笔记本、添加来源（PDF/DOCX/Markdown/URL），通过 RAG 聊天与文档对话，回答以 SSE 逐 token 流式传输。文档上传后经 SQS 异步处理（Apache Tika 文本提取、分块、embedding、pgvector 索引），聊天用相似度检索组装上下文。部署于 AWS（Cognito 认证、S3、RDS、ECS 等），LLM 走 OpenAI 兼容接口（Bedrock 或 OpenRouter）。本地运行需 docker 与 aws cli，项目为直播构建的系统设计教学案例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 笔记本/来源组织 + RAG 聊天，SSE 流式回答
- SQS 异步管道：Tika 提取、分块、embedding、pgvector 索引
- AWS 生产级架构：Cognito OAuth2、S3、RDS、ECS、API Gateway
- 本地脚本一键起 Postgres+pgvector 与 Cognito 模拟器

## 适用场景

- 我需要一个可私有部署的 NotebookLM 式文档问答平台
- 学习 AWS 上的企业 RAG 系统设计（配套直播与架构文档）
- 团队把 PDF/DOCX/网页资料汇总成可对话的笔记本

## 场景标签

`文档问答` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L9: Um clone simplificado do NotebookLM: usuários criam **notebooks**, adicionam **sources** (PDF, DOCX, Markdown ou URL
> L20: |LLM|Provider OpenAI-compatible: AWS Bedrock ou OpenRouter|
> L35: Upload de source dispara um fluxo **async request-reply** via SQS: extração de texto (Apache Tika), chunking, geraç

## 星数曲线

```mermaid
xychart-beta
    title "buildrun-tech/system-design-rag-enterprise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `502509345489` · [字段定义](../../DATASET.md)*
