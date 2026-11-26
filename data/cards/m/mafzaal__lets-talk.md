# mafzaal/lets-talk

⭐ 10 · Python · MIT · 推送 2026-11-01 · [GitHub](https://github.com/mafzaal/lets-talk) · [官网](https://thedataguy.pro/lets-talk/) · 个人维护

**为技术博客嵌入 RAG 问答聊天组件的开源项目**

面向技术博客作者的开源聊天组件：读者可在阅读时向博客内容提问、索取代码示例。实现上从文件系统与网站摄取文档，经递归切分与语义分块后索引进 Qdrant 向量库，检索层支持 BM25、多查询与语义检索，编排用 LangChain/LangGraph，接口为可嵌入博客的 Svelte 组件。另提供基于 FastAPI 的流水线调度系统，支持 cron 表达式定时更新内容与 REST API 管理监控。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从文件系统与网站摄取文档并用 Qdrant 建立向量索引
- 检索层含 BM25、多查询检索与语义搜索，嵌入模型可自定义
- FastAPI 调度系统：cron/间隔/一次性任务与 REST API 管理
- 提供 RAG 与 ReAct 两类 agent 工厂实现

## 适用场景

- 给技术博客或文档站添加内容问答聊天组件
- 定时自动更新博客内容的检索索引
- 读者边阅读边追问并获取代码示例

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L10: Have you ever wished you could ask follow-up questions while reading technical content? Meet **Let’s Talk** – an AI
> L32: - **Document Ingestion:** Supports ingesting documents from both the file system and websites
> L38: - **Orchestration:** LangChain and LangGraph for the complete RAG workflow


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e392e87c3be5` · [字段定义](../../DATASET.md)*
