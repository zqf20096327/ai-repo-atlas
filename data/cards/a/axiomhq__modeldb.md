# axiomhq/modeldb

⭐ 14 · TypeScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/axiomhq/modeldb) · [官网](https://modeldb.axiom.co) · 组织维护

**免费托管的 AI 模型元数据与价格查询 REST API**

由 Axiom 维护的模型元数据 API 服务：基于 LiteLLM 社区模型数据库构建，收录 1000+ 模型、40+ 提供商，提供按 token 与百万 token 计的实时定价、上下文窗口、能力标签（视觉/函数调用/JSON 模式）等字段。支持前缀、提供商、能力、弃用状态等过滤参数，输出 JSON/CSV/JSONL，无需认证。数据经 Cloudflare Cron 每小时刷新至 KV 与 Workers Cache，采用缓存优先的服务架构，可自行部署到 Cloudflare Workers。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1000+ 模型、40+ 提供商的元数据与实时定价
- 支持能力/提供商/弃用状态过滤与 CSV/JSONL 导出
- 数据每小时经 Cloudflare Cron 从 LiteLLM 同步
- 无需认证，CORS 启用，提供 OpenAPI 3.1 规范

## 适用场景

- 应用中做模型选型与成本估算
- 对比不同模型的能力与上下文窗口
- 批量导出模型价格数据用于数据分析

## 场景标签

 · 领域:LLM 基础设施/模型目录

## 证据(README 行号)

> L8: REST API service for AI model metadata and costs.
> L16: ModelDB provides a comprehensive database of AI language models with their associated metadata including costs, con
> L20: - Built from LiteLLM's community-maintained model pricing data

## 星数曲线

```mermaid
xychart-beta
    title "axiomhq/modeldb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6aec0ae28720` · [字段定义](../../DATASET.md)*
