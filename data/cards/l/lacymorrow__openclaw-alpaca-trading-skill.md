# lacymorrow/openclaw-alpaca-trading-skill

⭐ 13 · 推送 2026-02-24 · [GitHub](https://github.com/lacymorrow/openclaw-alpaca-trading-skill) · [官网](https://clawhub.ai/lacymorrow/alpaca-trading) · 个人维护

**OpenClaw 技能：通过 apcacli CLI 用 Alpaca API 交易股票与加密资产**

面向 ClawHub/OpenClaw 的技能包，封装 Rust 编写的命令行工具 apcacli，通过 Alpaca Trading API 执行股票、ETF、期权与加密资产交易。功能覆盖市价/限价/止损/追踪止损订单、持仓与账户管理、实时行情与账户事件流。面向开发者与算法交易者，需 Rust 1.71+ 工具链以 cargo 安装 apcacli，并配置 Alpaca API 密钥；提供 paper trading 模式（$100,000 虚拟资金）供无风险测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 市价/限价/止损/追踪止损订单的提交与撤销
- 股票、ETF、期权、加密资产的买卖与持仓管理
- 账户事件与成交的实时流式监控
- paper trading 模式与多账户会话管理

## 适用场景

- 用终端命令执行和管理 Alpaca 账户的交易
- 编写 shell 脚本自动化交易策略
- 让 OpenClaw agent 通过此技能操作交易与查看持仓
- 先用 paper trading 模拟账户测试命令

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L289: **Skill Type:** CLI Tool Integration
> L291: **Created for:** ClawHub / OpenClaw

## 星数曲线

```mermaid
xychart-beta
    title "lacymorrow/openclaw-alpaca-trading-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7c406dbe5eee` · [字段定义](../../DATASET.md)*
