# PCDCK/ozon-mcp

⭐ 23 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/PCDCK/ozon-mcp) · [官网](https://github.com/PCDCK/ozon-mcp) · 个人维护

**连接 AI 代理与 Ozon 卖家后台的 MCP 服务器（15 个工具）**

基于 FastMCP 的 MCP stdio 服务器，把 Ozon Seller API（420 方法）与 Performance API（46 方法）封装为 15 个工具，供 Claude、Cursor、Cline 等 MCP 客户端调用。内置 466 方法的 BM25 俄/英检索、5 档订阅级别门控、四种分页风格的自动翻页、429 指数退避与按端点排队、read/write/destructive 三级安全确认（43 个破坏性方法双重门控），并提供 13 个分析工作流（缺货风险、定价分析、订单同步等）。需 Python 3.12/3.13、uv 及 Ozon API 凭据，git clone 源码运行。

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

- 索引 466 个 Ozon API 方法，BM25 俄/英双语检索
- 订阅级别感知：Premium 门控方法在本地即拒绝调用
- 自动处理四种分页模式与速率限制（429 退避、Retry-After、按端点排队）
- 13 个预置分析工作流（缺货风险、健康检查、订单/财务同步等）

## 适用场景

- 在 Claude/Cursor 等客户端里用自然语言查询和管理 Ozon 店铺商品
- 运行缺货风险、定价、内容质量等分析工作流
- 增量同步订单、财务流水与广告数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: ozon-mcp is a knowledge-rich MCP server that turns the entire Ozon
> L53: ozon-mcp uses the standard MCP stdio transport. Every example below

## 星数曲线

```mermaid
xychart-beta
    title "PCDCK/ozon-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c2628bc44aa2` · [字段定义](../../DATASET.md)*
