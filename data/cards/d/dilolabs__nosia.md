# dilolabs/nosia

⭐ 214 · Ruby · MIT · 推送 2026-11-27 · [GitHub](https://github.com/dilolabs/nosia) · [官网](https://hub.docker.com/r/dilolabs/nosia) · 组织维护

**自托管 AI RAG + MCP 平台：在私有数据上运行 AI 模型**

基于 Ruby on Rails 的自托管平台，用户在自己的基础设施上运行 AI 模型：支持上传 PDF/文本/网页/Q&A 对构建知识库，启用 RAG 后检索相关文档块并注入提示词生成回答；通过 pgvector 做向量相似度搜索，集成 MCP 连接外部工具与服务，支持自定义 Agent Skills（LLM 与 Ruby 实现）。提供 OpenAI 兼容 API（SSE 流式）与多租户账户隔离；默认通过 Docker Compose 部署，默认使用 Docker Hub AI 的 Granite 模型，可经环境变量替换补全与嵌入模型。

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

- OpenAI 兼容 API，可作为 OpenAI 客户端的 drop-in 后端
- RAG 检索基于 pgvector，支持 PDF/文本/网页/Q&A 多格式
- MCP 集成与自定义 Agent Skills 扩展能力
- 一键安装脚本自动安装 Docker 并生成 .env 配置

## 适用场景

- 在私有服务器上对自有文档进行问答
- 为现有 OpenAI 客户端应用提供自托管的兼容 API
- 通过 MCP 让模型调用日历、数据库等外部工具

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **Self-hosted AI RAG + MCP Platform**
> L5: Nosia is a platform that allows you to run AI models on your own data with complete privacy and control. Beyond trad
> L230: |`AI_BASE_URL`|Base URL for OpenAI-compatible API|`http://model-runner.docker.internal/engines/llama.cpp/v1`|

## 星数曲线

```mermaid
xychart-beta
    title "dilolabs/nosia 星数(近 6 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-14", "2026-11-28"]
    y-axis "stars" 210 --> 215
    line [214, 213, 214, 211, 214, 214]
```

2026-10-26 214 → 2026-11-28 214（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `690789aa900c` · [字段定义](../../DATASET.md)*
