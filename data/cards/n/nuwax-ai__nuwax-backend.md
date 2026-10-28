# nuwax-ai/nuwax-backend

⭐ 39 · Java · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/nuwax-ai/nuwax-backend) · [官网](https://nuwax.com) · 组织维护 · 中文 README

**企业级 AI Agent 开发运营平台的后端服务**

Java 17 / Spring Boot 3.3.8 实现的 AI Agent 平台后端，提供可视化拖拽工作流编排、Java/Python 插件开发、多模型接入（OpenAI/Claude/Ollama/Qwen 等）、知识库管理（Milvus 向量检索 + Elasticsearch 全文的混合检索）、长短期记忆系统、模型代理（标注 In Development）、MCP 协议支持与插件市场。运行依赖 MySQL、Redis、Milvus、Elasticsearch 等基础服务，属于 nuwax-ai 多仓库体系的应用层，采用 DDD 分层架构，Apache 2.0 许可并另设商业许可条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽式零代码 Agent 工作流编排，支持 Java/Python 插件扩展
- 知识库混合检索：Milvus 向量 + 全文检索 + QA 检索
- 12 主类 50+ 子类的记忆系统与敏感信息过滤
- MCP 协议实现与插件市场

## 适用场景

- 企业搭建自有 Agent 平台并管理知识库与记忆
- 通过统一接口代理多家模型 API 并做配额计费
- 以插件生态扩展 Agent 能力并发布到插件市场

## 场景标签

`Agent 框架` `RAG` `模型网关` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Enterprise-grade AI Agent Development and Operation Platform** - Providing a complete solution for agent creation 
> L15: ### Agent Engine
> L204: |**Model Proxy**|Unified model proxy interface|

## 星数曲线

```mermaid
xychart-beta
    title "nuwax-ai/nuwax-backend 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f40af0de1327` · [字段定义](../../DATASET.md)*
