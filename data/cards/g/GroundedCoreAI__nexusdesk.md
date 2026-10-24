# GroundedCoreAI/nexusdesk

⭐ 97 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/GroundedCoreAI/nexusdesk) · [官网](https://www.aidet.top) · 组织维护 · 中文 README

**自托管通用 Agent 平台，首个参考应用为 AI 客服**

开源可自托管的可扩展 Agent 平台，分核心平台、扩展契约、业务能力、应用四层；以 ReAct 异步执行循环（LangGraph）运行推理与工具调用，Harness 层负责权限、执行边界、记忆、人工接管与审计。首个完整参考应用是 AI 客服（知识问答、工单起草、人工确认）。默认部署仅需 PostgreSQL，Docker Compose 启动，支持微信/飞书/Slack 等渠道与任意 OpenAI 兼容模型；项目自述尚未开箱生产就绪，Milvus 向量检索未端到端验证，MCP 适配器在计划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LangGraph ReAct 异步执行循环与工具调用
- Harness 治理层：权限、人工确认、记忆、审计
- 模型网关支持任意 OpenAI 兼容服务（Chat/Embedding/Rerank/OCR/语音）
- 默认部署仅需 PostgreSQL，Docker Compose 一键启动

## 适用场景

- 企业搭建自托管 AI 客服（知识问答+工单+人工接管）
- 通过渠道 API 接入企业微信、飞书、Slack 等消息平台
- 在受控权限与人工确认下让 Agent 调用业务工具

## 场景标签

`Agent 框架` `聊天机器人` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L9: **An open-source, self-hostable, and extensible general-purpose agent platform.**
> L94: |Agent configuration and execution|Configure, publish, and roll back agents; run reasoning and tool calls through a
> L26: Agents retrieve knowledge, call business tools, and decide what to do next based on execution results. The Harness 

## 星数曲线

```mermaid
xychart-beta
    title "GroundedCoreAI/nexusdesk 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 95 --> 98
    line [96, 97, 97]
```

2026-10-22 96 → 2026-10-24 97（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8f05cf81865b` · [字段定义](../../DATASET.md)*
