# LightningRAG/LightningRAG

⭐ 454 · Go · Apache-2.0 · 推送 2026-04-17 · [GitHub](https://github.com/LightningRAG/LightningRAG) · [官网](https://LightningRAG.com) · 组织维护 · 中文 README

**Vue+Gin 全栈 RAG 起始框架：知识库、检索与 Agent 编排**

前后端分离的全栈起始项目（Vue 前端 + Gin 后端），核心围绕 RAG：知识库的导入/解析/分块/向量检索，可插拔的 LLM、Embedding、向量库与重排器，以及画布式 Agent 编排节点（Begin/Retrieval/LLM/Message/Agent）。支持将发布的 Agent 通过 webhook 绑定到飞书、钉钉、Slack、Telegram 等渠道。附带 JWT、Casbin 权限、动态路由菜单、表单构建器与代码生成等后台脚手架功能。通过 GoReleaser 产出多平台二进制，可选 go:embed 将前端打包为单二进制。在线演示尚未部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库全流程：导入、解析、分块、向量写入（pgvector/Elasticsearch 等）
- 混合/多路检索（向量、关键词、PageIndex），可按请求启用重排
- 画布式 Agent 编排与可扩展工具注册表
- Agent 可经 webhook 绑定飞书/钉钉/Slack/Teams 等十余渠道

## 适用场景

- 搭建企业内部知识库问答系统
- 用画布编排多步检索与 LLM 工作流并发布到聊天渠道
- 作为前后端分离的全栈管理后台起始框架二次开发

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: > **LightningRAG** is built around **RAG**: **knowledge bases** (ingest, parse, chunk, vector retrieval), pluggable
> L23: - **Knowledge bases & RAG**: Ingest documents, parse and chunk, embed into pluggable vector stores; hybrid / multi-

## 星数曲线

```mermaid
xychart-beta
    title "LightningRAG/LightningRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 453 --> 455
    line [454, 454]
```

2026-10-18 454 → 2026-10-29 454（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `3a46c3c3a184` · [字段定义](../../DATASET.md)*
