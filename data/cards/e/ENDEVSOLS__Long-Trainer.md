# ENDEVSOLS/Long-Trainer

⭐ 30 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ENDEVSOLS/Long-Trainer) · [官网](https://endevsols.com/open-source/longtrainer) · 组织维护

**构建多租户 RAG 聊天机器人的 Python 框架**

基于 LangChain 构建的 Python RAG 框架，用少量代码把文档转为多租户聊天机器人：内置多机器人隔离、MongoDB 持久化记忆（Fernet 加密）、FAISS 等多种向量库、同步/异步流式输出、自定义工具调用、LangGraph agent 模式与视觉对话。1.4.0 提供 research/coding/financial/customer_support 四类命名 agent 类型，另有 FastAPI 服务与 CLI。限制：需运行 MongoDB；Python 3.11+；agent 目的需工具调用模型；1.4.0 尚未发布到 PyPI，需源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多机器人隔离管理，每 bot 独立 LLM/嵌入/检索配置
- MongoDB 持久化记忆 + Fernet 加密 + train_chats 反哺知识库
- 支持 FAISS/Pinecone/Chroma/Qdrant/PGVector/Milvus 等 10 种向量库
- 四类命名 agent 类型（research/coding/financial/customer_support）

## 适用场景

- 快速搭建多租户文档问答机器人
- 带工具调用的 research/coding/financial agent
- 通过 REST API 或 CLI 部署文档问答服务

## 场景标签

`RAG` `文档问答` `聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L40: LongTrainer is a **production-ready RAG framework** that turns your documents into intelligent, multi-tenant chatbo
> L42: Built on top of LangChain, LongTrainer handles the hard parts that every production RAG system needs: **multi-bot i

## 星数曲线

```mermaid
xychart-beta
    title "ENDEVSOLS/Long-Trainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `20e5269c4192` · [字段定义](../../DATASET.md)*
