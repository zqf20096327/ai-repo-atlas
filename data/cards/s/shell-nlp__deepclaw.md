# shell-nlp/deepclaw

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/shell-nlp/deepclaw) · 组织维护 · 中文 README

**企业级智能体工作台：单进程提供 Agent 运行时、RAG 与 IM 渠道接入**

基于 FastAPI + LangGraph 的智能体工作台与脚手架，一个进程同时提供 AG-UI 协议运行时（SSE 流式、断线重放）、通用 Agent 与 RAG 知识库问答（通过 agentId 切换）、技能管理、飞书/钉钉/微信渠道绑定、人工审批（HITL）与用户认证。会话状态经 LangGraph checkpoint 持久化到 PostgreSQL，支持多实例共享；模型走任意 OpenAI 兼容网关，支持三种执行后端与用户级容器沙箱隔离。面向需要私有化部署、统一承载多个业务智能体的团队，前端 Next.js 由同一进程托管，通过 uv 与 docker compose 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器与 IM 渠道统一走 AG-UI 协议，SSE 流式返回并支持断线重放
- 新增 Agent 只需定义 Agent 子类，注册表自动发现，无需改路由
- RAG 混合检索（BM25 + 向量 + RRF），可选 pgvector 或 Elasticsearch 后端
- 工具调用前人工审批（批准/编辑/拒绝），恢复走标准 resume[]

## 适用场景

- 统一入口承载多个业务智能体并接入飞书、钉钉、微信内部渠道
- 私有化部署企业知识库问答，状态落自己的 PostgreSQL
- 在关键工具调用前插入人工审批流程
- 为每个用户分配独立沙箱容器运行 Agent 任务

## 场景标签

`Agent 框架` `RAG` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L27: DeepClaw 把「智能体运行时」和「周边工程」收敛成一个可直接部署的服务：浏览器与 IM 渠道走同一套
> L42: |统一 AG-UI 运行时|浏览器与渠道都调用 `/api/agui/runs`，顶层 `agentId` 选择智能体，SSE 流式返回并支持 `Last-Event-ID` 断线重放|
> L45: |通用 Agent|基于 LangGraph / DeepAgents 构建，内置天气、网页抓取、检索等工具，支持 MCP 配置与技能包扩展|

## 星数曲线

```mermaid
xychart-beta
    title "shell-nlp/deepclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d6bfcf7ecf8e` · [字段定义](../../DATASET.md)*
