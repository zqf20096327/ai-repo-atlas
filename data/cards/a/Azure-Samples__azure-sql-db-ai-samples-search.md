# Azure-Samples/azure-sql-db-ai-samples-search

⭐ 35 · TSQL · 推送 2026-03-23 · [GitHub](https://github.com/Azure-Samples/azure-sql-db-ai-samples-search) · [官网](https://repos.opensource.microsoft.com/Azure-Samples/wizard?existingreponame=azure-sql-db-ai-samples-search&existingrepoid=886308952) · 组织维护

**Azure SQL 混合 RAG 示例应用：代码样例语义搜索**

微软 Azure-Samples 出品的端到端示例：用 Azure SQL 存储 Azure SQL 样例数据与向量嵌入，实现 Hybrid RAG——先用 LLM 判断问题可否仅用数据库 Schema 与 SQL 精确回答，否则走向量 RAG 语义检索，最终由 GPT-4o 生成结构化 JSON 答案并可与库中数据 join。架构含 Data API builder 暴露存储过程、React 前端，可本地运行或部署到 Azure Static Web Apps/Container Apps。需自备 Azure OpenAI 订阅，数据库须支持 vector 类型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hybrid RAG：精确 SQL 查询与语义向量检索两条路径结合
- RAG 逻辑以存储过程形式完全实现在数据库内
- 结果由 GPT-4o 生成结构化 JSON，可与库中数据 join
- 提供 React 前端 + Data API builder + Azure 部署方案

## 适用场景

- 学习如何在 Azure SQL 中实现向量检索与 RAG 模式
- 搭建代码样例/文档的语义搜索网站
- 参考 SQL Server 2025 vector 类型的应用开发方式

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: This sample demonstrates how to use Azure SQL to store and search data with AI. The sample uses RAG pattern, impleme
> L34: In either case the output is then sent back to the LLM to generate a final answer. Answer that is asked to be retur

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-sql-db-ai-samples-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7d3af3269e82` · [字段定义](../../DATASET.md)*
