# SemiAnalysisAI/InferenceX-app

⭐ 48 · TypeScript · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/SemiAnalysisAI/InferenceX-app) · [官网](https://inferencex.com) · 组织维护 · 中文 README

**LLM 推理基准数据的可视化仪表板（Next.js）**

InferenceX 的开源前端与数据层 monorepo：以 Next.js 16 + TypeScript 构建仪表板，从 Neon PostgreSQL（或标准 PostgreSQL）读取持续基准测试数据，经 API 路由与 React Query 供 D3.js 绘制交互图表，展示各模型×硬件组合下不同张量并行度与并发数的吞吐-延迟曲线。仓库另含共享常量包、DB 层（ETL/迁移/摄取脚本）与暴露只读基准工具的 MCP 服务器。面向关注 LLM 推理性能的开发者与研究者，自部署需 Bun、Node.js 24 及一个 PostgreSQL 数据库，生产部署在 Vercel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Next.js + D3.js 的基准数据可视化前端，DB-backed
- monorepo 含 db/constants/mcp 包，MCP 服务器暴露只读基准工具
- 支持标准 PostgreSQL 与 Neon 两种数据库驱动
- 提供数据库迁移、数据摄取与缓存管理脚本

## 适用场景

- 查看主流模型在各硬件平台上的夜间推理基准结果
- 自部署仪表板分析自己的基准数据库
- 通过 MCP server 以只读工具查询基准数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A Next.js dashboard for visualizing ML inference benchmark data. DB-backed with Neon PostgreSQL, React Query for dat
> L11: LLM inference performance is a major concern of providing AI services, but accurate performance analysis remains el
> L19: The frontend fetches data from API routes backed by a Neon PostgreSQL read replica. All presentation logic lives in

## 星数曲线

```mermaid
xychart-beta
    title "SemiAnalysisAI/InferenceX-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 46 --> 49
    line [47, 48]
```

2026-10-18 47 → 2026-10-26 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4ed22310f7e1` · [字段定义](../../DATASET.md)*
