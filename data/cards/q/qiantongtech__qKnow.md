# qiantongtech/qKnow

⭐ 299 · Java · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/qiantongtech/qKnow) · [官网](https://community.qknow.ai/) · 组织维护 · 中文 README

**面向企业的开源知识增强 Agent 平台，构建 RAG 与知识图谱应用**

qKnow 是一个围绕知识增强的开源 AI Agent 平台：将手册、政策与业务数据组织为知识库与知识图谱，在可视化画布上编排模型、知识与工具节点构建 Workflow/Chatflow/Agent（Bot），支持全文/向量/混合检索、Top-K 与相似度阈值调参、引用溯源与检索测试。技术上前后端分离，后端 JDK 17 + Spring Boot 3 + Spring AI，存储用 MySQL/Redis/Neo4j/Weaviate，支持 Docker Compose 部署或源码运行，采用附带附加条款的 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库 RAG 与实体/关系抽取构建知识图谱，答案可引用溯源
- 可视化画布编排 Workflow/Chatflow/Agent，可接入 MCP 服务与业务 API
- Bot 与应用实例分离，一个 Bot 可复用绑定到多个业务应用
- 支持 Docker Compose 部署与源码运行两种方式

## 适用场景

- 把产品手册与政策文件建成知识库做企业知识问答
- 抽取文档与数据库中的实体关系构建行业知识图谱
- 编排支持工单查询等工具调用的业务 Bot
- 多个团队复用同一问答逻辑并绑定各自知识资源

## 场景标签

`知识图谱` `RAG` `文档问答` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: **qKnow is an open-source AI agent platform built around knowledge augmentation.** It combines knowledge bases, kno
> L42: Create a Workflow, Chatflow, or Agent in the AI Workspace, then drag and connect model, knowledge, tool, and logic 
> L118: |Backend|JDK 17, Spring Boot 3, Spring Security, MyBatis-Plus, Spring AI|

## 星数曲线

```mermaid
xychart-beta
    title "qiantongtech/qKnow 星数(近 13 点)"
    x-axis ["2026-10-25", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-26", "2026-11-27"]
    y-axis "stars" 286 --> 302
    line [287, 288, 287, 292, 295, 296, 297, 298, 299, 301, 300, 299, 299]
```

2026-10-25 287 → 2026-11-27 299（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `732b26a79e05` · [字段定义](../../DATASET.md)*
