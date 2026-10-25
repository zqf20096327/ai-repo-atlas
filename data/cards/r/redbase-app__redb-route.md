# redbase-app/redb-route

⭐ 41 · C# · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/redbase-app/redb-route) · [官网](https://redbase.app) · 组织维护

**.NET 版 Apache Camel 式企业集成框架：任何系统接任何系统**

面向 .NET 开发者的企业集成框架，用流式 C# DSL 通过 From → Process → To 管道连接 Kafka、RabbitMQ、SQL、HTTP、gRPC、SFTP、MQTT、S3 等 29 种外部传输，内置 30+ 企业集成模式（EIP）与编译期表达式引擎。AI 相关能力包括 llm: 连接器（OpenAI 兼容 14 家厂商 + 原生 Anthropic Messages API）、mcp: MCP 客户端连接器、以及把任意传输暴露为 LLM 可调用工具的 .AsLlmTool()。生产部署依赖配套运行时 redb.Tsak（热重载、集群、REST API）。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 种外部传输 + 30+ EIP 模式，From→Process→To 流式 C# DSL
- llm: 连接器支持 OpenAI 兼容 14 家厂商与原生 Anthropic Messages API
- mcp: 连接器可启动外部 MCP server 并将其工具注册为可调用工具
- .AsLlmTool() 将其余 28 种传输暴露为 LLM 工具，端到端 token 流式输出

## 适用场景

- 在不同协议间做消息桥接与转换（如 Kafka → RabbitMQ、FTP → SQL）
- 构建文件摄取、webhook 分发、定时任务等集成管道
- 让 LLM agent 通过 MCP 与工具化传输调用企业系统

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: redb.Route is the .NET equivalent of Apache Camel — a fluent C# DSL that connects Kafka, RabbitMQ, Redis, SQL, HTTP,
> L23: - **29 external transports + 5 built-in components** (Direct, SEDA, Timer, Mock, Log). One of them — `llm:` — is a 

## 星数曲线

```mermaid
xychart-beta
    title "redbase-app/redb-route 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `563f4f11e998` · [字段定义](../../DATASET.md)*
