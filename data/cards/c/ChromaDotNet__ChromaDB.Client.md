# ChromaDotNet/ChromaDB.Client

⭐ 36 · C# · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ChromaDotNet/ChromaDB.Client) · [官网](https://chromadotnet.org) · 组织维护

**Chroma 向量数据库的 .NET 客户端库，支持 Chroma Cloud**

发布于 NuGet 的 .NET 客户端（ChromaDotNet.Client），为 Chroma 与 Chroma Cloud 提供集合/租户/数据库管理、记录读写、带过滤的最近邻查询、Chroma Cloud Search API（含 BM25 混合检索）以及 OpenTelemetry 追踪与指标。系社区项目，为 ssone95/ChromaDB.Client 的延续（原包已在 NuGet 标记弃用），测试覆盖 Chroma 0.4.10 至 1.5.9。配套包提供依赖注入、本地 Chroma 运行与嵌入计算，被 .NET Foundation AI Community Toolkit、Semantic Kernel 生态等项目使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖集合/租户/数据库、记录读写、带过滤的最近邻查询
- Chroma Cloud Search API 与 BM25 混合检索
- OpenTelemetry 追踪与指标支持
- 配套 ChromaDotNet.Local 免 Docker 本地运行与 ChromaDotNet.Embeddings 嵌入计算包

## 适用场景

- 在 .NET 应用中接入 Chroma 或 Chroma Cloud 存取向量数据
- 通过 GitHub Codespaces 在浏览器内快速试用库的功能
- 为 Semantic Kernel / Agent Framework 等框架提供 Chroma 后端

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L13: _ChromaDB.Client_, published on NuGet as `ChromaDotNet.Client`, is a .NET client for Chroma and Chroma Cloud. It co
> L16: - writing and reading records, and nearest neighbor queries with filters;
> L26: - CommunityToolkit.VectorData.Chroma: the Chroma provider for Microsoft.Extensions.VectorData, in the AI Community 

## 星数曲线

```mermaid
xychart-beta
    title "ChromaDotNet/ChromaDB.Client 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-24 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e05eb07f5176` · [字段定义](../../DATASET.md)*
