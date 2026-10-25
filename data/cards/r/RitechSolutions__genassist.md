# RitechSolutions/genassist

⭐ 64 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/RitechSolutions/genassist) · [官网](https://genassist.ai/) · 组织维护

**构建、管理和部署 AI agent 的自托管平台，含对话与分析**

GenAssist 是一个用于构建、管理和部署 AI agent 的开源平台，内置用户与角色管理、API key 管理、基于 RAG 的知识库、对话与情感分析、性能指标和审计日志。架构为 React/TypeScript 前端加 Python FastAPI 后端，配套 PostgreSQL、Redis、Celery、Chroma/Qdrant 向量库与 Whisper 转写等服务。推荐以 Docker Compose 本地运行（约 15 个服务，需给 Docker 至少 8 GB 内存），官方警告该配置仅限本地开发与演示，默认密码公开且服务暴露于局域网。支持多种 LLM provider（如 OpenAI key 为可选配置），另提供 React 插件、可嵌入网站的 JS 挂件与 iOS 插件。

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

- AI agent 配置管理，支持多种 LLM provider 与工具
- 知识库文档管理，基于 RAG，使用 Chroma/Qdrant 向量库
- 对话转写、情感分析、性能指标与审计日志
- 提供 React 插件、可嵌入任意网站的 JS 挂件与 iOS 插件

## 适用场景

- 自托管一套带用户权限管理的 AI agent 对话平台
- 为客服或内部助手搭建带 RAG 知识库的问答系统
- 通过嵌入式挂件把 agent 对话接入自己的网站

## 场景标签

`Agent 框架` `聊天机器人` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L5: GenAssist is an AI-powered platform for building, managing and deploying AI agents, with conversation management, an
> L16: - **AI agents:** configure and manage agents with various LLM providers and tools

## 星数曲线

```mermaid
xychart-beta
    title "RitechSolutions/genassist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-25 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `07a80f724a46` · [字段定义](../../DATASET.md)*
