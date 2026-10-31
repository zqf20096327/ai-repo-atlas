# BuyWhere/buywhere-mcp

⭐ 15 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/BuyWhere/buywhere-mcp) · [官网](https://buywhere.ai) · 组织维护

**供 AI agent 搜索比价 3 亿+商品 MCP 服务器**

通过 Model Context Protocol 向 AI agent 提供商品搜索与比价能力的 MCP 服务器：聚合新加坡、美国、马来西亚、泰国、越南市场的 Lazada、Shopee、Amazon 及本地商家数据，提供 search/compare/deals/best_price 等 13 个工具，支持 stdio 与远程 JSON-RPC 两种接入，另支持 A2A 协议。需申请 API key（可 POST 免注册即取），npx 直接运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个 MCP 工具：搜索/比价/最低价/降价追踪/相似推荐/商品收录
- 覆盖新加坡、美国、马来西亚、泰国、越南市场与多币种实时定价
- 支持 stdio 与远程 JSON-RPC 两种 MCP 接入及 A2A 协议
- 免注册免邮箱的 API key 自助发放

## 适用场景

- 让 Claude/Cursor 等 agent 帮我搜商品、比价、找降价
- 构建跨市场（东南亚+美国）购物 agent
- 把商品搜索能力集成进 CrewAI/Mastra/LangChain 等 agent 框架

## 场景标签

 · 领域:电商/agent 基础设施

## 证据(README 行号)

> L3: > **AI agents use BuyWhere to search products, compare prices, and discover deals across Singapore and US merchants 
> L41: Product search API for AI agents via Model Context Protocol. Built for AI agent commerce, not store management.
> L109: Remote MCP: `POST https://api.buywhere.ai/mcp` (JSON-RPC 2.0, protocolVersion 2024-11-05, 13 tools). Glama listing

## 星数曲线

```mermaid
xychart-beta
    title "BuyWhere/buywhere-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c5215410aa45` · [字段定义](../../DATASET.md)*
