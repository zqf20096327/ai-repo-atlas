# wzxsdf/DeepRAG

⭐ 17 · Python · 推送 2026-11-27 · [GitHub](https://github.com/wzxsdf/DeepRAG) · 个人维护 · 中文 README

**基于 LangGraph 的 CRAG 纠正式检索增强生成问答系统**

以 CRAG 状态机为核心的企业知识库问答工程实现：检索→证据评估→生成→校验，证据不足自动改写查询重检索，答案缺陷带反馈重生成。检索侧用 BGE-M3 dense 与 Qdrant 原生 BM25 加权 RRF 融合，再经 BGE-Reranker-v2-M3 Cross-Encoder 精排。自带 golden 消融基线、独立异模型 judge 评分、不可答负样本诚实降级率与断点续跑评测器，支持 JWT 强制鉴权的多租户与 SSE 流式输出。面向需要可量化、可回归检索链路的开发者与企业知识库场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRAG 自纠状态机：纠错式查询改写、反馈重生成、rerank 阈值拒答校准
- 混合检索（BGE-M3 dense + BM25 sparse 加权 RRF）+ Cross-Encoder 精排
- 评测基线：golden 消融、独立异模型 judge、不可答负样本诚实降级率、分块断点续跑
- 多租户 JWT 强制鉴权，tenant 从 token 全链路贯通

## 适用场景

- 搭建企业知识库问答系统
- 学习或二次开发 CRAG/Agentic RAG 架构
- 对检索/生成链路改动做可量化消融回归评测

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L19: DeepRAG 是一个**检索增强生成（RAG / Retrieval-Augmented Generation）**问答系统的完整工程实现，核心是 **CRAG（Corrective RAG，纠正式检索增强生成）**状态机：检索
> L27: DeepRAG is a production-style **Agentic RAG** system implementing **CRAG (Corrective Retrieval-Augmented Generation
> L23: > 适合场景：企业知识库问答、RAG 架构学习/二次开发、需要**可量化、可回归**的检索增强系统工程实践。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `2114de3457e7` · [字段定义](../../DATASET.md)*
