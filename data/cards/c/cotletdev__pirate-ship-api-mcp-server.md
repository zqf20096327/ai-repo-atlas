# cotletdev/pirate-ship-api-mcp-server

⭐ 6 · Python · NOASSERTION · 推送 2026-11-10 · [GitHub](https://github.com/cotletdev/pirate-ship-api-mcp-server) · [官网](https://cotlet.dev/integrations/pirate-ship-api-mcp-server) · 组织维护

**让 AI agent 操作 Pirate Ship 寄送业务的 MCP 服务器**

为 Pirate Ship（ USPS/UPS 打标签发货工具）提供非官方 API 与 MCP 服务器：自托管版在本地 Python 运行，暴露 51 个工具（费率查询、草稿标签与批次、SCAN Form、追踪、报表、店铺订单导入等），通过读取本机 Chrome 登录会话 cookie 并以 curl_cffi 模拟其 GraphQL 接口工作；花钱/退款类 6 个工具不含在内。另提供托管版 Cotlet（7 天免费，之后按量付费），供非技术卖家在 ChatGPT/Claude 应用内使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 51 个 Pirate Ship 工具，MCP（stdio/HTTP）与本地 REST API（含 OpenAPI 文档）双通道
- 通过 Chrome DevTools Protocol 读取会话 cookie，无需存储密码
- 带 persisted query 哈希白名单（operations.py），限制可发送的操作范围
- 工具标注只读/需确认提示，花钱退款类工具不包含在开源版中

## 适用场景

- 在 Claude Code/Cursor 里用自然语言查 USPS/UPS 运费并生成草稿标签
- 脚本或 n8n 自动化批量打单与追踪核查
- 查最近无承运商扫描的标签和月度运费支出报表

## 场景标签

 · 领域:电商/物流工具

## 证据(README 行号)

> L33: A **Pirate Ship API** and a **Pirate Ship MCP server** you run on your own computer, in Python, on the session of y
> L37: - **MCP server** for Claude Code, Claude Desktop, Cursor, Codex and any MCP client, over stdio or HTTP. Setup

## 星数曲线

```mermaid
xychart-beta
    title "cotletdev/pirate-ship-api-mcp-server 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-20"]
    y-axis "stars" 5 --> 7
    line [6, 6]
```

2026-11-08 6 → 2026-11-20 6（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `56b8745db420` · [字段定义](../../DATASET.md)*
