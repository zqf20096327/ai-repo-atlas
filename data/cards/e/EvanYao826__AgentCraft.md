# EvanYao826/AgentCraft

⭐ 35 · Python · Apache-2.0 · 推送 2026-05-20 · [GitHub](https://github.com/EvanYao826/AgentCraft) · 个人维护 · 中文 README

**多 Agent 协作 RAG 知识库全栈系统，兼作 Agent 架构学习项目**

Spring Boot + FastAPI + React 全栈 RAG 知识库问答平台：用户上传 PDF/Word/TXT 构建私有知识库，系统自动解析、向量化存储，提问经意图识别→问题改写→检索→Rerank→充分性判断→答案生成流程产出带引用来源的回答。AI 服务拆为 Interface/Orchestrator/Tool/Memory/Evaluation 五层，内置 Router/Retrieval/Ops/Inspection 多 Agent，Tool Registry 统一管理 8 类工具，runId/traceId 全链路追踪，Caffeine+Redis 多级缓存。README 明确定位为学习与简历展示项目，已知问题包括 Rerank 默认关闭、前端无 TypeScript、短信验证码为模拟模式。提供 Docker Compose 一键部署与手动启动两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五层可编排 Agent 架构（Interface/Orchestrator/Tool/Memory/Evaluation）
- Router/Retrieval/Ops/Inspection 多 Agent 协作与统一 Tool Registry（8 个已注册工具）
- RAG 全链路：解析→向量化→语义检索→Rerank→带引用答案，Milvus/FAISS 可切换
- runId/traceId 全链路追踪与 Caffeine+Redis 多级缓存

## 适用场景

- 把内部文档做成企业知识库供员工自然语言检索
- 基于产品文档和历史工单构建智能客服问答
- 作为 Agent 后端开发的学习与简历展示项目

## 场景标签

`多智能体` `RAG` `文档问答` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L18: AgentCraft 是一个"**前端 + Java 后端 + Python AI 微服务**"的**全栈 RAG 知识库系统**。用户可上传 PDF、Word、TXT 等文档构建私有知识库，系统自动完成解析、向量化存储，提问时通
> L20: 核心亮点是 **五层可编排 Agent 架构**——Interface、Orchestrator、Tool、Memory、Evaluation 五层解耦，支持意图识别→问题改写→检索→充分性判断→答案生成的完整工作流。系统内置 R

## 星数曲线

```mermaid
xychart-beta
    title "EvanYao826/AgentCraft 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-25 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `19683fe030a9` · [字段定义](../../DATASET.md)*
