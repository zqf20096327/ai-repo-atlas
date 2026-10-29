# kevmyung/swing-trading-agent

⭐ 24 · Python · Apache-2.0 · 推送 2026-05-15 · [GitHub](https://github.com/kevmyung/swing-trading-agent) · 个人维护

**多智能体波段交易系统：自动选股、研究与下单**

自动化波段交易代理，每日运行 EOD 信号、早盘、盘中三个交易周期，由量化引擎（RSI/MACD/ATR 等指标筛选标普 500 并识别市场状态）、研究代理（读取新闻与财报评估情绪与风险）和组合管理代理（决策、仓位、止损）协作完成，决策由 Amazon Bedrock 基础模型经 Strands Agents SDK 驱动。支持历史回测、经 Alpaca 的模拟盘与实盘交易，通过 AWS CDK 部署，前端为 React 面板加 FastAPI 服务。需 AWS 账号、Alpaca API key，可选 Polygon.io 用于含新闻的回测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三周期交易循环：EOD 信号→早盘确认下单→盘中持仓管理
- 量化指标确定性预计算，LLM 不参与数学计算
- 回测/模拟盘/实盘三种运行模式，含与 SPY 对比的回测分析
- 可编辑的交易 playbook（入场/出场规则与风险阈值）

## 适用场景

- 我想让代理自动执行波段选股、下单与止损管理
- 在投入真金前用历史数据回测自定义交易规则
- 通过 Alpaca 模拟盘验证策略在实时市场中的表现

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L11: The agent runs three trading cycles per day, each designed for a specific decision point in the market. Each cycle 
> L3: An autonomous trading agent that manages a portfolio across multiple daily cycles — screening candidates, reading ne

## 星数曲线

```mermaid
xychart-beta
    title "kevmyung/swing-trading-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `63272f6a8b66` · [字段定义](../../DATASET.md)*
