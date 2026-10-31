# Angular2Guy/AIDocumentLibraryChat

⭐ 31 · Java · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/Angular2Guy/AIDocumentLibraryChat) · 个人维护

**演示用 Spring AI 与 Ollama 实现文档库对话及多模态检索的应用**

基于 Spring Boot + Spring AI + Angular 的示例项目：上传文档后分块生成嵌入存入 PostgreSQL 向量库，聊天时按最近向量取回文档并让 AI 基于其内容生成回答、附来源链接。另含图像库自然语言检索（LLava 描述生成）、LLM 生成 SQL 查询关系库、函数调用查 OpenLibrary、MCP Client/Server、生成测试类与书籍摘要、Clef-Flash 文本分类等功能。支持 OpenAI 与本地 Ollama 两种模型通道，提供 Helm/Minikube 部署配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档上传→嵌入→向量检索→带来源链接的 RAG 问答全流程
- 图像库自然语言检索：LLava 生成描述并嵌入 PGVector
- LLM 依据元数据嵌入生成 SQL 查询关系数据库
- MCP Client/Server 工具调用（书籍/电影信息）

## 适用场景

- 学习 Spring AI 实现 RAG、函数调用与 MCP 的工程方式
- 搭建可与自有文档对话并溯源的原型系统
- 用本地 Ollama 模型离线实现文档/图像检索

## 场景标签

`RAG` `文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L10: This is a project to show howto use SpringAI 2.0.0+ to chat with the documents in a library. Document can be upload
> L61: ## Mission Statement

## 星数曲线

```mermaid
xychart-beta
    title "Angular2Guy/AIDocumentLibraryChat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8af87dc1b6c9` · [字段定义](../../DATASET.md)*
