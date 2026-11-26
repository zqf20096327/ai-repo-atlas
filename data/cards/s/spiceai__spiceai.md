# spiceai/spiceai

⭐ 3,130 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/spiceai/spiceai) · [官网](https://docs.spiceai.org) · 组织维护

**给运营数据库加实时分析节点的数据与 AI 引擎**

Rust 编写的单二进制数据与 AI 运行时，通过 spicepod.yaml 声明 30+ 数据源（PostgreSQL、MySQL、Snowflake、S3、Iceberg 等），可按数据集在内存/本地盘物化加速，经 CDC 保持约 2 秒新鲜度；对应用提供 SQL 查询（HTTP/Arrow Flight/JDBC/ODBC）、向量与全文混合检索、OpenAI 兼容 LLM 网关与 MCP server。面向为 AI 应用与 agent 构建数据基础设施的开发者，可作为 sidecar、独立服务或分布式集群运行。本仓库为 Apache-2.0 开源运行时，另有云端与企业发行版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 PostgreSQL/MySQL/MongoDB 的原生 CDC 实时复制，无需 ETL、Debezium 或 Kafka
- OpenAI 兼容 LLM 网关、MCP server+gateway、NSQL text-to-SQL、本地模型服务（CUDA/Metal 加速）
- 30+ 数据连接器与查询下推；Iceberg 读写含 ACID 的 SQL INSERT
- Cayenne 加速引擎（基于 Vortex）与 Ballista 分布式查询

## 适用场景

- 在不给生产库增加分析负载的前提下做实时分析查询
- 为 AI 应用统一提供 SQL、向量检索与 LLM 推理接口
- 作为应用旁的 sidecar 提供本地毫秒级数据查询

## 场景标签

`数据分析` `向量数据库` · 领域:效率与自动化

## 证据(README 行号)

> L16: **Spice** (Spice.ai Open Source) is a data and AI engine that brings your data to your application. Connect it to t
> L40: - 🤖 **AI-native runtime** — OpenAI-compatible APIs, MCP server + gateway, LLM memory, NSQL text-to-SQL, multi-vecto
> L55: 3. **OpenAI-Compatible APIs**: Hosted LLM gateway (OpenAI, Anthropic, xAI, Bedrock, Google Vertex AI, Databricks) a

## 星数曲线

```mermaid
xychart-beta
    title "spiceai/spiceai 星数(近 24 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-26"]
    y-axis "stars" 3099 --> 3166
    line [3104, 3105, 3104, 3108, 3110, 3113, 3116, 3120, 3122, 3105, 3130, 3143, 3148, 3149, 3150, 3151, 3153, 3155, 3156, 3160, 3161, 3150, 3132, 3130]
```

2026-10-24 3,104 → 2026-11-26 3,130（+26）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `0da46e77805f` · [字段定义](../../DATASET.md)*
