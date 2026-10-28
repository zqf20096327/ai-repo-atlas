# asgard-ai-platform/mcp-shopline

⭐ 20 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/asgard-ai-platform/mcp-shopline) · 组织维护 · 中文 README

**将 Shopline 开放 API 封装为 143 个 AI 可调用工具的 MCP 服务器**

面向 Shopline 电商商家的 MCP（Model Context Protocol）服务器：以 stdio JSON-RPC 2.0 方式将 Shopline Open API v1 封装为 143 个工具（75 读 + 68 写），覆盖订单、商品、库存、客户 RFM 分析、促销活动、退货、客服会话、评价等类别；供 Claude Code、Claude Desktop 等 MCP 兼容客户端的 AI agent 通过自然语言调用。内置分页、重试与限流处理，外部依赖仅 Python 3.9+ 标准库与 requests。需提供 Shopline 商家 API token，写操作受 token 权限范围控制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 143 个工具（75 读 + 68 写）覆盖订单/商品/库存/客户/促销/客服等类别
- 内置分页、重试与限流，工具内部处理 API 复杂性
- 结构化 JSON 输出，日期采用 YYYY-MM-DD 等对自然语言友好的参数
- 外部依赖仅 Python 3.9+ 标准库与 requests

## 适用场景

- 在 Claude Code/Desktop 中用自然语言查询店铺销售、库存与客户数据
- 让 AI agent 执行订单发货、促销创建、评价回复等店铺运营写操作
- 做客户 RFM 分层与促销 ROI 分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: An open-source MCP (Model Context Protocol) server that wraps the Shopline Open API into 143 AI-callable tools (75 
> L15: Built for Claude Code, Claude Cowork, and any MCP-compatible AI client. Enables AI agents to query orders, products

## 星数曲线

```mermaid
xychart-beta
    title "asgard-ai-platform/mcp-shopline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d4f9a426b7fe` · [字段定义](../../DATASET.md)*
