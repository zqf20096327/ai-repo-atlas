# Sugers955/agent-mill

⭐ 43 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/Sugers955/agent-mill) · [官网](https://sugers955.github.io/agent-mill/features.html) · 个人维护 · 中文 README

**企业 AI Agent 平台：低代码搭建数字员工并交付团队使用**

基于 Python/FastAPI + Vue 3 的前后端分离 AI agent 平台，管理员以搭积木方式配置具备工具调用、RAG 检索、文件处理与多 agent 协作的智能体，终端用户经 Web/移动端对话完成文档处理、数据分析、知识问答等任务。模型层集成 Claude Agent SDK，并为 DeepSeek、Qwen、OpenAI 等实现 OpenAI 兼容 tool_calls 循环；技能支持 ZIP/callable/YAML DAG 三种形式，MCP 连接器支持 stdio/sse/http 三协议。需自备 MySQL 8.0+，提供 docker compose 与 make dev 两种启动方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集成 Claude Agent SDK，双路 SSE 流式（Anthropic 原生 + OpenAI 兼容 tool_calls 循环）
- 三种技能形式（ZIP/callable/YAML DAG）与三种 MCP 协议（stdio/sse/http）
- 多 agent 编排：串行/并行/MapReduce
- RAG 知识库：ZVec 向量引擎、30+ 格式解析、会话轮自动检索注入
- RBAC 三角色 + SSO/LDAP + 审计日志与 7 层安全防护

## 适用场景

- 为团队搭建可交付使用的智能数字员工
- 统一管理多家 LLM 供应商并配置可复用 agent 模板
- 基于内部知识库构建带权限控制的问答/文档处理系统

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L14: Agent Mill is an **out-of-the-box enterprise AI agent platform**. It allows administrators to configure various AI 
> L16: **In one sentence**: Build an intelligent assistant with tool calling, knowledge retrieval, file processing, and mu
> L39: |AI models scattered, no unified management|Unified model gateway, manage all LLM providers in one platform|

## 星数曲线

```mermaid
xychart-beta
    title "Sugers955/agent-mill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `156a7f2d017b` · [字段定义](../../DATASET.md)*
