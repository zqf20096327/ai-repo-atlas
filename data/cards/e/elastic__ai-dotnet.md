# elastic/ai-dotnet

⭐ 21 · C# · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/elastic/ai-dotnet) · 组织维护

**Elasticsearch 官方 .NET 向量库连接器，接入 Semantic Kernel**

Elastic 官方维护的 .NET 库集合，含两个包：Elastic.SemanticKernel.Connectors.Elasticsearch 实现 Microsoft Semantic Kernel 的向量库抽象，支持通过 Elasticsearch 索引进行记录集合的创建、上传、检索与删除，支持 HNSW/FLAT 索引（32/8/4 bit 及 BBQ）、多种距离函数、混合搜索与多向量记录；Elastic.Extensions.AI 提供 Microsoft.Extensions.AI 的嵌入生成器实现。经 NuGet 安装，可接入 DI 容器或直接实例化，数据映射基于 System.Text.Json。

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

- 实现 Semantic Kernel Vector Store 抽象的官方 Elasticsearch 连接器
- 支持 HNSW/FLAT（32/8/4 bit、BBQ）索引与四种距离函数
- 支持混合搜索、全文索引与单记录多向量
- 附带 Microsoft.Extensions.AI 嵌入生成器包 Elastic.Extensions.AI

## 适用场景

- 在 Semantic Kernel 应用中用 Elasticsearch 作为向量存储后端
- 本地开发用 start-local 脚本起 Elasticsearch 后接入 RAG 管线
- 在 ASP.NET Core 项目中通过 DI 扩展方法注册向量库

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5: - `Elastic.SemanticKernel.Connectors.Elasticsearch` — The official Elasticsearch Vector Store Connector for Microsof
> L6: - `Elastic.Extensions.AI` — Elasticsearch embedding generator implementing Microsoft.Extensions.AI.
> L16: This repository contains the official Elasticsearch Vector Store Connector implementation for Semantic Kernel.

## 星数曲线

```mermaid
xychart-beta
    title "elastic/ai-dotnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b41999a92bda` · [字段定义](../../DATASET.md)*
