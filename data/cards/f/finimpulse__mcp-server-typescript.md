# finimpulse/mcp-server-typescript

⭐ 11 · TypeScript · 推送 2026-11-25 · [GitHub](https://github.com/finimpulse/mcp-server-typescript) · [官网](https://developers.finimpulse.com/) · 组织维护

**给 AI 客户端提供金融数据的 MCP 服务器**

实现 Model Context Protocol 的服务器，将 FinImpulse API 的金融数据（股票、ETF、共同基金、基本面、市场指标等）以标准化 MCP 接口暴露给 AI 系统与开发工具。提供两种接入方式：托管端点（Streamable HTTP + OAuth）或本地 stdio 运行（Node.js 18+ 与 API token）。暴露 39 个工具、分 11 个功能组，覆盖搜索、价格、财报、分析师评级、持仓、期权链与宏观经济数据，并给出 Cursor、Claude Desktop、ChatGPT 等多客户端的配置示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 39 个 MCP 工具分 11 组，覆盖价格、财报、分析师、持仓、期权、宏观数据
- 托管端点支持 Streamable HTTP + OAuth，无需手动配置 API token
- 提供约 39,000 个全球市场指数搜索与历史时间序列数据
- 给出 Cursor、Claude Desktop/Code、ChatGPT、VS Code 等客户端配置示例

## 适用场景

- 让 AI 投资助手用自然语言查询公司基本面与估值指标
- 构建自动化的金融研究工作流
- 在开发环境中通过 MCP 获取行情与期权链数据
- 为 AI 仪表盘接入分析师评级与内部人交易数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides structured financial market data to AI systems and development t
> L18: The MCP server translates tool calls from AI clients into FinImpulse API requests and returns structured responses 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `966d6a1adab3` · [字段定义](../../DATASET.md)*
