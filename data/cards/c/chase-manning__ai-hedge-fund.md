# chase-manning/ai-hedge-fund

⭐ 97 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/chase-manning/ai-hedge-fund) · 个人维护

**每4小时由Claude提案、确定性代码执行的多资产AI交易基金**

一个固定工作流的多资产交易基金：调度器每4小时对11个市场（美股指数、大盘股、黄金、原油、美元/日元、比特币、以太坊）取快照，调用Claude生成目标权重、24小时概率、止损与做空论点，再经确定性风险门控（仓位、总/净敞口、回撤、停损限制）后由代码执行下单，模型本身不下单。全程输入、推理摘要、订单与成本均记日志并发布到公开仪表盘。支持paper/testnet/live三档模式，默认离线假模型路径无需API key，主网交易需显式开启FUND_ALLOW_MAINNET。作者声明这是实验而非投资建议，无回测，仅有前向实盘记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Claude提议目标权重与论点、确定性风险门控与代码下单的分工机制
- 全部决策、订单、成本记日志并发布到公开dashboard（前向-only评估，无回测）
- 离线FakeClaude路径无需API key即可paper运行（基于20日均线固定规则）
- 多层安全：专用钱包、不可提现agent key、净值上限、回撤自动平仓、主网默认关闭

## 适用场景

- 研究LLM在真实多资产交易中的前向表现（含成本与Brier评分）
- 观察'模型提案+代码执行+风险门控'的自动交易架构实现
- 在paper或testnet模式下复现完整交易周期与评分流程

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L15: - Asks Claude for a target weight, a 24 hour probability, a stop and a short thesis for every market.
> L16: - Passes that proposal through a deterministic risk gate. The model never sends an order.
> L35:     D --> C[Claude<br/>targets, forecasts, theses]

## 星数曲线

```mermaid
xychart-beta
    title "chase-manning/ai-hedge-fund 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-23 97 → 2026-10-30 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5526f4d8a4ff` · [字段定义](../../DATASET.md)*
