# isdaniel/pgtuner_mcp

⭐ 30 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/isdaniel/pgtuner_mcp) · 个人维护

**PostgreSQL 性能调优的 MCP 服务器：供 AI 客户端分析慢查询与索引**

面向 MCP 客户端（如 Claude Desktop、Cline）的 PostgreSQL 性能调优服务器。提供慢查询检索（pg_stat_statements）、EXPLAIN/EXPLAIN ANALYZE 执行计划分析、基于工作负载的索引推荐，并借助 HypoPG 扩展在不建真实索引的情况下测试假设索引效果。另含数据库健康评分、锁等待、Vacuum 监控、I/O 与膨胀分析（pgstattuple）、配置审查等工具。支持 stdio/SSE/Streamable HTTP 三种模式，通过 DATABASE_URI 连接数据库；HTTP 模式自身不含认证与 TLS，网络部署需反向代理。

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

- 从 pg_stat_statements 检索慢查询并自动分析执行计划问题
- 基于 HypoPG 的假设索引测试（不占磁盘、不建真实索引）
- 数据库健康评分、Vacuum 进度、I/O 模式与膨胀分析（pgstattuple）
- stdio / SSE / Streamable HTTP 三种服务模式

## 适用场景

- 在 Claude Desktop 等 MCP 客户端中让 AI 分析和调优 PostgreSQL
- 在创建索引前用假设索引验证查询计划改进
- 监控数据库健康、Vacuum 进度与膨胀情况

## 场景标签

 · 领域:数据库运维/开发工具

## 证据(README 行号)

> L13: A Model Context Protocol (MCP) server that provides AI-powered PostgreSQL performance tuning capabilities. This ser
> L66: ### Standard Installation (for MCP clients like Claude Desktop)

## 星数曲线

```mermaid
xychart-beta
    title "isdaniel/pgtuner_mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `377e697d0ad2` · [字段定义](../../DATASET.md)*
