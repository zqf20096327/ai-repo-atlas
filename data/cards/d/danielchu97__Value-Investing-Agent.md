# danielchu97/Value-Investing-Agent

⭐ 24 · TypeScript · MIT · 推送 2026-01-29 · [GitHub](https://github.com/danielchu97/Value-Investing-Agent) · 个人维护 · 中文 README

**面向价值投资者的 MCP 服务器：格雷厄姆/巴菲特式股票分析**

以 MCP server 形式提供的价值投资分析工具：向 Claude Desktop 等 MCP 客户端暴露 10 个工具，涵盖实时行情、财报获取、DCF 与 Graham Number 内在价值计算（含安全边际）、护城河分析、新闻聚合、自选股管理与报告生成。数据源采用可插拔架构，内置 Yahoo Finance（默认免 key）、Finnhub、Alpha Vantage，可通过模板实现自定义 provider。声明仅供教育研究、不构成投资建议；要求 Node.js ≥ 18 与任意 MCP 兼容客户端。

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

- 10 个 MCP 工具：行情/财报/DCF 与 Graham 估值/护城河分析/报告生成
- 可插拔数据源：yahoo-finance（默认免 key）、finnhub、alpha-vantage，支持自定义 provider
- 自选股管理与每日摘要/深度分析报告生成
- 估值/盈利/安全三大类价值投资关键指标判定

## 适用场景

- 通过 Claude 等客户端对话式查询行情与财报
- 计算股票内在价值并按安全边际评估买点
- 维护自选股并生成每日摘要和深度分析报告

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: An AI-powered MCP server for value investors. Analyze stocks using principles from Benjamin Graham and Warren Buffet
> L32: - Any MCP-compatible client (Claude Desktop, Claude Code, or your own application)

## 星数曲线

```mermaid
xychart-beta
    title "danielchu97/Value-Investing-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bfb28691c006` · [字段定义](../../DATASET.md)*
