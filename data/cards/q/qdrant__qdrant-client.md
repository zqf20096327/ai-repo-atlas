# qdrant/qdrant-client

⭐ 1,373 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/qdrant/qdrant-client) · [官网](https://qdrant.tech) · 组织维护

**Qdrant 向量搜索引擎的 Python 客户端库与 SDK**

为 Qdrant 向量搜索引擎提供同步与异步的 Python 客户端，覆盖全部 API 方法的类型定义，支持 REST 与 gRPC 两种协议。提供本地模式（内存或持久化到磁盘），无需运行服务端即可在 CI/CD、Colab、Jupyter 中使用同一套代码。内置 Inference API：本地可经 FastEmbed（基于 ONNX Runtime，支持 CPU/GPU）生成嵌入并上传，或使用 Qdrant Cloud 的远程推理（付费计划）。以 pip 包形式安装。

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

- 全部 Qdrant API 方法的类型提示，同步/异步双客户端
- 本地模式：内存或磁盘持久化，无需服务端即可开发与测试
- REST 与 gRPC 支持，gRPC 加速批量上传
- 经 FastEmbed 本地生成嵌入（CPU/GPU）或 Qdrant Cloud 远程推理

## 适用场景

- 在 Python 项目中连接并操作 Qdrant 向量数据库
- 在笔记本或 CI 中用本地模式原型开发与测试向量检索
- 本地生成嵌入并上传向量以简化 RAG 流程

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3:  Python Client library for the Qdrant vector search engine.
> L15: Library contains type definitions for all Qdrant API and allows to make both Sync and Async requests.

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 1373 --> 1375
    line [1374, 1374]
```

2026-10-18 1,374 → 2026-10-22 1,374（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `91b6faaa8761` · [字段定义](../../DATASET.md)*
