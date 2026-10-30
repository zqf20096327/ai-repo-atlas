# smclab/openk9

⭐ 51 · Java · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/smclab/openk9) · [官网](https://www.openk9.io) · 组织维护

**面向企业的开源认知搜索引擎，用 ML 增强非结构化数据检索**

OpenK9 是一个开源认知搜索引擎，采用可扩展微服务架构，用机器学习增强非结构化数据以构建搜索体验。核心栈含 PostgreSQL、OpenSearch、RabbitMQ、API Gateway、Ingestion、Searcher 与前端；可选 profile 增加文件处理（Tika/Docling/SeaweedFS）、生成式 AI（RAG 模块、Embedding 模块、Talk-To 对话搜索）与 Keycloak OAuth2。通过 docker compose 一条命令运行，开发者可用 k9.sh 脚本（封装 Maven/Docker/Compose）从源码构建，生产环境建议以 Helm Chart 部署到 Kubernetes/OpenShift。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- docker compose up -d 一条命令启动核心栈
- gen-ai profile 提供 RAG、Embedding 与 Talk-To 对话搜索
- k9.sh 开发脚本封装 Maven/Docker/Compose 并含 doctor 前置检查
- 生产部署提供 Kubernetes/OpenShift 的 Helm Chart 指南

## 适用场景

- 企业内构建对非结构化文档的认知搜索
- 为搜索体验添加 RAG 对话式问答
- 在 Kubernetes/OpenShift 上部署生产级搜索服务

## 场景标签

`语义搜索` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: OpenK9 is a new Cognitive Search Engine that allows you to build next generation search experiences. It employs a sc
> L40: |`gen-ai`|`compose-with-gen-ai.yaml`|RAG module, Embedding module, Talk-To chat|

## 星数曲线

```mermaid
xychart-beta
    title "smclab/openk9 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `02b89740e25b` · [字段定义](../../DATASET.md)*
