# randomness11/probablyprofit

⭐ 40 · Python · MIT · 推送 2026-01-27 · [GitHub](https://github.com/randomness11/probablyprofit) · 个人维护

**用自然语言策略构建 Polymarket 自动交易机器人的 Python 框架**

面向 Polymarket 预测市场的 AI 交易机器人构建框架：用户以英文描述交易策略，由 Claude、GPT-4、Gemini 等模型（支持 ensemble 共识模式）处理市场分析、仓位计算与下单执行。集成 Polymarket CLOB API，提供 Kelly 公式仓位管理、止损、最大回撤保护、紧急停止开关、纸面交易与回测，以及 Telegram 告警和 Web 仪表盘。以 pip 包提供，也可 Docker 部署。README 声明为实验性教育软件，实盘交易需显式确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言定义交易策略，无需编码
- 多模型提供方支持（Claude/GPT-4/Gemini）与 ensemble 共识模式
- 风险管理：Kelly 公式、止损、最大回撤保护、紧急停止开关
- 纸面交易、回测与 Web 仪表盘监控

## 适用场景

- 用英文描述策略即可在 Polymarket 上运行交易机器人
- 先用模拟资金测试策略再切实盘
- 实时监控持仓与盈亏并接收 Telegram 告警

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L12: **Build autonomous trading bots for Polymarket using natural language strategies.**
> L22: ProbablyProfit is a framework for building AI-powered trading bots that operate on prediction markets. Define your 
> L38: |**Multi-Provider AI**|Support for Claude, GPT-4, and Gemini with ensemble consensus mode|

## 星数曲线

```mermaid
xychart-beta
    title "randomness11/probablyprofit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d85bf4a11dca` · [字段定义](../../DATASET.md)*
