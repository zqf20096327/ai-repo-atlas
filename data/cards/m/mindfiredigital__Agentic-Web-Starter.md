# mindfiredigital/Agentic-Web-Starter

⭐ 16 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/mindfiredigital/Agentic-Web-Starter) · 组织维护

**构建 Agentic RAG 服务的 FastAPI 后端模板**

基于 FastAPI 的生产级 RAG 服务脚手架：提供文档摄入（上传并索引到 Qdrant）、检索增强聊天端点、可选 JWT 认证与用户/角色管理（SQLite 持久化）、Redis 或内存式会话聊天历史，以及可选 RabbitMQ 异步文档处理。LLM 后端需配置 OpenAI 或 Gemini API key。设计为克隆后扩展，功能可通过环境变量开关禁用。附带 Docusaurus 文档站、Pytest 测试套件与 GitHub Actions CI，推荐以 Docker Compose 运行，也可本地 uvicorn 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档上传并索引到 Qdrant 的摄入管线
- RAG 聊天端点：检索相关上下文后再查询 LLM
- 可选 JWT 认证与用户/角色管理子系统
- Redis/RabbitMQ 均为可选，环境变量开关控制功能启用

## 适用场景

- 快速搭建带认证的检索增强问答服务
- 在其基础上扩展自定义 agent、提示词与数据源
- 以容器化方式部署带文档摄入管线的 RAG 后端

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L12: **Agentic Web Starter** is a production-ready, batteries-included template for building agentic
> L16: - a **chat endpoint** that retrieves relevant context before querying an LLM,

## 星数曲线

```mermaid
xychart-beta
    title "mindfiredigital/Agentic-Web-Starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fab0933926b8` · [字段定义](../../DATASET.md)*
