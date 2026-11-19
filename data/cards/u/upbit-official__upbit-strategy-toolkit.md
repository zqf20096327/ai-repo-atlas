# upbit-official/upbit-strategy-toolkit

⭐ 10 · Python · NOASSERTION · 推送 2026-07-13 · [GitHub](https://github.com/upbit-official/upbit-strategy-toolkit) · [官网](https://github.com/upbit-official/upbit-strategy-toolkit) · 组织维护

**通过 AI agent 对话构建与回测 Upbit 交易策略的工具包**

Upbit 官方发布的 Python 工具包（Beta），用于设计和回测基于指标的数字资产交易策略：用户用自然语言与 Claude Code/Codex/Cursor 等 agent 对话，由 agent 将策略假设结构化为 JSON（入场/出场/止损/止盈），再用内置回测引擎基于 Upbit 历史行情生成 CSV 结果与绩效摘要。仅支持回测，不需要实盘权限或账户信息；仅支持 Upbit KR 交易所。也可脱离 agent 直接使用 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言策略→JSON 结构化（/create-strategy）→回测（/backtest）→修订的完整流程
- 直接 CLI 用法：strategy validate / backtest run / cache 管理
- 回测输出 CSV 报告与含 Sharpe、胜率、Profit Factor 的绩效摘要
- 明确声明不构成投资建议，不支持实盘交易

## 适用场景

- 用自然语言描述策略假设并快速回测验证
- 对同一策略调整参数后比较回测结果
- 无需实盘权限地检验 KRW-BTC/USDT 市场的历史策略表现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L9: Upbit Strategy Toolkit enables users to build and validate indicator-based trading strategies through natural-langua
> L11: Quickly validate your own trading hypotheses by working with AI agents such as Claude Code or Cursor using simple p

## 星数曲线

```mermaid
xychart-beta
    title "upbit-official/upbit-strategy-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-19"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-19 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `017731cc8822` · [字段定义](../../DATASET.md)*
