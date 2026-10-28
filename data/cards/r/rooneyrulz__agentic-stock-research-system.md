# rooneyrulz/agentic-stock-research-system

⭐ 120 · Python · 推送 2026-09-15 · [GitHub](https://github.com/rooneyrulz/agentic-stock-research-system) · 个人维护

**面向印度 NSE 股票的多 Agent AI 研究与买卖推荐系统**

基于 LangGraph/多 Agent 架构的 NSE 股票分析系统：Stock Finder Agent 筛选股票，Market Data Agent 采集实时行情与技术指标（RSI/MACD/均线），News Analyst Agent 做新闻情感分类，Recommendation Agent 综合 produce BUY/SELL/HOLD 建议与目标价、止损位和置信度评分。通过 Bright Data MCP 采集数据，使用 OpenAI API，前端为 Streamlit。声明仅用于教育与研究目的。

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

- 四个分工 Agent（选股/行情/新闻/推荐）协作产出买卖建议
- 技术指标（RSI、MACD、均线）与新闻情感分析
- 给出入场/离场价、止损位与置信度评分
- Streamlit 交互界面与 CSV 导出

## 适用场景

- 我想快速获得 NSE 股票的短线/中线分析参考
- 我需要带止损与风险收益比的投资建议报告
- 我想跟踪推荐准确率并与实际走势对比

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L12: - **Stock Finder Agent**: Identifies promising NSE stocks based on liquidity, market cap, and momentum
> L15: - **Recommendation Agent**: Provides actionable BUY/SELL/HOLD recommendations with target prices
> L142: - Synthesizes all data into actionable recommendations

## 星数曲线

```mermaid
xychart-beta
    title "rooneyrulz/agentic-stock-research-system 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 119 --> 122
    line [121, 120, 120]
```

2026-10-18 121 → 2026-10-28 120（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `39080e90f4c6` · [字段定义](../../DATASET.md)*
