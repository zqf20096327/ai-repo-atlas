# n-kostadinov/yfinance-agent-mcp

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/n-kostadinov/yfinance-agent-mcp) · [官网](https://n-kostadinov.github.io/yfinance-agent-mcp/) · 个人维护

**给 AI 交易研究 agent 提供只读 Yahoo Finance 行情数据的 MCP 服务器**

基于 yfinance 的只读 Model Context Protocol 服务器，通过 uvx 运行、以 stdio 通信，向 AI agent 提供 13 个工具：报价、带技术指标的价史、新闻、筛选器、财报与经济日历、基本面、分析师观点、期权与实时价格。响应附带 as_of 时间戳、延迟分钟数等新鲜度字段，错误以 rate_limited/not_found 等可操作形式返回；带进程级限速、HTTP 429 后暂停与短时缓存，新闻文本标记为 untrusted 字段。只能读数据，不能下单。

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

- 13 个覆盖 yfinance 全部能力的面向 agent 工具
- 响应默认控制在 20,000 字符内，含指标而非原始 K 线
- 每个回答带 as_of/market_state/delay_min 新鲜度字段
- 限速、缓存与 429 暂停机制，只读不可交易

## 适用场景

- 让 Claude Code 等 MCP 客户端查询个股新闻与价格走势
- 按成交量和分析师上调筛选当日涨幅居前的证券
- 对比两家公司的估值、利润率与六个月趋势

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L9: **yfinance-agent-mcp** is a read-only Model Context Protocol server that gives AI agents market data from Yahoo Fina
> L31: You need uv. `uvx` downloads and runs the server; it talks MCP over stdio.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `cd7de4da98aa` · [字段定义](../../DATASET.md)*
