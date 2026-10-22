# imbenrabi/Financial-Modeling-Prep-MCP-Server

⭐ 150 · TypeScript · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server) · 个人维护

**为 AI 助手接入 Financial Modeling Prep 金融数据的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Financial Modeling Prep API 的 250+ 金融数据工具（覆盖股票、ETF、加密货币、外汇、大宗商品、宏观经济等 24 类）暴露给 AI 助手。支持 Dynamic/Static/All Tools 三种运行模式，内置运行时启用/禁用工具集的 meta-tools；通过 HTTP/SSE 传输，兼容 Claude.ai、Claude Desktop 及 MCP 注册表。提供托管实例，也可经 npm、Docker 或源码自托管，需自备 FMP API key，Node.js 25.3.0+（v2.6.0+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 250+ 金融数据工具，覆盖 24 个类别
- 三种服务器模式与运行时工具集管理的 meta-tools
- HTTP/SSE 传输，兼容 Claude.ai/Claude Desktop/MCP 注册表
- 托管实例可用，或 npm/Docker/源码自托管

## 适用场景

- 让 Claude 等 AI 助手查询股票行情与公司基本面数据
- 在 MCP 客户端中接入金融数据源做分析
- 通过 meta-tools 按需加载所需金融工具集

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L6: A Model Context Protocol (MCP) server for the Financial Modeling Prep API, exposing 250+ financial data tools to AI 
> L14: - **HTTP/SSE Transport** — compatible with Claude.ai, Claude Desktop, and MCP registries

## 星数曲线

```mermaid
xychart-beta
    title "imbenrabi/Financial-Modeling-Prep-MCP-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-22 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `769da5f440a0` · [字段定义](../../DATASET.md)*
