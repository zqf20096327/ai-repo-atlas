# cy-Yin/TradingAgents-CN-lite

⭐ 23 · Python · Apache-2.0 · 推送 2026-05-31 · [GitHub](https://github.com/cy-Yin/TradingAgents-CN-lite) · 个人维护 · 中文 README

**多智能体股票分析框架：输入代码与日期，输出买卖建议与报告**

TauricResearch/TradingAgents 的轻量 fork，保留 CLI 架构并新增 A 股数据（BaoStock 行情与技术指标、AkShare 财务与新闻、东方财富股吧散户情绪、央视财经宏观新闻），同时支持港股与美股/全球市场（yfinance / Alpha Vantage），按 ticker 格式自动识别市场。流程为：四个专家智能体并行分析（基本面/情绪/新闻/技术），多头与空头研究员多轮辩论，研究经理与交易员决策，三位风险分析师辩论后由组合经理给出 BUY/SELL/HOLD，并生成 Markdown+HTML 中英文报告。无 Web UI、数据库与 Docker，需配置 LLM API Key。README 声明仅供研究与教育用途，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体流水线：分析→多空辩论→风险评审→最终 BUY/SELL/HOLD 决策
- A 股行情/财务/新闻/散户情绪多数据源接入（BaoStock/AkShare/东方财富股吧/央视财经）
- 支持 A 股、港股、美股/全球市场，按 ticker 格式自动识别
- 生成中英文 Markdown+HTML 结构化报告

## 适用场景

- 输入股票代码与日期，获得多智能体辩论式的交易分析报告
- 研究 A 股基本面对接国内数据源的多智能体分析架构
- 本地或云端 LLM 驱动的投资研究辅助学习

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L22: You give it a **stock ticker** and a **date**. It runs a team of AI agents that analyze the stock from every angle 
> L90: 👑 **Portfolio Manager** makes the final **BUY / SELL / HOLD** decision.
> L9: A lightweight fork of TauricResearch/TradingAgents, adding **A-share market data** (BaoStock + AkShare + EastMoney G

## 星数曲线

```mermaid
xychart-beta
    title "cy-Yin/TradingAgents-CN-lite 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-28 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `93ce604e7dae` · [字段定义](../../DATASET.md)*
