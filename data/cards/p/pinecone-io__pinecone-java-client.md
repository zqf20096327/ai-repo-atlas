# pinecone-io/pinecone-java-client

⭐ 51 · Java · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/pinecone-io/pinecone-java-client) · [官网](https://www.pinecone.io) · 组织维护

**Pinecone 向量数据库官方 Java 客户端，供 JVM 应用接入**

由 Pinecone 官方维护的 Java SDK，供 JVM 应用与 Pinecone 向量数据库服务交互。覆盖控制面操作（创建/列出/描述/删除 serverless、pod、BYOC 索引，配置读容量与删除保护）与数据面操作（向量 upsert/query/fetch/update/delete/list，支持元数据过滤）。客户端通过 apiKey 初始化，内置共享 OkHttpClient，支持自定义 OkHttpClient、HTTP 代理、禁用 TLS 校验，并可捕获响应元数据（延迟、读单元等）对接 OpenTelemetry/Prometheus/Datadog。要求 Java 1.8+，需 Pinecone 账号与 API key，属云服务依赖而非本地运行时。

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

- 控制面与数据面完整 API：索引管理与向量增删改查
- 支持 serverless、pod、BYOC 三类索引及读容量配置
- 响应元数据捕获，可对接 OpenTelemetry/Prometheus/Datadog 观测
- 支持自定义 OkHttpClient、HTTP 代理与 TLS 配置

## 适用场景

- 在 Java 服务中实现向量存储与相似度检索（RAG 检索层）
- 通过代码管理 Pinecone 索引生命周期与容量配置
- 采集向量操作延迟与用量指标用于监控

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L1: # Pinecone Java SDK
> L3: The Pinecone Java SDK lets JVM applications interact with Pinecone services.

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pinecone-java-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f4f656513852` · [字段定义](../../DATASET.md)*
