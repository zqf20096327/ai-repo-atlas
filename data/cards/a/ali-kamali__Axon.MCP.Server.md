# ali-kamali/Axon.MCP.Server

⭐ 166 · Python · NOASSERTION · 推送 2026-06-30 · [GitHub](https://github.com/ali-kamali/Axon.MCP.Server) · [官网](https://ali-kamali.github.io/Axon.MCP.Server/) · 个人维护

**把代码库变成 MCP 知识库，为 AI IDE 提供代码智能上下文**

面向 Cursor、Google AntiGravity、Claude 等 MCP 客户端的代码智能服务器：从 GitLab/Azure DevOps 自动发现仓库，用 Tree-sitter 做多语言语法解析、Roslyn 做编译级 C# 语义分析，构建调用图、继承树、服务与 EF 实体映射等关系模型，并生成 pgvector 向量嵌入支持语义搜索；通过 12 个 MCP 工具向 AI 助手暴露这些能力。后端为 FastAPI + Celery + PostgreSQL 15/pgvector + Redis，Docker Compose 一键部署，含 React 仪表盘与 Prometheus/Grafana 监控、JWT/RBAC 鉴权。限制：需 Docker 与源码平台访问令牌，LLM 摘要功能依赖 OpenAI/OpenRouter。

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

- 12 个 MCP 工具：语义搜索、调用图、继承树、API 端点、架构图等
- Tree-sitter 多语言解析 + Roslyn 编译级 C# 语义分析
- pgvector 向量嵌入支持按语义查找代码
- 自动发现 GitLab/Azure DevOps 仓库并构建关系型代码模型（14 张表）

## 适用场景

- 在 Cursor/AntiGravity 等 AI IDE 中获得整个代码库的深度上下文
- 新成员通过问答了解认证流程、架构与依赖关系
- 重构前做影响分析与依赖追踪
- 自动生成服务依赖图与模块文档

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: **Model Context Protocol (MCP) Server for AI IDEs - Cursor, AntiGravity & Claude**
> L86: The server exposes **12 powerful tools** to AI assistants via the Model Context Protocol:
> L212: **The main purpose of Axon MCP Server is to provide deep code intelligence to AI-powered IDEs:**

## 星数曲线

```mermaid
xychart-beta
    title "ali-kamali/Axon.MCP.Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 165 --> 167
    line [166, 166]
```

2026-10-18 166 → 2026-10-26 166（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f203f26bac26` · [字段定义](../../DATASET.md)*
