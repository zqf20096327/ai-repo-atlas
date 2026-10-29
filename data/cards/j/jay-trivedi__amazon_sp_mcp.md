# jay-trivedi/amazon_sp_mcp

⭐ 33 · TypeScript · MIT · 推送 2025-11-17 · [GitHub](https://github.com/jay-trivedi/amazon_sp_mcp) · 个人维护

**让 AI 代理读取亚马逊卖家后台数据的 MCP 服务器**

基于 Node.js/TypeScript 的 Model Context Protocol 服务器，通过 Amazon Selling Partner API（SP-API）向 AI 代理开放卖家数据：订单与销售指标、退货退款、FBA/FBM 库存、商品 listing 与 ASIN 目录、报告生成与下载。认证采用 LWA OAuth 2.0 与 AWS 凭证，内置按 SP-API 限额的自动限流与请求队列、401 自动刷新令牌、429/5xx 重试。可与 Google Sheets、PostgreSQL 等 MCP 组合做利润分析；订单履约、定价、广告等为规划中功能。需 Claude Code/Claude Desktop 等 MCP 客户端使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 19 个 MCP 工具覆盖销售/退货/库存/listing/报告五类数据
- LWA OAuth 2.0 认证，令牌自动刷新与 401/429/5xx 重试
- 基于 SP-API 限额的自动限流与请求队列
- 可与 Google Sheets/PostgreSQL/Filesystem MCP 组合做多源业务分析

## 适用场景

- 在 Claude 中用自然语言查询订单、销量与库存数据
- 结合 Google Sheets 成本表让 AI 代理计算 SKU 利润率
- 拉取亚马逊卖家报告并做退货与库存健康分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides AI agents with access to Amazon Seller Central data through the 
> L7: This MCP server enables AI agents to interact with Amazon Seller Central, allowing them to retrieve sales data, inve

## 星数曲线

```mermaid
xychart-beta
    title "jay-trivedi/amazon_sp_mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [33, 32, 33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `41598a1426f0` · [字段定义](../../DATASET.md)*
