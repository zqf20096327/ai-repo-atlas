# qdrant/qdrant-dotnet

⭐ 231 · C# · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/qdrant/qdrant-dotnet) · 组织维护

**Qdrant 向量数据库的官方 .NET SDK**

由 Qdrant 组织维护的 .NET 客户端库，以 NuGet 包 Qdrant.Client 分发，通过底层 gRPC 客户端连接 Qdrant 服务（默认 localhost:6334）。高层 API 覆盖集合创建、向量插入、相似度检索与带过滤条件的检索；支持 TLS 证书指纹校验与 API key 认证，自动附加 qdrant-dotnet 版本号的 User-Agent。对 .NET Framework 有 gRPC over HTTP/2 的限制说明，需配置 TLS 与 WinHttpHandler。

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

- 高层 QdrantClient 封装 gRPC 通道，支持 TLS 与 API key 认证
- 覆盖集合创建、向量插入、相似度检索与过滤检索
- 自动在请求中附加 qdrant-dotnet/<version> User-Agent
- 针对 .NET Framework 的 WinHttpHandler 配置说明

## 适用场景

- 在 .NET 项目中连接并操作 Qdrant 向量数据库
- 为 .NET 应用添加向量相似度检索能力
- 需要 TLS 与 API key 认证的安全连接场景

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L1: # Qdrant .NET SDK
> L9: dotnet add package Qdrant.Client
> L28: Internally, the high level client uses a low level gRPC client to interact with Qdrant.

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-dotnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 230 --> 232
    line [231, 231]
```

2026-10-18 231 → 2026-10-31 231（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `db909571a2a5` · [字段定义](../../DATASET.md)*
