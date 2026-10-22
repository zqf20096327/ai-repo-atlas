# sorry510/go_binance_futures

⭐ 252 · Go · MIT · 推送 2026-10-18 · [GitHub](https://github.com/sorry510/go_binance_futures) · 个人维护 · 中文 README

**面向个人用户的币安合约量化交易机器人，内置 AI 分析与受控交易**

Go 编写的币安 U 本位合约交易程序，提供 Web UI 管理按币种配置的自定义技术指标策略、模拟交易测试、历史 1m 行情回测、实时模拟下单与止盈止损，并支持钉钉/Slack/WebSocket 推送。AI 部分包括：单币分析 Skill 输出结构化 TradingPlan、机会发现自动监控、多轮对话、Skill/MCP/Memory 管理，以及不经 LLM 直接下单的受控交易链路（Risk Engine→人工批准→执行→审计）。数据库建议 MySQL（Schema v19），启动前需执行 sync db 子命令。README 声明 Lead 带单实盘执行仍锁定、真实环境 Gate 未完成，且不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 单币分析输出结构化 TradingPlan，机会自动监控去重后衔接受控交易
- 受控交易链路：Proposal→确定性 Risk Engine→人工批准→执行前复检→审计，LLM 不决定下单数量
- 历史 1m 行情回测与实时模拟交易测试
- Skill/MCP Client/Memory 管理与 Token/Tool 调用预算治理

## 适用场景

- 为自己跑一套币安合约策略并做历史回测验证
- 用 AI 分析辅助判断行情，经人工批准后受控提交订单
- 配置到价提醒、市场监听与钉钉/Slack 通知

## 场景标签

 · 领域:加密货币量化交易

## 证据(README 行号)

> L322: ## 合约交易
> L271: 受控交易不是“让 LLM 直接下单”。真实执行固定经过：
> L62: UI 可在 `合约交易 → 策略模板` 中维护技术指标和策略方法，再到 `合约交易 → 合约交易` 为币种应用模板或直接维护策略配置。合约币种固定使用自定义策略，不再提供 `global / line_x / custom` 策略

## 星数曲线

```mermaid
xychart-beta
    title "sorry510/go_binance_futures 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 250 --> 253
    line [252, 251, 251]
```

2026-10-18 252 → 2026-10-22 251（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f26248a1a60f` · [字段定义](../../DATASET.md)*
