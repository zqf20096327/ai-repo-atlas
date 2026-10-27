# guangxiangdebizi/TradingAgents-MCPmode

⭐ 339 · Python · 推送 2025-11-22 · [GitHub](https://github.com/guangxiangdebizi/TradingAgents-MCPmode) · [官网](http://47.79.147.241:8501/) · 个人维护 · 中文 README

**面向个人投资者的多智能体股票分析与决策系统**

基于 Model Context Protocol (MCP) 工具集成的多智能体交易分析系统：15 个专业化智能体按分析师、研究员、管理层、风险管理四团队协作，对公司概述、市场、情绪、新闻、基本面等七维度进行并行分析，通过看涨/看跌投资辩论与三方风险辩论生成投资建议与风险管理决策。支持美股、A股、港股的自然语言查询。提供 Streamlit Web 前端（可动态启停智能体、实时调整辩论轮次）与命令行两种使用方式；通过 .env 配置 OpenAI API Key 与模型参数，通过 mcp_config.json 配置 MCP 服务器（默认指向 finvestai.top 的 finance-mcp，需 Tushare Token）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个专业化智能体四团队协作，6 个分析师并行执行
- 看涨/看跌投资辩论与激进/保守/中性三方风险辩论机制，轮次可前端实时配置
- 前端可动态启用/禁用智能体并按 Markdown/PDF/DOCX 导出历史报告
- 支持美股/A股/港股自然语言查询与 MCP 外部数据源接入

## 适用场景

- 我输入一句股票名就能得到多角度分析报告和投资建议
- 通过前端选择智能体组合做快速或深度股票分析
- 管理历史分析会话并导出报告

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L7: **TradingAgents-MCPmode** 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过15个专业化智能体的协作，提
> L22: - **📈 实时决策**: 基于最新数据的交易建议

## 星数曲线

```mermaid
xychart-beta
    title "guangxiangdebizi/TradingAgents-MCPmode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 337 --> 340
    line [338, 339, 339]
```

2026-10-18 338 → 2026-10-27 339（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `97030eea5796` · [字段定义](../../DATASET.md)*
