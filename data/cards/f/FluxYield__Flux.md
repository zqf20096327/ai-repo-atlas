# FluxYield/Flux

⭐ 22 · TypeScript · 推送 2026-06-22 · [GitHub](https://github.com/FluxYield/Flux) · 组织维护

**Solana DeFi 收益自动优化器：轮询借贷协议并用 Claude 决策再平衡**

TypeScript 编写的 Solana 收益优化机器人，每小时轮询 Kamino、MarginFi、Solend（Drift 可选）的利率，构建利率矩阵，调用 Claude（Anthropic API）推理最优资产配置，并在扣除 gas 成本后仅在预期改善超过阈值时执行再平衡。内建风险调整 APY 公式、协议集中度上限（50%）、利用率守卫（>90% 过滤）、利用率激增检测与复利计息。默认运行于 paper 模式，切换环境变量即可投入真实资金；通过 git clone 与 Bun 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每小时轮询 Kamino/MarginFi/Solend 利率并调用 Claude 推理最优配置
- 风险调整 APY 与 gas 经济性门控（收益须覆盖交易成本才再平衡）
- 默认 paper 模式，环境变量切换实盘
- 优化规则：5% 最低 APY、2% 再平衡阈值、50% 协议集中度上限、90% 利用率守卫

## 适用场景

- 把资金在 Solana 借贷协议间自动再平衡以获取更高收益
- 先用 paper 模式验证优化策略再上实盘
- 监控协议利用率与流动性风险以规避提款冻结

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L4: Polls Kamino, MarginFi, and Solend every hour. Reasons with Claude. Rebalances when it's worth it.
> L13: `Flux` fetches live rates across every major Solana lending protocol, builds a rate matrix, and asks Claude to reas

## 星数曲线

```mermaid
xychart-beta
    title "FluxYield/Flux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `953733b7770f` · [字段定义](../../DATASET.md)*
