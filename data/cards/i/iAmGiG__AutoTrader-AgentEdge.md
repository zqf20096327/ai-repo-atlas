# iAmGiG/AutoTrader-AgentEdge

⭐ 23 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/iAmGiG/AutoTrader-AgentEdge) · [官网](https://github.com/iAmGiG/AutoTrader-AgentEdge/wiki) · 个人维护

**基于 AutoGen 多智能体的美股交易系统，人机协同的纸面交易与研究验证**

OptionsCommander（原 RH2MAS）是构建于 Microsoft AutoGen 之上的多智能体交易平台，通过 Alpaca Markets 以人工监督方式交易 MACD+RSI 投票策略，GPT-4o-mini 用于自然语言意图分类。研究部分采用 walk-forward 验证、含交易成本与防前视偏差的回测；README 报告当前实盘规则无超额收益（Sharpe 0.69，alpha t=0.19），GEX 叠加研究已关闭。提供交互式 CLI、每日定时例程（cron/daemon）与 SQLite 数据缓存；ScannerAgent、RiskAgent、ExecutorAgent 仍在开发中。AGPL-3.0 许可，声明仅供教育与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AutoGen 多智能体架构，GPT-4o-mini 做自然语言交易指令意图分类
- walk-forward 验证、含交易成本与防前视偏差的回测方法论
- Alpaca 纸面交易集成，早晚定时例程做对账、止损管理与报告
- 交互式 CLI 覆盖下单、持仓、工作流与配置命令

## 适用场景

- 在 Alpaca 纸面账户上运行多智能体交易流程并人工复核
- 对 MACD+RSI、TSMOM、GEX 等策略做样本外稳健性研究
- 用自然语言向 CLI 下达交易与查询指令

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L26: **OptionsCommander** is a research-driven trading platform with a multi-agent AI architecture built on Microsoft Au
> L84: - **Natural Language Commands**: GPT-4o-mini parses trade requests

## 星数曲线

```mermaid
xychart-beta
    title "iAmGiG/AutoTrader-AgentEdge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9542ae9feba9` · [字段定义](../../DATASET.md)*
